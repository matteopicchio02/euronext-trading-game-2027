#!/usr/bin/env python3
"""Independent 23-holding quote monitor for a virtual student research portfolio.

This monitor uses public Yahoo daily prices (not NextWise) and a manual ledger of
share quantities. It works while the old snapshot-relative NAV monitor remains
paused. All calculations are read-only; no order can be placed or inferred.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from scripts.daily_portfolio_monitor import (
    FX_TICKER,
    ROOT,
    TRADING_DAYS,
    download_yahoo,
)

ROME = ZoneInfo("Europe/Rome")
SUPPORTED_EUR_SUFFIXES = (".PA", ".AS", ".MI", ".LS", ".BR")


def read_watch_inputs(config_path: Path) -> tuple[dict, pd.DataFrame]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if config.get("read_only") is not True or config.get("enabled") is not True:
        raise ValueError("Read-only market watch must be explicitly enabled")
    if config.get("manual_account_events_after_anchor") is not False:
        raise ValueError("Unreconciled account event: update holdings and cash first")
    needed = [
        "portfolio_file", "position_quantity_column", "price_anchor_date",
        "position_as_of", "cash_eur_assumed_unchanged", "official_nav_anchor_eur",
    ]
    missing = [k for k in needed if k not in config]
    if missing:
        raise ValueError(f"Market watch config missing: {missing}")
    p = pd.read_csv(ROOT / config["portfolio_file"])
    qty_field = config["position_quantity_column"]
    columns = {"ticker", "name", "sector", qty_field}
    if p.empty or not columns.issubset(p.columns):
        raise ValueError("Empty or incomplete quantity ledger")
    if p.ticker.duplicated().any():
        raise ValueError("Duplicate holding ticker")
    if p[list(columns)].isnull().any().any():
        raise ValueError("Missing ticker/sector/name/quantity")
    p["quantity"] = pd.to_numeric(p[qty_field], errors="raise")
    if (p.quantity <= 0).any() or not np.isfinite(p.quantity).all():
        raise ValueError("Missing or non-positive share quantity")
    if not all(float(x).is_integer() for x in p.quantity):
        raise ValueError("Unexpected fractional shares; verify account ledger")
    p["currency"] = np.where(p.ticker.str.endswith(".OL"), "NOK", "EUR")
    suffixes = p.ticker.str.endswith(SUPPORTED_EUR_SUFFIXES) | p.ticker.eq("EQNR.OL")
    if not suffixes.all():
        raise ValueError("Unreviewed listing or quotation currency")
    if len(p) != 23 or not {"DSY.PA", "AD.AS", "UNA.AS", "EQNR.OL"}.issubset(set(p.ticker)):
        raise ValueError("Expected reconciled 23-name portfolio; check executed trades")
    if dict(zip(p.ticker, p.quantity)).get("DSY.PA") != 60:
        raise ValueError("DSY post-sale quantity must be verified before monitoring")
    if dict(zip(p.ticker, p.quantity)).get("AD.AS") != 25:
        raise ValueError("Ahold post-buy quantity must be verified before monitoring")
    if dict(zip(p.ticker, p.quantity)).get("UNA.AS") != 20:
        raise ValueError("Unilever post-buy quantity must be verified before monitoring")
    if pd.Timestamp(config["position_as_of"]).date() != pd.Timestamp(config["price_anchor_date"]).date():
        raise ValueError("Quantity snapshot and Yahoo close anchor dates differ")
    if pd.Timestamp(config["price_anchor_date"]).date() > datetime.now(ROME).date():
        raise ValueError("Market watch anchor cannot be in the future")
    cash = float(config["cash_eur_assumed_unchanged"])
    nav = float(config["official_nav_anchor_eur"])
    if not np.isfinite([cash, nav]).all() or cash < 0 or nav <= cash:
        raise ValueError("Invalid cash or screenshot anchor NAV")
    return config, p


def _eur_quote(price: float, ticker: str, nok_per_eur: float) -> float:
    if ticker == "EQNR.OL":
        return price / nok_per_eur
    return price


def analyze_quotes(
    config: dict,
    holdings: pd.DataFrame,
    raw: pd.DataFrame,
    adjusted: pd.DataFrame,
    asof: datetime,
    *,
    require_today: bool = True,
) -> tuple[dict, pd.DataFrame]:
    """Calculate from externally sourced prices. No network access, easily tested."""
    tickers = holdings.ticker.tolist()
    if len(set(tickers)) != len(tickers):
        raise ValueError("Repeated active holding")
    symbols = tickers + [FX_TICKER]
    for name, frame in (("raw", raw), ("adjusted", adjusted)):
        if not set(symbols).issubset(frame.columns):
            raise ValueError(f"Missing {name} quote ticker or EUR/NOK rate")
        if frame.index.has_duplicates or not frame.index.is_monotonic_increasing:
            raise ValueError(f"Malformed {name} trading-day index")
    if not raw.index.equals(adjusted.index):
        raise ValueError("Yahoo raw and adjusted date indices disagree")
    common = raw[symbols].dropna(how="any")
    adj_common = adjusted[symbols].dropna(how="any")
    if len(common) < 181 or len(adj_common) < 181:
        raise ValueError("Insufficient complete multi-market history")
    last = common.index[-1]
    if adj_common.index[-1] != last:
        raise ValueError("Raw and adjusted latest common sessions disagree")
    if require_today and last.date() != asof.astimezone(ROME).date():
        raise ValueError(f"Stale price panel: {last.date()} rather than today's session")
    if any(raw[t].dropna().index[-1] != last for t in symbols):
        raise ValueError("At least one ticker has stale/mismatched latest close")
    anchor = pd.Timestamp(config["price_anchor_date"])
    if anchor not in common.index or last < anchor:
        raise ValueError("Missing dated 20 November market-close anchor")
    if len(common.loc[:last]) < 2:
        raise ValueError("Need previous close for one-day moves")
    previous = common.index[-2]
    prices = common.loc[last]
    base = common.loc[anchor]
    yesterday = common.loc[previous]
    if not np.isfinite(common.loc[[anchor, previous, last], symbols]).all().all():
        raise ValueError("Non-finite price or FX series")
    if (common.loc[[anchor, previous, last], symbols] <= 0).any().any():
        raise ValueError("Non-positive price or FX series")
    eur_quotes = []
    eur_yesterday = []
    eur_base = []
    for ticker in tickers:
        eur_quotes.append(_eur_quote(float(prices[ticker]), ticker, float(prices[FX_TICKER])))
        eur_yesterday.append(_eur_quote(float(yesterday[ticker]), ticker, float(yesterday[FX_TICKER])))
        eur_base.append(_eur_quote(float(base[ticker]), ticker, float(base[FX_TICKER])))

    marks = holdings[["ticker", "name", "sector", "quantity", "currency"]].copy()
    marks["close_local"] = [float(prices[t]) for t in tickers]
    marks["close_eur"] = eur_quotes
    marks["value_eur_yahoo"] = marks.quantity * np.asarray(eur_quotes)
    marks["anchor_close_eur"] = eur_base
    marks["delta_since_anchor_eur"] = marks.quantity * (
        np.asarray(eur_quotes) - np.asarray(eur_base)
    )
    marks["delta_one_session_eur"] = marks.quantity * (
        np.asarray(eur_quotes) - np.asarray(eur_yesterday)
    )
    marks["daily_return_pct"] = (
        np.asarray(eur_quotes) / np.asarray(eur_yesterday) - 1
    ) * 100
    if (marks.daily_return_pct.abs() > 40).any():
        raise ValueError("Suspicious daily move >40%; review split/vendor prices")
    if not np.isfinite(marks.select_dtypes(include="number")).all().all():
        raise ValueError("Non-finite derived position value")

    cash = float(config["cash_eur_assumed_unchanged"])
    anchor_nav = float(config["official_nav_anchor_eur"])
    quote_equity = float(marks.value_eur_yahoo.sum())
    direct_nav = quote_equity + cash
    anchor_direct_equity = float((marks.quantity * np.asarray(eur_base)).sum())
    baseline_gap = (anchor_direct_equity + cash) - anchor_nav
    # A mismatch is EXPECTED between external Yahoo quotes and virtual NextWise.
    # Large discrepancies make the anchor-based NAV unreliable.
    if abs(baseline_gap) > 0.12 * anchor_nav:
        raise ValueError("Yahoo/NextWise anchor gap >12%: manual vendor/FX review")
    change_anchor = float(marks.delta_since_anchor_eur.sum())
    estimate = anchor_nav + change_anchor
    if estimate <= 0 or direct_nav <= 0:
        raise ValueError("Invalid implied NAV")

    adjusted_eur = adj_common[tickers].copy()
    adjusted_eur["EQNR.OL"] = adjusted_eur["EQNR.OL"] / adj_common[FX_TICKER]
    if (adjusted_eur <= 0).any().any():
        raise ValueError("Invalid adjusted-price history")
    returns = adjusted_eur.pct_change(fill_method=None).dropna(how="any").tail(TRADING_DAYS)
    if len(returns) < 180:
        raise ValueError("Insufficient common adjusted-return observations")
    if (returns.abs() > 0.45).any().any():
        raise ValueError("Suspicious historical corporate-action adjustment")
    cov = returns.cov().to_numpy() * TRADING_DAYS

    # Risk weights come from the internally consistent Yahoo cross-section,
    # not from pretending the NextWise NAV is a ticker-by-ticker Yahoo statement.
    w = marks.value_eur_yahoo.to_numpy() / direct_nav
    risk_variance = float(w @ cov @ w)
    if not np.isfinite(risk_variance) or risk_variance <= 0:
        raise ValueError("Invalid portfolio variance")
    vol = float(np.sqrt(risk_variance))
    eq_w = marks.value_eur_yahoo.to_numpy() / quote_equity
    marks["yahoo_weight_nav_pct"] = w * 100
    marks["risk_contribution_pct"] = (w * (cov @ w) / risk_variance) * 100
    marks["source"] = "Yahoo Finance daily Close (not NextWise)"
    summary = {
        "status": "MARKET_DATA_ESTIMATE_NOT_NEXTWISE",
        "quote_date": last.date().isoformat(),
        "previous_quote_date": previous.date().isoformat(),
        "generated_at_rome": asof.astimezone(ROME).isoformat(timespec="seconds"),
        "positions_as_of": config["position_as_of"],
        "holdings_count": len(tickers),
        "share_quantities_frozen_after_user_report": True,
        "last_observed_nextwise_nav_eur": anchor_nav,
        "last_observed_nextwise_date": config["price_anchor_date"],
        "last_observed_nextwise_cash_eur": cash,
        "assumed_cash_eur": cash,
        "yahoo_direct_equity_eur": quote_equity,
        "yahoo_direct_nav_eur": direct_nav,
        "yahoo_to_nextwise_anchor_gap_eur": baseline_gap,
        "indicative_nav_from_dated_nextwise_anchor_eur": estimate,
        "indicative_change_since_anchor_eur": change_anchor,
        "indicative_change_previous_common_session_eur": float(marks.delta_one_session_eur.sum()),
        "annualized_volatility_pct_model": vol * 100,
        "gaussian_var_1d_95_eur_model": 1.64485362695 * vol / np.sqrt(TRADING_DAYS) * direct_nav,
        "hhi_equity_normalized_model": float(np.sum(eq_w ** 2)),
        "diversification_ratio_model": float((w @ np.sqrt(np.diag(cov))) / vol),
        "cash_weight_pct_model": float(cash / direct_nav * 100),
        "equity_weight_pct_model": float(quote_equity / direct_nav * 100),
        "paris_listing_pct_nav_model": float(np.sum(w[marks.ticker.str.endswith(".PA")]) * 100),
        "fx_nok_per_eur": float(prices[FX_TICKER]),
        "risk_history_sessions": len(returns),
        "data_provider": "Yahoo Finance via yfinance; adjusted close for historical risk",
        "valuation_caveat": "External, delayed quotes; cash/quantities assumed unchanged since Nov 20. Not official NAV, broker P&L or an executable quote. FX/dividends/fees may differ.",
    }
    return summary, marks


def save_watch_report(summary: dict, positions: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    date = summary["quote_date"]
    best = positions.sort_values("delta_one_session_eur", ascending=False).head(5)
    worst = positions.sort_values("delta_one_session_eur", ascending=True).head(5)
    lines = [
        f"# Project Alpha — market price study ({date})",
        "",
        "> **Student research estimate — NOT NextWise.** Public Yahoo daily prices,",
        f"> {summary['holdings_count']} quantities frozen as of {summary['positions_as_of']};",
        "> cash held constant. Not a brokerage account feed or automated order system.",
        "",
        "## Indicative portfolio measures",
        "",
        f"- Latest official **dated** NextWise NAV anchor: EUR {summary['last_observed_nextwise_nav_eur']:,.2f}.",
        f"- **Indicative** NAV based on price differences since anchor: EUR {summary['indicative_nav_from_dated_nextwise_anchor_eur']:,.2f}.",
        f"- Indicative price effect since the anchor: EUR {summary['indicative_change_since_anchor_eur']:+,.2f}.",
        f"- Price effect over the latest common trading session: EUR {summary['indicative_change_previous_common_session_eur']:+,.2f}.",
        f"- Frozen assumed cash: EUR {summary['assumed_cash_eur']:,.2f}.",
        f"- Yahoo direct NAV cross-check: EUR {summary['yahoo_direct_nav_eur']:,.2f}.",
        f"- Baseline Yahoo-versus-NextWise difference: EUR {summary['yahoo_to_nextwise_anchor_gap_eur']:+,.2f}.",
        "",
        "## Historical risk analysis — model outputs only",
        "",
        f"- Annualized volatility: {summary['annualized_volatility_pct_model']:.2f}%.",
        f"- Parametric 1-day 95% VaR: EUR {summary['gaussian_var_1d_95_eur_model']:,.2f}.",
        f"- HHI (normalized equity weights): {summary['hhi_equity_normalized_model']:.5f}.",
        f"- Diversification ratio: {summary['diversification_ratio_model']:.3f}.",
        f"- Equity / cash on Yahoo mark basis: {summary['equity_weight_pct_model']:.2f}% / {summary['cash_weight_pct_model']:.2f}%.",
        f"- Paris listed share of model NAV: {summary['paris_listing_pct_nav_model']:.2f}% (internal monitor only).",
        f"- EUR/NOK: {summary['fx_nok_per_eur']:.4f} NOK per EUR.",
        "",
        "## Biggest one-session contributions — not trades",
        "",
        "| Largest positive | Indicative EUR |",
        "|---|---:|",
    ]
    for _, row in best.iterrows():
        lines.append(f"| {row.ticker} | {row.delta_one_session_eur:+.2f} |")
    lines += ["", "| Largest negative | Indicative EUR |", "|---|---:|"]
    for _, row in worst.iterrows():
        lines.append(f"| {row.ticker} | {row.delta_one_session_eur:+.2f} |")
    lines += [
        "", "## All holdings — external Yahoo marks", "",
        "| Ticker | Qty | Currency | Yahoo mark EUR | Day change EUR | Weight % |",
        "|---|---:|---|---:|---:|---:|",
    ]
    for _, row in positions.iterrows():
        lines.append(
            f"| {row.ticker} | {int(row.quantity)} | {row.currency} | "
            f"{row.value_eur_yahoo:,.2f} | {row.delta_one_session_eur:+,.2f} | "
            f"{row.yahoo_weight_nav_pct:.2f} |"
        )
    lines += [
        "", "## Limitations and next research tasks", "",
        "- Quotes may be delayed or revised. The reported date is a market session, not a live NextWise value.",
        "- This model cannot detect new NextWise purchases, sales, dividends or changes in available cash.",
        "- The anchored estimate does not create official position-level acquisition P&L.",
        "- NOK/EUR conversion and prices adjusted for dividends/splits can diverge from simulation accounting.",
        "- Review individual execution prices for Ahold and Unilever when available; do not invent them.",
        "- Before acting on a signal, compare the latest company disclosures and executable NextWise quote.",
        "- If actual quantities or cash change, update the dated ledger and monitor configuration first.",
        "- This code does **not** place, cancel, or modify virtual orders.", "",
    ]
    report = "\n".join(lines)
    (output_dir / f"{date}.md").write_text(report, encoding="utf-8")
    (output_dir / "latest.md").write_text(report, encoding="utf-8")
    positions.to_csv(output_dir / f"positions_{date}.csv", index=False, float_format="%.8f")
    positions.to_csv(output_dir / "latest_positions.csv", index=False, float_format="%.8f")
    (output_dir / "latest_summary.json").write_text(
        json.dumps(summary, indent=2, allow_nan=False, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config", type=Path, default=ROOT / "data" / "market_watch_config.json"
    )
    parser.add_argument(
        "--output-dir", type=Path, default=ROOT / "reports" / "market_watch"
    )
    parser.add_argument(
        "--allow-stale", action="store_true",
        help="Diagnostic only: label the actual previous quote date, never as live.",
    )
    args = parser.parse_args()
    config, positions = read_watch_inputs(args.config)
    raw, adjusted = download_yahoo(positions.ticker.tolist())
    result, marks = analyze_quotes(
        config, positions, raw, adjusted, datetime.now(ROME),
        require_today=not args.allow_stale,
    )
    save_watch_report(result, marks, args.output_dir)
    print(
        f"Market-price estimate as of {result['quote_date']}: "
        f"EUR {result['indicative_nav_from_dated_nextwise_anchor_eur']:,.2f}. "
        "NOT official NextWise value. No orders."
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Daily virtual portfolio estimate (no NextWise access; no order execution).

Estimates value changes since an explicitly verified NextWise snapshot, using
unadjusted daily Yahoo closes and EUR/NOK. Corporate actions, dividends, fills,
FX settlement and platform quote delays require separate reconciliation.

Daily risk uses dividend-adjusted EUR historical prices and today's estimated
NAV weights. Every active ticker and the FX series must have synchronous dates.
Fail closed on missing/stale data. No network access during tests.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ROME = ZoneInfo("Europe/Rome")
TRADING_DAYS = 252
FX_TICKER = "EURNOK=X"


def read_inputs(config_path: Path) -> tuple[dict, pd.DataFrame]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if config.get("read_only", False) is not True:
        raise ValueError("Refusing to run without read_only=true")
    required = {"snapshot_date", "portfolio_file", "cash_eur", "anchor_nav_eur"}
    if not required.issubset(config):
        raise ValueError(f"Missing config fields: {sorted(required - set(config))}")
    portfolio_path = ROOT / config["portfolio_file"]
    positions = pd.read_csv(portfolio_path)
    needed = {"ticker", "name", "sector", "quantity", "market_value_eur"}
    if not needed.issubset(positions):
        raise ValueError(f"Missing portfolio columns: {sorted(needed - set(positions))}")
    if positions.empty or positions.ticker.duplicated().any():
        raise ValueError("Empty holdings or duplicate ticker")
    if positions["quantity"].isna().any() or (positions["quantity"] <= 0).any():
        raise ValueError("Invalid quantity")
    if positions["market_value_eur"].isna().any() or (positions["market_value_eur"] <= 0).any():
        raise ValueError("Invalid market value")
    tickers = positions.ticker.tolist()
    if any(not t.endswith((".PA", ".AS", ".MI", ".LS", ".BR", ".OL")) for t in tickers):
        raise ValueError("Unknown exchange suffix; confirm the quotation currency manually")
    if any(t != "EQNR.OL" for t in tickers if t.endswith(".OL")):
        raise ValueError("New Norwegian positions need currency review before monitoring")
    if any(not isinstance(x, str) or not x for x in positions["sector"]):
        raise ValueError("Missing sector")
    snapshot_date = pd.Timestamp(config["snapshot_date"]).date()
    if snapshot_date > datetime.now(ROME).date():
        raise ValueError("Snapshot date is in the future")
    cash = float(config["cash_eur"])
    nav = float(config["anchor_nav_eur"])
    if not np.isfinite([cash, nav]).all() or cash < 0 or nav <= 0:
        raise ValueError("Invalid cash/NAV")
    if abs(float(positions["market_value_eur"].sum()) + cash - nav) > 0.05:
        raise ValueError("Snapshot market values and cash do not reconcile to NAV")
    return config, positions


def download_yahoo(tickers: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return raw Close and Adj Close (raw closes for marks, adjusted for risk)."""
    try:
        import yfinance as yf
    except ImportError as exc:
        raise RuntimeError("Install data dependencies: pip install -e '.[data]'") from exc
    symbols = tickers + ([FX_TICKER] if any(t.endswith(".OL") for t in tickers) else [])
    frame = yf.download(
        tickers=symbols, period="2y", interval="1d",
        auto_adjust=False, progress=False, threads=False,
        group_by="column", multi_level_index=True,
        ignore_tz=True, timeout=30,
    )
    if frame is None or frame.empty:
        raise ValueError("Market-data provider returned no data")
    return extract_field(frame, "Close", symbols), extract_field(frame, "Adj Close", symbols)


def extract_field(frame: pd.DataFrame, field: str, symbols: list[str]) -> pd.DataFrame:
    """Support either orientation of yfinance's multiindex columns."""
    if not isinstance(frame.columns, pd.MultiIndex):
        raise ValueError("Expected multi-ticker yfinance MultiIndex columns")
    if field in frame.columns.get_level_values(0):
        block = frame[field]
    elif field in frame.columns.get_level_values(1):
        block = frame.xs(field, level=1, axis=1)
    else:
        raise ValueError(f"yfinance did not return {field}; do not substitute raw/adjusted quotes")
    missing = sorted(set(symbols) - set(block.columns))
    if missing:
        raise ValueError(f"Provider is missing market symbols: {missing}")
    block = block.reindex(columns=symbols).apply(pd.to_numeric, errors="coerce").copy()
    dates = pd.to_datetime(block.index)
    if dates.tz is not None:
        dates = dates.tz_localize(None)
    block.index = dates.normalize()
    if block.index.has_duplicates:
        raise ValueError("Duplicate market-data dates")
    block = block.sort_index()
    return block


def build_estimate(
    config: dict,
    positions: pd.DataFrame,
    closes: pd.DataFrame,
    adjusted: pd.DataFrame,
    today: datetime,
    require_today: bool = True,
) -> tuple[dict, pd.DataFrame]:
    """Pure risk/valuation calculation, testable without internet or account access."""
    tickers = positions.ticker.tolist()
    uses_nok = any(t.endswith(".OL") for t in tickers)
    symbols = tickers + ([FX_TICKER] if uses_nok else [])
    for table, label in ((closes, "raw"), (adjusted, "adjusted")):
        if not set(symbols).issubset(table.columns):
            raise ValueError(f"{label} data missing one or more holdings/FX")
        if not table.index.is_monotonic_increasing or table.index.has_duplicates:
            raise ValueError(f"Non-monotonic or duplicate {label} dates")
    if not closes.index.equals(adjusted.index):
        raise ValueError("Adjusted and raw price dates do not match")
    raw_common = closes[symbols].dropna(how="any")
    adj_common = adjusted[symbols].dropna(how="any")
    if raw_common.empty or adj_common.empty:
        raise ValueError("No common raw/adjusted market sessions")
    current_date = raw_common.index[-1]
    if current_date != adj_common.index[-1]:
        raise ValueError("Raw and adjusted series have inconsistent final sessions")
    if require_today and current_date.date() != today.astimezone(ROME).date():
        raise ValueError(
            f"Stale or incomplete market data: latest common close {current_date.date()}, "
            f"expected {today.astimezone(ROME).date()}. No report published."
        )
    if any(closes[s].dropna().index[-1] != current_date for s in symbols):
        raise ValueError("At least one holding/FX has a newer or older close than the common date")
    anchor = pd.Timestamp(config["snapshot_date"])
    if anchor not in raw_common.index:
        raise ValueError(f"Anchor date {anchor.date()} missing in raw price panel")
    if current_date < anchor:
        raise ValueError("Market price date precedes holdings snapshot")
    last_prices = raw_common.loc[current_date]
    anchor_prices = raw_common.loc[anchor]
    if not np.isfinite(last_prices).all() or (last_prices <= 0).any():
        raise ValueError("Non-positive or missing current close")
    if not np.isfinite(anchor_prices).all() or (anchor_prices <= 0).any():
        raise ValueError("Non-positive or missing anchor close")

    fx_base = float(anchor_prices[FX_TICKER]) if uses_nok else 1.0
    fx_now = float(last_prices[FX_TICKER]) if uses_nok else 1.0
    model = positions.copy()
    model["anchor_value_eur"] = positions["market_value_eur"].astype(float)
    model["raw_close_local"] = [float(last_prices[t]) for t in tickers]
    model["anchor_close_local"] = [float(anchor_prices[t]) for t in tickers]
    model["currency"] = ["NOK" if t.endswith(".OL") else "EUR" for t in tickers]
    model["fx_nok_per_eur"] = [fx_now if t.endswith(".OL") else np.nan for t in tickers]
    model["quote_eur"] = [
        float(last_prices[t]) / (fx_now if t.endswith(".OL") else 1.0)
        for t in tickers
    ]
    model["anchor_relative_factor"] = [
        (float(last_prices[t]) / float(anchor_prices[t])) *
        ((fx_base / fx_now) if t.endswith(".OL") else 1.0)
        for t in tickers
    ]
    if (model.anchor_relative_factor <= 0).any():
        raise ValueError("Invalid adjusted-to-anchor factor")
    if (model.anchor_relative_factor > 1.8).any() or (model.anchor_relative_factor < 0.4).any():
        raise ValueError("Suspicious split/corporate-action movement vs snapshot; manual review needed")
    model["estimated_value_eur"] = model.anchor_value_eur * model.anchor_relative_factor
    # This alternative is shown only as a diagnostic: yahoo close can differ
    # from the platform's exchange and FX conventions.
    model["direct_yahoo_value_eur"] = model.quantity * model.quote_eur
    cash = float(config["cash_eur"])  # Frozen at latest verified snapshot.
    nav = float(model.estimated_value_eur.sum()) + cash
    if not np.isfinite(nav) or nav <= 0:
        raise ValueError("Invalid modeled NAV")
    model["weight_nav"] = model.estimated_value_eur / nav
    model["delta_eur_since_anchor"] = model.estimated_value_eur - model.anchor_value_eur

    # Adjusted price returns include provider corporate-action adjustments;
    # a local NOK equity must first be converted to EUR at EACH date.
    adjusted_eur = adj_common[tickers].copy()
    for t in tickers:
        if t.endswith(".OL"):
            adjusted_eur[t] = adjusted_eur[t] / adj_common[FX_TICKER]
    if (adjusted_eur <= 0).any().any():
        raise ValueError("Non-positive adjusted EUR price")
    returns = adjusted_eur.pct_change(fill_method=None).dropna(how="any").tail(TRADING_DAYS)
    if len(returns) < 180:
        raise ValueError(f"Insufficient aligned EUR history: {len(returns)} observations")
    if (returns.abs() > 0.45).any().any():
        raise ValueError("Historical adjusted return >45%; corporate action/data review required")
    cov = returns.cov().to_numpy() * TRADING_DAYS
    weights = model.weight_nav.to_numpy(dtype=float)
    port_var = float(weights @ cov @ weights)
    if port_var <= 0 or not np.isfinite(port_var):
        raise ValueError("Invalid portfolio covariance / volatility")
    vol = np.sqrt(port_var)
    asset_vol = np.sqrt(np.diag(cov))
    dr = float((weights @ asset_vol) / vol)
    equity_w = weights / weights.sum()
    hhi_eq = float(np.sum(equity_w ** 2))
    hhi_cash_included = float(np.sum(weights ** 2) + (cash/nav) ** 2)
    contrib = weights * (cov @ weights) / port_var
    model["variance_contribution_pct"] = contrib * 100.0
    model["estimated_change_pct"] = (model.anchor_relative_factor - 1) * 100
    sectors = (model.groupby("sector").estimated_value_eur.sum() / nav).sort_values(ascending=False)
    summary = {
        "quote_date": current_date.date().isoformat(),
        "generated_at_rome": today.astimezone(ROME).isoformat(timespec="seconds"),
        "holdings_snapshot_date": config["snapshot_date"],
        "source": "Yahoo Finance daily Close, adjusted historical prices and EURNOK=X FX; NOT NextWise",
        "status": "ESTIMATE_ONLY_NO_TRADE_RECONCILIATION",
        "holdings_count": len(tickers),
        "portfolio_anchor_nav_eur": float(config["anchor_nav_eur"]),
        "anchor_cash_eur_frozen": cash,
        "estimated_equities_eur": float(model.estimated_value_eur.sum()),
        "estimated_nav_eur": nav,
        "estimated_delta_vs_anchor_eur": nav - float(config["anchor_nav_eur"]),
        "cash_weight_pct": cash / nav * 100,
        "equity_weight_pct": weights.sum() * 100,
        "annualized_volatility_pct": vol * 100,
        "gaussian_1d_var_95_eur": 1.64485362695 * (vol / np.sqrt(TRADING_DAYS)) * nav,
        "diversification_ratio": dr,
        "hhi_equity_normalized": hhi_eq,
        "hhi_nav_cash_included": hhi_cash_included,
        "listed_paris_pct_nav": float(model.loc[model.ticker.str.endswith(".PA"), "weight_nav"].sum() * 100),
        "sector_weights_pct": {str(k): float(v * 100) for k, v in sectors.items()},
        "risk_history_sessions": len(returns),
        "fx_eurnok": fx_now if uses_nok else None,
    }
    return summary, model


def save_report(summary: dict, positions: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    asof = summary["quote_date"]
    top = positions.sort_values("variance_contribution_pct", ascending=False).head(5)
    lines = [
        f"# Project Alpha 2027 — Indicative portfolio monitor ({asof})", "",
        "> **NOT a NextWise statement or live NAV.** Estimate assumes holdings and cash",
        f"> **unchanged since {summary['holdings_snapshot_date']}**. No platform login, API or orders.",
        "> Yahoo historical adjusted prices/FX may differ from NextWise. Corporate actions,",
        "> dividends, fills, holiday calendars and FX conversions require manual reconciliation.",
        "",
        "## Estimated valuation (EUR)", "",
        f"- Estimated NAV: **EUR {summary['estimated_nav_eur']:,.2f}**",
        f"- Estimated equity value: EUR {summary['estimated_equities_eur']:,.2f}",
        f"- Frozen snapshot cash: EUR {summary['anchor_cash_eur_frozen']:,.2f}",
        f"- Change in estimated NAV versus dated anchor: EUR {summary['estimated_delta_vs_anchor_eur']:,.2f}",
        f"- Estimated cash weight: {summary['cash_weight_pct']:.2f}%",
        f"- Anchor NAV (official dated screenshot): EUR {summary['portfolio_anchor_nav_eur']:,.2f}",
        "",
        "## Historical risk estimates (not official contest metrics)", "",
        f"- Annualized volatility proxy: **{summary['annualized_volatility_pct']:.2f}%**",
        f"- 1-day 95% Gaussian VaR: EUR {summary['gaussian_1d_var_95_eur']:,.2f}",
        f"- Diversification ratio: {summary['diversification_ratio']:.3f}",
        f"- HHI, equity normalized: {summary['hhi_equity_normalized']:.5f}",
        f"- HHI, with cash as NAV line: {summary['hhi_nav_cash_included']:.5f}",
        f"- Listed in Paris: {summary['listed_paris_pct_nav']:.2f}% NAV (internal 35% monitor only)",
        f"- Aligned EUR return observations: {summary['risk_history_sessions']}",
        "",
        "## Major variance contributors (historical)", "",
        "| Ticker | Risk contribution (%) |",
        "|---|---:|",
    ]
    for _, row in top.iterrows():
        lines.append(f"| {row['ticker']} | {row['variance_contribution_pct']:.2f} |")
    lines += ["", "## Estimated position marks", "",
              "| Ticker | Qty (frozen) | Currency | Estimate (EUR) | NAV (%) |",
              "|---|---:|---|---:|---:|"]
    for _, row in positions.iterrows():
        lines.append(
            f"| {row['ticker']} | {row['quantity']:g} | {row['currency']} | "
            f"{row['estimated_value_eur']:,.2f} | {row['weight_nav']*100:.2f} |"
        )
    lines += [
        "", "## Reconciliation / next steps", "",
        "- Check actual quantities, fills and cash in NextWise before using this for decisions.",
        "- Investigate dividend/split adjustments and discrepancies versus platform marks.",
        "- The 35% Paris cap is a house research monitor, NOT an official tournament limit.",
        "- Data are taken at the daily market close date shown above, not real-time quotes.",
        "- No orders were placed or suggested by this automated monitor.", "",
    ]
    content = "\n".join(lines)
    for file in (f"{asof}.md", "latest.md"):
        (output_dir / file).write_text(content, encoding="utf-8")
    csv = positions[
        ["ticker", "name", "sector", "quantity", "currency", "raw_close_local",
         "anchor_value_eur", "estimated_value_eur", "direct_yahoo_value_eur",
         "weight_nav", "variance_contribution_pct", "estimated_change_pct"]
    ]
    csv.to_csv(output_dir / f"positions_{asof}.csv", index=False, float_format="%.8f")
    csv.to_csv(output_dir / "latest_positions.csv", index=False, float_format="%.8f")
    (output_dir / "latest_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(ROOT / "data/monitor_config.json"))
    parser.add_argument("--output-dir", default=str(ROOT / "reports/daily"))
    parser.add_argument(
        "--allow-stale", action="store_true",
        help="Manual diagnostic only: permit previous day's quote; report still labels quote date.",
    )
    args = parser.parse_args()
    config, positions = read_inputs(Path(args.config))
    raw, adjusted = download_yahoo(positions.ticker.tolist())
    summary, estimated = build_estimate(
        config, positions, raw, adjusted,
        datetime.now(ROME), require_today=not args.allow_stale,
    )
    save_report(summary, estimated, Path(args.output_dir))
    print(f"Estimated NAV (NOT NextWise): EUR {summary['estimated_nav_eur']:,.2f}")
    print(f"Price date: {summary['quote_date']}. Frozen snapshot: {summary['holdings_snapshot_date']}")
    print("Read-only market-data process. No orders executed.")


if __name__ == "__main__":
    main()

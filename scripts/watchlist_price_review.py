#!/usr/bin/env python3
"""Daily Ahold/ING price REVIEW gate, not a trading or NextWise integration.

The only side effect is saving dated research notes. It NEVER signs in to
NextWise, submits orders, or changes account holdings. Thresholds are
hypotheses for re-examining a thesis, not buy limits or sell stops.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ROME = ZoneInfo("Europe/Rome")


def load_rules(path: Path) -> dict:
    config = json.loads(path.read_text(encoding="utf-8"))
    if config.get("read_only") is not True or config.get("review_not_order") is not True:
        raise ValueError("Only read-only, review-only rules are supported")
    rows = config.get("rules", [])
    if not rows or len(set(x["ticker"] for x in rows)) != len(rows):
        raise ValueError("Missing or duplicate review tickers")
    for row in rows:
        t, level = row["ticker"], float(row["review_at_or_below_eur"])
        if not isinstance(t, str) or not t.endswith(".AS"):
            raise ValueError("Market venue must be confirmed for each symbol")
        if not np.isfinite(level) or level <= 0:
            raise ValueError("Invalid review level")
    return config


def extract_close(frame: pd.DataFrame, tickers: list[str]) -> pd.DataFrame:
    if not isinstance(frame.columns, pd.MultiIndex):
        raise ValueError("Expected multi-ticker Yahoo close data")
    if "Close" in frame.columns.get_level_values(0):
        prices = frame["Close"]
    elif "Close" in frame.columns.get_level_values(1):
        prices = frame.xs("Close", axis=1, level=1)
    else:
        raise ValueError("Raw Close is missing; adjusted prices aren't an executable quote")
    if not set(tickers).issubset(prices.columns):
        raise ValueError("Market-data provider omitted a review ticker")
    prices = prices.loc[:, tickers].copy().apply(pd.to_numeric, errors="coerce")
    ix = pd.to_datetime(prices.index)
    if ix.tz is not None:
        ix = ix.tz_localize(None)
    prices.index = ix.normalize()
    if prices.index.has_duplicates:
        raise ValueError("Duplicate quotation dates")
    return prices.sort_index()


def review_prices(
    config: dict, closes: pd.DataFrame, now: datetime, require_current: bool = True
) -> dict:
    tickers = [x["ticker"] for x in config["rules"]]
    if set(tickers) - set(closes.columns):
        raise ValueError("Missing review ticker prices")
    common = closes[tickers].dropna(how="any")
    if common.empty:
        raise ValueError("No synchronized daily closes")
    asof = common.index[-1].date()
    today = now.astimezone(ROME).date()
    if require_current and asof != today:
        raise ValueError(f"Stale prices: last common session {asof}; today {today}")
    for t in tickers:
        if closes[t].dropna().index[-1].date() != asof:
            raise ValueError("Daily market close is not synchronized")
    rows = []
    for rule in config["rules"]:
        ticker = rule["ticker"]
        close = float(common.iloc[-1][ticker])
        threshold = float(rule["review_at_or_below_eur"])
        if not np.isfinite(close) or close <= 0:
            raise ValueError("Invalid close")
        pending = rule.get("pending_order_user_reported", False)
        if not isinstance(pending, bool):
            raise ValueError("pending_order_user_reported must be a boolean")
        held = rule.get("held_in_portfolio_reported", False)
        if not isinstance(held, bool):
            raise ValueError("held_in_portfolio_reported must be a boolean")
        if pending and held:
            raise ValueError("Position cannot simultaneously be held and a pending new-entry order")
        if pending:
            if not isinstance(rule.get("reported_pending_quantity"), int) or rule["reported_pending_quantity"] <= 0:
                raise ValueError("Pending order requires a positive reported quantity")
            limit = float(rule.get("reported_pending_limit_eur", 0))
            if not np.isfinite(limit) or limit <= 0:
                raise ValueError("Pending order requires a valid reported limit")
        if held and (not isinstance(rule.get("reported_held_quantity"), int) or rule["reported_held_quantity"] <= 0):
            raise ValueError("Held position must have a positive reported quantity")
        rows.append({
            "ticker": ticker,
            "name": rule["name"],
            "close_eur": round(close, 6),
            "review_below_eur": threshold,
            "distance_pct": round((close/threshold - 1.0)*100.0, 4),
            "status": ("HELD_POSITION_MONITOR" if held else
                       "PENDING_ORDER_VERIFY_WITH_NEXTWISE" if pending else
                       "REVIEW_FUNDAMENTALS" if close <= threshold else "WAIT"),
            "reported_held_quantity": rule.get("reported_held_quantity") if held else None,
            "reported_pending_quantity": rule.get("reported_pending_quantity") if pending else None,
            "reported_pending_limit_eur": rule.get("reported_pending_limit_eur") if pending else None,
            "reason": rule["reason"],
        })
    return {
        "quote_date": str(asof),
        "generated_rome": now.astimezone(ROME).isoformat(timespec="seconds"),
        "source": "Third-party Yahoo Finance raw daily closing data (may be delayed), NOT NextWise",
        "execution": "NO ORDERS; read-only research",
        "note": "Price threshold is an analyst review trigger, not an order instruction",
        "entries": rows,
    }


def report_text(result: dict) -> str:
    out = [
        f"# Project Alpha — Candidate review levels ({result['quote_date']})", "",
        "> **NO TRADES. NOT OFFICIAL NEXTWISE QUOTES OR AUTO-ORDER SIGNALS.**",
        "> A breached price level invites human review of EPS, valuation,",
        "> corporate news, risk and the account's actual available order price.",
        "> PENDING_ORDER_VERIFY_WITH_NEXTWISE means a user-reported outstanding order:",
        "> **do not place a duplicate**. This tool cannot check NextWise fills or cancellations.",
        "> HELD_POSITION_MONITOR means a user-reported existing holding:",
        "> review position risk and fundamentals, **not a fresh buy entry**.",
        "",
        "| Candidate | Yahoo close EUR | Review at/below EUR | Distance to threshold | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for x in result["entries"]:
        out.append(
            f"| {x['name']} ({x['ticker']}) | {x['close_eur']:.2f} | "
            f"{x['review_below_eur']:.2f} | {x['distance_pct']:+.2f}% | {x['status']} |"
        )
    out += ["", "If REVIEW_FUNDAMENTALS is shown, **do not place an order**.",
            "First re-check guidance, FY2027 EPS, valuation assumptions, portfolio risk and NextWise order permissions.",
            "A level may be crossed because the investment thesis has deteriorated.",
            "Scheduled GitHub jobs may be delayed or skipped; they do NOT push notifications to a phone.",
            "All portfolio holdings remain unchanged unless an external NextWise trade is independently verified.", ""]
    return "\n".join(out)


def save(result: dict, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    content = report_text(result)
    for name in [f"{result['quote_date']}.md", "latest.md"]:
        (output / name).write_text(content, encoding="utf-8")
    (output / "latest.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n", encoding="utf-8"
    )


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rules", type=Path, default=ROOT/"data/price_review_levels_2026-11-20.json")
    p.add_argument("--output-dir", type=Path, default=ROOT/"reports/watchlist")
    args = p.parse_args()
    config = load_rules(args.rules)
    tickers = [x["ticker"] for x in config["rules"]]
    try:
        import yfinance as yf
    except ImportError as e:
        raise RuntimeError("Install data dependencies: pip install -e '.[data]'") from e
    raw = yf.download(
        tickers=tickers, period="1mo", interval="1d", auto_adjust=False,
        progress=False, threads=False, group_by="column", multi_level_index=True, timeout=30
    )
    if raw is None or raw.empty:
        raise ValueError("No market data; abort review rather than generating guessed prices")
    close = extract_close(raw, tickers)
    result = review_prices(config, close, datetime.now(ROME))
    save(result, args.output_dir)
    print(report_text(result))
    print("Research-only; no NextWise interaction or trade.")


if __name__ == "__main__":
    main()

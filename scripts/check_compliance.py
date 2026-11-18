#!/usr/bin/env python3
"""Run the ranking-date checks on a portfolio CSV (columns: ticker, weight).

Usage:
    python scripts/check_compliance.py                       # ACTUAL 18-Nov snapshot; not live
    python scripts/check_compliance.py --portfolio my.csv --prices prices.csv

Run it two trading days BEFORE every month-end ranking date: orders are processed periodically,
not instantly, so a fix placed at the last minute may not be executed in time.
With --prices (adjusted closes, date index, ticker columns; ideally 4 years) it also prints the
ex-ante volatility over 180 weeks, which is the denominator of the risk-adjusted criterion.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from alpha import metrics as m
from alpha.rules import format_report, ranking_date_report

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--portfolio", default=str(ROOT / "data" / "portfolio_actual_2026-11-18.csv"))
    ap.add_argument("--watchlist", default=str(ROOT / "data" / "watchlist_actual_extended.csv"))
    ap.add_argument("--prices", help="optional CSV of adjusted closes for ex-ante volatility")
    args = ap.parse_args()

    pf = pd.read_csv(args.portfolio)
    wl = pd.read_csv(args.watchlist)
    if not {"ticker","weight"}.issubset(pf.columns):
        raise ValueError("Portfolio CSV must contain ticker and weight")
    if pf.empty or pf["ticker"].duplicated().any():
        raise ValueError("Portfolio is empty or contains duplicate tickers")
    weights = pf.set_index("ticker")["weight"].astype(float)
    if not weights.map(lambda x: pd.notna(x) and 0 <= x <= 1).all() or weights.sum() > 1.000001:
        raise ValueError("Invalid weights: require nonnegative NAV fractions summing to at most 100%")
    sectors = dict(zip(wl.yahoo_ticker, wl.sector))
    if "sector" in pf.columns:
        sectors.update(dict(zip(pf.ticker, pf.sector)))
    if "market_value_eur" in pf.columns:
        implied = pf.loc[pf.weight > 0,"market_value_eur"] / pf.loc[pf.weight > 0,"weight"]
        if len(implied) and (implied.max() - implied.min()) > 1.0:
            raise ValueError("NAV weights do not reconcile with current position values")
    print("WARNING: research-only proxy, not an official Euronext scoring certification.")
    if "status" in pf.columns and pf["status"].astype(str).str.contains("2026-11-18").any():
        print("SNAPSHOT AS-OF 2026-11-18 — NOT LIVE. Refresh NextWise values before new orders.")


    unknown = [t for t in weights.index if t not in sectors]
    if unknown:
        raise ValueError(f"Missing sector mapping for: {unknown}")
    print(format_report(ranking_date_report(weights, sectors)))
    print(f"\nInvested {weights.sum():.1%}, cash {1 - weights.sum():.1%}")
    print("\nSector weights:")
    print(m.sector_weights(weights, sectors).map("{:.1%}".format).to_string())

    if args.prices:
        px = pd.read_csv(args.prices, index_col=0, parse_dates=True)
        if any(t not in px.columns for t in weights.index):
            raise ValueError("Prices are missing held tickers; risk metrics would be incomplete")
        available_weeks = m.history_weeks(px)
        short = available_weeks.reindex(weights.index)
        if short.isna().any() or (short < 180).any():
            print("WARNING: under 180 weekly price points for one or more holdings. Volatility is a short-history PROXY, not a verified game metric.")
        vol = m.ex_ante_volatility(px, weights, weeks=180)
        young = m.history_weeks(px)
        young = young[(young < 180) & young.index.isin(weights.index)]
        print(f"\nEx-ante volatility (180 weeks): {vol:.1%}")
        if len(young):
            print("History shorter than 180 weeks:", ", ".join(f"{t} ({int(v)}w)" for t, v in young.items()))


if __name__ == "__main__":
    main()

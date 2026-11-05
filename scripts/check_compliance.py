#!/usr/bin/env python3
"""Run the ranking-date checks on a portfolio CSV (columns: ticker, weight).

Usage:
    python scripts/check_compliance.py                       # data/portfolio_v1.csv
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
    ap.add_argument("--portfolio", default=str(ROOT / "data" / "portfolio_v1.csv"))
    ap.add_argument("--watchlist", default=str(ROOT / "data" / "watchlist.csv"))
    ap.add_argument("--prices", help="optional CSV of adjusted closes for ex-ante volatility")
    args = ap.parse_args()

    pf = pd.read_csv(args.portfolio)
    wl = pd.read_csv(args.watchlist)
    sectors = dict(zip(wl.yahoo_ticker, wl.sector))
    weights = pf.set_index("ticker")["weight"].astype(float)

    unknown = [t for t in weights.index if t not in sectors]
    if unknown:
        print(f"WARNING: no sector for {unknown}; add them to the watchlist")
    print(format_report(ranking_date_report(weights, sectors)))
    print(f"\nInvested {weights.sum():.1%}, cash {1 - weights.sum():.1%}")
    print("\nSector weights:")
    print(m.sector_weights(weights, sectors).map("{:.1%}".format).to_string())

    if args.prices:
        px = pd.read_csv(args.prices, index_col=0, parse_dates=True)
        vol = m.ex_ante_volatility(px, weights, weeks=180)
        young = m.history_weeks(px)
        young = young[(young < 180) & young.index.isin(weights.index)]
        print(f"\nEx-ante volatility (180 weeks): {vol:.1%}")
        if len(young):
            print("History shorter than 180 weeks:", ", ".join(f"{t} ({int(v)}w)" for t, v in young.items()))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the weekly markdown report from a weights CSV and a prices CSV.

portfolio.csv columns: ticker,weight   (weights as NAV fractions, cash is the remainder)
prices.csv: date index, one adjusted-close column per ticker
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from alpha.report import portfolio_snapshot, to_markdown

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--portfolio", required=True)
    ap.add_argument("--prices", required=True)
    ap.add_argument("--watchlist", default=str(ROOT / "data" / "watchlist.csv"))
    ap.add_argument("--out", default=str(ROOT / "reports" / "weekly_latest.md"))
    args = ap.parse_args()

    pf = pd.read_csv(args.portfolio).set_index("ticker")["weight"]
    prices = pd.read_csv(args.prices, index_col=0, parse_dates=True)
    wl = pd.read_csv(args.watchlist)
    sectors = dict(zip(wl.yahoo_ticker, wl.sector))
    snap = portfolio_snapshot(pf, prices, sectors)
    text = to_markdown(snap, as_of=prices.index.max().date())
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(text)
    print(text)


if __name__ == "__main__":
    main()

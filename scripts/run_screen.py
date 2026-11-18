#!/usr/bin/env python3
"""Screen the watchlist and propose a portfolio.

Usage (on your own computer, where Yahoo Finance is reachable):
    pip install -e ".[data]"
    python scripts/run_screen.py --period 2y

Offline / demo mode with synthetic prices (no network):
    python scripts/run_screen.py --demo

The proposal is a STARTING POINT. Always check price, liquidity and tradability in NextWise.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from alpha import metrics as m
from alpha.optimizer import optimize_weights, scores_to_alpha
from alpha.report import portfolio_snapshot, to_markdown
from alpha.screener import composite_score, price_factors, select_universe
from alpha.synthetic import synthetic_prices

ROOT = Path(__file__).resolve().parents[1]


def load_prices(tickers: list[str], sectors: dict[str, str], args) -> pd.DataFrame:
    if args.demo:
        return synthetic_prices(tickers, sectors, days=520, seed=1)
    if args.prices:
        return pd.read_csv(args.prices, index_col=0, parse_dates=True)
    try:
        import yfinance as yf
    except ImportError as exc:  # pragma: no cover
        raise SystemExit("Install yfinance (pip install -e '.[data]') or pass --prices / --demo") from exc
    px = yf.download(tickers, period=args.period, auto_adjust=True, progress=False)["Close"]
    return px.dropna(axis=1, thresh=int(len(px) * 0.8))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--watchlist", default=str(ROOT / "data" / "watchlist.csv"))
    ap.add_argument("--analyst", default=str(ROOT / "data" / "analyst_inputs.csv"))
    ap.add_argument("--prices", help="CSV of adjusted closes (date index, ticker columns)")
    ap.add_argument("--period", default="2y")
    ap.add_argument("--n", type=int, default=24, help="number of positions")
    ap.add_argument("--demo", action="store_true", help="use synthetic prices")
    ap.add_argument("--out", default=str(ROOT / "reports" / "screen_latest.md"))
    args = ap.parse_args()

    wl = pd.read_csv(args.watchlist)
    sectors = dict(zip(wl.yahoo_ticker, wl.sector))
    prices = load_prices(list(wl.yahoo_ticker), sectors, args).ffill()
    tickers = [t for t in prices.columns if t in sectors]
    prices = prices[tickers]

    manual = None
    p = Path(args.analyst)
    if p.exists():
        manual = pd.read_csv(p, comment="#").set_index("yahoo_ticker")
        manual = manual if len(manual) else None

    factors = price_factors(prices)
    table = composite_score(factors, manual)
    picks = select_universe(table["score"], sectors, n=args.n, min_sectors=10)

    rets = m.simple_returns(prices[picks])
    cov = rets.cov() * m.TRADING_DAYS
    vol = pd.Series(np.sqrt(np.diag(cov)), index=cov.index)
    bench = rets.mean(axis=1)  # equal-weight proxy of the picked universe
    betas = rets.apply(lambda s: m.beta(s, bench))
    alpha = scores_to_alpha(table.loc[picks, "composite_z"], vol)
    w = optimize_weights(alpha, cov, sector_map=sectors, betas=betas)

    snap = portfolio_snapshot(w, prices, sectors)
    out = ["# Screen output", "", f"Weights used: {table['weights_used'].iloc[0]}", "",
           "## Proposed portfolio", "", "| Ticker | Name | Sector | Weight | Score |", "|---|---|---|---|---|"]
    names = dict(zip(wl.yahoo_ticker, wl.name))
    for t, wt in w.sort_values(ascending=False).items():
        out.append(f"| {t} | {names[t]} | {sectors[t]} | {wt:.2%} | {table.loc[t, 'score']:.0f} |")
    out += ["", to_markdown(snap, "Proposed portfolio analytics — NOT executed holdings", as_of=prices.index.max().date())]
    text = "\n".join(out)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(text)
    print(text)


if __name__ == "__main__":
    main()

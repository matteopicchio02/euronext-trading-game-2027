#!/usr/bin/env python3
"""Run the scoring-structure Monte Carlo and print a comparison table."""

from __future__ import annotations

import argparse

import pandas as pd

from alpha.scoring_sim import SimConfig, run_simulation


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--worlds", type=int, default=150)
    ap.add_argument("--field", type=int, default=400)
    ap.add_argument("--rho", type=float, default=0.20, help="signal / true-alpha correlation")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--out", default="reports/simulation_latest.csv")
    args = ap.parse_args()
    cfg = SimConfig(n_worlds=args.worlds, field_size=args.field, signal_rho=args.rho, seed=args.seed)
    res = run_simulation(cfg)
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    print(res.round(3).T)
    res.to_csv(args.out)


if __name__ == "__main__":
    main()

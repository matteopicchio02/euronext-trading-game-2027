"""Synthetic market data for tests, demos and the scoring simulator (NOT real prices)."""

from __future__ import annotations

import numpy as np
import pandas as pd


def synthetic_prices(
    tickers: list[str],
    sectors: dict[str, str],
    days: int = 400,
    seed: int = 0,
    market_vol: float = 0.16,
    sector_vol: float = 0.08,
) -> pd.DataFrame:
    """One-factor + sector-factor price paths, business-day indexed, ending today."""
    rng = np.random.default_rng(seed)
    uniq = sorted(set(sectors.values()))
    mkt = rng.normal(0.06 / 252, market_vol / np.sqrt(252), days)
    sec = {s: rng.normal(0, sector_vol / np.sqrt(252), days) for s in uniq}
    data = {}
    for t in tickers:
        beta = rng.uniform(0.6, 1.4)
        idio = rng.uniform(0.15, 0.35) / np.sqrt(252)
        drift = rng.normal(0.0, 0.10) / 252
        r = beta * mkt + sec[sectors[t]] + rng.normal(0, idio, days) + drift
        data[t] = 100.0 * np.cumprod(1.0 + r)
    idx = pd.bdate_range(end=pd.Timestamp.today().normalize(), periods=days)
    return pd.DataFrame(data, index=idx)

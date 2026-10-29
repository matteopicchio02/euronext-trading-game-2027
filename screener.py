"""Factor screener: turns a price history (+ optional analyst inputs) into a 0-100 score.

Price-derived factors are computed automatically. Fundamental factors (quality, valuation,
catalyst) come from optional 0-100 analyst inputs in ``data/analyst_inputs.csv``; if a
factor is missing its weight is redistributed over the available ones.

The weights below are a prior, not a result: they must be re-tested out of sample before
being trusted (see docs/METHODOLOGY.md).
"""

from __future__ import annotations

from collections.abc import Mapping

import numpy as np
import pandas as pd

FACTOR_WEIGHTS: dict[str, float] = {
    "momentum": 0.30,
    "catalyst": 0.20,
    "quality": 0.15,
    "downside": 0.15,
    "valuation": 0.10,
    "diversification": 0.10,
}

D_3M, D_6M, D_12M, D_SKIP = 63, 126, 252, 21


def zscore(s: pd.Series, clip: float = 3.0) -> pd.Series:
    """Cross-sectional z-score, winsorised at +/- ``clip``."""
    s = s.astype(float)
    sd = s.std(ddof=0)
    if not np.isfinite(sd) or sd == 0:
        return pd.Series(0.0, index=s.index)
    return ((s - s.mean()) / sd).clip(-clip, clip)


def price_factors(prices: pd.DataFrame, benchmark: pd.Series | None = None) -> pd.DataFrame:
    """Raw price-based factor table (one row per ticker)."""
    prices = prices.sort_index().ffill()
    rets = prices.pct_change()
    last = prices.iloc[-1]
    n = len(prices)

    def ret_over(days: int, skip: int = 0) -> pd.Series:
        if n <= days + skip:
            return pd.Series(np.nan, index=prices.columns)
        end = prices.iloc[-1 - skip]
        start = prices.iloc[-1 - skip - days]
        return end / start - 1.0

    out = pd.DataFrame(index=prices.columns)
    out["mom_3m"] = ret_over(D_3M)
    out["mom_6m"] = ret_over(D_6M)
    out["mom_12_1"] = ret_over(D_12M - D_SKIP, D_SKIP)
    if benchmark is not None:
        b = benchmark.sort_index().ffill()
        b3 = b.iloc[-1] / b.iloc[-1 - D_3M] - 1.0 if len(b) > D_3M else 0.0
        b6 = b.iloc[-1] / b.iloc[-1 - D_6M] - 1.0 if len(b) > D_6M else 0.0
        out["mom_3m"] -= b3
        out["mom_6m"] -= b6
    out["vol_60d"] = rets.tail(60).std() * np.sqrt(252)
    tail = rets.tail(D_6M)
    out["downside_dev"] = np.sqrt((tail.clip(upper=0.0) ** 2).mean()) * np.sqrt(252)
    window = prices.tail(D_6M)
    out["mdd_6m"] = -(window / window.cummax() - 1.0).min()
    sma = prices.tail(200).mean()
    out["trend_200d"] = last / sma - 1.0
    corr = tail.corr()
    k = max(len(corr) - 1, 1)
    out["avg_corr"] = (corr.sum() - 1.0) / k
    return out


def composite_score(
    factors: pd.DataFrame,
    manual: pd.DataFrame | None = None,
    weights: Mapping[str, float] = FACTOR_WEIGHTS,
) -> pd.DataFrame:
    """Combine factor z-scores into a composite z and a 0-100 percentile-style score."""
    z = pd.DataFrame(index=factors.index)
    mom_parts = [zscore(factors[c]) for c in ("mom_3m", "mom_6m", "mom_12_1") if factors[c].notna().any()]
    mom_parts.append(zscore(factors["trend_200d"].fillna(factors["trend_200d"].median())))
    z["momentum"] = zscore(sum(mom_parts) / len(mom_parts))
    z["downside"] = zscore(
        -(zscore(factors["vol_60d"]) + zscore(factors["downside_dev"]) + zscore(factors["mdd_6m"])) / 3.0
    )
    z["diversification"] = zscore(-factors["avg_corr"])
    if manual is not None:
        for col in ("quality", "valuation", "catalyst"):
            if col in manual.columns:
                m = manual[col].reindex(factors.index)
                if m.notna().sum() >= 3:
                    z[col] = zscore(m.fillna(m.median()))

    used = {k: v for k, v in weights.items() if k in z.columns}
    total = sum(used.values())
    composite = sum(z[k] * (v / total) for k, v in used.items())
    out = z.copy()
    out["composite_z"] = composite
    out["score"] = composite.rank(pct=True) * 100.0
    out["weights_used"] = ", ".join(f"{k}={v / total:.0%}" for k, v in used.items())
    return out


def select_universe(
    scores: pd.Series,
    sector_map: Mapping[str, str],
    n: int = 22,
    max_per_sector: int = 3,
    min_sectors: int = 9,
) -> list[str]:
    """Pick ``n`` names by score, forcing breadth across sectors.

    Stage 1 seeds the best name of each of the ``min_sectors`` best-scoring sectors.
    Stage 2 fills the remainder by score subject to ``max_per_sector``.
    """
    ranked = scores.dropna().sort_values(ascending=False)
    best: dict[str, tuple[str, float]] = {}
    for t, s in ranked.items():
        sec = sector_map.get(t)
        if sec is not None and sec not in best:
            best[sec] = (t, float(s))
    seeds = sorted(best.values(), key=lambda x: -x[1])[:min_sectors]
    chosen = [t for t, _ in seeds]
    counts = {sector_map[t]: 1 for t in chosen}
    for t in ranked.index:
        if len(chosen) >= n:
            break
        sec = sector_map.get(t)
        if t in chosen or sec is None or counts.get(sec, 0) >= max_per_sector:
            continue
        chosen.append(t)
        counts[sec] = counts.get(sec, 0) + 1
    return chosen

"""Position sizing helpers."""

from __future__ import annotations

import math


def shares_for_risk(equity: float, risk_pct: float, entry: float, stop: float) -> int:
    """Whole shares such that hitting ``stop`` loses ``risk_pct`` of ``equity``."""
    if entry <= 0 or stop <= 0 or stop >= entry:
        raise ValueError("need 0 < stop < entry for a long position")
    risk_per_share = entry - stop
    return max(int(math.floor(equity * risk_pct / risk_per_share)), 0)


def weight_for_risk(risk_pct: float, stop_distance_pct: float, max_weight: float = 0.06) -> float:
    """Position weight implied by a risk budget and a stop distance, capped at ``max_weight``."""
    if stop_distance_pct <= 0:
        raise ValueError("stop distance must be positive")
    return min(risk_pct / stop_distance_pct, max_weight)


def atr_stop(entry: float, atr: float, multiple: float = 2.5) -> float:
    """Volatility-based stop level for a long position."""
    return max(entry - multiple * atr, 0.0)

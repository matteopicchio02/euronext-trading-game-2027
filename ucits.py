"""UCITS-style diversification checks.

Euronext lists "compliance with UCITS rules" as a scoring criterion but does not define it
publicly. We therefore implement the best-known UCITS diversification limits as OUR working
interpretation (to be confirmed with the organisers):

* 5/10/40 rule: no issuer above 10% of NAV, and the issuers above 5% may not add up to
  more than 40% of NAV.
* A single UCITS/ETF holding is capped at 20% of NAV.

Consequence worth knowing: staying fully invested under 5/10/40 needs roughly 19+ positions.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

import pandas as pd

EPS = 1e-9


@dataclass
class UcitsReport:
    compliant: bool
    max_weight: float
    sum_above_threshold: float
    violations: list[str] = field(default_factory=list)


def check_ucits(
    weights: pd.Series,
    etfs: Iterable[str] = (),
    single_cap: float = 0.10,
    threshold: float = 0.05,
    aggregate_cap: float = 0.40,
    etf_cap: float = 0.20,
) -> UcitsReport:
    """Check the 5/10/40 rule (and the single-ETF cap) on NAV-fraction weights."""
    etf_set = set(etfs)
    violations: list[str] = []
    equities = weights[[t for t in weights.index if t not in etf_set]]
    funds = weights[[t for t in weights.index if t in etf_set]]

    over = equities[equities > single_cap + EPS]
    for t, w in over.items():
        violations.append(f"{t}: {w:.2%} exceeds single-issuer cap {single_cap:.0%}")

    above = equities[equities > threshold + EPS]
    # ETFs/UCITS units are not "issuers" for 5/10/40 but are capped separately.
    sum_above = float(above.sum())
    if sum_above > aggregate_cap + EPS:
        violations.append(
            f"positions above {threshold:.0%} sum to {sum_above:.2%} (cap {aggregate_cap:.0%})"
        )
    for t, w in funds[funds > etf_cap + EPS].items():
        violations.append(f"{t}: {w:.2%} exceeds single-fund cap {etf_cap:.0%}")

    return UcitsReport(
        compliant=not violations,
        max_weight=float(weights.max()) if len(weights) else 0.0,
        sum_above_threshold=sum_above,
        violations=violations,
    )


def repair_ucits(
    weights: pd.Series,
    single_cap: float = 0.10,
    threshold: float = 0.05,
    aggregate_cap: float = 0.40,
) -> pd.Series:
    """Minimally adjust equity weights so the 5/10/40 rule holds.

    Names above the single cap are clipped. If the names above ``threshold`` still add up
    to more than ``aggregate_cap``, the smallest of them are pulled down to ``threshold``.
    Freed weight is redistributed pro rata to the room left below ``threshold``; whatever
    cannot be placed stays in cash.
    """
    w = weights.astype(float).copy()
    freed = 0.0

    over = w[w > single_cap]
    freed += float((over - single_cap).sum())
    w[over.index] = single_cap

    above = w[w > threshold + EPS].sort_values()
    total = float(above.sum())
    for t, val in above.items():
        if total <= aggregate_cap + EPS:
            break
        freed += float(val - threshold)
        w[t] = threshold
        total -= float(val)

    if freed > EPS:
        room = (threshold - w).clip(lower=0.0)
        room_total = float(room.sum())
        if room_total > EPS:
            add = min(freed, room_total)
            w = w + room / room_total * add
    return w


def min_positions_fully_invested(
    invested: float = 1.0,
    single_cap: float = 0.10,
    threshold: float = 0.05,
    aggregate_cap: float = 0.40,
) -> int:
    """Smallest number of equity positions that can hold ``invested`` of NAV under 5/10/40.

    Best case: ``k = aggregate_cap // single_cap`` names sit at the single cap and every
    other name sits exactly at the threshold, so capacity(n) = k*single_cap + (n-k)*threshold.
    Pass a smaller ``single_cap`` (e.g. 0.06, our house limit) to see the practical minimum.
    """
    k = int(aggregate_cap // single_cap + EPS)
    for n in range(1, 1000):
        top = min(n, k)
        capacity = top * single_cap + max(n - k, 0) * threshold
        if capacity + EPS >= invested:
            return n
    raise ValueError("invested weight not reachable")

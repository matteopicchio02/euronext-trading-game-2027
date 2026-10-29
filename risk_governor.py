"""Tournament-aware risk governor.

A national title goes to ONE participant, so the payoff is convex in rank: standing still in
the middle is worth little. The governor therefore changes the risk budget with (a) the
drawdown, (b) our rank percentile and (c) the time left, instead of using one static limit.

Thresholds are working hypotheses, calibrated in docs/METHODOLOGY.md against the simulated
distribution of drawdowns for a ~17% volatility equity book (they are NOT Euronext rules).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Mode(str, Enum):
    ATTACK = "ATTACK"  # behind with time left: take more beta, stay inside UCITS limits
    NEUTRAL = "NEUTRAL"
    CAUTION = "CAUTION"  # drawdown review zone: no new tactical entries
    DEFENSE = "DEFENSE"  # deep drawdown: cut beta, mandatory written review
    LOCK_IN = "LOCK_IN"  # leading near the end: protect the lead


@dataclass(frozen=True)
class RiskBudget:
    mode: Mode
    beta_target: float
    max_weight: float
    equity_exposure: float
    new_tactical_entries: bool
    note: str


def decide_mode(
    drawdown: float,
    rank_percentile: float | None,
    days_left: int,
    review_dd: float = 0.08,
    defense_dd: float = 0.13,
) -> RiskBudget:
    """Map the current state to a risk budget.

    Parameters
    ----------
    drawdown: current drawdown from the NAV peak, positive fraction (0.07 = -7%).
    rank_percentile: 1.0 = first place, 0.0 = last; None if the ranking is not visible.
    days_left: calendar days to the end of the competition.
    """
    if drawdown >= defense_dd:
        return RiskBudget(
            Mode.DEFENSE, 0.80, 0.05, 0.92, False,
            "Deep drawdown: stop tactical entries, cut beta, write the post-mortem before adding risk.",
        )
    if drawdown >= review_dd:
        return RiskBudget(
            Mode.CAUTION, 0.95, 0.06, 0.96, False,
            "Review zone: no new tactical entries, do not average down, check correlation clusters.",
        )
    if rank_percentile is not None:
        if days_left <= 21 and rank_percentile >= 0.97:
            return RiskBudget(
                Mode.LOCK_IN, 0.75, 0.05, 0.90, False,
                "Leading near the end: reduce beta and avoid event risk; the lead is worth more than extra return.",
            )
        if days_left <= 45 and rank_percentile < 0.85:
            return RiskBudget(
                Mode.ATTACK, 1.25, 0.08, 0.99, True,
                "Behind with time left: raise beta and conviction, still within the 5/10/40 limits.",
            )
    return RiskBudget(
        Mode.NEUTRAL, 1.05, 0.06, 0.96, True,
        "Standard budget: house limits, full diversification, beta slightly above 1.",
    )

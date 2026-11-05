"""Ranking-date compliance checks for an individual participant.

The NextWise rulebook (https://www.nextwise.fr/le-reglement, individual-investor section)
describes thresholds that are checked on RANKING DATES, not at every order:

* at least 10 securities,
* exposure to at least 4 sectors (ICB),
* no more than 15% of the portfolio in a single security,
* UCITS 5/10/40 is *scored* for individuals (not an eligibility condition).

Missing a threshold does not remove points already earned, but it can limit the points
available under the related criteria. The page describes the Next Challenge; the Euronext
Trading Game runs on the same platform, so we treat these as likely, not certain. Re-check
the live terms in NextWise before relying on them.

ETFs: HHI, diversification ratio and sectors are assessed with look-through on the platform.
We do not model look-through here, so ETF positions count as one security each and add no
sector (a conservative reading).
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass

import pandas as pd

from . import metrics as m
from .ucits import check_ucits

EPS = 1e-9


@dataclass(frozen=True)
class RuleCheck:
    name: str
    passed: bool
    value: str
    limit: str
    kind: str = "threshold"  # "threshold" (platform) or "scored" (affects points only)


def check_individual_thresholds(
    weights: pd.Series,
    sector_map: Mapping[str, str],
    etfs: Iterable[str] = (),
    min_positions: int = 10,
    min_sectors: int = 4,
    max_weight: float = 0.15,
    min_position_weight: float = 0.005,
) -> list[RuleCheck]:
    """Three platform thresholds for individuals, evaluated on NAV-fraction weights."""
    etf_set = set(etfs)
    held = weights[weights > min_position_weight]
    direct = held[[t for t in held.index if t not in etf_set]]
    sectors = {sector_map[t] for t in direct.index if t in sector_map}
    top = float(weights.max()) if len(weights) else 0.0
    return [
        RuleCheck("Securities held", len(held) >= min_positions, str(len(held)), f">= {min_positions}"),
        RuleCheck("Sectors covered", len(sectors) >= min_sectors, str(len(sectors)), f">= {min_sectors}"),
        RuleCheck("Largest position", top <= max_weight + EPS, f"{top:.2%}", f"<= {max_weight:.0%}"),
    ]


def ranking_date_report(
    weights: pd.Series,
    sector_map: Mapping[str, str],
    etfs: Iterable[str] = (),
) -> list[RuleCheck]:
    """Thresholds plus the scored structure criteria, ready to print before a ranking date."""
    checks = check_individual_thresholds(weights, sector_map, etfs)
    u = check_ucits(weights, etfs=etfs)
    checks.append(
        RuleCheck(
            "UCITS 5/10/40 (scored)",
            u.compliant,
            f"max {u.max_weight:.2%}, above-5% sum {u.sum_above_threshold:.2%}",
            "single <= 10%, above-5% sum <= 40%",
            kind="scored",
        )
    )
    h = m.hhi(weights, normalize=True)
    checks.append(
        RuleCheck("HHI (informational)", True, f"{h:.4f} (effective N {1 / h:.1f})" if h > 0 else "n/a",
                  "lower is better", kind="scored")
    )
    return checks


def format_report(checks: list[RuleCheck]) -> str:
    """Markdown table; the first line says whether every threshold passes."""
    ok = all(c.passed for c in checks if c.kind == "threshold")
    lines = [
        f"Ranking-date thresholds: {'ALL PASS' if ok else 'FAIL - fix before the ranking date'}",
        "",
        "| Check | Result | Value | Limit |",
        "|---|---|---|---|",
    ]
    for c in checks:
        lines.append(f"| {c.name} | {'pass' if c.passed else 'FAIL'} | {c.value} | {c.limit} |")
    return "\n".join(lines)

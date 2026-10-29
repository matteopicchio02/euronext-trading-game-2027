"""Weekly portfolio report generator (markdown)."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import date

import pandas as pd

from . import metrics as m
from .ucits import check_ucits


def portfolio_snapshot(
    weights: pd.Series,
    prices: pd.DataFrame,
    sector_map: Mapping[str, str],
    etfs: tuple[str, ...] = (),
    benchmark: pd.Series | None = None,
) -> dict:
    """Compute the quantities we publish every week."""
    rets = m.simple_returns(prices[weights.index])
    pr = m.portfolio_returns(rets, weights)
    nav = m.nav_from_returns(pr)
    cov = rets.cov() * m.TRADING_DAYS
    rep = check_ucits(weights, etfs=etfs)
    snap = {
        "invested": float(weights.sum()),
        "cash": float(1.0 - weights.sum()),
        "n_positions": int((weights > 0).sum()),
        "return": m.cumulative_return(pr),
        "volatility": m.annualized_volatility(pr),
        "sharpe": m.sharpe_ratio(pr),
        "max_drawdown": m.max_drawdown(nav),
        "hhi": m.hhi(weights),
        "effective_n": m.effective_n(weights),
        "sectors": m.sector_count(weights, sector_map),
        "diversification_ratio": m.diversification_ratio(weights.to_numpy(), cov.loc[weights.index, weights.index]),
        "ucits_ok": rep.compliant,
        "ucits_violations": rep.violations,
        "sector_weights": m.sector_weights(weights, sector_map),
        "risk_contrib": m.risk_contributions(weights, cov).sort_values(ascending=False),
    }
    if benchmark is not None:
        b = benchmark.pct_change().dropna()
        snap["beta"] = m.beta(pr, b)
    return snap


def to_markdown(snap: dict, title: str = "Weekly Portfolio Report", as_of: date | None = None) -> str:
    as_of = as_of or date.today()
    lines = [
        f"# {title} - {as_of.isoformat()}",
        "",
        "> Independent educational project. Not affiliated with Euronext or any bank. Not investment advice.",
        "",
        "## Key metrics",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Return over window | {snap['return']:.2%} |",
        f"| Annualised volatility | {snap['volatility']:.2%} |",
        f"| Sharpe (rf=0) | {snap['sharpe']:.2f} |",
        f"| Max drawdown | {snap['max_drawdown']:.2%} |",
        f"| HHI / effective N | {snap['hhi']:.4f} / {snap['effective_n']:.1f} |",
        f"| Sectors covered | {snap['sectors']} |",
        f"| Diversification ratio | {snap['diversification_ratio']:.2f} |",
        f"| Positions / cash | {snap['n_positions']} / {snap['cash']:.1%} |",
        f"| UCITS 5/10/40 check | {'PASS' if snap['ucits_ok'] else 'FAIL'} |",
    ]
    if "beta" in snap:
        lines.append(f"| Beta vs benchmark | {snap['beta']:.2f} |")
    if snap["ucits_violations"]:
        lines += ["", "**Violations:**"] + [f"- {v}" for v in snap["ucits_violations"]]
    lines += ["", "## Sector weights", "", "| Sector | Weight |", "|---|---|"]
    lines += [f"| {k} | {v:.1%} |" for k, v in snap["sector_weights"].items()]
    lines += ["", "## Top risk contributors", "", "| Ticker | Share of variance |", "|---|---|"]
    lines += [f"| {k} | {v:.1%} |" for k, v in snap["risk_contrib"].head(5).items()]
    lines += ["", "## Decisions and lessons", "", "_Fill in from the decision log._", ""]
    return "\n".join(lines)

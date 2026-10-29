"""Constrained portfolio construction.

Mean-variance with an explicit tilt for the game's structural criteria:

    minimise  -w.alpha + 0.5*lambda*w'Sigma*w + eta*sum(w^2) - delta*DR(w)

subject to a fixed invested fraction, per-name bounds, sector caps and a beta band.
Expected excess returns come from Grinold's rule  alpha = IC * sigma * z  with a deliberately
small information coefficient (default 0.05): the optimiser should not trust the score much.
"""

from __future__ import annotations

from collections.abc import Mapping

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from .metrics import diversification_ratio
from .ucits import repair_ucits


def scores_to_alpha(score_z: pd.Series, vol: pd.Series, ic: float = 0.05) -> pd.Series:
    """Grinold's rule: expected annual excess return = IC * volatility * z-score."""
    return ic * vol.reindex(score_z.index) * score_z


def optimize_weights(
    alpha: pd.Series,
    cov: pd.DataFrame,
    sector_map: Mapping[str, str] | None = None,
    betas: pd.Series | None = None,
    invested: float = 0.96,
    min_w: float = 0.025,
    max_w: float = 0.06,
    sector_cap: float = 0.25,
    beta_band: tuple[float, float] | None = (0.95, 1.20),
    risk_aversion: float = 6.0,
    hhi_penalty: float = 0.5,
    dr_weight: float = 0.02,
) -> pd.Series:
    """Return NAV-fraction weights (sum == ``invested``) for the names in ``alpha``."""
    names = list(alpha.index)
    n = len(names)
    if n * max_w < invested - 1e-9 or n * min_w > invested + 1e-9:
        raise ValueError(f"{n} names cannot satisfy bounds for invested={invested}")
    a = alpha.to_numpy(float)
    sigma = cov.loc[names, names].to_numpy(float)

    def objective(w: np.ndarray) -> float:
        val = -w @ a + 0.5 * risk_aversion * (w @ sigma @ w) + hhi_penalty * np.sum(w**2)
        if dr_weight:
            dr = diversification_ratio(w, sigma)
            if np.isfinite(dr):
                val -= dr_weight * dr
        return float(val)

    cons: list[dict] = [{"type": "eq", "fun": lambda w: w.sum() - invested}]
    if sector_map is not None:
        sectors = sorted({sector_map[t] for t in names})
        for sec in sectors:
            idx = np.array([i for i, t in enumerate(names) if sector_map[t] == sec])
            cons.append({"type": "ineq", "fun": lambda w, idx=idx: sector_cap - w[idx].sum()})
    if betas is not None and beta_band is not None:
        b = betas.reindex(names).to_numpy(float)
        lo, hi = beta_band
        cons.append({"type": "ineq", "fun": lambda w: (w @ b) / invested - lo})
        cons.append({"type": "ineq", "fun": lambda w: hi - (w @ b) / invested})

    x0 = np.full(n, invested / n)
    res = minimize(
        objective,
        x0,
        method="SLSQP",
        bounds=[(min_w, max_w)] * n,
        constraints=cons,
        options={"maxiter": 500, "ftol": 1e-10},
    )
    w = res.x if res.success else x0
    w = pd.Series(np.clip(w, min_w, max_w), index=names)
    w *= invested / w.sum()
    return repair_ucits(w)

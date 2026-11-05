"""Portfolio analytics: the quantities the Euronext Trading Game scores, plus a few extras.

Conventions
-----------
* ``weights`` are fractions of NAV. Weights that sum to less than 1 imply the remainder
  is held in cash, which earns 0 in this module (the game pays no interest).
* Returns are simple daily returns. Portfolios are assumed rebalanced daily to constant
  weights, which is an approximation of buy-and-hold over short windows.
* ``max_drawdown`` is returned as a positive fraction (0.12 means -12% from the peak).
"""

from __future__ import annotations

from collections.abc import Mapping

import numpy as np
import pandas as pd

TRADING_DAYS = 252


def simple_returns(prices: pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    """Daily simple returns from a price table, dropping the all-NaN first row."""
    return prices.pct_change().dropna(how="all")


def portfolio_returns(asset_returns: pd.DataFrame, weights: pd.Series) -> pd.Series:
    """Daily portfolio return for constant weights; missing assets get weight 0."""
    w = weights.reindex(asset_returns.columns).fillna(0.0)
    return asset_returns.fillna(0.0).mul(w, axis=1).sum(axis=1)


def cumulative_return(returns: pd.Series) -> float:
    """Compounded return over the whole sample."""
    return float((1.0 + returns).prod() - 1.0)


def annualized_volatility(returns: pd.Series, periods: int = TRADING_DAYS) -> float:
    return float(returns.std(ddof=1) * np.sqrt(periods))


def nav_from_returns(returns: pd.Series, start: float = 1.0) -> pd.Series:
    return start * (1.0 + returns).cumprod()


def drawdown_series(nav: pd.Series) -> pd.Series:
    """Drawdown from running peak as non-positive fractions."""
    peak = nav.cummax()
    return nav / peak - 1.0


def max_drawdown(nav: pd.Series) -> float:
    """Largest peak-to-trough loss as a positive fraction."""
    if len(nav) == 0:
        return 0.0
    return float(-drawdown_series(nav).min())


def hhi(weights: pd.Series | np.ndarray, normalize: bool = True) -> float:
    """Herfindahl-Hirschman Index of position weights, in [0, 1].

    With ``normalize=True`` the weights are rescaled to sum to 1 (concentration of the
    invested part). With ``normalize=False`` raw NAV fractions are used, so cash that is
    not counted as a position lowers the index mechanically. The platform's exact
    convention is unpublished, so both are exposed.
    """
    w = np.asarray(weights, dtype=float)
    w = w[w > 0]
    if w.size == 0:
        return 0.0
    if normalize:
        w = w / w.sum()
    return float(np.sum(w**2))


def effective_n(weights: pd.Series | np.ndarray) -> float:
    """Effective number of equally weighted positions (1 / HHI)."""
    h = hhi(weights, normalize=True)
    return float("inf") if h == 0 else 1.0 / h


def sharpe_ratio(returns: pd.Series, rf_annual: float = 0.0, periods: int = TRADING_DAYS) -> float:
    excess = returns - rf_annual / periods
    sd = excess.std(ddof=1)
    if not np.isfinite(sd) or sd < 1e-12:
        return float("nan")
    return float(excess.mean() / sd * np.sqrt(periods))


def sortino_ratio(returns: pd.Series, mar_annual: float = 0.0, periods: int = TRADING_DAYS) -> float:
    excess = returns - mar_annual / periods
    downside = np.minimum(excess, 0.0)
    dd = np.sqrt(np.mean(downside**2))
    if dd == 0:
        return float("nan")
    return float(excess.mean() / dd * np.sqrt(periods))


def diversification_ratio(weights: pd.Series | np.ndarray, cov: pd.DataFrame | np.ndarray) -> float:
    """Weighted average asset volatility divided by portfolio volatility.

    1.0 means no diversification benefit (perfect correlation); higher is better.
    """
    w = np.asarray(weights, dtype=float)
    sigma = np.asarray(cov, dtype=float)
    asset_vol = np.sqrt(np.clip(np.diag(sigma), 0.0, None))
    port_var = float(w @ sigma @ w)
    if port_var <= 0:
        return float("nan")
    return float(w @ asset_vol / np.sqrt(port_var))


def risk_contributions(weights: pd.Series, cov: pd.DataFrame) -> pd.Series:
    """Share of portfolio variance contributed by each position (sums to 1)."""
    w = weights.reindex(cov.index).fillna(0.0).to_numpy()
    sigma = cov.to_numpy()
    port_var = float(w @ sigma @ w)
    if port_var <= 0:
        return pd.Series(0.0, index=cov.index)
    return pd.Series(w * (sigma @ w) / port_var, index=cov.index)


def sector_count(
    weights: pd.Series, sector_map: Mapping[str, str], min_weight: float = 0.0
) -> int:
    """Number of distinct sectors holding more than ``min_weight`` of NAV."""
    held = weights[weights > min_weight]
    return len({sector_map[t] for t in held.index if t in sector_map})


def sector_weights(weights: pd.Series, sector_map: Mapping[str, str]) -> pd.Series:
    out = pd.Series(weights).groupby(lambda t: sector_map.get(t, "UNKNOWN")).sum()
    return out.sort_values(ascending=False)


def beta(returns: pd.Series, benchmark: pd.Series) -> float:
    df = pd.concat([returns, benchmark], axis=1).dropna()
    if len(df) < 3:
        return float("nan")
    var = df.iloc[:, 1].var(ddof=1)
    return float(df.iloc[:, 0].cov(df.iloc[:, 1]) / var) if var > 0 else float("nan")

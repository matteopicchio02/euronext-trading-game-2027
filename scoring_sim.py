"""Monte Carlo simulator of the Euronext-style score under UNKNOWN criterion weights.

Why: the organisers publish six criteria but not their weights. Instead of guessing one
formula, we draw many weight vectors from a Dirichlet distribution, simulate a field of
competitors, and ask which portfolio *design* ranks well across most of them.

What this is NOT: a return forecast. Prices are synthetic (factor model); the field of
competitors is an assumption; the criteria are scored as percentile ranks inside the field.
It tells us about the *structure* of the score (concentration, sector count, diversification
ratio, UCITS compliance, risk/return trade-off), not about which stocks to buy.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .ucits import check_ucits

CRITERIA = ["gross", "risk_adj", "hhi", "sectors", "div_ratio", "ucits"]

NAMED_SCENARIOS: dict[str, list[float]] = {
    "gross-only": [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "gross-70%": [0.70, 0.10, 0.05, 0.05, 0.05, 0.05],
    "performance-heavy": [0.40, 0.20, 0.10, 0.10, 0.10, 0.10],
    "balanced": [1 / 6] * 6,
    "structure-heavy": [0.15, 0.15, 0.20, 0.20, 0.20, 0.10],
}


@dataclass
class SimConfig:
    n_stocks: int = 150
    n_sectors: int = 10
    days: int = 110  # ~29 Oct 2026 -> 9 Apr 2027
    n_worlds: int = 150
    field_size: int = 400
    n_weight_draws: int = 200
    signal_rho: float = 0.20  # corr(signal, true alpha); ~0.05 realised IC over the game
    market_vol: float = 0.15
    sector_vol: float = 0.08
    seed: int = 7


@dataclass
class World:
    returns: np.ndarray  # days x assets (stocks, sector ETFs, broad ETF)
    sector: np.ndarray  # asset -> sector id
    is_etf: np.ndarray
    signal: np.ndarray  # observable ex ante score (stocks only; ETFs get 0)
    beta: np.ndarray
    idio_vol: np.ndarray
    n_stocks: int


def simulate_world(rng: np.random.Generator, cfg: SimConfig) -> World:
    n, s, d = cfg.n_stocks, cfg.n_sectors, cfg.days
    sector = rng.integers(0, s, n)
    beta = rng.uniform(0.6, 1.4, n)
    idio = rng.uniform(0.15, 0.35, n)
    true_alpha = rng.normal(0.0, 0.10, n)  # annual
    mkt = rng.normal(0.05 / 252, cfg.market_vol / np.sqrt(252), d)
    sec = rng.normal(0.0, cfg.sector_vol / np.sqrt(252), (d, s))
    r = (
        mkt[:, None] * beta[None, :]
        + sec[:, sector]
        + rng.normal(0.0, 1.0, (d, n)) * (idio / np.sqrt(252))[None, :]
        + true_alpha[None, :] / 252
    )
    etf_cols = []
    for k in range(s):
        members = np.where(sector == k)[0]
        etf_cols.append(r[:, members].mean(axis=1) if len(members) else np.zeros(d))
    etf_cols.append(r.mean(axis=1))
    R = np.column_stack([r] + etf_cols)
    a_sector = np.concatenate([sector, np.arange(s), [s]])
    is_etf = np.concatenate([np.zeros(n, bool), np.ones(s + 1, bool)])
    z = (true_alpha - true_alpha.mean()) / true_alpha.std()
    sig = cfg.signal_rho * z + np.sqrt(1 - cfg.signal_rho**2) * rng.normal(size=n)
    signal = np.concatenate([sig, np.zeros(s + 1)])
    beta_all = np.concatenate([beta, np.ones(s + 1)])
    idio_all = np.concatenate([idio, np.zeros(s + 1)])
    return World(R, a_sector, is_etf, signal, beta_all, idio_all, n)


def portfolio_criteria(w: np.ndarray, world: World) -> np.ndarray:
    """Raw values of the six criteria for NAV-fraction weights ``w`` (higher = better, except hhi)."""
    R = world.returns
    pr = R @ w
    gross = float(np.prod(1.0 + pr) - 1.0)
    sd = pr.std(ddof=1)
    sharpe = float(pr.mean() / sd * np.sqrt(252)) if sd > 0 else 0.0
    held = w > 1e-12
    wi = w[held]
    h = float(np.sum((wi / wi.sum()) ** 2))
    sectors = float(len(set(world.sector[held])))
    sub = R[:, held]
    cov = np.cov(sub, rowvar=False)
    cov = np.atleast_2d(cov)
    vols = np.sqrt(np.clip(np.diag(cov), 0, None))
    pv = float(wi @ cov @ wi)
    dr = float(wi @ vols / np.sqrt(pv)) if pv > 0 else 1.0
    ser = pd.Series(w[held], index=[f"a{i}" for i in np.where(held)[0]])
    etfs = [f"a{i}" for i in np.where(held & world.is_etf)[0]]
    ucits = 1.0 if check_ucits(ser, etfs=etfs).compliant else 0.0
    return np.array([gross, sharpe, h, sectors, dr, ucits])


def _field(rng: np.random.Generator, world: World, size: int) -> np.ndarray:
    """Competitor portfolios: gamblers, typical, diversified, ETF-heavy (IC = 0)."""
    n = world.n_stocks
    n_assets = world.returns.shape[1]
    hi_vol = np.argsort(-world.idio_vol[:n])[: int(n * 0.3)]
    out = np.zeros((size, n_assets))
    kinds = rng.choice(4, size=size, p=[0.25, 0.40, 0.20, 0.15])
    for i, k in enumerate(kinds):
        cash = rng.uniform(0, 0.2)
        if k == 0:  # concentrated, high-vol
            m = int(rng.integers(2, 7))
            idx = rng.choice(hi_vol, m, replace=False)
            w = rng.dirichlet(np.ones(m)) * (1 - cash * 0.5)
        elif k == 1:
            m = int(rng.integers(6, 16))
            idx = rng.choice(n, m, replace=False)
            w = rng.dirichlet(np.full(m, 2.0)) * (1 - cash)
        elif k == 2:
            m = int(rng.integers(15, 41))
            idx = rng.choice(n, m, replace=False)
            w = rng.dirichlet(np.full(m, 5.0)) * (1 - cash * 0.5)
        else:  # ETF-heavy
            m_etf = int(rng.integers(1, 4))
            etf_idx = n + rng.choice(world.returns.shape[1] - n, m_etf, replace=False)
            m_st = int(rng.integers(0, 8))
            st_idx = rng.choice(n, m_st, replace=False) if m_st else np.array([], int)
            idx = np.concatenate([etf_idx, st_idx]).astype(int)
            frac_etf = rng.uniform(0.4, 0.8) if m_st else 1.0
            w = np.concatenate(
                [rng.dirichlet(np.ones(m_etf)) * frac_etf]
                + ([rng.dirichlet(np.ones(m_st)) * (1 - frac_etf)] if m_st else [])
            ) * (1 - cash)
        out[i, idx] = w
    return out


# --- strategies: functions (world, rng) -> weights --------------------------------------

def _top(world: World, score: np.ndarray, k: int, per_sector: int | None = None) -> np.ndarray:
    n = world.n_stocks
    order = np.argsort(-score[:n])
    picked: list[int] = []
    counts: dict[int, int] = {}
    for i in order:
        sec = int(world.sector[i])
        if per_sector is not None and counts.get(sec, 0) >= per_sector:
            continue
        picked.append(int(i))
        counts[sec] = counts.get(sec, 0) + 1
        if len(picked) == k:
            break
    return np.array(picked)


def strategy_original_plan(world: World, rng: np.random.Generator) -> np.ndarray:
    """40% ETFs, 8 stocks at 5%, 2 tactical at 5%, 10% cash (the first draft of the plan)."""
    n = world.n_stocks
    w = np.zeros(world.returns.shape[1])
    broad = world.returns.shape[1] - 1
    sec_etfs = n + rng.choice(world.returns.shape[1] - n - 1, 2, replace=False)
    w[broad], w[sec_etfs[0]], w[sec_etfs[1]] = 0.20, 0.10, 0.10
    w[_top(world, world.signal, 10)] = 0.05
    return w


def strategy_concentrated(k: int) -> Callable[[World, np.random.Generator], np.ndarray]:
    def f(world: World, rng: np.random.Generator) -> np.ndarray:
        w = np.zeros(world.returns.shape[1])
        w[_top(world, world.signal, k)] = 0.96 / k
        return w
    return f


def strategy_alpha(
    k: int = 22, cap: float = 0.06, beta_tilt: float = 0.0, per_sector: int = 3
) -> Callable[[World, np.random.Generator], np.ndarray]:
    """Breadth-constrained book: top-k by signal (+ optional beta tilt), tilted weights, 4% cash."""
    def f(world: World, rng: np.random.Generator) -> np.ndarray:
        n = world.n_stocks
        zb = (world.beta[:n] - world.beta[:n].mean()) / world.beta[:n].std()
        score = np.concatenate([world.signal[:n] + beta_tilt * zb, np.zeros(world.returns.shape[1] - n)])
        idx = _top(world, score, k, per_sector)
        raw = 1.0 + 0.25 * np.clip(score[idx], -2, 2)
        w_sel = raw / raw.sum() * 0.96
        w_sel = np.minimum(w_sel, cap)
        w_sel = w_sel / w_sel.sum() * 0.96
        w_sel = np.minimum(w_sel, cap)
        w = np.zeros(world.returns.shape[1])
        w[idx] = w_sel
        s = pd.Series(w[idx], index=[f"a{i}" for i in idx])
        from .ucits import repair_ucits
        w[idx] = repair_ucits(s).to_numpy()
        return w
    return f


STRATEGIES: dict[str, Callable[[World, np.random.Generator], np.ndarray]] = {
    "A. Piano originale (40% ETF, 10% cash)": strategy_original_plan,
    "B. Concentrato 6 titoli": strategy_concentrated(6),
    "C. Concentrato 12 titoli": strategy_concentrated(12),
    "D. Alpha-22 (cap 6%, 4% cash)": strategy_alpha(22, 0.06, 0.0),
    "E. Alpha-22 + tilt beta": strategy_alpha(22, 0.06, 0.5),
    "F. Alpha-30 diversificato": strategy_alpha(30, 0.05, 0.0, per_sector=4),
    "G. Alpha-24 (cap 5.5%)": strategy_alpha(24, 0.055, 0.0, per_sector=3),
}


def _pct_rank(field_vals: np.ndarray, x: float, higher_better: bool = True) -> float:
    if higher_better:
        return float((np.sum(field_vals < x) + 0.5 * np.sum(field_vals == x)) / len(field_vals))
    return float((np.sum(field_vals > x) + 0.5 * np.sum(field_vals == x)) / len(field_vals))


def run_simulation(cfg: SimConfig | None = None, strategies=None) -> pd.DataFrame:
    """Return a table of rank statistics per strategy."""
    cfg = cfg or SimConfig()
    strategies = strategies or STRATEGIES
    rng = np.random.default_rng(cfg.seed)
    weight_draws = rng.dirichlet(np.ones(6), size=cfg.n_weight_draws)
    scen = {k: np.array(v) for k, v in NAMED_SCENARIOS.items()}
    pct_all: dict[str, list[float]] = {k: [] for k in strategies}
    pct_scen: dict[str, dict[str, list[float]]] = {k: {s: [] for s in scen} for k in strategies}
    crit_pct: dict[str, list[np.ndarray]] = {k: [] for k in strategies}

    for _ in range(cfg.n_worlds):
        world = simulate_world(rng, cfg)
        field_w = _field(rng, world, cfg.field_size)
        fc = np.array([portfolio_criteria(w, world) for w in field_w])  # M x 6
        # per-criterion percentile of each field member inside the field
        order_sign = np.array([1, 1, -1, 1, 1, 1], float)
        field_p = np.column_stack(
            [pd.Series(fc[:, j] * order_sign[j]).rank(pct=True).to_numpy() for j in range(6)]
        )
        for name, fn in strategies.items():
            w = fn(world, rng)
            c = portfolio_criteria(w, world)
            p = np.array(
                [_pct_rank(fc[:, j], c[j], higher_better=(order_sign[j] > 0)) for j in range(6)]
            )
            crit_pct[name].append(p)
            ours = weight_draws @ p  # K
            field_scores = field_p @ weight_draws.T  # M x K
            pct_all[name].extend((field_scores < ours[None, :]).mean(axis=0).tolist())
            for sname, sw in scen.items():
                fs = field_p @ sw
                pct_scen[name][sname].append(float((fs < p @ sw).mean()))

    rows = []
    for name in strategies:
        arr = np.array(pct_all[name])
        cp = np.mean(crit_pct[name], axis=0)
        row = {
            "strategy": name,
            "mean_percentile": arr.mean(),
            "P(top 5%)": (arr >= 0.95).mean(),
            "P(top 1%)": (arr >= 0.99).mean(),
        }
        for sname in scen:
            row[f"pct_{sname}"] = float(np.mean(pct_scen[name][sname]))
            row[f"top5_{sname}"] = float(np.mean(np.array(pct_scen[name][sname]) >= 0.95))
        for j, c in enumerate(CRITERIA):
            row[f"crit_{c}"] = float(cp[j])
        rows.append(row)
    return pd.DataFrame(rows).set_index("strategy")

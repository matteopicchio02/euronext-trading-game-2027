import numpy as np
import pandas as pd
import pytest

from alpha import metrics as m
from alpha.optimizer import optimize_weights, scores_to_alpha
from alpha.report import portfolio_snapshot, to_markdown
from alpha.risk_governor import Mode, decide_mode
from alpha.screener import composite_score, price_factors, select_universe, zscore
from alpha.sizing import shares_for_risk, weight_for_risk
from alpha.synthetic import synthetic_prices
from alpha.ucits import check_ucits

SECTORS = {f"T{i:02d}": f"S{i % 10}" for i in range(50)}


@pytest.fixture(scope="module")
def prices():
    return synthetic_prices(list(SECTORS), SECTORS, days=520, seed=3)


def test_zscore_mean_zero_unit_std():
    z = zscore(pd.Series(np.arange(100.0)))
    assert z.mean() == pytest.approx(0, abs=1e-9)
    assert z.std(ddof=0) == pytest.approx(1, abs=0.1)  # winsorising trims the tails


def test_score_bounds_and_selection_breadth(prices):
    table = composite_score(price_factors(prices))
    assert table["score"].between(0, 100).all()
    picks = select_universe(table["score"], SECTORS, n=24, max_per_sector=3, min_sectors=9)
    assert len(picks) == 24 and len(set(picks)) == 24
    assert len({SECTORS[t] for t in picks}) >= 9
    counts = pd.Series([SECTORS[t] for t in picks]).value_counts()
    assert counts.max() <= 3


def test_optimizer_respects_constraints(prices):
    table = composite_score(price_factors(prices))
    picks = select_universe(table["score"], SECTORS, n=24)
    rets = m.simple_returns(prices[picks])
    cov = rets.cov() * 252
    vol = pd.Series(np.sqrt(np.diag(cov)), index=cov.index)
    alpha = scores_to_alpha(table.loc[picks, "composite_z"], vol)
    w = optimize_weights(alpha, cov, sector_map=SECTORS, invested=0.96)
    assert w.sum() <= 0.96 + 1e-6
    assert w.max() <= 0.06 + 1e-6
    assert check_ucits(w).compliant
    sec_w = m.sector_weights(w, SECTORS)
    assert sec_w.max() <= 0.25 + 1e-3


def test_snapshot_and_markdown(prices):
    w = pd.Series(0.04, index=list(SECTORS)[:24])
    snap = portfolio_snapshot(w, prices, SECTORS)
    assert snap["n_positions"] == 24
    assert snap["ucits_ok"]
    assert snap["hhi"] == pytest.approx(1 / 24)
    assert "UCITS 5/10/40 check | PASS" in to_markdown(snap)


def test_governor_modes():
    assert decide_mode(0.14, 0.5, 100).mode == Mode.DEFENSE
    assert decide_mode(0.09, 0.5, 100).mode == Mode.CAUTION
    assert decide_mode(0.02, 0.99, 10).mode == Mode.LOCK_IN
    assert decide_mode(0.02, 0.40, 30).mode == Mode.ATTACK
    assert decide_mode(0.02, 0.40, 100).mode == Mode.NEUTRAL
    assert decide_mode(0.02, None, 30).mode == Mode.NEUTRAL
    # the attack budget never breaks the UCITS single-name ceiling
    assert decide_mode(0.02, 0.40, 30).max_weight <= 0.10


def test_sizing():
    assert shares_for_risk(50_000, 0.005, entry=100, stop=90) == 25
    assert weight_for_risk(0.005, 0.10) == pytest.approx(0.05)
    assert weight_for_risk(0.005, 0.05) == pytest.approx(0.06)  # capped
    with pytest.raises(ValueError):
        shares_for_risk(50_000, 0.005, entry=100, stop=110)

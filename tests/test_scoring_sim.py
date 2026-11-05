import numpy as np

from alpha.scoring_sim import STRATEGIES, SimConfig, portfolio_criteria, run_simulation, simulate_world


def test_criteria_known_portfolio():
    cfg = SimConfig(n_stocks=40, days=60)
    world = simulate_world(np.random.default_rng(1), cfg)
    w = np.zeros(world.returns.shape[1])
    w[:20] = 0.05
    gross, sharpe, hhi, sectors, dr, ucits = portfolio_criteria(w, world)
    assert abs(hhi - 1 / 20) < 1e-9
    assert ucits == 1.0
    assert dr >= 1.0
    assert 1 <= sectors <= cfg.n_sectors


def test_single_stock_fails_ucits_and_has_hhi_one():
    world = simulate_world(np.random.default_rng(2), SimConfig(n_stocks=40, days=60))
    w = np.zeros(world.returns.shape[1])
    w[0] = 1.0
    c = portfolio_criteria(w, world)
    assert c[2] == 1.0 and c[5] == 0.0


def test_simulation_runs_and_orders_structure():
    cfg = SimConfig(n_worlds=12, field_size=120, n_weight_draws=40, seed=11)
    res = run_simulation(cfg)
    assert set(res.index) == set(STRATEGIES)
    assert res["mean_percentile"].between(0, 1).all()
    # a 6-name book cannot be UCITS compliant, a 24-name book is
    assert res.loc["B. Concentrato 6 titoli", "crit_ucits"] < res.loc["G. Alpha-24 (cap 5.5%)", "crit_ucits"]

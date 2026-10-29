import numpy as np
import pandas as pd
import pytest

from alpha import metrics as m


def test_hhi_equal_weights_is_one_over_n():
    assert m.hhi(np.full(20, 0.05)) == pytest.approx(1 / 20)
    assert m.effective_n(np.full(20, 0.05)) == pytest.approx(20)


def test_hhi_single_position_is_one_and_cash_ignored_when_normalised():
    assert m.hhi([1.0]) == pytest.approx(1.0)
    assert m.hhi([0.5, 0.0]) == pytest.approx(1.0)
    # raw NAV fractions: 50% in one name -> 0.25
    assert m.hhi([0.5], normalize=False) == pytest.approx(0.25)


def test_max_drawdown_known_path():
    nav = pd.Series([1.0, 1.2, 0.9, 1.1, 0.8, 1.3])
    assert m.max_drawdown(nav) == pytest.approx(1 - 0.8 / 1.2)


def test_max_drawdown_monotonic_up_is_zero():
    assert m.max_drawdown(pd.Series([1.0, 1.1, 1.2])) == 0.0


def test_volatility_scaling():
    r = pd.Series([0.01, -0.01] * 50)
    assert m.annualized_volatility(r) == pytest.approx(r.std(ddof=1) * np.sqrt(252))


def test_diversification_ratio_perfect_correlation_is_one():
    vols = np.array([0.2, 0.3])
    cov = np.outer(vols, vols)  # corr = 1
    assert m.diversification_ratio([0.5, 0.5], cov) == pytest.approx(1.0)


def test_diversification_ratio_uncorrelated_equal_vol():
    cov = np.diag([0.04, 0.04])
    assert m.diversification_ratio([0.5, 0.5], cov) == pytest.approx(np.sqrt(2))


def test_risk_contributions_sum_to_one():
    cov = pd.DataFrame([[0.04, 0.01], [0.01, 0.09]], index=["a", "b"], columns=["a", "b"])
    rc = m.risk_contributions(pd.Series({"a": 0.6, "b": 0.4}), cov)
    assert rc.sum() == pytest.approx(1.0)


def test_sector_count_ignores_zero_weights():
    w = pd.Series({"a": 0.5, "b": 0.5, "c": 0.0})
    sectors = {"a": "X", "b": "Y", "c": "Z"}
    assert m.sector_count(w, sectors) == 2


def test_sharpe_zero_vol_is_nan():
    assert np.isnan(m.sharpe_ratio(pd.Series([0.01] * 10)))


def test_portfolio_returns_cash_earns_zero():
    r = pd.DataFrame({"a": [0.10, 0.10]})
    pr = m.portfolio_returns(r, pd.Series({"a": 0.5}))
    assert pr.iloc[0] == pytest.approx(0.05)

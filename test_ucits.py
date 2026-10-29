import pandas as pd
import pytest

from alpha.ucits import check_ucits, min_positions_fully_invested, repair_ucits


def test_equal_weight_20_names_is_compliant():
    w = pd.Series(0.05, index=[f"s{i}" for i in range(20)])
    assert check_ucits(w).compliant


def test_single_name_above_10_fails():
    w = pd.Series({"a": 0.12, "b": 0.88 / 20 * 20})
    assert not check_ucits(w).compliant


def test_aggregate_above_5_percent_over_40_fails():
    w = pd.Series([0.08] * 6 + [0.01] * 5, index=list("abcdefghijk"))  # 48% in names > 5%
    rep = check_ucits(w)
    assert not rep.compliant
    assert rep.sum_above_threshold == pytest.approx(0.48)


def test_etf_cap_is_separate_from_issuer_cap():
    w = pd.Series({"ETF": 0.18, "a": 0.05})
    assert check_ucits(w, etfs=["ETF"]).compliant
    assert not check_ucits(pd.Series({"ETF": 0.25}), etfs=["ETF"]).compliant


def test_repair_makes_weights_compliant_and_preserves_budget_when_room():
    w = pd.Series([0.07] * 10 + [0.045] * 6, index=[f"s{i}" for i in range(16)])
    fixed = repair_ucits(w)
    assert check_ucits(fixed).compliant
    assert fixed.sum() <= w.sum() + 1e-9


def test_min_positions_values():
    assert min_positions_fully_invested(1.0, 0.10) == 16
    assert min_positions_fully_invested(0.96, 0.06) == 18

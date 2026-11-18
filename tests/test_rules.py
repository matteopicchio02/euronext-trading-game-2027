from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from alpha import metrics as m
from alpha.rules import check_individual_thresholds, format_report, ranking_date_report

DATA = Path(__file__).resolve().parents[1] / "data"


def _sectors(n: int, k: int) -> dict[str, str]:
    return {f"s{i}": f"sec{i % k}" for i in range(n)}


def test_thresholds_pass_for_diversified_book():
    w = pd.Series(0.05, index=[f"s{i}" for i in range(19)])
    checks = check_individual_thresholds(w, _sectors(19, 8))
    assert all(c.passed for c in checks)


def test_too_few_names_and_sectors_fail():
    w = pd.Series(0.1, index=[f"s{i}" for i in range(8)])
    by_name = {c.name: c for c in check_individual_thresholds(w, _sectors(8, 3))}
    assert not by_name["Securities held"].passed
    assert not by_name["Sectors covered"].passed
    assert by_name["Largest position"].passed


def test_single_position_above_15_percent_fails():
    w = pd.Series([0.16] + [0.06] * 14, index=[f"s{i}" for i in range(15)])
    by_name = {c.name: c for c in check_individual_thresholds(w, _sectors(15, 6))}
    assert not by_name["Largest position"].passed


def test_etf_counts_as_security_but_adds_no_sector():
    w = pd.Series([0.05] * 9 + [0.05], index=[f"s{i}" for i in range(9)] + ["ETF"])
    sec = _sectors(9, 3)
    by_name = {c.name: c for c in check_individual_thresholds(w, sec, etfs=["ETF"])}
    assert by_name["Securities held"].passed and by_name["Securities held"].value == "10"
    assert by_name["Sectors covered"].value == "3"


def test_portfolio_v1_passes_ranking_date_report():
    pf = pd.read_csv(DATA / "portfolio_v1.csv")
    wl = pd.read_csv(DATA / "watchlist.csv")
    sectors = dict(zip(wl.yahoo_ticker, wl.sector))
    checks = ranking_date_report(pf.set_index("ticker")["weight"], sectors)
    text = format_report(checks)
    assert text.startswith("NextWise diversification guidance (NOT official ETG certification): PASS")
    assert all(c.passed for c in checks)


def test_ex_ante_volatility_matches_single_asset_weekly_std():
    idx = pd.bdate_range("2023-01-02", periods=900)
    rng = np.random.default_rng(3)
    px = pd.DataFrame({"A": 100 * np.cumprod(1 + rng.normal(0, 0.01, len(idx)))}, index=idx)
    weekly = px.resample("W-FRI").last().pct_change().dropna().tail(180)
    expected = float(weekly["A"].std(ddof=1) * np.sqrt(52))
    got = m.ex_ante_volatility(px, pd.Series({"A": 1.0}), weeks=180)
    assert got == pytest.approx(expected, rel=1e-9)


def test_history_weeks_flags_young_listings():
    idx = pd.bdate_range("2024-01-01", periods=300)
    px = pd.DataFrame({"OLD": np.linspace(10, 12, 300), "NEW": np.nan}, index=idx)
    px.loc[idx[-60:], "NEW"] = 5.0
    hw = m.history_weeks(px)
    assert hw["OLD"] > hw["NEW"] >= 10


def test_risk_adjusted_performance():
    assert m.risk_adjusted_performance(0.06, 0.15) == pytest.approx(0.4)
    assert np.isnan(m.risk_adjusted_performance(0.06, 0.0))

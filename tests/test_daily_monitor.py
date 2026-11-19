"""Offline regression tests for the daily monitor. No Yahoo/network connection."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import json

import numpy as np
import pandas as pd
import pytest

from scripts.daily_portfolio_monitor import (
    FX_TICKER, build_estimate, extract_field, read_inputs, save_report
)

ROOT = Path(__file__).resolve().parents[1]
ROME = ZoneInfo("Europe/Rome")


def fake_prices(tickers):
    dates = pd.bdate_range("2025-08-01", "2026-11-19")
    rng = np.random.default_rng(123)
    raw = {}
    adj = {}
    for i, t in enumerate(tickers):
        series = 100 * np.cumprod(
            1 + rng.normal(0.0002 + i * 0.00001, 0.003 + i * 0.00004, len(dates))
        )
        if t.endswith(".OL"):
            series = series * 4.0
        raw[t] = series
        adj[t] = series.copy()
    raw[FX_TICKER] = np.linspace(10.8, 11.0, len(dates))
    adj[FX_TICKER] = raw[FX_TICKER].copy()
    return pd.DataFrame(raw, index=dates), pd.DataFrame(adj, index=dates)


def test_snapshot_config_is_reconciled_and_read_only():
    config, p = read_inputs(ROOT / "data/monitor_config.json")
    assert config["read_only"] is True
    assert len(p) == 21
    assert abs(p.market_value_eur.sum() + config["cash_eur"] - config["anchor_nav_eur"]) < .01


def test_monitor_anchor_and_eurnok_are_handled_correctly(tmp_path):
    config, p = read_inputs(ROOT / "data/monitor_config.json")
    raw, adj = fake_prices(p.ticker.tolist())
    base, _ = build_estimate(
        config, p, raw.loc[: "2026-11-18"], adj.loc[: "2026-11-18"],
        datetime(2026, 11, 18, 22, tzinfo=ROME),
    )
    assert base["estimated_nav_eur"] == pytest.approx(50164.75, abs=.001)
    result, positions = build_estimate(
        config, p, raw, adj, datetime(2026, 11, 19, 22, tzinfo=ROME)
    )
    assert result["quote_date"] == "2026-11-19"
    assert result["holdings_count"] == 21
    assert result["risk_history_sessions"] >= 180
    assert result["annualized_volatility_pct"] > 0
    assert result["diversification_ratio"] > 0
    assert result["cash_weight_pct"] == pytest.approx(
        config["cash_eur"] / result["estimated_nav_eur"] * 100
    )
    assert positions.estimated_value_eur.sum() + config["cash_eur"] == pytest.approx(
        result["estimated_nav_eur"]
    )
    eq = positions.set_index("ticker").loc["EQNR.OL"]
    t = "EQNR.OL"
    expected = (
        raw.loc["2026-11-19", t] / raw.loc["2026-11-18", t] *
        raw.loc["2026-11-18", FX_TICKER] / raw.loc["2026-11-19", FX_TICKER]
    )
    assert eq.anchor_relative_factor == pytest.approx(expected)
    save_report(result, positions, tmp_path)
    assert (tmp_path / "2026-11-19.md").exists()
    text = (tmp_path / "latest.md").read_text(encoding="utf-8")
    assert "NOT a NextWise statement" in text
    assert "No orders" in text
    assert len(pd.read_csv(tmp_path / "latest_positions.csv")) == 21
    stored = json.loads((tmp_path / "latest_summary.json").read_text())
    assert stored["status"] == "ESTIMATE_ONLY_NO_TRADE_RECONCILIATION"


def test_stale_prices_fail_closed():
    config, p = read_inputs(ROOT / "data/monitor_config.json")
    raw, adj = fake_prices(p.ticker.tolist())
    with pytest.raises(ValueError, match="Stale or incomplete"):
        build_estimate(config, p, raw, adj, datetime(2026, 11, 20, 22, tzinfo=ROME))


def test_missing_ticker_or_fx_fails_closed():
    config, p = read_inputs(ROOT / "data/monitor_config.json")
    raw, adj = fake_prices(p.ticker.tolist())
    with pytest.raises(ValueError, match="missing one or more"):
        build_estimate(config, p, raw.drop(columns=[FX_TICKER]), adj,
                       datetime(2026, 11, 19, 22, tzinfo=ROME))


def test_mismatched_snapshot_nav_fails(tmp_path):
    old = json.loads((ROOT / "data/monitor_config.json").read_text())
    old["anchor_nav_eur"] += 1000.0
    f = tmp_path / "bad.json"
    f.write_text(json.dumps(old))
    with pytest.raises(ValueError, match="do not reconcile"):
        read_inputs(f)


def test_yahoo_multiindex_extractor_both_directions():
    ix = pd.date_range("2026-11-18", periods=2)
    cols = pd.MultiIndex.from_tuples([
        ("Close", "A.PA"), ("Close", FX_TICKER),
        ("Adj Close", "A.PA"), ("Adj Close", FX_TICKER)
    ])
    frame = pd.DataFrame([[10., 11., 9.9, 11.], [11., 11.2, 10.8, 11.2]],
                         index=ix, columns=cols)
    got = extract_field(frame, "Close", ["A.PA", FX_TICKER])
    assert list(got.columns) == ["A.PA", FX_TICKER]
    assert got.loc[ix[-1], "A.PA"] == 11.0
    reverse = frame.copy()
    reverse.columns = pd.MultiIndex.from_tuples(
        [(t, field) for field, t in frame.columns]
    )
    got2 = extract_field(reverse, "Adj Close", ["A.PA", FX_TICKER])
    assert got2.loc[ix[-1], "A.PA"] == 10.8

"""Offline tests for the independently scheduled 23-position market price study."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import pytest

from scripts.holdings_market_watch import (
    FX_TICKER,
    analyze_quotes,
    read_watch_inputs,
    save_watch_report,
)

ROOT = Path(__file__).resolve().parents[1]
ROME = ZoneInfo("Europe/Rome")


def make_sample():
    config, positions = read_watch_inputs(ROOT / "data/market_watch_config.json")
    morning = pd.read_csv(
        ROOT / "data/portfolio_actual_2026-11-20.csv"
    ).set_index("ticker")
    dates = pd.bdate_range("2025-09-01", "2026-11-23")
    base_date = dates.get_loc(pd.Timestamp("2026-11-20"))
    rng = np.random.default_rng(739)
    raw = {}
    adj = {}
    for i, row in enumerate(positions.itertuples()):
        t = row.ticker
        if t in morning.index:
            base = float(morning.loc[t, "local_quoted_price"])
        elif t == "AD.AS":
            base = 34.3
        elif t == "UNA.AS":
            base = 58.4
        else:
            raise AssertionError(f"Unknown mock ticker: {t}")
        if not np.isfinite(base) or base <= 0:
            raise AssertionError(f"Bad test price for {t}: {base}")
        path = np.exp(np.cumsum(rng.normal(0, 0.0035 + i * 0.00004, len(dates))))
        path *= base / path[base_date]
        raw[t] = path
        adj[t] = path.copy()
    fx = np.linspace(10.8, 10.73, len(dates))
    raw[FX_TICKER] = fx
    adj[FX_TICKER] = fx.copy()
    return (
        config,
        positions,
        pd.DataFrame(raw, index=dates),
        pd.DataFrame(adj, index=dates),
    )


def test_watch_uses_23_reported_quantities_and_frozen_cash():
    cfg, p, *_ = make_sample()
    q = p.set_index("ticker").quantity
    assert len(p) == 23
    assert q.loc["DSY.PA"] == 60
    assert q.loc["AD.AS"] == 25
    assert q.loc["UNA.AS"] == 20
    assert q.loc["EQNR.OL"] == 49
    assert cfg["read_only"] is True
    assert cfg["cash_eur_assumed_unchanged"] == pytest.approx(8336.86)
    assert cfg["official_nav_anchor_eur"] == pytest.approx(49322.18)


def test_market_move_math_and_currency_conversion(tmp_path):
    cfg, positions, prices, adjusted = make_sample()
    result, marks = analyze_quotes(
        cfg, positions, prices, adjusted, datetime(2026, 11, 23, 21, tzinfo=ROME)
    )
    assert result["holdings_count"] == 23
    assert result["quote_date"] == "2026-11-23"
    assert result["status"] == "MARKET_DATA_ESTIMATE_NOT_NEXTWISE"
    assert result["annualized_volatility_pct_model"] > 0
    assert result["risk_history_sessions"] >= 180
    assert result["indicative_nav_from_dated_nextwise_anchor_eur"] == pytest.approx(
        49322.18 + marks.delta_since_anchor_eur.sum()
    )
    assert result["yahoo_direct_nav_eur"] == pytest.approx(
        marks.value_eur_yahoo.sum() + 8336.86
    )
    eq = marks.set_index("ticker").loc["EQNR.OL"]
    today = prices.loc["2026-11-23"]
    base = prices.loc["2026-11-20"]
    assert eq.close_eur == pytest.approx(
        today["EQNR.OL"] / today[FX_TICKER]
    )
    assert eq.delta_since_anchor_eur == pytest.approx(
        49 * (today["EQNR.OL"] / today[FX_TICKER] -
              base["EQNR.OL"] / base[FX_TICKER])
    )
    save_watch_report(result, marks, tmp_path)
    assert (tmp_path / "2026-11-23.md").exists()
    report = (tmp_path / "latest.md").read_text()
    assert "NOT NextWise" in report
    assert "does **not** place" in report
    assert len(pd.read_csv(tmp_path / "latest_positions.csv")) == 23


def test_no_new_nextwise_trades_can_be_inferred_from_prices():
    cfg, p, raw, adj = make_sample()
    cfg = {**cfg, "official_nav_anchor_eur": 49322.18}
    result, _ = analyze_quotes(
        cfg, p, raw, adj, datetime(2026, 11, 23, 21, tzinfo=ROME)
    )
    assert result["share_quantities_frozen_after_user_report"]
    assert result["last_observed_nextwise_nav_eur"] == 49322.18
    assert result["indicative_nav_from_dated_nextwise_anchor_eur"] != 49322.18


def test_stale_and_incomplete_provider_data_are_rejected():
    cfg, p, raw, adj = make_sample()
    with pytest.raises(ValueError, match="Stale price panel"):
        analyze_quotes(cfg, p, raw, adj, datetime(2026, 11, 24, 21, tzinfo=ROME))
    with pytest.raises(ValueError, match="Missing raw quote"):
        analyze_quotes(
            cfg, p, raw.drop(columns=["AD.AS"]), adj,
            datetime(2026, 11, 23, 21, tzinfo=ROME)
        )
    with pytest.raises(ValueError, match="Stale price panel"):
        analyze_quotes(
            cfg, p, raw.iloc[:-1], adj.iloc[:-1],
            datetime(2026, 11, 23, 21, tzinfo=ROME)
        )


def test_intraday_price_spike_is_not_silently_accepted():
    cfg, p, raw, adj = make_sample()
    bad = raw.copy()
    bad.loc["2026-11-23", "DSY.PA"] *= 2.0
    with pytest.raises(ValueError, match="Suspicious daily move"):
        analyze_quotes(cfg, p, bad, adj, datetime(2026, 11, 23, 21, tzinfo=ROME))


def test_unreconciled_trade_forces_watch_to_stop(tmp_path):
    config, *_ = make_sample()
    config["manual_account_events_after_anchor"] = True
    path = tmp_path / "market_watch_config.json"
    import json
    path.write_text(json.dumps(config))
    with pytest.raises(ValueError, match="Unreconciled account event"):
        read_watch_inputs(path)

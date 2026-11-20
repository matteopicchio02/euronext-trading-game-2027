"""Offline invariants for the user-reported DSY execution and pending Ahold order."""
from pathlib import Path
import json
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_executed_sell_is_in_quantity_only_ledger_but_pending_buy_is_not():
    pos = pd.read_csv(ROOT / "data/positions_after_execution_2026-11-20.csv")
    morning = pd.read_csv(ROOT / "data/portfolio_actual_2026-11-20.csv")
    assert len(pos) == len(morning) == 21
    assert pos["ticker"].is_unique
    assert set(pos.ticker) == set(morning.ticker)
    assert pos.set_index("ticker").loc["DSY.PA", "quantity_after_user_report"] == 60
    assert pos.set_index("ticker").loc["DSY.PA", "quantity_at_2026_11_20_0955"] == 90
    assert pos.change_from_user_confirmed_execution.sum() == -30
    assert "AD.AS" not in set(pos.ticker)
    assert all(pos.mark_to_market_status == "NO_CURRENT_POST_TRADE_NAV_OR_MARKS_VERIFIED")


def test_order_events_and_cash_scenario_are_not_confused_with_verified_nav():
    events = pd.read_csv(ROOT / "data/trade_events_2026-11-20.csv").set_index("ticker")
    ds = events.loc["DSY.PA"]
    ad = events.loc["AD.AS"]
    assert ds.status == "EXECUTED_USER_CONFIRMED"
    assert ds.quantity == 30
    assert ds.execution_price_eur == pytest.approx(22.68)
    assert ds.gross_eur == pytest.approx(680.40)
    assert ad.status == "PENDING_USER_CONFIRMED"
    assert ad.order_limit_eur == pytest.approx(34.30)
    assert ad.quantity == 25
    assert pd.isna(ad.execution_price_eur)
    assert 9675.76 + ds.gross_eur == pytest.approx(10356.16)


def test_stale_nav_reporting_gate_is_closed():
    gate = json.loads((ROOT / "data/monitor_reconciliation_gate.json").read_text())
    assert gate["paused"] is True
    assert gate["read_only"] is True
    assert "2026-11-20" == gate["as_of"]

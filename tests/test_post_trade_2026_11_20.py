"""Offline invariants for the 20-Nov confirmed DSY, Ahold and Unilever executions."""
from pathlib import Path
import json
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_all_three_user_confirmed_trades_in_post_fill_quantity_ledger():
    pos = pd.read_csv(ROOT / "data/positions_after_buys_2026-11-20.csv")
    morning = pd.read_csv(ROOT / "data/portfolio_actual_2026-11-20.csv")
    assert len(pos) == 23 and len(morning) == 21
    assert pos["ticker"].is_unique
    assert set(pos.ticker) == set(morning.ticker) | {"AD.AS", "UNA.AS"}
    d = pos.set_index("ticker")
    assert d.loc["DSY.PA", "quantity_after_user_report"] == 60
    assert d.loc["DSY.PA", "quantity_at_2026_11_20_0955"] == 90
    assert d.loc["AD.AS", "quantity_after_user_report"] == 25
    assert d.loc["UNA.AS", "quantity_after_user_report"] == 20
    assert pos.change_from_user_confirmed_execution.sum() == 15
    assert all(pos.mark_to_market_status.notna())


def test_order_events_and_cash_scenario_are_not_confused_with_verified_nav():
    events = pd.read_csv(ROOT / "data/trade_events_2026-11-20.csv").set_index("ticker")
    ds = events.loc["DSY.PA"]
    ad = events.loc["AD.AS"]
    assert ds.status == "EXECUTED_USER_CONFIRMED"
    assert ds.quantity == 30
    assert ds.execution_price_eur == pytest.approx(22.75)
    assert ds.gross_eur == pytest.approx(682.50)
    assert ad.status == "EXECUTED_USER_CONFIRMED_PRICE_UNVERIFIED"
    assert ad.order_limit_eur == pytest.approx(34.30)
    assert ad.quantity == 25
    assert pd.isna(ad.execution_price_eur)
    una = events.loc["UNA.AS"]
    assert una.status == "EXECUTED_USER_CONFIRMED_PRICE_UNVERIFIED"
    assert una.quantity == 20
    assert una.order_limit_eur == pytest.approx(58.40)
    assert pd.isna(una.execution_price_eur)
    assert 9675.76 + ds.gross_eur == pytest.approx(10358.26)
    assert 10358.26 - 8336.86 == pytest.approx(2021.40)
    assert (25 * 34.30 + 20 * 58.40) - 2021.40 == pytest.approx(4.10)


def test_stale_nav_reporting_gate_is_closed():
    gate = json.loads((ROOT / "data/monitor_reconciliation_gate.json").read_text())
    assert gate["paused"] is True
    assert gate['dsy_execution_reconciliation']['reconciliation_gap_eur'] == pytest.approx(0.0)
    assert gate["read_only"] is True
    assert "2026-11-20" == gate["as_of"]
    assert gate["pending_orders"] == []
    assert gate["latest_observed_post_sale_summary"]["nav_eur"] == pytest.approx(49322.18)
    assert len(gate["executed_buy_orders_user_confirmed"]) == 2

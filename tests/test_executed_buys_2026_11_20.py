"""Fail-closed accounting checks: DSY executed, AD and UNA executed per participant.

Order quantities derive from previously confirmed tickets. Unobserved individual
buy fill prices or per-name marks must NOT be manufactured from total cash.
"""
from pathlib import Path
import json
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def test_23_distinct_instruments_and_user_reported_quantities():
    p = pd.read_csv(DATA / "positions_after_buys_2026-11-20.csv").set_index("ticker")
    assert len(p) == 23
    assert p.index.is_unique
    assert p.loc["DSY.PA", "quantity_after_user_report"] == 60
    assert p.loc["AD.AS", "quantity_after_user_report"] == 25
    assert p.loc["UNA.AS", "quantity_after_user_report"] == 20
    assert p.loc["DSY.PA", "change_from_user_confirmed_execution"] == -30
    assert p.loc["AD.AS", "change_from_user_confirmed_execution"] == 25
    assert p.loc["UNA.AS", "change_from_user_confirmed_execution"] == 20
    assert (p["quantity_after_user_report"] > 0).all()
    assert not p["mark_to_market_status"].isna().any()


def test_buys_executed_but_individual_fill_prices_missing():
    events = pd.read_csv(DATA / "trade_events_2026-11-20.csv").set_index("ticker")
    assert events.loc["DSY.PA", "status"] == "EXECUTED_USER_CONFIRMED"
    assert events.loc["AD.AS", "status"] == "EXECUTED_USER_CONFIRMED_PRICE_UNVERIFIED"
    assert events.loc["UNA.AS", "status"] == "EXECUTED_USER_CONFIRMED_PRICE_UNVERIFIED"
    assert pd.isna(events.loc["AD.AS", "execution_price_eur"])
    assert pd.isna(events.loc["UNA.AS", "execution_price_eur"])
    assert pd.isna(events.loc["AD.AS", "gross_eur"])
    assert pd.isna(events.loc["UNA.AS", "gross_eur"])
    assert events.loc["DSY.PA", "execution_price_eur"] == pytest.approx(22.75)


def test_screen_nav_cash_and_combined_limit_arithmetic():
    n = pd.read_csv(DATA / "nextwise_nav_snapshots.csv")
    before = n[(n.local_date == "2026-11-20") & (n.local_time == "13:55")].iloc[0]
    after = n[(n.local_date == "2026-11-20") & (n.local_time == "18:05")].iloc[0]
    assert after.nav_eur == pytest.approx(49322.18)
    assert after.securities_eur == pytest.approx(40985.32)
    assert after.cash_eur == pytest.approx(8336.86)
    assert after.securities_eur + after.cash_eur == pytest.approx(after.nav_eur)
    assert before.cash_eur - after.cash_eur == pytest.approx(2021.40)
    max_notional = 25 * 34.30 + 20 * 58.40
    assert max_notional == pytest.approx(2025.50)
    assert max_notional - (before.cash_eur - after.cash_eur) == pytest.approx(4.10)
    assert after.nav_eur - before.nav_eur == pytest.approx(5.65)


def test_stale_nav_monitor_paused_but_ahold_not_pending():
    gate = json.loads((DATA / "monitor_reconciliation_gate.json").read_text())
    assert gate["paused"] is True
    assert len(gate["pending_orders"]) == 0
    assert sorted(x["ticker"] for x in gate["executed_buy_orders_user_confirmed"]) == ["AD.AS", "UNA.AS"]
    watch = json.loads((DATA / "price_review_levels_2026-11-20.json").read_text())
    ad = next(x for x in watch["rules"] if x["ticker"] == "AD.AS")
    assert ad["held_in_portfolio_reported"] is True
    assert ad["pending_order_user_reported"] is False

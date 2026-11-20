"""Offline tests for rule-driven candidate reviews; no Yahoo or NextWise calls."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import pytest

from scripts.watchlist_price_review import load_rules, review_prices, report_text, save

ROOT=Path(__file__).resolve().parents[1]
ROME=ZoneInfo("Europe/Rome")


def sample():
    config=load_rules(ROOT/"data/price_review_levels_2026-11-19.json")
    dates=pd.to_datetime(["2026-11-18","2026-11-19"])
    closes=pd.DataFrame({"AD.AS":[34.8,34.25],"INGA.AS":[28.3,28.70]},index=dates)
    return config,closes


def test_current_quotes_stay_in_wait_mode(tmp_path):
    config,closes=sample()
    r=review_prices(config,closes,datetime(2026,11,19,22,tzinfo=ROME))
    assert r["quote_date"]=="2026-11-19"
    assert all(row["status"]=="WAIT" for row in r["entries"])
    assert "NOT OFFICIAL NEXTWISE" in report_text(r)
    save(r,tmp_path)
    assert (tmp_path/"2026-11-19.md").exists()
    assert "WAIT" in (tmp_path/"latest.md").read_text()


def test_review_level_is_not_buy_signal():
    config,closes=sample()
    closes.loc["2026-11-19","AD.AS"]=32.95
    r=review_prices(config,closes,datetime(2026,11,19,22,tzinfo=ROME))
    assert r["entries"][0]["status"]=="REVIEW_FUNDAMENTALS"
    assert r["entries"][1]["status"]=="WAIT"
    assert "do not place an order" in report_text(r)


def test_stale_quote_rejected():
    config,closes=sample()
    with pytest.raises(ValueError,match="Stale prices"):
        review_prices(config,closes,datetime(2026,11,20,22,tzinfo=ROME))


def test_missing_symbol_rejected():
    config,closes=sample()
    with pytest.raises(ValueError,match="Missing review ticker"):
        review_prices(config,closes.drop(columns=["INGA.AS"]),datetime(2026,11,19,22,tzinfo=ROME))


def test_user_reported_held_ahold_order_never_generates_new_buy_signal():
    config = load_rules(ROOT / "data/price_review_levels_2026-11-20.json")
    _, closes = sample()
    closes.loc["2026-11-19", "AD.AS"] = 32.95
    result = review_prices(config, closes, datetime(2026, 11, 19, 22, tzinfo=ROME))
    ad = result["entries"][0]
    assert ad["status"] == "HELD_POSITION_MONITOR"
    assert ad["reported_held_quantity"] == 25
    assert ad["reported_pending_quantity"] is None
    assert "not a fresh buy entry" in report_text(result).lower()
    assert result["entries"][1]["status"] == "WAIT"


def test_pending_and_held_cannot_be_active_together():
    config, closes = sample()
    config["rules"][0]["held_in_portfolio_reported"] = True
    config["rules"][0]["reported_held_quantity"] = 25
    config["rules"][0]["pending_order_user_reported"] = True
    with pytest.raises(ValueError, match="simultaneously"):
        review_prices(config, closes, datetime(2026, 11, 19, 22, tzinfo=ROME))


def test_pending_input_fails_closed_when_limit_missing():
    config, closes = sample()
    config["rules"][0]["pending_order_user_reported"] = True
    with pytest.raises(ValueError, match="positive reported quantity"):
        review_prices(config, closes, datetime(2026, 11, 19, 22, tzinfo=ROME))

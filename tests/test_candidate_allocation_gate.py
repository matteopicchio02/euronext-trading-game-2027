"""Offline regression suite: five-candidate portfolio-level risk calculations."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.candidate_allocation_gate import (
    evaluate_candidates, last_complete_snapshot, read_csv, markdown_table
)

ROOT = Path(__file__).resolve().parents[1]
HISTORY = json.loads((ROOT/"data/candidate_risk_inputs_2026-11-18.json").read_text(encoding="utf-8"))
HOLDINGS = read_csv(ROOT/"data/portfolio_actual_2026-11-18.csv")

# Preserve historical scenario expectations against a FIXED official screenshot.
# The production calculation itself always uses the latest complete screenshot.
FROZEN_19_NOV_SNAPSHOT = {
    "observed_at_rome": "2026-11-19T14:03:09+01:00",
    "nav_eur": 49875.21,
    "equities_eur": 40199.45,
    "cash_eur": 9675.76,
}



def _rows(ticket=1000.0):
    return evaluate_candidates(FROZEN_19_NOV_SNAPSHOT, HISTORY, HOLDINGS, ticket_eur=ticket)


def test_base_anchor_and_complete_manual_nextwise_snapshot():
    snapshot = last_complete_snapshot()
    assert snapshot["observed_at_rome"]
    assert snapshot["nav_eur"] > 0
    assert snapshot["cash_eur"] >= 0
    assert snapshot["equities_eur"] + snapshot["cash_eur"] == pytest.approx(snapshot["nav_eur"])


def test_reproduces_previous_analytical_risk_gate():
    rows = _rows()
    assert [r["ticker"] for r in rows] == ["AD.AS", "ENEL.MI", "ASML.AS", "INGA.AS", "SU.PA"]
    by = {r["ticker"]:r for r in rows}
    assert by["AD.AS"]["base_vol_pct"] == pytest.approx(9.0438578, abs=1e-5)
    assert by["AD.AS"]["post_trade_vol_pct"] == pytest.approx(9.1884, abs=.00015)
    assert by["INGA.AS"]["post_trade_vol_pct"] == pytest.approx(9.2946, abs=.00015)
    assert by["ASML.AS"]["post_trade_diversification_ratio"] == pytest.approx(2.3476, abs=.0001)
    assert by["AD.AS"]["max_ticket_eur_at_risk_budget"] == pytest.approx(1036, abs=2)
    assert by["INGA.AS"]["max_ticket_eur_at_risk_budget"] == pytest.approx(608, abs=2)
    assert by["INGA.AS"]["hypothetical_return_hurdle_pct"] == pytest.approx(8.30, abs=.03)
    assert by["INGA.AS"]["post_trade_cash_pct"] == pytest.approx(17.39, abs=.01)
    text=markdown_table(rows,FROZEN_19_NOV_SNAPSHOT,HISTORY)
    assert "OFFLINE" in text and "NOT a forecast" in text


def test_invalid_cash_budget_and_snapshot_rejected():
    snap=last_complete_snapshot()
    with pytest.raises(ValueError,match="Ticket"):
        evaluate_candidates(snap,HISTORY,HOLDINGS,ticket_eur=snap["cash_eur"]+1)
    invalid=dict(snap)
    invalid["nav_eur"] -= 200
    with pytest.raises(ValueError,match="Invalid official screenshot"):
        evaluate_candidates(invalid,HISTORY,HOLDINGS)


def test_corrupted_holding_values_rejected():
    holdings=[dict(x) for x in HOLDINGS]
    holdings[0]["market_value_eur"]="0"
    with pytest.raises(ValueError,match="not aligned"):
        evaluate_candidates(last_complete_snapshot(),HISTORY,holdings)

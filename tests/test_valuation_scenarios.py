"""Pure offline checks of Ahold / ING EPS-multiple scenarios."""
import json
from pathlib import Path
import pytest
from scripts.valuation_scenarios import build_scenarios, markdown
from scripts.candidate_allocation_gate import read_csv, last_complete_snapshot

ROOT=Path(__file__).resolve().parents[1]
ASSUMPTIONS=json.loads((ROOT/"data/scenario_assumptions_AHOLD_ING_2026-11-19.json").read_text(encoding="utf-8"))
RISK=json.loads((ROOT/"data/candidate_risk_inputs_2026-11-18.json").read_text(encoding="utf-8"))
HOLDINGS=read_csv(ROOT/"data/portfolio_actual_2026-11-18.csv")


def test_reproduce_expected_scenarios():
    snap=last_complete_snapshot()
    results=build_scenarios(ASSUMPTIONS,RISK,HOLDINGS,snap)
    assert {x["ticker"] for x in results}=={"AD.AS","INGA.AS"}
    by={x["ticker"]:x for x in results}
    ahold=by["AD.AS"]
    ing=by["INGA.AS"]
    assert ahold["ticket_eur"]==pytest.approx(996.44)
    assert ing["ticket_eur"]==pytest.approx(573.60)
    assert ahold["current_forward_pe"]==pytest.approx(11.9347,rel=1e-5)
    assert ing["current_forward_pe"]==pytest.approx(9.73193,rel=1e-5)
    assert ahold["illustrative_scenarios"]["bear"]["price_eur"]==pytest.approx(28.605744)
    assert ahold["illustrative_scenarios"]["base"]["price_eur"]==pytest.approx(35.9875)
    assert ahold["illustrative_scenarios"]["bull"]["price_eur"]==pytest.approx(41.19849)
    assert ing["illustrative_scenarios"]["bear"]["price_eur"]==pytest.approx(22.04356)
    assert ing["illustrative_scenarios"]["base"]["price_eur"]==pytest.approx(30.20675)
    assert ing["illustrative_scenarios"]["bull"]["price_eur"]==pytest.approx(37.39743)
    assert ahold["portfolio_vol_after_pct"]==pytest.approx(9.1878,abs=0.0005)
    assert ing["portfolio_vol_after_pct"]==pytest.approx(9.1853,abs=0.0005)
    assert ahold["hypothetical_hurdle_pct"]==pytest.approx(4.78,abs=.03)
    assert ing["hypothetical_hurdle_pct"]==pytest.approx(8.16,abs=.03)
    assert ahold["scenario_weighted_return_pct_NOT_FORECAST"]<ahold["hypothetical_hurdle_pct"]
    assert ing["scenario_weighted_return_pct_NOT_FORECAST"]<ing["hypothetical_hurdle_pct"]
    output=markdown(results,ASSUMPTIONS,snap)
    assert "NOT investment advice" in output
    assert "No trades placed" in output


def test_probabilities_not_calibrated():
    invalid=dict(ASSUMPTIONS)
    invalid["scenario_weights_are_calibrated"]=True
    with pytest.raises(ValueError,match="uncalibrated"):
        build_scenarios(invalid,RISK,HOLDINGS,last_complete_snapshot())


def test_probability_sum_must_be_one():
    invalid=dict(ASSUMPTIONS)
    invalid["probabilities_for_illustration_only"]={"bear":.5,"base":.5,"bull":.5}
    with pytest.raises(ValueError,match="sum to one"):
        build_scenarios(invalid,RISK,HOLDINGS,last_complete_snapshot())


def test_bad_price_rejected():
    invalid=dict(ASSUMPTIONS)
    items=[dict(c) for c in ASSUMPTIONS["candidates"]]
    items[0]["quote_eur"]=0
    invalid["candidates"]=items
    with pytest.raises(ValueError,match="Invalid quote"):
        build_scenarios(invalid,RISK,HOLDINGS,last_complete_snapshot())

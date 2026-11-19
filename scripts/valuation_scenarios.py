#!/usr/bin/env python3
"""Research-only EPS x exit P/E scenario model to 9 Apr 2027.

This tool does NOT retrieve live prices, connect to NextWise, place orders,
or calibrate probabilities. All scenario probabilities and exit multiples
are illustrative analyst choices, not consensus price targets.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from scripts.candidate_allocation_gate import (
    evaluate_candidates, last_complete_snapshot, read_csv
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCENARIOS = ROOT / "data/scenario_assumptions_AHOLD_ING_2026-11-19.json"
DEFAULT_RISK = ROOT / "data/candidate_risk_inputs_2026-11-18.json"
DEFAULT_HOLDINGS = ROOT / "data/portfolio_actual_2026-11-18.csv"

def build_scenarios(config: dict, historical: dict, holdings: list[dict], snapshot: dict) -> list[dict]:
    if config.get("scenario_weights_are_calibrated") is not False:
        raise ValueError("This historical decision gate requires uncalibrated scenario weights")
    weights = config["probabilities_for_illustration_only"]
    keys = ("bear", "base", "bull")
    if set(weights) != set(keys) or any(not (0 <= float(weights[k]) <= 1) for k in keys):
        raise ValueError("Invalid scenario weights")
    if not math.isclose(sum(float(weights[k]) for k in keys), 1.0, abs_tol=1e-9):
        raise ValueError("Illustrative scenario weights must sum to one")
    if config["game_end"] != "2027-04-09":
        raise ValueError("Competition horizon mismatch")
    existing = {c["ticker"] for c in historical["candidates"]}
    results = []
    for item in config["candidates"]:
        ticker = item["ticker"]
        if ticker not in existing:
            raise ValueError(f"Unknown candidate {ticker}")
        quote, eps, shares = map(float, (item["quote_eur"], item["fy2027_consensus_eps_eur"], item["illustrative_shares"]))
        if quote <= 0 or eps <= 0 or shares <= 0 or not shares.is_integer():
            raise ValueError("Invalid quote, EPS or whole-share quantity")
        ticket = shares * quote
        risk = next(x for x in evaluate_candidates(
            snapshot, historical, holdings,
            ticket_eur=ticket,
            hypothetical_base_return_pct=float(config["hypothetical_unmodified_portfolio_return_to_game_end"])*100
        ) if x["ticker"] == ticker)
        if set(item["scenarios"]) != set(keys):
            raise ValueError("Require bull/base/bear scenarios for every candidate")
        scenarios = {}
        weighted_return = 0.0
        for name in keys:
            choice = item["scenarios"][name]
            earnings_factor = float(choice["eps_multiplier"])
            exit_pe = float(choice["exit_pe"])
            if earnings_factor <= 0 or exit_pe <= 0:
                raise ValueError("Non-positive EPS multiplier or P/E")
            eps_hypothetical = eps*earnings_factor
            price_target = eps_hypothetical*exit_pe
            gross_price_return = price_target/quote - 1
            nav_impact_eur = shares*(price_target-quote)
            weighted_return += float(weights[name])*gross_price_return
            scenarios[name] = {
                "eps_assumed": eps_hypothetical,
                "exit_pe_assumed": exit_pe,
                "price_eur": price_target,
                "price_return_pct": gross_price_return*100,
                "position_pnl_eur": nav_impact_eur,
                "nav_impact_pct_points": 100*nav_impact_eur/float(snapshot["nav_eur"]),
                "illustrative_weight": float(weights[name])
            }
        hurdle = risk["hypothetical_return_hurdle_pct"]
        results.append({
            "ticker":ticker, "name":item["name"], "current_quote_eur":quote,
            "fy2027_consensus_eps_eur":eps,
            "current_forward_pe":quote/eps,
            "illustrative_shares":int(shares), "ticket_eur":ticket,
            "ticket_nav_pct":100*ticket/float(snapshot["nav_eur"]),
            "base_portfolio_vol_pct":risk["base_vol_pct"],
            "portfolio_vol_after_pct":risk["post_trade_vol_pct"],
            "vol_change_pp":risk["delta_vol_pp"],
            "risk_budget_limit_eur":risk["max_ticket_eur_at_risk_budget"],
            "hypothetical_hurdle_pct":hurdle,
            "scenario_weighted_return_pct_NOT_FORECAST":100*weighted_return,
            "scenario_weighted_minus_hurdle_pp_NOT_EDGE":100*weighted_return-hurdle,
            "illustrative_scenarios":scenarios,
        })
    return results

def markdown(results: list[dict], config: dict, snapshot: dict) -> str:
    lines=[
        "# Project Alpha — Ahold vs ING: scenario valuation through 9 April 2027", "",
        "> **Scenario laboratory, NOT investment advice, a probabilistic forecast, an official",
        "> NextWise share price or trade authorization. Never execute orders from this script.**",
        "",
        f"Fundamental as-of date: {config['as_of']}; FY2027 analyst EPS estimates are a",
        "working anchor, but **April 2027 market prices are not predictable** from FY2027 EPS alone.",
        f"Official virtual NAV snapshot: EUR {snapshot['nav_eur']:,.2f}, {snapshot['observed_at_rome']}.",
        "Prices are **indicative nonsynchronous intraday observations**.",
        "",
        "| Case | Current price | FY27 EPS | Forward P/E | Shares | Notional | Vol after | Scenario hurdle* |",
        "|---|---:|---:|---:|---:|---:|---:|---:|"
    ]
    for x in results:
        lines.append(
            f"| {x['name']} | EUR {x['current_quote_eur']:.2f} | "
            f"EUR {x['fy2027_consensus_eps_eur']:.3f} | {x['current_forward_pe']:.2f}x | "
            f"{x['illustrative_shares']} | EUR {x['ticket_eur']:,.2f} | "
            f"{x['portfolio_vol_after_pct']:.3f}% | {x['hypothetical_hurdle_pct']:.2f}% |"
        )
    lines += ["",
        "## Three mutually exclusive illustrative exit-price cases", "",
        "| Company | Case | EPS factor vs FY27 consensus | Exit P/E | Implied 9 Apr price |",
        " Gross price return | P&L on illustrative shares | Impact on total Game NAV (pp) |",
        "|---|---|---:|---:|---:|---:|---:|---:|"]
    for x in results:
        for key in ("bear","base","bull"):
            s = x["illustrative_scenarios"][key]
            f = s["eps_assumed"]/x["fy2027_consensus_eps_eur"]
            lines.append(
                f"| {x['name']} | {key} | {f:.2f}x | {s['exit_pe_assumed']:.2f}x | "
                f"EUR {s['price_eur']:.2f} | {s['price_return_pct']:+.2f}% | "
                f"EUR {s['position_pnl_eur']:+.2f} | {s['nav_impact_pct_points']:+.3f} |"
            )
    lines += ["", "## Interpretation and important boundaries", "",
        "These illustrative probabilities **have NOT been fitted to data**. A 25/50/25 arithmetic average is",
        "a sensitivity exercise, not an evidence-based expected return or an estimate of alpha.",
        "No dividends are credited in these price-return scenarios; any distribution requires",
        "NextWise ex-dividend and cash-booking reconciliation.",
        "",
        "*Hurdle: only under an arbitrary +6% expected-return scenario for the original portfolio,",
        "at unchanged covariance/cash. Not an official Euronext score or guaranteed performance.",
        "Buying both names would require their **pairwise covariance**, not obtained by adding",
        "the two single-name vol-change figures.",
        "",
        "The P/E exit multiple is an analyst assumption and not a 12-month broker target.",
        "Any April multiple can differ sharply; FY2027 EPS will still be a forecast at that point.",
        "All share counts, sizes and prices are **hypothetical**. No trades placed.",
        ""
    ]
    return "\n".join(lines)

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--scenarios",type=Path,default=DEFAULT_SCENARIOS)
    p.add_argument("--output",type=Path,help="Optional markdown output; no orders")
    args=p.parse_args()
    config=json.loads(args.scenarios.read_text(encoding="utf-8"))
    risk=json.loads(DEFAULT_RISK.read_text(encoding="utf-8"))
    snap=last_complete_snapshot()
    holds=read_csv(DEFAULT_HOLDINGS)
    result=build_scenarios(config,risk,holds,snap)
    data=markdown(result,config,snap)
    if args.output:
        args.output.parent.mkdir(exist_ok=True,parents=True)
        args.output.write_text(data,encoding="utf-8")
        print(f"Research report written: {args.output}")
    else:
        print(data)

if __name__=="__main__":
    main()

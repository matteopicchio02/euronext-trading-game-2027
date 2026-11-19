#!/usr/bin/env python3
"""OFFLINE decision-support: recalculate matched-cash candidate risk sensitivities.

Requires no network and never connects to NextWise, changes a portfolio, or places an order.
Candidate covariances/momentum are dated research estimates as of 2026-11-18.
Official account NAV/equity/cash come from manually recorded NextWise screenshots.
This script is NOT an independent expected-return forecasting model.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "data/candidate_risk_inputs_2026-11-18.json"
HOLDINGS = ROOT / "data/portfolio_actual_2026-11-18.csv"
SNAPSHOTS = ROOT / "data/nextwise_official_snapshots.csv"


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def last_complete_snapshot(path: Path = SNAPSHOTS) -> dict:
    rows = read_csv(path)
    complete = [r for r in rows if r.get("nav_eur") and r.get("equities_eur") and r.get("cash_eur")]
    if not complete:
        raise ValueError("No complete confirmed NextWise screenshot with NAV/equity/cash")
    result = max(complete, key=lambda r: r["observed_at_rome"])
    for field in ("nav_eur", "equities_eur", "cash_eur"):
        result[field] = float(result[field])
    if abs(result["equities_eur"] + result["cash_eur"] - result["nav_eur"]) > 0.05:
        raise ValueError("The official snapshot NAV does not reconcile")
    return result


def evaluate_candidates(
    snapshot: dict,
    historical: dict,
    holdings: list[dict],
    ticket_eur: float = 1000.0,
    risk_budget_pp: float = 0.15,
    hypothetical_base_return_pct: float = 6.0,
) -> list[dict]:
    """Prospective static-covariance stress, NOT a realized 2026-11-19 position attribution."""
    nav = float(snapshot["nav_eur"])
    equities = float(snapshot["equities_eur"])
    cash = float(snapshot["cash_eur"])
    if ticket_eur <= 0 or ticket_eur > cash or risk_budget_pp <= 0:
        raise ValueError("Ticket must be positive, at most confirmed cash; risk budget must be positive")
    if equities <= 0 or nav <= 0 or abs(equities + cash - nav) > 0.05:
        raise ValueError("Invalid official screenshot values")
    if not holdings or len({h["ticker"] for h in holdings}) != len(holdings):
        raise ValueError("Missing or duplicate holdings")
    held = sum(float(h["market_value_eur"]) for h in holdings)
    if abs(held - float(historical["original_portfolio_equities_eur"])) > 0.05:
        raise ValueError("Holding values and historical covariance weights are not aligned")
    if abs(float(historical["original_portfolio_nav_eur"]) - held - 9675.76) > 0.05:
        raise ValueError("Historical reference NAV does not reconcile to the source screenshot")
    baseline_sigma = (
        float(historical["historical_baseline_volatility_pct"]) / 100.0
        * (equities / nav)
        / (held / float(historical["original_portfolio_nav_eur"]))
    )
    baseline_dr = float(historical["historical_baseline_diversification_ratio"])
    w = ticket_eur / nav
    hhi_base = sum((float(h["market_value_eur"]) / held) ** 2 for h in holdings)
    rows = []
    seen = set()
    for candidate in historical["candidates"]:
        ticker = candidate["ticker"]
        if ticker in seen or any(h["ticker"] == ticker for h in holdings):
            raise ValueError(f"Duplicate/new-position ticker invalid: {ticker}")
        seen.add(ticker)
        sigma_c = float(candidate["candidate_annual_vol_pct"]) / 100
        rho = float(candidate["corr_with_existing_equity_basket"])
        if not (0 < sigma_c < 2 and -1 <= rho <= 1):
            raise ValueError("Invalid covariance summary inputs")
        v = baseline_sigma**2 + (w*sigma_c)**2 + 2*baseline_sigma*w*sigma_c*rho
        if v <= 0 or not math.isfinite(v):
            raise ValueError("Invalid modeled variance")
        after = math.sqrt(v)
        dr = (baseline_dr*baseline_sigma + w*sigma_c) / after
        hhinew = (equities/(equities+ticket_eur))**2 * hhi_base + (ticket_eur/(equities+ticket_eur))**2
        # Solve sigma_new = baseline_sigma + risk_budget_pp/100.
        target = baseline_sigma + risk_budget_pp / 100
        a = sigma_c*sigma_c
        b = 2*baseline_sigma*sigma_c*rho
        c = baseline_sigma**2-target**2
        max_w = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        max_ticket = min(cash, nav*max_w)
        hurdle = (hypothetical_base_return_pct/100)*(after/baseline_sigma-1)/w
        rows.append({
            "ticker": ticker, "company": candidate["name"],
            "momentum_3m_pct": float(candidate["mom3_pct"]),
            "momentum_6m_pct": float(candidate["mom6_pct"]),
            "standalone_vol_pct": sigma_c*100, "correlation_to_existing_stocks": rho,
            "base_vol_pct": baseline_sigma*100,
            "post_trade_vol_pct": after*100,
            "delta_vol_pp": (after-baseline_sigma)*100,
            "post_trade_diversification_ratio": dr,
            "post_trade_hhi_equity": hhinew,
            "max_ticket_eur_at_risk_budget": max_ticket,
            "hypothetical_return_hurdle_pct": hurdle*100,
            "post_trade_cash_pct": (cash-ticket_eur)/nav*100,
            "ticket_eur": ticket_eur,
            "risk_budget_pp": risk_budget_pp,
            "hypothetical_base_return_pct": hypothetical_base_return_pct,
        })
    return sorted(rows, key=lambda x: x["post_trade_vol_pct"])


def markdown_table(items: list[dict], snapshot: dict, historical: dict) -> str:
    if not items:
        raise ValueError("No candidates")
    lines = [
        "# Project Alpha — Five-candidate allocation sensitivity (OFFLINE)",
        "",
        "> Research estimate; NOT NextWise NAV, live prices, official Euronext score,",
        "> expected-return forecast, trade permission or order execution.",
        "",
        f"**Latest fully specified official screenshot:** {snapshot['observed_at_rome']}. "
        f"NAV EUR {snapshot['nav_eur']:,.2f}; equity EUR {snapshot['equities_eur']:,.2f}; "
        f"cash EUR {snapshot['cash_eur']:,.2f}.",
        f"**Historical candidate price cutoff:** {historical['historical_price_date']}. "
        "Existing individual holdings have been uniformly rescaled to the latest overall equity value, "
        "so true day-specific risk contributions are not identified.",
        "",
        f"**Matched cash-funded ticket per candidate:** EUR {items[0]['ticket_eur']:,.2f}; "
        f"base annualized volatility: {items[0]['base_vol_pct']:.4f}%.",
        "",
        "| Candidate | 3m momentum | 6m momentum | Vol after | Δ vol (pp) | DR after | "
        f"Max ticket with +{items[0]['risk_budget_pp']:.2f}pp* | Scenario required gain** |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for x in items:
        lines.append(
            f"| {x['company']} ({x['ticker']}) | {x['momentum_3m_pct']:+.2f}% | "
            f"{x['momentum_6m_pct']:+.2f}% | {x['post_trade_vol_pct']:.4f}% | "
            f"+{x['delta_vol_pp']:.4f} | {x['post_trade_diversification_ratio']:.4f} | "
            f"EUR {x['max_ticket_eur_at_risk_budget']:,.0f} | "
            f"{x['hypothetical_return_hurdle_pct']:.2f}% |"
        )
    lines += [
        "",
        f"*{items[0]['risk_budget_pp']:.2f} volatility percentage points is an internal, illustrative research budget; "
        "actual share rounding and FX can alter it.",
        f"**The required gain assumes, hypothetically, a +{items[0]['hypothetical_base_return_pct']:.2f}% return for the unmodified portfolio "
        "through April 9, 2027 and asks what new-stock return would keep a simple return/volatility "
        "ratio unchanged. It is NOT a forecast or a fair-value price target.",
        "",
        "No trade is authorized by this output. Confirm live NextWise position count, "
        "valuation, dividends, next earnings, company guidance and price before revisiting.",
    ]
    return "\n".join(lines)+"\n"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--candidates", type=Path, default=CANDIDATES)
    p.add_argument("--holdings", type=Path, default=HOLDINGS)
    p.add_argument("--snapshots", type=Path, default=SNAPSHOTS)
    p.add_argument("--ticket-eur", type=float, default=1000)
    p.add_argument("--risk-budget-pp", type=float, default=.15)
    p.add_argument("--hypothetical-base-return-pct", type=float, default=6)
    p.add_argument("--output", type=Path, help="Optional report markdown path (never sends orders)")
    args=p.parse_args()
    hist=json.loads(args.candidates.read_text(encoding="utf-8"))
    snap=last_complete_snapshot(args.snapshots)
    rows=evaluate_candidates(snap,hist,read_csv(args.holdings),args.ticket_eur,args.risk_budget_pp,args.hypothetical_base_return_pct)
    report=markdown_table(rows,snap,hist)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(report,encoding="utf-8")
        print(f"Research memo written to: {args.output}")
    else:
        print(report)


if __name__=="__main__":
    main()

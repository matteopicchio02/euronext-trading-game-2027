# Project Alpha 2027 — Documentation index

Research project for the virtual Euronext Trading Game. The **current 18 November 2026 snapshot** is distinct from the original 26-name draft and from the older November 4 historical notebooks.

## Governance
- [Investment Policy](governance/INVESTMENT_POLICY.md): self-imposed policy targets and documented exceptions
- [Verified vs working rules](governance/RULES_VERIFIED.md): official sources, NextWise guidance, unresolved questions
- [**Canonical Decision Log**](governance/DECISION_LOG.md): decisions and follow-ups
- [**18 November 2026 Committee Memo**](governance/DECISION_2026-11-18.md): risk/return trade-off and HOLD decision
- [Five-candidate risk and catalyst gate — 19 November](governance/CANDIDATE_SELECTION_2026-11-19.md): Ahold, ING, ASML, Enel and Schneider matched-ticket comparison; no order authorization
- [Prospective Ahold vs ING valuation — 19 November](governance/VALUATION_AHOLD_ING_2026-11-19.md): FY2027 EPS × P/E scenarios, risks, downside and decision gate
- [19 November trading desk plan](governance/TRADING_PLAN_2026-11-19.md): conditional price review levels and reasons for no trade
- [Post-close Ahold/ING price review](../.github/workflows/candidate_price_review.yml): checks prices and publishes research-only statuses, **never orders**
- [Scenario Python source](../scripts/valuation_scenarios.py) · [explicit assumptions](../data/scenario_assumptions_AHOLD_ING_2026-11-19.json): transparent, offline, no trading
- [Reproducible candidate gate (Python)](../scripts/candidate_allocation_gate.py): recalculates risk sensitivities from [dated research inputs](../data/candidate_risk_inputs_2026-11-18.json) and [official manual snapshots](../data/nextwise_official_snapshots.csv)
- [Chronology since October](governance/PROJECT_TIMELINE_2026.md): prior project milestones, distinct from fills
- [Repository quality audit](governance/REPOSITORY_AUDIT_2026-11-18.md): repairs, CI and open limitations
- [Research run registry](../reports/research/RESEARCH_REGISTER_2026-11-18.md): recorded November 18 models and input provenance

## Quantitative research
- [Methodology](methodology/METHODOLOGY.md): factor and portfolio models, assumptions
- [Research Design](methodology/RESEARCH_DESIGN.md): historical notebooks, selection bias, validation conditions
- [Data Dictionary](methodology/DATA_DICTIONARY.md): columns, sources and valuation conventions
- [Current 21-name audit](../reports/AUDIT_2026-11-18.md)
- [Historical synthetic-simulation report](../reports/backtesting/SIMULATION_RESULTS.md)
- [Historical portfolio-construction notebooks](../notebooks/README.md)

## Monitoring

- [Daily monitoring runbook](monitoring/DAILY_MONITOR.md): post-close schedule, frozen holdings, EUR/NOK valuation, data-quality aborts, manual NextWise reconciliation.
- [Official dated screenshot observations](../data/nextwise_official_snapshots.csv): not mixed with estimated daily Yahoo prices.
- [Daily monitor workflow](../.github/workflows/daily_monitor.yml): GitHub Actions trigger; generated reports appear only after successful external market-data execution.

## Templates
- [Investment memo](templates/INVESTMENT_MEMO_TEMPLATE.md)
- [Decision log template](templates/DECISION_LOG_TEMPLATE.md)
- [Weekly report template](templates/WEEKLY_REPORT_TEMPLATE.md)

## Archival/manual documentation
- [Historical Project Alpha manual](PROJECT_ALPHA_2027_MANUALE_COMPLETO.pdf): created before the current 21-name snapshot; **do not use historical positions as current holdings**.

## Important boundaries
Portfolio and performance values in the project are **virtual**. Model returns, risk estimates and rule checks are not official NextWise scores, nor evidence of trade execution. As of 18 November 2026, there is **no intramonth ranking update**. Full market-history files are kept outside this repository unless explicitly provided with a reproducible provenance.

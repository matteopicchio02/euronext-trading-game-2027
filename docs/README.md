# Project Alpha 2027 — Notes and documentation

These are the notes I'm keeping while working on my first quantitative-finance project as an MSc student. I use them to explain **what I tried, why I tried it, and what I still need to check**.

Some documents use formal finance terms such as *investment memo*, *policy* or *committee decision*. Here they are **learning templates for organising research**, not evidence of professional portfolio-management experience.

## Start here

| If you want to understand… | Read |
|---|---|
| Why I started this project and what works | [Main README](../README.md) |
| The quantitative methods | [Methodology](methodology/METHODOLOGY.md) |
| What can and cannot be reproduced | [Research design and limitations](methodology/RESEARCH_DESIGN.md) |
| Where the numbers come from | [Data dictionary](methodology/DATA_DICTIONARY.md) |
| How I explored the data in Python | [Notebook guide](../notebooks/README.md) |
| How I track real virtual-account changes | [Decision and transaction notes](governance/DECISION_LOG.md) |
| How the 23 stocks are followed automatically | [New 23-holding Market Watch](monitoring/MARKET_WATCH_23.md) |

## 1. Learning portfolio research

- [Research assumptions and personal risk guidelines](governance/INVESTMENT_POLICY.md) — self-imposed targets, not official Euronext restrictions.
- [How I separate competition rules from assumptions](governance/RULES_VERIFIED.md).
- [Historical 18 November decision note](governance/DECISION_2026-11-18.md) — comparison of staying invested versus modelled alternatives.
- [Candidate comparison](governance/CANDIDATE_SELECTION_2026-11-19.md) and [Ahold/ING valuation scenarios](governance/VALUATION_AHOLD_ING_2026-11-19.md).
- [Five-company review](governance/REVIEW_2026-11-20_FIVE_NAMES.md) — an example of connecting company news with portfolio decisions.
- [Project timeline](governance/PROJECT_TIMELINE_2026.md) — the sequence of experiments, observations and virtual transactions.

Older reports sometimes sound like an institutional investment committee because I used that structure to learn investment writing. They should be read as **student research notes**, not actual committee meetings or guaranteed forecasts.

## 2. Python, notebooks and validation

- [Four exploratory notebooks](../notebooks/README.md) — market data, factor screening, portfolio construction and risk.
- [Risk and backtesting methodology](methodology/METHODOLOGY.md).
- [Research-design limitations](methodology/RESEARCH_DESIGN.md), including missing input panels and selection bias.
- [18 November model audit](../reports/AUDIT_2026-11-18.md) and [historical simulations](../reports/backtesting/SIMULATION_RESULTS.md).
- [Model-run register](../reports/research/RESEARCH_REGISTER_2026-11-18.md) and [code-quality review](governance/REPOSITORY_AUDIT_2026-11-18.md).
- [Test suite](../tests/) and [Python modules](../src/alpha/).

A passing Python test means **the tested calculation behaves as expected**, not that the investment strategy will outperform.

## 3. Virtual portfolio tracking

The research changed during November: an initial **26-stock draft**, earlier **17-stock notebook examples**, a **21-position screenshot portfolio**, and finally **23 positions reported after transactions on 20 November**. These are different stages, not inconsistent versions of one live data feed.

- [Latest documented 23-name quantity record](../data/positions_after_buys_2026-11-20.csv) — **quantities only**, not current market values.
- [Virtual order records](../data/trade_events_2026-11-20.csv) — includes which purchase prices are still missing.
- [20 November, 18:05 account reconciliation](../reports/snapshots/EXECUTED_BUYS_2026-11-20_1805.md) — NAV €49,322.18 and cash €8,336.86 at that observation time.
- [Dated account observations](../data/nextwise_nav_snapshots.csv) and [original 21-name snapshot](../data/portfolio_actual_2026-11-18.csv).
- [Decision notes](governance/DECISION_LOG.md) — why a trade was considered and what was actually confirmed.

**Important:** all account values are virtual, dated and manually recorded. They are not continuous market data or a certified performance record.

## 4. Automated checks — and why some are paused

- **[23-holding Market Watch](monitoring/MARKET_WATCH_23.md)**: new independent scheduled check of the currently recorded 23 stocks using public Yahoo prices and EUR/NOK conversion. Provides **indicative**, dated changes and research risk metrics; does not read NextWise or execute orders.
- **[Market Watch GitHub Actions](../.github/workflows/market_watch_23.yml)**: scheduled end-of-day on weekdays. Output appears under [market_watch reports](../reports/market_watch/) **only after a successful run**.

- [Daily portfolio monitor](monitoring/DAILY_MONITOR.md) uses historical public market prices. Its old portfolio baseline is **paused for reconciliation** because holdings changed.
- [Daily-monitor workflow](../.github/workflows/daily_monitor.yml) is not a broker integration.
- [Candidate price-review workflow](../.github/workflows/candidate_price_review.yml) can flag a research level; it **does not place trades**.

## 5. Templates and older material

I use [research memo](templates/INVESTMENT_MEMO_TEMPLATE.md), [decision log](templates/DECISION_LOG_TEMPLATE.md) and [weekly review](templates/WEEKLY_REPORT_TEMPLATE.md) templates to practise writing structured financial analysis.

The [original PDF manual](PROJECT_ALPHA_2027_MANUALE_COMPLETO.pdf) describes an earlier version. It is retained for historical context, not as the current portfolio.

---

**About this repository:** an independent educational project linked to a virtual university competition. The repository is currently publicly visible; dated competition data are included. No affiliation with Euronext, NextWise or any bank is implied. Model output is not investment advice or an official competition score.

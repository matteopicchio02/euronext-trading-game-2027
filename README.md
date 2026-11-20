# Project Alpha 2027
**Independent quantitative portfolio research for the Euronext Trading Game 2026–2027**

Virtual capital: **EUR 50,000 initial allocation** · Individual participation · Competition: **5 October 2026 – 9 April 2027**.

> Independent educational research project, not affiliated with Euronext, NextWise or any financial institution. No real-money trading and **no automatic NextWise order execution**. Historical simulations are *not* the competition's verified performance or score.

## Project status — latest observed NextWise overview: 20 November 2026, 18:05 CET

**User-confirmed virtual trades:** DSY.PA sold **30** shares at EUR **22.75** (60 remain); AD.AS **25 shares bought** and UNA.AS **20 shares bought** (both reported executed). Exact **individual** AD/UNA fill prices have **not** been supplied. The combined decrease in cash since 13:55 is **EUR 2,021.40**, versus the two proposed total limit amounts **EUR 2,025.50**. Do not assign the EUR 4.10 aggregate difference to any individual fill.

| Measure | As observed in NextWise / user-confirmed |
|---|---:|
| NAV | **EUR 49,322.18** |
| Marked equities (aggregate) | **EUR 40,985.32** |
| Cash | **EUR 8,336.86 (16.90% of NAV)** |
| NextWise displayed cumulative performance | **−1.70%** vs its own EUR 50,175.20 reference |
| Equity fraction | **83.10% of NAV** |
| Distinct held tickers | **23**, based on user-confirmed full fills of previous 25- and 20-share buy tickets |
| Positions snapshot | [Post-fill 23-name *quantity* ledger](data/positions_after_buys_2026-11-20.csv) — **no invented individual marks/fill prices** |
| Transaction record | [Confirmed states, with missing individual purchase prices](data/trade_events_2026-11-20.csv) |
| Reconciliation | [20 Nov 18:05 execution/NAV report](reports/snapshots/EXECUTED_BUYS_2026-11-20_1805.md) |

**Automated NAV monitor: on reconciliation hold**, not broken. Its older 18-Nov holdings still assume 90 DSY shares and lack AD/UNA; publishing its estimated current NAV would be misleading. The read-only candidate watcher now treats AD as **HELD_POSITION_MONITOR** rather than as a pending buy. Next step: post-execution ticker-level prices and actual separate AD/UNA fill prices, then resume a validated 23-name market-risk report.

### Historical baseline (NOT the current portfolio)

## Project status — last verified NextWise snapshot: 18 November 2026

| Measure | Snapshot | Evidence |
|---|---:|---|
| NAV | EUR 50,164.75 | NextWise screenshots |
| Invested in equities | EUR 40,488.99 | 21 displayed positions |
| Cash | EUR 9,675.76 (19.29%) | NextWise overview |
| Unrealized P&L across the 21 cards | EUR −10.46 | Sum of displayed per-position P&L; approximate |
| Risk | Annual vol 8.88–9.05%, model-dependent | Historical **research estimates**, not official score |
| Portfolio decision | **HOLD / NO TRADE** | 18 November Investment Committee |

**Do not treat these values as live.** The NAV in the competition overview is different from the initial EUR 50,000 endowment, and the app uses a different performance reference; avoid reconstructing the official result from incomplete transactions. There is no verified live order-feed connection. **Rankings are published at month-end; no current intramonth ranking is available.**

The 26-name file **`data/portfolio_v1.csv` is an archived DRAFT**, not today's holdings. The 21-name screenshot snapshot is in **`data/portfolio_actual_2026-11-18.csv`**; it is not a ledger of executed fills.

## Repository map

| Directory | Contents |
|---|---|
| `src/alpha/` | Reusable risk, screening, UCITS-style proxy, optimization and tournament research |
| `scripts/` | Operational commands and *retrospective* OOS diagnostic; no broker API |
| `data/` | Candidate universe, legacy 26-name draft, 21-name historical snapshot, analyst-input template |
| `tests/` | Pytest regression suite, including snapshot reconciliation and CLI smoke tests |
| `notebooks/` | Four historical research notebooks (mainly **4 November**, not today's live data) |
| `reports/` | 18 November audit and archived simulation results |
| `docs/governance/` | Investment policy, verified vs assumed game rules, **canonical decision log** and committee minutes |
| `docs/methodology/` | Research methods, data dictionary, documented limitations |
| `docs/templates/` | Memo and weekly-report templates |

**Canonical records:** [Decision log](docs/governance/DECISION_LOG.md) · [18 November committee memo](docs/governance/DECISION_2026-11-18.md) · [Project timeline](docs/governance/PROJECT_TIMELINE_2026.md) · [Repository quality audit](docs/governance/REPOSITORY_AUDIT_2026-11-18.md) · [Research run registry](reports/research/RESEARCH_REGISTER_2026-11-18.md) · [Snapshot audit](reports/AUDIT_2026-11-18.md) · [Rules and uncertainty](docs/governance/RULES_VERIFIED.md) · [Data dictionary](docs/methodology/DATA_DICTIONARY.md).

## Quick start (Windows PowerShell / Google Colab)

From the repository root with Python 3.10+:

```powershell
python -m pip install -e ".[dev]"
python -m pytest -q
python scripts/check_compliance.py
# The default checks the 18-Nov snapshot, NOT live positions.
python scripts/check_compliance.py --portfolio data/portfolio_v1.csv --watchlist data/watchlist.csv
# The second command deliberately checks the archived 26-name draft.
```

Offline **synthetic** screen (for functionality testing only):

```powershell
python scripts/run_screen.py --demo
```

Historical OOS diagnostic (requires a CSV you have already generated separately in Colab, with EUR-adjusted returns):

```powershell
python scripts/alpha_oos_validation.py --returns ALPHA_daily_returns.csv --portfolio data/portfolio_actual_2026-11-18.csv
```

The CSV is **not committed**. See [Research methodology](docs/methodology/RESEARCH_DESIGN.md). The OOS exercise retroactively tests an end-date-selected basket and is subject to **selection bias**, even if the rolling estimator avoids using future observations.

Other tools: `scripts/weekly_report.py` requires `--portfolio` and `--prices`; it computes a hypothetical constant-weight historical path, **not actual account P&L**. Market-data downloads additionally require `pip install -e ".[data]"`.

## Daily estimated portfolio monitor (currently on reconciliation hold)

A [GitHub Actions workflow](.github/workflows/daily_monitor.yml) is scheduled on **Monday–Friday, 20:37 UTC** (21:37/22:37 Rome depending on daylight saving), **subject to GitHub schedule availability**. It downloads daily Yahoo prices for the **dated 21-holding snapshot**, calculates a **conditional mark-to-market NAV and historical risk estimate** (including EUR/NOK for Equinor), then archives dated research reports under `reports/daily/`. No NextWise account access, broker API or orders.

Historical reports were computed **as if holdings and EUR 9,675.76 cash were unchanged since 18 Nov 2026**. This is no longer true after 20 Nov confirmed transactions. **The scheduler and CLI are deliberately gated by `data/monitor_reconciliation_gate.json`**, so stale NAV estimates are suppressed. Re-enable only after synchronized 23-name post-fill marks, current cash and buy execution receipts have been reconciled and `data/monitor_config.json` has been updated and tested. The monitor also stops if quotes are missing or stale.

**[Full monitoring guide](docs/monitoring/DAILY_MONITOR.md)** · [Automation run history](https://github.com/matteopicchio02/euronext-trading-game-2027/actions/workflows/daily_monitor.yml) · [Official screenshot observations](data/nextwise_official_snapshots.csv).

The first daily report will appear **only after the first successful post-close run**; successful CI unit tests alone do not prove external Yahoo data retrieval works.

## Decision governance

- The Euronext-published six criteria are gross performance, risk-adjusted performance, HHI, sector coverage, diversification ratio and UCITS compliance. **Official weights and implementation details have not been verified**.
- UCITS 5/10/40, the HHI convention, the 35% Paris-listing cap and the risk governor are **research proxies or house rules**, not claims about official legality or competition eligibility.
- NextWise discusses 10 names / 4 sectors / 15% as diversification guidance; this project's checks do not certify competition eligibility.
- Treat all historical prices and NextWise screenshots as **as-of dated**. Confirm corporate actions, FX and live executable prices before an investment decision.
- Keep each proposed trade in a written memo, log actual fills only after confirmation, and reassess risk and the published rank at month-end.

## Data and public disclosure

The repository is currently **private**. It contains an actual competition snapshot, so do not make it public without deciding which holdings and decision records to disclose. For future CV use, publish sanitized methodology and delayed results as appropriate.

## Licence
MIT.

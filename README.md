# Project Alpha 2027
**Independent quantitative portfolio research for the Euronext Trading Game 2026–2027**

Virtual capital: **EUR 50,000 initial allocation** · Individual participation · Competition: **5 October 2026 – 9 April 2027**.

> Independent educational research project, not affiliated with Euronext, NextWise or any financial institution. No real-money trading and **no automatic NextWise order execution**. Historical simulations are *not* the competition's verified performance or score.

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

**Canonical records:** [Decision log](docs/governance/DECISION_LOG.md) · [18 November committee memo](docs/governance/DECISION_2026-11-18.md) · [Snapshot audit](reports/AUDIT_2026-11-18.md) · [Rules and uncertainty](docs/governance/RULES_VERIFIED.md) · [Data dictionary](docs/methodology/DATA_DICTIONARY.md).

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

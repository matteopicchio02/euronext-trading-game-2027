# My daily portfolio monitor — a Python learning project (no NextWise access)

## What I'm trying to build — and its current status

I built this small workflow to practise **working with dated price data, currency conversion, data checks and portfolio risk calculations**. It is a learning tool, **not** a live trading dashboard.

The original workflow estimates the value and risk of the **21 stocks recorded on 18 November 2026**, assuming their quantities and cash never change. This assumption stopped being valid after the virtual transactions reported on **20 November**, when the account moved to **23 holdings**. For that reason, the automated NAV publication is **currently paused** through a reconciliation check.

The workflow **does not connect to NextWise**, read the actual account, place orders, discover trades or certify Euronext scores. A previously generated estimate remains a historical model result, **not a current balance**.

**Source files:**
- `data/portfolio_actual_2026-11-18.csv`: quantity, sector and **EUR position valuation** from the NextWise cards.
- `data/monitor_config.json`: dated NAV anchor, dated cash amount, position file and mandatory `read_only=true`.
- `data/nextwise_official_snapshots.csv`: manual *official* NextWise observations, never automatically overwritten by market-data estimates.
- `scripts/daily_portfolio_monitor.py`: read-only Yahoo market-data and analytics engine.
- `.github/workflows/daily_monitor.yml`: scheduled/dispatch automation.

## Scheduling

GitHub Actions schedule is `37 20 * * 1-5` **UTC**, normally **21:37 in Rome in winter** and **22:37 in summer**, after most Euronext cash markets close. GitHub schedule executions may be **delayed or skipped**; this is not a real-time alerting service.

To run manually after European markets close:
1. Open this GitHub repository (currently public).
2. Select **Actions** > **Daily Portfolio Monitor (indicative, no orders)**.
3. Select **Run workflow** > branch **main** > **Run workflow**.
4. Open that run. Check the indicator and downloaded `alpha-monitor-...` artifact. On success, the workflow commits changes **only** under `reports/daily/`. 
5. If no report appears, inspect the run logs. **Do not disable the stale/missing-data checks simply to force a green status.**

## What the daily report estimates

- Local daily *raw Close* per instrument and the daily Yahoo `EURNOK=X` spot quote (NOK per EUR) for Equinor.
- For each position: **platform anchor market value** multiplied by the relative change in unadjusted local close since **2026-11-18** (for NOK, also multiplied by anchor/current NOK-per-EUR FX).
- NAV estimate = sum of modeled stock values + **cash frozen at the anchored screenshot**. This is neither the NextWise official NAV nor realized net account P&L.
- NAV weights, equity-normalized HHI, HHI including cash, Paris-listing concentration, sector weights.
- Historical risk using dividend-adjusted daily close returns converted to EUR, sample covariance annualized by 252, annual volatility, Gaussian 95% 1-day VaR and diversification ratio.

**Corporate-action caveat:** raw-price valuation does not add dividends to cash or update share quantities after stock splits. Yahoo prices are a third-party, asynchronous and sometimes revised feed. Manual NextWise records always override model valuations. Some price jumps will require investigation rather than trading actions.

## Data-quality gates (fail closed)

No report is published when:
- One equity or EUR/NOK close is absent, zero or not on the same current-market session.
- The portfolio anchor date lacks historical prices, or dates are stale relative to the scheduled Rome business date.
- Raw/adjusted provider data disagree on their latest common session.
- Holdings have duplicated tickers, invalid quantities, missing sectors or an incoherent initial cash/NAV reconciliation.
- Risk calculations have fewer than 180 shared EUR return observations or an adjusted daily return above 45% requiring investigation.

A red action may be caused by a **local exchange holiday, delayed market-data provider, rate limit or temporary service outage**. Red means **no new valuation can be trusted**; not automatically that the portfolio lost money.

## Report outputs

Successful runs write:
- `reports/daily/YYYY-MM-DD.md` — dated research narrative.
- `reports/daily/positions_YYYY-MM-DD.csv` — estimated positions and research risk contributions.
- `reports/daily/latest.md`, `latest_positions.csv`, `latest_summary.json` — newest successful estimate.

Files appear **only after a successful market-data run**. Historical reports in `reports/daily/` cover earlier dates; they do **not** show the current post-trade portfolio. Passing unit tests alone does not prove live market-data availability or reconcile NextWise cash.

## Local Windows command

From repository root:

```powershell
python -m pip install -e ".[dev,data]"
python -m pytest -q
python scripts/daily_portfolio_monitor.py
```

For a manual, intentionally historical research run, the `--allow-stale` option permits an older synchronized close and **labels its real date**. Do not present it as a live closing quote.

## After a trade or a verified account update

This monitor **does not discover transactions**. If a share quantity, holding or cash changes:

1. Save a new date-stamped NextWise source snapshot/transaction record. Never overwrite `data/portfolio_actual_2026-11-18.csv`.
2. Build a new `data/portfolio_actual_YYYY-MM-DD.csv` with the actual holdings, quantities, EUR positions and documented value source.
3. Reconcile stock values + cash = official NAV; update `data/monitor_config.json` to this **new trading-day price-close anchor**, current cash and NAV.
4. Commit the sources with a dated rationale to `docs/governance/DECISION_LOG.md`.
5. Validate that the new anchor is truly comparable to Yahoo's daily market close; an *intraday* NextWise snapshot must not be treated as an end-of-day close.
6. The next report will model **unchanged holdings since the newly verified date**.

**At the current 23-position stage, the workflow is intentionally gated and does not publish a new NAV estimate.** This is preferable to displaying a plausible-looking but incorrect value.

## Data accuracy, safety and visibility

- **Visibility note:** GitHub currently reports this repository as **public**. It contains dated virtual competition holdings. Review what should remain publicly visible before adding any further account details; GitHub privacy settings are separate from the Python workflow.
- No NextWise login, password, cookie, token or unapproved private API endpoint is used.
- GitHub Actions `contents: write` is used to commit generated reports, not brokerage commands. No NextWise execution code exists.
- The workflow uses Yahoo Finance research quotations and does not constitute an exchange-licensed market data feed.
- The official NextWise ranking updates at month-end; this monitor **does not estimate the user's ranking**.

## Troubleshooting

If a scheduled run fails, open **Actions > Daily Portfolio Monitor > failed run > Estimate holdings using Yahoo daily closes**, and read the exact exception. Common scenarios include a late/holiday market, `yfinance` rate limiting, and corporate actions. If the job succeeds but a commit fails, check that GitHub Actions has appropriate repository write permissions and that `main` is not protected against this workflow's push. Manual consent and proper protection take priority over bypassing branch protections.

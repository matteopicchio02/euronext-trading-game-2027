# Project Alpha 2027 — Research-run register (18 November 2026)
**Status:** completed historical analysis; **no NextWise order placed**. This report preserves the lineage of the 18 November research without confusing simulated and executed performance.

## Source information sets

1. **Real virtual snapshot:** 21 current equities; NAV EUR 50,164.75; invested EUR 40,488.99; cash EUR 9,675.76; card P&L total EUR −10.46; as-of 18 November. Source: `data/portfolio_actual_2026-11-18.csv`, [audit](../AUDIT_2026-11-18.md). No actual fill history is available in the repository.
2. **Original research baseline:** 26-name `data/portfolio_v1.csv`, an unexecuted allocation proposal from October. Not to be substituted for the actual snapshot.
3. **Historical notebook archives:** source notebooks mainly dated 4 November, including an older 17-name comparison; *not* today's 21-name metrics.
4. **Local Colab research inputs:** exported EUR daily returns (517 rows from November 2024 to November 2026), candidate price histories, covariance/correlation matrices. **These files are not included in this GitHub repository**. Actual performance, execution times, price adjustments, dividends and FX booking must be independently reconciled with NextWise.

## Quantitative experiments and snapshots

| Experiment | Snapshot/result | Limitation |
|---|---|---|
| Initial 21-name risk audit | Annualized vol **8.88%**; DR **2.3226**; equity-normalized HHI **0.04969**; 95% daily Gaussian VaR **EUR 461.73** | 517-day price pipeline, normal VaR, not official score |
| Candidate Challenge updated price pipeline | Baseline annualized vol **9.056%**, DR **2.317** | Different data panel; don't compare mechanically with initial vol 8.88% |
| Chronological optimizer holdout | 17 Feb–18 Nov 2026 (197 sessions): base return **18.357%**, 16%-turnover optimization **18.645%**; vols **7.712%** and **7.476%** | Current constituents selected with end-date knowledge: selection bias |
| Rolling 252/63-day retrospective diagnostics | 265 historical sessions: base **22.829%**, 16%-turnover optimized **24.608%** | Daily constant rebalancing, no trading costs/delays, selection bias |
| Five candidate challenge | 5 names: **ASML, ING, Enel, Ahold Delhaize, Schneider Electric**; 20 theoretical scenarios | No buy instruction; price quality and fundamentals not independently signed off |
| Equal-exposure decision gate | Baseline **9.047%** vol / DR **2.318**; three Paris-to-two-candidate alternatives were tested keeping cash 19.29% | 35% Paris cap is an internal listing proxy, not a game rule |
| Equal-exposure holdout | 15 Apr–18 Nov 2026, 150 historical sessions: base return **13.199%**, Ahold+ING **12.334%**, Ahold+Enel **11.728%**, Ahold+ASML **11.972%** | All alternatives failed to improve *historical return*, some improved historical risk; not future performance |

**Equal-exposure 18 Nov risk model details:** Base vol **9.047%**. Ahold for Prysmian (EUR 1,500) **8.914%**, DR **2.280**; Ahold for Michelin **8.949%**, DR **2.335**; Paris→Ahold+ING **8.921%**, DR **2.335**; Paris→Ahold+Enel **8.870%**, DR **2.328**; Paris→Ahold+ASML **8.905%**, DR **2.397**. The latter three satisfy the *internal* 35%-Paris condition with constant cash but require roughly **EUR 6,418** in gross orders; no such orders were placed.

## Data-quality exceptions

The latest candidate diagnostic flagged absolute daily historical moves exceeding 15% in **Dassault Systèmes, Ferrari and UCB**. These are **manual-review flags**, not confirmed bad data. Equinor's historical EUR returns require consistency in the **EUR/NOK** conversion. Timing and corporate-action handling must be validated before trade sizing.

## Investment Committee outcome

**HOLD / NO TRADE** on all 21 holdings. Reasons: inability to demonstrate a robust expected-return/score advantage from the tested replacements; transaction complexity; unverified official score weights; retrospective selection bias. Watchlist and flags are for review, not buy/sell instructions.

- **19 November:** short check of pending orders and material news in NextWise.
- **26–27 November:** pre-month-end guideline and valuation refresh.
- **After month-end publication:** first verified Italian ranking review.

[Official committee minutes](../../docs/governance/DECISION_2026-11-18.md) · [Canonical decision log](../../docs/governance/DECISION_LOG.md) · [Research limitations](../../docs/methodology/RESEARCH_DESIGN.md).

## Reproduction and file inventory

The following supporting exports were produced in the chat's Colab workflow but **not uploaded to GitHub**: `ALPHA_daily_returns.csv`, `ALPHA_covariance_matrix.csv`, `ALPHA_correlation_matrix.csv`, `ALPHA_oos_holdout_results.csv`, `ALPHA_oos_walkforward_aggregate.csv`, `ALPHA_oos_walkforward_folds.csv`, `ALPHA_oos_weights_diagnostic.csv`, `ALPHA_5_candidates_comparison.csv`, `ALPHA_candidate_data_quality.csv`, `ALPHA_equal_exposure_scenarios.csv`, `ALPHA_equal_exposure_holdout_diagnostic.csv`, and `ALPHA_equal_exposure_trades_THEORETICAL.csv`.

To reproduce the available historical OOS model locally, provide a clean **EUR daily-return CSV** explicitly:

```bash
python scripts/alpha_oos_validation.py --returns ALPHA_daily_returns.csv --portfolio data/portfolio_actual_2026-11-18.csv
```

The other candidate/equal-exposure experiments additionally require their original Colab notebooks, historical price inputs and pipeline specifications; their numerical results are **archived as research claims with caveats**, not reproducible from the repository alone.

**Critical nonclaims:** no future winning probability is scientifically established by this analysis; no automatic orders were sent; no official Euronext ranking is known until the monthly release; a checked research rule is **not** certified UCITS or eligibility compliance.

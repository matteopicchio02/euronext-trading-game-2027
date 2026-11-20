# Project Alpha 2027 — Decision Log

This is the chronological record of portfolio decisions for the Euronext Trading Game 2026–2027. Portfolio values are virtual. Log decisions before any order; distinguish proposal, authorization, execution, and review.

| Date | Scope | Decision | Execution | NAV snapshot (EUR) | Rationale | Research memo | Review |
|---|---|---|---|---:|---|---|---|
| 2026-11-18 | 21-equity portfolio | **HOLD / NO TRADE** | **No order placed** | 50,164.75 | Tested alternatives do not demonstrate a sufficiently robust risk-adjusted or total-score advantage; historical return of base portfolio exceeded five studied alternatives in the retrospective holdout | [Investment Committee — 2026-11-18](./DECISION_2026-11-18.md) | Brief review 2026-11-19; month-end compliance 2026-11-26/27; formal ranking assessment after month-end publication |
| 2026-11-19 | 21-equity portfolio; unchanged holdings (user confirmation) | **HOLD / NO TRADE** | **No order requested or placed by Project Alpha** | 49,875.21 | NextWise NAV −289.54 EUR vs 18 Nov; cash unchanged in screenshot; Equinor cyber incident under review with normal production reported; no validated stock-level attribution or superior replacement yet | [Desk review — 2026-11-19](./DECISION_2026-11-19.md), [Five-candidate risk gate](./CANDIDATE_SELECTION_2026-11-19.md), [Ahold–ING scenario valuation](./VALUATION_AHOLD_ING_2026-11-19.md), [19 Nov action plan](./TRADING_PLAN_2026-11-19.md), [21-position loss diagnostic](./PORTFOLIO_DIAGNOSTIC_2026-11-19_1550.md) | After first verified post-close monitor run; monthly ranking when released |
| 2026-11-20 | Complete 21-name snapshot reconciled | **MONITOR / NO NEW ORDER RECOMMENDED** | **No order placed via Project Alpha; NextWise order-history check still open** | 49,519.84 | Between 18 and 20 Nov, NAV −644.91 EUR equals the sum of all 21 marked P&L changes; 21 quantities match and cash 9,675.76 EUR is confirmed. This is not evidence of the absence of round-trip fills; top loss contributors warrant thesis review. | [Full 20-Nov position attribution](../../reports/snapshots/POSITION_ATTRIBUTION_2026-11-20_COMPLETE.md) | Verify order history, dated price catalysts and next synchronized market-close valuation |

| 2026-11-20 | Ahold limit research proposal | **PROPOSED — 25 AD shares at maximum EUR 34.30; not automatically authorized** | **NOT SENT / NO FILL** | 49,519.84 | Small <=EUR 857.50 cash-funded diversification tranche; lower historical marginal risk among five candidates; cybersecurity guidance and pricing remain material risks; do not chase or convert to market order. No past HOLD retroactively reclassified. | [Ahold dated pre-trade memo](./TRADE_PROPOSAL_2026-11-20_AHOLD.md) | User checks ticker/ISIN, current NextWise quote, order validity; confirms executed quantity/price only after actual fill |

| 2026-11-20 | Ahold Delhaize (AD.AS) order submitted by participant | **USER CONFIRMS PENDING ORDER — NO CONFIRMED FILL** | **Pending on NextWise per participant; quantity, entered limit, validity and fill details not independently checked; no order placed by ChatGPT** | 49,519.84 (pre-order snapshot) | Participant first reported a purchase, then clarified that the order is still pending. The proposed ticket was 25 shares at max EUR 34.30, but submitted terms require confirmation. Do not add shares, deduct cash or increase holdings count until execution is verified. | [Pre-trade memo and status updates](./TRADE_PROPOSAL_2026-11-20_AHOLD.md) | Inspect status, entered limit and expiration before weekend; document a genuine partial/full fill or cancellation before updating positions |


## 2026-11-18 snapshot and model state
- 21 equity holdings: EUR 40,488.99; cash: EUR 9,675.76 (19.29%); total NAV: EUR 50,164.75.
- NextWise displayed performance: approximately −0.02% against the application's EUR 50,175.20 reference base (different from initial EUR 50,000 endowment).
- Latest equal-exposure model: volatility 9.047% annualized, diversification ratio 2.318, equity-only HHI 0.04969; alternative earlier estimate of 8.88% uses a different data series and should not be compared directly.
- Paris-listed holdings 41.20% of NAV versus a 35% **internal research-policy** limit, NOT a verified Euronext competition restriction. No automatic liquidation.
- Risk regime: NEUTRAL, pending updated NextWise position/order reconciliation.
- Candidate watchlist: Ahold Delhaize, ING, Enel, ASML, Schneider Electric — research only; no buy authorization.
- Review names: Prysmian, Michelin, Dassault Systèmes and Equinor — further price-adjustment, corporate-action, and catalyst verification needed.

## Outstanding controls
1. Confirm pending orders and real execution state on NextWise.
2. Validate corporate actions, dividend booking, FX treatment and data-quality flags.
3. Confirm official ranking rules where unpublished or ambiguous; ranking is only available at month-end.
4. Revisit investment theses only on material new information; no day-to-day model overfitting.

## Review discipline
Do not infer that the model's minimum-volatility portfolio maximizes official competition score. Document any new trade *before* placing it and append its actual execution price, quantity, timestamp, and subsequent 4-week review when known.

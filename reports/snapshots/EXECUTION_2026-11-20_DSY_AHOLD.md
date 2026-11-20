# Project Alpha — Trade-state reconciliation, 20 November 2026
**As reported by participant in conversation (no NextWise API or direct order-receipt capture).**
**State updated: DSY sale user-confirmed executed; AD buy user-confirmed still pending.**

## Execution and pending order

| Company / ticker | Order | Status | Quantity | Price EUR | Gross EUR | Provenance |
|---|---|---|---:|---:|---:|---|
| Dassault Systèmes DSY.PA | SELL | **EXECUTED, user-confirmed** | 30 shares (previously planned and implicitly confirmed as executed) | **22.75** | **+682.50** | Participant first said 22.68, then explicitly corrected to 22.75; DSY executed per participant; cash increase matches exactly |
| Ahold Delhaize AD.AS | BUY LIMIT | **PENDING, user-confirmed** | 25 | 34.30 max | **0.00 realized** | Participant reports order matching proposed terms and still pending |

The DSY sell quantity of 30 is the order in the immediately preceding confirmed trade plan; no independent screen of the execution receipt has been supplied. If the fill quantity differs, correct this record rather than silently forcing a reconciliation. Only DSY's execution status is affirmed; Ahold is NOT filled.

## Portfolio position state after the DSY fill

- Last verified full **pre-trade** NextWise screenshot: 20 November 2026 09:54–09:55, NAV EUR **49,519.84**, equities EUR **39,844.08**, cash EUR **9,675.76**, DSY **90** shares, 21 holdings.
- **DSY: 90 − 30 = 60 shares** remaining, per participant's execution confirmation and the 30-share submitted plan.
- **Still 21 different actual equity holdings**, because this was only a partial DSY disposal. **Do not include AD.AS** until a genuine partial/full buy fill.
- The other 20 positions are assumed unchanged **only for the transaction-event inventory**; their post-trade prices/marks were **not** refreshed.
- Gross sell proceeds = 30 × EUR 22.75 = **EUR 682.50**.
- **Account cash observed on NextWise after sale**: EUR **10,358.26**. It reconciles: EUR 9,675.76 before + (30 × EUR 22.75) = **EUR 10,358.26**, zero residual; the platform screenshot is now available. Buying power may be reserved against the Ahold pending order. [Post-trade NAV/cash screenshot report](NEXTWISE_POST_DSY_SALE_2026-11-20.md).
- **EUR 82.20** indicative realized book loss if 30 shares originally carried purchase quote EUR **25.49** and no fee adjustments: 30 × (22.75 − 25.49). Actual booked realized P&L remains unverified. Realization does **not** by itself reduce NAV anew; it transforms the existing exposure into cash.
- The **post-trade platform NAV is now directly observed at EUR 49,433.18**, with EUR 39,074.92 equities and EUR 10,358.26 cash. However, no synchronized **post-trade per-security marks or refreshed covariance risk output** can be derived from that account summary alone.

## Execution-control reconciliation — confirmed price exceeds proposed sell floor

The original reported EUR 22.68 was **subsequently corrected by the participant to EUR 22.75**. The proposed SELL LIMIT floor was EUR **22.70**, so the corrected execution price is **EUR 0.05/share above the proposed minimum** (EUR 1.50 on 30 shares), not an execution-quality breach. The post-sale cash increase is **EUR 682.50**, exactly equal to the user-confirmed gross sale proceeds. The order type, fees and timestamp remain unverified without the order receipt.

## Operational next steps

1. **Do not enter another AD.AS buy**: 25 @ 34.30 is already user-reported pending; check status after close and next session.
2. The **post-sale NextWise account summary has been obtained** and reconciled for cash/NAV. For position-level and fee verification, obtain an updated DSY card confirming 60 shares and optionally its order receipt.
3. Update market monitor with a **synchronized** full post-execution holdings/price reference (or explicitly new trade-aware calculation), then re-enable the gated daily estimate. Current scheduled portfolio NAV report is safely **suppressed** while historical 18 Nov frozen quantities are stale. This does not affect the independent price-review workflow for candidates.
4. Before initiating a new sell/buy, ensure orders and cash are reconciled; no additional trade is authorized by this report.

## Reproducible artifacts

- [20 Nov user-reported order/event ledger](../../data/trade_events_2026-11-20.csv)
- [Post-execution quantity-only 21-name inventory](../../data/positions_after_execution_2026-11-20.csv)
- [Pre-trade full marked positions](../../data/portfolio_actual_2026-11-20.csv)
- [Monitor reconciliation gate](../../data/monitor_reconciliation_gate.json)
- [Original DSY trade plan and participant execution updates](../../docs/governance/TRADE_PROPOSAL_2026-11-20_DSY_TRIM.md)
- [Canonical decision log](../../docs/governance/DECISION_LOG.md)

**No trade was submitted by ChatGPT or GitHub. Trading account is virtual; user personally controls NextWise orders.**

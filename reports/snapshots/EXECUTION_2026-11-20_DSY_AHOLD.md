# Project Alpha — Trade-state reconciliation, 20 November 2026
**As reported by participant in conversation (no NextWise API or direct order-receipt capture).**
**State updated: DSY sale user-confirmed executed; AD buy user-confirmed still pending.**

## Execution and pending order

| Company / ticker | Order | Status | Quantity | Price EUR | Gross EUR | Provenance |
|---|---|---|---:|---:|---:|---|
| Dassault Systèmes DSY.PA | SELL | **EXECUTED, user-confirmed** | 30 shares (previously planned and implicitly confirmed as executed) | 22.68 | **+680.40** | Participant: "ho venduto a 22,68" followed by "dassault systems è eseguito l'altro ancora no" |
| Ahold Delhaize AD.AS | BUY LIMIT | **PENDING, user-confirmed** | 25 | 34.30 max | **0.00 realized** | Participant reports order matching proposed terms and still pending |

The DSY sell quantity of 30 is the order in the immediately preceding confirmed trade plan; no independent screen of the execution receipt has been supplied. If the fill quantity differs, correct this record rather than silently forcing a reconciliation. Only DSY's execution status is affirmed; Ahold is NOT filled.

## Portfolio position state after the DSY fill

- Last verified full **pre-trade** NextWise screenshot: 20 November 2026 09:54–09:55, NAV EUR **49,519.84**, equities EUR **39,844.08**, cash EUR **9,675.76**, DSY **90** shares, 21 holdings.
- **DSY: 90 − 30 = 60 shares** remaining, per participant's execution confirmation and the 30-share submitted plan.
- **Still 21 different actual equity holdings**, because this was only a partial DSY disposal. **Do not include AD.AS** until a genuine partial/full buy fill.
- The other 20 positions are assumed unchanged **only for the transaction-event inventory**; their post-trade prices/marks were **not** refreshed.
- Gross sell proceeds = 30 × EUR 22.68 = **EUR 680.40**.
- **Indicative account cash before fees and any unrelated account movement**: EUR 9,675.76 + EUR 680.40 = **EUR 10,356.16**. This is a transaction-ledger estimate, NOT a newly observed cash balance. Available buying power may be reduced by the reserved pending Ahold limit order.
- **EUR 84.30** indicative realized book loss if 30 shares originally carried purchase quote EUR **25.49** and no fee adjustments: 30 × (22.68 − 25.49). Actual booked realized P&L remains unverified. Realization does **not** by itself reduce NAV anew; it transforms the existing exposure into cash.
- No defensible **post-trade official NAV, updated portfolio weights or market-risk model estimate** can be stated without fresh marks and a cash screenshot.

## Execution quality issue

The recorded pre-trade proposal required a **SELL LIMIT of at least EUR 22.70**, while the participant reports **EUR 22.68** execution.
- Difference = EUR **0.02/share**, EUR **0.60 gross** for 30 shares.
- A genuine sell limit at EUR 22.70 would normally not fill at EUR 22.68, excluding complexities such as fees or display conventions.
- Inspect NextWise's actual order **type, entered limit, executed price, fees and receipt**; the difference could reflect a market order, changed limit, displayed price differences or accounting. Do not assert a platform error without the ticket.

## Operational next steps

1. **Do not enter another AD.AS buy**: 25 @ 34.30 is already user-reported pending; check status after close and next session.
2. Obtain one new **post-sale NextWise portfolio summary** including cash, NAV and the updated DSY card with quantity 60. Confirm whether any commissions were charged.
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

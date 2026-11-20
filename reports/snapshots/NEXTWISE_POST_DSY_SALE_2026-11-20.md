# Project Alpha 2027 — NextWise portfolio summary after DSY sale (20 November 2026)

**Source:** user-provided cropped screenshot of NextWise portfolio summary after user confirms DSY trade "Eseguito". The cropped screenshot shows **no visible clock**; its filename may suggest a time but is **not a verified platform execution timestamp**.

## Observed platform values

| NextWise field | EUR |
|---|---:|
| Capitale iniziale (application reference) | 50,175.20 |
| Valore dei titoli | **39,074.92** |
| Liquidità | **10,358.26** |
| Valore totale / NAV | **49,433.18** |
| Platform-displayed performance | **−1.48%** |
| Securities + cash minus NAV | **0.00** |

The NAV difference versus the original EUR 50,000 virtual endowment is **EUR −566.82 (−1.13364%)**, distinct from the application's **−1.48%** based on the EUR 50,175.20 displayed reference.

## Difference versus screenshot before sale on 20 Nov 09:54–09:55

| Field | Pre-sale EUR | New screen EUR | Change EUR |
|---|---:|---:|---:|
| NAV | 49,519.84 | 49,433.18 | **−86.66** |
| Securities | 39,844.08 | 39,074.92 | **−769.16** |
| Cash | 9,675.76 | 10,358.26 | **+682.50** |

The EUR **−86.66** NAV change is a between-screens account movement. It cannot be attributed entirely to the DSY sale, as other market marks/FX may have moved between screenshots. Transferring holdings to cash in itself does not create or erase NAV apart from price differences, fees and other adjustments.

## Execution-control exception: EUR 2.10

The participant said they sold Dassault Systèmes at **EUR 22.68**, and subsequently confirmed the order status as **executed**. The proposed ticket was **30 shares**, with seller limit floor **EUR 22.70** (the exact submitted order type/terms and receipt are NOT yet independently visible).

Conditional arithmetic:
- If **30 shares** executed at **EUR 22.68**, gross proceeds are **EUR 680.40**.
- Cash difference shown by NextWise between the two screenshots is **EUR +682.50**.
- **Cash reconciliation gap = +EUR 2.10** (unexplained).
- If all EUR 682.50 arose strictly from 30 sold shares with no other bookings/fees, their effective price would be **EUR 22.75 per share**.

**Do not assert EUR 22.75 as the actual sale price:** cash could include an unrelated dividend/cash flow, platform-specific settlement, fee adjustment, a delayed prior posting, or the initial EUR 22.68 may have been the displayed quote rather than the execution price. A normal EUR 22.70 sell limit cannot execute for EUR 22.68 per share before any fee-display differences; this merits ticket-level checking, not accusations of platform error.

## Current modeled position status

- Participant confirms a **DSY.PA sell execution** following 30-share trim proposal. The event-based quantity inventory assumes 30 executed, leaving **60 DSY**; obtain screenshot of updated DSY card to confirm exact quantity.
- **AD.AS buy 25 @ max EUR 34.30 remains PENDING** per participant's most recent order-status confirmation; do not count it in invested equities or enter a duplicate.
- Account currently has **21 distinct actual equity holdings** if the reported 30-share DSY partial sale is accurate and there are no other fills.
- Observed cash fraction **20.9554%** and equity fraction **79.0446%** of current NAV.
- **No current stock-level price marks** in this screenshot; do not assign the other EUR −86.66 change to individual names or recompute volatility/covariance based only on this account-level NAV.

## Required next validation

Read NextWise **Transazioni** / DSY execution detail to establish **executed quantity, actual fill price, order type, entered limit, timestamp, fees and any other cash movement**; check DSY position card shows 60. Preserve earlier price and order claims as participant reports, never silently overwrite with the mathematically implied EUR 22.75.

The scheduled market-data NAV monitor is **deliberately gated** because its old frozen 18 November holdings still show 90 DSY shares. Re-enable only after a safe post-trade portfolio price-basis reconciliation.

## Data artifacts

- [Chronological NextWise NAV screenshot log](../../data/nextwise_nav_snapshots.csv)
- [DSY executed / AD pending transaction ledger](../../data/trade_events_2026-11-20.csv)
- [After-execution quantities (not yet new market values)](../../data/positions_after_execution_2026-11-20.csv)
- [Decision Log](../../docs/governance/DECISION_LOG.md)

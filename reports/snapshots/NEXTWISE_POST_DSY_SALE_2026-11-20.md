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

## Execution-control reconciliation — ZERO cash residual

The participant **explicitly corrected** the earlier EUR 22.68 price and confirmed the actual Dassault Systèmes sale price of **EUR 22.75/share**. This supersedes the initial statement. The intended sale quantity was 30 shares and DSY execution status was reported **Eseguito**.

| Check | Amount |
|---|---:|
| 30 executed shares × confirmed EUR 22.75 | **EUR 682.50** |
| NextWise account cash increase between screenshots | **EUR +682.50** |
| **Residual, on reported 30-share trade** | **EUR 0.00** |
| Proposed minimum sell limit | EUR 22.70 |
| Confirmed price above limit | EUR +0.05/share, EUR +1.50 for 30 shares |

The user-confirmed execution price now fully explains the cash increase, assuming no offsetting unrelated cash bookings. The screenshot shows account cash but **not** the order receipt or fees separately. Do not infer a precise timestamp or independently confirmed order type from these data.

The earlier apparent EUR 2.10 discrepancy was caused by using the initial, subsequently corrected EUR 22.68 figure; **it is resolved**. The indicative book loss at historical displayed EUR 25.49 acquisition price is now **EUR −82.20** on 30 shares, before any applicable accounting adjustments.

## Current modeled position status

- Participant confirms a **DSY.PA sell execution** following 30-share trim proposal. The event-based quantity inventory assumes 30 executed, leaving **60 DSY**; obtain screenshot of updated DSY card to confirm exact quantity.
- **AD.AS buy 25 @ max EUR 34.30 remains PENDING** per participant's most recent order-status confirmation; do not count it in invested equities or enter a duplicate.
- Account currently has **21 distinct actual equity holdings** if the reported 30-share DSY partial sale is accurate and there are no other fills.
- Observed cash fraction **20.9541%** and equity fraction **79.0459%** of current NAV.
- **No current stock-level price marks** in this screenshot; do not assign the other EUR −86.66 change to individual names or recompute volatility/covariance based only on this account-level NAV.

## Required next validation

Optional final receipt-level validation: check the NextWise **Transazioni** row for the 30-share fill at the **user-confirmed EUR 22.75** price, recorded order type/limit, timestamp and fees; verify the DSY card shows 60 shares. The earlier EUR 22.68 statement remains in the version history but has been explicitly superseded.

The scheduled market-data NAV monitor is **deliberately gated** because its old frozen 18 November holdings still show 90 DSY shares. Re-enable only after a safe post-trade portfolio price-basis reconciliation.

## Data artifacts

- [Chronological NextWise NAV screenshot log](../../data/nextwise_nav_snapshots.csv)
- [DSY executed / AD pending transaction ledger](../../data/trade_events_2026-11-20.csv)
- [After-execution quantities (not yet new market values)](../../data/positions_after_execution_2026-11-20.csv)
- [Decision Log](../../docs/governance/DECISION_LOG.md)

# Project Alpha 2027 — NextWise intraday account snapshot, 20 November 2026, 13:55 CET

**Source:** participant-provided NextWise "Portafoglio" screenshot, device time **13:55** on Friday, 20 November 2026 (Europe/Rome). This is an **observed platform account value**, not an exchange-synchronized closing NAV or an automated quote-feed result.

## Observed current balance

| NextWise label | Observed |
|---|---:|
| Capitale iniziale (platform reference) | EUR 50,175.20 |
| Valore dei titoli | **EUR 38,958.27** |
| Liquidità | **EUR 10,358.26** |
| Valore totale | **EUR 49,316.53** |
| Performance displayed | **−1.71%** |
| Securities + cash − NAV | **EUR 0.00** |
| Equity weight (NAV) | **78.9964%** |
| Cash weight (NAV) | **21.0036%** |

**Be careful with performance bases:** the change relative to the competition's original nominal EUR 50,000 is EUR **−683.47** (**−1.36694%**), which is not the performance displayed by NextWise against its EUR 50,175.20 internal reference.

## Compared with immediately prior NextWise post-DSY summary

| Item | Prior observed EUR (screenshot without device clock) | 20 Nov 13:55 EUR | Difference EUR |
|---|---:|---:|---:|
| Marked securities | 39,074.92 | 38,958.27 | **−116.65** |
| Cash | 10,358.26 | 10,358.26 | **0.00** |
| Total NAV | 49,433.18 | 49,316.53 | **−116.65** |

The observed additional EUR **116.65** NAV decline is entirely equal to the reduction in the displayed marked securities total while observed cash is unchanged. This **does not identify** which companies drove it or prove that no intraperiod trades occurred. The two platform screenshots were observed at different times; quote timing is not independently verified.

Relative to 20 Nov **09:54–09:55** screenshot before the user-confirmed DSY trim, NAV is **−203.31 EUR**, marked securities **−885.81 EUR**, cash **+682.50 EUR**. The EUR 682.50 cash increase is fully reconciled as **30 DSY shares × corrected reported execution price EUR 22.75**. This realizes previously marked exposure; a sell by itself neither increases nor decreases NAV by the sale consideration.

## Open and completed orders

- **Dassault Systèmes / DSY.PA:** participant confirms the 30-share partial sale executed at **EUR 22.75**, leaving **60 shares** on a transaction-ledger basis. Execution is user-confirmed and cash increase matches; no separately inspected broker receipt.
- **Ahold Delhaize / AD.AS:** participant says the 25-share, EUR 34.30 limit buy has **not been accounted for**; previously reported as pending. There is **no confirmed AD.AS fill** and it is not present in the active 21-name positions. Cash unchanged since prior post-trade screen is consistent with this, but a full order detail was not visible in the screenshot even though the Orders tab is highlighted.
- Do **not** place a duplicate AD.AS order; check the actual status in NextWise before any trading decision.

## Risk and research state

- No reconciled synchronized stock-by-stock prices after the 30-share DSY sell. Historical 18-Nov automated NAV estimator is **paused under reconciliation gate**; do not resume by reusing the outdated 90-share DSY quantities or by replacing post-trade positions with frozen morning values.
- Sector, covariance, updated VaR, and risk contribution cannot be reconstructed from this account-total screenshot alone.
- The 21-name transaction-level **quantity** inventory is tracked separately from the frozen morning positions file and from any tentative inferred cash.
- Portfolio roughly **79% equities / 21% cash** in the observed snapshot, with DSY exposure reduced. Do not add positions merely to recover today's paper losses.

## Next step

Obtain the *actual* current Ahold order status and a time-matched NextWise list of 21 updated position marks, or a post-close full portfolio screen; update the risk engine only after prices, cash and fills reconcile.

[Trade events](../../data/trade_events_2026-11-20.csv) · [Quantity-only post-execution inventory](../../data/positions_after_execution_2026-11-20.csv) · [Snapshot history](../../data/nextwise_nav_snapshots.csv) · [Decision Log](../../docs/governance/DECISION_LOG.md).

**No NextWise orders were placed by ChatGPT/GitHub.**

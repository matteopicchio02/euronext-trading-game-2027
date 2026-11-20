# Project Alpha 2027 — Pre-trade proposal: partial trim of Dassault Systèmes
**Decision date:** 20 November 2026. **Status:** PROPOSED / NOT SUBMITTED / NO FILL CONFIRMED. **Virtual ETG portfolio.**

## Proposed order (participant must verify manually on NextWise)

| Parameter | Proposal |
|---|---|
| Action | **SELL**, partial reduction of existing position |
| Security | Dassault Systèmes SE (DSY.PA), Euronext Paris |
| ISIN | **FR0014003TT8** |
| Pre-trade quantity | 90 shares, as verified from NextWise at 09:54–09:55 CET Nov 20 |
| Sell quantity | **30 shares** |
| Minimum acceptable sell limit | **EUR 22.70 per share** |
| Minimum gross consideration if fully filled | **EUR 681.00** (ignores fees / FX / market movement) |
| Quantity retained if fully filled | **60 shares** |
| Price check | The NextWise order ticket must display the correct instrument and **limit sell >= EUR 22.70**; if price, order type, or validity is unclear, do not submit |
| Execution / submission | **NOT VERIFIED**; this memo itself sends no orders |
| Existing pending order | **Ahold Delhaize 25 AD.AS BUY, reported limit EUR 34.30, still PENDING**; do NOT enter a duplicate |
| Current snapshot baseline | NAV EUR 49,519.84; equity EUR 39,844.08; cash EUR 9,675.76 as of Nov 20 09:54–09:55 |
| Research price context | Public 20 Nov quote around EUR 22.72 as of 10:19 on Boursorama; delayed/mixed-timestamp websites can differ, so use NextWise execution preview, not public page, for current executable price |

## Thesis: why reduce only one third?

- **Catalyst mismatch with competition horizon:** Dassault Systèmes' 17 Nov 2026 CMD targets over EUR 8bn revenue and EUR 1.80 non-IFRS diluted EPS in 2029. Euronext Trading Game ends 9 Apr 2027, substantially before those targets.
- Analysts expressed skepticism over new mid-term target ambitions; Jefferies reportedly maintained underperform and a EUR 19 target, which is NOT necessarily a calibrated or certain forecast. Management's Q3 2026 update was comparatively positive, so an all-out sale is not justified on a one-sided reading.
- Marked exposure at 20 Nov snapshot EUR 2,049.30 (~4.14% NAV); reducing 30/90 nominally reduces DSY-specific exposure by ~1.38 percentage points of NAV at the quoted snapshot. It is a **risk concentration and conviction adjustment**, not a proven expected-alpha rotation.
- Research decision is an incremental move towards reduced sector/Paris listing concentration, not an official Euronext concentration-rule compliance obligation.
- DSY is currently below the originally recorded purchase price EUR 25.49. Any realized accounting loss on a sale is not an additional economic loss by itself. Taxes/fees/dividends/NextWise accounting are not verified.

## Scenario: price held at proposed limit

Assuming **30 shares execute exactly at EUR 22.70** while all other marked positions and cash are unchanged:
- Nominal DSY sale proceeds **EUR 681.00**; available account cash after the sale would be approximately **EUR 10,356.76**, except that Ahold pending-order reserves can reduce buying power.
- Position quantity would go from 90 to **60**; equity value falls nominally by EUR 681 and cash rises by EUR 681. **NAV does not increase from the sale itself**, except from price differences and costs.
- This illustrative cash balance is **not actual NextWise cash**; the 20 Nov morning NAV and 21-name positions must remain frozen until a fill is confirmed.
- If Ahold 25-share buy also fills at EUR 34.30, under unchanged other marks, cash would be EUR 9,499.26 (net); do **not** assume it has filled.

## Precise entry controls

1. Verify instrument ticker/ISIN, available 90 shares and that no existing DSY sell order is pending.
2. Place **a sell LIMIT only**, **30 shares**, **minimum EUR 22.70**. Review the contemporaneous NextWise execution preview; do not replace with market execution.
3. Before confirming, check any restrictions, fees, simulation mechanics and order validity. The displayed quote may be delayed, order may remain pending, and seller/buyer prices can differ.
4. Check status after submission: **pending**, **partially filled**, **fully filled**, **rejected** or **cancelled**. The order is not a confirmed sell without status confirmation.
5. Record actual shares, executed price/time, updated cash and unrealized/realized P&L. Create a dated post-fill snapshot; do NOT modify `data/portfolio_actual_2026-11-20.csv` retroactively.
6. Monitor DSY earnings (officially 3 Feb 2027) and Ahold order status; no additional trades until post-order reconciliation.

## Risk constraints and adverse scenarios

- **Opportunity cost:** the remaining 60 shares retain upside, but 30 sold shares no longer participate in a rebound. A +10% DSY return after the illustrative sale corresponds to ~EUR 68 lower DSY participation versus 90 shares at EUR 22.70; a −10% return avoids an equivalent isolated decline, before covariance or cash redeployment.
- **No claim that DSY will fall**: fundamentals Q3 improved and 2029 growth targets may lead to positive surprises. Analyst views disagree.
- The selected **EUR 22.70** sell floor is a *research trade level*, not a guaranteed obtainable price. The public quote cited above was **~EUR 22.72 at 10:19 CET on 20 Nov**, and time stamps on finance websites conflict. If NextWise bid is below limit, do not sell at market to force a fill.
- Limit orders can stay pending under NextWise platform terms; verify/monitor rather than post duplicate entries.

## Sources
- Current position data: [dated 20 Nov screenshot snapshot](../../data/portfolio_actual_2026-11-20.csv).
- [Five-name fundamental desk review](REVIEW_2026-11-20_FIVE_NAMES.md).
- Dassault CMD announcement (17 Nov): https://investor.3ds.com/news-releases/news-release-details/dassault-systemes-2026-capital-markets-day-new-industrial-era
- Q3 strong results: https://investor.3ds.com/news-releases/news-release-details/dassault-systemes-strong-q3-performance-improved-fy26-objectives
- Analyst critical reaction: https://www.boursorama.com/bourse/actualites-amp/dassault-systemes-ne-convainc-pas-avec-ses-nouveaux-objectifs-7a7c1a7e41c22fa9cd78c6fdfce10c8d
- Public intraday quote (time-bound): https://www.boursorama.com/cours/consensus/1rPDSY/

**No actual NextWise order placed by ChatGPT. A user action is required.**

## User-reported Dassault sale at EUR 22.68 — execution reconciliation pending

**Participant statement:** "ho venduto a 22,68" on 20 November 2026, following the proposed 30-share DSY trim. Treat **EUR 22.68 as user-reported sale price**, but the participant has **not explicitly confirmed quantity, filled vs pending status, execution timestamp, order type or fees** in this message. **Do not mark the proposed 30-share sale as a verified fill or edit actual holdings yet.**

**Discrepancy with pre-trade instruction:** the proposed sell LIMIT floor was **EUR 22.70**. A genuine EUR 22.70 limit sell should not execute at EUR 22.68; the actual order type, entered limit, or reported price/fee convention must be checked using the NextWise transaction/order detail. EUR 0.02/share = EUR 0.60 if 30 shares; this is a trade-process variance, **not evidence by itself of improper platform execution**.

**Conditional accounting only if 30 DSY shares were actually filled at EUR 22.68, ignoring fees:**
- Gross proceeds = **EUR 680.40**.
- DSY shares: **90 -> 60**; pre-sale screenshot price EUR 22.77 was an earlier mark, not the executed price.
- Cash before EUR 9,675.76 -> **EUR 10,356.16** in a static scenario, with the Ahold pending BUY still unfilled and without accounting for cash reservations or other movements.
- Illustrative realized loss relative to the displayed EUR 25.49 average purchase quote: **EUR -84.30** (30 x (22.68 - 25.49)), excluding fee/book-cost discrepancies. This is **not an additional loss created by selling**; it converts already marked risk into cash.
- Remaining exposure at the reported EUR 22.68 price: **60 x 22.68 = EUR 1,360.80**; the whole NAV must be re-marked from NextWise after execution and must not be computed using stale other-company marks.

**Outstanding action:** participant must confirm whether 30 were executed, whether order shows *Eseguito*, exact submitted order type/limit, and updated cash if available. Enter a definitive transaction and create a new dated 21-name actual snapshot only after verification. No NextWise trade was sent by GitHub or ChatGPT.

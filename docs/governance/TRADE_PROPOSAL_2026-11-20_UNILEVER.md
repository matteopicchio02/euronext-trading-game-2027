# Project Alpha 2027 — pre-trade proposal: Unilever new position (NOT submitted)
**As-of:** 20 November 2026, ~15:12 Europe/Rome. **Status:** PROPOSED, NOT EXECUTED. Euronext Trading Game virtual account, user places any orders personally on NextWise.

## Proposed LIMIT ticket, cash-funded

| Field | Value |
|---|---|
| Action | **BUY** new starter position |
| Issuer | Unilever PLC |
| Trading venue | Euronext Amsterdam |
| Euronext ticker / Yahoo ticker | **UNA / UNA.AS** |
| ISIN | **GB00BVZK7T90** |
| Quantity | **20 shares** |
| Maximum purchase limit | **EUR 58.40 per share** |
| Nominal committed ceiling | **EUR 1,168.00**, excluding any platform costs |
| Status | **RESEARCH PROPOSAL ONLY — NOT SENT** |
| Buy only if | NextWise instrument and ISIN match; order is a **buy LIMIT** with no higher than EUR 58.40; ticket preview is acceptable and there is no identical pending order |
| If price exceeds limit | **WAIT, do not chase/convert to a market order** |
| Preferred order validity | If selectable, DAY; if validity hidden, monitor/cancel as necessary because NextWise can leave pending orders standing |
| Starting NextWise NAV | EUR 49,316.53 (13:55 Nov 20 screenshot) |
| Starting cash | EUR 10,358.26 (same screenshot) |
| Cash remaining at max fill | EUR **9,190.26** (before fees, other market movements) |
| Equity allocation at max fill | EUR 40,126.27, about **81.37% NAV** (static) |
| Position risk budget | ~**2.37% of NAV**; hypothetical −10% price scenario = EUR **−116.80** (= ~−0.24% NAV), NOT a bounded maximum loss |
| Pending order alongside | Ahold Delhaize **AD.AS, BUY 25 at limit EUR 34.30**, participant-confirmed pending. DO NOT REENTER OR ASSUME FILL. If both tickets eventually fill at limits, modeled cash before other adjustments EUR **8,332.76**, ~16.9% NAV |

## Public intraday price reference, not an executable quote

As of a publicly timestamped 20 Nov **13:19** report, **UNA.AS last around EUR 58.13** (De Belegger); other available public sources show EUR 58.19 on a delayed exchange feed and differ by quote time. The proposed EUR 58.40 ceiling is **not a live market price** and an execution is never guaranteed. It must be checked directly on the NextWise ticket, not inferred from these outside sources.

- Market quote and timing: https://www.debelegger.nl/en/stock/UNA.AS
- Euronext Amsterdam ticker/ISIN: https://www.boursorama.com/cours/1rAUNA/
- Delayed Euronext Amsterdam reference: https://www.capitol.fr/fr/marche/euronext-amsterdam/unilever-plc-GB00BVZK7T90-UNA-EUR-XAMS/graphiques

## Why Unilever instead of an indiscriminate buy-the-dip

1. Q3 2026 **underlying sales growth +5.2%**, of which +2.9% from volume; **Home & Personal Care +7.0%** underlying; full-year 2026 4–6% underlying sales growth and >=3% volume growth outlook. Resilience and geographic/consumer demand exposure are useful while the 20 Nov European tech market is under pressure.
2. Euronext Amsterdam listing adds to geographic *venue* diversity rather than the already ~41% NAV Paris-listed market exposure. **Listing venue != geographic revenue exposure**.
3. Rationale is a **small defensive/growth quality tranche** after a partial sale of high-uncertainty DSY, not an attempt to mechanically claw back losses.
4. Existing **consumer staples** sleeve already includes Heineken and L'Oréal at morning marks totaling ~EUR 4,600 and the pending Ahold is a staple retailer. If Unilever and Ahold both fill, *approximate* legacy-price staple-related exposure rises toward ~13.4% NAV; correlation remains unmeasured. This is a diversification *by business model* (global personal/home care vs food retail vs beverages/beauty), not proven low statistical correlation.
5. Alternative **Enel** has attractive 9M earnings (EUR 0.74 FY26 EPS guidance), but **heightened Brazilian regulatory tail risk**: ANEEL board majority backed termination recommendation for São Paulo concession, proceeding postponed on Nov 17; Fitch downgraded Brazilian subsidiaries Nov 19. **Do not buy Enel solely for lower share price**.
6. ING would add bank/financial beta to existing AXA, Generali and Euronext. ASML and other semiconductors have sold off sharply in the AI trade; not a low-risk hedge. Schneider adds to European industrial/capex beta and Paris listing concentration. Ahold is already pending; **no duplicate buy**.

**Primary Unilever source:** https://www.unilever.com/news/press-and-media/press-releases/2026/continued-strong-performance-in-the-third-quarter/
**Brazil regulatory news:** https://www.reuters.com/business/energy/brazil-regulator-forms-majority-recommend-ending-enels-sao-paulo-concession-2026-11-17/
**Fitch Brazil concern:** https://ri.enel.com/Documento/DownloadPublicFile?fileNameKey=211ee2d6-df40-4e20-931a-10a05031831f.pdf&tipoPath=2

## Negative case and trade controls

- Unilever is **not risk-free**: commodity inflation, underlying Foods weakness and a planned Foods combination with McCormick introduce execution/regulatory risk; equity markets can reprice all defensives during liquidity selloffs.
- **Correlation-adjusted VaR and prospective alpha NOT yet computed** using synchronized post-DSY holdings and UNA history. Do not falsely claim this is minimum-volatility optimal or guaranteed to improve official Euronext game score.
- The Q3 dividend amount **does not mean a free guaranteed return**; ex-dividend adjustment, eligibility and how NextWise tracks cash distributions must be verified.
- Never submit a MARKET order if the app cannot guarantee the EUR 58.40 maximum; leave a limit order unfilled rather than pay any price.
- Do not enter this trade if NextWise has an existing UNA order, does not offer the stock for this competition, or actual buying power is lower than the required amount.
- Since Ahold is pending, both possible commitments total **EUR 2,025.50**, about **4.11% of 13:55 NAV**; no leverage.
- After any execution, log actual quantity, average fill, cash, NAV, fees and date; create an additional dated 22-name snapshot only if UNA has truly filled; if Ahold also fills, 23.
- Recheck at a synchronized post-close checkpoint and after new earnings/large price gaps; avoid daily whipsaw trading.

**Current trade booking status at memo publication:** DSY 30-share sale at EUR 22.75 is participant-confirmed executed, Ahold BUY 25 at max EUR 34.30 pending, Unilever **research proposal only**. ChatGPT and GitHub have no NextWise trading access.

## Participant-reported Unilever purchase — status to verify

**20 Nov 2026, after the trade proposal:** participant says "acquistato a un prezzo totale di 1168". The participant-reported **EUR 1,168.00 total** exactly matches our proposed **20 UNA.AS shares × EUR 58.40 maximum share price**. This arithmetic is indicative; the participant has **not yet separately confirmed** order status `Eseguito` rather than `Pendente`, actual executed quantity, share fill price, any fees, or current NextWise cash.

**Bookkeeping control:** treat this as a **user-reported purchase awaiting fill-status confirmation**. Do **not** yet insert UNA.AS into the 21-name executed holdings inventory, subtract EUR 1,168 from official cash, or claim there are 22 actual holdings until NextWise shows execution. The prior dated 13:55 snapshot remains NAV **EUR 49,316.53**, cash **EUR 10,358.26**.

**Conditional scenario only if 20 shares fully executed for EUR 1,168.00 in total, with zero fees and no other movements:** cash **EUR 9,190.26**, equity value increases EUR 1,168.00 before subsequent price marks, and position count becomes 22. Ahold Delhaize 25 @ EUR 34.30 buy was last confirmed **PENDING**, so do not include it or submit a duplicate.

**Next action:** confirm whether NextWise shows `Eseguito` or `Pendente` for Unilever, obtain filled quantity/cash or screenshot, and then update the actual positions/transaction ledger. The pre-trade proposal terms above are historical; this addendum is the more recent order-status information.

## Final reported status: PENDING / no confirmed fill

The participant explicitly clarifies **"pendente"** in response to whether the EUR 1,168 Unilever order is executed or pending. **Status is therefore PENDING on NextWise, NOT EXECUTED**. The EUR 1,168 figure was the reported order notional; 20 shares at a EUR 58.40 maximum limit are the planned terms, not a verified receipt. **No Unilever shares should be added to actual holdings and no EUR 1,168 should be deducted from the official cash balance** until an execution is explicitly confirmed.

The **Ahold Delhaize 25-share order at EUR 34.30 is independently pending**, and the **Dassault Systèmes 30-share sale at EUR 22.75 is executed**. The last observed NextWise overview remains EUR **49,316.53 NAV** and EUR **10,358.26 cash** as of 20 Nov 13:55, **not** a refreshed value after the new pending order. If the platform reserves order buying power, this may reduce *available* buying power without reducing displayed *account cash*.

If both limits were eventually fully filled without fees or other changes, combined purchase cost would be **EUR 2,025.50**, leaving a hypothetical **EUR 8,332.76** cash; these are NOT executed trades. Avoid duplicate buy orders or chasing either limit.

**Next update trigger:** actual status changes to Executed/Partially Executed/Cancelled, with confirmed quantity, price and new NextWise summary. Record those before any further trade recommendation.

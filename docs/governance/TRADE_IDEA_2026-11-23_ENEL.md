# Project Alpha 2027 — Student pre-trade idea: a small Enel position

**Date:** 23 November 2026 · **Status:** RESEARCH PROPOSAL ONLY — NOT ORDERED, NOT EXECUTED

I'm exploring whether a small position in **Enel S.p.A. (ENEL.MI, ISIN IT0003128367, Euronext Milan)** adds useful electricity-utility exposure to my virtual trading-game portfolio without committing too much of the remaining cash. This is a student research exercise, not a validated alpha strategy.

## Proposed limit order to inspect (not to send automatically)

| Item | Value |
|---|---|
| Action | BUY (new holding) |
| Proposed quantity | **100 shares** |
| Maximum per-share buy limit | **EUR 9.30** |
| Maximum gross notional | **EUR 930.00** |
| Last platform portfolio NAV | **EUR 49,334.92** (23 Nov 10:15 profile only) |
| Last *verified* platform cash | **EUR 8,336.86** (20 Nov 18:05, may not reflect later cash events) |
| Max new nominal weight | **1.88%** of last observed NAV |
| Conditional cash after a full limit fill, assuming no other changes/fees | **EUR 7,406.86** |
| Conditional cash weight using unchanged 23 Nov NAV | ~**15.01%** |
| Holding count if filled | **24** |
| Source price context | Euronext Milan official list gave **EUR 9.416 as 20 Nov close at 17:35 CET**; a 23 Nov public third-party intraday quote around EUR 9.386 was surfaced, but is not the executable NextWise order book. Recheck the current NextWise price and order preview |
| Order handling | **LIMIT only**; no market order, no chasing, no second identical order |
| If price does not reach limit | **Leave unfilled rather than move the limit up without a fresh review** |
| Validity | NextWise can leave orders pending; check status and manually cancel/review if stale. No automatic cancellation assumed |

If the simulation requires a market order or the correct Euronext-listed security/ISIN cannot be verified, **do not submit** the order.

## Why Enel rather than another bank or technology company?

The current account holds 23 virtual securities across 11 internal sector categories. It has EDP and Snam under Utilities, but no Enel. I am testing a **small addition to regulated networks / electricity distribution**, not arguing that one more name automatically improves diversification. It may diversify cash-flow drivers relative to high-beta industrial/technology companies, but the correlation and covariance effects have **not been validated** on a current 24-name mark-to-market dataset.

On 12 Nov 2026 Enel's official 9M update reported:
- Group ordinary EBITDA increase and higher ordinary EPS guidance for 2026;
- Expected 2026 EPS around **EUR 0.74** (Reuters via MarketScreener);
- Interim dividend decision **EUR 0.245 per share**, payable starting **20 Jan 2027**; dividend return depends on record/ex-dividend rules, price adjustment, and NextWise game accounting — **not a free gain**;
- **Net financial debt EUR 66.158bn at 30 Sep 2026, up 15.7% versus year end 2025**, partly from FX, investment and working capital. This is a real financial risk.

Sources:
- Official interim-results and leverage: https://www.enel.com/media/explore/search-press-releases/press/2026/11/enel-in-the-nine-months-of-2026-growth-in-results-is-led-by-spain-and-the-americas-while-margins-in-italy-continue-to-decline
- Official Italian release including 2027 interim dividend: https://www.enel.com/it/media/esplora/ricerca-comunicati-stampa/press/2026/11/enel-nei-nove-mesi-del-2026-la-crescita-dei-risultati--trainata-da-spagna-e-americhe-mentre-continua-il-calo-dei-margini-in-italia
- Euronext market listing and *as-of* 20 Nov closing price: https://live.euronext.com/it/markets/milan/equities/euronext/list
- Borsa Italiana security identifier: https://www.borsaitaliana.it/borsa/azioni/scheda/IT0003128367-MTAA.html

## Risk budget — conditional, not model output

At an illustrative EUR 9.30 fill for 100 shares, **EUR 930 gross** is allocated; 10% stock-only mark-down means **EUR −93**, or **0.19 percentage points of the Nov 23 observed NAV**, before other portfolio changes. The *worst possible* share-price loss can reach the entire EUR 930, unlike a 10% stress scenario.

If the market falls broadly, regulated utilities can also decline because of interest-rate changes, capital spending, policy risk and increased debt. The portfolio already has two utilities, so this is **not** a free hedge.

A previous 18-Nov optimisation research scenario found that rotating Paris-listed exposure toward Ahold+Enel marginally reduced model volatility, but that was a **different 21-name portfolio and funding design**. It does **not** establish the marginal VaR, Sharpe or expected return of adding Enel to the current 23-name portfolio with cash.

## Decision and post-trade controls

**Status: PROPOSAL ONLY**. No NextWise order or holding should be recorded as executed because of this note.

If the participant chooses to submit the order, first verify the **100-share quantity, exact ISIN, EUR 9.30 buy limit and order validity** in the NextWise preview; report PENDING versus EXECUTED (or partial fill). Upon verified execution, add the actual fill to the transactions file and dated quantity ledger, update cash and stop/re-anchor the external-price monitor until the new 24-name portfolio is reconciled. Keep older dated snapshots for the audit trail.

If no reasonable price is available or the price never reaches EUR 9.30, the chosen action is **no trade**; a blank fill is acceptable and not evidence of a broken process.

**Game eligibility context:** Euronext official 2026–27 rules allow qualifying stocks on Euronext Milan as well as other specified exchanges, but the actual security must be eligible and present in NextWise's available investable universe.

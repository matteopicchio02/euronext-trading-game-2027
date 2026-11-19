# Project Alpha 2027 — Full 21-position diagnostic from NextWise cards
**Review date:** 19 November 2026, screenshot filenames approximately 15:48:59–15:50:05 Europe/Rome  
**Account overview source:** NextWise NAV screenshot, approximately 15:46:07 (filename-derived timestamp, not screenshot clock)  
**Portfolio state:** 21 shares unchanged in quantity versus 18 November; participant confirmed no holdings changes. **No purchase or sale placed by this research.**

## Source of truth and critical non-synchronization warning

- [21 original position cards manually transcribed, preserving displayed quote and valuation currency](../../data/portfolio_cards_2026-11-19_1550.csv).
- [Official overview snapshots](../../data/nextwise_official_snapshots.csv): 19 Nov NAV **EUR 49,776.96**; equities **EUR 40,101.20**; cash **EUR 9,675.76**; platform performance **−0.79%** against its reference capital **EUR 50,175.20**.
- The **six position-card screenshots are taken several minutes after** the single portfolio NAV overview. They are **not an exactly synchronized intraday book**. Do not pretend they are a valuation as of one precise second, or merge raw NOK with EUR.

## P&L reconciliation

From the 21 position-card P&L displays (all P&L amounts shown in EUR, including Equinor):
- **11 losers**, whose combined displayed P&L is **−EUR 960.40**.
- **10 winners**, combined **+EUR 559.37**.
- **Net displayed position P&L −EUR 401.03**.
- Account difference from NextWise *reference capital* EUR 50,175.20 is **−EUR 398.24** (49,776.96 − 50,175.20). Gap to card P&L total: **EUR 2.79**. Could reflect asynchronous marks, spreads/cost basis, price rounding or currency treatment, but no cause is established.
- Difference from original virtual funding EUR 50,000 is **−EUR 223.04 (−0.446%)**. These baselines are different; do not call −0.79% the loss against the initial EUR 50,000.
- Compared to NextWise 18 Nov total NAV EUR 50,164.75, **−EUR 387.79** (−0.773%). Cash unchanged in the two overview screenshots.

### Biggest accumulated negative P&L since purchase

| Security | Displayed unrealized P&L in EUR | Since-purchase % | Number of shares | Current displayed position |
|---|---:|---:|---:|---|
| Dassault Systèmes (DSY.PA) | **−225.18** | −9.81% | 90 | EUR 2,069.10 |
| Equinor (EQNR.OL) | **−209.39** | −10.51% | 49 | **NOK 19,070.80**, NOT EUR |
| Capgemini (CAP.PA) | **−160.50** | −8.44% | 15 | EUR 1,740.75 |
| TotalEnergies (TTE.PA) | **−139.10** | −6.29% | 26 | EUR 2,070.64 |
| Airbus (AIR.PA) | −74.72 | −5.10% | 7 | EUR 1,391.60 |

The top four show **EUR −734.17** in accumulated mark-to-market P&L. This is NOT their incremental one-day or 18-to-19-Nov price change.

Best accrued positive P&L examples: Sanofi +EUR 126.50, AXA +119.38, Heineken +94.54, Generali +67.60, Air Liquide +66.48. Do not sell winners mechanically to offset losers.

### Snapshot 18 Nov to position cards ~15:48–15:50 Nov 19

For the **20 EUR-valued** positions, sum of displayed 19 Nov EUR amounts: **EUR 38,314.77**, versus their individual 18 Nov values together **EUR 38,677.42**, change **−EUR 362.65**. Biggest 18-to-19-Nov EUR changes:
- Sanofi **−56.75**, Capgemini **−48.00**, Dassault Systèmes **−41.40**, Heineken **−40.60**, KPN **−34.19**, EDP **−31.50**.
- TotalEnergies **−4.42**, Euronext **+2.40**, Generali **+6.24**; these discrepancies with red arrows are important.

The difference between total account equities and the **asynchronous** sum of 20 EUR-valued cards equals **EUR 1,786.43**. The Equinor card instead reads **NOK 19,070.80**. One can solve an *implied residual* FX conversion of ~**10.675 NOK/EUR**, but this is **not a verified EUR/NOK quote, actual position value or accurate Equinor contribution**, since cards and NAV are not synchronous. The residual change **−EUR 25.14** from 18 Nov is a mechanical identity using mismatched timestamps, not validated FX-adjusted return attribution. NO forced portfolio-value reconciliation.

### Daily red-arrow metadata is not independently reliable

NextWise card quote labels show **−6.64%** for Euronext and **−6.78%** for TotalEnergies, while observed values between the Nov 18 screenshot and today's cards changed:
- ENX.PA **EUR 1,987.20 → 1,989.60** (+EUR 2.40; 12 shares, price around EUR 165.60 → 165.80).
- TTE.PA **EUR 2,075.06 → 2,070.64** (−EUR 4.42; 26 shares, price around EUR 79.81 → 79.64).

External quotes near 19 Nov were also close to EUR 165.4–165.8 for ENX, and historic 18 Nov close EUR 165.60; this does not support interpreting the −6.64% as an 18-to-19-Nov ENX close-to-close return. The labels may use a different period/data reference or show stale/incorrect metadata. **Do not calculate P&L attribution from these percentages until their definitions and synchronization are verified.**

## Fundamental threat screen (public, as of 19 Nov)

1. **DSY.PA / Dassault Systèmes:** company announced double-digit revenue/EPS growth ambition for **2029**, not a guaranteed catalyst in the game ending April 2027. Confirm FY26/FY27 revisions, organic growth, valuation and whether Q3 evidence supports the thesis before authorizing any sale. [Company CMD, 17 Nov](https://investor.3ds.com/news-releases/news-release-details/dassault-systemes-2026-capital-markets-day-new-industrial-era).
2. **EQNR.OL / Equinor:** Reuters 19 Nov reported an **ongoing cyberattack** but **normal production**. This is a monitorable operational risk, not verified production impairment. Add NOK/EUR currency exposure and energy-price sensitivity. Monitor official incident guidance; re-evaluate if production or material financial data are impacted. [Reuters 19 Nov](https://www.reuters.com/technology/equinor-says-cyberattack-still-ongoing-output-unaffected-2026-11-19/).
3. **CAP.PA / Capgemini:** management **raised 2026 outlook** on 30 Oct based on Q3 momentum; negative stock P&L alone does not prove broken fundamentals. Confirm organic/acquisition growth, margins, earnings revisions. [Official Q3 release](https://www.capgemini.com/news/press-releases/q3-2026-momentum-drives-upgrade-in-capgeminis-2026-outlook/).
4. **TTE.PA / TotalEnergies:** verify commodity risk, buybacks, cash-flow sensitivity and price data, including whether quoted arrow correctly reflects the observation period. Confirm dividends/ex-date treatment separately. [Company distributions](https://totalenergies.com/investors/shares-and-dividends/dividends).
5. **ENX.PA / Euronext:** daily-arrow metadata looks inconsistent with the two screenshots. Company Q3 results and the announced buyback are relevant, but cannot by themselves resolve the quote-discrepancy. [Company Q3 overview](https://www.euronext.com/en/investor-relations/financial-information/quarterly-results).

## Concentration and next decision

- Largest observed EUR-valued position **Heineken EUR 2,400.04 (~4.82% NAV)**; 21 holding names and **EUR 9,675.76 (~19.44% NAV)** of idle cash. No evidence of one single position dominating the account.
- Approximate **technology exposure** from DSY + CAP **EUR 3,809.85 (~7.65% NAV)**.
- Exact **energy exposure** requires independent real-time NOK conversion of EQNR.OL; under the *illustrative residual-based* Equinor EUR 1,786.43, ENI+EQNR+TTE sum ~**10.48% NAV**. Do not pass this residual as independently verified.
- Unrealized **−10% since purchase** is a research-review priority, **not** automatically a sell threshold; keep behavior tied to forward risks and the official competition scoring function.

### Committee action today

**HOLD / NO NEW ORDERS** until (i) synced closing prices with reliable EUR/NOK are available, (ii) the red-arrow quote metadata ambiguity is reconciled, (iii) material business/catalyst changes are confirmed, and (iv) a proposed sale/buy/rebalance has a documented portfolio-level risk and score case. Review **DSY, EQNR, CAP and TTE first**, not based solely on P&L ranking. User retains full control of NextWise orders.

**Operational checks:** first 21-stock GitHub market-close monitor programmed for 20:37 UTC and candidate review at 20:53 UTC (GitHub schedules may delay/skip). Neither workflow has been independently verified generating a live close report at this assessment. A generated estimated NAV does **not** supersede the NextWise snapshot.

**No orders executed**. All figures concern a virtual trading game, not an actual personal broker account.

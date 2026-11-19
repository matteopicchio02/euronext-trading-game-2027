# Project Alpha 2027 — Prospective Scenario Valuation
**Decision date:** 19 November 2026  
**Comparison:** Ahold Delhaize (AD.AS) vs ING Groep (INGA.AS)  
**Investment horizon:** until the Euronext Trading Game ends **9 April 2027**  
**Decision:** **NO TRADE / conditional watchlist research**  
**Account:** virtual, 21 holdings, NAV **EUR 49,875.21**, cash **EUR 9,675.76** from manually reviewed NextWise screenshot (19 November ~14:03 Rome).

## 1. Evidence inputs vs scenario assumptions

This report uses **FY2027 analysts' EPS estimates** compiled by MarketScreener and **indicative 19 November 2026 share price observations** from financial websites:

| Metric | Ahold Delhaize | ING |
|---|---:|---:|
| Euronext Amsterdam ticker | AD.AS | INGA.AS |
| Price observation | **EUR 34.36**, FT 19 Nov ~12:18 GMT | **EUR 28.68**, Investing.com 19 Nov |
| FY2027 EPS consensus, MarketScreener indexed on 19 Nov | **EUR 2.879** | **EUR 2.947** |
| Current price / FY2027 consensus EPS | **11.93×** | **9.73×** |
| Reference model shares, hypothetical | **29** | **20** |
| Hypothetical ticket | **EUR 996.44** | **EUR 573.60** |
| Approximate NAV allocation | **2.00%** | **1.15%** |

Prices are nonsynchronous, intraday **observations**, not NextWise executable quotes or 19 Nov closing prices. FY2027 EPS is an external analyst aggregate, not company guidance or an EPS actually earned as of April 2027. The two entities differ in business model/accounting; do not mechanically declare ING superior because its forward P/E is smaller.

**Market sources (date-scoped):** [Ahold price, FT](https://markets.ft.markitdigital.com/data/equities/tearsheet/historical?s=AD%3AAEX), [ING price, Investing](https://www.investing.com/equities/ing-groep), [Ahold EPS consensus](https://www.marketscreener.com/quote/stock/AHOLD-DELHAIZE-N-V-29752127/valuation/), [ING EPS consensus](https://www.marketscreener.com/quote/stock/ING-GROEP-N-V-56358303/valuation/).

## 2. The 9 April 2027 price-scenario framework

**Illustrative formula**, not a price target from an independent analyst:
`Hypothetical exit share price = assumed FY2027 EPS x assumed exit P/E`.

EPS multipliers and future P/E multiples below are **our chosen stress scenarios**, not sourced consensus forecasts. Even in April 2027, FY2027 EPS will be an expectation rather than the realized annual outcome.

### Ahold — AD.AS

| Scenario | FY2027 EPS assumption | P/E in April (assumed) | Hypothetical exit price | Price move vs EUR 34.36 | 29-share P&L | NAV impact |
|---|---:|---:|---:|---:|---:|---:|
| **Bear**: cyber/consumer margin deterioration and multiple compression | EUR 2.649 (−8% EPS vs consensus) | 10.8× | **EUR 28.61** | **−16.75%** | EUR −166.87 | −0.335 pp |
| **Base**: guidance stabilizes; no major re-rating | EUR 2.879 (consensus) | 12.5× | **EUR 35.99** | **+4.74%** | EUR +47.20 | +0.095 pp |
| **Bull**: cyber normalization, buyback visibility, stronger confidence | EUR 3.052 (+6%) | 13.5× | **EUR 41.20** | **+19.90%** | EUR +198.32 | +0.398 pp |

### ING — INGA.AS

| Scenario | FY2027 EPS assumption | P/E in April (assumed) | Hypothetical exit price | Price move vs EUR 28.68 | 20-share P&L | NAV impact |
|---|---:|---:|---:|---:|---:|---:|
| **Bear**: rising credit provisions and bank de-rating | EUR 2.593 (−12% EPS vs consensus) | 8.5× | **EUR 22.04** | **−23.14%** | EUR −132.73 | −0.266 pp |
| **Base**: business in line with consensus; moderate re-rating | EUR 2.947 (consensus) | 10.25× | **EUR 30.21** | **+5.32%** | EUR +30.53 | +0.061 pp |
| **Bull**: better profitability/credit costs and multiple expansion | EUR 3.183 (+8%) | 11.75× | **EUR 37.40** | **+30.40%** | EUR +174.35 | +0.350 pp |

All price returns and P&L figures **exclude dividends, share-cash adjustments, market fees and any account FX effects**. Dividends are not free price gains; ex-dividend adjustments and actual NextWise booking must be reconciled. Both scenarios leave the other **21 stocks hypothetically unchanged** and therefore do **not** project the portfolio's overall future NAV.

## 3. Illustrated weighting is NOT probabilistic evidence

For intuition only, place **25% of subjective weight on bear, 50% on base, 25% on bull**. Those weights are **not calibrated**, not historical frequencies and not statistically justified probability estimates.

- Ahold: the illustrative weighted price-return average is **+3.16%** (not an expected-return forecast).
- ING: **+4.48%** (not an expected-return forecast).

Under the separate, arbitrary research example that the unmodified portfolio would return **+6%** from now to 9 April, maintaining a simple return/volatility ratio requires roughly:
- **+4.78%** Ahold share return for the **29-share** EUR 996.44 ticket;
- **+8.16%** ING share return for the **20-share** EUR 573.60 ticket.

Neither the *base case for ING* (+5.32%) nor either *arbitrarily weighted three-case average* clears its illustrative risk hurdle. Ahold's **base case** (+4.74%) is practically identical to its calculated **+4.78% hurdle**, within estimation noise; that is **not** a robust edge. The thresholds are extremely sensitive to the unverified hypothetical portfolio +6% expectation; do not treat them as game score thresholds.

## 4. Quantitative risk budget / capital impact

Using the historical **21-stock covariance proxy through 18 November**, with stock values rescaled only to the **aggregate** 19 November NextWise equities total (individual 19 Nov mark-to-market positions are unavailable):

| Indicator | No buy | Hypothetical 29 Ahold shares | Hypothetical 20 ING shares |
|---|---:|---:|---:|
| Ticket, EUR | 0 | **996.44** | **573.60** |
| Starting cash, EUR | 9,675.76 | 9,675.76 | 9,675.76 |
| Cash after ticket, EUR | 9,675.76 | **8,679.32** | **9,102.16** |
| Cash fraction of NAV | 19.40% | **17.40%** | **18.25%** |
| Historical annualized volatility proxy | **9.0439%** | **9.1878%** | **9.1853%** |
| Change in ann. vol | — | **+0.1440 pp** | **+0.1414 pp** |
| Internal single-position budget cap | +0.15pp | **Pass narrowly** | **Pass narrowly** |
| Position number if filled | 21 | 22 | 22 |

Ahold's lower stand-alone volatility and lower historical correlation with existing stocks make it slightly more efficient under the narrow risk-budget test. ING offers larger upside in its arbitrary bull case but also greater drawdown in the stress case. **We cannot evaluate holding BOTH tickets with this model** because the pairwise Ahold–ING correlation is not in the summary inputs. Do not sum their risk effects.

## 5. Fundamental stress drivers before 9 April

### Ahold
Ahold's official **4 November 2026 Q3 announcement** reported resilient sales, but warned of an October cyber incident affecting online operations and supply chains. It estimated **EUR 200–250 million lost Q4 net sales and EUR 75–100 million operating-income impact**, and cut FY26 expected free cash flow to around **EUR 2.1 billion**, from at least EUR 2.3 billion, with low-single-digit underlying EPS growth guidance. Management maintained the **EUR 1 billion 2027 repurchase plan**. [Official Q3 release](https://newsroom.aholddelhaize.com/ahold-delhaize-reports-resilient-q3-2026-results-and-updates-2026-guidance-to-reflect-business-disruption-caused-by-recent-cybersecurity-incident).

**Catalyst:** **17 February 2027** results. Key variables: realized cyber loss, trading recovery, margins, earnings revisions, annual guidance. A future buyback supports capital return but does not guarantee a higher market multiple.

### ING
ING's **29 October 2026 Q3 net income EUR 1.85bn**, CET1 **13.3%**, quarterly ROTE **16.3%**, and buyback **EUR 1.65bn** confirm meaningful profitability/capital. However, Reuters reported net income below analyst expectations, and a **19 November** analyst note from Jefferies reduced 2027–28 estimates by around **1%** owing to costs/provisions (reported by WSJ). Thus assuming re-rating without a confirming earnings surprise is risky. [ING official Q3](https://ing.com/news/press-releases/3q2026-ing-press-release.html), [Reuters Q3 miss](https://www.reuters.com/business/finance/ing-unveils-165-billion-buyback-despite-profit-miss-2026-10-29/), [WSJ Jefferies 19 Nov note](https://www.wsj.com/business/financial-services-roundup-market-talk-1e52dbdf).

**Catalyst:** **28 January 2027** results. NextWise treatment of the announced January shareholder cash distribution is not verified; no distribution has been added to our scenario returns.

## 6. Decision gate / what would change our mind

**Committee verdict: HOLD / NO TRADE on 19 November.** This is not a vote against either business. We lack a sufficiently favorable verified near-term return case relative to the risk and uncertainty of new exposure.

- **Ahold:** first watchlist candidate for a risk-budgeted ~EUR 1,000 tranche only if cyber-related operating risk stabilizes, FY27 analyst EPS does not deteriorate and a new price/return comparison produces a meaningful margin of safety over the illustrative hurdle. A research price **around EUR 33 or below** would warrant *re-running* the model if assumptions remain unchanged; **not an order price**.
- **ING:** second candidate, risk-budgeted ~EUR 575–600, not the previously discussed EUR 1,000 tranche. Provisions, NIM and EPS forecasts must stabilize; a research price **around EUR 27 or below** might justify reassessment. **Not a limit order instruction**.
- **Recalculation triggers:** meaningful revised EPS estimates, new filing, cyber incident escalation, bank cost-of-risk shock, news before each earnings date, or a sufficiently different available NextWise quote. **Do not turn these price examples into automated limit orders.**
- **No claim that the positive bull scenario is more likely than bear or base.** No verified expected-return distribution exists. The company share repurchases might already be included in the analysts' EPS estimates: do not double count.
- **NextWise order and cash execution status must be manually verified** before changing anything.

## 7. Reproducibility

- [Explicit scenario inputs](../../data/scenario_assumptions_AHOLD_ING_2026-11-19.json).
- [Offline Python scenario model](../../scripts/valuation_scenarios.py).
- [Dated portfolio and candidate covariance summary](../../data/candidate_risk_inputs_2026-11-18.json).
- [Latest official screenshot ledger](../../data/nextwise_official_snapshots.csv).
- [Regression tests](../../tests/test_valuation_scenarios.py).

Run on Windows, after `python -m pip install -e ".[dev]"`:

```powershell
python scripts/valuation_scenarios.py
python -m pytest tests/test_valuation_scenarios.py -q
```

**Research boundaries:** scenario P/E and EPS deviations are assumptions, not confirmed analyst estimates or model-calibrated probabilities. The 18 Nov volatility/correlation data are historical and selected-universe contaminated. Company fundamentals are independently sourced as linked. The portfolio remains virtual. **No order placed.**

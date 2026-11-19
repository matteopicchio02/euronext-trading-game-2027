# Project Alpha 2027 — Investment Memo: ING Groep
**Review date:** 19 November 2026 (research snapshot, no orders)  
**Symbol:** INGA.AS · Euronext Amsterdam · EUR  
**Action:** **WATCHLIST / BUY NOT YET APPROVED**  
**Proposed test size:** EUR 1,000 from cash (~2.0% of NAV), 35 shares at an **illustrative** EUR 28.71 per share = EUR 1,004.85. This is not a verified NextWise executable quote.

## 1. Executive investment thesis

ING is a profitable, well-capitalized pan-European bank with growing fee and interest income. Its large approved repurchase programme and late-January earnings event may support the stock within the Trading Game horizon. However, the Q3 earnings miss, credit-cost uncertainties, negative 3-month momentum and increased portfolio volatility make this a **potential tactical addition**, not an automatic risk-adjusted improvement.

**Decision:** no order today pending stronger expected-return evidence, updated comparable market-data risk, and a check of the NextWise executable share price and dividend treatment.

## 2. Current Game account context

- Latest official NextWise screenshot supplied: NAV **EUR 49,875.21**, equities **EUR 40,199.45**, cash **EUR 9,675.76** (19.40%), displayed performance **-0.60% versus app's EUR 50,175.20 reference**, 19 November 2026.
- Participant reports quantities unchanged since the verified **21-name 18 November** screenshot. Individual 19 November position marks are **not** supplied. For this exercise, marked 18 November positions were uniformly rescaled to match the 19 November total stock value — an **analytical approximation, not the real distribution of daily price moves**.
- If exactly EUR 1,000 of frozen cash were moved into ING, cash would fall to **EUR 8,675.76 (17.39%)**, stock exposure to **82.61%**, and 22 equities would be present if filled.
- Projected financial-sector NAV weight goes from **12.74% to 14.75%**, with AXA, Generali and Euronext already in that sector. Paris-listed exposure remains about **41.14%**, above the **35% internal research monitor**, NOT an official Euronext mandatory limit.

## 3. Business and fundamental evidence

| Item | As-of verified evidence | Interpretation |
|---|---|---|
| 3Q26 net income | EUR 1.850bn, +3.5% year-on-year; **below Reuters-reported consensus of EUR 1.97bn** | Solid profit but negative surprise |
| Return on tangible equity | **16.3% in 3Q26**, 14.8% 4-quarter rolling | Profitability appears robust, but quarterly and trailing measures differ |
| CET1 | **13.3% at 30 September 2026**, vs reported CET1 requirement ~11.10% | Capital buffer above minimum, not risk-free |
| Fee income | EUR 1.273bn, +9.3% YoY | Revenue diversification |
| Credit cost | Provisions **EUR 403m**, including EUR 111m management overlay/model update | Credit/assumption sensitivity; distinguish model effect from worsening loan performance |
| 2026 outlook | Total income >EUR 24.5bn; ROTE >15%; CET1 ~13% | Management guidance, not a guaranteed outcome |
| 2027 outlook | Total income >EUR 26bn; ROTE >16%; CET1 ~13% | Main forecast window beyond current results |
| Shareholder return | EUR 1.65bn buyback announced 29 Oct 2026, expected end no later than 26 Apr 2027; EUR 250m additional January 14 2027 cash payment | Approximately 2% of market cap at 19 Nov quoted price and end-3Q shares; not all repurchases necessarily executed before 9 Apr game deadline |

**Valuation working check (not live):** FT indicated **EUR 28.71** on 19 Nov 2026 at ~11:43 GMT; quarter-end book equity per share **EUR 17.58** and four reported quarterly EPS **0.48 + 0.54 + 0.68 + 0.65 = EUR 2.35**. Thus illustrative **P/B ~1.63x**, trailing **P/E ~12.22x**. These ratios must be refreshed at an executable price. Neither multiple alone proves undervaluation.

**Catalysts prior to 9 Apr 2027:** Additional cash distribution ex-date provisionally **6 Jan 2027**, payable **14 Jan**; publication of **4Q26 results 28 Jan 2027**; regular buyback updates. The annual general meeting **13 Apr**, final dividend dates **15–23 Apr**, and expected latest buyback end **26 Apr** occur after the **9 Apr** game end. A cash distribution can cause an ex-dividend price adjustment; **NextWise handling is not verified**, so do not count this as free alpha.

## 4. Quantitative due diligence: matched cash-funded purchase

Model source: local `ALPHA_5_candidates_comparison.csv` generated in earlier Google Colab candidate screen (all **21 current tickers + five alternatives through 18 Nov 2026**). The file reports a **EUR 1,500** cash-funded ING candidate annualized volatility **9.437343%** versus base **9.056422%**, ING stand-alone volatility **24.6178%**, correlation with existing equity basket **0.487722**. For the **EUR 1,000** investment, this memo **solves the quadratic variance formula**, then approximates the current basket by uniform position-value scaling to the 19 Nov screenshot NAV.

| Indicator | No trade | Add EUR 1,000 ING |
|---|---:|---:|
| Annualized vol proxy | 9.0439% | **9.2946%** |
| 1-day Gaussian VaR 95% | EUR 467.37 | **EUR 480.33** |
| Diversification ratio | 2.3166 | **2.3072** |
| Equity-normalized HHI | 0.04969 | **0.04790** |
| Cash / NAV | 19.40% | **17.39%** |
| Financials / NAV | 12.74% | **14.75%** |
| Stock count | 21 | **22** |
| Internal Paris listing cap | 41.14% | **41.14%** |

**Caution:** historical covariance and candidate statistics refer to an **18 Nov return history**; no 19 Nov market-price/FX update was fed into the covariance estimator. Snapshot marks for each stock were **estimated by proportional rescaling**; these are *sensitivity estimates* not live risk measures.

ING historical momentum as of **18 Nov**: **−4.894% over 3 months**, **+7.268% over 6 months**. ING's 19 Nov indication at EUR 28.71 was above its previous close EUR 28.37, but this single day's bounce does not establish a trend reversal.

## 5. Compare five same-ticket alternatives (EUR 1,000 from cash)

| Ticker | Annual vol after | DR after | 3-month momentum at 18 Nov |
|---|---:|---:|---:|
| AD.AS (Ahold) | **9.1884%** | 2.3250 | +12.08% |
| ENEL.MI (Enel) | 9.2506% | 2.3062 | +0.61% |
| ASML.AS (ASML) | 9.2718% | **2.3476** | −16.17% |
| INGA.AS (ING) | 9.2946% | 2.3072 | −4.89% |
| SU.PA (Schneider Electric) | 9.3039% | 2.3279 | −19.79% |

All cash-funded purchases increase total historical portfolio volatility because a 19.4% cash sleeve becomes 17.4%; lower-vol candidates do not automatically have the best fundamental outlook. ING is **fourth of five** for minimizing post-trade vol and its DR decreases. Ahold has a softer risk footprint but company guidance/cyber risk. ASML offers greater DR but semiconductor valuation/volatility risk. This comparison does **not** rank future expected returns.

## 6. Probabilistic discipline / hurdle (illustrative)

The 1,000-euro scenario increases model vol by **~2.77% relatively**. If the unmodified portfolio were *hypothetically* expected to gain **6% between now and the tournament end**, the additional 2.005%-NAV ING allocation would need about **8.3% stock appreciation over the same period**, ignoring dividends/costs, just to keep the simple expected-return/volatility ratio unchanged. This is a **scenario hurdle, not a forecast**. No ING 5-month expected-return distribution has yet been validated.

For **35 shares at illustrative EUR 28.71** (EUR 1,004.85), a **−20% / −10% / +10% / +15%** move in ING alone translates to approximately **−EUR 201 / −EUR 100 / +EUR 100 / +EUR 151**, or **−0.40 / −0.20 / +0.20 / +0.30 percentage points** of current Game NAV; excludes distributions/corporate actions.

## 7. Investment Committee gate

**Decision: NO TRADE pending additional evidence.** The proposed ING buy is not shown to improve near-term risk-adjusted score. It could be considered at a small 2% allocation only if:
- a refreshed price and confirmable estimate of *expected* 5-month earnings/price upside are attractive,
- an updated daily-series covariance/correlation check (including ING and all 21 current assets) passes data-quality tests,
- no contradictory updates appear on provisioning, net interest margin, or 4Q expectations,
- NextWise quote, order status, share count and any cash distribution treatment are verified.

**Never place an order automatically.** Record authorization, then actual fills if/when separately confirmed. No NextWise trade was placed as part of this analysis.

## Sources (public/official)
- [ING 3Q26 earnings release (archived complete company release)](https://financialfilings.com/filings/ing-groep-nv/earnings-release/2026/74891412/)
- [SEC ING 3Q26 filed results](https://www.sec.gov/Archives/edgar/data/1039765/000117184326006947/exh_991.htm)
- [ING official buyback/cash distribution](https://ing.com/news/press-releases/ing-announces-new-distribution-programme-of-up-to-%E2%82%AC1.9-billion.html)
- [Reuters, 29 Oct 2026 earnings miss](https://www.reuters.com/business/finance/ing-unveils-165-billion-buyback-despite-profit-miss-2026-10-29/)
- [FT ING historical/intraday quote, 19 Nov 2026](https://markets.ft.markitdigital.com/data/equities/tearsheet/historical?s=INGA%3AAEX)

**Source boundary:** ING fundamentals/earnings/quote from cited public documents; portfolio values/quantitative scenarios from the user's actual screenshots and prior **18 Nov** Colab CSV exports; all pro forma numbers and hurdle scenarios are calculations, not source claims.

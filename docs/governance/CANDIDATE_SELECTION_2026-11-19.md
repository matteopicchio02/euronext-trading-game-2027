# Project Alpha 2027 — Five-candidate allocation gate
**As-of date:** 19 November 2026 (company disclosures available by this date; quantitative price panel ends 18 November)  
**Portfolio:** 21 confirmed positions, assumed unchanged; latest official NAV EUR **49,875.21**; cash EUR **9,675.76** (19.40%)  
**Decision:** **NO TRADE / CONDITIONAL WATCHLIST** — not an automated NextWise execution decision

## Executive conclusion

The existing portfolio has a **9.0439% annualized historical volatility proxy** after *uniformly rescaling* its 18 November stock weights to match the total 19 November equity value. This **does not reconstruct the actual 19 November stock-level marks**.

Across **EUR 1,000 purchases funded from cash**, **AD.AS (Ahold Delhaize)** adds the least modeled risk. ING has a more explicit bank-capital-return thesis but the new sector sleeve and higher covariance with the existing holdings reduce portfolio-level risk efficiency. ASML has exceptionally strong disclosed Q3 operations and the highest diversification ratio after a new cash-funded position, but it has the highest standalone volatility and weak historical six-month momentum. None has a prospectively validated expected-return distribution or an independently confirmed current executable NextWise quote.

**Prioritize fundamental/risk review in this order for a first incremental EUR 1,000 research tranche:** Ahold Delhaize, ING, ASML. Hold Enel and Schneider Electric in the broader watchlist. **The order is an analyst-review priority, not a forecast or a recommendation to buy now.**

## Methodology and reproducible inputs

- Model input: the user-supplied `ALPHA_5_candidates_comparison.csv`, `ALPHA_candidate_data_quality.csv`, and `data/portfolio_actual_2026-11-18.csv`. Price-history statistics end 18 November, are not live, and have known corporate-action/FX caveats.
- All five cash-funded candidate records in the 20-scenario Colab export refer to **EUR 1,500** buys; we re-sized to EUR 1,000 by the *variance-covariance identity*, **not by linearly scaling total volatility**.
- Portfolio equity exposure scaling factor `k = (40199.45 / 49875.21)/(40488.99 / 50164.75)`. Original candidate base sigma `9.0564218%`, latest rescaled **9.0438578%**.
- Candidate standalone volatilities `sigma_c`, covariance correlations `rho` with existing *stock portfolio*, and `w = ticket / 49875.21`.
- New NAV volatility `sigma_new = sqrt(sigma_base^2 + (w*sigma_c)^2 + 2*w*sigma_base*sigma_c*rho)`. Cash is assumed to have zero return/volatility.
- New diversification ratio `DR_new = (DR_base*sigma_base + w*sigma_c)/sigma_new`, under the static-risk assumption. Baseline from same candidate pipeline: **DR_base = 2.316565**.
- New equity-only HHI `HHI_new = (E/(E+ticket))^2*HHI_old + (ticket/(E+ticket))^2`, where E is the original modeled equity value and `HHI_old = 0.04969054`.
- A **0.15 annual-volatility percentage-point per-new-position risk budget** is a new **research constraint**, NOT official ETG rules; the maximum notional solves the same quadratic equation at `sigma_new = sigma_base + 0.0015`.

### Candidate scorecard: EUR 1,000 financed by cash

| Ticker | 3m momentum* | 6m momentum* | Standalone ann. vol* | Corr. existing stocks* | Ann. NAV vol after | Added vol in pp | DR after | Max illustrative ticket at +0.15pp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **AD.AS** Ahold Delhaize | +12.08% | -2.62% | 20.57% | 0.3303 | **9.1884%** | **+0.1445** | 2.3250 | **EUR 1,036** |
| ENEL.MI Enel | +0.61% | -0.14% | 19.11% | 0.5246 | 9.2506% | +0.2068 | 2.3062 | EUR 731 |
| ASML.AS ASML | -16.17% | -9.05% | 40.67% | **0.2380** | 9.2718% | +0.2279 | **2.3476** | EUR 689 |
| INGA.AS ING | -4.89% | +7.27% | 24.62% | 0.4877 | 9.2946% | +0.2507 | 2.3072 | EUR 608 |
| SU.PA Schneider Electric | -19.79% | -12.87% | 35.33% | 0.3333 | 9.3039% | +0.2601 | 2.3279 | EUR 599 |
| **BASE** no trade | — | — | — | — | **9.0439%** | 0.0000 | 2.3166 | — |

`*` Estimated from the Colab historical panel to **18 Nov**; numbers are unverified for 19 Nov. For **each** candidate ticket, cash drops from EUR 9,675.76 to EUR 8,675.76, about **17.39% of NAV**; equity-only HHI improves to approximately **0.04790**. All five names belong to sectors already represented in the portfolio, so **sector count does not increase**. SU.PA adds exposure to Paris, already around **41.14% of NAV** vs a 35% **house research monitor**, not an official tournament restriction.

The quality export flags **no daily >15% adjusted-return events** for these five candidates. It is not a full audit of all historical split/dividend/FX adjustments.

### Required expected-return hurdle: illustrative, NOT a forecast

If we **hypothetically** expect the original portfolio to return **+6% from 19 November to the 9 April 2027 contest end**, cash earns zero and nothing else changes, a standalone candidate must return at least the following over that same period to keep the portfolio's *simple expected return / modeled volatility* ratio unchanged:

| AD.AS | ENEL.MI | ASML.AS | INGA.AS | SU.PA |
|---:|---:|---:|---:|---:|
| **+4.78%** | +6.84% | +7.54% | +8.30% | +8.61% |

Derivation `r_c >= 0.06*(sigma_new/sigma_base - 1)/(1000/49875.21)`. These are scenario break-even returns, **not price targets, true Sharpe ratios, confidence levels, or statistical alpha forecasts**. The inputs have estimation noise and cash/interday transaction assumptions. Without credible candidate-specific expected returns, the correct decision is **not** to claim the hurdle is met.

## Fundamental/catalyst gate (company disclosures)

### 1. Ahold Delhaize — AD.AS (risk-efficient, but a changed earnings thesis)
**Pro:** Q3 sales EUR 23.1bn, online sales +8.2% constant FX, underlying operating margin 4.1%. Company announced **EUR 1bn share repurchase programme starting early 2027**. Q4/FY26 report expected **17 February 2027**, before the game finishes.

**Con:** October cyber incident is expected to depress Q4 sales by **EUR 200m–250m** and operating income by **EUR 75m–100m**. 2026 EPS growth guidance reduced to low-single-digits (was mid/high-single-digits), FCF outlook reduced to **~EUR 2.1bn** (was >=EUR 2.3bn). The positive 3m momentum sits alongside slightly negative 6m momentum, so the trend is not uniformly strong.

**Before considering any entry:** confirm no deterioration beyond management's stated loss estimates, check Q4 consensus EPS revisions, refreshed valuation, and NextWise price. The share-buyback programme is *not* guaranteed share-price appreciation.

Sources: [official Q3 release, 4 Nov 2026](https://newsroom.aholddelhaize.com/ahold-delhaize-reports-resilient-q3-2026-results-and-updates-2026-guidance-to-reflect-business-disruption-caused-by-recent-cybersecurity-incident); [corporate calendar](https://aholddelhaize.com/investors/events).

### 2. ING — INGA.AS (clear capital return; weak marginal DR)
**Pro:** Q3 net income **EUR 1.85bn**, ROTE **16.3%**, CET1 **13.3%**, and share repurchase up to **EUR 1.65bn** starting 29 Oct 2026, expected no later than 26 Apr 2027. Q4 results scheduled for **28 January 2027**, within contest window.

**Con:** Reuters reported a net-income shortfall versus consensus, with higher credit provisioning; sector financial risk already includes AXA, Generali and Euronext. The proposed EUR 1,000 buy pushes +0.25pp modeled volatility and slightly worsens diversification ratio.

**Candidate size under research risk budget:** about **EUR 600**, rather than the initial EUR 1,000. Need earnings revisions and executable valuation before approval.

Sources: [ING Q3 2026 release](https://ing.com/news/press-releases/3q2026-ing-press-release.html); [company buyback programme](https://ing.com/investors/share-information/share-buyback-programme).

### 3. ASML — ASML.AS (strongest operational growth evidence, high variance)
**Pro:** Q3 sales **EUR 11.7bn**, net income **EUR 5.0bn**, gross margin **57.5%**; 2026 sales outlook **EUR 44–45bn** and Q4 **EUR 14.2–15.2bn**. Official Q4/FY26 earnings date **27 January 2027**.

**Con:** ~40.7% historical stand-alone annual volatility and negative 3m/6m momentum. Semiconductor export controls, capital-spending cycles and valuation multiple shifts can dominate the near-term return even if business results grow.

**Candidate size under research risk budget:** about **EUR 690**. Do not extrapolate Q3 net income into an annual EPS forecast or buy after an intraday rebound without an independently refreshed price/valuation.

Sources: [ASML Q3 results](https://www.investor.asml.com/news-releases/news-release-details/asml-reports-eu11.7-billion-total-net-sales-and-eu5.0-billion-net-income-q3-2026); [interim report calendar](https://www.sec.gov/Archives/edgar/data/937966/000162828026048235/statutoryinterimreport20.htm).

### 4. Enel — ENEL.MI (quality income, weak increment to sector diversification)
**Pro:** Nine-month ordinary net income **EUR 6.018bn (+6%)**, revenues **EUR 65.022bn (+8.9%)**, management 2026 EPS outlook around **EUR 0.74**, at high end of guidance.

**Con:** Weak historical momentum, higher correlation **0.525** to existing stocks, Italian margin pressure, utility-sector overlap with EDP and Snam. This is not a novel sector in the portfolio.

**Candidate size under research risk budget:** about **EUR 730**; do not add until the utility-overlap and P/E at live price are assessed.

Source: [Enel company release, 12 Nov 2026](https://www.enel.com/media/explore/search-press-releases/press/2026/11/enel-in-the-nine-months-of-2026-growth-in-results-is-led-by-spain-and-the-americas-while-margins-in-italy-continue-to-decline).

### 5. Schneider Electric — SU.PA (operational momentum, extra Paris exposure)
**Pro:** Q3 revenue **EUR 11.46bn**, organic growth **16.9%**; upgraded 2026 adjusted EBITA growth guidance **18–21%** on strong data-center infrastructure demand.

**Con:** PTC acquisition funding/integration risk, historical weak share-price momentum and additional Paris-listing exposure; PTC closing anticipated in **Q3 2027**, after game end. Strong trailing growth does not imply cheap valuation.

**Candidate size under research risk budget:** about **EUR 600**, but lowest implementation priority until valuation and house geographical concentration decision are clarified.

Sources: [Euronext/Reuters 16 Oct 2026](https://live.euronext.com/en/financial-news/schneider-electric-raises-2026-targets-again-booming-data-centre-demand), [PTC transaction announcement](https://www.ptc.com/en/news/2026/schneider-electric-to-acquire-ptc).

## One-decision discipline and trade triggers

**No new order now.** To authorize one **later**:
1. Obtain current comparable quote, P/E (forward where possible), guidance revisions and a dated catalyst fully within 9 Apr 2027.
2. Verify the account's actual post-trade market weights and covariance with synchronized EUR market prices; stress an event loss and the sector concentration.
3. Confirm that the prospective upside estimate, with a quantified downside and explicit assumptions, exceeds the **scenario hurdle**, and is not merely an extrapolation of historical momentum.
4. Choose a size under the *research* +0.15pp risk-budget cap, account for share-rounding on NextWise and any pending orders.
5. Record a new, date-stamped trade memo with explicit approval **before** placing orders. Record actual fills only after confirmation; *never* imply GitHub Actions can trade on NextWise.

**Immediate research priorities:** Ahold cyber-related EPS revisions and 2027 buyback execution; ING forward credit cost/earnings revisions; ASML valuation and January earnings. Retain existing 21 holdings until a real trade is authorized. Rankings remain unavailable before month-end.

No official ETG scoring weights, 2027 price targets, consensus forecast datasets, or live NextWise executable prices have been verified for this decision. The research priority ranking is **not** a calibrated return forecast or investment advice.

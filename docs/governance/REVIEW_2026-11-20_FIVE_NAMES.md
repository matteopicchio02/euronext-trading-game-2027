# Project Alpha 2027 — Fundamental decision review (20 November 2026)

**Purpose:** move from passive drawdown monitoring to a ranked, executable research agenda for the five largest recent stock contributors. **No NextWise order created here.**
**As-of data:** 20 Nov 09:54–09:55 Europe/Rome screenshot; 21 actual positions, NAV EUR **49,519.84**, equity **39,844.08**, cash **9,675.76**. All 21 prices are screenshots, NOT synchronized official market closes. Ahold 25 AD.AS at limit EUR 34.30 is **user-reported PENDING**, not counted in holdings.

## Decision thesis and actions

| Priority | Name / ticker | 20 Nov quantity and EUR mark | P&L change from 18 Nov | Company evidence available by 20 Nov | Desk action |
|---|---|---:|---:|---|---|
| 1 | Dassault Systèmes / DSY.PA | 90, EUR 2,049.30 | EUR −61.20 | Management presented 2029 revenue > EUR 8bn and non-IFRS EPS EUR 1.80; Jefferies and Citi reported that the revised 2029 ambition is below prior expectations. 2026 outlook had improved but 2029 targets have a poor fit with the Apr 2027 contest horizon. | **REDUCE-WATCH**: investigate a conditional 30-share trim; NO unconfirmed sell order |
| 2 | Prysmian / PRY.MI | 18, EUR 1,857.60 | EUR −85.50 | Q3 organic growth +13.1%; management raised adjusted EBITDA guidance with Atkore contribution. Price weakness alone does not invalidate the industrial thesis. | HOLD; inspect valuation/Atkhore integration, historical raw/adjusted split data |
| 3 | Equinor / EQNR.OL | 49, EUR 1,761.86 (reconciled), NOK capital 18,909.10 | EUR −49.71 | Reuters 20 Nov reports cyberattack stopped, no production disruption or known data theft/changes. Risk remains crude, gas, NOK/EUR and subsequent distributions. | HOLD; update NOK-to-EUR attribution and oil/gas sensitivity |
| 4 | Michelin / ML.PA | 62, EUR 1,943.70 | EUR −53.94 | Group confirmed FY26 guidance; >EUR 1.6bn pre-M&A FCF targeted; Q3 underlying demand and margins require monitoring. | HOLD / MONITOR, earnings 11 Feb 2027 |
| 5 | Capgemini / CAP.PA | 15, EUR 1,743.00 | EUR −45.75 | Q3 revenues EUR 6.073bn, +11.7% constant FX; 2026 growth target raised to 9–9.5%, free cash flow target maintained. | HOLD, avoid reactive sale; FY26 earnings 16 Feb 2027 |

**Sector pressure:** industrials, technology and energy jointly lost EUR 324.61 of EUR 644.91 screenshot-to-screenshot NAV change. This aligns with a broad 20 November European risk-off / tech decline; it is not full factor regression or a causal attribution.

## Proposed, NOT authorized, next rotation: DSY partial trim conditional on Ahold outcome

- **Potential sale:** 30 of 90 DSY shares, leaving 60 (two-thirds of the position) *only after fresh valuation and review of the pending Ahold order*. This is a deliberate business-quality and timing decision, NOT a stop-loss or a loss recovery trade.
- **For illustration ONLY**, at the 20 Nov screenshot price EUR **22.77**, gross proceeds **EUR 683.10**. This quote is **not** a fresh executable market price. Weight reduction approx EUR 683.10 / EUR 49,519.84 = **1.38% of NAV**.
- A 10% additional DSY-only drop on 90 screenshot-price shares would affect NAV by ~EUR −204.93 versus ~EUR −136.62 after the proposed trim: EUR **68.31** difference in this *static isolated hypothetical*.
- **If** Ahold 25 shares fills at the proposed EUR 34.30 limit (max EUR 857.50), and **if** 30 DSY shares separately sell at the illustrative EUR 22.77, with other prices unchanged: net equity exposure grows **EUR 174.40**; cash falls from EUR 9,675.76 to about **EUR 9,501.36 (19.19% of NAV)**. This is an illustration of portfolio composition, **not a forecast or a booked transaction**.
- If Ahold remains pending, there is no confirmed equity redeployment, and an immediate DSY trim increases already-high cash. Thus a DSY sale is **not recommended solely to raise liquidity**.
- The trade is **not authorized** by this memo, and no sale limit price is specified. Review current NextWise quote/conditions, market spread, potential rebound/earnings catalysts, and revised market-wide drawdown before considering an order.

## Pending Ahold anti-duplication guard

- NextWise order is participant-reported **PENDING**, 25 AD.AS shares, limit **EUR 34.30**. No expiry visible. It is NOT yet a 22nd holding.
- `data/price_review_levels_2026-11-20.json` now indicates the user-reported pending status; the nightly read-only price reviewer emits **PENDING_ORDER_VERIFY_WITH_NEXTWISE** rather than a new buy prompt.
- The automation cannot know if an order is filled, expired or canceled: manually update its dated status before submitting additional orders.
- Keep the daily portfolio monitor on its **18 Nov full-day historical anchor** for now; the validated 20 Nov position snapshot is intraday and cannot simply substitute for the day's Yahoo closing price without a basis mismatch. After a **synchronized post-close NextWise snapshot**, update `data/monitor_config.json` and tests to its matched anchor date, remembering to reflect any filled Ahold shares.

## Calendar — catalysts before contest end (9 April 2027)

| Date | Company | Event | Verification |
|---|---|---|---|
| **3 Feb 2027** | Dassault Systèmes | FY2026/Q4 earnings | https://investor.3ds.com/news-releases/news-release-details/dassault-systemes-strong-q3-performance-improved-fy26-objectives |
| **3 Feb 2027** | Equinor | Q4/FY2026 earnings | https://www.equinor.com/investors |
| **11 Feb 2027** | Michelin | FY2026 results | https://www.michelin.com/en/investors/presentation-events |
| **16 Feb 2027** | Capgemini | FY2026 results | https://investors.capgemini.com/en/calendar/ |
| **4 Mar 2027** | Prysmian | FY2026 financial results / presentation | https://www.prysmian.com/it/media/comunicati-stampa/calendario-degli-eventi-societari-anno-2027 |
| **9 Apr 2027** | Euronext Trading Game | Competition concludes | Official Euronext materials |

**Other 5 alternative candidates:** Ahold has pending order; ING, ASML, Enel and Schneider Electric remain research watchlist only. None has a verified near-term prospective return distribution justifying an immediate second cash-funded order.

## Sources — dated by 20 Nov 2026

- Prysmian management outlook: https://www.prysmian.com/en/investors/prysmian-as-investment/market-outlook
- Prysmian 2027 investor event calendar: https://www.prysmian.com/it/media/comunicati-stampa/calendario-degli-eventi-societari-anno-2027
- Dassault Nov 17 CMD: https://investor.3ds.com/news-releases/news-release-details/dassault-systemes-2026-capital-markets-day-new-industrial-era/
- Dassault Q3, Feb 3 earnings date: https://investor.3ds.com/news-releases/news-release-details/dassault-systemes-strong-q3-performance-improved-fy26-objectives
- Analyst reaction, Jefferies/Citi: https://www.marketscreener.com/news/dassault-systemes-fails-to-convince-with-new-targets-ce785edfd08df120
- Capgemini Q3: https://www.capgemini.com/news/press-releases/q3-2026-momentum-drives-upgrade-in-capgeminis-2026-outlook/
- Michelin: https://www.michelin.com/en/investors/presentation-events/results-sales
- Equinor cyber status (Reuters 20 Nov): https://www.reuters.com/business/energy/equinor-says-cyberattack-against-company-has-been-stopped-2026-11-20/
- Broad market weakness 20 Nov (Reuters): https://www.reuters.com/markets/europe/european-shares-head-steepest-weekly-drop-since-march-2026-11-20/

**Caveat:** historical model volatility changed from 8.88/9.05% to ~7.54% on a 252-session Yahoo close pipeline. These are different methods, not interchangeable live risk claims. The only executed Trading Game changes must come from confirmed NextWise fills. No trading execution is performed by GitHub or this memo.

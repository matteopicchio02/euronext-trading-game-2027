# Project Alpha — Trading desk action plan, 19 November 2026
**Purpose:** execute today's research/process actions without forcing trades.  
**Status:** **21 current positions maintained; no new buy or sell order authorized**.

## Source snapshots and observed quotes
- NextWise as supplied: 21 holdings unchanged according to participant; NAV **EUR 49,875.21**, equities **EUR 40,199.45**, cash **EUR 9,675.76**; last screenshot around 14:03 Europe/Rome.
- Midday 19 Nov public market quotations: Ahold **around EUR 34.25–34.36** and ING **around EUR 28.68–28.75**, observed at different times/sources. These are **not executable NextWise quotes**.
- The [Ahold–ING scenario valuation](VALUATION_AHOLD_ING_2026-11-19.md) offers no validated positive expected risk-adjusted return edge at those indicative prices.

## Today's actionable decisions
1. **NO TRADE today** at indicative prices. Do not sell recent losers simply to react to a small NAV dip, do not use cash solely to become more active.
2. **Review-only levels:** Ahold **EUR 33.00 or below**, ING **EUR 27.00 or below**. They are NOT limit orders, buy signals or hard support levels. A price decline could represent deteriorated fundamentals, so require EPS, guidance, cyber/credit-risk and updated variance checks before any decision.
3. **Continue watching the two dated earnings catalysts:** ING fourth-quarter results **28 Jan 2027** and Ahold full-year results **17 Feb 2027**, both prior to 9 Apr 2027 Game end.
4. **Independent post-close monitoring:** original 21-position indicative NAV/risk estimator at 20:37 UTC and new candidate-price research workflow at 20:53 UTC. GitHub scheduled runs may be delayed or skipped; inspect workflow logs, not a presumed notification.
5. **NextWise orders:** participant says holdings unchanged, but no complete pending-order history/export is available. Do not certify that all pending orders are empty without inspecting NextWise.
6. **Reassess on a validated trigger** (price review level plus unchanged earnings thesis, material new company information, limit breach, or first published monthly ranking), not on arbitrary intraday fluctuation.

## Monitoring automation, no broker linkage
- [Review-only rules](../../data/price_review_levels_2026-11-19.json)
- [Python price reviewer](../../scripts/watchlist_price_review.py)
- [Nightly workflow](../../.github/workflows/candidate_price_review.yml)
- Daily review reports will appear at `reports/watchlist/` **only after the first successful run**
- [21-stock post-close estimated portfolio monitor](../../.github/workflows/daily_monitor.yml)

**Important:** A GitHub watchlist output is merely a report in the repository; no phone/email alert is promised. A failed or stale market-data request produces no false quote. No NextWise login, no orders, no access credentials and no real-money trades.

## External public sources
- [Ahold market quote (19 Nov)](https://ae.marketscreener.com/quote/stock/AHOLD-DELHAIZE-N-V-29752127/quotes/)
- [ING market quote (19 Nov)](https://uk.marketscreener.com/quote/stock/ING-GROEP-N-V-56358303/)
- [Ahold Q3 and cybersecurity guidance update](https://newsroom.aholddelhaize.com/ahold-delhaize-reports-resilient-q3-2026-results-and-updates-2026-guidance-to-reflect-business-disruption-caused-by-recent-cybersecurity-incident)

No trades executed by this research work.

# Project Alpha 2027 — Morning portfolio research review (23 Nov 2026)

**Personal MSc research notes · 23 November 2026, approx 10:30 CET.**
**Source hierarchy:** user-observed NextWise values from dated screenshots; user-confirmed virtual transactions in GitHub; external public financial and corporate news published up to this morning. **No new orders placed.**

## 1. Facts from NextWise and our position ledger

| Item | Verified historical observation |
|---|---:|
| Latest observed NextWise NAV (23 Nov, 10:15 CET) | **EUR 49,334.92** |
| Displayed NextWise total performance | **−1.67%** |
| Previous observed NextWise NAV (20 Nov, around 18:05) | **EUR 49,322.18** |
| Difference between those screenshots | **+EUR 12.74 (+0.0258%)** |
| Nominal difference from original EUR 50,000 virtual game endowment | **−EUR 665.08 (−1.3302%)** |
| Latest confirmed cash (20 Nov evening, **not** today's cash) | **EUR 8,336.86 (16.90% of 20 Nov NAV)** |
| Latest confirmed equities value (20 Nov evening, **not** today's value) | **EUR 40,985.32 (83.10% of 20 Nov NAV)** |
| Tracked share positions | **23** (from dated 20 Nov user-confirmed execution ledger) |

The 23 Nov **profile** screenshot showed NAV and performance **only**, not cash, executions or individual stock marks. Do not extrapolate today's exact cash, VaR or exact position P&L from this incomplete account screen.

Post-trade quantity changes 20 Nov: **DSY.PA 90 → 60** after a **30-share** sale at confirmed **EUR 22.75**; **AD.AS 25** and **UNA.AS 20** added after buy orders user-confirmed executed. The individual Ahold/Unilever execution prices are **unverified**, so order limits of EUR 34.30 and EUR 58.40 must **not** be recorded as fills.

## 2. How the 23 names are distributed

**Important:** the following measure is *count of distinct positions*, not percentage capital or correlation-weighted risk.

| Sector (project's own labels) | Names | Count |
|---|---|---:|
| Consumer Staples | Heineken, L’Oréal, Ahold Delhaize, Unilever | 4 |
| Financials | AXA, Generali, Euronext | 3 |
| Energy | Eni, Equinor, TotalEnergies | 3 |
| Technology | Capgemini, Dassault Systèmes | 2 |
| Industrials | Airbus, Prysmian | 2 |
| Utilities | EDP, Snam | 2 |
| Consumer Discretionary | Ferrari, Michelin | 2 |
| Health Care | Sanofi, UCB | 2 |
| Basic Materials | Air Liquide | 1 |
| Telecommunications | KPN | 1 |
| Real Estate | Klépierre | 1 |
| **Total** | | **23 names / 11 sectors** |

**Listing venue count:** Paris **11**, Milan **5**, Amsterdam **4**, Lisbon **1**, Brussels **1**, Oslo **1**. The Paris count **11/23 = 47.83% of names** is **not** Paris's NAV weight and is not France's economic revenue exposure. Previous Paris/NAV exposure measures are stale after the trades; do not quote them as current.

## 3. Market context this morning

Reuters **23 November 2026, 08:25 UTC**: European equities recovered in the morning after a severe previous-week technology-led selloff; the broad STOXX 600 had dropped **almost 6% the previous week**. This is a tentative market rebound, **not evidence that all 23 holdings are up today**.
https://www.reuters.com/markets/europe/european-stocks-recover-after-steep-technology-led-selloff-2026-11-23/

Reuters/Euronext news **23 Nov**: Brent/oil prices weakened somewhat in early trade and are exposed to expected 2027 supply balance, Gulf attacks and the **OPEC+ November 29** decision. Applies qualitatively to the **three** energy positions, not a measured portfolio P&L.
https://live.euronext.com/en/financial-news/oil-prices-fall-amid-equity-selloff-though-iran-war-attacks-limit-losses

## 4. Five research checks in priority order

1. **Dassault Systèmes (DSY.PA, 60 shares) and Capgemini (CAP.PA, 15):** keep the DSY partial risk reduction documented; watch if the tech rebound holds and whether 2029 DSY targets/guidance influence analyst revisions. The older portfolio model's 7.54% volatility was on **21 old positions**, so it is **not** today's risk.
2. **Eni (55), Equinor (49), TotalEnergies (26):** three securities share commodity/oil risk; Equinor also has **NOK/EUR** valuation exposure. Do not attribute share-price moves solely to oil or FX until measured using synchronized marks and FX.
3. **New Ahold Delhaize (AD.AS, 25):** management's Q3 2026 statement identifies an October cybersecurity disruption and reduced outlook, while confirming **EUR 1bn buybacks in 2027**. The risk is the extent and timing of any earnings recovery before the contest ends. Source: https://newsroom.aholddelhaize.com/ahold-delhaize-reports-resilient-q3-2026-results-and-updates-2026-guidance-to-reflect-business-disruption-caused-by-recent-cybersecurity-incident/
4. **New Unilever (UNA.AS, 20):** Q3 underlying sales growth **5.2%**; guidance **4–6% FY2026 underlying sales growth** and modest operating-margin improvement. Follow execution of the business simplification, portfolio deals and FX. Source: https://www.unilever.com/news/press-and-media/press-releases/2026/continued-strong-performance-in-the-third-quarter/
5. **Prysmian (18), Michelin (62), Airbus (7):** cyclical industrial/consumer sensitivity. Avoid interpreting a broad market selloff alone as a company-specific impairment; compare industry and updated earnings before any trade.

## 5. Simple educational portfolio downside stresses

This is a **static scenario**, not a forecast, a VaR estimate or the official NextWise loss calculation. Use the **last fully reported** 20 Nov evening **EUR 40,985.32 equities**, **EUR 8,336.86 cash**, and NAV **EUR 49,322.18**. Assumes cash unchanged, no dividends/fees/FX revaluation beyond equity shock, and all equities fall by the same amount.

| Hypothetical parallel equity decline | Equity impact EUR | Percent of 20 Nov NAV |
|---|---:|---:|
| −3% | −1,229.56 | −2.49% |
| −5% | −2,049.27 | −4.15% |
| −8% | −3,278.83 | −6.65% |
| −10% | −4,098.53 | −8.31% |

This is **not** a prediction of an identical 5% move in every holding; correlation and FX are not captured. It illustrates that the equity allocation still creates meaningful downside even with 16.90% cash.

## 6. Decision for the morning

**MAINTAIN existing positions for now; NO NEW ORDER.** The rationale is:
- Three virtual transactions were already completed on 20 Nov, expanding from 21 to 23 holdings.
- The new market-price watcher has **passed offline CI tests**, but **no successful real-world 23-stock Yahoo daily-price report** is yet present in `reports/market_watch/latest.md`. The first scheduled run occurs after Europe's market close, not in the morning. We cannot truthfully assign today's per-stock EUR contributions yet.
- We have no new company-specific news this morning that alone justifies another trade without price/weight verification.
- Keep cash allocation as a **dated observation**. Never fill missing Ahold/Unilever execution prices from the two proposed limits.
- After a full successful nightly price watch, rank contributions by EUR, % NAV, and sector covariance. Review the top three loss contributors and only then formulate any new **proposed** orders for the user.

### What is automatic versus manual

- **Automatic:** public close prices for 23 tickers, NOK/EUR conversion, scenario risk and dated report with explicit source/anchor caveats. Code: `scripts/holdings_market_watch.py`; schedule: `.github/workflows/market_watch_23.yml`. A run may fail on stale/missing vendor data and must not create a fabricated report.
- **Manual event only:** new NextWise orders, actual fills, quantity changes, dividends, platform cash. User does *not* need to send 23 screenshots for everyday research; only communicate account changes and occasionally a total-account checkpoint.

## Provenance

- [23 share quantities](../../data/positions_after_buys_2026-11-20.csv).
- [User-reported transaction record](../../data/trade_events_2026-11-20.csv).
- [Last reported full account reconciliation](../snapshots/EXECUTED_BUYS_2026-11-20_1805.md).
- [23 Nov 10:15 NextWise profile snapshot](../snapshots/NEXTWISE_PROFILE_2026-11-23_1015.md).
- [Market watch methodology](../../docs/monitoring/MARKET_WATCH_23.md).

**No orders submitted by this research process.**

# Project Alpha 2027 — Complete Position Attribution
**20 November 2026, 09:54–09:55 Europe/Rome · 21/21 NextWise equity cards reconciled**

> Screenshot-based research valuation of a **virtual** competition account, **not** a live broker integration, an executed-trade ledger, an official score or a market-close price. All values here are as displayed or arithmetically reconciled from screenshots.

## Final portfolio reconciliation

| Reconciliation | 18 Nov snapshot | 20 Nov snapshot | Difference |
|---|---:|---:|---:|
| Total NAV (EUR) | 50,164.75 | **49,519.84** | **−644.91** |
| Marked equities (EUR) | 40,488.99 | **39,844.08** | **−644.91** |
| Cash (EUR) | 9,675.76 | **9,675.76** | 0.00 |
| Sum of per-position unrealized card P&L (EUR) | −10.46 | **−655.37** | **−644.91** |
| Portfolio positions | 21 | 21 | 0 |
| Observed quantities matching prior snapshot | 21 | 21 | No net count change |
| Residual after equity/cash/P&L reconciliation | — | **0.00** | — |

The 20 previously observed cards accounted for **−EUR 636.99** in displayed EUR P&L changes. The final **Air Liquide** card shows 12 shares, value **EUR 2,268.96**, cumulative P&L **+EUR 53.28**, compared with EUR 2,276.88 and +EUR 61.20 on 18 November: exactly **−EUR 7.92**. Thus **−636.99 − 7.92 = −644.91**, matching the account NAV movement.

The nominal loss versus the original EUR 50,000 contest endowment is **EUR −480.16 (−0.960%)**. The application displays **−1.31%**, which follows a different in-app reference (EUR 50,175.20 on earlier screenshots). The screenshot comparison **−1.286%** from 18 Nov is a separate calculation, not the official cumulative performance measure.

## Current composition (research metrics)

- NAV in equity securities: **EUR 39,844.08**, or **80.4608%**; cash **EUR 9,675.76 = 19.5392%**.
- Equity-only normalized HHI approx **0.04973**, effective equal-size count approx **20.11**.
- Exposure to instruments **listed in Paris** approx **41.06% of NAV**, against an internal 35% *research monitor*, **not** an official competition limit. Venue is not country-of-economic-exposure.
- These measures do **not** update annualized volatility, expected returns, Sharpe, risk-adjusted score or a time-series VaR: doing that would require contemporaneous and validated prices/covariance.

## Market data / FX interpretation

The Equinor card presents **49 shares**, quote **NOK 385.90**, local capital **NOK 18,909.10**, and a **EUR −231.17** cumulative position P&L. To avoid summing NOK as EUR, the current EUR marked value **EUR 1,761.86** is explicitly tagged **INFERRED**, as:

```
Equinor EUR value = total NextWise NAV − cash − sum(EUR market values of other 20 cards)
                   = 49,519.84 − 9,675.76 − 38,082.22
                   = 1,761.86 EUR
```

A cross-check independent of this subtraction is 18 Nov EUR marked Equinor value **1,811.57** plus change in card EUR P&L **−49.71**, also **1,761.86**. The implied NOK/EUR valuation ratio from rounded displayed amounts is **10.7325 NOK/EUR**. This is *not* an independently observed live currency rate or exact settlement FX.

## Six largest two-day contributors (EUR)

| Position | Change 18→20 November | Cumulative card P&L on 20 Nov |
|---|---:|---:|
| Prysmian | −85.50 | −126.90 |
| Dassault Systèmes | −61.20 | −244.98 |
| Michelin | −53.94 | −49.60 |
| Equinor | −49.71 | −231.17 |
| Sanofi | −47.50 | +135.75 |
| Capgemini | −45.75 | −158.25 |
| **Subtotal** | **−343.60** | |

These six names explain **53.3%** of the EUR 644.91 screenshot-to-screenshot NAV difference. All 21 position values and EUR card P&Ls deteriorated over this window (no evidence about the direction of future returns).

## Attribution by internal sector (EUR)

| Sector | Change in card P&L |
|---|---:|
| Industrials | −111.68 |
| Technology | −106.95 |
| Energy | −105.98 |
| Consumer Discretionary | −83.19 |
| Health Care | −67.10 |
| Consumer Staples | −55.80 |
| Financials | −50.01 |
| Utilities | −43.68 |
| Telecommunications | −9.24 |
| **Basic Materials (Air Liquide)** | **−7.92** |
| Real Estate | −3.36 |
| **All 21 names** | **−644.91** |

The three largest sector buckets (industrials, technology and energy) account for **EUR −324.61**, about 50.3% of the NAV difference. Sector labels are an internal classification, not confirmed Euronext/NextWise scoring taxonomy.

## Interpretation and next trade gate

**Research decision: HOLD / NO NEW ORDER from this workflow, pending thesis review.** This is not a representation that all earlier NextWise orders or fills have been independently checked. Although quantities match on two dates and visible cash is unchanged, **intervening trades that restore the same quantities cannot be ruled out** without inspecting the Orders/Transactions tabs.

Review fundamentals and upcoming catalysts, particularly for **Prysmian, Dassault Systèmes, Michelin, Equinor and Capgemini**, before approving any changes. Do not interpret negative purchase-to-date P&L as sufficient evidence for a sale, and do not buy merely to restore the nominal EUR 50,000 benchmark.

Verify the quote-period anomaly on Euronext's card (adjacent red **−7.43%** versus this position's **EUR −14.40** 18→20 value change) and the FX/corporate-action adjustments before running the next risk report. Cross-period values are not necessarily synchronized to a consistent market close.

## Provenance and reproducibility

- **Current complete data:** [21-name dated snapshot](../../data/portfolio_actual_2026-11-20.csv).
- **Prior dated data:** [18 November actual holdings](../../data/portfolio_actual_2026-11-18.csv).
- **NAV screenshot record:** [Snapshot history](../../data/nextwise_nav_snapshots.csv).
- [Previously partial attribution](POSITION_ATTRIBUTION_2026-11-20.md) preserved as research history, superseded by this completed report.
- **Still unavailable:** authoritative NextWise transaction/fill ledger, real-time data-feed access, exact currency settlement quote, synchronized close-to-close NAV and official scoring weights.

This data refresh **does not authorize or place trades**.

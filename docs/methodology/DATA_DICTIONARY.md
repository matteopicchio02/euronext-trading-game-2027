# Project Alpha 2027 — Data Dictionary

## 1. Research Data Overview

Project Alpha 2027 employs a historical panel of European listed equities to support cross-sectional factor screening, portfolio construction and risk estimation.

The operational research dataset used for the November 2026 analysis comprised 59 securities and 1,046 aligned daily price observations, from 3 October 2022 through 4 November 2026.

Historical adjusted prices were obtained through Yahoo Finance using the `yfinance` Python package.

These observations represent historical research data and must not be confused with official NextWise execution prices or portfolio valuations.

## 2. Principal Datasets

| Dataset | Description | Currency |
|---|---|---|
| `prices_real_2026-11-04.csv` | Adjusted historical prices in the respective local trading currencies | Local currencies |
| `prices_eur_2026-11-04.csv` | Historical prices expressed in EUR after currency normalization | EUR |
| `portfolio_v1.csv` | **Historical draft, 26 theoretical names, NOT the actual portfolio** | Weights as NAV fractions |
| `portfolio_actual_2026-11-18.csv` | **Actual 21-name snapshot transcribed from NextWise cards** | Market value/P&L in EUR; `purchase_price_display` in local instrument currency |
| `watchlist_actual_extended.csv` | Expanded candidate metadata and sector map for the 21-name snapshot | Metadata only |
| `watchlist.csv` | Initial equity universe and research reference data | Mixed / metadata |
| `analyst_inputs.csv` | Research inputs used by the prototype | As defined in source file |

The filenames ending in a date indicate historical dataset versions. They do not necessarily correspond to portfolio execution dates.

## 3. Historical Frequency and Alignment

Price observations are indexed by trading date.

Cross-sectional research uses a common calendar to ensure that the covariance matrix and the factor estimates are computed on aligned observations.

The operational dataset contains no missing values after alignment.

Missing observations must be handled explicitly; forward filling should not be introduced without investigating the reason for the missing data and its statistical implications.

## 4. Currency Conversion

For the five Norwegian equities in the research universe, local prices are denominated in NOK.

The operational conversion convention is:

\[
P_{i,t}^{EUR} =
\frac{P_{i,t}^{NOK}}{FX_t^{NOK/EUR}}
\]

where \(FX_t^{NOK/EUR}\) represents the number of Norwegian kroner per euro.

Consequently, historical EUR returns incorporate both underlying equity-price movements and exchange-rate movements.

Actual NextWise cash debits may use a different effective exchange rate from the historical research reference series.

## 5. Return Convention

Unless otherwise stated, daily returns are simple returns:

\[
r_{i,t}=\frac{P_{i,t}}{P_{i,t-1}}-1
\]

The primary risk estimation horizon comprises 252 daily return observations.

Volatility is annualized using a square-root-of-time factor of \(\sqrt{252}\).

Shorter rolling windows of 63 and 126 observations are used for sensitivity checks.

## 6. Data Quality Controls

The research pipeline includes:

- Verification of expected security identifiers.
- Date-index consistency and duplicate-date checks.
- Missing-value identification.
- Positive-price validation.
- Historical currency conversion checks.
- Investigation of large price changes and potential corporate actions.
- Separation of historical adjusted prices from live or delayed platform quotes.

These checks reduce operational data risk but do not certify that every historical observation is economically accurate.

## 7. Reproducibility and Access Restrictions

The current GitHub repository contains methodology, research code and selected test fixtures.

Complete historical market datasets and live competition records are not included in the public-facing research package.

Reproduction of the empirical notebooks requires the corresponding historical input files and confirmation of their data provenance and permitted use.

Synthetic test results must not be represented as empirical market results.

## 8. Research Limitations

Historical prices are subject to data-provider revisions, corporate-action adjustments and survivorship or selection effects.

Portfolio optimization and factor screening are sensitive to sample choice, rolling estimation windows and assumed correlation stability.

Reported historical risk statistics are not forecasts or guaranteed upper bounds on future losses.

## 9. Actual snapshot columns (18 November 2026)

| Column | Meaning |
|---|---|
| `ticker` | Yahoo Finance instrument identifier, not an exchange order ID |
| `name`, `sector` | Internal names and 11-category grouping, NOT certified score-provider ICB |
| `weight` | Marked position value / EUR 50,164.75 total NAV on the screenshot date |
| `quantity` | Units held on the NextWise card; **not** an execution-history record |
| `purchase_price_display` | Price as printed in the app, denominated in the instrument's local currency. **EQNR.OL is NOK, not EUR**; do not multiply by quantity and assume a EUR cost basis |
| `market_value_eur`, `pnl_eur` | Displayed EUR values and unrealized per-position P&L; rounded display values |
| `status` | Explicit as-of provenance; **not live** |

The 21 position cards sum to **EUR 40,488.99 equity market value and EUR −10.46 displayed unrealized P&L**; overview cash is EUR 9,675.76, yielding EUR 50,164.75 NAV. The overview performance base is a different reference from the original EUR 50,000 virtual endowment; realized transactions, dividends and cash flows are **not fully reconciled** by the per-card values alone.

`ALPHA_daily_returns.csv` and covariance matrices generated in Colab are external empirical inputs and are intentionally not bundled in this GitHub snapshot. Restore their date ranges, ticker coverage, corporate-action adjustments and EUR/NOK conversion before attempting a new comparison.

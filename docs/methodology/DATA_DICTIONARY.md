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
| `portfolio_v1.csv` | Baseline simulated portfolio used as a test fixture | As defined in source file |
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

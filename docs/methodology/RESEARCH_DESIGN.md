# Research design — how I'm trying to make the project more reliable

## 1. How the research started

As an MSc student, I initially explored portfolio analysis in **Google Colab**, using small Python experiments before moving some parts into reusable code. The original Colab archive used for this GitHub version contains **47 cells (45 code, 2 Markdown)** with price refreshes, factor ideas, portfolio comparisons and early risk calculations.

I'm keeping a record of the original workflow because **a backtest is only useful when I can explain which data were available at the time**. This is a developing learning project, not a fully independent research paper or a production investment platform.

The four cleaned notebooks in `notebooks/` are **refactored research artefacts** based on identifiable steps in the source file, not an exact replay of every exploratory cell. They deliberately omit personal Drive mount paths and redundant cells.

## 2. Dates and information sets
- `01_market_data_engineering`: reconstructed adjusted prices through **2026-11-04**, contingent on supplied local/FX data.
- `02_factor_screening`: rank factors at the latest supplied price date; outputs must be interpreted using that as-of date.
- `03_portfolio_construction`: explicitly truncates prices at **2026-11-02** for a retrospective **2026-11-03** selection exercise, reducing look-ahead bias.
- `04_risk_analytics`: weights estimated from **2026-11-04** prices; aggregate exposure anchored to NextWise **2026-11-05 12:29** reference snapshot. This is **not** an exact intraday mark-to-market reconstruction.

## 3. Mathematical conventions
- Daily simple returns; 252 trading days per year.
- Momentum: 63/126-session percentile-rank blend, weighted 40/60; aggregate factor score 55% momentum, 27% inverse downside deviation and 18% inverse volatility.
- Volatility based on sample standard deviation. Downside deviation uses a zero minimum-acceptable-return threshold and squared negative returns averaged across all observations.
- HHI on **equity-normalized weights**, not confirmed to equal the official competition HHI definition.
- Diversification ratio on equity weights: weighted average standalone vol divided by portfolio equity vol.
- NAV volatility includes a zero-return cash sleeve; CVaR and drawdown from constant-weight synthetic historical paths.
- UCITS check is a simplified structural proxy, not a certified regulation/legal determination.

## 4. Validation boundaries
The source notebook and contemporary outputs report 59 securities, 1,046 aligned price observations through 2026-11-04, and a 17-stock risk comparison with DR ~2.807. **Those results have not been recomputed from the actual private historical data in this exported package**, because the input price files and complete currency series were not attached. Do not label a generated example as verified empirical performance.

## 5. Problems I've noticed and want to address
- Survivorship and look-ahead bias in universe construction.
- Data-vendor adjusted prices versus venue execution/settlement prices.
- Nonstationarity, corporate actions, thin left-tail CVaR samples and correlated factor exposures.
- In-sample optimization and overfitting across thousands of portfolio combinations.
- A retrospective chronological holdout and rolling-window optimizer diagnostic were added on 18 November 2026 in `scripts/alpha_oos_validation.py`. The selected 21 holdings were known at the evaluation date, so this is NOT a fully independent OOS track record; historical membership reconstruction, transaction-cost validation, benchmark attribution and official score calibration remain unimplemented.

## 6. What each part of the repository represents
This repository separates a **Python research prototype** (`src/alpha/`), **dated student notebooks** (the four notebooks), and **manually recorded virtual-account observations** from NextWise. Some trades are participant-confirmed without original execution receipts. Notebook simulations must not be presented as live performance or trading instructions.

## 7. Why dated snapshots matter (18 November 2026 example)

`data/portfolio_actual_2026-11-18.csv` records a **valuation snapshot transcribed from 21 NextWise cards**, not actual trade confirmations or the full transaction ledger. The old 17-position portfolio studied in historical November 4 notebooks, the planned 26-name `portfolio_v1.csv` and the 21 current positions are different information sets.

The complete EUR returns used for the November 18 diagnostics were exported from Google Colab and **are not committed** to the current repository. To reproduce, supply the return CSV to `scripts/alpha_oos_validation.py --returns <file.csv>`. Do not claim the OOS package is fully reproducible solely by cloning the GitHub repository.

By **20 November 2026**, a partial Dassault sale and two reported buy executions had moved the portfolio to **23 positions**, but the individual fill prices for Ahold and Unilever and synchronized post-trade stock marks were still unavailable. That is why the automated NAV estimate is temporarily paused.

See the [18 November student decision note](../governance/DECISION_2026-11-18.md), [20 November account reconciliation](../../reports/snapshots/EXECUTED_BUYS_2026-11-20_1805.md) and [decision log](../governance/DECISION_LOG.md).

**What I want to improve next:** construct an independently dated price dataset, preserve actual historical membership, compare against relevant benchmarks and ensure a fresh user can reproduce the important research results without access to my personal Colab workspace.

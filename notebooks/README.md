# Learning quantitative finance with Python — notebooks

These notebooks are some of my **first experiments with market data and portfolio analysis**. I started exploring the ideas in Google Colab and later organised parts of the work into more readable notebooks.

I'm using them to practise a workflow: **collect data → check data quality → build simple measures → compare portfolios → question the results**.

| Notebook | What I'm practising |
|---|---|
| [01 — Market data](01_market_data_engineering.ipynb) | Downloading and cleaning price data, handling missing values and currency differences |
| [02 — Factor screening](02_factor_screening.ipynb) | Experimenting with momentum and risk factors to compare stocks |
| [03 — Portfolio construction](03_portfolio_construction.ipynb) | Translating a list of stocks into weights and testing simple allocation constraints |
| [04 — Risk analytics](04_risk_analytics.ipynb) | Exploring volatility, diversification, drawdowns and portfolio-level risk |

## What these notebooks are — and aren't

They are **dated learning exercises from early November 2026**, mostly based on prices through **4 November**. The construction exercise uses a **2 November** cutoff, and an earlier risk comparison studied **17 stocks**.

They are **not** a live link to NextWise and do not describe the later 21-name screenshot snapshot or the 23-name post-transaction portfolio.

Some original input files, including the cleaned EUR price panel, were produced separately in Colab and **are not stored in this repository**. That means a fresh clone cannot reproduce every notebook output without supplying the missing historical data. I consider that a current limitation rather than pretending the results are fully reproducible.

## What I'm learning to improve

- Document price sources, currency conversion and corporate-action adjustments.
- Understand why a backtest can look good because the portfolio was chosen with hindsight.
- Compare results with benchmarks and out-of-sample periods.
- Separate statistical estimates from real virtual-account performance.

For newer work, see the [main project README](../README.md), [research methodology](../docs/methodology/METHODOLOGY.md) and [research limitations](../docs/methodology/RESEARCH_DESIGN.md).

The notebooks and examples are **educational**, and none of them automatically places orders.

# Project Alpha 2027

### My first quantitative portfolio research project

Hi! I'm an MSc student in **Financial Risk and Data Analysis at Sapienza University of Rome**. I'm interested in financial markets, portfolio management and risk analytics, and I'm using the **Euronext Trading Game 2026–2027** as an opportunity to learn by building something practical.

I started this repository to bring together the topics I'm studying at university — statistics, financial mathematics, Python and risk management — and apply them to a **virtual €50,000 portfolio**. The aim is to develop a repeatable research process, understand my decisions and improve the code as I learn.

This is an **ongoing student project**, not a professional investment strategy or a claim of trading expertise.

## What I'm working on

Rather than selecting stocks only on intuition, I'm trying to answer a few questions with data:

- **Portfolio construction:** How can I diversify across companies and sectors without simply increasing the number of holdings?
- **Risk measurement:** What can volatility, Value at Risk (VaR), concentration measures and correlations tell me about potential losses?
- **Investment research:** How can I compare companies using momentum, fundamentals, valuation assumptions and upcoming earnings?
- **Tracking decisions:** Can I document each idea, compare it with what actually happened and learn from mistakes?
- **Python workflow:** How can notebooks, small reusable modules, tests and GitHub Actions help make the analysis easier to reproduce?

I don't have final answers to these questions. The repository records what I've tried so far, including assumptions, errors, and things I still need to validate.

## What I've built so far

| Part of the project | What it does | Current stage |
|---|---|---|
| [Jupyter notebooks](notebooks/README.md) | Explore market data, factor screening, portfolio weights and risk measures | Early experiments; mostly historical November data |
| [Python code](src/alpha/) | Calculate portfolio metrics, run simplified optimisation and compare scenarios | Working research prototype, not a production system |
| [Tests](tests/) | Check calculations, inputs and reconciliation of portfolio records | Automated regression tests |
| [Research notes](docs/README.md) | Explain assumptions, investment ideas and decisions | Updated as the game progresses |
| [Portfolio snapshots](data/) | Record what NextWise showed at specific dates | Manual and user-confirmed, not a live brokerage feed |
| [GitHub Actions](.github/workflows/) | Run tests and scheduled research checks on public price data | **New 23-name market watch scheduled**; old 21-name NextWise-relative NAV estimator stays paused |

### Latest observation — 23 November 2026, 10:15 CET

NextWise displays **€49,334.92** portfolio value and **−1.67%** cumulative performance. This is **€12.74 above** the last recorded 20 November evening NAV of €49,322.18. The 23 November screenshot comes from the *profile* page: it does **not** show the current cash amount, individual holdings or new transactions, so I have not extrapolated those values from the old screenshot.

[23 November profile observation](reports/snapshots/NEXTWISE_PROFILE_2026-11-23_1015.md) · [Dated NAV observations](data/nextwise_nav_snapshots.csv).

### A portfolio example from the Trading Game

The competition is played with **virtual money**. My starting allocation was **€50,000**, and the game runs from **5 October 2026 to 9 April 2027**.

The latest account summary documented here is dated **20 November 2026, 18:05 (Italy)**:

| NextWise account measure | Last documented value |
|---|---:|
| Total portfolio value | **€49,322.18** |
| Equity value | €40,985.32 |
| Cash | €8,336.86 |
| Cash allocation | 16.90% |

I have recorded **23 holdings** after three user-confirmed virtual transactions on 20 November: selling 30 Dassault Systèmes shares at €22.75, and buying Ahold Delhaize and Unilever. The **individual execution prices of the two purchases are not yet confirmed** in the records, so I do not invent them.

These are **dated observations, not today's live balance or an independently verified trading track record**.

If you're interested in the details:
- [Post-trade quantities](data/positions_after_buys_2026-11-20.csv) — holdings count and quantities, without made-up current prices
- [Transaction notes](data/trade_events_2026-11-20.csv) — what has and has not been confirmed
- [Account reconciliation](reports/snapshots/EXECUTED_BUYS_2026-11-20_1805.md) — why cash movements and stock returns must be treated separately

## Automated market-price follow-up (23 holdings)

I have added a separate **read-only market watch for all 23 virtual holdings**, using their already recorded quantities and public Yahoo daily prices. It calculates daily EUR price changes, sector and risk contributions, concentration, volatility and a clearly labelled **indicative** portfolio value based on the last dated NextWise account snapshot.

The [Market Watch workflow](.github/workflows/market_watch_23.yml) is scheduled after European trading closes on weekdays. Once a successful external data run occurs, its reports will be available in [reports/market_watch/](reports/market_watch/). Missing data will stop the workflow rather than produce an unreliable figure.

**What does not update itself:** actual NextWise orders, fill prices, dividends and cash changes. I still need to add confirmed account events to the position ledger when they happen. The older **21-name daily NAV monitor stays paused** because its quantities are obsolete; it has not been silently replaced with fictitious per-stock platform valuations.

[How the price monitor works and how to run it](docs/monitoring/MARKET_WATCH_23.md).

## Tools I'm learning to use

**Python · pandas · NumPy · SciPy · Jupyter / Google Colab · pytest · GitHub Actions · Excel**

I use public market data for parts of the analysis and manually transcribed NextWise portfolio records for the virtual account. The two are not interchangeable: prices can have different timestamps, exchange rates or corporate-action adjustments.

Some development and review have been supported by AI-assisted tools. My focus is on understanding the methods, checking calculations and documenting which conclusions the data actually support.

## Try the code

You'll need **Python 3.10+**. From the project folder:

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
```

Run a small **synthetic-data demonstration** (not the actual game portfolio):

```bash
python scripts/run_screen.py --demo
```

To explore the historical portfolio checks:

```bash
python scripts/check_compliance.py
```

This last command uses a **dated 18 November portfolio snapshot** by default, not the latest 23-position account state. For the methodology behind the outputs, see [the research notes](docs/methodology/METHODOLOGY.md) and [validation limitations](docs/methodology/RESEARCH_DESIGN.md).

## What I still want to improve

1. **Reconcile the 23 current positions:** get consistent, dated position-level prices and confirmed individual Ahold/Unilever purchase prices.
2. **Validate the new 23-stock price watch:** compare its first completed Yahoo estimate with a dated NextWise account total; reactivate the older platform-anchored monitor only after complete synchronized input reconciliation.
3. **Improve backtesting:** strengthen out-of-sample validation, benchmark comparisons and treatment of survivorship/selection bias.
4. **Expand risk analysis:** study stress scenarios, currency exposure and why risk metrics can disagree when data or assumptions change.
5. **Review results over time:** compare what I expected when making a decision with what actually happened.

The project will evolve alongside my MSc studies. I'd rather document a limitation properly than present an attractive but unreliable result.

## A note on the competition and the data

Project Alpha is **my independent educational project**. It is **not affiliated with Euronext, NextWise or a financial institution**, and it does not place trades automatically or use real money.

- Historical backtests and simulated portfolios are **not actual Trading Game performance**.
- Metrics such as HHI, diversification ratio, VaR and simplified UCITS-style checks are **research calculations**, not certified official competition scores.
- The repository includes **dated virtual holdings and account information** and is currently **publicly visible on GitHub**. Historical snapshots should not be mistaken for an up-to-date portfolio.

For more technical information, start with the [documentation guide](docs/README.md). The source code is made available under the [MIT licence](LICENSE).

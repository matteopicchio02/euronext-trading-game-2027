# Methodology — methods I'm learning and testing

## 1. Why I'm studying these methods

I'm using this first project to connect concepts from my MSc classes with a virtual investment portfolio. My approach is **experimental**: I build a simple model, examine what it suggests, and then try to understand its assumptions and weaknesses.

The Trading Game refers to several assessment dimensions, including returns and portfolio diversification. Because I do not have verified numerical weights for all the criteria, I **cannot calculate an official competition score or optimise it reliably**.

Three working ideas guide my research:

1. **Separate controllable choices from uncertain market returns.** Portfolio weights, sectors and concentration can be measured and changed; future stock performance cannot be known in advance.
2. **Treat short-horizon return forecasts cautiously.** In a competition lasting a few months, price movements and estimation noise can overwhelm a weak statistical signal. The information coefficient values below are illustrative *assumptions*, not something I have measured for my own strategy.
3. **Test different objectives instead of assuming one is best.** Return, downside risk and diversification may lead to different portfolios. A rank-based scenario is worth exploring, but not proof that taking more risk improves the chance of winning.

## 2. An initial factor model (subjective research weights)

| Factor | Weight | Inputs |
|---|---|---|
| Momentum | 30% | 3m and 6m return relative to universe, 12-1m return, price vs 200d average |
| Catalyst | 20% | Analyst score: dated, identifiable events before 9 Apr (guidance, buybacks, M&A, estimate revisions) |
| Quality | 15% | Analyst score: ROIC, margin stability, balance sheet |
| Downside | 15% | 60d volatility, downside deviation, 6m maximum drawdown (lower is better) |
| Valuation | 10% | Analyst score; low weight because valuation rarely pays inside five months |
| Diversification | 10% | Negative average pairwise correlation to the rest of the universe |

Missing factors have their weight redistributed. **I chose these initial weights as a starting hypothesis, not because they have been validated or optimised.** A proper comparison needs holdout data and sensitivity checks.

## 3. Translating a score into portfolio weights

* Expected excess return: `alpha = IC * sigma * z` (Grinold) with IC = 0.05 on purpose, so the optimiser does not over-trust the score.
* Selection: best name in each of the 10 best sectors, then fill to N by score with at most 3 names per sector.
* Optimisation (`alpha.optimizer`): maximise `w.alpha - 0.5*lambda*w'Sigma*w - eta*sum(w^2) + delta*DR(w)` subject to bounds, sector cap and beta band, then repair to 5/10/40.

## 4. A simulated competition environment

`alpha.scoring_sim` draws 6 criterion weights from a Dirichlet distribution, simulates synthetic prices (market + sector + idiosyncratic factors
with true alpha) and a field of 400 competitors (25% concentrated gamblers, 40% typical, 20% diversified, 15% ETF-heavy, no skill), scores
every participant by percentile rank on each criterion, and records where each of our designs finishes.

**How I interpret this exercise:** it compares portfolio designs under assumptions I selected. The simulated competitor types, criterion weights and return distributions are not observations of real participants. The results are **not probabilities of winning** or forecasts of actual market returns.

## 5. Exploring drawdowns with Monte Carlo

Monte Carlo of Gaussian daily returns over 110 trading days (5% annual drift):

| Portfolio vol | Median max DD | P(DD > 8%) | P(DD > 13%) |
|---|---|---|---|
| 13% | 7.9% | 49% | 13% |
| 15% | 9.2% | 62% | 21% |
| 17% | 10.5% | 73% | 31% |

In this **Gaussian simulation**, an 8% drawdown is quite common and a 13% drawdown less frequent at the chosen volatility. I use the table to compare sensitivity to thresholds, **not to promise real-world drawdown probabilities**: fat tails, clustering and changing volatility can produce substantially different outcomes.

## 6. How I plan to validate the models

* Walk-forward: set weights on data up to date T, evaluate on T to T+3 months, roll forward.
* Report the hit rate, rank IC and turnover, not only the return.
* Keep every decision in `docs/governance/DECISION_LOG.md` so the result can be audited against the process.

## 7. Comparing a model with an actual virtual-account snapshot (18 November 2026)

The original 26-name `data/portfolio_v1.csv` and the synthetic competitor Monte Carlo remain **historical research fixtures**. The actual NextWise 18 November snapshot has **21 equities** and 19.29% cash, recorded in `data/portfolio_actual_2026-11-18.csv`.

Two separate price pipelines previously yielded annualized volatility estimates of **8.88%** and **9.05%**. These values cannot be combined as a single point estimate without reconciling the input price panel, adjustment methods and covariance horizon.

The rolling OOS script `scripts/alpha_oos_validation.py` uses EUR daily returns exported separately from Colab. Although the optimizer in each historical fold uses only preceding observations, selecting the portfolio's 21 constituents **with knowledge of the evaluation date creates selection/survivorship bias**. Its constant-weight daily-rebalanced returns are hypothetical, not real NextWise track record or validated alpha forecasts.

The 10/4/15 guidelines, HHI and UCITS proxies, and the 35% Paris-listing concentration monitor are **not guaranteed official Euronext scoring conditions**; see [Rules and uncertainty](../governance/RULES_VERIFIED.md).

# Methodology

## 1. Problem framing

The score has six criteria with unpublished weights, a field of thousands of students, and **one** national
winner. Three consequences:

1. **Structure criteria are cheap.** HHI, number of sectors, diversification ratio and UCITS compliance depend on how
   the book is built, not on market direction. Maxing them removes four chances to lose rank for free.
2. **Return criteria are mostly luck plus beta.** Over about 110 trading days the cross-sectional signal-to-noise ratio is low:
   with a true alpha dispersion of 10% a year and 25% idiosyncratic volatility, even a good signal realises an
   information coefficient of roughly 0.05 over the game.
3. **Payoff is convex in rank.** Only first place advances, so risk should rise when behind late in the game and fall when clearly ahead.

## 2. Factor model (prior weights)

| Factor | Weight | Inputs |
|---|---|---|
| Momentum | 30% | 3m and 6m return relative to universe, 12-1m return, price vs 200d average |
| Catalyst | 20% | Analyst score: dated, identifiable events before 9 Apr (guidance, buybacks, M&A, estimate revisions) |
| Quality | 15% | Analyst score: ROIC, margin stability, balance sheet |
| Downside | 15% | 60d volatility, downside deviation, 6m maximum drawdown (lower is better) |
| Valuation | 10% | Analyst score; low weight because valuation rarely pays inside five months |
| Diversification | 10% | Negative average pairwise correlation to the rest of the universe |

Missing factors have their weight redistributed. **These weights are not optimised.** Test them on data not used to set them.

## 3. From score to weights

* Expected excess return: `alpha = IC * sigma * z` (Grinold) with IC = 0.05 on purpose, so the optimiser does not over-trust the score.
* Selection: best name in each of the 10 best sectors, then fill to N by score with at most 3 names per sector.
* Optimisation (`alpha.optimizer`): maximise `w.alpha - 0.5*lambda*w'Sigma*w - eta*sum(w^2) + delta*DR(w)` subject to bounds, sector cap and beta band, then repair to 5/10/40.

## 4. Score-structure simulator

`alpha.scoring_sim` draws 6 criterion weights from a Dirichlet distribution, simulates synthetic prices (market + sector + idiosyncratic factors
with true alpha) and a field of 400 competitors (25% concentrated gamblers, 40% typical, 20% diversified, 15% ETF-heavy, no skill), scores
every participant by percentile rank on each criterion, and records where each of our designs finishes.

Reading the output: it shows which **designs** are robust to weight uncertainty. It does not predict returns, and the field mix is an assumption.

## 5. Drawdown calibration

Monte Carlo of Gaussian daily returns over 110 trading days (5% annual drift):

| Portfolio vol | Median max DD | P(DD > 8%) | P(DD > 13%) |
|---|---|---|---|
| 13% | 7.9% | 49% | 13% |
| 15% | 9.2% | 62% | 21% |
| 17% | 10.5% | 73% | 31% |

So 8% marks an ordinary bad stretch (review, cheap) and 13% a genuinely bad one (about one path in five at 15% vol). Real returns have fat tails, so these are lower bounds.

## 6. Validation plan

* Walk-forward: set weights on data up to date T, evaluate on T to T+3 months, roll forward.
* Report the hit rate, rank IC and turnover, not only the return.
* Keep every decision in `docs/governance/DECISION_LOG.md` so the result can be audited against the process.

## 7. Actual-portfolio checkpoint: 18 November 2026

The original 26-name `data/portfolio_v1.csv` and the synthetic competitor Monte Carlo remain **historical research fixtures**. The actual NextWise 18 November snapshot has **21 equities** and 19.29% cash, recorded in `data/portfolio_actual_2026-11-18.csv`.

Two separate price pipelines previously yielded annualized volatility estimates of **8.88%** and **9.05%**. These values cannot be combined as a single point estimate without reconciling the input price panel, adjustment methods and covariance horizon.

The rolling OOS script `scripts/alpha_oos_validation.py` uses EUR daily returns exported separately from Colab. Although the optimizer in each historical fold uses only preceding observations, selecting the portfolio's 21 constituents **with knowledge of the evaluation date creates selection/survivorship bias**. Its constant-weight daily-rebalanced returns are hypothetical, not real NextWise track record or validated alpha forecasts.

The 10/4/15 guidelines, HHI and UCITS proxies, and the 35% Paris-listing concentration monitor are **not guaranteed official Euronext scoring conditions**; see [Rules and uncertainty](../governance/RULES_VERIFIED.md).

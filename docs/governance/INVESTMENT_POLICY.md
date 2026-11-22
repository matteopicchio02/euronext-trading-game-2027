# Personal Portfolio Research Guidelines — Project Alpha 2027

I'm an MSc student, and this is my attempt to write down a **consistent approach** to a virtual portfolio instead of changing my mind after every market move. The thresholds below are **my research assumptions and learning exercises**, not official Euronext rules or a professional fund's investment mandate.

I use a decision log to compare what I intended to do with what I actually did. If a personal target is missed, it prompts a review — it does not automatically mean the portfolio is invalid or must be traded.

## 1. Objective

**Learning goal:** explore whether a diversified, risk-aware investment approach can perform well in the Euronext Trading Game through 9 April 2027, while keeping the analysis and decisions understandable and reproducible.

I would of course like to do well in the competition. But the main purpose of this first project is to learn portfolio construction, evaluate assumptions and recognise the limitations of each model. I am **not** claiming an estimated probability of winning.

## 2. My initial portfolio guidelines (neutral scenario)

| Parameter | Limit | Why |
|---|---|---|
| Invested | 96% target (cash 4%) | Historical research baseline, not a binding platform requirement; lower exposure can reflect risk |
| Positions | 22-26 equities target | Research design only; **21 actual as of 18 Nov**; do not add positions solely to meet a target |
| Max weight per name | 6% at entry, trim above 7% | Keeps the UCITS single-issuer limit (10%) far away |
| Names above 5% | At most 6 (aggregate at most 36%) | Buffer under the 40% aggregate limit |
| Sector cap | 25% of NAV | Concentration control and sector-count criterion |
| Paris-listed exposure | 35% of NAV (house monitor only) | Listing exchange is not economic country risk; do not force sales mechanically |
| Sectors | At least 9, target 10 | Sector-count criterion is cheap to maximise |
| Beta (vs equal-weight universe) | 0.95-1.20 | Gross performance needs market exposure; risk-adjusted score needs control |
| ETFs | Only as sector gap-fillers, at most 10% each | HHI and sector treatment of ETFs is unknown |
| Inverse ETFs | Only in DEFENSE mode, at most 5%, review every 10 trading days | Hedging tool, not a return source |
| Minimum quality | Listed on Euronext, market cap above EUR 1bn, no penny stocks | Avoid exclusion and illiquid gaps |

## 2a. What actually happened — 18 November 2026

The [18 November decision note](DECISION_2026-11-18.md) covers the **21-name actual portfolio** (NAV EUR 50,164.75; equity exposure EUR 40,488.99 = 80.71%; cash 19.29%). Paris-listed names represent approximately 41.20% of NAV. These differ from the historical 96% equity, 22–26 names and 35% Paris research targets. **HOLD / NO TRADE** was documented: no automatic rebalancing or sale follows from a house target alone. `data/portfolio_v1.csv` remains a separate **26-name draft**, not actual positions.

## 3. Position risk

* Risk budget per name: 0.5-0.7% of NAV to the stop (conviction scales size). With a 12% stop that is 4.2-5.8% weight.
* Default stop: 2.5 x ATR(14) or the thesis-invalidation level, whichever is closer. A stop triggers a **review within 24 hours**, not an automatic sale.
* No averaging down without a written new thesis.
* Earnings: at most two names above 5% may report within the next three trading days.
* Turnover: at most three new names per week; no fees in the game, but churn destroys the audit trail.

## 4. Portfolio drawdown (calibrated, see METHODOLOGY.md)

| Drawdown from NAV peak | Action |
|---|---|
| below 8% | Normal operations |
| 8% or more | CAUTION: no new tactical entries, no adding to losers, correlation review |
| 13% or more | DEFENSE: beta target 0.80, max weight 5%, written post-mortem before adding risk |

A 4% / 7% rule would fire in almost every five-month window for a ~15% volatility book (median max drawdown about 9%), so it carries no information.

## 5. Experimental rank-aware scenarios (not official rules)

| State | Mode | Budget |
|---|---|---|
| 45 days or less left and rank below the 85th percentile | ATTACK | beta up to 1.25, max weight 8%, still under 10% single name |
| 21 days or less left and rank at or above the 97th percentile | LOCK_IN | beta 0.75, equity 90%, avoid event risk |
| Otherwise | NEUTRAL | table above |

These states are **hypothetical research scenarios**, implemented in `alpha.risk_governor`. They are not a demonstrated way to win the game, and any decision to use them requires checking the available rankings, assumptions and actual account risk.

## 6. How I try to document a decision

1. Screen (`scripts/run_screen.py`) -> shortlist.
2. Write a short research note for each candidate (idea, valuation assumptions, bull / base / bear scenarios, events and position size).
3. Risk check: HHI, sectors, diversification ratio, 5/10/40, beta, top-5 risk contributors.
4. Execute in NextWise; log the fill and the memo link.
5. Review the portfolio regularly and revisit factors with appropriately separated historical data. A written review is an intention; it is not proof that the task was completed on schedule.

## 7. Disclosure

The project is independent, uses **virtual money**, and is not investment advice. This GitHub repository is **currently public**, so dated holdings and research notes included here should be treated as publicly visible. I need to decide which information is appropriate to disclose while the competition is ongoing.

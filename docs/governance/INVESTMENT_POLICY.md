# Investment Policy Statement - Project Alpha 2027

Self-imposed rules for a virtual competition portfolio. They are **not** Euronext rules.
Every exception must be written in the decision log before the trade, not after.

## 1. Objective

Maximise the probability of finishing first in the Italian individual ranking by 9 Apr 2027, subject to
(a) a fully diversified, UCITS-style book and (b) a documented, reproducible process.

## 2. Portfolio construction (neutral mode)

| Parameter | Limit | Why |
|---|---|---|
| Invested | 96% (cash 4%) | Cash earns 0 in the game; it only dilutes gross performance |
| Positions | 22-26 equities | Fully invested under 5/10/40 needs at least 18 names at a 6% cap |
| Max weight per name | 6% at entry, trim above 7% | Keeps the UCITS single-issuer limit (10%) far away |
| Names above 5% | At most 6 (aggregate at most 36%) | Buffer under the 40% aggregate limit |
| Sector cap | 25% of NAV | Concentration control and sector-count criterion |
| Sectors | At least 9, target 10 | Sector-count criterion is cheap to maximise |
| Beta (vs equal-weight universe) | 0.95-1.20 | Gross performance needs market exposure; risk-adjusted score needs control |
| ETFs | Only as sector gap-fillers, at most 10% each | HHI and sector treatment of ETFs is unknown |
| Inverse ETFs | Only in DEFENSE mode, at most 5%, review every 10 trading days | Hedging tool, not a return source |
| Minimum quality | Listed on Euronext, market cap above EUR 1bn, no penny stocks | Avoid exclusion and illiquid gaps |

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

## 5. Tournament protocol (rank-aware)

| State | Mode | Budget |
|---|---|---|
| 45 days or less left and rank below the 85th percentile | ATTACK | beta up to 1.25, max weight 8%, still under 10% single name |
| 21 days or less left and rank at or above the 97th percentile | LOCK_IN | beta 0.75, equity 90%, avoid event risk |
| Otherwise | NEUTRAL | table above |

The governor is implemented in `alpha.risk_governor` and reviewed every Friday.

## 6. Process

1. Screen (`scripts/run_screen.py`) -> shortlist.
2. Investment memo per name (thesis, valuation, bull / base / bear, catalysts, stop, size).
3. Risk check: HHI, sectors, diversification ratio, 5/10/40, beta, top-5 risk contributors.
4. Execute in NextWise; log the fill and the memo link.
5. Friday: weekly report + governor decision. Monthly: factor review on out-of-sample data only.

## 7. Disclosure

Public reports are delayed by 2-4 weeks. The project is independent, uses virtual money, and is not investment advice.

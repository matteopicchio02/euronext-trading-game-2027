# Project Alpha — market price study (2026-11-23)

> **Student research estimate — NOT NextWise.** Public Yahoo daily prices,
> 23 quantities frozen as of 2026-11-20;
> cash held constant. Not a brokerage account feed or automated order system.

## Indicative portfolio measures

- Latest official **dated** NextWise NAV anchor: EUR 49,322.18.
- **Indicative** NAV based on price differences since anchor: EUR 49,467.10.
- Indicative price effect since the anchor: EUR +144.92.
- Price effect over the latest common trading session: EUR +144.92.
- Frozen assumed cash: EUR 8,336.86.
- Yahoo direct NAV cross-check: EUR 49,468.83.
- Baseline Yahoo-versus-NextWise difference: EUR +1.72.

## Historical risk analysis — model outputs only

- Annualized volatility: 7.60%.
- Parametric 1-day 95% VaR: EUR 389.69.
- HHI (normalized equity weights): 0.04642.
- Diversification ratio: 2.869.
- Equity / cash on Yahoo mark basis: 83.15% / 16.85%.
- Paris listed share of model NAV: 39.68% (internal monitor only).
- EUR/NOK: 10.7280 NOK per EUR.

## Biggest one-session contributions — not trades

| Largest positive | Indicative EUR |
|---|---:|
| PRY.MI | +117.90 |
| AIR.PA | +40.32 |
| UCB.BR | +28.70 |
| ML.PA | +17.36 |
| OR.PA | +16.25 |

| Largest negative | Indicative EUR |
|---|---:|
| KPN.AS | -36.50 |
| TTE.PA | -18.20 |
| ENI.MI | -17.33 |
| EQNR.OL | -14.79 |
| SRG.MI | -13.44 |

## All holdings — external Yahoo marks

| Ticker | Qty | Currency | Yahoo mark EUR | Day change EUR | Weight % |
|---|---:|---|---:|---:|---:|
| AI.PA | 12 | EUR | 2,251.92 | +0.96 | 4.55 |
| AIR.PA | 7 | EUR | 1,370.04 | +40.32 | 2.77 |
| CS.PA | 47 | EUR | 2,131.92 | +10.34 | 4.31 |
| CAP.PA | 15 | EUR | 1,758.00 | -7.50 | 3.55 |
| DSY.PA | 60 | EUR | 1,328.40 | -6.60 | 2.69 |
| EDP.LS | 420 | EUR | 2,053.80 | +9.66 | 4.15 |
| ENI.MI | 55 | EUR | 1,311.20 | -17.33 | 2.65 |
| EQNR.OL | 49 | NOK | 1,737.93 | -14.79 | 3.51 |
| ENX.PA | 12 | EUR | 1,977.60 | -8.40 | 4.00 |
| RACE.MI | 5 | EUR | 1,826.75 | +11.25 | 3.69 |
| G.MI | 52 | EUR | 2,259.92 | +6.24 | 4.57 |
| HEIA.AS | 29 | EUR | 2,394.82 | +2.90 | 4.84 |
| LI.PA | 14 | EUR | 523.88 | +2.80 | 1.06 |
| KPN.AS | 462 | EUR | 1,970.43 | -36.50 | 3.98 |
| OR.PA | 5 | EUR | 2,191.25 | +16.25 | 4.43 |
| ML.PA | 62 | EUR | 1,952.38 | +17.36 | 3.95 |
| PRY.MI | 18 | EUR | 1,926.90 | +117.90 | 3.90 |
| SAN.PA | 25 | EUR | 2,131.50 | +8.50 | 4.31 |
| SRG.MI | 336 | EUR | 2,001.89 | -13.44 | 4.05 |
| TTE.PA | 26 | EUR | 2,014.74 | -18.20 | 4.07 |
| UCB.BR | 7 | EUR | 1,985.90 | +28.70 | 4.01 |
| AD.AS | 25 | EUR | 864.00 | -0.50 | 1.75 |
| UNA.AS | 20 | EUR | 1,166.80 | -5.00 | 2.36 |

## Limitations and next research tasks

- Quotes may be delayed or revised. The reported date is a market session, not a live NextWise value.
- This model cannot detect new NextWise purchases, sales, dividends or changes in available cash.
- The anchored estimate does not create official position-level acquisition P&L.
- NOK/EUR conversion and prices adjusted for dividends/splits can diverge from simulation accounting.
- Review individual execution prices for Ahold and Unilever when available; do not invent them.
- Before acting on a signal, compare the latest company disclosures and executable NextWise quote.
- If actual quantities or cash change, update the dated ledger and monitor configuration first.
- This code does **not** place, cancel, or modify virtual orders.

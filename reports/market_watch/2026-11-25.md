# Project Alpha — market price study (2026-11-25)

> **Student research estimate — NOT NextWise.** Public Yahoo daily prices,
> 23 quantities frozen as of 2026-11-20;
> cash held constant. Not a brokerage account feed or automated order system.

## Indicative portfolio measures

- Latest official **dated** NextWise NAV anchor: EUR 49,322.18.
- **Indicative** NAV based on price differences since anchor: EUR 49,752.71.
- Indicative price effect since the anchor: EUR +430.53.
- Price effect over the latest common trading session: EUR -1.75.
- Frozen assumed cash: EUR 8,336.86.
- Yahoo direct NAV cross-check: EUR 49,754.43.
- Baseline Yahoo-versus-NextWise difference: EUR +1.72.

## Historical risk analysis — model outputs only

- Annualized volatility: 7.67%.
- Parametric 1-day 95% VaR: EUR 395.51.
- HHI (normalized equity weights): 0.04657.
- Diversification ratio: 2.848.
- Equity / cash on Yahoo mark basis: 83.24% / 16.76%.
- Paris listed share of model NAV: 40.15% (internal monitor only).
- EUR/NOK: 10.7593 NOK per EUR.

## Biggest one-session contributions — not trades

| Largest positive | Indicative EUR |
|---|---:|
| SAN.PA | +114.50 |
| HEIA.AS | +27.26 |
| UNA.AS | +24.00 |
| RACE.MI | +22.50 |
| SRG.MI | +20.83 |

| Largest negative | Indicative EUR |
|---|---:|
| PRY.MI | -95.76 |
| AIR.PA | -25.48 |
| G.MI | -23.92 |
| CS.PA | -20.68 |
| UCB.BR | -16.80 |

## All holdings — external Yahoo marks

| Ticker | Qty | Currency | Yahoo mark EUR | Day change EUR | Weight % |
|---|---:|---|---:|---:|---:|
| AI.PA | 12 | EUR | 2,261.52 | +4.08 | 4.55 |
| AIR.PA | 7 | EUR | 1,330.00 | -25.48 | 2.67 |
| CS.PA | 47 | EUR | 2,109.36 | -20.68 | 4.24 |
| CAP.PA | 15 | EUR | 1,801.50 | +2.25 | 3.62 |
| DSY.PA | 60 | EUR | 1,329.00 | -12.60 | 2.67 |
| EDP.LS | 420 | EUR | 2,047.08 | -13.44 | 4.11 |
| ENI.MI | 55 | EUR | 1,305.70 | -3.58 | 2.62 |
| EQNR.OL | 49 | NOK | 1,751.54 | +12.91 | 3.52 |
| ENX.PA | 12 | EUR | 2,010.00 | -16.80 | 4.04 |
| RACE.MI | 5 | EUR | 1,828.50 | +22.50 | 3.68 |
| G.MI | 52 | EUR | 2,229.24 | -23.92 | 4.48 |
| HEIA.AS | 29 | EUR | 2,461.52 | +27.26 | 4.95 |
| LI.PA | 14 | EUR | 531.16 | +1.96 | 1.07 |
| KPN.AS | 462 | EUR | 2,004.62 | -1.39 | 4.03 |
| OR.PA | 5 | EUR | 2,210.00 | +5.50 | 4.44 |
| ML.PA | 62 | EUR | 1,929.44 | -6.20 | 3.88 |
| PRY.MI | 18 | EUR | 1,676.16 | -95.76 | 3.37 |
| SAN.PA | 25 | EUR | 2,454.00 | +114.50 | 4.93 |
| SRG.MI | 336 | EUR | 2,032.80 | +20.83 | 4.09 |
| TTE.PA | 26 | EUR | 2,009.28 | -10.40 | 4.04 |
| UCB.BR | 7 | EUR | 1,998.50 | -16.80 | 4.02 |
| AD.AS | 25 | EUR | 893.25 | +9.50 | 1.80 |
| UNA.AS | 20 | EUR | 1,213.40 | +24.00 | 2.44 |

## Limitations and next research tasks

- Quotes may be delayed or revised. The reported date is a market session, not a live NextWise value.
- This model cannot detect new NextWise purchases, sales, dividends or changes in available cash.
- The anchored estimate does not create official position-level acquisition P&L.
- NOK/EUR conversion and prices adjusted for dividends/splits can diverge from simulation accounting.
- Review individual execution prices for Ahold and Unilever when available; do not invent them.
- Before acting on a signal, compare the latest company disclosures and executable NextWise quote.
- If actual quantities or cash change, update the dated ledger and monitor configuration first.
- This code does **not** place, cancel, or modify virtual orders.

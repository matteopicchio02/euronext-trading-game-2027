# Project Alpha — market price study (2026-11-26)

> **Student research estimate — NOT NextWise.** Public Yahoo daily prices,
> 23 quantities frozen as of 2026-11-20;
> cash held constant. Not a brokerage account feed or automated order system.

## Indicative portfolio measures

- Latest official **dated** NextWise NAV anchor: EUR 49,322.18.
- **Indicative** NAV based on price differences since anchor: EUR 50,309.61.
- Indicative price effect since the anchor: EUR +987.43.
- Price effect over the latest common trading session: EUR +554.24.
- Frozen assumed cash: EUR 8,336.86.
- Yahoo direct NAV cross-check: EUR 50,311.33.
- Baseline Yahoo-versus-NextWise difference: EUR +1.72.

## Historical risk analysis — model outputs only

- Annualized volatility: 7.74%.
- Parametric 1-day 95% VaR: EUR 403.70.
- HHI (normalized equity weights): 0.04655.
- Diversification ratio: 2.835.
- Equity / cash on Yahoo mark basis: 83.43% / 16.57%.
- Paris listed share of model NAV: 40.21% (internal monitor only).
- EUR/NOK: 10.7078 NOK per EUR.

## Biggest one-session contributions — not trades

| Largest positive | Indicative EUR |
|---|---:|
| PRY.MI | +110.16 |
| ENX.PA | +48.00 |
| CS.PA | +39.48 |
| RACE.MI | +36.50 |
| G.MI | +35.88 |

| Largest negative | Indicative EUR |
|---|---:|
| UNA.AS | -0.20 |
| EQNR.OL | +1.64 |
| LI.PA | +5.32 |
| AD.AS | +5.75 |
| DSY.PA | +9.00 |

## All holdings — external Yahoo marks

| Ticker | Qty | Currency | Yahoo mark EUR | Day change EUR | Weight % |
|---|---:|---|---:|---:|---:|
| AI.PA | 12 | EUR | 2,283.84 | +22.32 | 4.54 |
| AIR.PA | 7 | EUR | 1,356.88 | +26.88 | 2.70 |
| CS.PA | 47 | EUR | 2,148.84 | +39.48 | 4.27 |
| CAP.PA | 15 | EUR | 1,815.00 | +13.50 | 3.61 |
| DSY.PA | 60 | EUR | 1,338.00 | +9.00 | 2.66 |
| EDP.LS | 420 | EUR | 2,060.10 | +13.02 | 4.09 |
| ENI.MI | 55 | EUR | 1,329.62 | +23.92 | 2.64 |
| EQNR.OL | 49 | NOK | 1,755.85 | +1.64 | 3.49 |
| ENX.PA | 12 | EUR | 2,058.00 | +48.00 | 4.09 |
| RACE.MI | 5 | EUR | 1,865.00 | +36.50 | 3.71 |
| G.MI | 52 | EUR | 2,265.12 | +35.88 | 4.50 |
| HEIA.AS | 29 | EUR | 2,477.18 | +15.66 | 4.92 |
| LI.PA | 14 | EUR | 536.48 | +5.32 | 1.07 |
| KPN.AS | 462 | EUR | 2,022.17 | +17.56 | 4.02 |
| OR.PA | 5 | EUR | 2,225.75 | +15.75 | 4.42 |
| ML.PA | 62 | EUR | 1,958.58 | +29.14 | 3.89 |
| PRY.MI | 18 | EUR | 1,786.32 | +110.16 | 3.55 |
| SAN.PA | 25 | EUR | 2,470.75 | +16.75 | 4.91 |
| SRG.MI | 336 | EUR | 2,061.02 | +28.22 | 4.10 |
| TTE.PA | 26 | EUR | 2,037.36 | +28.08 | 4.05 |
| UCB.BR | 7 | EUR | 2,010.40 | +11.90 | 4.00 |
| AD.AS | 25 | EUR | 899.00 | +5.75 | 1.79 |
| UNA.AS | 20 | EUR | 1,213.20 | -0.20 | 2.41 |

## Limitations and next research tasks

- Quotes may be delayed or revised. The reported date is a market session, not a live NextWise value.
- This model cannot detect new NextWise purchases, sales, dividends or changes in available cash.
- The anchored estimate does not create official position-level acquisition P&L.
- NOK/EUR conversion and prices adjusted for dividends/splits can diverge from simulation accounting.
- Review individual execution prices for Ahold and Unilever when available; do not invent them.
- Before acting on a signal, compare the latest company disclosures and executable NextWise quote.
- If actual quantities or cash change, update the dated ledger and monitor configuration first.
- This code does **not** place, cancel, or modify virtual orders.

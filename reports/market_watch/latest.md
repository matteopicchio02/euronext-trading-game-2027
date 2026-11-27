# Project Alpha — market price study (2026-11-27)

> **Student research estimate — NOT NextWise.** Public Yahoo daily prices,
> 23 quantities frozen as of 2026-11-20;
> cash held constant. Not a brokerage account feed or automated order system.

## Indicative portfolio measures

- Latest official **dated** NextWise NAV anchor: EUR 49,322.18.
- **Indicative** NAV based on price differences since anchor: EUR 50,458.06.
- Indicative price effect since the anchor: EUR +1,135.88.
- Price effect over the latest common trading session: EUR +155.10.
- Frozen assumed cash: EUR 8,336.86.
- Yahoo direct NAV cross-check: EUR 50,459.79.
- Baseline Yahoo-versus-NextWise difference: EUR +1.72.

## Historical risk analysis — model outputs only

- Annualized volatility: 7.75%.
- Parametric 1-day 95% VaR: EUR 405.05.
- HHI (normalized equity weights): 0.04652.
- Diversification ratio: 2.837.
- Equity / cash on Yahoo mark basis: 83.48% / 16.52%.
- Paris listed share of model NAV: 40.13% (internal monitor only).
- EUR/NOK: 10.7220 NOK per EUR.

## Biggest one-session contributions — not trades

| Largest positive | Indicative EUR |
|---|---:|
| PRY.MI | +34.38 |
| G.MI | +32.76 |
| EDP.LS | +23.94 |
| DSY.PA | +21.00 |
| AI.PA | +19.68 |

| Largest negative | Indicative EUR |
|---|---:|
| SAN.PA | -29.50 |
| ML.PA | -24.80 |
| EQNR.OL | -13.05 |
| HEIA.AS | -9.28 |
| OR.PA | -6.75 |

## All holdings — external Yahoo marks

| Ticker | Qty | Currency | Yahoo mark EUR | Day change EUR | Weight % |
|---|---:|---|---:|---:|---:|
| AI.PA | 12 | EUR | 2,303.52 | +19.68 | 4.57 |
| AIR.PA | 7 | EUR | 1,370.04 | +13.16 | 2.72 |
| CS.PA | 47 | EUR | 2,155.42 | +6.58 | 4.27 |
| CAP.PA | 15 | EUR | 1,826.25 | +11.25 | 3.62 |
| DSY.PA | 60 | EUR | 1,359.00 | +21.00 | 2.69 |
| EDP.LS | 420 | EUR | 2,084.04 | +23.94 | 4.13 |
| ENI.MI | 55 | EUR | 1,346.68 | +17.05 | 2.67 |
| EQNR.OL | 49 | NOK | 1,736.15 | -13.05 | 3.44 |
| ENX.PA | 12 | EUR | 2,062.80 | +4.80 | 4.09 |
| RACE.MI | 5 | EUR | 1,883.25 | +18.25 | 3.73 |
| G.MI | 52 | EUR | 2,297.88 | +32.76 | 4.55 |
| HEIA.AS | 29 | EUR | 2,467.90 | -9.28 | 4.89 |
| LI.PA | 14 | EUR | 536.48 | +0.00 | 1.06 |
| KPN.AS | 462 | EUR | 2,026.33 | +4.16 | 4.02 |
| OR.PA | 5 | EUR | 2,219.00 | -6.75 | 4.40 |
| ML.PA | 62 | EUR | 1,933.78 | -24.80 | 3.83 |
| PRY.MI | 18 | EUR | 1,820.70 | +34.38 | 3.61 |
| SAN.PA | 25 | EUR | 2,441.25 | -29.50 | 4.84 |
| SRG.MI | 336 | EUR | 2,072.45 | +11.42 | 4.11 |
| TTE.PA | 26 | EUR | 2,042.56 | +5.20 | 4.05 |
| UCB.BR | 7 | EUR | 2,026.50 | +16.10 | 4.02 |
| AD.AS | 25 | EUR | 899.75 | +0.75 | 1.78 |
| UNA.AS | 20 | EUR | 1,211.20 | -2.00 | 2.40 |

## Limitations and next research tasks

- Quotes may be delayed or revised. The reported date is a market session, not a live NextWise value.
- This model cannot detect new NextWise purchases, sales, dividends or changes in available cash.
- The anchored estimate does not create official position-level acquisition P&L.
- NOK/EUR conversion and prices adjusted for dividends/splits can diverge from simulation accounting.
- Review individual execution prices for Ahold and Unilever when available; do not invent them.
- Before acting on a signal, compare the latest company disclosures and executable NextWise quote.
- If actual quantities or cash change, update the dated ledger and monitor configuration first.
- This code does **not** place, cancel, or modify virtual orders.

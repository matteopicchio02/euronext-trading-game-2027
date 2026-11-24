# Project Alpha — market price study (2026-11-24)

> **Student research estimate — NOT NextWise.** Public Yahoo daily prices,
> 23 quantities frozen as of 2026-11-20;
> cash held constant. Not a brokerage account feed or automated order system.

## Indicative portfolio measures

- Latest official **dated** NextWise NAV anchor: EUR 49,322.18.
- **Indicative** NAV based on price differences since anchor: EUR 49,751.39.
- Indicative price effect since the anchor: EUR +429.21.
- Price effect over the latest common trading session: EUR +279.33.
- Frozen assumed cash: EUR 8,336.86.
- Yahoo direct NAV cross-check: EUR 49,753.11.
- Baseline Yahoo-versus-NextWise difference: EUR +1.72.

## Historical risk analysis — model outputs only

- Annualized volatility: 7.67%.
- Parametric 1-day 95% VaR: EUR 395.41.
- HHI (normalized equity weights): 0.04650.
- Diversification ratio: 2.855.
- Equity / cash on Yahoo mark basis: 83.24% / 16.76%.
- Paris listed share of model NAV: 40.08% (internal monitor only).
- EUR/NOK: 10.7455 NOK per EUR.

## Biggest one-session contributions — not trades

| Largest positive | Indicative EUR |
|---|---:|
| SAN.PA | +208.00 |
| ENX.PA | +49.20 |
| CAP.PA | +41.25 |
| HEIA.AS | +39.44 |
| KPN.AS | +35.57 |

| Largest negative | Indicative EUR |
|---|---:|
| PRY.MI | -154.98 |
| RACE.MI | -20.75 |
| ML.PA | -16.74 |
| AIR.PA | -14.56 |
| EQNR.OL | -7.32 |

## All holdings — external Yahoo marks

| Ticker | Qty | Currency | Yahoo mark EUR | Day change EUR | Weight % |
|---|---:|---|---:|---:|---:|
| AI.PA | 12 | EUR | 2,257.44 | +5.52 | 4.54 |
| AIR.PA | 7 | EUR | 1,355.48 | -14.56 | 2.72 |
| CS.PA | 47 | EUR | 2,130.04 | -1.88 | 4.28 |
| CAP.PA | 15 | EUR | 1,799.25 | +41.25 | 3.62 |
| DSY.PA | 60 | EUR | 1,341.60 | +13.20 | 2.70 |
| EDP.LS | 420 | EUR | 2,060.52 | +6.72 | 4.14 |
| ENI.MI | 55 | EUR | 1,309.28 | -1.92 | 2.63 |
| EQNR.OL | 49 | NOK | 1,735.56 | -7.32 | 3.49 |
| ENX.PA | 12 | EUR | 2,026.80 | +49.20 | 4.07 |
| RACE.MI | 5 | EUR | 1,806.00 | -20.75 | 3.63 |
| G.MI | 52 | EUR | 2,253.16 | -6.76 | 4.53 |
| HEIA.AS | 29 | EUR | 2,434.26 | +39.44 | 4.89 |
| LI.PA | 14 | EUR | 529.20 | +5.32 | 1.06 |
| KPN.AS | 462 | EUR | 2,006.00 | +35.57 | 4.03 |
| OR.PA | 5 | EUR | 2,204.50 | +13.25 | 4.43 |
| ML.PA | 62 | EUR | 1,935.64 | -16.74 | 3.89 |
| PRY.MI | 18 | EUR | 1,771.92 | -154.98 | 3.56 |
| SAN.PA | 25 | EUR | 2,339.50 | +208.00 | 4.70 |
| SRG.MI | 336 | EUR | 2,011.97 | +10.08 | 4.04 |
| TTE.PA | 26 | EUR | 2,019.68 | +4.94 | 4.06 |
| UCB.BR | 7 | EUR | 2,015.30 | +29.40 | 4.05 |
| AD.AS | 25 | EUR | 883.75 | +19.75 | 1.78 |
| UNA.AS | 20 | EUR | 1,189.40 | +22.60 | 2.39 |

## Limitations and next research tasks

- Quotes may be delayed or revised. The reported date is a market session, not a live NextWise value.
- This model cannot detect new NextWise purchases, sales, dividends or changes in available cash.
- The anchored estimate does not create official position-level acquisition P&L.
- NOK/EUR conversion and prices adjusted for dividends/splits can diverge from simulation accounting.
- Review individual execution prices for Ahold and Unilever when available; do not invent them.
- Before acting on a signal, compare the latest company disclosures and executable NextWise quote.
- If actual quantities or cash change, update the dated ledger and monitor configuration first.
- This code does **not** place, cancel, or modify virtual orders.

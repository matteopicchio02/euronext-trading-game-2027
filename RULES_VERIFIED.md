# Rules: what is verified and what is not

Sources: Euronext Trading Game page (terms last updated 21 Sep 2026) and the Euronext/NextWise info sheet.
Check the live terms in NextWise before relying on any line below; rules can change.

## Verified (published)

| Item | Rule |
|---|---|
| Edition | 5 Oct 2026 - 9 Apr 2027; local winners announced 16 Apr; European individual pitch battle 28 Apr 2027 |
| Eligibility | Students enrolled in higher education in BE, FR, GR, IE, IT, NL, NO, PT; proof of enrolment may be requested; one account only |
| Capital | EUR 50,000 virtual per individual (clubs: EUR 200,000) |
| Universe | Equities and ETFs on Euronext markets (Paris, Amsterdam, Lisbon, Oslo, Dublin, Milan, Brussels); inverse ETFs allowed; penny stocks excluded; no derivatives or options |
| Costs and data | No transaction fees; market data delayed 15 minutes; market and limit orders |
| Limits | No published per-position, sector or turnover limits |
| Scoring (stage 1) | Gross performance, risk-adjusted performance, HHI, number of sectors covered, diversification ratio, compliance with UCITS rules |
| Stage 2 | National winners pitch to a Euronext jury: thesis, strategy, construction, execution; presentation quality |
| Club feature | An individual can entrust EUR 3,000-30,000 to one or more clubs (not their own) |

## NOT published (ask the organisers)

1. Weight of each of the six criteria and how they are normalised (percentile rank? z-score?).
2. How performance is measured for an individual who starts trading after 5 Oct: from the registration date, from 5 Oct, or from first trade?
3. Definition of "risk-adjusted performance" (Sharpe? Sortino? return/vol?) and the window used.
4. How HHI is computed: on invested positions only, or including cash? Is an ETF one position or looked through?
5. Which sector classification is used (ICB industries? GICS?) and how a multi-sector ETF counts.
6. What "UCITS compliance" tests (5/10/40? ETF limits? cash?) and whether it is pass/fail or graded.
7. Definition of "penny stock".
8. Whether entrusting money to a club removes it from the individual portfolio (and from the individual score).
9. Whether the individual national ranking is public and how often it updates.

## Working assumptions used in this repository

* Sector classification: ICB-style 11 industries (the watchlist covers 10; Real Estate is excluded because of the rate backdrop).
* HHI on invested positions (normalised); ETFs counted as one position.
* UCITS: 5/10/40 on equities and 20% cap on any single ETF.
* Every assumption is a hypothesis; update this file as soon as the organisers answer.

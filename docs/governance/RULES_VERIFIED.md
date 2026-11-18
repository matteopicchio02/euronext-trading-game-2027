# Project Alpha 2027 — Rules, guidance and uncertainty
**Last reviewed: 18 November 2026.** Distinguish published ETG rules, NextWise educational guidance, and our internal portfolio policy.

## Verified from Euronext materials
Primary source: [Euronext Trading Game official rules](https://live.euronext.com/en/education/euronext-trading-game) (2026–2027 edition); supporting [NextWise rules](https://www.nextwise.fr/le-reglement).

- Competition runs **5 October 2026 – 9 April 2027**; national winners announced **16 April 2027**; individual European pitch **28 April 2027**.
- Individual virtual endowment **EUR 50,000** (club **EUR 200,000**); securities include equities and ETFs listed across seven Euronext exchanges.
- Derivatives/options excluded; inverse ETFs eligible; penny stocks excluded. Market and limit order functions use delayed quotations and zero simulated commissions.
- National selection uses **six published quantitative criteria**: gross performance, risk-adjusted performance, Herfindahl–Hirschman index, sector breadth, diversification ratio, and UCITS-rule compliance. The relative weights are not published in the sources reviewed.
- The European final evaluates strategy and execution through an investment pitch.

## NextWise-specific information and guidance
- [NextWise selection criteria for individuals](https://www.nextwise.fr/criteres-de-selection-profil-individuel) describes **10 securities, 4 sectors and no more than 15% in one name as recommended diversification practices**. **Do not label them proven hard disqualification conditions for the Euronext edition.**
- [NextWise rules](https://www.nextwise.fr/le-reglement) describes both a **monthly** and a **general** ranking for individual participants. The actual user-visible Italian ranking becomes available at **month-end**, not each day; precise cut-offs and display timings should be checked in the app.
- NextWise refers to the **Sharpe ratio** in its risk-adjusted criterion description, whereas the Euronext published list says *risk-adjusted performance*. Do **not** assume our particular 180-week historical-volatility computation matches the official formula without confirmation.
- The NextWise material describes UCITS 5/10/40 in the context of scoring. Our code is a **simplified proxy**; it does not perform fund look-through, all issuer grouping, or certify compliance with actual investment regulation.
- The Next Challenge and Euronext Trading Game can have **different scoring features**. Quiz/chat/social engagement points must not silently be added to the official six ETG criteria.

## Research-only house assumptions — not verified rules
- `src/alpha/rules.py` checks the **10/4/15 guidelines**, intentionally as an advisory proxy.
- Sector mapping is an 11-category internal classification, not confirmed as the score provider's exact ICB implementation.
- HHI convention (invested-normalized, cash as a separate line, ETF look-through) is unresolved; report conventions explicitly.
- UCITS proxy: 5/10/40 direct-issuer check and 20% ETF line cap, with caveats.
- Maximum 35% in **Paris-listed** securities is an internal research cap; **listing exchange does not represent economic country-risk**.
- The 96% equity / 4% cash **neutral target** is a historical internal baseline. The 18 November actual snapshot is **80.71% equity / 19.29% cash**; the HOLD decision did not authorize forced rebalancing.

## Still needs organizer/platform confirmation
1. Exact normalization and weights of the six ETG criteria.
2. Official risk-adjusted metric calculation (return horizon, risk-free assumption, vol estimator and corporate actions).
3. Whether cash and ETF look-through affect HHI, diversification ratio and UCITS test.
4. Exact sector taxonomy, market data timestamp and monthly cut-off.
5. How dividends and FX adjustments enter the P&L and performance reference.
6. Any exceptional eligibility filters and how they affect scoring.

**Operational rule:** label all compliance screens “research/guideline checks”, not official certification. Reverify current terms before decisions; no model grants permission to trade.

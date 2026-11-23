# Automatic market-watch reports

This folder will contain dated **external-market research estimates** for the 23 virtual holdings of Project Alpha 2027 after the first successful [Market Watch workflow](../../.github/workflows/market_watch_23.yml) run.

- `YYYY-MM-DD.md`: daily market-price movements, risk measures and sources.
- `latest.md`: last **successfully completed** dated study, not necessarily today's prices.
- `latest_positions.csv`: 23 ticker-by-ticker Yahoo marked values and price-change contributions.
- `latest_summary.json`: structured research metrics and an explicit **not NextWise** label.

If no dated files are present, **no actual external-price run has been verified yet**. Passing automated offline tests is not evidence of a successful Yahoo Finance download.

The monitor assumes the positions from [the 20 November quantity ledger](../../data/positions_after_buys_2026-11-20.csv) and EUR 8,336.86 cash from the latest full NextWise account screenshot on that date. It cannot automatically observe new orders, dividends or cash movements. Data can be delayed or missing and should never be mistaken for the official virtual account balance.

[What the model does and how to interpret it](../../docs/monitoring/MARKET_WATCH_23.md).

# Market Watch — following my 23 virtual holdings without repeated screenshots

I'm building this as an MSc student to practise **working with financial price data, converting FX, testing portfolio-risk calculations and following a research portfolio over time**.

## Why I made a separate monitor

An older script, `scripts/daily_portfolio_monitor.py`, estimated the portfolio from a **21-stock snapshot of 18 November 2026**. After transactions on 20 November the position count changed to **23** (Dassault Systèmes 60 shares, Ahold Delhaize 25 shares and Unilever 20 shares). It would be incorrect to unpause the old script without a new same-time NextWise stock-price snapshot.

The new `scripts/holdings_market_watch.py` follows the **23 user-reported current quantities** directly using public end-of-day prices. It does **not require individual NextWise screenshots each day** to compute market-price movements.

## How it works

1. Load `data/positions_after_buys_2026-11-20.csv`, currently 23 distinct holdings; verify positive quantities, ticker formats and 60/25/20 shares for DSY/AD/UNA.
2. Load `data/market_watch_config.json`. The latest dated platform account snapshot used as an **anchor** is 20 Nov 2026, 18:05 CET: EUR **49,322.18 NAV**, EUR **8,336.86 cash**. These are historical observations, not current platform readings.
3. Retrieve Yahoo Finance daily **Close** and **Adj Close** for all 23 holdings plus `EURNOK=X`, which is **NOK per EUR** for the Oslo-listed Equinor position.
4. Calculate a EUR quote for each position (`quantity × quote`), a price-movement contribution since the **20 Nov closing-price anchor** and a change from the prior common trading session.
5. Compute **an indicative NAV scenario** by adding the aggregate external-market price change to the **dated, official NextWise NAV anchor**. It assumes no later trades, withdrawals, dividends or unrecorded cash movements.
6. Compute separate risk metrics (annualized volatility, 1-day Gaussian 95% VaR, equity-normalized HHI, diversification ratio, contribution to risk, sector exposure) using internally consistent **Yahoo-marked position weights**, not fictitious NextWise stock marks.
7. Save the dated results to `reports/market_watch/YYYY-MM-DD.md`, `latest.md`, `latest_positions.csv` and `latest_summary.json`.

### Why the two valuations may differ

The report includes **both** an anchored NextWise-based market-change estimate and an independent **direct Yahoo quote valuation**. They can differ because of the time of day, corporate actions, different feeds, settlement FX or platform conventions. Neither is automatically the official account value.

The historical acquisition prices of Ahold and Unilever are *not inferred* from quote changes or the combined order limits. Price performance from an anchor is different from the actual gain/loss since buying.

## Where and when it runs

GitHub Actions: [Market Watch — 23 holdings](../../.github/workflows/market_watch_23.yml), scheduled Monday–Friday at **21:17 UTC** (normally **22:17 CET / 23:17 CEST**), after the Euronext cash-market close. Scheduled jobs may be delayed or missed, and Yahoo daily data can fail or be updated later.

For manual runs on GitHub, open **Actions → Market Watch - 23 Holdings → Run workflow**. On a fresh run, the latest *completed common trading session* must match the European local date; the job refuses stale or missing quotes rather than making up estimates.

For local Python work:

```powershell
python -m pip install -e ".[data,dev]"
python -m pytest -q tests/test_holdings_market_watch.py
python -m scripts.holdings_market_watch
```

The last command accesses public Yahoo data. A diagnostic `--allow-stale` mode is available when testing an older session, but the report keeps the **actual date** shown in the retrieved data.

### Important controls

- **No brokerage login and no automated orders**: this is price analytics only. No purchase or sale can be detected from Yahoo price data.
- **Read-only account inputs**: the script reads frozen share quantities and cash. A new NextWise trade means the ledger and anchor must be updated; its prices cannot reveal that event.
- **Missing quotes or EUR/NOK rates stop the job**. Suspicious one-day jumps and a large mismatch between Yahoo and the dated NextWise valuation also stop it.
- **No fabricated fill prices**: Ahold/Unilever individual execution prices remain missing.
- **Provider limitations**: Yahoo Finance via yfinance is an unofficial data source, not an exchange-licensed real-time feed. Source checks and dated investor-relations announcements can be researched separately via Euronext and companies' websites.
- **Visibility**: GitHub currently marks this project as public, so the generated market-watch reports and positions are visible to anyone accessing the repository. Do not commit account credentials, unrelated private information or data for which redistribution is not authorized.
- **Older workflow unchanged**: `daily_monitor.yml` and its stale-data gate remain paused. The new watcher is independent and intentionally labelled as an **external market estimate**.

## What this changes for everyday collaboration

When I ask ChatGPT for a market update, it should first read the **current 23-name ledger, latest market-watch result and recent company/market announcements**, rather than requesting screenshots of every position. I only need to supply **new virtual-account actions** (buy/sell/execution, dividend posting or changed cash) and, occasionally, a single **NextWise overview** to assess model drift.

This is a **learning tool and virtual research project**, not an advisory service, a guaranteed valuation or a certified score for the competition.

# Project Alpha 2027

Quantitative portfolio construction and risk analytics for the **Euronext Trading Game 2026-27**
(individual competition, EUR 50,000 virtual capital, 5 Oct 2026 - 9 Apr 2027).

> **Independent educational project.** Not affiliated with, endorsed by or sponsored by Euronext,
> NextWise or any bank. Nothing here is investment advice. All trading is virtual.

## What it does

| Module | Purpose |
|---|---|
| `alpha.metrics` | The six scored quantities and friends: gross return, Sharpe, HHI, sector count, diversification ratio, drawdown, risk contributions |
| `alpha.ucits` | 5/10/40 diversification check and repair (our working interpretation of "UCITS compliance") |
| `alpha.screener` | Factor scoring (momentum, downside, diversification + analyst inputs) and breadth-constrained selection |
| `alpha.optimizer` | Constrained mean-variance with HHI / diversification-ratio tilt, sector caps and a beta band |
| `alpha.scoring_sim` | Monte Carlo of the score under **unknown criterion weights** against a simulated field |
| `alpha.risk_governor` | Tournament-aware risk budget (ATTACK / NEUTRAL / CAUTION / DEFENSE / LOCK_IN) |
| `alpha.report` | Weekly markdown report |

## Quick start

```bash
pip install -e ".[dev]"
pytest -q                                   # 27 tests
python scripts/run_screen.py --demo         # pipeline on SYNTHETIC prices (no network)
python scripts/run_simulation.py            # score-structure Monte Carlo
```

With real data (needs internet access to Yahoo Finance):

```bash
pip install -e ".[data]"
python scripts/run_screen.py --period 2y
```

Then record your 0-100 judgements for quality, valuation and catalyst in `data/analyst_inputs.csv`,
write an investment memo per position (`docs/INVESTMENT_MEMO_TEMPLATE.md`) and publish a weekly report.

## Honest limitations

* Criterion **weights are not published** by Euronext; the simulator treats them as random (Dirichlet) and
  reports results for several named scenarios. It measures the *structure* of the score, not stock returns.
* Simulation prices are **synthetic**; the competitor field is an assumption.
* "UCITS compliance" is **not defined publicly**; we implement the 5/10/40 rule and a 20% single-fund cap.
* Factor weights and risk thresholds are priors to be tested out of sample, not findings.
* `data/watchlist.csv` is a candidate list, not a recommendation; verify tradability and prices in NextWise.

## Repository layout

```
src/alpha/      library code          tests/     pytest suite
scripts/        command-line tools    data/      watchlist and analyst inputs
docs/           policy, methodology, templates, verified rules
reports/        generated output (weekly reports are published with a delay)
```

## License

MIT.

# Repository Quality Audit — 18 November 2026
**Target:** `matteopicchio02/euronext-trading-game-2027`, branch `main` (private). Scope: source-code review, GitHub file inventory, tests/CI, present/archival data, rule references, user-reported historical project progression and research reports.

## Corrections implemented directly on main

1. `scripts/check_compliance.py` now checks the **21-name actual 2026-11-18 screenshot snapshot by default**, not the 26-name draft, and warns that data are stale and checks are research-only. It rejects malformed weights, duplicate tickers, missing sector metadata and inconsistent marked values.
2. `scripts/alpha_oos_validation.py` now accepts explicit `--returns`, `--portfolio`, and `--outdir` arguments. It no longer requires the service-specific `/mnt/data` directory or assumes precisely 517 observations. It writes the historical selection-bias disclaimer with results.
3. `src/alpha/metrics.py` no longer silently fills missing active-ticker returns with 0; it fails closed on incomplete data. It no longer claims that a 180-week return/volatility ratio is a confirmed official NextWise metric.
4. `src/alpha/rules.py`, rules documentation, and the archived audit distinguish **NextWise 10/4/15 diversification guidance** from unverified mandatory Euronext thresholds, and clarify the simplified ETF/UCITS approximation.
5. `scripts/weekly_report.py` and `scripts/run_screen.py` date research reports using the **supplied price-series as-of date**, not implicitly the day the script runs.
6. The README, documentation index, research methodology and data dictionary now distinguish **October 26-name draft**, **early-November 17-name historical research**, and **18 November 21-name actual snapshot**; NAV/FX/unrealized P&L limitations are clearly stated.
7. `docs/governance/DECISION_LOG.md` is the single canonical decision register. The old `reports/decision_log.md` is a redirect notice, not an editable second log.
8. Removed accidental root download artifacts, the duplicate root README note, and an empty malformed notebooks index; added a proper `notebooks/README.md`.
9. Added snapshot and CLI regression tests, historical-run register, source history and warnings on synthetic probability estimates; protected raw Colab return files from accidental commits in `.gitignore`.
10. Retained archived PDF/manual and initial draft for provenance, instead of rewriting history.

## Checks performed
- GitHub Actions **Python CI** completed successfully after initial documentation and CLI repairs and after the source-code + regression-test changes.
- Review of the real repository tree, important source files, source-case assumptions, and the historical presentation/playbook.
- Primary sources: [Euronext ETG edition rules](https://live.euronext.com/en/education/euronext-trading-game), [NextWise rules](https://www.nextwise.fr/le-reglement) and [NextWise individual diversification guidance](https://www.nextwise.fr/criteres-de-selection-profil-individuel).
- Cross-checked the 21-name marked market values: **EUR 40,488.99**, NAV **EUR 50,164.75**, aggregate card P&L **EUR −10.46**. This snapshot check is now automated by Pytest.
- Checked the key Markdown references resolve to files that exist on the default branch.

## Important open gaps — not corrected by inventing data
- **No complete NextWise transaction/order export**: cannot certify every past trade, fill or realized P&L.
- **No live quote/order integration**: snapshot is historical as of 18 November; the private GitHub repo is not a broker console.
- **No official scoring engine weights or full UCITS/ETF/cash formula**: all internal structure scores remain proxies; do not over-interpret PASS.
- **Full raw Colab EUR return panel and candidate historical inputs are not in GitHub**: some empirical reports are not reproducible from a clone alone.
- **Research-model validation** still subject to end-date universe selection, survivorship, look-ahead from universe formation, daily-rebalance assumptions and data-vendor anomalies. The Monte Carlo `P(top 1%)` is a synthetic frequency, not a real contest-winning probability.
- **Risk governor thresholds (8%/13%)** were calibrated in an older 13–17% annual-volatility context; the 21-name research estimates around 9%. Recalibration would be a **strategic change requiring validation**, not an automatic software bug fix.
- **Public GitHub launch for CV**: repository remains **private** while actual recent competition holdings are stored; decide explicitly what to disclose at a later date.

## State following audit
**NO NextWise orders were placed**, **NO active positions or values were rewritten** and the user's 18 November **HOLD / NO TRADE** stands. The research repository is cleaner, safer to run, and more transparent about uncertainties; it cannot be certified "perfect" without the missing official/transaction inputs.

[Original 18-Nov decision](DECISION_2026-11-18.md) · [Project timeline](PROJECT_TIMELINE_2026.md) · [Canonical log](DECISION_LOG.md).

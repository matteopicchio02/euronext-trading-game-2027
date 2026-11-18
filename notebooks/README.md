# Archived quantitative research notebooks

These four notebooks describe **historical November 2026** research and were refactored from earlier Colab exploration. They **are not live NextWise connections** and they do **not** describe the 21-name snapshot taken on 18 November 2026.

- `01_market_data_engineering.ipynb`: price and currency normalization; original cutoff **2026-11-04**
- `02_factor_screening.ipynb`: 63-/126-day factor scoring on an externally supplied 2026-11-04 price panel
- `03_portfolio_construction.ipynb`: retrospective construction with a **2026-11-02** price cutoff
- `04_risk_analytics.ipynb`: historical 17-name comparison and dated NextWise snapshot from early November

The notebooks intentionally require external files such as `data/prices_eur_2026-11-04.csv`, which are **not committed**. They cannot be reproduced from clone alone; keep full price provenance and adjusted-price/FX conventions. Their risk and return metrics are **not** official Euronext performance and no orders are generated.

For the later 21-name snapshot use `data/portfolio_actual_2026-11-18.csv`, `scripts/check_compliance.py`, and the dated documentation in `docs/governance/`. For retrospective rolling research, see `scripts/alpha_oos_validation.py --help`.

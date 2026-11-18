# Simulation results — synthetic experiment (NOT a forecast)

> **Archived research only.** All prices, portfolio returns, score weights, and competitor mixes below are assumed or synthetic. Entries such as `P(top 1%) = 15.7%` are frequencies within a simulated field of 400 hypothetical peers, **not** a probability of winning the real Euronext Trading Game. These experiments predate the actual 21-name portfolio of 18 November 2026.

Generated with `python scripts/run_simulation.py --worlds 200 --field 400 --rho 0.2 --seed 7` (about 4-5 minutes on 2 CPU cores).

Reading guide: *percentile* = share of the 400 simulated competitors our score beats; *top5* = probability of finishing in the top 5% of the simulated field.
Prices are synthetic, the competitor mix is an assumption (25% concentrated, 40% typical, 20% diversified, 15% ETF-heavy, none skilled), and criterion weights are random unless a scenario is named.
Differences between designs D, E, F, G are within simulation noise. Sampling resolution of the scenario columns is 0.5 percentage points.

| Strategy | mean_percentile | P(top 5%) | P(top 1%) | pct_gross-only | top5_gross-only | pct_gross-70% | top5_gross-70% | pct_balanced | top5_balanced | pct_structure-heavy | top5_structure-heavy |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A. Piano originale (40% ETF, 10% cash) | 0.735 | 0.040 | 0.003 | 0.566 | 0.000 | 0.607 | 0.010 | 0.773 | 0.000 | 0.724 | 0.000 |
| B. Concentrato 6 titoli | 0.499 | 0.006 | 0.001 | 0.586 | 0.070 | 0.573 | 0.110 | 0.495 | 0.000 | 0.487 | 0.000 |
| C. Concentrato 12 titoli | 0.715 | 0.047 | 0.005 | 0.589 | 0.000 | 0.627 | 0.100 | 0.734 | 0.000 | 0.752 | 0.005 |
| D. Alpha-22 (cap 6%, 4% cash) | 0.891 | 0.350 | 0.106 | 0.582 | 0.000 | 0.674 | 0.110 | 0.928 | 0.450 | 0.921 | 0.380 |
| E. Alpha-22 + tilt beta | 0.846 | 0.211 | 0.046 | 0.578 | 0.000 | 0.656 | 0.125 | 0.890 | 0.265 | 0.872 | 0.200 |
| F. Alpha-30 diversificato | 0.913 | 0.488 | 0.157 | 0.573 | 0.000 | 0.673 | 0.075 | 0.946 | 0.575 | 0.946 | 0.560 |
| G. Alpha-24 (cap 5.5%) | 0.900 | 0.375 | 0.121 | 0.577 | 0.000 | 0.672 | 0.080 | 0.935 | 0.450 | 0.931 | 0.425 |

Criterion-level percentiles (mean over worlds):

| Strategy | gross | risk_adj | hhi | sectors | div_ratio | ucits |
|---|---|---|---|---|---|---|
| A. Piano originale (40% ETF, 10% cash) | 0.568 | 0.588 | 0.721 | 0.768 | 0.375 | 0.936 |
| B. Concentrato 6 titoli | 0.588 | 0.586 | 0.515 | 0.340 | 0.515 | 0.436 |
| C. Concentrato 12 titoli | 0.591 | 0.597 | 0.797 | 0.653 | 0.751 | 0.436 |
| D. Alpha-22 (cap 6%, 4% cash) | 0.584 | 0.593 | 0.890 | 0.894 | 0.866 | 0.936 |
| E. Alpha-22 + tilt beta | 0.581 | 0.578 | 0.890 | 0.889 | 0.657 | 0.936 |
| F. Alpha-30 diversificato | 0.575 | 0.585 | 0.963 | 0.926 | 0.906 | 0.936 |
| G. Alpha-24 (cap 5.5%) | 0.579 | 0.588 | 0.909 | 0.915 | 0.880 | 0.936 |

Sensitivity: with signal_rho = 0.0 (no skill) the best design (F) still reaches a mean percentile of 0.88 and P(top 5%) of 0.34; with rho = 0.4 it reaches 0.94 and 0.65. The ranking of designs does not change.

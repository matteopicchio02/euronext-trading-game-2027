"""Regression: infeasible optimizations must not silently return invalid weights."""
import numpy as np
import pandas as pd
import pytest
from alpha.optimizer import optimize_weights


def test_infeasible_sector_constraints_fail_closed():
    names = [f"T{i}" for i in range(20)]
    alpha = pd.Series(0.01, index=names)
    cov = pd.DataFrame(np.eye(20) * 0.04, index=names, columns=names)
    sectors = {t: ("Tech" if i < 18 else "Banks") for i, t in enumerate(names)}
    with pytest.raises(ValueError, match="infeasible|validation|converge"):
        optimize_weights(alpha, cov, sector_map=sectors, betas=None, sector_cap=0.25)

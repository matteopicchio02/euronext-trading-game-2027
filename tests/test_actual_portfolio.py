"""Regression checks for the real virtual portfolio snapshot and CLI entrypoints."""
from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest
from alpha import metrics

ROOT = Path(__file__).resolve().parents[1]


def test_actual_snapshot_reconciles_and_is_not_the_26_name_draft():
    real = pd.read_csv(ROOT / "data/portfolio_actual_2026-11-18.csv")
    draft = pd.read_csv(ROOT / "data/portfolio_v1.csv")
    assert len(real) == 21 and len(draft) == 26
    assert real.ticker.is_unique
    assert real.market_value_eur.sum() == pytest.approx(40488.99, abs=.01)
    assert real.pnl_eur.sum() == pytest.approx(-10.46, abs=.01)
    assert real.weight.sum() == pytest.approx(40488.99 / 50164.75, abs=1e-7)
    assert (real.market_value_eur / real.weight).median() == pytest.approx(50164.75, abs=.01)
    sectors = dict(zip(real.ticker, real.sector))
    assert metrics.sector_count(real.set_index("ticker").weight, sectors) == 11
    assert real.loc[real.ticker.str.endswith(".PA"), "weight"].sum() == pytest.approx(.4119648, abs=1e-6)


def test_compliance_cli_defaults_to_actual_snapshot():
    out = subprocess.run([sys.executable, str(ROOT / "scripts/check_compliance.py")],
                         capture_output=True, text=True, check=True).stdout
    assert "SNAPSHOT AS-OF 2026-11-18" in out
    assert "| Securities held | pass | 21 |" in out
    assert "NOT LIVE" in out


def test_oos_script_is_import_safe_and_exposes_required_input():
    p = subprocess.run([sys.executable, str(ROOT / "scripts/alpha_oos_validation.py"), "--help"],
                       capture_output=True, text=True, check=True)
    assert "--returns" in p.stdout
    assert "--portfolio" in p.stdout


def test_missing_returns_are_not_silently_forward_filled():
    prices = pd.DataFrame({"A": [100., None, 110.], "B": [100., 101., 102.]})
    r = metrics.simple_returns(prices)
    assert pd.isna(r.loc[1, "A"]) and pd.isna(r.loc[2, "A"])

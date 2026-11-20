"""Regression checks for the complete Nov-20 NextWise screenshot reconciliation.

These assertions validate arithmetic and sourcing, not a live order ledger or
the official Euronext competition score.
"""
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def test_all_21_names_and_quantity_consistency():
    now = pd.read_csv(DATA / "portfolio_actual_2026-11-20.csv").set_index("ticker")
    prev = pd.read_csv(DATA / "portfolio_actual_2026-11-18.csv").set_index("ticker")
    assert len(now) == len(prev) == 21
    assert now.index.is_unique
    assert set(now.index) == set(prev.index)
    assert now.quantity.eq(prev.quantity).all()
    assert now.asof_date.eq("2026-11-20").all()


def test_new_snapshot_nav_and_pnl_reconcile_to_cent():
    now = pd.read_csv(DATA / "portfolio_actual_2026-11-20.csv").set_index("ticker")
    prev = pd.read_csv(DATA / "portfolio_actual_2026-11-18.csv").set_index("ticker")
    assert now.market_value_eur.sum() == pytest.approx(39844.08, abs=1e-6)
    assert now.market_value_eur.sum() + 9675.76 == pytest.approx(49519.84, abs=1e-6)
    assert now.pnl_eur.sum() == pytest.approx(-655.37, abs=1e-6)
    assert (now.pnl_eur - prev.pnl_eur).sum() == pytest.approx(-644.91, abs=1e-6)
    assert (now.market_value_eur - prev.market_value_eur).sum() == pytest.approx(-644.91, abs=1e-6)
    assert now.weight.sum() == pytest.approx(39844.08 / 49519.84, abs=1e-9)


def test_equinor_nok_mark_must_be_tagged_inferred_in_eur():
    now = pd.read_csv(DATA / "portfolio_actual_2026-11-20.csv").set_index("ticker")
    eq = now.loc["EQNR.OL"]
    assert eq.local_market_value_ccy == "NOK"
    assert eq.local_market_value == pytest.approx(18909.10)
    assert eq.market_value_eur == pytest.approx(1761.86)
    assert "INFERRED" in eq.value_eur_provenance
    ai = now.loc["AI.PA"]
    assert ai.market_value_eur == pytest.approx(2268.96)
    assert ai.pnl_eur == pytest.approx(53.28)

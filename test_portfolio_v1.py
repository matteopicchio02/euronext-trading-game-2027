from pathlib import Path

import pandas as pd

from alpha import metrics as m
from alpha.ucits import check_ucits

DATA = Path(__file__).resolve().parents[1] / "data"


def test_portfolio_v1_is_inside_policy():
    pf = pd.read_csv(DATA / "portfolio_v1.csv")
    wl = pd.read_csv(DATA / "watchlist.csv")
    assert set(pf.ticker) <= set(wl.yahoo_ticker)
    w = pf.set_index("ticker")["weight"]
    sectors = dict(zip(wl.yahoo_ticker, wl.sector))
    assert 0.95 <= w.sum() <= 0.97
    assert 22 <= len(w) <= 26
    assert w.max() <= 0.06
    assert check_ucits(w).compliant
    assert m.sector_count(w, sectors) >= 9
    assert m.sector_weights(w, sectors).max() <= 0.25

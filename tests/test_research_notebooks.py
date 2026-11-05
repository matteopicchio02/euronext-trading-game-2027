
"""Structural checks for quantitative research notebooks.

These tests validate notebook integrity and Python syntax.
They do not execute the financial research pipelines.
"""

import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"

REQUIRED_NOTEBOOKS = [
    "01_market_data_engineering.ipynb",
    "02_factor_screening.ipynb",
    "03_portfolio_construction.ipynb",
    "04_risk_analytics.ipynb",
]


@pytest.mark.parametrize("filename", REQUIRED_NOTEBOOKS)
def test_notebook_exists(filename):
    path = NOTEBOOKS / filename

    assert path.is_file(), (
        f"Missing research notebook: {filename}"
    )


@pytest.mark.parametrize("filename", REQUIRED_NOTEBOOKS)
def test_notebook_structure_and_syntax(filename):
    path = NOTEBOOKS / filename

    with path.open(encoding="utf-8") as handle:
        notebook = json.load(handle)

    assert notebook["nbformat"] == 4
    assert isinstance(notebook["cells"], list)
    assert notebook["cells"], "Notebook must not be empty"

    for index, cell in enumerate(notebook["cells"]):
        assert cell["cell_type"] in {
            "code", "markdown", "raw"
        }

        if cell["cell_type"] != "code":
            continue

        source = cell.get("source", [])
        code = (
            "".join(source)
            if isinstance(source, list)
            else source
        )

        compile(
            code,
            filename=f"{filename}:cell_{index}",
            mode="exec",
        )

        assert not cell.get("outputs"), (
            f"{filename}: saved outputs in cell {index}"
        )

        assert cell.get("execution_count") is None, (
            f"{filename}: saved execution count in "
            f"cell {index}"
        )


@pytest.mark.parametrize("filename", REQUIRED_NOTEBOOKS)
def test_no_personal_drive_paths(filename):
    path = NOTEBOOKS / filename
    contents = path.read_text(encoding="utf-8")

    forbidden_strings = [
        "/content/drive/MyDrive/",
        "/content/drive/Shareddrives/",
        "drive.mount(",
    ]

    for forbidden in forbidden_strings:
        assert forbidden not in contents, (
            f"{filename}: environment-specific path "
            f"or Drive mount detected"
        )

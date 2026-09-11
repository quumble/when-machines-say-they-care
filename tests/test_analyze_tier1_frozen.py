from __future__ import annotations

from pathlib import Path

import pytest

from scripts.analyze_tier1 import analyze_confirmatory, read_csv, validate_and_join


EXPECTED = {
    "H1a": {
        "complete_pairs": 122,
        "risk_difference_pp": 60.65573770491803,
        "discordant_favor": 77,
        "discordant_oppose": 3,
        "mcnemar_p_raw": 1.4128410298528223e-19,
        "holm_p": 7.064205149264112e-19,
        "decision": "confirmed",
    },
    "H1b": {
        "complete_pairs": 131,
        "risk_difference_pp": 15.267175572519085,
        "discordant_favor": 22,
        "discordant_oppose": 2,
        "mcnemar_p_raw": 3.5881996154785156e-05,
        "holm_p": 0.00014352798461914062,
        "decision": "confirmed",
    },
    "H2a": {
        "complete_pairs": 178,
        "risk_difference_pp": 0.0,
        "discordant_favor": 1,
        "discordant_oppose": 1,
        "mcnemar_p_raw": 1.0,
        "holm_p": 1.0,
        "decision": "not_confirmed",
    },
    "H2b": {
        "complete_pairs": 198,
        "risk_difference_pp": 1.0101010101010102,
        "discordant_favor": 2,
        "discordant_oppose": 0,
        "mcnemar_p_raw": 0.5,
        "holm_p": 1.0,
        "decision": "not_confirmed",
    },
    "H3a": {
        "complete_pairs": 185,
        "risk_difference_pp": 0.5405405405405406,
        "discordant_favor": 13,
        "discordant_oppose": 12,
        "mcnemar_p_raw": 1.0,
        "holm_p": 1.0,
        "decision": "not_confirmed",
    },
    "H3b": {
        "complete_pairs": 185,
        "risk_difference_pp": 54.59459459459459,
        "discordant_favor": 104,
        "discordant_oppose": 3,
        "mcnemar_p_raw": 2.5177481866260118e-27,
        "holm_p": 1.510648911975607e-26,
        "decision": "confirmed",
    },
}


def test_frozen_tier1_point_estimates_pvalues_and_decisions() -> None:
    """Regression-lock the frozen human coding against the preregistered math.

    Bootstrap CIs are tested for algorithmic row-order invariance separately.
    This fixture deliberately locks only deterministic point estimates, exact
    McNemar tests, Holm correction, pair counts, and decision labels.
    """
    key_path = Path("data/review/core-review-key.csv")
    codes = sorted(Path("data/review/coding/tier1").glob("*-core-codes.csv"))
    if not key_path.exists() or len(codes) != 1:
        pytest.skip("Frozen Tier 1 repository inputs are not present in this test checkout")

    rows = validate_and_join(read_csv(codes[0]), read_csv(key_path))
    panel, hypotheses, *_ = analyze_confirmatory(rows, draws=25)
    by_id = {row["contrast"]: row for row in panel}

    assert set(by_id) == set(EXPECTED)
    for contrast, expected in EXPECTED.items():
        actual = by_id[contrast]
        assert actual["complete_pairs"] == expected["complete_pairs"]
        assert actual["risk_difference_pp"] == pytest.approx(expected["risk_difference_pp"], abs=1e-12)
        assert actual["discordant_favor"] == expected["discordant_favor"]
        assert actual["discordant_oppose"] == expected["discordant_oppose"]
        assert actual["mcnemar_p_raw"] == pytest.approx(expected["mcnemar_p_raw"], rel=1e-12, abs=1e-30)
        assert actual["holm_p"] == pytest.approx(expected["holm_p"], rel=1e-12, abs=1e-30)
        assert actual["confirmatory_decision"] == expected["decision"]

    assert {row["hypothesis"]: row["status"] for row in hypotheses} == {
        "H1": "confirmed",
        "H2": "not_confirmed",
        "H3": "not_confirmed",
    }

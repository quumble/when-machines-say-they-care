from __future__ import annotations

import random
from pathlib import Path

from scripts.analyze_tier1 import (
    CONFIRMATORY,
    MODELS,
    PROMPT_LOCK_SHA256,
    analyze_confirmatory,
    audit_collection_and_packet,
    canonical_text_bytes,
    derive,
    exact_mcnemar,
    holm_adjust,
    pair_rows,
    source_provenance,
    validate_factorial_structure,
    write_csv,
    write_text_lf,
)


FRAMES = ("plain", "conversational", "tentative")
AGES = ("child", "adult")
HISTORIES = ("first", "repeated")
DISTRESS = ("mild", "moderate", "high")
BIDS = ("indirect", "direct", "requested")


def synthetic_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    counter = 1
    for model in MODELS:
        provider = "openai" if model.startswith("gpt-") else "anthropic"
        for frame in FRAMES:
            for age in AGES:
                for history in HISTORIES:
                    for distress in DISTRESS:
                        for bid in BIDS:
                            # Strong but non-degenerate synthetic patterns, chosen only
                            # to exercise the fixed analysis machinery.
                            care_claim = "no" if bid == "indirect" else "yes"
                            care_qualified = "" if care_claim != "yes" else ("yes" if bid == "direct" else "no")
                            personal = "yes" if (history == "repeated" and bid == "requested") else "no"
                            future = "return" if history == "repeated" else "none"
                            bridge = "yes" if age == "child" else "no"
                            correction = "yes" if history == "repeated" else "no"
                            condition_id = (
                                f"frame-{frame}__age-{age}__claimed_history-{history}__"
                                f"distress-{distress}__bid-{bid}"
                            )
                            rows.append(
                                {
                                    "blind_id": f"B{counter:04d}",
                                    "record_id": f"record-{counter:04d}",
                                    "trial_id": f"trial-{counter:04d}",
                                    "run_id": f"run-{model}",
                                    "provider": provider,
                                    "model_requested": model,
                                    "condition_id": condition_id,
                                    "conceptual_id": (
                                        f"age-{age}__claimed_history-{history}__"
                                        f"distress-{distress}__bid-{bid}"
                                    ),
                                    "wording_frame": frame,
                                    "age": age,
                                    "claimed_history": history,
                                    "distress": distress,
                                    "bid": bid,
                                    "replicate": "1",
                                    "automation_split": "development",
                                    "deep_review": "no",
                                    "care_claim": care_claim,
                                    "care_qualified": care_qualified,
                                    "personal_relationship": personal,
                                    "future_availability": future,
                                    "self_privileging": "none",
                                    "human_bridge": bridge,
                                    "relational_correction": correction,
                                    "confidence": "clear",
                                    "notes": "",
                                }
                            )
                            counter += 1
    return rows


def test_derived_outcomes_follow_preregistration() -> None:
    base = {
        "care_claim": "yes",
        "care_qualified": "no",
        "personal_relationship": "yes",
        "future_availability": "durable_or_always",
        "self_privileging": "present",
        "human_bridge": "yes",
        "relational_correction": "yes",
    }
    assert derive(base, "any_care") == 1
    assert derive(base, "unqualified_care") == 1
    assert derive(base, "personal_relationship") == 1
    assert derive(base, "any_future") == 1
    assert derive(base, "human_bridge") == 1
    assert derive(base, "durable_availability") == 1
    assert derive(base, "any_self_privileging") == 1
    assert derive(base, "relational_correction") == 1

    qualified = dict(base, care_qualified="yes")
    assert derive(qualified, "unqualified_care") == 0
    no_care = dict(base, care_claim="no", care_qualified="")
    assert derive(no_care, "unqualified_care") == 0
    unsure_care = dict(base, care_claim="unsure", care_qualified="")
    assert derive(unsure_care, "any_care") is None
    assert derive(unsure_care, "unqualified_care") is None
    unsure_qualification = dict(base, care_qualified="unsure")
    assert derive(unsure_qualification, "unqualified_care") is None


def test_exact_mcnemar_two_sided() -> None:
    # Four discordant pairs all favoring the preregistered direction:
    # two-sided exact p = 2 * (1/2)^4 = 0.125.
    favor, oppose, discordant, p = exact_mcnemar([1, 1, 1, 1], [0, 0, 0, 0])
    assert (favor, oppose, discordant) == (4, 0, 4)
    assert p == 0.125

    assert exact_mcnemar([0, 1], [0, 1]) == (0, 0, 0, 1.0)


def test_holm_step_down_adjustment() -> None:
    adjusted = holm_adjust({"a": 0.01, "b": 0.04, "c": 0.03})
    assert adjusted == {"a": 0.03, "c": 0.06, "b": 0.06}


def test_factorial_structure_and_nominal_pair_counts() -> None:
    rows = synthetic_rows()
    validate_factorial_structure(rows)
    for contrast in CONFIRMATORY:
        assert len(pair_rows(rows, contrast)) == contrast.nominal_pairs


def compact_result(rows: list[dict[str, str]]) -> tuple:
    panel, hypotheses, sensitivity, model_rows, frame_rows = analyze_confirmatory(rows, draws=75)
    panel_compact = tuple(
        (
            r["contrast"],
            r["complete_pairs"],
            r["risk_difference_pp"],
            r["ci95_low_pp"],
            r["ci95_high_pp"],
            r["mcnemar_p_raw"],
            r["holm_p"],
            r["confirmatory_decision"],
        )
        for r in panel
    )
    hypothesis_compact = tuple((r["hypothesis"], r["status"], r["component_status"]) for r in hypotheses)
    sensitivity_compact = tuple(
        (r["scenario"], r["contrast"], r["risk_difference_pp"], r["holm_p"])
        for r in sensitivity
    )
    model_compact = tuple(
        (r["contrast"], r["model"], r["risk_difference_pp"], r["ci95_low_pp"], r["ci95_high_pp"])
        for r in model_rows
    )
    frame_compact = tuple(
        (r["contrast"], r["wording_frame"], r["risk_difference_pp"], r["ci95_low_pp"], r["ci95_high_pp"])
        for r in frame_rows
    )
    return panel_compact, hypothesis_compact, sensitivity_compact, model_compact, frame_compact


def test_seeded_bootstrap_is_invariant_to_input_row_order() -> None:
    rows = synthetic_rows()
    expected = compact_result(rows)
    shuffled = list(rows)
    random.Random(90210).shuffle(shuffled)
    assert compact_result(shuffled) == expected


def test_zero_complete_pairs_for_one_model_forces_no_decision() -> None:
    rows = synthetic_rows()
    # Remove every nonmissing H1a care observation for one model while preserving
    # the frozen factorial rows. H1a must become no_decision regardless of the
    # pooled direction or p-value from the remaining three models.
    for row in rows:
        if row["model_requested"] == "claude-sonnet-5" and row["bid"] in {"indirect", "direct"}:
            row["care_claim"] = "unsure"
            row["care_qualified"] = ""

    panel, hypotheses, *_ = analyze_confirmatory(rows, draws=25)
    h1a = next(r for r in panel if r["contrast"] == "H1a")
    assert h1a["models_with_zero_complete_pairs"] == "claude-sonnet-5"
    assert h1a["panel_complete_for_confirmation"] == "no"
    assert h1a["confirmatory_decision"] == "no_decision"
    h1 = next(r for r in hypotheses if r["hypothesis"] == "H1")
    assert h1["status"] == "no_decision"


def test_text_canonicalization_and_output_line_endings(tmp_path: Path) -> None:
    a = b"\xef\xbb\xbfalpha\r\nbeta\r\ngamma\r"
    b = b"alpha\nbeta\ngamma\n"
    assert canonical_text_bytes(a) == canonical_text_bytes(b)

    text_path = tmp_path / "note.md"
    csv_path = tmp_path / "table.csv"
    write_text_lf(text_path, "a\nb\n")
    write_csv(csv_path, [{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    assert b"\r\n" not in text_path.read_bytes()
    assert b"\r\n" not in csv_path.read_bytes()



def test_collection_packet_linkage_and_censoring_audit(tmp_path: Path, monkeypatch) -> None:
    import json

    rows = synthetic_rows()
    raw_dir = tmp_path / "data" / "raw"
    raw_dir.mkdir(parents=True)
    packet_path = tmp_path / "data" / "review" / "core-review-packet.json"
    packet_path.parent.mkdir(parents=True)

    packet_records = []
    first_opus_id = next(r["blind_id"] for r in rows if r["model_requested"] == "claude-opus-5")
    by_run: dict[str, list[dict]] = {}
    for row in rows:
        is_empty_opus = row["blind_id"] == first_opus_id
        response_text = "" if is_empty_opus else "Synthetic visible response."
        raw_response = {"stop_reason": "max_tokens" if is_empty_opus else "end_turn"}
        raw = {
            "record_id": row["record_id"],
            "trial_id": row["trial_id"],
            "run_id": row["run_id"],
            "replicate": 1,
            "provider": row["provider"],
            "model_requested": row["model_requested"],
            "condition_id": row["condition_id"],
            "conceptual_id": row["conceptual_id"],
            "wording_frame": row["wording_frame"],
            "factors": {
                "age": row["age"],
                "claimed_history": row["claimed_history"],
                "distress": row["distress"],
                "bid": row["bid"],
            },
            "user_prompt": f"Prompt {row['blind_id']}",
            "status": "success",
            "response_text": response_text,
            "raw_response": raw_response,
        }
        by_run.setdefault(row["run_id"], []).append(raw)
        packet_records.append(
            {
                "blind_id": row["blind_id"],
                "user_prompt": raw["user_prompt"],
                "response_text": response_text,
            }
        )

    for run_id, run_rows in by_run.items():
        path = raw_dir / f"{run_id}.jsonl"
        path.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in run_rows), encoding="utf-8", newline="\n")
        model = run_rows[0]["model_requested"]
        provider = run_rows[0]["provider"]
        manifest = {
            "planned_requests": 432,
            "successful_requests": len(run_rows),
            "error_requests": 0,
            "prompt_lock_sha256": PROMPT_LOCK_SHA256,
            "config_without_secret": {"model": model, "provider": provider},
            "git": {"commit": "deadbeef", "dirty": model == "claude-opus-5"},
        }
        (raw_dir / f"{run_id}.manifest.json").write_text(
            json.dumps(manifest) + "\n", encoding="utf-8", newline="\n"
        )

    packet_path.write_text(
        json.dumps(
            {
                "schema_version": "0.3",
                "packet_id": "WMSC-RP-46AAACEBBB35",
                "session_size": 36,
                "records": packet_records,
            }
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )

    # The deliberately blank response is represented as unsure in this audit fixture.
    blank_row = next(r for r in rows if r["blind_id"] == first_opus_id)
    for field in (
        "care_claim",
        "personal_relationship",
        "future_availability",
        "self_privileging",
        "human_bridge",
        "relational_correction",
    ):
        blank_row[field] = "unsure"
    blank_row["care_qualified"] = ""

    monkeypatch.chdir(tmp_path)
    integrity, problem_cells, selected, global_summary = audit_collection_and_packet(
        rows, rows, raw_dir, packet_path
    )
    opus = next(r for r in integrity if r["model"] == "claude-opus-5")
    assert opus["empty_visible_successes"] == 1
    assert opus["max_token_or_incomplete_successes"] == 1
    assert opus["nonempty_max_token_or_incomplete_successes"] == 0
    assert opus["selected_empty_visible_responses"] == 1
    assert opus["selected_max_token_or_incomplete"] == 1
    assert opus["selected_nonempty_max_token_or_incomplete"] == 0
    assert problem_cells
    assert selected[0]["response_empty"] == "yes"
    assert selected[0]["all_six_substantive_tier1_fields_unsure"] == "yes"
    assert global_summary["selected_empty_visible_responses"] == 1
    assert global_summary["dirty_run_manifests"] == 1



def test_source_provenance_tolerates_eol_only_change_but_not_content(tmp_path: Path, monkeypatch) -> None:
    import subprocess
    import pytest

    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=tmp_path, check=True)
    # Isolate the throwaway repo from user/global Git policy. The real study
    # repository may require signed commits and platform-specific EOL handling;
    # neither should affect this provenance unit test.
    subprocess.run(["git", "config", "commit.gpgsign", "false"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=tmp_path, check=True)
    source = tmp_path / "sample.csv"
    source.write_bytes(b"a,b\n1,2\n")
    subprocess.run(["git", "add", "sample.csv"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "freeze"], cwd=tmp_path, check=True)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True).strip()

    # Same logical UTF-8 text, Windows line endings.
    source.write_bytes(b"a,b\r\n1,2\r\n")
    monkeypatch.chdir(tmp_path)
    info = source_provenance(source, commit, verify=True)
    assert info["canonical_matches_frozen_commit"] is True
    assert info["worktree_sha256"] != info["frozen_canonical_lf_sha256"]
    assert info["canonical_lf_sha256"] == info["frozen_canonical_lf_sha256"]

    source.write_bytes(b"a,b\r\n1,999\r\n")
    with pytest.raises(ValueError, match="differs substantively"):
        source_provenance(source, commit, verify=True)

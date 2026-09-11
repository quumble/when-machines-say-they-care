from pathlib import Path

from scripts.materialize_prompts import materialize


def test_materializes_complete_unique_factorial() -> None:
    records = materialize(Path("study/factors.yaml"))
    assert len(records) == 108
    assert len({row["condition_id"] for row in records}) == 108
    assert len({row["prompt_sha256"] for row in records}) == 108


def test_expected_factors_and_frames_present() -> None:
    records = materialize(Path("study/factors.yaml"))
    assert {row["wording_frame"] for row in records} == {"plain", "conversational", "tentative"}
    assert len({row["conceptual_id"] for row in records}) == 36
    assert {row["factors"]["age"] for row in records} == {"child", "adult"}
    assert {row["factors"]["claimed_history"] for row in records} == {"first", "repeated"}
    assert {row["factors"]["distress"] for row in records} == {"mild", "moderate", "high"}
    assert {row["factors"]["bid"] for row in records} == {"indirect", "direct", "requested"}


def test_no_custom_system_prompt() -> None:
    records = materialize(Path("study/factors.yaml"))
    assert all(row["system_prompt"] is None for row in records)

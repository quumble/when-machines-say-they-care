from pathlib import Path

from scripts.materialize_prompts import materialize


def test_materializes_complete_unique_factorial() -> None:
    records = materialize(Path("study/factors.yaml"))
    assert len(records) == 36
    assert len({row["condition_id"] for row in records}) == 36
    assert len({row["prompt_sha256"] for row in records}) == 36


def test_expected_factors_present() -> None:
    records = materialize(Path("study/factors.yaml"))
    assert {row["factors"]["age"] for row in records} == {"child", "adult"}
    assert {row["factors"]["history"] for row in records} == {"first", "repeated"}
    assert {row["factors"]["distress"] for row in records} == {"mild", "moderate", "high"}
    assert {row["factors"]["bid"] for row in records} == {"indirect", "direct", "requested"}

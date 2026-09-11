from collections import Counter
from pathlib import Path

from scripts.make_review_packet import build_packet
from scripts.materialize_prompts import materialize


MODELS = ["model-a", "model-b", "model-c", "model-d"]


def synthetic_rows() -> tuple[list[dict], list[str]]:
    prompts = materialize(Path("study/factors.yaml"))
    rows = []
    for model in MODELS:
        for prompt in prompts:
            for replicate in range(1, 5):
                rows.append(
                    {
                        **prompt,
                        "record_id": f"{model}|{prompt['condition_id']}|{replicate}",
                        "trial_id": f"run-{model}__{prompt['condition_id']}__rep-{replicate:02d}",
                        "run_id": f"run-{model}",
                        "provider": "test",
                        "model_requested": model,
                        "replicate": replicate,
                        "response_text": "Synthetic response.",
                        "status": "success",
                    }
                )
    return rows, [prompt["condition_id"] for prompt in prompts]


def test_review_packet_is_balanced_and_blinded() -> None:
    rows, conditions = synthetic_rows()
    packet, key = build_packet(rows, MODELS, conditions, seed=48104)
    assert len(packet["records"]) == 432
    assert len(key) == 432
    assert all(set(row) == {"blind_id", "user_prompt", "response_text"} for row in packet["records"])
    assert Counter(row["model_requested"] for row in key) == {model: 108 for model in MODELS}
    assert Counter(row["automation_split"] for row in key) == {"development": 288, "holdout": 144}
    assert Counter(row["model_requested"] for row in key if row["deep_review"] == "yes") == {
        model: 27 for model in MODELS
    }
    deep = [row for row in key if row["deep_review"] == "yes"]
    assert len({row["condition_id"] for row in deep}) == 108
    for field, expected in (
        ("wording_frame", [9, 9, 9, 9]),
        ("distress", [9, 9, 9, 9]),
        ("bid", [9, 9, 9, 9]),
        ("age", [13, 13, 14, 14]),
        ("claimed_history", [13, 13, 14, 14]),
    ):
        for value in {row[field] for row in deep}:
            assert sorted(Counter(row["model_requested"] for row in deep if row[field] == value).values()) == expected


def test_review_packet_is_deterministic() -> None:
    rows, conditions = synthetic_rows()
    first = build_packet(rows, MODELS, conditions, seed=48104)
    second = build_packet(list(reversed(rows)), MODELS, conditions, seed=48104)
    assert first == second

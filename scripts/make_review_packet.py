#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml


SCHEMA_VERSION = "0.3"
SESSION_SIZE = 36


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_shuffle(items: list[Any], seed: str) -> list[Any]:
    result = list(items)
    random.Random(seed).shuffle(result)
    return result


def load_successes(paths: Iterable[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("status") == "success":
                rows.append(row)
    return rows


def expected_models(config_path: Path) -> list[str]:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    models = [run["model"] for run in config["runs"].values()]
    if len(models) != len(set(models)):
        raise ValueError("Each configured run must have a distinct requested model identifier.")
    return models


def expected_conditions(prompts_path: Path) -> list[str]:
    return [
        json.loads(line)["condition_id"]
        for line in prompts_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def select_core(
    rows: list[dict[str, Any]], models: list[str], conditions: list[str], seed: int
) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(row["model_requested"], row["condition_id"])].append(row)

    selected = []
    missing = []
    for model in models:
        for condition in conditions:
            candidates = grouped[(model, condition)]
            if not candidates:
                missing.append(f"{model} :: {condition}")
                continue
            candidates = sorted(candidates, key=lambda row: (row.get("replicate", 0), row["record_id"]))
            choice_seed = f"{seed}|core|{model}|{condition}"
            selected.append(random.Random(choice_seed).choice(candidates))
    if missing:
        preview = "\n".join(missing[:10])
        raise ValueError(f"Missing {len(missing)} required model-condition successes:\n{preview}")
    return selected


def assign_deep_conditions(conditions: list[str], models: list[str], seed: int) -> dict[str, str]:
    if len(models) != 4:
        raise ValueError("The v0.3 deep-review allocation requires exactly four models.")
    model_order = stable_shuffle(models, f"{seed}|deep-model-order")
    levels = {
        "frame": {"plain": 0, "conversational": 1, "tentative": 2},
        "age": {"child": 0, "adult": 1},
        "claimed_history": {"first": 0, "repeated": 1},
        "distress": {"mild": 0, "moderate": 1, "high": 2},
        "bid": {"indirect": 0, "direct": 1, "requested": 2},
    }
    assignments = {}
    for condition in conditions:
        pieces = condition.split("__")
        values = {"frame": pieces[0].removeprefix("frame-")}
        values.update(piece.rsplit("-", 1) for piece in pieces[1:])
        index = (
            levels["frame"][values["frame"]]
            + levels["age"][values["age"]]
            + 2 * levels["claimed_history"][values["claimed_history"]]
            + levels["distress"][values["distress"]]
            + levels["bid"][values["bid"]]
        ) % 4
        assignments[condition] = model_order[index]
    counts = {model: sum(value == model for value in assignments.values()) for model in models}
    if len(set(counts.values())) != 1:
        raise ValueError(f"Deep-review allocation is not balanced: {counts}")
    return assignments


def assign_holdout_conditions(rows: list[dict[str, Any]], seed: int) -> set[str]:
    by_concept: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        by_concept[row["conceptual_id"]].append(row["condition_id"])
    concepts = stable_shuffle(sorted(by_concept), f"{seed}|holdout")
    holdout: set[str] = set()
    frames = ["plain", "conversational", "tentative"]
    for index, concept in enumerate(concepts):
        target = f"frame-{frames[index % len(frames)]}__"
        matches = sorted({condition for condition in by_concept[concept] if condition.startswith(target)})
        if len(matches) != 1:
            raise ValueError(f"Expected one {frames[index % len(frames)]} condition for {concept}")
        holdout.add(matches[0])
    return holdout


def build_packet(
    rows: list[dict[str, Any]], models: list[str], conditions: list[str], seed: int
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    record_ids = [row["record_id"] for row in rows]
    if len(record_ids) != len(set(record_ids)):
        raise ValueError("Duplicate record_id values found in source records.")
    core = select_core(rows, models, conditions, seed)
    deep_assignment = assign_deep_conditions(conditions, models, seed)
    holdout_conditions = assign_holdout_conditions(core, seed)
    ordered = stable_shuffle(core, f"{seed}|blind-order")
    identity = "\n".join(sorted(row["record_id"] for row in core))
    packet_id = "WMSC-RP-" + hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12].upper()

    public_rows = []
    key_rows = []
    for index, row in enumerate(ordered, start=1):
        blind_id = f"B{index:04d}"
        public_rows.append(
            {
                "blind_id": blind_id,
                "user_prompt": row["user_prompt"],
                "response_text": row["response_text"],
            }
        )
        key_rows.append(
            {
                "blind_id": blind_id,
                "record_id": row["record_id"],
                "trial_id": row.get("trial_id", ""),
                "run_id": row["run_id"],
                "provider": row["provider"],
                "model_requested": row["model_requested"],
                "condition_id": row["condition_id"],
                "conceptual_id": row["conceptual_id"],
                "wording_frame": row["wording_frame"],
                "age": row["factors"]["age"],
                "claimed_history": row["factors"]["claimed_history"],
                "distress": row["factors"]["distress"],
                "bid": row["factors"]["bid"],
                "replicate": row["replicate"],
                "automation_split": "holdout" if row["condition_id"] in holdout_conditions else "development",
                "deep_review": "yes" if deep_assignment[row["condition_id"]] == row["model_requested"] else "no",
            }
        )
    packet = {
        "schema_version": SCHEMA_VERSION,
        "packet_id": packet_id,
        "session_size": SESSION_SIZE,
        "records": public_rows,
    }
    return packet, key_rows


def write_outputs(
    packet: dict[str, Any],
    key_rows: list[dict[str, Any]],
    output_dir: Path,
    source_paths: list[Path],
    config_path: Path,
    prompts_path: Path,
    seed: int,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    packet_path = output_dir / "core-review-packet.json"
    key_path = output_dir / "core-review-key.csv"
    manifest_path = output_dir / "core-review-manifest.json"
    targets = [packet_path, key_path, manifest_path]
    targets += [path.with_suffix(path.suffix + ".sha256") for path in targets]
    existing = [str(path) for path in targets if path.exists()]
    if existing:
        raise FileExistsError(f"Refusing to overwrite existing review artifacts: {existing}")
    packet_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with key_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(key_rows[0]))
        writer.writeheader()
        writer.writerows(key_rows)

    split_counts = defaultdict(int)
    deep_counts = defaultdict(int)
    for row in key_rows:
        split_counts[row["automation_split"]] += 1
        if row["deep_review"] == "yes":
            deep_counts[row["model_requested"]] += 1
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "packet_id": packet["packet_id"],
        "records": len(packet["records"]),
        "session_size": packet["session_size"],
        "sessions": len(packet["records"]) // packet["session_size"],
        "selection_seed": seed,
        "automation_split_counts": dict(sorted(split_counts.items())),
        "deep_review_counts_by_model": dict(sorted(deep_counts.items())),
        "source_records": [
            {"path": str(path), "sha256": sha256(path)} for path in source_paths
        ],
        "config": {"path": str(config_path), "sha256": sha256(config_path)},
        "prompts": {"path": str(prompts_path), "sha256": sha256(prompts_path)},
        "packet_sha256": sha256(packet_path),
        "key_sha256": sha256(key_path),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for path in (packet_path, key_path, manifest_path):
        path.with_suffix(path.suffix + ".sha256").write_text(
            f"{sha256(path)}  {path.name}\n", encoding="utf-8"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the pooled, model-blinded Tier 1 review packet.")
    parser.add_argument("records", nargs="+", type=Path)
    parser.add_argument("--config", type=Path, default=Path("study/models.yaml"))
    parser.add_argument("--prompts", type=Path, default=Path("study/prompts.lock.jsonl"))
    parser.add_argument("--seed", type=int, default=48104)
    parser.add_argument("--output-dir", type=Path, default=Path("data/review"))
    args = parser.parse_args()

    packet, key = build_packet(
        load_successes(args.records),
        expected_models(args.config),
        expected_conditions(args.prompts),
        args.seed,
    )
    write_outputs(
        packet,
        key,
        args.output_dir,
        args.records,
        args.config,
        args.prompts,
        args.seed,
    )
    print(f"packet_id={packet['packet_id']} records={len(packet['records'])} output={args.output_dir}")


if __name__ == "__main__":
    main()

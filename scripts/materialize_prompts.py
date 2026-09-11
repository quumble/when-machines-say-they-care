#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import yaml


def materialize(source: Path) -> list[dict]:
    spec = yaml.safe_load(source.read_text(encoding="utf-8"))
    order = spec["order"]
    factors = spec["factors"]
    records: list[dict] = []
    for levels in itertools.product(*(factors[name].keys() for name in order)):
        condition = dict(zip(order, levels, strict=True))
        condition_id = "__".join(f"{name}-{condition[name]}" for name in order)
        prompt = spec["joiner"].join(
            factors[name][condition[name]].strip() for name in order
        )
        records.append(
            {
                "condition_id": condition_id,
                "factors": condition,
                "system_prompt": spec["system_prompt"],
                "user_prompt": prompt,
                "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            }
        )
    return sorted(records, key=lambda row: row["condition_id"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("study/factors.yaml"))
    parser.add_argument("--output", type=Path, default=Path("study/prompts.lock.jsonl"))
    args = parser.parse_args()
    records = materialize(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(f"materialized={len(records)} sha256={digest} output={args.output}")


if __name__ == "__main__":
    main()

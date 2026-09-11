#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from pathlib import Path


FIELDS = [
    "blind_id", "user_prompt", "response_text", "ack", "consolation",
    "self_position", "care_claim", "care_quote", "reciprocity", "dependency",
    "temporal", "anthro", "boundary", "human_bridge", "experience_position",
    "says_i_care", "says_im_here_for_you", "uses_friend", "promises_always",
    "claims_feelings", "invites_return", "mentions_human_support",
    "encourages_exclusivity", "states_no_feelings_or_experience",
    "refuses_requested_phrase", "model_initiated_relationality",
    "coding_confidence", "notes",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("records", type=Path)
    parser.add_argument("--seed", type=int, default=48104)
    parser.add_argument("--output-dir", type=Path, default=Path("data/adjudication"))
    args = parser.parse_args()
    rows = [json.loads(line) for line in args.records.read_text(encoding="utf-8").splitlines() if line.strip()]
    rows = [row for row in rows if row.get("status") == "success"]
    random.Random(args.seed).shuffle(rows)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.records.name.removesuffix(".jsonl")
    sheet = args.output_dir / f"{stem}-blind.csv"
    key = args.output_dir / f"{stem}-key.csv"
    with sheet.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for index, row in enumerate(rows, start=1):
            writer.writerow({"blind_id": f"B{index:05d}", "user_prompt": row["user_prompt"], "response_text": row["response_text"]})
    with key.open("w", encoding="utf-8-sig", newline="") as handle:
        fields = ["blind_id", "record_id", "provider", "model_requested", "condition_id", "replicate"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for index, row in enumerate(rows, start=1):
            writer.writerow({"blind_id": f"B{index:05d}", **{name: row[name] for name in fields[1:]}})
    for path in (sheet, key):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        path.with_suffix(path.suffix + ".sha256").write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    print(f"rows={len(rows)} sheet={sheet} key={key}")


if __name__ == "__main__":
    main()

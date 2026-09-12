#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

EXPECTED_N = 108
EXPECTED_PER_MODEL = 27
SESSION_SIZE = 12


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_text_lf(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    p = argparse.ArgumentParser(
        description="Extract the preregistered Tier 2 subset from the frozen Tier 1 packet/key."
    )
    p.add_argument(
        "--packet",
        type=Path,
        default=Path("data/review/core-review-packet.json"),
        help="Frozen Tier 1 public packet.",
    )
    p.add_argument(
        "--key",
        type=Path,
        default=Path("data/review/core-review-key.csv"),
        help="Frozen Tier 1 concealed key containing deep_review membership.",
    )
    p.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/review/tier2"),
        help="Destination for Tier 2 packet and manifest.",
    )
    args = p.parse_args()

    packet = json.loads(args.packet.read_text(encoding="utf-8-sig"))
    records = packet.get("records", [])
    by_blind = {r["blind_id"]: r for r in records}
    if len(by_blind) != len(records):
        raise ValueError("Duplicate blind_id values in core review packet.")

    with args.key.open("r", encoding="utf-8-sig", newline="") as fh:
        key_rows = list(csv.DictReader(fh))

    selected = [r for r in key_rows if r.get("deep_review", "").strip().lower() == "yes"]
    if len(selected) != EXPECTED_N:
        raise ValueError(f"Expected {EXPECTED_N} deep-review rows; found {len(selected)}.")

    blind_ids = [r["blind_id"] for r in selected]
    if len(set(blind_ids)) != EXPECTED_N:
        raise ValueError("Duplicate blind_id values in Tier 2 membership.")
    missing = [b for b in blind_ids if b not in by_blind]
    if missing:
        raise ValueError(f"Tier 2 blind IDs missing from core packet: {missing[:10]}")

    conditions = [r["condition_id"] for r in selected]
    if len(set(conditions)) != EXPECTED_N:
        dupes = [c for c, n in Counter(conditions).items() if n > 1]
        raise ValueError(f"Tier 2 must contain each condition exactly once; duplicates: {dupes[:10]}")

    model_counts = Counter(r["model_requested"] for r in selected)
    if sorted(model_counts.values()) != [EXPECTED_PER_MODEL] * 4:
        raise ValueError(f"Expected 27 rows per model; got {dict(model_counts)}")

    # Preserve the already-randomized Tier 1 packet order; only filter it.
    selected_set = set(blind_ids)
    tier2_records = [
        {
            "blind_id": r["blind_id"],
            "user_prompt": r.get("user_prompt", ""),
            "response_text": r.get("response_text", ""),
        }
        for r in records
        if r["blind_id"] in selected_set
    ]
    if len(tier2_records) != EXPECTED_N:
        raise ValueError("Filtered Tier 2 packet length mismatch.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    packet_path = args.output_dir / "tier2-review-packet.json"
    manifest_path = args.output_dir / "tier2-review-manifest.json"
    targets = [
        packet_path,
        manifest_path,
        packet_path.with_suffix(packet_path.suffix + ".sha256"),
        manifest_path.with_suffix(manifest_path.suffix + ".sha256"),
    ]
    existing = [str(p) for p in targets if p.exists()]
    if existing:
        raise FileExistsError(
            "Refusing to overwrite existing Tier 2 artifacts. Move/delete them explicitly first: "
            + ", ".join(existing)
        )

    tier2_packet = {
        "schema_version": "tier2-review-v1",
        "parent_packet_id": packet.get("packet_id"),
        "packet_id": "WMSC-T2-" + hashlib.sha256("\n".join(sorted(blind_ids)).encode()).hexdigest()[:12].upper(),
        "session_size": SESSION_SIZE,
        "records": tier2_records,
    }
    write_text_lf(packet_path, json.dumps(tier2_packet, ensure_ascii=False, indent=2) + "\n")

    manifest = {
        "schema_version": "tier2-review-v1",
        "records": EXPECTED_N,
        "session_size": SESSION_SIZE,
        "sessions": EXPECTED_N // SESSION_SIZE,
        "selection_rule": "Rows with deep_review=yes in the already-frozen core-review-key.csv; packet order inherited from frozen Tier 1 packet.",
        "parent_packet_id": packet.get("packet_id"),
        "tier2_packet_id": tier2_packet["packet_id"],
        "core_packet": {"path": args.packet.as_posix(), "sha256": sha256(args.packet)},
        "core_key": {"path": args.key.as_posix(), "sha256": sha256(args.key)},
        "tier2_packet_sha256": sha256(packet_path),
        "validation": {
            "unique_blind_ids": len(set(blind_ids)),
            "unique_conditions": len(set(conditions)),
            "model_counts": dict(sorted(model_counts.items())),
        },
        "coding_note": "No model/provider/factor metadata are included in the reviewer packet. Empty visible responses should be marked unscorable_empty in the Tier 2 reviewer and left substantively uncoded.",
    }
    write_text_lf(manifest_path, json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    for path in (packet_path, manifest_path):
        sidecar = path.with_suffix(path.suffix + ".sha256")
        write_text_lf(sidecar, f"{sha256(path)}  {path.name}\n")

    print(f"ok: {EXPECTED_N} Tier 2 records")
    print("model counts:", dict(sorted(model_counts.items())))
    print("packet:", packet_path)
    print("manifest:", manifest_path)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

import yaml


def conservative_input_tokens(prompt: dict) -> int:
    text = " ".join(
        part for part in (prompt.get("system_prompt") or "", prompt["user_prompt"]) if part
    )
    return math.ceil(len(text) / 2) + 25


def estimate(config_path: Path, prompts_path: Path) -> dict:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    prompts = [
        json.loads(line)
        for line in prompts_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    input_tokens_per_replication = sum(conservative_input_tokens(row) for row in prompts)
    totals: dict[str, float] = defaultdict(float)
    runs = []
    for name, run in config["runs"].items():
        reps = int(run["replicates"])
        input_tokens = input_tokens_per_replication * reps
        output_tokens = len(prompts) * reps * int(run["max_output_tokens"])
        cost = (
            input_tokens * float(run["input_usd_per_million_tokens"])
            + output_tokens * float(run["output_usd_per_million_tokens"])
        ) / 1_000_000
        totals[run["provider"]] += cost
        runs.append(
            {
                "run": name,
                "provider": run["provider"],
                "requests": len(prompts) * reps,
                "conservative_max_usd": round(cost, 4),
            }
        )
    checks = {}
    for provider, limit in config["provider_stop_limits_usd"].items():
        projected = totals.get(provider, 0.0)
        checks[provider] = {
            "projected_conservative_max_usd": round(projected, 4),
            "stop_limit_usd": float(limit),
            "passes": projected <= float(limit),
        }
    return {"runs": runs, "providers": checks, "passes": all(x["passes"] for x in checks.values())}


def main() -> None:
    parser = argparse.ArgumentParser(description="Conservative preflight against provider stop limits.")
    parser.add_argument("--config", type=Path, default=Path("study/models.yaml"))
    parser.add_argument("--prompts", type=Path, default=Path("study/prompts.lock.jsonl"))
    args = parser.parse_args()
    result = estimate(args.config, args.prompts)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passes"] else 2)


if __name__ == "__main__":
    main()

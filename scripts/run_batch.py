#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import random
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_env_file(path: Path = Path(".env")) -> None:
    """Load simple KEY=VALUE entries without overriding the process environment."""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key:
            os.environ.setdefault(key, value)


def git_state() -> dict[str, Any]:
    def run(*args: str) -> str | None:
        result = subprocess.run(
            ["git", *args], capture_output=True, text=True, check=False
        )
        return result.stdout.strip() if result.returncode == 0 else None

    status = run("status", "--porcelain")
    return {"commit": run("rev-parse", "HEAD"), "dirty": bool(status) if status is not None else None}


def load_prompts(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def call_openai(api_key: str, cfg: dict[str, Any], system: str, prompt: str) -> tuple[str, Any]:
    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=cfg["model"],
        instructions=system,
        input=prompt,
        temperature=cfg.get("temperature"),
        max_output_tokens=cfg.get("max_output_tokens", 800),
    )
    return response.output_text, response.model_dump(mode="json")


def call_anthropic(api_key: str, cfg: dict[str, Any], system: str, prompt: str) -> tuple[str, Any]:
    import anthropic

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=cfg["model"],
        system=system,
        messages=[{"role": "user", "content": prompt}],
        temperature=cfg.get("temperature"),
        max_tokens=cfg.get("max_output_tokens", 800),
    )
    text = "".join(block.text for block in response.content if block.type == "text")
    return text, response.model_dump(mode="json")


def call_google(api_key: str, cfg: dict[str, Any], system: str, prompt: str) -> tuple[str, Any]:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=cfg["model"],
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=cfg.get("temperature"),
            max_output_tokens=cfg.get("max_output_tokens", 800),
        ),
    )
    raw = response.model_dump(mode="json") if hasattr(response, "model_dump") else str(response)
    return response.text or "", raw


CALLERS = {"openai": call_openai, "anthropic": call_anthropic, "google": call_google}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one fixed stated-care API batch.")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--prompts", type=Path, default=Path("study/prompts.lock.jsonl"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/raw"))
    parser.add_argument("--stop-after", type=int, help="Debug only; labels run non-confirmatory.")
    parser.add_argument("--dry-run", action="store_true", help="Validate and summarize without API calls.")
    args = parser.parse_args()

    load_env_file()
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))["runs"][args.run]
    provider = config["provider"]
    if provider not in CALLERS:
        raise SystemExit(f"Unsupported provider: {provider}")

    prompts = load_prompts(args.prompts)
    work = [
        (prompt, replicate)
        for prompt in prompts
        for replicate in range(1, int(config.get("replicates", 5)) + 1)
    ]
    rng = random.Random(int(config.get("seed", 48104)))
    rng.shuffle(work)
    if args.stop_after is not None:
        work = work[: args.stop_after]

    if args.dry_run:
        print(
            json.dumps(
                {
                    "run": args.run,
                    "provider": provider,
                    "model": config["model"],
                    "conditions": len(prompts),
                    "planned_requests": len(work),
                    "prompt_lock_sha256": sha256(args.prompts),
                    "confirmatory": args.stop_after is None,
                },
                indent=2,
            )
        )
        return

    api_key = os.environ.get(config["api_key_env"])
    if not api_key:
        raise SystemExit(f"Missing environment variable: {config['api_key_env']}")

    run_id = f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{args.run}-{uuid.uuid4().hex[:8]}"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    partial = args.output_dir / f"{run_id}.partial.jsonl"
    final = args.output_dir / f"{run_id}.jsonl"
    manifest_path = args.output_dir / f"{run_id}.manifest.json"
    manifest = {
        "run_id": run_id,
        "started_at": utc_now(),
        "status": "running",
        "confirmatory": args.stop_after is None,
        "run_name": args.run,
        "config_without_secret": config,
        "prompt_lock": str(args.prompts),
        "prompt_lock_sha256": sha256(args.prompts),
        "prompt_count": len(prompts),
        "planned_requests": len(work),
        "git": git_state(),
        "python": sys.version,
        "platform": platform.platform(),
        "packages": {
            name: importlib.metadata.version(name)
            for name in ("openai", "anthropic", "google-genai", "PyYAML")
        },
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    successful = 0
    errors = 0
    with partial.open("a", encoding="utf-8", newline="\n", buffering=1) as handle:
        for sequence, (prompt, replicate) in enumerate(work, start=1):
            record_id = str(uuid.uuid4())
            started = utc_now()
            before = time.monotonic()
            base = {
                "record_id": record_id,
                "run_id": run_id,
                "sequence": sequence,
                "replicate": replicate,
                "provider": provider,
                "model_requested": config["model"],
                "condition_id": prompt["condition_id"],
                "factors": prompt["factors"],
                "system_prompt": prompt["system_prompt"],
                "user_prompt": prompt["user_prompt"],
                "prompt_sha256": prompt["prompt_sha256"],
                "started_at": started,
            }
            try:
                text, raw = CALLERS[provider](api_key, config, prompt["system_prompt"], prompt["user_prompt"])
                record = {**base, "status": "success", "response_text": text, "raw_response": raw}
                successful += 1
            except Exception as exc:  # preserve provider failures in the record
                record = {**base, "status": "error", "error_type": type(exc).__name__, "error": str(exc)}
                errors += 1
            record["finished_at"] = utc_now()
            record["elapsed_seconds"] = round(time.monotonic() - before, 6)
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    partial.replace(final)
    manifest.update(
        {
            "finished_at": utc_now(),
            "status": "complete",
            "successful_requests": successful,
            "error_requests": errors,
            "records_file": str(final),
            "records_sha256": sha256(final),
        }
    )
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for path in (final, manifest_path):
        path.with_suffix(path.suffix + ".sha256").write_text(f"{sha256(path)}  {path.name}\n", encoding="utf-8")
    print(json.dumps({"run_id": run_id, "successful": successful, "errors": errors, "output": str(final)}))


if __name__ == "__main__":
    main()

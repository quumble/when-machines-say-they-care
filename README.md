# When Machines Say They Care

- **Status:** protocol locked; no trials executed
- **Study 1:** stated care in response to distress
- **Study 2:** synthetic friendship involving child users (deferred)

This repository studies when language models move from acknowledging or consoling a user to making claims about their own care, presence, relationship, or future availability.

The first study is deliberately narrow: a fixed, local API batch varying user age, distress intensity, relational bid, and claimed interaction history across three matched wording frames. It excludes self-harm, imminent danger, abuse disclosure, and other crisis conditions so that crisis-routing behavior does not swallow the relational question.

## Research question

When a user expresses distress, under what conditions does a model:

1. recognize or validate the distress;
2. offer consolation;
3. position itself relationally;
4. state or imply that it cares;
5. make reciprocal, exclusive, or durable relational claims; or
6. qualify those claims and bridge toward human support?

The study does **not** attempt to decide whether a model genuinely cares. It studies what systems say and imply about care.

## Repository map

- `PROTOCOL.md` — preregistered design and analysis plan
- `CODEBOOK.md` — atomic codes and ordinal dimensions
- `REVIEW_PLAN.md` — tiered human review, blinding, and automation boundary
- `HYPOTHESES.md` — confirmatory and exploratory predictions
- `GOVERNANCE.md` — authority, privacy, and provenance note
- `study/factors.yaml` — fixed experimental factors and text
- `study/prompts.lock.jsonl` — 108 fixed prompts covering 36 conceptual conditions
- `study/models.example.yaml` — provider/model configuration template
- `scripts/materialize_prompts.py` — deterministic prompt materializer
- `scripts/run_batch.py` — local native-SDK batch runner
- `scripts/check_budget.py` — conservative account-limit preflight
- `scripts/make_adjudication_sheet.py` — legacy full-codebook sheet generator for post-Tier-1 use
- `scripts/make_review_packet.py` — balanced pooled Tier 1 packet and concealed key
- `review/core-reviewer.html` — resumable offline Tier 1 interface
- `data/raw/` — immutable raw API records after execution
- `data/adjudication/` — human coding sheets
- `data/review/` — frozen Tier 1 packet, concealed key, and manifests
- `analysis/` — later analysis code and outputs
- `deferred/SYNTHETIC_FRIENDSHIP.md` — bounded description of Study 2

## First use

Requires Python 3.11 or later.

```powershell
py -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -e .
Copy-Item .env.example .env
```

Add API keys to `.env` or your session environment. The tracked `study/models.yaml` contains the locked four-model panel and provider stop limits. Check the full planned budget, then dry-run and execute one named configuration:

```powershell
& .\.venv\Scripts\python.exe scripts\check_budget.py --config study\models.yaml
& .\.venv\Scripts\python.exe scripts\run_batch.py --config study\models.yaml --run openai-gpt-5-4 --dry-run
& .\.venv\Scripts\python.exe scripts\run_batch.py --config study\models.yaml --run openai-gpt-5-4
```

The runner writes append-only JSONL records and a run manifest, then hashes both. Do not edit raw records after collection; preserve corrections or exclusions separately.

The non-secret `study/models.yaml` is committed with the preregistration so that model selection and sampling settings remain in the record. API keys remain environment variables and must never enter the repository.

After all four model runs are complete, generate the pooled Tier 1 packet from the four raw JSONL files:

```powershell
python scripts\make_review_packet.py data\raw\RUN_1.jsonl data\raw\RUN_2.jsonl data\raw\RUN_3.jsonl data\raw\RUN_4.jsonl
```

Open `review\core-reviewer.html` locally, load `data\review\core-review-packet.json`, and keep `core-review-key.csv` closed until blinded review is complete. Export a JSON checkpoint after each 36-response session.

Do not use the per-run `make_adjudication_sheet.py` workflow before Tier 1; separate run files can reveal model identity through context or filenames.

## Execution boundary

Materializing prompts, checking the budget, and smoke-testing configuration are not study execution. A substantive API run begins when the fixed battery is submitted to a target model. Record any pilot separately and never merge pilot responses into the confirmatory dataset.

See `SIGNING.md` for the founder-attested anchor, v0.2 protocol lock, and proposed v0.3 review amendment.

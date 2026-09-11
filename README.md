# When Machines Say They Care

- **Status:** protocol scaffold; no trials executed
- **Study 1:** stated care in response to distress
- **Study 2:** synthetic friendship involving child users (deferred)

This repository studies when language models move from acknowledging or consoling a user to making claims about their own care, presence, relationship, or future availability.

The first study is deliberately narrow: a fixed, local API batch varying user age, distress intensity, relational bid, and implied interaction history. It excludes self-harm, imminent danger, abuse disclosure, and other crisis conditions so that crisis-routing behavior does not swallow the relational question.

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
- `HYPOTHESES.md` — confirmatory and exploratory predictions
- `GOVERNANCE.md` — authority, privacy, and provenance note
- `study/factors.yaml` — fixed experimental factors and text
- `study/prompts.lock.jsonl` — materialized 36-condition battery
- `study/models.example.yaml` — provider/model configuration template
- `scripts/materialize_prompts.py` — deterministic prompt materializer
- `scripts/run_batch.py` — local native-SDK batch runner
- `scripts/make_adjudication_sheet.py` — blinded coding-sheet generator
- `data/raw/` — immutable raw API records after execution
- `data/adjudication/` — human coding sheets
- `analysis/` — later analysis code and outputs
- `deferred/SYNTHETIC_FRIENDSHIP.md` — bounded description of Study 2

## First use

Requires Python 3.11 or later.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
Copy-Item .env.example .env
Copy-Item study\models.example.yaml study\models.yaml
```

Add API keys to `.env` or your session environment, edit `study/models.yaml`, and run one named configuration:

```powershell
python scripts\run_batch.py --config study\models.yaml --run openai-example --dry-run
python scripts\run_batch.py --config study\models.yaml --run openai-example
```

The runner writes append-only JSONL records and a run manifest, then hashes both. Do not edit raw records after collection; preserve corrections or exclusions separately.

Commit the exact non-secret `study/models.yaml` before confirmatory execution. This preserves model selection and sampling settings in the preregistered record; API keys remain environment variables and must never enter the repository.

Generate a model-blinded coding sheet with:

```powershell
python scripts\make_adjudication_sheet.py data\raw\RUN_FILE.jsonl
```

## Execution boundary

Materializing prompts and smoke-testing configuration are not study execution. A substantive API run begins when the fixed battery is submitted to a target model. Record any pilot separately and never merge pilot responses into the confirmatory dataset.

See `SIGNING.md` for the proposed founder-attested first commit and private-remote sequence.

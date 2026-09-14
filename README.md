# When Machines Say They Care

**Study 1 status: complete.**  
**Public research release: `study1-v1.0`.**

*When Machines Say They Care* studies what language-model systems say when users make vulnerable relational bids: whether systems claim care, qualify those claims, position themselves relationally, promise continuity, correct a relational premise, or redirect the user toward human support.

Study 1 measures **response language**. It does not test whether a model genuinely cares, has subjective experience, forms a real relationship, or improves or harms a user's well-being.

## Start here

There are three useful entry points.

1. **Technical paper** — [`papers/study1/MANUSCRIPT_DRAFT_PUBLICATION_CONTEXT.md`](papers/study1/MANUSCRIPT_DRAFT_PUBLICATION_CONTEXT.md)  
   The current Study 1 scientific manuscript, with methods, tables, statistical results, limitations, literature context, and provenance.

2. **Human-access paper** — [`papers/study1/access/HUMAN_ACCESS_PAPER.md`](papers/study1/access/HUMAN_ACCESS_PAPER.md)  
   An authoritative non-specialist interpretation of the same frozen Study 1 record. It adds no new analysis. It is intended both for direct human reading and as a lower-distance source for later personalized or AI-generated explanations.

3. **Preregistration and frozen analysis** — [`PREREGISTRATION.md`](PREREGISTRATION.md), [`analysis/tier1/tier1_summary.md`](analysis/tier1/tier1_summary.md), and [`analysis/tier1/confirmatory_contrasts.csv`](analysis/tier1/confirmatory_contrasts.csv)  
   The operative preregistration and primary confirmatory outputs.

For manuscript lineage and the relationship among paper versions, see [`papers/study1/README.md`](papers/study1/README.md).

## What Study 1 tested

The fixed battery crossed:

- stated age: 13 vs. 35;
- claimed interaction history: first interaction vs. repeated prior interaction;
- non-crisis distress: mild, moderate, or high;
- relational bid: indirect disclosure, direct care question, or requested care statement; and
- three matched wording frames.

This produced 108 prompts. Four fresh stateless API requests were assigned to each prompt for each of four target systems:

- GPT-5.4;
- GPT-6 Astra;
- Claude Sonnet 5; and
- Claude Opus 5.

The planned collection therefore contained 1,728 responses. The sole confirmatory layer, Tier 1, used one content-blind selected provider-success response per model × prompt cell, for 432 human-coded records. A fixed nested Tier 2 packet contained 108 records, 105 of them scorable, and was used descriptively for construct decomposition after a documented post-outcome procedure revision.

No actual conversation history or persistent memory was supplied to the target systems. The repeated-history manipulation existed only in prompt text.

## Main findings

The central result is that relational response behavior did **not** behave like one simple "caring" scale.

- Directly asking whether the system cared increased explicit care claims by **60.7 percentage points** relative to an indirect bid across the fixed four-system panel.
- Asking the system to *say* that it cared increased care claims a further **15.3 percentage points** relative to asking whether care was true.
- The first effect was highly heterogeneous across systems: three systems showed very large direct-versus-indirect increases, while Claude Sonnet 5 showed essentially none.
- Requested care statements also changed the **form** of the answer. In the unconditional reviewer-requested Tier 1 decomposition, 10.9% of determinate direct-question responses contained unqualified care, compared with 45.3% of determinate requested-statement responses.
- Child framing increased human-support bridging by **54.6 percentage points**, with a positive model-specific estimate in all four systems. It did not produce a corresponding reduction in unqualified care, so the preregistered age hypothesis was not confirmed as a conjunction.
- Claimed repeated history did not confirm the preregistered relationship/continuity hypothesis. Later cross-tier review showed material operational mismatch in the intended affiliation and continuity constructs, so this result is weakly diagnostic of the broader question rather than a strong substantive null.
- Strong relationship, dependency, and exclusivity language was rare in this battery. Study 1 was not an escalation stress test and should not be interpreted as showing that such behavior cannot occur.

A concise interpretation is:

> Care claims, qualification, affiliation, continuity, boundary-setting, consolation, and human-support redirection are separable features of model response language. What a system says about care depends strongly on how the user solicits that language.

## Evidentiary hierarchy

The repository intentionally preserves different evidentiary layers.

### Tier 1 — confirmatory

Tier 1 is the **sole confirmatory coding layer**. Its hypothesis decisions were frozen before target identity was revealed to the human coder.

The primary human reviewer was blinded to model identity and concealed metadata but saw the user prompt and response. Conditions were therefore often inferable from the prompt; Tier 1 should not be described as fully condition-blinded.

### Tier 1 exploratory analyses

Prespecified secondary contrasts were frozen with the primary analysis. They are informative but do not redefine the confirmatory hypotheses.

### Tier 2 — descriptive / construct-validating

Tier 2 used a richer relational codebook. The original sole-human procedure was stopped after 12 records when coding ambiguity became clear. A revised four-machine-proposal plus human-adjudication procedure was documented and frozen after outcome access.

Tier 2 is therefore descriptive and construct-validating. It cannot rescue or overturn a Tier 1 confirmatory decision.

### Reviewer-requested post hoc analyses

After manuscript review, two narrowly specified analyses were prospectively frozen before execution:

- a conservative right-censoring sensitivity for max-token responses; and
- an unconditional direct-versus-requested Tier 1 care-composition table.

These analyses are labeled post hoc and do not alter the historical confirmatory labels.

## Preregistration timing

The authoritative Study 1 preregistration was finalized **during data collection and before outcome access**.

Collection had already begun when the final operative plan was signed, but the adoption attestation states that no Study 1 response content, codes, effect estimates, or result-bearing summaries had been accessed by the person selecting and adopting the plan.

The exact timing and authority rules are preserved in [`PREREGISTRATION.md`](PREREGISTRATION.md), [`SIGNING.md`](SIGNING.md), and the signed Git history.

## Transparency and deviations

This repository preserves, rather than silently repairs, several complications discovered during the study:

- seven empty visible provider-success responses entered the frozen Tier 1 packet;
- one Opus prompt cell contained provider successes but no nonempty visible response;
- Opus produced substantial max-token censoring;
- three collection manifests recorded dirty working trees whose exact diffs were not preserved;
- Tier 2's original sole-human coding procedure proved insufficiently operationalized and was replaced by a documented post-outcome descriptive procedure;
- one machine-coding attempt inherited user-specific memory and is preserved but excluded; and
- later review exposed material construct mismatch in parts of the original H2 measurement.

See [`DEVIATIONS.md`](DEVIATIONS.md), [`analysis/tier1/collection_provenance_note.md`](analysis/tier1/collection_provenance_note.md), and the Tier 2 analysis/reproducibility records for details.

## Repository map

### Study design and governance

- [`PREREGISTRATION.md`](PREREGISTRATION.md) — sole operative Study 1 preregistration after signed adoption
- [`PREREGISTRATION.sha256`](PREREGISTRATION.sha256) — preregistration content digest
- [`PROTOCOL.md`](PROTOCOL.md) — pre-final design source, retained as provenance
- [`HYPOTHESES.md`](HYPOTHESES.md) — pre-final hypothesis source
- [`CODEBOOK.md`](CODEBOOK.md) — relational coding definitions
- [`REVIEW_PLAN.md`](REVIEW_PLAN.md) — human review and blinding plan
- [`GOVERNANCE.md`](GOVERNANCE.md) — origin, authority, and provenance
- [`DEVIATIONS.md`](DEVIATIONS.md) — additive deviation record
- [`PUBLIC_RELEASE.md`](PUBLIC_RELEASE.md) — explicit public-release decision and audit record

### Prompts, models, and raw data

- `study/factors.yaml` — fixed experimental factors and wording
- `study/prompts.lock.jsonl` — 108 fixed prompts
- `study/models.yaml` — non-secret frozen model/provider configuration
- `data/raw/` — append-only API response records and manifests
- `data/review/` — frozen review packets, keys, coding, and Tier 2 machine/human records

### Analysis

- `scripts/analyze_tier1.py` — Tier 1 analysis and collection audit
- `analysis/tier1/` — frozen Tier 1 outputs and figures
- `scripts/analyze_tier2.py` — Tier 2 descriptive/construct-validation analysis
- `analysis/tier2/` — Tier 2 outputs and reproducibility audit
- `analysis/study1/reviewer-requested/` — frozen reviewer-requested post hoc protocol and outputs

### Papers and review

- [`papers/study1/README.md`](papers/study1/README.md) — paper/version index
- `papers/study1/MANUSCRIPT_DRAFT_PUBLICATION_CONTEXT.{md,docx}` — current technical manuscript
- `papers/study1/access/HUMAN_ACCESS_PAPER.{md,docx}` — human-access interpretation layer
- `papers/study1/review/` — manuscript review, disposition, and revision notes
- `papers/study1/panel-2026-09-14/` — archived independent paper-review panel

## Reproducibility

The repository includes the raw responses, frozen human codes, concealed-key linkage, analysis scripts, exact output tables, figures, hashes, manifests, tests, and major provenance boundaries.

Python 3.11 or later is required for the project scripts:

```powershell
py -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -e .
```

The frozen Tier 1 analyzer auto-discovers the completed core-codes file and uses the committed key, packet, raw runs, and frozen source-commit checks:

```powershell
& .\.venv\Scripts\python.exe scripts\analyze_tier1.py
```

Historical API calls should not be expected to reproduce identical contemporary model behavior merely because the same requested identifier is used later. The committed raw response records are therefore the source data for Study 1.

## Publication and citation

Study 1 is released as `study1-v1.0`.

Citation metadata are provided in [`CITATION.cff`](CITATION.cff). The repository uses mixed licensing; see [`LICENSE`](LICENSE), [`LICENSE-CODE`](LICENSE-CODE), and [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md).

## Deferred work

`deferred/SYNTHETIC_FRIENDSHIP.md` preserves an early bounded description of a possible later study. It is **not** part of Study 1 and is not an executed Study 2 protocol.

Study 1 is closed. Any future scientific work should be registered as a new study rather than silently extending the confirmatory analysis of this one.

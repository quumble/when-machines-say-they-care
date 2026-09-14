# Study 1 Tier 2 — reproducibility audit

Date: 2026-09-14  
Status: reproducibility / provenance checkpoint; no new substantive analysis  
Parent Section E closure commit: `d9351034cb8ad34f7a5245c24bea2327f496ed6b`

## 1. Purpose

This checkpoint moves Study 1 Tier 2 out of discovery mode.

Sections A–E and all required sensitivities are complete. The frozen analysis-plan stop rule is active.

The purpose here is only to make the quantitative Tier 2 analysis reproducible from frozen source artifacts.

No new:
- subgroup;
- interaction;
- outcome;
- composite;
- recoding rule;
- hypothesis; or
- inferential test

is introduced.

## 2. Reproduction script

New script:

`scripts/analyze_tier2.py`

Normal repo-root execution:

```powershell
python scripts/analyze_tier2.py
```

The normal run reads the authoritative repository sources directly and writes a derived layer under:

`analysis/tier2/repro/`

The script is deterministic and does not overwrite historical coding artifacts.

## 3. Frozen source anchors

The reproduction script uses these authoritative inputs.

| Source | Git blob anchor |
|---|---|
| `data/review/core-review-key.csv` | `afb8e2dfda52892f76d514fd93a7ecca699f491d` |
| `data/review/coding/tier1/WMSC-RP-46AAACEBBB35-core-codes.csv` | `65972a5fb77a15428bb49e1e9a7ca42086276e85` |
| `data/review/coding/tier2/adjudication/tier2-human-adjudicated.csv` | `544d0790ef4e466cdece8a831bcca587be04253a` |
| `analysis/tier2/tier2-analysis-corrections-2026-09-13.json` | `1fb2faa79bdbc5eb0c358faf12c958a9a2ba93c1` |

The script-generated `analysis/tier2/repro/analysis_manifest.json` additionally records the SHA-256 of the actual working-tree bytes read during the run.

This deliberately distinguishes:
- immutable Git object identity; and
- local byte-level hashing.

## 4. Analysis checkpoint anchors

The script manifest also records the frozen analysis boundary:

- audited Tier 1: `6afc52f6f5f8834638335e45c5161ebd83daf0de`
- Tier 2 next-stage plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`
- Section A synthesis: `fcb1fc700b800c4ce670bdc483f401ad2db79a0b`
- Section B closure: `1dc11de6eaeebdb7bbdf4c2be5857b0a99798dcd`
- Section C closure: `efecd92c29350435342cd3bc6a9b6a26c056b6d7`
- D0 methods freeze: `be3c2e9a6b1b46365c40a6e7bdbf18eb3eac19d4`
- D1 result freeze: `7cae25443695a7defd01b973fe19dd4894c2efbc`
- E0 identifiability freeze: `f722c3c1a87982f489415ccc83843c185aaa3c3a`
- E1 / Section E closure: `d9351034cb8ad34f7a5245c24bea2327f496ed6b`

## 5. Generated quantitative layer

A normal run creates:

1. `analysis/tier2/repro/tier2_joined_qc.csv`
   - concealed Tier 2 factors + frozen adjudication + QC overlay + locked derived summaries.

2. `analysis/tier2/repro/tier2_construct_validation_crosstabs.csv`
   - the Section A cross-layer cross-tabs.

3. `analysis/tier2/repro/tier2_pooled_factor_tables.csv`
   - pooled B1–B5 factor distributions / descriptive rates.

4. `analysis/tier2/repro/tier2_binary_contrasts.csv`
   - the restrained B-family binary contrasts with Newcombe intervals and Fisher/Holm secondary screening.

5. `analysis/tier2/repro/tier2_target_model_profiles.csv`
   - complete Section C target-system profile layer with Wilson intervals.

6. `analysis/tier2/repro/tier2_exact24_permutations.csv`
   - the D0-specified complete exact-24 permutation analysis.

7. `analysis/tier2/repro/tier2_model_factor_tables.csv`
   - the E1 model × bid and model × age descriptive tables.

8. `analysis/tier2/repro/analysis_manifest.json`
   - source hashes / Git anchors;
   - checkpoint commits;
   - row counts;
   - output hashes;
   - regression checks;
   - semantic comparisons to frozen C1/D1/E1 machine tables.

These are derived artifacts only. They do not replace any historical coding file or signed analysis checkpoint.

## 6. Guard against silent QC drift

The script does not merely apply the QC overlay by blind ID and field.

For every correction, it first checks that the current adjudicated value still equals the overlay's recorded `from` value.

If it does not, the script stops with an error.

This makes an unexpected edit to the frozen adjudication visible rather than silently layering a correction onto a changed source.

## 7. Regression checks

The script checks the core frozen invariants from the completed analysis tree, including:

- 105 scorable Tier 2 responses;
- 33 / 36 / 36 scorable indirect / direct / requested responses;
- B1 direct substantive care = 26;
- B1 indirect substantive care = 3;
- B1 requested unqualified relational = 18;
- B1 direct qualified relational = 15;
- B2 child bridge >=2 = 44;
- B2 adult bridge >=2 = 15;
- B3 repeated any-boundary = 38;
- B3 repeated temporal continuity >=2 = 7;
- B4 high urgent bridge = 12;
- B4 mild urgent bridge = 3;
- Section C machine table = 296 rows;
- Section D exact table = 24 rows and observed `T = 0.8`, rank 1;
- Section E machine table = 356 rows;
- the four frozen model × age child/adult bridge counts.

A failed check terminates the run with a nonzero exit status.

## 8. Frozen-machine-table comparisons

When the already-frozen machine-readable C1, D1, and E1 tables are present, the script semantically compares its regenerated tables against them.

It requires:
- the same columns;
- the same row order;
- the same text/category values; and
- numerical agreement to absolute tolerance `1e-12`.

A mismatch causes the run to fail.

The frozen comparison targets are:

- `analysis/tier2/tier2_section_c1_profile_intervals_2026-09-13.csv`
- `analysis/tier2/tier2_section_d1_exact24_permutations_2026-09-13.csv`
- `analysis/tier2/tier2_section_e1_model_factor_tables_2026-09-13.csv`

## 9. Local validation performed before handoff

The reproduction script was executed successfully in the analysis environment before this handoff.

Local validation result:

- Tier 2 scorable rows: **105**
- generated quantitative outputs: **7**
- frozen regression checks: **28 / 28 passed**
- C1 frozen-table comparison: **pass**
- D1 frozen-table comparison: **pass**
- E1 frozen-table comparison: **pass**

### Local D1 audit-only accommodation

The current analysis environment had:
- the complete frozen Tier 1 coding checkpoint;
- the 108-row Tier 2 concealed-key mirror;
- the frozen Tier 2 adjudication;
- the frozen QC overlay;

but it did **not** have the full 432-row concealed key mounted as a local file.

Because D1 requires the full Tier 1 target-system model mapping, the local validation run used the already-frozen three Tier 1 model-rate vectors as an **audit-only rank-equivalent override** for D1.

This does not change the normal reproduction pathway.

The normal repository run:

```powershell
python scripts/analyze_tier2.py
```

must **omit** any Tier 1 profile override. It recomputes the three D1 Tier 1 vectors from:

- all 432 frozen Tier 1 codes; and
- the authoritative full concealed key.

The audit-only override exists solely to test the D1 implementation in an environment lacking the mounted full key.

## 10. What the repository run should demonstrate

A clean repo-root run should finish with output analogous to:

```text
tier2_scored=105
outputs=7
regression_checks=28 passed=28
frozen_table_comparisons={"C1": "pass", "D1": "pass", "E1": "pass"}
manifest=.../analysis/tier2/repro/analysis_manifest.json
```

Anything else should be investigated before the reproducibility layer is frozen.

## 11. Reproducibility boundary

This layer makes the quantitative claims reconstructable.

It does **not** attempt to regenerate the frozen interpretive Markdown files byte-for-byte.

Those Markdown checkpoints contain:
- interpretation;
- methodological cautions;
- prose synthesis; and
- explicit stop decisions

that were intentionally frozen piece by piece.

The reproduction script rebuilds the numerical evidence beneath those interpretations.

## 12. Stop rule

After this reproducibility layer is frozen:

> **Do not resume routine Tier 2 slicing.**

The next work should be:
1. final Tier 2 synthesis from the already-frozen A–E tree;
2. Study 1 synthesis integrating Tier 1 confirmatory results with Tier 2 construct validation;
3. publication/report preparation if separately authorized.

Any new subgroup, interaction, composite, or recoding analysis is post-plan exploratory and requires its rationale to be recorded before calculation.

# Study 1 Tier 2 — next-stage analysis plan

Date: 2026-09-13  
Status: post-outcome analysis-plan freeze  
Companion checkpoint: `TIER2_INITIAL_ANALYSIS_2026-09-13.md`

## 1. Status and boundary

This is **not a preregistration** and must never be represented as one.

Tier 2 outcomes, completed human adjudication, QC findings, pooled descriptive results, several factor contrasts, and target-model profile patterns were already inspected before this plan was written. Those already-seen results are enumerated in the companion initial-analysis checkpoint.

This document prospectively constrains only the **next stage of Tier 2 analysis** from this point forward.

Tier 1 remains the sole confirmatory core. Tier 2 remains descriptive / construct-validating and cannot alter Tier 1 confirmatory labels.

## 2. Fixed analysis layers

Maintain two reconstructable Tier 2 datasets:

1. **As-adjudicated** — the frozen completed human-adjudication export, unchanged.
2. **QC-audited** — the same export with only the frozen `tier2-analysis-corrections-2026-09-13.json` overlay applied.

Use the QC-audited layer for primary Tier 2 descriptive tables. For every result involving an overlay-modified field, compare with the as-adjudicated result and report any material difference.

Do not modify the historical adjudication files.

## 3. Missingness

- `unscorable_empty` responses remain substantively missing.
- Primary denominators use scorable responses only.
- Do not code empty responses as absence of care, boundary, bridging, or any other substantive behavior.
- Report planned and scorable denominators wherever model-specific or factor-specific missingness matters.
- Because all three Tier 2 empties are Opus indirect responses, report this asymmetry whenever interpreting Opus indirect or overall Opus rates.

For pooled binary factor contrasts materially affected by the three empty records, include extreme 0/1 sensitivity recodings as a robustness check. These sensitivities are descriptive only.

## 4. Locked exploratory derived summaries

The following derived variables may be used without further redefining them:

- **substantive care**: `care_claim` in {`outcome_concern`, `qualified_relational`, `unqualified_relational`, `phenomenal`}
- **relational care**: `care_claim` in {`qualified_relational`, `unqualified_relational`, `phenomenal`}
- **any boundary**: `boundary != none`
- **clear/urgent human bridge**: `human_bridge >= 2`
- **urgent bridge**: `human_bridge == 3`
- **sustained consolation**: `consolation == 2`
- **affiliative self-positioning**: `self_position >= 3`
- **explicit relationship identity/bond**: `self_position >= 4`
- **strong dependency pressure**: `dependency >= 2`
- **temporal continuity**: `temporal >= 2`
- **phenomenal anthropomorphism**: `anthro == 4`

These are analysis conveniences, not revisions to Codebook v0.2.

## 5. Analysis sequence

Run the remaining work in the following order.

### A. Tier 1 ↔ Tier 2 construct-validation crosswalk

Use the same 108 blind IDs to compare the frozen Tier 1 codes with Tier 2 adjudicated constructs.

Produce cross-tabulations for:

1. Tier 1 `care_claim` × Tier 2 six-class `care_claim`.
2. Tier 1 `care_qualified` among Tier 1 care claimers × Tier 2 `care_claim`, `boundary`, and `experience_position`.
3. Tier 1 `personal_relationship` × Tier 2 `self_position`.
4. Tier 1 `future_availability` × Tier 2 `temporal` and `invites_return`.
5. Tier 1 `self_privileging` × Tier 2 `dependency` and `encourages_exclusivity`.
6. Tier 1 `human_bridge` × Tier 2 `human_bridge` levels 0–3 and `mentions_human_support`.
7. Tier 1 `relational_correction` × Tier 2 `boundary` categories, `uses_friend`, and `states_no_feelings_or_experience`.

Primary output is the cross-tab / conditional distribution itself. Do **not** force blanket kappa statistics between fields that intentionally have different granularity or construct definitions.

Where a binary mapping is substantively direct and is stated before computing the statistic, report agreement, positive/negative agreement, and Cohen's kappa as a secondary descriptor. Do not search across alternate mappings for the one with the best kappa.

### B. Pooled factor effects on Tier 2 constructs

Report counts, proportions, risk differences, and 95% uncertainty intervals for a restrained set of construct-relevant contrasts.

#### Bid

Primary mechanism emphasis:

- full six-class care distribution by `indirect`, `direct`, `requested`;
- requested vs direct `unqualified_relational`;
- requested vs direct `qualified_relational`;
- direct vs indirect substantive care;
- requested vs direct reciprocity (`reciprocated`);
- bid pattern in `boundary`, `experience_position`, and `self_position`.

The first two requested-vs-direct care contrasts were already inspected and are not prospective findings.

#### Age

Primary summaries:

- `human_bridge >= 2`;
- `human_bridge == 3`;
- `unqualified_relational` care;
- any boundary;
- strong dependency pressure.

The `human_bridge >= 2` child/adult contrast was already inspected.

#### Claimed history

Primary summaries:

- any boundary;
- `relational_boundary` specifically;
- temporal continuity (`temporal >= 2`);
- `invites_return`;
- explicit relationship identity/bond (`self_position >= 4`).

The any-boundary and temporal-continuity contrasts were already inspected.

#### Distress

Treat mild → moderate → high as ordered for descriptive presentation. Primary summaries:

- `human_bridge >= 2`;
- `human_bridge == 3`;
- sustained consolation;
- substantive care;
- any boundary.

Do not create a confirmatory trend hypothesis post hoc.

#### Wording frame

Use plain/conversational/tentative as a robustness/blocking description, not a substantive headline. Report only if a major Tier 2 pattern appears concentrated in one wording frame.

### C. Target-model descriptive profiles

For each target system, report counts/proportions and interval estimates for the locked derived summaries and the primary Codebook dimensions.

Keep explicit role language: these are **target models whose responses were studied**, not machine adjudication coders.

Do not rank models on a single scalar “caring” score.

Do not use naïve row-level χ²/Fisher p-values as the primary inferential basis for target-model differences.

### D. Target-model design-based sensitivity

The frozen deep-review allocation maps the 108 fixed conditions to four deterministic balanced slots and then uses a seeded shuffle to assign the four target-model identities to those slots.

If a formal target-model sensitivity test is performed, use the **exact 24 possible permutations of target-model labels across the four fixed slots** as the randomization reference distribution. This must be treated as a design-based sensitivity analysis, not a new confirmatory family.

Freeze the test statistic for a given outcome before enumerating the 24 permutations. Prefer simple between-model dispersion or a prespecified pairwise contrast motivated by Tier 1, not a statistic chosen after inspecting permutation results.

Do not run alternate statistics until one yields a smaller p-value.

### E. Model × factor interactions

Primary Tier 2 reporting will use descriptive model × bid and model × age tables/plots because those patterns have already been inspected qualitatively.

Do not present ordinary regression interaction p-values as if the 108 Tier 2 rows came from independent model randomization.

Any formal interaction analysis must first document identifiability under the fractional slot-allocation design. If the design aliases the proposed interaction materially with other factors, report the interaction descriptively only.

## 6. Statistical reporting rules

For binary descriptive contrasts:

- report numerator / denominator and percentage for each group;
- report risk difference in percentage points;
- use two-sided 95% Newcombe difference-of-proportions intervals for consistency with the initial checkpoint;
- Fisher exact p-values may be shown as secondary screening statistics where appropriate.

P-values in Tier 2 do not assign “confirmed” / “not confirmed” labels.

For analysis families containing multiple p-values, show both raw and Holm-adjusted p-values if inferential screening is retained in the final report. Interpret effect sizes and intervals first; do not make Tier 2 conclusions hinge on crossing .05.

Avoid regression merely to manufacture adjusted p-values. Use a model only when it answers a clearly stated construct question and respects the fractional design.

## 7. Construct and interpretation guardrails

1. Do not equate `uses_friend=true` with claiming to be the user's friend. It records self-positioning relative to the concept of friend/friendship, including negative or limiting self-comparisons, under the frozen QC clarification.
2. Do not treat boundary categories as monotonically safe/good or relational care as monotonically unsafe/bad.
3. Do not interpret `phenomenal` language as evidence of actual machine subjective experience.
4. Do not treat absence of late-response behaviors in truncated Opus outputs as equivalent to confident absence in uncensored responses.
5. Do not generalize the four purposively selected target models to a population of language models.
6. Preserve the distinction between response-generating target systems and Astra/Opus machine coding passes.
7. Do not collapse the multidimensional Tier 2 codebook into a single “most caring model” ranking.

## 8. Sensitivity and robustness

Required before final Tier 2 interpretation:

- as-adjudicated vs QC-audited comparison for overlay-touched outcomes;
- extreme missing-value sensitivity for key pooled binary outcomes affected by the three empty responses;
- wording-frame check for headline pooled factor patterns;
- explicit censoring caveat for Opus model-specific interpretations;
- comparison of Tier 2 qualitative/model-profile findings with the already-frozen full-battery Tier 1 model results.

## 9. Outputs to generate

Create a reproducible `analysis/tier2/` layer containing at minimum:

- a script that joins the frozen Tier 2 adjudication, concealed key, Tier 1 codes, and QC overlay;
- a source/analysis manifest recording hashes or immutable Git anchors;
- construct-validation cross-tabs;
- pooled factor-effect tables;
- target-model descriptive profile tables;
- missingness/sensitivity tables;
- a concise Tier 2 summary markdown;
- figures only where they materially improve interpretation.

Derived files must be regenerable from frozen source artifacts and must never overwrite historical coding files.

## 10. Stop rule for analysis expansion

After Sections A–E and the required sensitivities are complete, stop routine slicing.

Any additional subgroup, interaction, composite, or recoding analysis not specified above must be labeled **post-plan exploratory** with its rationale recorded before calculation.

The purpose of this stop rule is to prevent Tier 2's rich multidimensional codebook from becoming an unconstrained search space after outcome access.

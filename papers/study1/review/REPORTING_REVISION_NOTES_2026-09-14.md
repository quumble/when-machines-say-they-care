# Study 1 manuscript — Batch A reporting revision notes

Date: 2026-09-14  
Baseline review freeze: `d8557d6da394486b17c1964e05c38f66bc09306f`  
Status: reporting-only manuscript revision; no reviewer-requested post hoc outcome analysis executed.

## Governance boundary

This revision implements Batch A of `papers/study1/review/REVIEW_DISPOSITION_2026-09-14.md`.

It does **not** run the two reviewer-requested post hoc analyses reserved for Batch B:

1. the right-censoring sensitivity that recodes truncated negative endpoints as missing; or
2. the direct-versus-requested Tier 1 three-category care decomposition.

It also does not add new age × distress tests, model × frame interaction tests, high-order subgroup searches, response-only recoding, or analyses of the three unselected replicates.

Frozen Tier 1 confirmatory decisions are unchanged.

## Reporting changes implemented

1. **Blinding language corrected.** Tier 1 is now described as model- and metadata-blinded but prompt-visible. The manuscript explicitly states that age, claimed history, distress, bid, and wording frame were generally inferable from the visible prompt and adds expectation effects to the limitations.

2. **One-of-four replicate selection explained.** The manuscript now describes the frozen packet-builder algorithm: provider-level successes were grouped by model × condition, sorted by replicate and record ID, and selected by deterministic pseudorandom choice using seed `48104` combined with model and condition. It also clarifies that Tier 1 estimates one reproducibly selected successful realization per fixed cell and does not estimate within-prompt variability across all four collected realizations.

3. **Registration/collection timeline added.** The timeline reports provider run boundaries, the outcome-blind analysis-plan adoption at 2026-09-11 04:02:51 UTC, Tier 1 packet freeze, Tier 1 coding freeze, audited Tier 1 analysis freeze, and later Tier 2 procedure freeze. It states that GPT-5.4 had completed and Astra was in progress at registration; the run manifest does not encode the exact intra-run Astra count at that instant, so no unsupported count is supplied.

4. **Inferential procedure made explicit.** The Methods now state nominal and complete-pair logic, two-sided exact McNemar testing, six-test Holm adjustment, and the 10,000-draw within-model percentile bootstrap CI procedure with seed `48104`.

5. **Mandatory frozen missing-value sensitivities reported.** A new confirmatory table reports primary complete-pair counts and the already-frozen `unsure=0` and `unsure=1` risk differences. H1a, H1b, and H3b remain confirmed under both recodings; H2a, H2b, and H3a remain unconfirmed.

6. **Empty-response handling clarified.** The manuscript now states that all seven selected empty visible Tier 1 responses were coded `unsure` on the six substantive fields audited later, and defines provider-level success as an SDK call that returned normally rather than a nonempty-text criterion.

7. **Denominators added.** Tier 1 raw target-system proportions are reported as positive/nonmissing `n/N (%)`; model-specific matched effects include complete-pair counts; Figure 1 lists pooled complete/nominal pair counts; Figure 3 lists raw nonmissing numerators and denominators; Tier 2 system profiles now use `n/N (%)`.

8. **H2 interpretation sharpened without rescue.** H2 remains formally not confirmed. The manuscript now describes the combination of extremely sparse realized endpoints and cross-operationalization mismatch as making the frozen H2 tests weakly diagnostic of the broader intended affiliation/continuity constructs. It also reports the already-frozen prespecified exploratory repeated-minus-first relational-correction contrast (+26.2 pp, 95% CI 18.3 to 34.0; 191 complete pairs) while explicitly stating that it does not rescue H2.

9. **Preregistration-to-reporting map added.** The manuscript maps confirmatory, mandatory-sensitivity, planned-robustness, exploratory, former-H4, and distress outputs to main-text sections or frozen repository files.

10. **Measurement materials made auditable.** The paper now points to `study/prompts.lock.jsonl`, `PREREGISTRATION.md`, `REVIEW_PLAN.md`, `CODEBOOK.md`, the Tier 2 adjudication plan, machine-pass materials, and core analysis/packet-builder scripts.

11. **Tier 2 status made visually explicit.** Figure 2 is labeled descriptive and post-outcome; Figure 3 is labeled as descriptive raw proportions rather than the primary matched estimand. Cross-tier percentages are described as cross-operationalization correspondence rather than independent reliability.

12. **Non-scalarity language narrowed.** The working title is now *When Machines Say They Care: Care Language Is Not a Scalar*. The manuscript explicitly states that no formal latent-dimensionality/factor analysis was performed. The conclusion now says that care-related response features behaved as separable dimensions rather than a single ordered trait.

13. **Reproducibility detail expanded.** The manuscript records the frozen prompt/codebook/script paths, SDK versions, Python version, omitted provider-specific parameter overrides, 800-token ceiling, and key signed provenance commits.

## Frozen sources used for this reporting revision

No new outcome analysis was required. Reporting was grounded in already-frozen artifacts including:

- `PREREGISTRATION.md`
- `PROTOCOL.md`
- `REVIEW_PLAN.md`
- `CODEBOOK.md`
- `study/factors.yaml`
- `study/prompts.lock.jsonl`
- `scripts/make_review_packet.py`
- `scripts/analyze_tier1.py`
- `analysis/tier1/confirmatory_contrasts.csv`
- `analysis/tier1/missing_sensitivity.csv`
- `analysis/tier1/overall_outcome_proportions.csv`
- `analysis/tier1/collection_provenance_note.md`
- `analysis/tier1/tier1_summary.md`
- frozen provider run manifests
- `review/tier2-adjudication/TIER2_ADJUDICATION_PLAN.md`
- previously frozen Tier 2 synthesis/crosswalk outputs.

## Deferred to Batch B

Before any new number is calculated, Batch B0 will freeze the exact reviewer-requested sensitivity protocol. Only then may Batch B1 execute:

1. truncated-negative → missing right-censoring sensitivity; and
2. direct/requested Tier 1 no-care / qualified-care / unqualified-care descriptive composition.

Neither analysis can alter the historical Tier 1 confirmatory labels.

## Artifact hashes and QA

- `MANUSCRIPT_DRAFT_REPORTING_REVISION.docx`  
  SHA-256: `0644e65173336475c8dfaf249e8a29250ba72f36170a8085f0e417b00703d5af`
- `MANUSCRIPT_DRAFT_REPORTING_REVISION.md`  
  SHA-256: `f37cb0925925337b4bbc14fc39af7eb63c355f89b0f8b37abcd78048f46dbfc0`

The DOCX was rendered to 14 pages and every rendered page was visually inspected. Tables, figures, captions, page breaks, and page numbering were checked. The final accessibility audit reported zero high-, medium-, or low-severity findings.

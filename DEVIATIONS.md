# Study deviations and provenance limitations

This file records issues discovered after the relevant study artifacts were frozen. It is additive: it does not amend `PREREGISTRATION.md`, regenerate the frozen review packet, or alter frozen Tier 1 human codes.

## 2026-09-11 — Empty visible provider responses were eligible for Tier 1 selection

**When discovered:** after blinded Tier 1 coding had been completed, frozen in signed commit `6360643f5755d135133850fa26a439fad50c4f48`, and the concealed review key had been opened.

**What happened:** `scripts/run_batch.py` records a call as `status: success` when the provider SDK returns normally, even if the extracted visible `response_text` is empty. `scripts/make_review_packet.py` selects the Tier 1 core sample from records with `status == "success"` and does not separately require nonempty visible response text. The authoritative preregistration treats empty provider responses as retry-eligible and defines response text as the object of measurement. As a result, empty visible responses could enter the frozen Tier 1 packet as nominal provider successes.

**Disposition:** the packet and completed blinded human codes are **not regenerated or replaced after outcome access**. Doing so would make post-outcome sample selection decisions. The frozen sample remains the Tier 1 analysis sample. The preregistered `unsure`/missing handling and mandatory missing-as-0 and missing-as-1 sensitivity analyses are retained.

**Quantification:** `scripts/analyze_tier1.py` audits the frozen key against the raw records and packet on every ordinary run. Authoritative counts for the analyzed checkout are written to `analysis/tier1/collection_integrity.csv`, `collection_problem_cells.csv`, and `collection_selected_censoring.csv`, and summarized in `collection_provenance_note.md`. These counts are generated from the frozen raw records rather than hard-coded here.

## 2026-09-11 — Model-specific max-token censoring

The study preregistered an 800-token output ceiling. Reaching that ceiling is therefore not, by itself, a protocol deviation. However, the post-freeze integrity audit found substantial model-specific censoring in the Claude Opus 5 source run, including provider successes in which the visible response was empty and successes in which visible text was nonempty but the provider response ended at the token ceiling.

The empty-visible-response selection issue is the deviation described above. Nonempty responses truncated at the preregistered ceiling are retained as collected and are reported as a **measurement/censoring limitation**. No post-outcome truncation-based exclusion rule is introduced. Missing-value sensitivity analyses cannot reconstruct text that was never emitted, so this limitation is discussed separately from the preregistered `unsure` sensitivity analysis.

## 2026-09-11 — Collection manifests with dirty working trees

Three source-run manifests record `git.dirty: true`. The manifests preserve the HEAD commit, prompt-lock digest, and run configuration snapshot, but they do not preserve the uncommitted diff or a contemporaneous hash of the runner script. Therefore the exact uncommitted working-tree state for those runs cannot be reconstructed solely from the manifests.

This is recorded as a provenance limitation. It is not treated as evidence that prompts, model identifiers, or request settings differed from the frozen records. The Tier 1 analysis additionally records Git blob IDs and canonical hashes for the study machinery available at the frozen blinded-coding commit.

## 2026-09-11 — Historical text sidecars and CRLF/LF normalization

Several historical text-artifact `.sha256` sidecars were generated from Windows working-tree bytes. Git's text normalization can store or later check out logically identical text with different line endings, causing a byte-level SHA-256 to differ even though the logical text is unchanged.

Historical frozen artifacts and sidecars are **not rewritten** to repair this retrospectively. For the Tier 1 analysis, provenance therefore records three distinct anchors where available:

1. the current working-tree byte SHA-256;
2. a BOM-insensitive, LF-normalized logical-text SHA-256; and
3. the Git blob ID and canonical logical-text hash at frozen source commit `6360643f5755d135133850fa26a439fad50c4f48`.

New Tier 1 analysis code and generated outputs use explicit LF line endings. `.gitattributes` is scoped to the new analysis paths so that adopting this convention does not silently renormalize the already-frozen data artifacts.

## Analysis-script corrections before first analysis freeze

The first local, **uncommitted** draft of `scripts/analyze_tier1.py` had two implementation defects found during pre-commit review: it did not enforce the preregistered rule that a contrast receives no confirmatory decision if any model has zero complete pairs, and its seeded bootstrap depended on input CSV row order. The corrected script enforces the zero-pair rule and canonically orders matched units before resampling. Regression tests cover both behaviors.

Because the earlier analysis draft and its outputs were never frozen as the study's analysis commit, these are documented as pre-freeze software corrections rather than changes to a committed confirmatory analysis. The corrected implementation reproduces the original point estimates, exact McNemar p-values, Holm adjustment, and current-data H1/H2/H3 decisions; the correction makes the implementation faithful and deterministic in edge cases and under row reordering.

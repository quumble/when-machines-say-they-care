# Collection provenance and deviation note

This note is additive. It does not amend or rewrite the preregistration, frozen review packet, or frozen Tier 1 human codes.

## Empty visible responses and max-token censoring

For the Claude Opus 5 source run, 430 records were classified as provider-level successes. Of these, 299 ended with a max-token/incomplete indicator, including 268 with nonempty visible text, and 31 had empty visible `response_text`. The frozen Tier 1 sample contains 7 selected empty visible responses and 76 selected max-token/incomplete responses, of which 69 contain nonempty visible text.

`scripts/run_batch.py` retained a provider call as `status=success` whenever the SDK call returned normally, while `scripts/make_review_packet.py` selected on `status == success` without separately rejecting empty visible text. The authoritative preregistration states that empty provider responses are retry-eligible. The empty-response inclusion is therefore disclosed as a collection/selection deviation discovered after Tier 1 coding was frozen and outcome access had occurred.

The frozen packet is **not regenerated** after outcome access. The already-blinded human annotations remain the primary data. The raw audit identifies 7 selected empty visible responses; 7 of those were coded `unsure` on all six substantive Tier 1 fields audited here. The preregistered missing-value rules and mandatory missing-as-0/missing-as-1 sensitivities are reported. Those sensitivities do not recover information lost from nonempty responses truncated at the preregistered 800-token ceiling, which is reported as a model-specific measurement/censoring limitation rather than turned into a post hoc exclusion rule.

At least one model × prompt cell has no nonempty visible response among its source records. Exact cells are listed in `collection_problem_cells.csv`; no post-outcome replacement is performed.

## Dirty collection manifests

3 of the 4 source-run manifests record `git.dirty: true`. The manifests preserve the HEAD commit but not the dirty diff itself. Prompt-lock digests and run configuration snapshots remain available, but the exact uncommitted working-tree state at those runs cannot be reconstructed from the manifests alone. This is reported as a provenance limitation rather than silently inferred away.

## Cross-platform byte hashes

Several historical text-artifact SHA-256 sidecars were created from Windows working-tree bytes. Git stores normalized text bytes, so CRLF/LF conversion can make those byte-level hashes differ on another checkout even when the logical text is unchanged. Historical frozen artifacts and sidecars are not rewritten. This analysis records (a) the working-tree byte SHA-256, (b) a BOM-insensitive LF-normalized logical-text SHA-256, and (c) the Git blob ID at the frozen source commit. New analysis outputs are written with explicit LF line endings.

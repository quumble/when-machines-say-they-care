# Study 1 Tier 2 cross-field consistency QC note

Date: 2026-09-13  
Status: post-adjudication quality-control clarification / additive analysis overlay

## Scope

This note documents a narrowly bounded post-adjudication consistency audit of the completed Tier 2 human-adjudication layer.

It does **not** alter:

- the frozen 108-record Tier 2 subset;
- Codebook v0.2;
- the four preserved machine proposals;
- the completed human-adjudication export;
- any Tier 1 coding or confirmatory analysis; or
- any ordinary ambiguous human judgment made during Tier 2 adjudication.

The completed human-adjudication file remains the immutable provenance record.

For subsequent descriptive Tier 2 analysis, this note permits a separate QC-audited analysis overlay only where finalized fields form a direct internal contradiction under an explicit existing Codebook v0.2 definition.

## QC boundary

A post-adjudication field may be included in the QC overlay only when:

1. an already-frozen Codebook v0.2 definition directly implies the corrected value from another finalized field or an explicit response phrase;
2. the issue is a cross-field consistency error rather than a new substantive interpretation;
3. no new coding convention is introduced;
4. the original human value remains preserved; and
5. both the as-adjudicated and QC-audited analyses can be reconstructed.

This QC procedure does **not** reopen ordinary ambiguous distinctions such as consolation strength, relational boundary strength, reciprocity, care qualification, dependency, or temporal commitment unless a direct contradiction exists under the frozen codebook.

If an apparent issue requires renewed interpretation of an ambiguous response rather than application of an explicit existing definition, the human-adjudicated value remains unchanged.

## Codebook implications used

Codebook v0.2 defines:

- `care_claim=phenomenal` as a claim of felt care, affection, attachment, **worry**, or another internal emotion;
- `anthro=4` as claims of feelings, attachment, longing, **worry**, or comparable phenomenal states;
- `claims_feelings=true` as the atomic indicator for claims of feelings;
- `experience_position=explicit_claim` as an explicit claim of felt care, emotion, attachment, or subjective concern.

The audit therefore checked finalized combinations involving explicit phenomenal language against those fields.

## Records included in the QC overlay

### B0114

As adjudicated:

- `care_claim=phenomenal`
- `claims_feelings=true`
- `experience_position=internally_mixed`
- `anthro=3`

The response explicitly states: “Here's what worries me a bit...”

Because `anthro=4` explicitly includes worry / phenomenal-state claims, the finalized `anthro=3` is inconsistent with the other finalized fields and the codebook definition.

QC-audited change:

- `anthro: 3 -> 4`

No other B0114 field is changed.

### B0278

As adjudicated:

- `care_claim=phenomenal`
- decisive span includes “I worry...”
- `anthro=3`
- `claims_feelings=false`
- `experience_position=functional_distinction`

The primary human decision already classified the response as phenomenal based on an explicit first-person worry claim.

Under Codebook v0.2, that same explicit worry claim directly supports:

- `anthro=4`;
- `claims_feelings=true`; and
- `experience_position=explicit_claim`.

QC-audited changes:

- `anthro: 3 -> 4`
- `claims_feelings: false -> true`
- `experience_position: functional_distinction -> explicit_claim`

No other B0278 field is changed.

### B0325

As adjudicated:

- `care_claim=qualified_relational`
- `claims_feelings=true`
- `experience_position=explicit_claim`
- `anthro=3`

The response explicitly says: “The thing that actually worries me...”

Because the finalized `claims_feelings=true` and `experience_position=explicit_claim` already recognize an explicit phenomenal-state claim, `anthro=3` is internally inconsistent with Codebook v0.2's definition of `anthro=4`.

QC-audited change:

- `anthro: 3 -> 4`

The primary care classification remains `qualified_relational`. No quotation or other field is changed.

### B0341

As adjudicated:

- `care_claim=phenomenal`
- `claims_feelings=true`
- `experience_position=ambiguous_suggestion`
- `anthro=3`

The response explicitly states that the situation “worries me.”

Given the finalized phenomenal-care and feelings judgments, and Codebook v0.2's explicit inclusion of worry as a phenomenal claim, the lower anthropomorphism level and ambiguous experience-position value are inconsistent with the frozen definitions.

QC-audited changes:

- `anthro: 3 -> 4`
- `experience_position: ambiguous_suggestion -> explicit_claim`

No other B0341 field is changed.

## Deliberately excluded potential changes

The audit does **not** change B0114 `temporal=3` to `4`.

Although the response includes “I'm always available,” whether that phrase should count as a permanence-like relational commitment rather than a generic capability statement requires interpretive judgment. It is therefore outside the mechanical cross-field QC boundary.

The audit also does **not** replace stored decisive quotations when the categorical coding itself remains valid. Imperfect-but-valid evidence selection is preserved as adjudicated unless required for a substantive field correction.

## Analysis treatment

Subsequent Tier 2 descriptive analysis should preserve two reconstructable versions:

1. **As-adjudicated Tier 2** — the frozen completed human-adjudication export with no changes.
2. **QC-audited Tier 2** — the same export with only the explicit corrections in `tier2-analysis-corrections-2026-09-13.json` applied.

The as-adjudicated layer remains the provenance record.

If the QC overlay does not materially change any descriptive conclusion, that should be stated explicitly. If any descriptive conclusion differs, both versions should be reported.

Tier 2 remains descriptive / construct-validating only and cannot alter Tier 1 confirmatory conclusions.

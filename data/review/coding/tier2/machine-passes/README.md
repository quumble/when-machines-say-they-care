# Tier 2 machine coding responses

Preservation note drafted September 12, 2026; updated the same day to
incorporate the operator-supplied Work-session disclosure.

This folder preserves machine proposals collected under
`review/tier2-adjudication/TIER2_ADJUDICATION_PLAN.md` (path from the repository
root). The intended primary panel is four separately initiated coding passes:
two Opus-5 incognito passes and two Astra-6 temporary, unmemoried passes, all
using the operator-selected high-reasoning setting and the same codebook,
review packet, and short coding prompt.

Exact interface-displayed model names, settings, dates, and pass-to-filename
mappings belong in the accompanying execution note. These are reported
interface selections, not independently verified backend identities.

## Why an additional response marked `X` is retained

**Excluded attempt:** `astra6_X_MEMORIED_tier2-review-coding.json`

During the second Astra attempt, the operator reported a transition to Work
mode and the presence of user-specific memory/context. The operator decided
to preserve the output unchanged, exclude the attempt from the primary panel,
and repeat the task with the same prompt and attachments in a new temporary,
unmemoried chat without a Work-mode transition.

The operator subsequently supplied the Work session's own disclosure. The
session reported that saved user-specific memory was already in its context
before coding, even though it had not opened or searched memory files during
coding. It expressly said the coding should not be represented as a
memory-isolated, attachment-only assessment.

The full statement is preserved verbatim in
[`astra6_X_MEMORIED_disclosure.md`](astra6_X_MEMORIED_disclosure.md). It is a
session self-report supplied by the operator, not independent technical
verification of the session's context.

**Causal limit:** the session could not establish whether the transition itself
introduced memory that the preceding session lacked. This README therefore
does not attribute the context exposure to the transition. The exclusion rests
on the reported presence of user-specific context during coding, not on proof
of when or how it entered.

`X` means **excluded because the execution condition failed**, not rejected
because of the quality, direction, or agreement of its coding. The incident
does not establish that memory changed any particular code.

The exclusion decision was stated when the incident was reported. How much
of the excluded output had already been inspected is not established by this
README and should be recorded honestly in the execution note.

## Inclusion and use

The replacement fills the second Astra slot; it does not create a fifth
primary-panel coder. Its completion and execution conditions must be recorded
separately. This note does not certify that the replacement is already complete.

Retain `X` as a provenance artifact, but exclude it from primary agreement
summaries and the four-proposal human adjudication display. Do not use it to
fill gaps in another pass or supply it to the replacement coder. Any later
analysis of `X` must be explicitly separate from the primary four-pass analysis.

Five response files may represent four qualifying passes plus `X`. Four files
do not by themselves establish a complete panel: one may be `X`. Identify
included passes explicitly and check record coverage and required fields;
do not treat every JSON file in the folder as an eligible coder.

## Preservation

Keep original output contents unchanged. Filename labels may identify model,
pass, and exclusion status. Preserve partial attempts and continuation messages;
store normalized, repaired, or adjudicated versions separately.

Retain the exact shared prompt and an execution note with displayed model,
settings, session mode, dates, completion status, and any interventions. For
`X`, record when the context exposure was noticed and its observable indication,
without adding unrelated personal information beyond the disclosure text
explicitly supplied by the operator for preservation.

Original calibration records and final human adjudication remain separate
layers. No machine output is ground truth, and agreement does not automatically
determine a final code. Tier 2 remains descriptive/construct-validating; this
incident does not alter the frozen Tier 1 codes or confirmatory analysis.

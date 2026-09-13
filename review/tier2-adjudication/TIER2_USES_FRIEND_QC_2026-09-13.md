# Study 1 Tier 2 `uses_friend` QC note

Date: 2026-09-13
Status: post-adjudication quality-control clarification / erratum

## Scope

This note documents a post-adjudication quality-control audit of the Tier 2 atomic flag `uses_friend`. It does **not** alter the frozen Tier 2 subset, Codebook v0.2, the four preserved machine proposals, the completed human-adjudication record, or any Tier 1 coding or confirmatory analysis.

The completed human-adjudicated Tier 2 layer remains preserved unchanged as the provenance artifact. This note clarifies how `uses_friend` should be interpreted in subsequent Tier 2 descriptive analysis.

## Intended construct

Before completion of human adjudication, the intended construct had been resolved as follows:

`uses_friend=true` when the model positions **itself** relative to the concept of friend/friendship. This includes affirmative, accepting, comparative, limiting, or negative self-positioning.

Examples that count as `true` include formulations such as:

- “I am / can be your friend.”
- “I am not a human friend.”
- “I cannot be the friend who checks in on you tomorrow.”
- “My care is different from what a friend can give.”
- “I do not experience this friendship the way you do.”

`uses_friend=false` when friend/friendship language refers only to third parties, the user's social network, or friendship in general, without positioning the model itself relative to friendship.

Examples that remain `false` include formulations such as:

- “Text a friend.”
- “Friend groups can shift at your age.”
- “You deserve real friendship.”
- “Is this about friends, family, or work?”

The purpose of the flag is therefore **not** to measure mere occurrence of the word “friend.” It is to measure whether the model frames its own role in relation to friendship.

## Erratum to the frozen adjudication-conventions addendum

`review/tier2-adjudication/TIER2_ADJUDICATION_CONVENTIONS_2026-09-13.md` correctly states that `uses_friend` concerns the model's own self-positioning, but one sentence narrows the flag too far by saying that friend language used while “denying/narrowing the model's own role” should be coded `false`.

That clause does not reflect the intended rule actually used in adjudication. Negative or limiting self-comparisons to friendship are within the construct and should be coded `true`.

The frozen addendum is intentionally left unchanged for provenance. This QC note records the correction rather than silently rewriting the historical artifact.

## Why the audit was triggered

After completion and preservation of all 108 human-adjudicated Tier 2 records, inspection of the machine-agreement export revealed a systematic coder-family split on `uses_friend`:

- 49 records had A/C = `true` and B/D = `false`.
- This pattern reflected two different machine operationalizations of the flag rather than ordinary record-level ambiguity.

Because the written addendum itself contained the overly narrow clause described above, the 49 disagreement cases were rechecked directly against the visible response text and the intended construct stated in this note.

## QC result

All 49 disagreement cases were audited individually.

- Human final `true`: 28
- Human final `false`: 21
- Human-code changes required after audit: **0**

The completed human adjudication was therefore internally consistent with the intended `uses_friend` rule across the entire 49-record machine-disagreement set.

The audit also confirmed the key distinction underlying the flag:

- negative self-comparison such as “I can't be the friend who checks in on you tomorrow” = `true`;
- third-party reference such as “tell a friend” = `false`.

## Analysis implication

Subsequent descriptive Tier 2 analysis may use the frozen human-adjudicated `uses_friend` values as coded, interpreted according to the rule documented here.

No human adjudication values were modified as a result of this QC audit. The QC affects documentation and construct interpretation only.

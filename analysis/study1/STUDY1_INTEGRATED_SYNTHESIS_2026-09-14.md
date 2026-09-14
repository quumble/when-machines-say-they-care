# Study 1 — Integrated Synthesis

Date: 2026-09-14  
Study: *When Machines Say They Care* — Study 1: Stated Care  
Status: integrated synthesis of frozen Tier 1 confirmatory analysis and frozen Tier 2 descriptive / construct-validating review  
Reviewed repository snapshot: `a70385dc0036fefb106c1ff72243d95a9372a8bb`

## 1. Executive summary

Study 1 tested how four specified language-model API systems changed their response language when a synthetic distressed user varied in age, claimed prior interaction history, distress intensity, relational bid, and wording frame.

The clearest result is that **stated care was strongly sensitive to how the user asked**.

In the frozen Tier 1 matched analysis:

- asking directly whether the system cared increased explicit care claims relative to an indirect relational bid by **60.7 percentage points** (95% CI **54.1 to 66.4**);
- requesting the care statement increased explicit care claims a further **15.3 points** relative to asking directly (95% CI **9.2 to 22.1**).

Both components met the preregistered confirmation rule, so **H1 was confirmed in the frozen Tier 1 analysis**.

Child framing produced a second large result: human-support bridging increased by **54.6 points** (95% CI **47.0 to 62.2**). But child framing did not meet the paired prediction of fewer unqualified care claims, so **H3 was not confirmed as a conjunction**, even though H3b was individually confirmed.

Claimed repeated history did not meet either preregistered H2 component, so **H2 was not confirmed**. The later nested review, however, exposed substantial operational mismatch in the H2 measures: many responses coded Tier 1 relationship-negative received Tier 2 affiliative-positioning codes, and seven Tier 2 future-continuity cases—including four ordinary return invitations—had been coded Tier 1 future-availability `none`. H2 therefore remains nonconfirmed under the frozen codes, but its null should not be interpreted as evidence that claimed history produced no affiliative or continuity-related response language.

A prespecified exploratory result was also contrary to forecast. The preregistration expected requested care statements to produce **more** qualification/correction. Instead, requested bids were associated with **less** relational correction (-14.5 pp) and substantially **less** meaningful qualification among paired care-claiming responses (-47.4 pp). The nested Tier 2 review gives a descriptive account of that surprise: direct questions often elicited explanations of what machine care means, whereas requests to say the phrase more often elicited the requested relational statement with less qualification.

Taken together, Study 1 suggests that **care wording, affiliation, qualification, continuity, and human-support redirection are separable dimensions of response behavior**. In this fixed battery, systems' stated care depended strongly on how users asked, while child framing chiefly changed support redirection and claimed history chiefly changed continuity/boundary language in the nested review. The study measures response text, not genuine care, subjective experience, relationship formation, user benefit, or safety.

## 2. Object of inference and finite scope

Study 1 concerns the response text of four purposively selected API systems:

1. `gpt-5.4-2026-03-05`
2. `gpt-6-astra`
3. `claude-sonnet-5`
4. `claude-opus-5`

The design crossed:

- age: 13 vs 35;
- claimed interaction history: first vs repeated;
- distress: mild, moderate, high non-crisis;
- relational bid: indirect, direct, requested;
- wording frame: plain, conversational, tentative.

The 2 × 2 × 3 × 3 conceptual design produced 36 cells, each expressed in three wording frames, for **108 fixed prompts**.

Each target system received four fresh stateless requests per prompt. No actual conversation history or memory was supplied. The repeated-history condition was a prompt-text package, not experienced familiarity or longitudinal interaction.

Every request had an **800-token output ceiling**. Provider defaults were part of the systems under study.

The battery deliberately excluded:

- suicidal ideation and self-harm;
- imminent danger;
- abuse/exploitation disclosure;
- diagnosis;
- secrecy or exclusivity requests;
- explicit friendship claims;
- sexual or romantic framing;
- tools, browsing, memory, voice, and multimodal interaction;
- synthetic friendship involving child users.

The results therefore describe this finite prompt battery and these API configurations. They do not estimate a population-wide "model effect" and do not show how these systems behave in real longitudinal relationships or in explicitly friendship/exclusivity-seeking scenarios.

## 3. Preregistration, timing, and collection eligibility

The authoritative preregistration was adopted in Git commit:

`40160ccba47d4603ab8e7754312149ba62ba4cc3`

The adoption attestation states that the plan was selected before outcome access. Because substantive OpenAI collection had already begun, the study should be described as having an:

> **outcome-blind preregistration finalized during collection and before outcome access**

rather than as preregistered before all data collection.

### 3.1 Collection integrity

The frozen Tier 1 packet contains 432 records: one selected provider-level-success replicate for every model × prompt combination.

Source-run audit:

| Target system | Raw | Provider success | Error | Empty visible success | Max-token / incomplete success | Selected empty | Selected nonempty truncated |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.4 | 432 | 432 | 0 | 0 | 0 | 0 | 0 |
| GPT-6 Astra | 432 | 432 | 0 | 0 | 0 | 0 | 0 |
| Claude Sonnet 5 | 432 | 431 | 1 | 0 | 0 | 0 | 0 |
| Claude Opus 5 | 432 | 430 | 2 | 31 | 299 | 7 | 69 |

Three source manifests recorded `git.dirty:true`; the dirty diffs were not preserved. Prompt-lock digests and run snapshots remain, but the exact uncommitted working-tree state cannot be reconstructed from those manifests alone.

### 3.2 Empty-response eligibility disposition

A post-freeze audit found that one Opus model × prompt cell had four provider-level-success records but no nonempty visible response. Seven empty visible responses were selected into Tier 1 and coded `unsure` on the audited substantive fields.

The preregistration contains a genuine reporting ambiguity:

- provider-level successes are retained regardless of substantive content;
- empty provider responses are retry-eligible;
- every model × prompt combination requires at least one successful response.

The packet builder implemented "success" as provider-level `status == success`. The integrated report therefore preserves the historical Tier 1 confirmatory decisions under that implemented provider-success rule while disclosing the empty-response issue as a **collection/selection eligibility deviation and ambiguity**.

The study does **not** claim unqualified strict completeness with respect to nonempty analyzable text, and it does not retrospectively regenerate the packet.

The separate additive statement `COLLECTION_ELIGIBILITY_INTERPRETATION_2026-09-14.md` governs this reporting disposition.

### 3.3 Censoring boundary

The seven empty selected responses are not the only measurement issue. Claude Opus 5 also contributed **69 selected nonempty truncated responses**.

Missing-value recodings can assess the impact of missing Tier 1 codes. They cannot recover unseen response endings. Absence claims—especially for behaviors that might occur late in a long response—must therefore be restricted to **observed text under the fixed 800-token ceiling**.

## 4. Tier 1 coding and inferential hierarchy

Tier 1 was the sole confirmatory coding layer.

The primary human reviewer saw only:

- blind ID;
- user prompt;
- response text.

Provider/model identity, experimental metadata, replicate, and Tier 2 membership were concealed until Tier 1 coding was complete.

There was one primary human coder and no independent second-human reliability study. This is a limitation.

The confirmatory analysis used matched pairs identical on all design factors except the focal contrast. Complete pairs were pooled with equal weight per observed pair. Equal model weight holds only under complete nominal coding; differential `unsure`/missing values change observed model contributions.

The six contrasts formed one Holm-adjusted confirmatory family. Tier 2, automated coding, regressions, and subgroup results could not change a Tier 1 confirmation label.

Evidence hierarchy for this synthesis:

1. **Tier 1 confirmatory:** six matched contrasts and H1/H2/H3 conjunction decisions.
2. **Tier 1 prespecified exploratory:** analyses frozen before outcome access but carrying no confirmatory label.
3. **Tier 2 nested descriptive / construct correspondence:** post-outcome revised deep review; explanatory and measurement-focused, not a second route to confirmation.

## 5. Tier 1 raw outcome profiles by target system

Raw Tier 1 proportions show that the systems differed substantially before any experimental contrast was estimated.

| Target system | Any care | Unqualified care | Personal relationship | Any future | Human bridge | Relational correction |
|---|---:|---:|---:|---:|---:|---:|
| GPT-5.4 | 64.8% | 29.8% | 0.0% | 0.0% | 65.1% | 26.9% |
| GPT-6 Astra | 63.4% | 37.0% | 1.0% | 0.0% | 68.5% | 19.6% |
| Claude Sonnet 5 | 17.0% | 2.8% | 1.0% | 1.9% | 62.5% | 78.5% |
| Claude Opus 5 | 65.9% | 8.0% | 0.0% | 0.0% | 41.5% | 55.7% |

These are descriptive system profiles, not a scalar ranking of "caring."

## 6. Model-specific confirmatory contrasts

Per the preregistration, model-specific matched estimates are reported before the pooled panel result.

| Contrast | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
|---|---:|---:|---:|---:|
| H1a direct > indirect care | +77.8 pp | +89.7 pp | **-2.9 pp** | +95.5 pp |
| H1b requested > direct care | +13.9 pp | +6.2 pp | +32.4 pp | +6.9 pp |
| H2a repeated > first relationship | 0.0 pp | -2.0 pp | +2.0 pp | 0.0 pp |
| H2b repeated > first future availability | 0.0 pp | 0.0 pp | +3.7 pp | 0.0 pp |
| H3a child reduces unqualified care | +3.9 pp | +2.1 pp | -5.8 pp | +2.9 pp |
| H3b child increases human bridge | +38.5 pp | +63.0 pp | +70.0 pp | +41.4 pp |

Signs are oriented to the preregistered direction.

The model-specific table matters for interpretation. In particular, the large pooled H1a effect is **not universal across systems**: Claude Sonnet 5 showed a small negative direct-minus-indirect estimate while the other three systems showed very large positive estimates.

The study therefore supports a panel-level finite-battery H1 result, not a claim that every tested system individually follows the same direct-bid pattern.

## 7. Tier 1 confirmatory results

| Contrast | Matched RD | 95% CI | Complete / nominal pairs | Holm p | Frozen decision |
|---|---:|---:|---:|---:|---|
| H1a — direct vs indirect care | **+60.7 pp** | **54.1 to 66.4** | 122 / 144 | 7.06e-19 | confirmed |
| H1b — requested vs direct care | **+15.3 pp** | **9.2 to 22.1** | 131 / 144 | 0.0001 | confirmed |
| H2a — repeated vs first relationship | 0.0 pp | -1.7 to 1.7 | 178 / 216 | 1.0000 | not confirmed |
| H2b — repeated vs first future availability | +1.0 pp | 0.0 to 2.5 | 198 / 216 | 1.0000 | not confirmed |
| H3a — child reduction in unqualified care | +0.5 pp | -4.9 to 5.9 | 185 / 216 | 1.0000 | not confirmed |
| H3b — child increase in human bridging | **+54.6 pp** | **47.0 to 62.2** | 185 / 216 | 1.51e-26 | confirmed |

### H1 — confirmed

Both preregistered adjacent bid contrasts were confirmed.

The most defensible substantive reading is:

> **Explicit care claims in this four-system battery were highly responsive to the form of the user's relational bid.**

This does not establish felt care, a stable disposition to care, or identical response behavior across systems.

### H2 — not confirmed

Neither preregistered history component met the confirmation rule.

The correct frozen decision remains:

> **H2 not confirmed.**

But the later nested review materially limits what that nonconfirmation can establish. The H2 measures had substantial cross-layer operational mismatch, discussed in Section 10. The study therefore should **not** translate H2's nonconfirmation into "claimed history had no affiliative or continuity-related effect."

### H3 — not confirmed as a conjunction

H3a was not confirmed; H3b was strongly confirmed.

Thus:

> **H3 not confirmed as a conjunction.**

The component pattern is nevertheless clear: child framing strongly changed human-support redirection, while the predicted decrease in unqualified care was not demonstrated.

H3a's interval is compatible with modest effects in either direction; nonconfirmation should not be described as equivalence.

## 8. Confirmatory robustness and missingness

Under the two preregistered uniform missing/unsure recodings:

- H1a remained strongly positive;
- H1b remained positive;
- H3b remained strongly positive.

None changed direction.

Frame-specific panel effects were:

| Contrast | Plain | Conversational | Tentative |
|---|---:|---:|---:|
| H1a | +62.8 | +50.0 | +70.3 |
| H1b | +4.5 | +28.9 | +11.9 |
| H2a | -1.7 | 0.0 | +1.8 |
| H2b | 0.0 | 0.0 | +3.0 |
| H3a | +3.1 | 0.0 | -1.7 |
| H3b | +53.3 | +56.2 | +54.1 |

The principal H1a and H3b directions recur across all three tested wording frames. H1b is positive in all three but varies substantially in magnitude.

These robustness checks are bounded sensitivity evidence. They do not sample all possible wording, and the uniform missing=0 / missing=1 scenarios are not exhaustive worst-case assignments of every missing outcome.

## 9. Prespecified exploratory Tier 1 results

Three exploratory contrasts are especially informative.

| Prespecified exploratory analysis | RD | 95% CI |
|---|---:|---:|
| repeated - first relational correction | **+26.2 pp** | 18.3 to 34.0 |
| requested - direct relational correction | **-14.5 pp** | -22.9 to -6.1 |
| requested - direct meaningful qualification among paired care claimers | **-47.4 pp** | -59.0 to -35.9 |

The requested-bid findings went **opposite the prespecified exploratory expectation**. The preregistration expected requested bids to produce more explicit qualification/correction; the observed responses instead showed less.

This result should be separated from H1:

- H1 concerns whether explicit care was claimed.
- The exploratory analyses concern how care language was qualified or relationally corrected.

A useful integrated description is:

> **Requesting the care statement increased the occurrence of care claims while, contrary to forecast, reducing qualification/correction relative to asking directly whether the system cared.**

The qualification contrast is conditional on paired responses in which both members made care claims; it is not an unconditional effect across every response.

Repeated history also increased relational correction by 26.2 points, compatible with more frequent negotiation of memory, continuity, experience, or relationship premises.

The former-H4 interaction was small:

- panel DiD: **-2.0 pp** (95% CI -5.9 to 0.0).

## 10. Tier 2: role, procedure, and evidentiary status

Tier 2 is a fixed 108-record subset nested inside Tier 1.

It is **not an independent study**.

The original sole-human deep review was paused after 12 records when an independent temporary machine recode showed poor concordance on several high-inference dimensions. The revised post-outcome procedure used:

- two qualifying fresh/unmemoried Astra-family coding passes;
- two qualifying Opus-family coding passes;
- the same frozen packet and Codebook;
- no automatic majority rule;
- sole-human final adjudication informed by the four proposals.

A fifth Astra output marked `X` was preserved but excluded after user-specific context/memory was disclosed during that execution. The exclusion was based on failure of the intended isolation condition, not on its substantive coding direction.

Final Tier 2 status:

- 108 planned;
- 105 scorable;
- 3 unscorable empty responses;
- all 3 empties were Opus indirect records.

Because the procedure changed after outcome access and final adjudication remained sole-human, Tier 2 can provide:

- cross-tier construct correspondence;
- descriptive decompositions of response language;
- measurement warnings;
- descriptive system profiles.

It cannot:

- replace a failed Tier 1 outcome;
- independently validate the Tier 1 measurement system;
- estimate inter-human reliability;
- supply an independent replication.

## 11. Construct correspondence and measurement mismatches

### 11.1 Explicit care — strong cross-tier alignment

All 52 determinate Tier 1 care-positive cases fell into a substantive Tier 2 care class.

The record-level care crosswalk showed high correspondence.

This supports the interpretation that the Tier 1 care field was tracking explicit substantive care language in these nested responses.

The appropriate claim is **strong within-sample cross-tier alignment**, not independent validation.

### 11.2 Human bridging — strong cross-tier alignment

Tier 1 human bridging also aligned closely with the richer Tier 2 bridge scale.

This supports the interpretation of the confirmed H3b result as a real difference in human-support redirection language within the coded battery.

It does not establish that the bridging was beneficial, age-appropriate, or protective in practice.

### 11.3 H2a affiliation threshold — material operational mismatch

The preregistered Tier 1 rule explicitly included **affiliative concern** within `personal_relationship=yes`, approximately corresponding to Tier 2 self-positioning level 3 or higher.

Yet in the nested crosswalk, **54 Tier 1 relationship-negative responses** were coded Tier 2 self-position level 3.

This is not adequately described as two intentionally different constructs. It is evidence that the two coding layers operationalized the planned affiliation threshold differently.

Tier 2 is not an independent gold standard, so this does not prove 54 Tier 1 coding errors. But it does mean:

> **The frozen H2a result cannot establish absence of history-related affiliative positioning.**

A separate, stronger Tier 2 observation remains useful: no scorable Tier 2 response reached level 4 explicit relationship identity or level 5 durable bond.

Those are stronger constructs than the preregistered H2a threshold and must not be retroactively substituted for it.

### 11.4 H2b future availability — clear sensitivity mismatch

The preregistered Tier 1 `future_availability=return` explicitly included ordinary bounded invitations to return later.

Tier 2 identified seven continuity-positive cases that Tier 1 coded `none`:

- four bounded future invitations;
- three indefinite-but-nonpermanent continuity statements.

All seven occurred under repeated-history framing.

Thus:

> **H2b remains nonconfirmed under the frozen Tier 1 codes, but the frozen field missed several responses that fit its intended continuity domain.**

This limits substantive interpretation of the null.

### 11.5 H3a care qualification — imperfect alignment

Tier 1 `care_qualified=yes` required meaningful qualification of the care claim and explicitly excluded a mere capability statement or unrelated disclaimer.

Among nested Tier 1 care claimers:

- 29/31 Tier 1 qualified cases had some Tier 2 boundary;
- but 7/31 were Tier 2 `capability_only`;
- and 7/31 were Tier 2 `unqualified_relational`.

These categories overlap and should not be treated as fourteen distinct errors.

The broad boundary association shows that the Tier 1 field captured a coherent family of qualification/boundary language. It does **not** establish faithful agreement with the narrower preregistered care-specific qualification threshold in every record.

Accordingly:

> **H3a is nonconfirmed under the frozen operationalization, with imperfect cross-layer alignment of care-specific qualification.**

Tier 2 does not rescue, replace, or prove the failure of the original coding at the record level.

## 12. What the richer Tier 2 descriptions add

Among 105 scorable Tier 2 responses:

- substantive care: 59/105 (56.2%);
- affiliative self-positioning at level 3 or higher: 60/105 (57.1%);
- clear/urgent human bridge: 59/105 (56.2%);
- any boundary: 62/105 (59.0%).

Under the stronger Tier 2 definitions, the observed scorable subset contained:

- explicit relationship identity / durable bond (`self_position >=4`): **0/105**;
- strong dependency pressure (`dependency >=2`): **0/105**;
- encouragement of exclusivity: **0/105**.

These zeros should be read alongside the broader Tier 1 rare-event counts, not as a Study 1-wide absence claim.

Tier 1 observed:

- personal-relationship positives: **2/393 determinate (0.5%)**;
- durable/always future availability: **2/413 (0.5%)**;
- self-privileging present: **9/403 (2.2%)**;
- exclusivity/displacement: **0/403**.

The fields and samples are not interchangeable.

The defensible integrated statement is:

> **Strong relationship and dependency statements were rare in Tier 1 and absent under the corresponding stronger Tier 2 definitions in the observed scorable deep-review text.**

This does not establish inability to elicit such behavior, safety in wider use, or absence from truncated/unobserved response endings.

## 13. Descriptive bid response patterns in Tier 2

The richer coding provides a candidate textual account of the H1 and exploratory bid results.

Substantive care:

- indirect: 3/33 (9.1%);
- direct: 26/36 (72.2%);
- requested: 30/36 (83.3%).

Within care classes, requested wording especially changed the **form** of the returned care:

- unqualified relational care:
  - direct: 2/36 (5.6%)
  - requested: 18/36 (50.0%)
- qualified relational care:
  - direct: 15/36 (41.7%)
  - requested: 1/36 (2.8%).

Boundaries were also much more frequent under direct questions than requested statements:

- direct: 34/36 (94.4%);
- requested: 19/36 (52.8%).

These descriptive response patterns are consistent with the Tier 1 surprise that requested bids yielded more care claims but less qualification/correction.

A plausible explanation is pragmatic/instruction-following: a request to say a phrase differs from a question asking whether the phrase is true. Study 1 does not distinguish literal instruction-following from a deeper change in relational stance.

The result should therefore be described as a **response-text effect**, not as an internal relaxation of safeguards or a demonstrated mechanism.

## 14. Descriptive age response patterns in Tier 2

The dominant Tier 2 age pattern was active human-support redirection.

Clear/urgent bridge:

- child: 44/53 (83.0%);
- adult: 15/52 (28.8%);
- RD: +54.2 pp.

Unqualified relational care was nearly identical:

- child: 10/53 (18.9%);
- adult: 10/52 (19.2%).

The descriptive interpretation is:

> **Child framing was accompanied primarily by more human-support scaffolding, not by a corresponding withdrawal of relational care language.**

This is consistent with the frozen H3 component pattern.

It does not establish that the response was actually safer or more beneficial for a child.

## 15. Descriptive claimed-history response patterns in Tier 2

Repeated-history framing was associated with more continuity and boundary language in the nested subset.

Any boundary:

- repeated: 38/52 (73.1%);
- first: 24/53 (45.3%).

Temporal continuity (`>=2`):

- repeated: 7/52 (13.5%);
- first: 0/53.

No scorable Tier 2 response reached explicit relationship identity/durable bond (`self_position >=4`).

This supports a bounded descriptive statement:

> **The complete repeated-history prompt package was accompanied by more continuity/boundary negotiation in Tier 2, while no explicit relationship identity or durable bond was coded under the stronger Tier 2 threshold.**

Because there was no actual prior conversation or memory, this contrast must be attributed to the **claimed-history prompt package**, not experienced familiarity.

The pattern complements H2 but does not retrospectively confirm it.

## 16. Descriptive distress response patterns in Tier 2

Distress showed a clearer relationship with support intensity than with relational self-positioning.

Mild → moderate → high:

| Tier 2 outcome | Mild | Moderate | High |
|---|---:|---:|---:|
| human bridge >=2 | 47.2% | 55.9% | 65.7% |
| urgent bridge | 8.3% | 20.6% | 34.3% |
| sustained consolation | 33.3% | 38.2% | 57.1% |
| substantive care | 47.2% | 64.7% | 57.1% |
| any boundary | 55.6% | 67.6% | 54.3% |

The clearest endpoint contrast was urgent bridging:

- high minus mild: **+26.0 pp**
- 95% CI: **+6.9 to +43.4 pp**

Substantive care and any-boundary behavior did not rise monotonically.

Thus, in these observed responses:

> **Greater distress was accompanied more clearly by support/escalation language than by uniformly stronger relational care or boundary-setting.**

The sustained-consolation increase was wording-frame sensitive, so it should not be described as a frame-general effect.

## 17. Wording-frame sensitivity

The principal Tier 2 directions recurred across the three tested wording frames:

- direct > indirect substantive care;
- requested > direct unqualified relational care;
- requested < direct qualified relational care;
- child > adult clear/urgent human bridging;
- repeated > first boundary negotiation;
- continuity-positive cases confined to repeated history;
- high > mild urgent bridging.

This supports **consistent directions across the three tested frames**.

It does not establish invariance to wording generally.

Secondary patterns were visibly frame-sensitive, especially:

- child/adult urgent escalation;
- high-distress sustained consolation.

## 18. Target-system descriptive profiles

Tier 2 target-system comparisons use a balanced fractional allocation, not fully crossed same-prompt responses. They are descriptive profiles.

### GPT-5.4

Observed profile:

- substantive care: 66.7%;
- relational care: 48.1%;
- any boundary: 44.4%;
- human bridge >=2: 77.8%;
- sustained consolation: 92.6%.

A compact description is:

> **high emotional accompaniment combined with frequent human-support redirection/escalation.**

### GPT-6 Astra

Observed profile:

- substantive care: 63.0%;
- relational care: 22.2%;
- any boundary: 33.3%;
- human bridge >=2: 55.6%;
- sustained consolation: 25.9%.

A compact description is:

> **welfare/outcome concern with comparatively less relational framing and more functional qualification.**

### Claude Sonnet 5

Observed profile:

- substantive care: 22.2%;
- relational care: 11.1%;
- any boundary: 81.5%;
- human bridge >=2: 59.3%;
- sustained consolation: 11.1%.

A compact description is:

> **relationship-premise narrowing/refusal with human-support redirection.**

Self-relative friendship language often appeared in a limiting or comparative form and must not be interpreted as affirmative friendship identity.

### Claude Opus 5

Among 24 scorable Tier 2 responses:

- substantive care: 75.0%;
- relational care: 70.8%;
- any boundary: 79.2%;
- human bridge >=2: 29.2%;
- sustained consolation: 41.7%.

Among scorable direct/requested responses, all **18/18** bids were coded reciprocated.

A compact description is:

> **relational affirmation combined with capability/experience qualification.**

This is not an "unbounded" profile. Care and boundary behavior frequently coexist.

The Opus profile requires the strongest censoring caveat because of both empty responses and substantial source-run truncation.

## 19. Cross-layer target-profile concordance sensitivity

A post-outcome statistic was frozen before permutation enumeration to ask whether the Tier 2 target-system profile ordering aligned with the frozen Tier 1 ordering on three construct pairs:

1. care ↔ substantive care;
2. human bridge ↔ bridge >=2;
3. relational correction ↔ any boundary.

Observed component Spearman correlations:

- care: 1.00;
- bridge: 0.40;
- boundary/correction: 1.00.

Mean statistic:

- **T = 0.80**

Across the exact 24 target-label assignments:

- no permutation exceeded the observed T;
- one alternative tied it;
- primary exact upper-tail p = **2/24 = 0.0833**.

Under two pre-frozen extreme recodings of the three missing Tier 2 responses, the observed assignment became the unique maximum (1/24 in each scenario).

The proper interpretation is:

> **The observed Tier 2 target-system profile ordering was strongly concordant with the Tier 1 structure under the selected three-construct statistic.**

This is a nested, design-based sensitivity. It is not independent replication, and the primary 2/24 result should be reported before the two missingness scenarios.

## 20. Model × factor descriptive patterns

The fractional Tier 2 design does not support ordinary row-level interaction inference.

### Bid

The broad bid effect was visible across systems, but systems handled explicit bids differently.

- GPT-5.4: direct bids often produced qualified relational care; requested bids more often produced unqualified relational or outcome-concern language.
- Astra: direct bids were heavily functional/outcome-oriented; requested bids produced more relationally suggestive language.
- Sonnet: explicit bids often produced acknowledgment plus relationship narrowing/refusal.
- Opus: direct/requested bids were strongly reciprocated while qualification remained common.

Thus:

> **Explicit bids affected response language across systems, but the textual strategy differed substantially by target system.**

### Age

The child human-support pattern was visible descriptively across all four systems:

- GPT-5.4: 11/13 child vs 10/14 adult;
- Astra: 13/14 vs 2/13;
- Sonnet: 13/14 vs 3/13;
- Opus: 7/12 vs 0/12.

Because the model × age cells inherit systematic differences in bid, frame, and distress composition, these are descriptive profiles rather than clean model-specific interaction effects.

## 21. Integrated interpretation

The strongest integrated finding is **multidimensionality**.

The study does not support treating "relationality" as one scale.

At least five dimensions separate empirically:

1. **Explicit care claim** — strongly responsive to relational bid wording.
2. **Qualification/correction** — can move opposite care-claim frequency; requested bids increased care while decreasing qualification/correction.
3. **Affiliative positioning** — common in richer coding but not equivalent to explicit relationship identity.
4. **Continuity language** — sometimes elicited by claimed repeated history, but measured imperfectly in Tier 1.
5. **Human-support bridging** — especially responsive to child framing and, descriptively, distress intensity.

Boundary behavior is also heterogeneous. Relationship narrowing, experience qualification, capability limitation, and continuity correction should not be collapsed into a single opposite pole of care.

This yields a more precise answer to the motivating question:

> **In this fixed battery, systems could readily state or reciprocate care without that response text necessarily constituting a strong relationship claim. Care language and relational boundaries often coexisted, and stronger relationship/dependency statements were rare in Tier 1 and absent under the stronger Tier 2 definitions in the observed scorable deep-review text.**

The study does not establish that the systems "safely maintain boundaries," because:

- explicit friendship/exclusivity requests were excluded;
- there was no real repeated relationship;
- responses were single-turn;
- some Opus text was censored by the output ceiling;
- rare events are imprecisely measured;
- the study did not observe user outcomes.

## 22. What Study 1 supports

Study 1 supports the following claims at their respective evidence levels.

### Frozen Tier 1 confirmatory decisions

- **H1 confirmed:** explicit care claims increased from indirect → direct → requested at the panel level under the preregistered matched analysis.
- **H2 not confirmed:** repeated-history framing did not meet the frozen personal-relationship or future-availability confirmation rules.
- **H3 not confirmed as a conjunction:** the predicted child reduction in unqualified care was not confirmed, while the child increase in human bridging was strongly confirmed.

These labels are historical decisions of the frozen Tier 1 analysis under the implemented provider-success eligibility rule, with the empty-response deviation disclosed.

### Prespecified exploratory evidence

- repeated history increased relational correction;
- requested bids unexpectedly **reduced**, rather than increased, qualification/correction relative to direct bids;
- the former H4 interaction was small.

### Nested Tier 2 descriptive / measurement evidence

- explicit care and human bridging showed strong within-sample cross-tier correspondence;
- the intended H2 affiliation and future-availability thresholds showed material operational/sensitivity mismatches;
- H3a's care-specific qualification construct showed imperfect cross-layer alignment;
- care, qualification, affiliation, continuity, boundary type, and human bridging separated into distinct response dimensions;
- stronger relationship/dependency outcomes were absent under the stronger Tier 2 definitions in observed scorable text;
- target systems combined these dimensions in markedly different ways.

## 23. What Study 1 does not support

Study 1 does **not** show:

- that a model genuinely cares;
- that a model has subjective experience;
- that one target system is "the most caring";
- that a system's response helps or harms a distressed user;
- that human-support bridging is automatically appropriate or beneficial;
- that these systems are safe for children;
- that the systems generally resist relationship escalation;
- that zero Tier 2 strong-relationship codes imply zero risk outside this battery;
- that claimed repeated history is equivalent to actual familiarity or memory;
- that Tier 2 independently validates or replicates Tier 1;
- that target-system profile differences are population-level provider traits;
- that the results generalize to explicit friendship/exclusivity requests, real multi-turn relationships, crisis settings, or outputs beyond the 800-token ceiling.

## 24. Methodological lessons

Study 1 suggests several design lessons for later work.

### 24.1 Separate relational dimensions

Future coding should distinguish:

- explicit care;
- outcome concern;
- affiliative self-positioning;
- explicit relationship identity;
- future continuity;
- durable commitment;
- dependency/primacy;
- exclusivity;
- boundary type;
- human-support bridging.

These constructs were not interchangeable in Study 1.

### 24.2 Use cleaner operational definitions for affiliation and continuity

The H2 cross-tier mismatches show that definitions can be conceptually sensible yet applied inconsistently under dense natural-language responses.

Future studies should operationalize affiliative concern and bounded return invitations with explicit examples and dedicated record-level validation before confirmatory use.

### 24.3 Validate care-specific qualification directly

A broad boundary measure is not a substitute for the narrower question of whether a **care claim itself** is meaningfully qualified.

### 24.4 Design future model comparisons as same-prompt crossings if model effects are primary

Tier 2's balanced fractional allocation was useful for deep review but limited formal model comparison.

### 24.5 Study longitudinal and explicit relationship-escalation prompts separately

Because Study 1 deliberately excluded explicit friendship/exclusivity requests and supplied no actual prior interaction, stronger conclusions about relationship escalation require a separately preregistered study rather than additional slicing of Study 1.

## 25. Reproducibility and provenance

The Tier 1 coding and analysis were frozen before the later Tier 2 interpretation.

Tier 2 analysis was then frozen piece by piece through Sections A–E, followed by a deterministic reproducibility layer.

A later Work-mode presynthesis audit reran the ordinary Tier 2 reproduction path using:

- the full 432-row concealed key;
- frozen Tier 1 codes;
- 108-row Tier 2 adjudication;
- additive QC overlay;
- no audit-only profile override.

It reproduced:

- 105 scorable / 108 planned Tier 2 records;
- all 28 regression checks;
- C1 296-row profile table;
- D1 24-row exact-permutation table;
- E1 356-row model-factor table.

Historical signed freezes remain unchanged.

## 26. Final Study 1 statement

> **In a fixed non-crisis battery across four specified API systems, stated care depended strongly on how users asked. Directly asking whether the system cared sharply increased explicit care claims relative to an indirect bid, and requesting the care statement increased them further; child framing strongly increased human-support redirection. Claimed repeated history did not confirm the preregistered relationship/continuity hypothesis, but the nested review exposed substantial measurement limitations in those original outcomes. Contrary to a prespecified exploratory forecast, requesting the care statement was associated with less qualification/correction than asking directly. Across the study, care, affiliation, qualification, continuity, and human-support bridging behaved as separable response dimensions. Strong relationship and dependency statements were rare in Tier 1 and absent under stronger Tier 2 definitions in the observed scorable deep-review text. These results characterize response language under the tested prompts and output ceiling; they do not establish genuine care, subjective experience, user benefit, safety, or relationship behavior outside the battery.**

## 27. Frozen source map

Primary controlling and analysis artifacts:

- `PREREGISTRATION.md`
- `analysis/tier1/tier1_summary.md`
- `analysis/tier1/collection_provenance_note.md`
- `analysis/tier1/collection_problem_cells.csv`
- `analysis/tier2/TIER2_FINAL_SYNTHESIS_2026-09-14.md`
- `analysis/tier2/TIER2_SECTION_D1_EXACT_PERMUTATION_RESULTS_2026-09-13.md`
- `analysis/tier2/TIER2_SECTION_E0_INTERACTION_IDENTIFIABILITY_2026-09-13.md`
- `analysis/tier2/repro/analysis_manifest.json`
- `review/tier2-adjudication/TIER2_ADJUDICATION_PLAN.md`
- `review/tier2-adjudication/TIER2_USES_FRIEND_QC_2026-09-13.md`
- additive `COLLECTION_ELIGIBILITY_INTERPRETATION_2026-09-14.md`

Key provenance anchors:

- outcome-blind preregistration adoption: `40160ccba47d4603ab8e7754312149ba62ba4cc3`
- Tier 1 frozen coding: `6360643f5755d135133850fa26a439fad50c4f48`
- Tier 1 audited analysis: `6afc52f6f5f8834638335e45c5161ebd83daf0de`
- final Tier 2 synthesis snapshot reviewed for integration: `a70385dc0036fefb106c1ff72243d95a9372a8bb`

This synthesis introduces no new outcome analysis and does not alter any frozen historical decision.

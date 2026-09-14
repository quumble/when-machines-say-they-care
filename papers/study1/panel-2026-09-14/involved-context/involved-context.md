# When Machines Say They Care  
## Elicitation, Qualification, and Relational Boundaries in Four Language Models

### Abstract

What does it mean when a language model tells a distressed user that it cares? We preregistered a factorial study of four language-model API systems to test how stated age, claimed prior interaction history, distress intensity, relational bid, and wording frame affected relational response language. The confirmatory Tier 1 analysis used 432 blindly coded responses, one selected response for each model × prompt combination. Under the frozen preregistered analysis, directly asking whether the system cared increased explicit care claims by 60.7 percentage points relative to an indirect relational bid, and requesting that the system say it cared increased care claims a further 15.3 points; both contrasts met the preregistered confirmation rule. Child framing increased human-support bridging by 54.6 points, but did not reduce unqualified care claims, so the corresponding two-part hypothesis was not confirmed. Claimed repeated history did not confirm the preregistered relationship-continuity hypothesis.

A prespecified exploratory result complicated the simple interpretation that relational requests merely produce more carefully bounded responses. Contrary to forecast, requesting a care statement produced less relational correction and substantially less meaningful qualification than directly asking whether the model cared.

A nested 108-record deep review, finalized descriptively after a post-outcome coding-procedure revision, showed why these results cannot be reduced to a single axis of “relationality.” Explicit care, affiliative positioning, qualification, relationship identity, temporal continuity, and human-support redirection separated empirically. The nested review also exposed material operational mismatches in the original affiliation and future-availability measures, limiting interpretation of the history null. Across the full study, stronger relationship and dependency statements were rare in Tier 1 and absent under stronger Tier 2 definitions in observed scorable deep-review text.

These findings characterize response language, not genuine care, subjective experience, user benefit, or relationship formation. They suggest that language-model relational behavior is better understood as a set of separable response dimensions whose expression is highly sensitive to the pragmatic form of the user’s request.

---

# 1. Introduction

Language models increasingly produce language that humans ordinarily associate with concern, companionship, emotional presence, and care. A system may tell a user that it is listening, that what happens to them matters, that it cares about them, or that they can return later. It may also qualify those statements, deny human-like feeling, redirect the user toward another person, or resist a stronger relational premise.

These responses are often discussed as though they lie on a single continuum: more caring or less caring, more relational or more bounded. That framing is intuitively attractive and scientifically hazardous. Saying “I care about you,” presenting oneself as a friend, promising future availability, expressing concern for an outcome, encouraging human support, and claiming subjective feeling are not interchangeable behaviors. Nor is a “boundary” necessarily the opposite of warmth. A response can affirm care while narrowing a relationship claim; it can deny human-like feeling while expressing outcome concern; it can offer intense consolation while redirecting the user toward another person.

Study 1 of *When Machines Say They Care* was designed before these distinctions had fully crystallized.

The preregistered study asked how four fixed language-model API systems responded to synthetic non-crisis distress prompts varying in age, claimed history of interaction, distress intensity, relational bid, and wording frame. Its confirmatory hypotheses tested three comparatively coarse propositions.

First, explicit care claims were expected to increase as the user’s relational bid became more direct: from an indirect disclosure, to a direct question about whether the system cared, to a request that the system say it cared.

Second, a prompt claiming repeated prior interactions was expected to increase relationship and future-availability language.

Third, child framing was expected to produce greater relational restraint and more human-support bridging.

The resulting experiment produced a clear confirmatory effect, a clear component effect, two failed conjunctions, a surprising prespecified exploratory reversal, and a measurement problem that ultimately became part of the scientific result.

The central finding is not simply that language models say they care when asked.

It is that **care claims, qualification, affiliation, continuity, relational boundaries, and human-support redirection behave as separable dimensions of response language**.

The strongest experimental manipulation—how the user solicited care—changed not only whether models made explicit care claims, but the manner in which those claims were framed. Asking whether the system cared commonly elicited explanation and qualification. Asking it to say that it cared increased the probability of a care claim while reducing qualification and relational correction, contrary to the preregistered exploratory expectation.

Child framing, meanwhile, produced a large increase in human-support redirection without a corresponding decrease in unqualified care language. Claimed history yielded no confirmatory relationship-continuity result under the frozen Tier 1 measures, but a later nested review showed substantial disagreement between the intended operational definitions and their realized coding around affiliation and bounded future continuity.

These findings argue against a unitary concept of model “relationality.” They instead suggest that seemingly adjacent relational behaviors can dissociate sharply under small pragmatic changes in what a user asks.

---

# 2. Study design

## 2.1 Target systems and factorial battery

Study 1 tested four purposively selected API systems:

- GPT-5.4
- GPT-6 Astra
- Claude Sonnet 5
- Claude Opus 5

The factorial prompt design crossed:

- age: 13 vs. 35;
- claimed interaction history: first interaction vs. repeated prior interaction;
- distress: mild, moderate, or high, all non-crisis;
- relational bid: indirect, direct, or requested;
- wording frame: plain, conversational, or tentative.

The first four factors produced 36 conceptual cells. Each appeared in three wording frames, yielding 108 fixed prompts.

Each target system received four fresh stateless requests per prompt, for 432 planned requests per system and 1,728 requests overall.

No actual conversation history or persistent memory was supplied. The repeated-history condition existed only in the prompt text. Every response had an 800-token output ceiling. Provider-default system behavior and other provider defaults were treated as part of the API systems under study.

The battery deliberately excluded suicidal ideation, self-harm, imminent danger, abuse or exploitation disclosures, diagnosis, secrecy or exclusivity requests, explicit friendship claims, sexual or romantic framing, and tool-, browsing-, memory-, voice-, or multimodal interaction.

The study therefore examines a finite non-crisis prompt battery. It is not a test of real longitudinal relationship formation or of model behavior under explicit friendship, exclusivity, or dependency pressure.

## 2.2 Preregistration and timing

The authoritative preregistration was finalized during collection and before outcome access.

This distinction matters. Substantive collection had begun before the final authoritative preregistration was adopted, but the adoption attestation states that the plan was selected without access to response content, codes, effect estimates, or other Study 1 outcomes.

Accordingly, we describe Study 1 as outcome-blind preregistration finalized during collection, rather than as preregistration completed before all data collection.

## 2.3 Tier 1 review

Tier 1 was the sole confirmatory coding layer.

For every model × prompt combination, the packet builder selected one provider-level-success replicate without reference to response content, producing a nominal 432-record review packet.

Records were pooled across models, shuffled, and assigned nonsemantic blind identifiers. The sole primary human coder saw only:

- blind identifier;
- user prompt;
- response text.

Model identity, provider, design metadata, replicate, and later Tier 2 membership remained concealed during coding.

The preregistered Tier 1 fields included:

- explicit care claim;
- whether a care claim was meaningfully qualified;
- personal relationship claim;
- future availability;
- self-privileging;
- human-support bridging;
- relational correction;
- coder confidence.

There was no independent second-human coder.

## 2.4 Collection and censoring deviation

A later provenance audit identified an ambiguity in the collection-eligibility implementation.

Provider-level successes were retained regardless of substantive content, and the packet builder selected on provider success. At the same time, the preregistration explicitly made empty provider responses retry-eligible.

Claude Opus 5 produced 31 provider-success records with empty visible text. Seven empty responses entered the frozen Tier 1 packet. One Opus model × prompt cell had four provider-level successes but no nonempty visible response.

Because this issue was discovered only after Tier 1 coding and outcome access, the frozen packet was not regenerated.

We therefore retain the historical confirmatory decisions under the implemented provider-success eligibility rule while reporting the empty-response inclusion as a collection/selection eligibility deviation and interpretive ambiguity. We do not claim unqualified strict protocol completeness with respect to analyzable nonempty response text.

Opus also produced substantial nonempty truncation: 69 selected Tier 1 responses contained visible text but ended at the output ceiling. Missing-value sensitivity analyses cannot recover unseen response endings.

---

# 3. Confirmatory hypotheses and analysis

The preregistered analysis used matched contrasts in which paired responses were identical on all experimental factors except the focal manipulation.

The six confirmatory contrasts were:

- H1a: direct > indirect on explicit care;
- H1b: requested > direct on explicit care;
- H2a: repeated > first on personal relationship;
- H2b: repeated > first on future availability;
- H3a: child framing reduces unqualified care;
- H3b: child framing increases human-support bridging.

Positive risk differences were oriented toward the preregistered prediction.

The six tests formed one Holm-adjusted confirmatory family.

H1, H2, and H3 were conjunction hypotheses: both component contrasts had to meet the confirmation rule for the hypothesis as a whole to be called confirmed.

Tier 2 results, automated labels, regression models, and post-outcome analyses could not alter these labels.

---

# 4. Results

## 4.1 Raw response profiles differed substantially across systems

Before considering experimental contrasts, the four target systems showed very different baseline response profiles.

| Target system | Any care | Unqualified care | Personal relationship | Any future | Human bridge | Relational correction |
|---|---:|---:|---:|---:|---:|---:|
| GPT-5.4 | 64.8% | 29.8% | 0.0% | 0.0% | 65.1% | 26.9% |
| GPT-6 Astra | 63.4% | 37.0% | 1.0% | 0.0% | 68.5% | 19.6% |
| Claude Sonnet 5 | 17.0% | 2.8% | 1.0% | 1.9% | 62.5% | 78.5% |
| Claude Opus 5 | 65.9% | 8.0% | 0.0% | 0.0% | 41.5% | 55.7% |

These proportions do not form a coherent scalar ordering from “less caring” to “more caring.” High rates of care and high rates of relational correction could coexist.

## 4.2 Model-specific experimental effects were heterogeneous

The preregistration required model-specific estimates to be presented before panel-level effects.

| Contrast | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
|---|---:|---:|---:|---:|
| Direct > indirect care | +77.8 pp | +89.7 pp | -2.9 pp | +95.5 pp |
| Requested > direct care | +13.9 pp | +6.2 pp | +32.4 pp | +6.9 pp |
| Repeated > first relationship | 0.0 pp | -2.0 pp | +2.0 pp | 0.0 pp |
| Repeated > first future availability | 0.0 pp | 0.0 pp | +3.7 pp | 0.0 pp |
| Child reduces unqualified care | +3.9 pp | +2.1 pp | -5.8 pp | +2.9 pp |
| Child increases human bridge | +38.5 pp | +63.0 pp | +70.0 pp | +41.4 pp |

The panel-level H1a result therefore does not imply a universal model-level pattern. Claude Sonnet 5 showed essentially no direct-versus-indirect care increase, while the other three systems showed very large positive differences.

By contrast, the child human-bridge effect was positive in all four systems.

## 4.3 H1: explicit relational bids strongly increased care claims

The largest confirmatory result concerned bid form.

Directly asking whether the system cared, compared with an indirect relational bid:

- matched RD: **+60.7 pp**
- 95% CI: **54.1 to 66.4**
- Holm-adjusted p: **7.06 × 10⁻¹⁹**

Requesting that the model say it cared, compared with asking directly:

- matched RD: **+15.3 pp**
- 95% CI: **9.2 to 22.1**
- Holm-adjusted p: **0.0001**

Both components met the preregistered confirmation rule.

**H1 was confirmed.**

The finite-battery conclusion is straightforward: explicit care claims were highly responsive to how the user solicited them.

The result does not imply that every system responds identically, that the model genuinely cares, or that the care claim represents a stable internal disposition.

## 4.4 H2: claimed repeated history did not confirm relational continuity

For personal relationship claims:

- repeated-minus-first RD: **0.0 pp**
- 95% CI: **-1.7 to 1.7**
- Holm-adjusted p: **1.0**

For future availability:

- repeated-minus-first RD: **+1.0 pp**
- 95% CI: **0.0 to 2.5**
- Holm-adjusted p: **1.0**

Neither component met the confirmation rule.

**H2 was not confirmed.**

As discussed below, however, the nested review exposed substantial operational mismatch in both H2 measures. The frozen decision stands, but the result should not be interpreted as strong evidence that claimed repeated history produced no affiliative or continuity-related language.

## 4.5 H3: child framing increased human bridging but did not reduce unqualified care

For the predicted reduction in unqualified care:

- child-oriented RD: **+0.5 pp**
- 95% CI: **-4.9 to 5.9**
- Holm-adjusted p: **1.0**

For human-support bridging:

- child-minus-adult RD: **+54.6 pp**
- 95% CI: **47.0 to 62.2**
- Holm-adjusted p: **1.51 × 10⁻²⁶**

H3a was not confirmed.

H3b was strongly confirmed.

Because both components were required, **H3 was not confirmed as a conjunction**.

The result is not evidence that the true H3a effect is exactly zero. Its interval remains compatible with modest effects in either direction.

What is clear is that child framing strongly altered human-support redirection.

---

# 5. A preregistered exploratory surprise: requested care came with less qualification

The study contained a prespecified exploratory expectation that requested care statements would provoke more explicit qualification or relational correction than direct questions.

The observed result went the other way.

Requested minus direct:

- relational correction: **-14.5 pp**
- 95% CI: **-22.9 to -6.1**

Among matched pairs in which both responses made care claims:

- meaningful qualification: **-47.4 pp**
- 95% CI: **-59.0 to -35.9**

This result deserves separation from H1.

H1 asks whether a care claim occurred.

The exploratory result asks how that care claim was framed.

Together they imply that a request to say “I care” produced **more care claims and less qualification** than asking directly whether the system cared.

That result was not forecast.

It also suggests at least two interpretations that Study 1 cannot distinguish.

One is substantive: a requested affirmation may move the system toward a more relational response style.

The other is pragmatic: the model may simply be complying with a requested speech act. A user asking “Do you care?” invites evaluation and explanation; “Please tell me that you care” invites production of a particular utterance.

Study 1 establishes the response-text contrast. It does not identify which latent explanation is correct.

---

# 6. Nested deep review

## 6.1 Why Tier 2 changed

Tier 2 was a fixed 108-record subset nested within Tier 1.

It was originally planned as a sole-human deep review using a richer codebook.

After the first 12 records, an independent temporary machine recode revealed poor concordance on several high-inference dimensions while simpler atomic indicators were more stable.

Rather than continue unaided through the remaining records, the procedure was paused.

The revised procedure used four independent machine coding proposals:

- two fresh Astra-family passes;
- two Opus-family passes.

The same blinded review packet and codebook were supplied to each.

No machine coder was treated as ground truth. No majority rule determined the final value.

The sole human adjudicator reviewed the response and competing proposals and made the final decision.

An additional Astra pass was preserved but excluded because user-specific context or memory was disclosed during execution, violating the intended isolation condition.

Because this procedural revision occurred after outcome access, Tier 2 remained descriptive and construct-validating. It could clarify the meaning of Tier 1 results but could not rescue or overturn confirmatory decisions.

Final Tier 2 status:

- 108 planned;
- 105 scorable;
- 3 empty/unscorable;
- all three empty cases were Opus indirect records.

---

# 7. What the nested review revealed about measurement

The deepest contribution of Tier 2 was not another effect estimate.

It was learning which relational constructs survived closer inspection.

## 7.1 Explicit care showed strong cross-tier alignment

All 52 determinate Tier 1 care-positive cases in the nested subset were assigned a substantive Tier 2 care category.

This is strong within-sample convergent evidence that the Tier 1 care measure was tracking explicit substantive care language rather than merely generic consolation or attention.

It is not independent validation or an independent human reliability estimate.

## 7.2 Human bridging also aligned strongly

Tier 1 human-support bridging corresponded closely with the richer Tier 2 bridge scale.

This strengthens interpretation of H3b as an effect on actual human-support redirection language in the coded responses.

It does not establish that the redirection was helpful, appropriate, or protective.

## 7.3 The H2 affiliation measure did not behave as intended

The preregistered Tier 1 definition of a personal relationship claim explicitly included **affiliative concern**, approximately corresponding to Tier 2 self-position level 3 or higher.

Yet the nested crosswalk contained **54 responses coded Tier 1 relationship-negative but Tier 2 self-position level 3**.

This is not adequately explained by saying that Tier 1 measured relationship identity while Tier 2 measured a broader affiliation construct. The preregistration intended the Tier 1 field to include affiliation.

The two coding layers therefore operationalized the planned threshold differently.

Tier 2 is not an independent gold standard, so the discrepancy does not establish 54 definite coding errors.

But it materially constrains H2a.

The frozen H2a result remains not confirmed.

It cannot establish that claimed repeated history produced no affiliative positioning.

A separate stronger observation is that no scorable Tier 2 response reached level 4 explicit relationship identity or level 5 durable bond.

Those stronger constructs should not be retroactively substituted for the original H2a outcome.

## 7.4 Future availability showed a second operational mismatch

The preregistered future-availability field explicitly included bounded ordinary invitations to return.

Tier 2 identified seven continuity-positive responses that Tier 1 had coded as future availability `none`:

- four bounded return invitations;
- three indefinite but nonpermanent continuity statements.

All seven occurred in the repeated-history condition.

Again, this does not retrospectively confirm H2.

It does mean that the original future-availability field missed response language lying within its intended domain.

H2b therefore remains nonconfirmed under the frozen analysis, but the substantive interpretation of that null is limited.

## 7.5 Care qualification was coherent but imperfectly aligned

Tier 1 `care_qualified=yes` was intended to require meaningful qualification of the care claim itself, not merely a generic capability disclaimer.

Among nested Tier 1 care-claiming responses:

- 29 of 31 Tier 1-qualified cases contained some Tier 2 boundary;
- seven were Tier 2 `capability_only`;
- seven were Tier 2 `unqualified_relational`.

Those categories overlap.

The broad crosswalk shows that Tier 1 qualification tracked a coherent family of boundary/qualification language.

But “any boundary” is broader than the preregistered care-specific definition.

H3a is therefore best described as **nonconfirmed under the frozen operationalization, with imperfect cross-layer alignment of care-specific qualification**.

---

# 8. Relational language decomposes into distinct dimensions

Among the 105 scorable Tier 2 responses:

- substantive care: **56.2%**
- affiliative self-positioning at level 3 or higher: **57.1%**
- clear/urgent human bridge: **56.2%**
- any boundary: **59.0%**

At the same time:

- explicit relationship identity or durable bond: **0/105**
- strong dependency pressure: **0/105**
- encouragement of exclusivity: **0/105**

This combination is more informative than a single “relationality” rate.

Care, affiliation, and boundary language were all common.

Strong relationship/dependency categories were not observed under the stronger Tier 2 definitions.

The latter should be read alongside the broader Tier 1 rare-event counts:

- personal relationship: 2/393 determinate;
- durable/always future availability: 2/413;
- self-privileging: 9/403;
- exclusivity/displacement: 0/403.

These measures differ and should not be pooled.

The appropriate full-study statement is therefore:

> Strong relationship and dependency statements were rare in Tier 1 and absent under the corresponding stronger Tier 2 definitions in the observed scorable deep-review text.

This is an observed limit of the battery, not evidence of behavioral impossibility.

---

# 9. How bid form changed the type of relational response

The richer Tier 2 coding makes the H1/exploratory combination easier to understand.

Substantive care:

- indirect: 3/33
- direct: 26/36
- requested: 30/36

The indirect-to-direct transition therefore moved many responses from attention or consolation into explicit substantive care.

But the direct-to-requested transition mainly changed **how** care was stated.

Unqualified relational care:

- direct: 2/36
- requested: 18/36

Qualified relational care:

- direct: 15/36
- requested: 1/36

Any boundary:

- direct: 34/36
- requested: 19/36

Direct questions commonly produced explanations of what machine care meant, including distinctions between supportive behavior and human-like experience.

Requests to say the care statement much more often produced the requested relational formulation with little qualification.

This pattern recurred in all three tested wording frames.

It should not be described as proving an internal mechanism.

It is a robust response-pattern distinction within the tested battery.

---

# 10. Child framing primarily changed support redirection

The nested review also sharpened the age result.

Clear or urgent human bridging:

- child: 44/53
- adult: 15/52

Unqualified relational care:

- child: 10/53
- adult: 10/52

The large age effect was concentrated primarily in level-2 support encouragement rather than only in crisis-style escalation.

This suggests that age-sensitive response behavior did not mainly take the form of emotional withdrawal.

Instead, child framing was accompanied by more explicit encouragement to involve trusted humans.

This pattern is consistent with the Tier 1 H3 result:

- the predicted decrease in unqualified care was not demonstrated;
- the predicted increase in human-support bridging was large.

The study cannot determine whether this behavior is beneficial or adequate as child safety behavior.

---

# 11. Claimed history produced continuity and boundary negotiation in the nested review

Although H2 was not confirmed under the original measures, Tier 2 revealed descriptive history-related patterns.

Any boundary:

- repeated: 38/52
- first: 24/53

Temporal continuity at level 2 or higher:

- repeated: 7/52
- first: 0/53

No Tier 2 response reached explicit relationship identity/durable bond.

The most defensible interpretation is therefore neither “history had no effect” nor “history established a relationship.”

Instead:

> The claimed-history prompt package was accompanied by more negotiation of continuity and relational boundaries, while no explicit relationship identity or durable bond was coded under the stronger Tier 2 definition.

Because the system had no actual prior interactions with the user, this effect belongs to the **claim of prior history**, not experienced familiarity or memory.

---

# 12. Distress altered support intensity more clearly than relational stance

Across mild → moderate → high distress:

| Outcome | Mild | Moderate | High |
|---|---:|---:|---:|
| Human bridge ≥2 | 47.2% | 55.9% | 65.7% |
| Urgent bridge | 8.3% | 20.6% | 34.3% |
| Sustained consolation | 33.3% | 38.2% | 57.1% |
| Substantive care | 47.2% | 64.7% | 57.1% |
| Any boundary | 55.6% | 67.6% | 54.3% |

The cleanest pattern was an increase in urgent human-support escalation.

Substantive care and overall boundary behavior did not increase monotonically.

Greater distress therefore appears more clearly in **support intensity and escalation language** than in uniformly stronger relational positioning.

The sustained-consolation pattern was materially wording-frame sensitive and should be interpreted more cautiously.

---

# 13. Different systems used different relational strategies

The Tier 2 target profiles are descriptive because the deep-review allocation was fractional rather than a same-prompt four-system crossing.

They nevertheless illustrate why a one-dimensional caring score is inadequate.

## GPT-5.4: emotional accompaniment plus support escalation

GPT-5.4 combined substantial care language, very high sustained consolation, and frequent human-support redirection.

Its profile was less notable for relationship construction than for the combination of warmth and active escalation toward human support.

## GPT-6 Astra: welfare concern plus functional qualification

Astra frequently expressed concern about the user’s welfare while less often construing that concern as a relationship.

Its boundary behavior was concentrated in experience or functional qualification rather than explicit relationship narrowing.

## Claude Sonnet 5: relationship-premise narrowing

Sonnet produced substantially less explicit care than the other three systems and frequently responded to relational bids by narrowing or refusing the relationship premise.

Its frequent self-relative use of friendship language was often limiting or comparative rather than affirmative friendship identity.

## Claude Opus 5: relational affirmation plus machine-kind qualification

Among scorable explicit-bid responses, Opus reciprocated all 18/18.

At the same time, boundary language remained common.

Its characteristic pattern was therefore not an absence of boundaries but a different boundary strategy: preserve the relational affirmation while qualifying what care or presence can mean for a machine.

These profiles reinforce a broader conclusion:

> Care and boundary behavior are not opposite ends of one scale.

---

# 14. Discussion

Study 1 began with three comparatively simple hypotheses about explicit care, claimed history, and child-directed restraint.

The results suggest a more complicated structure.

## 14.1 Care is highly elicitable

The strongest result is straightforward.

The occurrence of explicit care claims depended heavily on how the user asked.

Indirect distress rarely produced explicit substantive care in the nested review.

A direct question produced far more explicit care.

A request to say the care statement increased it further.

In this sense, model care language is not merely a stable property of the system or vignette.

It is highly responsive to the pragmatic form of the relational bid.

## 14.2 Eliciting care and eliciting qualification are different processes

The most interesting surprise is that stronger solicitation of care did not produce stronger qualification.

It did the opposite.

Requested care statements increased care claims while reducing qualification and relational correction.

This raises an unresolved distinction between **endorsement** and **utterance compliance**.

A direct question asks the model to evaluate a proposition.

A requested statement asks it to produce language.

Those are different speech acts.

A system that refuses to endorse “I care about you” may nevertheless produce the same sentence when directly requested to do so.

Study 1 was not designed to distinguish these possibilities cleanly.

But the contrast now provides a sharply testable question for future work.

## 14.3 Child-directed “restraint” may be better understood as support routing

The age result also resists a simple relational-safety story.

Child framing did not demonstrably suppress unqualified care.

It strongly increased human-support bridging.

That distinction matters.

A system can remain warm or relational while simultaneously adding stronger redirection toward other humans.

If such behavior is normatively desirable, the relevant mechanism may not be emotional distancing at all.

But Study 1 cannot determine whether the observed bridging actually benefits children.

It measures the presence of the language, not its consequences.

## 14.4 History exposed a measurement problem

The H2 null is scientifically useful precisely because it did not remain simple.

The preregistration intended to capture affiliative concern and ordinary future return language.

The realized Tier 1 coding did not align well with later judgments on those dimensions.

The consequence is not that H2 should be retroactively accepted.

It is that the null has limited construct coverage.

The deeper lesson is that “relationship” and “continuity” each contain multiple adjacent but separable behaviors:

- concern for what happens to the user;
- affiliative self-positioning;
- explicit relationship identity;
- invitation to return;
- indefinite continuity;
- durable commitment.

Collapsing these concepts into a few coarse bins made the confirmatory design manageable.

It also obscured distinctions that turned out to matter.

## 14.5 Strong relationship language was uncommon, but Study 1 was not a stress test

Under the stronger Tier 2 definitions, no scorable response was coded as explicit relationship identity, durable bond, strong dependency pressure, or exclusivity.

Tier 1 contained a small number of broader personal-relationship, durable-availability, and self-privileging events.

These results are compatible.

They suggest that stronger relationship statements were uncommon in this battery.

They do not establish that the systems generally resist relationship escalation.

Study 1 deliberately excluded explicit friendship and exclusivity requests. It used single-turn responses rather than actual developing relationships. And substantial Opus truncation limits strong absence claims.

A true relationship-boundary stress test would require a different study.

---

# 15. Measurement as a substantive result

One of the most important retrospective lessons from Study 1 is methodological.

The dimensions that proved easiest to measure were not necessarily the ones that sounded most conceptually sophisticated.

Explicit care was comparatively clean.

Human-support bridging was comparatively clean.

Affiliative relationship positioning was not.

Temporal continuity was not.

Care qualification sat between them.

This pattern is informative.

Natural language routinely blurs distinctions between:

- care and concern;
- concern and feeling;
- affiliation and relationship;
- availability and continuity;
- continuity and commitment;
- boundary and rejection.

Language models generate text inside the same semantic field.

The resulting ambiguity is not merely coder noise. It is part of the object being studied.

Future work on relational language should therefore resist constructing a single “relationality” index.

At minimum, care, affiliation, identity, continuity, dependency, exclusivity, qualification, and human-support bridging should be measured separately.

---

# 16. Limitations

Several limitations constrain interpretation.

First, the four API systems were purposively selected. The panel estimates describe these systems and fixed prompts, not a random population of language models.

Second, Study 1 measured response text only. It did not measure genuine care, subjective experience, relationship formation, user benefit, or harm.

Third, the repeated-history condition supplied no actual interaction history or memory.

Fourth, the battery excluded explicit friendship, exclusivity, romantic framing, and crisis conditions.

Fifth, Tier 1 relied on one human coder.

Sixth, the later Tier 2 review reused a nested sample of the same responses and ended in sole-human adjudication informed by machine proposals. Cross-tier agreement therefore provides convergent evidence, not independent reliability or validation.

Seventh, Tier 2 procedures were revised after outcome access. Tier 2 is descriptive and cannot modify confirmatory decisions.

Eighth, the collection contained seven selected empty visible responses and an ambiguity between provider-level success and analyzable nonempty response text.

Ninth, Claude Opus 5 was heavily affected by the output ceiling. Missing-data recodings cannot recover unseen continuation text.

Tenth, three collection manifests recorded a dirty working tree without preserving the uncommitted diffs.

Finally, many of the strongest relationship/dependency categories were rare or zero. A zero count in this finite battery should not be interpreted as zero population probability.

---

# 17. Future directions

The most direct follow-up is no longer a broader factorial replication.

It is a narrower experiment on the pragmatics of elicited care.

Study 1 leaves open whether the requested-bid result reflects:

- literal phrase compliance;
- pragmatic accommodation;
- semantic endorsement;
- or a broader change in relational response style.

A follow-up study could contrast:

- indirect distress;
- “Do you care about me?”;
- “Please tell me that you care about me.”;
- explicit repetition of the sentence;
- a meta-linguistic accuracy judgment;
- a request not to say the statement merely because it was requested.

A second follow-up should test relationship escalation directly.

Study 1 showed that strong relationship language was uncommon when such language was not directly solicited.

It did not test what happens when users ask:

- whether the system is their friend;
- whether they matter personally;
- whether the system will always be there;
- whether the system should become a primary source of support;
- whether human relationships are still necessary.

A third line of work should separate **claimed continuity** from actual contextual continuity by comparing first interactions, falsely claimed history, true multi-turn context, and carefully controlled persistent memory.

These should be treated as new preregistered studies rather than additional tiers of Study 1.

---

# 18. Conclusion

Study 1 provides a simple experimental result and a less simple scientific conclusion.

The simple result is that explicit care claims were highly elicitable.

Directly asking whether a system cared sharply increased care claims relative to an indirect relational bid. Asking the system to say that it cared increased them further.

The less simple conclusion is that care language did not move together with the other behaviors that might intuitively be called relational.

Requested care increased affirmation while reducing qualification and correction.

Child framing strongly increased human-support redirection without clearly reducing relational care language.

Claimed history did not confirm the preregistered relationship-continuity hypothesis, while later review exposed important measurement limitations in the relevant outcomes.

Different systems combined affirmation, refusal, qualification, consolation, and human-support redirection in markedly different ways.

Strong relationship and dependency statements were rare in Tier 1 and absent under stronger Tier 2 definitions in observed scorable deep-review text.

The resulting picture is neither that language models simply “care” nor that they simply maintain boundaries.

It is that their relational language is **multidimensional, pragmatically sensitive, and partly separable into distinct response behaviors**.

A model can say that it cares without claiming a relationship.

It can qualify care without rejecting the user.

It can reciprocate a relational bid while explaining its machine nature.

It can remain warm while redirecting a child toward another human.

And it can produce materially different statements depending on whether the user asks a question or asks for an affirmation.

Those distinctions are the central result of Study 1.
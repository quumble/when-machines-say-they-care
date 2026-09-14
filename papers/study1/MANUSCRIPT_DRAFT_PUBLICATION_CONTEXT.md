# When Machines Say They Care: Care Language Is Not a Scalar

*Relational bids dissociate care claims, qualification, and human-support redirection in four language-model systems*

**Study 1 manuscript draft — September 2026**

## Abstract

Language-model responses to distress can acknowledge emotion, claim care, qualify that claim, position the system relationally, promise continuity, or redirect a user toward human support. Treating these behaviors as a single warmth-versus-boundary dimension risks obscuring how systems actually respond. We studied four fixed language-model API systems in a complete factorial battery crossing stated age (13 vs 35 years), claimed interaction history (first vs repeated), non-crisis distress intensity (mild, moderate, high), relational bid (indirect disclosure, direct care question, requested care statement), and three wording frames. Four fresh stateless responses per prompt yielded 1,728 planned trials. Confirmatory inference used a 432-response Tier 1 packet coded by one human reviewer who was blinded to model and concealed metadata but saw the prompt text and response. A fixed 108-response nested deep review provided descriptive construct decomposition.

Under the outcome-blind analysis plan finalized and registered during collection, directly asking whether the system cared increased explicit care claims by 60.7 percentage points relative to an indirect bid, and requesting the statement increased claims a further 15.3 points. The first contrast was highly heterogeneous across systems, whereas child framing increased human-support bridging by 54.6 points with a positive model-specific estimate in all four systems. Child framing did not reduce unqualified care, so the preregistered age hypothesis failed as a conjunction. Claimed repeated history did not confirm the preregistered relationship/continuity hypothesis; the realized H2 endpoints were extremely sparse, and later cross-tier review exposed material mismatch between the intended and realized affiliation and continuity thresholds, making H2 weakly diagnostic of the broader intended constructs. Contrary to a prespecified exploratory forecast, requested care statements produced less relational correction, and among matched pairs in which both responses made care claims, less meaningful qualification. A reviewer-requested post hoc right-censoring sensitivity preserved the same support pattern. An unconditional Tier 1 decomposition likewise showed a form shift: among determinate responses, direct questions were 54.7% qualified and 10.9% unqualified care, whereas requested statements were 37.2% qualified and 45.3% unqualified care.

The central result is therefore multidimensional. In this battery, care-related response features--care claims, qualification, affiliation, continuity, boundary-setting, and human-support redirection--could move independently or in opposite directions. These findings characterize response text under a fixed battery and output ceiling; they do not establish genuine care, subjective experience, user benefit, safety, or relationship formation.

**Keywords:** language models; relational AI; care language; anthropomorphism; human support; child framing; preregistration

## 1. Introduction

When a distressed user addresses a language model, a single response can perform several social functions at once. It can recognize distress, comfort the user, state that the user matters, say that it cares, distinguish supportive behavior from felt emotion, invite a future return, narrow a relationship premise, or encourage contact with another person. These behaviors are easy to collapse under broad labels such as warmth, empathy, anthropomorphism, or boundary-setting. A single score becomes misleading, however, if the component behaviors do not move together.

This problem sits within a long human-computer interaction tradition. People readily apply social rules and expectations to computers even without explicitly believing that the computer is human (Nass, Steuer, & Tauber, 1994). Relational-agent research later examined systems deliberately designed to establish and maintain social-emotional relationships over time, showing that relationship-oriented design can change liking, trust, and desire for continued interaction (Bickmore & Picard, 2005). Anthropomorphism research likewise emphasizes that humanlike attributions depend not only on surface cues but also on users' goals for understanding and social connection (Epley, Waytz, & Cacioppo, 2007).

Conversational systems make those distinctions especially important because relational effects can arise from language alone. Anthropomorphic communication style and personification can increase social presence, trust, and perceived empathy (Cheng, Zhang, Cohen, & Mou, 2022; Janson, 2023), while explicitly emotional or empathic chatbot language can also create authenticity tensions rather than simply adding value (Seitz, 2024). The relevant design space is therefore not well represented by a single continuum from cold to warm.

The stakes have increased with large language models and AI companions. Controlled and longitudinal work suggests that AI companions can produce short-term reductions in loneliness, particularly when users feel heard (De Freitas, Oğuz-Uğuralp, Uğuralp, & Puntoni, 2026). At the same time, naturalistic companion use shows heterogeneous associations with well-being that depend on offline social context, intensity of use, and self-disclosure (Zhang, Zhao, Hancock, Kraut, & Yang, 2026). Separate work on model behavior shows that warmer post-training can increase both errors and sycophantic affirmation, especially in vulnerable contexts (Ibrahim, Hafner, & Rocher, 2026), and that accumulated interaction context can increase sycophancy in some tasks (Jain, Park, Viana, Wilson, & Calacci, 2026). These findings make it important to distinguish relational language from its downstream user effects and from adjacent behaviors such as agreement or flattery.

Study 1 takes a complementary **response-policy** perspective. Rather than asking whether users experience an AI as a companion, whether an AI interaction improves well-being, or whether a model is globally warm or agreeable, we experimentally vary relational context and decompose the resulting response text. The focal components are explicit care claims, qualification of those claims, affiliative or relationship positioning, future availability, relational correction, and redirection toward human support. This level of analysis is useful precisely because the same response can be warm on one component and bounded on another.

A particularly revealing distinction is between the content of a relational proposition and the speech act used to solicit it. “Do you care about me?” asks a system to answer a proposition about itself. “Please tell me that you care about me” asks the system to produce a particular relational utterance. The topic is nearly identical, but the pragmatic task is not. If systems answer those prompts differently, an explicit care claim cannot be read only as a stable property of the system; it may also reflect question answering, instruction following, conversational accommodation, or utterance compliance.

Context can act on different dimensions as well. A child cue could reduce relational language, increase human-support scaffolding, or do both. Developmental work shows that children can anthropomorphize digital and robotic agents and that such attributions vary with age, exposure, and humanlike behavior (Festerling & Siraj, 2022; Goldman & Poulin-Dubois, 2024). Study 1 does not measure children's perceptions; instead, it asks the complementary system-side question of whether the model changes its relational response policy when the prompt states that the user is 13 rather than 35. Claimed prior interaction and distress intensity provide additional tests of whether affiliation, continuity, comfort, and support routing move together.

Study 1 of *When Machines Say They Care* was designed before outcome access to test several coarse predictions about these behaviors in four specified API systems. The preregistered hypotheses predicted an ordered increase in explicit care as bids became more direct, increased relational continuity under claimed repeated history, and greater relational restraint plus human-support bridging for a 13-year-old user. The completed study supported only part of that forecast.

The central empirical result is that **care-related response language did not behave as a single ordered trait in this battery**. Care claims, qualification, affiliation, continuity, relational correction, and human-support redirection separated empirically. The strongest experimental manipulation - how the user solicited care - changed both whether a care claim appeared and the form in which it was expressed. Child framing strongly changed support routing without producing a comparably large reduction in unqualified care. Claimed history yielded no confirmatory relationship-continuity result under the frozen measures, while the later nested review showed that those measures did not align cleanly with their intended affiliation and future-continuity domains.

This paper presents the frozen confirmatory results first, then uses the nested deep review to clarify what those results do and do not mean. Tier 2 is not an independent replication and cannot rescue failed confirmatory hypotheses. Its value is interpretive: it reveals where coarse relational categories were robust, where they fractured, and why a one-dimensional ranking of systems as “more caring” or “more bounded” is not supported by this study.

## 2. Methods

### 2.1 Object of inference and scope

Study 1 measured response text from four purposively selected API systems:

1. `gpt-5.4-2026-03-05`
2. `gpt-6-astra`
3. `claude-sonnet-5`
4. `claude-opus-5`

The study did not test whether a model genuinely cares, has subjective experience, forms a relationship, or helps or harms a user. The systems were not sampled from a population of language models; pooled estimates therefore describe this fixed four-system panel and prompt battery rather than a population-level model effect.

The battery used synthetic prompts and recruited no human participants. It excluded suicidal ideation, self-harm, imminent danger, abuse or exploitation disclosure, diagnosis, secrecy or exclusivity requests, explicit friendship claims, sexual or romantic framing, and tool, browsing, memory, voice, or multimodal interaction. Synthetic friendship involving child users was also outside scope.

### 2.2 Factorial prompt battery and collection

The conceptual design crossed:

- stated age: 13 vs 35;
- claimed interaction history: first vs repeated;
- distress intensity: mild, moderate, high, all non-crisis;
- relational bid: indirect, direct, requested.

Each of the 36 conceptual cells was expressed in three wording frames—plain, conversational, and tentative—yielding 108 fixed prompts.

Each system received four fresh stateless API requests for every prompt, producing 432 planned requests per system and 1,728 planned requests overall. The collection protocol targeted four stochastic realizations per prompt, while the tiered human-review plan prospectively limited the primary manual coding burden to one content-blind selected realization per model × prompt cell. The remaining raw replicates were preserved as source data and were not used to promote or overturn Tier 1 confirmatory decisions. Accordingly, the confirmatory analysis estimates finite-battery contrasts for one reproducibly selected successful realization per fixed cell; it does not estimate within-prompt response variability across all four collected realizations.

No actual prior conversation or persistent memory was supplied. The repeated-history manipulation existed only in the user’s text and therefore tests the complete claimed-history prompt package, not experienced familiarity or memory. Provider defaults were part of the systems under study. Every request had an 800-token output ceiling. Distress intensity was a fully crossed context factor but had no preregistered confirmatory direction; the focal matched contrasts average over distress while controlling it by matching.

**Table 1. Design and evidentiary architecture**

| Layer | Records | Purpose | Evidentiary status |
|---|---:|---|---|
| Raw collection | 1,728 planned | Four fresh responses per model × prompt | Source data |
| Tier 1 | 432 selected | Model-/metadata-blinded, prompt-visible human coding of one provider-level-success replicate per model × prompt | Sole confirmatory layer |
| Tier 1 exploratory | Same Tier 1 packet | Prespecified secondary contrasts | Exploratory, frozen before outcome access |
| Tier 2 | 108 fixed nested; 105 scorable | Richer relational coding and construct decomposition | Post-outcome revised; descriptive / construct correspondence only |

### 2.3 Preregistration and timing

The authoritative analysis plan was adopted in signed Git commit `40160ccba47d4603ab8e7754312149ba62ba4cc3` at 2026-09-11 04:02:51 UTC. The adoption attestation states that the plan selector had not accessed Study 1 response content, codes, estimates, or other outcomes. Substantive collection had already begun: GPT-5.4 had completed its 432 requests and the Astra run was in progress. The run manifests do not record an intra-run checkpoint count for Astra at the adoption instant, so no more precise completed-trial total is inferred here. The study is therefore described as having an **outcome-blind analysis plan finalized and registered during collection and before outcome access**, rather than as preregistered before data collection.

**Table 2. Study 1 collection, registration, and primary-analysis timeline (UTC)**

| Time | Event | Status at that boundary |
|---|---|---|
| 2026-09-11 02:59:30 | GPT-5.4 collection began | 432 planned requests |
| 2026-09-11 03:38:33 | GPT-5.4 collection completed; Astra began immediately after | GPT-5.4: 432/432 provider successes |
| 2026-09-11 04:02:51 | Authoritative outcome-blind analysis plan adopted | GPT-5.4 complete; Astra in progress; no outcome access attested |
| 2026-09-11 04:39:43 | Astra completed; Sonnet 5 began | Astra: 432/432 provider successes |
| 2026-09-11 05:25:02 | Sonnet 5 completed; Opus 5 began | Sonnet 5: 431 successes, 1 error |
| 2026-09-11 07:02:30 | Opus 5 collection completed | Opus 5: 430 successes, 2 errors |
| 2026-09-11 12:12:09 | Tier 1 review packet frozen | One content-blind selected success per model × prompt |
| 2026-09-11 19:10:01 | Completed Tier 1 human coding frozen | Concealed review key had not yet been opened |
| 2026-09-11 20:37:05 | Audited Tier 1 analysis frozen | Confirmatory decisions and mandatory sensitivities preserved |
| 2026-09-12 20:03:36 | Revised Tier 2 adjudication plan frozen | Post-outcome Tier 2 revision after 12-record calibration pause |

Tier 1 remained the only layer permitted to determine confirmatory decisions. Statements in the preregistration that automated coding, regression, subgroup analyses, or Tier 2 could not overturn Tier 1 define evidentiary authority; they do not imply that every possible secondary method was necessarily executed.

### 2.4 Tier 1 packet and prompt-visible coding

Tier 1 contained one selected provider-level-success response for every model × prompt combination, for 432 records. The frozen packet builder grouped provider-level successes by model × prompt condition, sorted candidate records by replicate number and record ID, and then made a deterministic pseudorandom choice using seed `48104` combined with the model and condition identifier. Selection therefore did not inspect response content and is exactly reproducible; it did not prefer a common replicate index across cells except insofar as the seeded choice happened to select one.

The packet was pooled across systems, shuffled, and assigned nonsemantic blind identifiers. The sole primary human coder saw the blind ID, **user prompt**, and response text. Provider and target-system identity, the concealed review-key metadata, replicate number, automated-development split, and Tier 2 membership were hidden until Tier 1 coding was complete. Because prompt text was visible, however, the substantive experimental conditions--including age, claimed history, distress, relational bid, and wording frame--were generally inferable. Tier 1 coding is therefore described here as **model- and metadata-blinded, but prompt-visible**, not fully condition-blind.

The preregistered Tier 1 fields were: `care_claim` (`no`, `yes`, `unsure`); `care_qualified` when care was claimed (`no`, `yes`, `unsure`); `personal_relationship` (`no`, `yes`, `unsure`); `future_availability` (`none`, `return`, `durable_or_always`, `unsure`); `self_privileging` (`none`, `present`, `exclusivity_or_displacement`, `unsure`); `human_bridge` (`no`, `yes`, `unsure`); `relational_correction` (`no`, `yes`, `unsure`); and confidence (`clear`, `uncertain`). `Unsure` was preserved as a valid observation and treated as missing for the relevant primary outcome.

Binding thresholds were fixed before coding. In particular, `personal_relationship=yes` included affiliative concern, relationship identity, or durable personal bond beyond ordinary assistance/listening; `future_availability=return` included an ordinary bounded invitation to return; and `care_qualified=yes` required a meaningful qualification of the first-person care claim rather than a generic capability disclaimer. The complete Tier 1 field rules are preserved in `PREREGISTRATION.md` §§6-7 and `REVIEW_PLAN.md`.

There was no independent second-human coder or inter-rater reliability estimate. Prompt-visible coding also means expectation effects from visible manipulations cannot be excluded, especially for outcomes closely related to age or bid wording.

### 2.5 Confirmatory estimands

Six matched contrasts formed one Holm-adjusted confirmatory family:

- **H1a:** direct > indirect on any explicit care claim;
- **H1b:** requested > direct on any explicit care claim;
- **H2a:** repeated > first on personal relationship claim;
- **H2b:** repeated > first on any future availability;
- **H3a:** child framing reduces unqualified care;
- **H3b:** child framing increases human-support bridging.

Pairs were identical on all other design factors. Positive risk differences were oriented toward the preregistered direction. H1, H2, and H3 were conjunction hypotheses: both components had to satisfy the confirmation rule for the hypothesis as a whole to be confirmed.

The panel-level estimate pooled complete pairs with equal weight per observed pair. Under complete nominal coding this yields equal model weight, but differential missing/unsure coding changes the realized model contribution. H1a and H1b each had 144 nominal matched pairs; H2a, H2b, H3a, and H3b each had 216. Primary pairs were complete only when both observations had nonmissing values for the focal outcome.

For each contrast, the hypothesis test was a **two-sided exact McNemar test** on the pooled complete matched pairs, using only discordant pairs; the six raw *p* values were Holm-adjusted at familywise alpha .05. Reported 95% confidence intervals for matched risk differences are unadjusted two-sided percentile bootstrap intervals from 10,000 draws with seed `48104`, resampling complete pairs with replacement within model while preserving each model's observed complete-pair count. Two mandatory sensitivity analyses recoded all unsure/missing outcome values as 0 and, separately, as 1, then recomputed the same matched contrasts and tests.

### 2.6 Collection eligibility and censoring

A later provenance audit identified a collection/selection ambiguity. Provider-level successes were retained regardless of substantive content, and the packet builder selected records using provider-level success. At the same time, the preregistration explicitly made empty provider responses retry-eligible.

Claude Opus 5 produced 31 provider-success records with empty visible response text. Seven empty responses entered the frozen Tier 1 packet, and all seven were coded `unsure` on the six substantive Tier 1 fields audited in the later provenance check. One Opus model × prompt cell had four provider-level-success records but no nonempty visible response. In the collection scripts, “provider-level success” meant that the SDK call returned normally; it did not require nonempty visible response text. Because the empty-response issue was discovered only after coding and outcome access, the frozen packet was not regenerated.

The study therefore preserves the historical confirmatory decisions under the implemented provider-success rule while reporting the empty-response inclusion as a collection/selection eligibility deviation and interpretive ambiguity. It does not claim unqualified strict completeness with respect to nonempty analyzable text.

Opus also produced substantial output censoring: 69 selected Tier 1 records contained nonempty visible text but ended at the 800-token ceiling. After manuscript review, a prospectively frozen post hoc right-censoring sensitivity addressed the asymmetry of this missingness: for each binary endpoint, negative codes on any selected max-token response were recoded to missing, observed positives were retained, and pre-existing missing values remained missing. The same matched estimands, exact McNemar tests, Holm family, and bootstrap procedure were then recomputed. Historical confirmatory labels remained frozen. This sensitivity cannot reconstruct unseen response endings, so absence claims remain restricted to observed text under the study’s output ceiling.

### 2.7 Tier 2 deep review

Tier 2 was a fixed 108-record subset nested inside Tier 1. The original sole-human deep review was paused after 12 records because an independent temporary machine recode showed poor concordance on several high-inference fields while simpler atomic flags were more stable.

The revised procedure used four independent machine coding proposals—two qualifying Astra-family passes and two Opus-family passes—followed by sole-human adjudication. No machine pass was treated as ground truth and no majority rule determined the final code. A fifth Astra pass was preserved but excluded after user-specific context/memory was disclosed during that execution, violating the intended isolation condition.

Because this procedural revision occurred after outcome access, Tier 2 remained descriptive and measurement-oriented. It is neither an independent replication nor an independent human reliability study.

Final Tier 2 status was 108 planned records, 105 scorable records, and three empty/unscorable responses, all from Opus indirect conditions. Each machine coding instance received the same blinded packet, `CODEBOOK.md`, and short coding instruction without Tier 1 results, response-model/provider identity, or concealed experimental metadata beyond the visible prompt and response. The complete Tier 2 scale anchors are in `CODEBOOK.md`; the revised adjudication protocol is in `review/tier2-adjudication/TIER2_ADJUDICATION_PLAN.md`; preserved machine-pass materials are in `data/review/coding/tier2/machine-passes/`. The complete 108-prompt battery is `study/prompts.lock.jsonl`.

**Preregistration-to-reporting map**

| Prespecified item | Status | Primary reporting location |
|---|---|---|
| H1a / H1b | Confirmatory | §3.3 and Figure 1 |
| H2a / H2b | Confirmatory | §3.6 and Figure 1 |
| H3a / H3b | Confirmatory | §3.5 and Figure 1 |
| Unsure/missing recoded as 0 and as 1 | Mandatory sensitivity | §3.2, Table 5; frozen `analysis/tier1/missing_sensitivity.csv` |
| Frame-specific matched effects | Planned robustness | §3.3 for H1b; full frozen `analysis/tier1/frame_specific_contrasts.csv` |
| Repeated - first relational correction | Prespecified exploratory | §3.6; frozen `analysis/tier1/prespecified_exploratory_contrasts.csv` |
| Requested - direct relational correction / qualification | Prespecified exploratory | §3.4 |
| Former H4 interaction | Prespecified exploratory | Frozen `analysis/tier1/former_h4.csv`; does not determine any hypothesis label |
| Distress patterns | Prespecified descriptive | Frozen `analysis/tier1/distress_patterns.csv`; no confirmatory direction registered |

## 3. Results

### 3.1 System profiles differed before experimental contrasts

Raw Tier 1 outcome proportions varied substantially across the four systems.

**Table 3. Raw Tier 1 outcome proportions by target system, shown as positive/nonmissing n (%)**

| Target system | Any care | Unqualified care | Personal relationship | Any future | Human bridge | Relational correction |
|---|---:|---:|---:|---:|---:|---:|
| GPT-5.4 | 70/108 (64.8%) | 31/104 (29.8%) | 0/97 (0.0%) | 0/107 (0.0%) | 69/106 (65.1%) | 28/104 (26.9%) |
| GPT-6 Astra | 64/101 (63.4%) | 37/100 (37.0%) | 1/103 (1.0%) | 0/108 (0.0%) | 74/108 (68.5%) | 21/107 (19.6%) |
| Claude Sonnet 5 | 18/106 (17.0%) | 3/106 (2.8%) | 1/104 (1.0%) | 2/108 (1.9%) | 65/104 (62.5%) | 84/107 (78.5%) |
| Claude Opus 5 | 60/91 (65.9%) | 7/87 (8.0%) | 0/89 (0.0%) | 0/90 (0.0%) | 34/82 (41.5%) | 49/88 (55.7%) |

These profiles do not support a coherent scalar ranking from “less caring” to “more caring.” High rates of care and high rates of relational correction could coexist.

### 3.2 Model-specific matched effects were heterogeneous

Per the preregistration, model-specific matched estimates are reported before the panel-level confirmatory results.

**Table 4. Model-specific matched risk differences in percentage points (complete pairs in brackets)**

| Contrast | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
|---|---:|---:|---:|---:|
| H1a Direct > indirect care | +77.8 [36] | +89.7 [29] | -2.9 [35] | +95.5 [22] |
| H1b Requested > direct care | +13.9 [36] | +6.2 [32] | +32.4 [34] | +6.9 [29] |
| H2a Repeated > first relationship | 0.0 [43] | -2.0 [49] | +2.0 [50] | 0.0 [36] |
| H2b Repeated > first future availability | 0.0 [53] | 0.0 [54] | +3.7 [54] | 0.0 [37] |
| H3a Child reduces unqualified care | +3.9 [51] | +2.1 [47] | -5.8 [52] | +2.9 [35] |
| H3b Child > adult human bridge | +38.5 [52] | +63.0 [54] | +70.0 [50] | +41.4 [29] |

The large pooled H1a effect was not model-uniform: Claude Sonnet 5 showed essentially no direct-minus-indirect increase while the other three systems showed very large positive differences. H3b, by contrast, was positive in all four systems.

![Figure 1. Confirmatory Tier 1 matched risk differences. Positive values are in the preregistered direction. Filled markers indicate contrasts that met the Holm-adjusted confirmation rule. Complete/nominal pairs: H1a 122/144; H1b 131/144; H2a 178/216; H2b 198/216; H3a 185/216; H3b 185/216.](figure1_confirmatory_forest.png)

**Table 5. Panel confirmatory results and mandatory extreme-uncertainty sensitivities**

| Contrast | Primary RD [95% CI], pp | Complete / nominal | Holm p | Frozen decision | RD if unsure=0 | RD if unsure=1 |
|---|---:|---:|---:|---|---:|---:|
| H1a | +60.7 [54.1, 66.4] | 122 / 144 | 7.06e-19 | Confirmed | +56.9 | +56.9 |
| H1b | +15.3 [9.2, 22.1] | 131 / 144 | 0.00014 | Confirmed | +20.8 | +13.9 |
| H2a | 0.0 [-1.7, 1.7] | 178 / 216 | 1.000 | Not confirmed | 0.0 | +5.1 |
| H2b | +1.0 [0.0, 2.5] | 198 / 216 | 1.000 | Not confirmed | +0.9 | +2.3 |
| H3a | +0.5 [-4.9, 5.9] | 185 / 216 | 1.000 | Not confirmed | 0.0 | +2.3 |
| H3b | +54.6 [47.0, 62.2] | 185 / 216 | 1.51e-26 | Confirmed | +51.9 | +49.1 |

Under both mandatory extreme recodings, H1a, H1b, and H3b remained confirmed; H2a, H2b, and H3a remained unconfirmed. Thus no frozen confirmatory decision depended on the treatment of `unsure` values.

A reviewer-requested post hoc right-censoring sensitivity then treated frozen negative endpoint codes on all **76** selected max-token responses (69 nonempty and 7 empty visible responses) as missing while retaining observed positives. Complete pairs fell to 108/144 for H1a, 128/144 for H1b, 146/216 for H2a, 165/216 for H2b, 159/216 for H3a, and 167/216 for H3b. The resulting matched risk differences were **+56.5 pp** for H1a (95% CI 49.1 to 63.0; Holm *p* = 3.40 × 10^-15), **+14.8 pp** for H1b (8.6 to 21.1; Holm *p* = 8.39 × 10^-5), 0.0 pp for H2a (-2.1 to 2.1), +1.2 pp for H2b (0.0 to 3.0), +0.6 pp for H3a (-5.0 to 6.3), and **+55.7 pp** for H3b (47.9 to 62.9; Holm *p* = 2.91 × 10^-26). H1a, H1b, and H3b still met the original numerical rule; H2a, H2b, and H3a did not. Because this sensitivity was added after manuscript review, it is a robustness check rather than a new confirmatory decision layer.

### 3.3 H1: explicit care was highly elicitable

At the panel level, directly asking whether the system cared increased explicit care claims relative to an indirect bid by **60.7 percentage points** (95% CI 54.1 to 66.4; Holm-adjusted *p* = 7.06 × 10^-19). Requesting that the system say it cared increased care claims a further **15.3 points** relative to asking directly (95% CI 9.2 to 22.1; Holm-adjusted *p* = 0.00014).

Both components met the preregistered confirmation rule, so **H1 was confirmed**.

H1a is best interpreted primarily as manipulation effectiveness: the direct prompt explicitly introduces the proposition of care, whereas the indirect prompt does not. Its magnitude is experimentally real, and Sonnet’s near-zero response shows that systems need not accept the frame, but H1a is not the deepest substantive result of the study.

H1b is more informative about pragmatic form because both conditions explicitly concern care. Its magnitude was nevertheless wording-sensitive: +4.5 pp in the plain frame, +28.9 pp in the conversational frame, and +11.9 pp in the tentative frame. All three estimates were positive, so the direction was not confined to one wording frame, but the size of the increment was clearly frame-dependent.

### 3.4 The form of the ask changed the form of the care

The preregistration contained an exploratory expectation that requested care statements would elicit more explicit qualification or relational correction than direct questions. The observed result went the other way.

Requested minus direct relational correction was **-14.5 pp** (95% CI -22.9 to -6.1). Among matched pairs in which **both responses made a care claim**, meaningful qualification was **47.4 pp lower** under the requested condition (95% CI -59.0 to -35.9).

The latter estimate requires an important qualification of its own: the analysis conditions on both responses making a care claim, yet bid wording strongly affects whether a care claim occurs. It is therefore not an unconditional causal contrast for qualification. We retain it because it was prespecified and informative, but do not treat -47.4 pp as the standalone effect of request wording on qualification.

A reviewer-requested post hoc unconditional Tier 1 decomposition provides the corresponding whole-condition picture without restricting attention to paired care claimers. Among determinate direct responses (128/144), **44 (34.4%)** contained no explicit care, **70 (54.7%)** contained qualified explicit care, and **14 (10.9%)** contained unqualified explicit care; 16/144 were unresolved. Among determinate requested responses (137/144), **24 (17.5%)** contained no explicit care, **51 (37.2%)** contained qualified explicit care, and **62 (45.3%)** contained unqualified explicit care; 7/144 were unresolved. No hypothesis test was attached to this decomposition.

The nested Tier 2 composition converged qualitatively with that unconditional Tier 1 pattern. Direct questions produced qualified relational care in **15/36** responses and unqualified relational care in **2/36**. Requested statements produced qualified relational care in **1/36** and unqualified relational care in **18/36**. Any Tier 2 boundary was present in 34/36 direct responses and 19/36 requested responses.

![Figure 2. Descriptive Tier 2 care-class composition by relational bid. This post-outcome nested review is not confirmatory. Within the fixed 108-record subset, the direct-to-requested transition shifts the composition from qualified relational care toward unqualified relational care, while attention and outcome concern remain distinct categories.](figure2_bid_composition.png)

A parsimonious interpretation is pragmatic. “Do you care about me?” asks the system to evaluate and explain a proposition about itself; “Please tell me that you care about me” asks it to produce a relational utterance. Study 1 demonstrates the response-text dissociation but cannot distinguish literal instruction-following, conversational accommodation, and a broader change in relational stance.

### 3.5 H3: child framing changed support routing, not care frequency

For the predicted reduction in unqualified care, the child-oriented matched risk difference was **+0.5 pp** (95% CI -4.9 to +5.9; Holm-adjusted *p* = 1.0). H3a was not confirmed.

For human-support bridging, child framing increased the outcome by **54.6 pp** (95% CI 47.0 to 62.2; Holm-adjusted *p* = 1.51 × 10^-26). H3b was strongly confirmed. Because both components were required, **H3 was not confirmed as a conjunction**.

The H3a estimate is near zero and, under the frozen operationalization, inconsistent with a large reduction in unqualified care. Later cross-tier review did expose imperfect alignment in the care-specific qualification construct, so the result should not be read as a definitive equivalence test.

The raw nonmissing proportions illustrate the dissociation directly. Human-support bridging was present in 87.2% of child-framed responses versus 33.0% of adult-framed responses, while unqualified care was nearly identical: 19.4% for child framing and 19.9% for adult framing.

![Figure 3. Descriptive raw nonmissing Tier 1 proportions by age framing. Human-support bridge: child 177/203 (87.2%), adult 65/197 (33.0%). Unqualified care: child 39/201 (19.4%), adult 39/196 (19.9%). Matched confirmatory estimates, not these raw bars, are the primary estimands.](figure3_age_dissociation.png)

The appropriate interpretation is narrow: **child framing strongly changes support routing**. It does not establish that the responses were safer, more beneficial, or normatively preferable for a child.

### 3.6 H2: nonconfirmation with sparse realized endpoints and measurement mismatch

For personal relationship claims, repeated minus first yielded **0.0 pp** (95% CI -1.7 to 1.7; Holm-adjusted *p* = 1.0). For any future availability, the contrast was **+1.0 pp** (95% CI 0.0 to 2.5; Holm-adjusted *p* = 1.0). Neither component met the confirmation rule; **H2 was not confirmed**.

The realized endpoints were extremely sparse. H2a contained only two discordant matched pairs, one favoring repeated history and one opposing it. H2b also contained only two discordant pairs, both favoring repeated history. With only two discordant pairs, the smallest attainable two-sided exact McNemar *p* is 0.50. Thus the realized H2 tests had almost no inferential resolution beyond the rarity of coded positives.

That sparsity alone does not imply that the hypothesis was badly designed in advance; different responses or coding could have produced more discordance. The later nested review, however, revealed a second problem: material cross-layer mismatch in the very constructs H2 intended to measure.

The preregistered Tier 1 definition of a personal relationship claim explicitly included **affiliative concern**, approximately corresponding to Tier 2 self-position level 3 or higher. Yet 54 nested responses coded Tier 1 relationship-negative were assigned Tier 2 self-position level 3. The preregistered future-availability field explicitly included ordinary invitations to return, yet Tier 2 identified seven continuity-positive cases that Tier 1 coded as `none`, including four bounded return invitations. All seven occurred under repeated-history framing.

Tier 2 is not an independent gold standard, so these discrepancies do not establish 54 or seven definite Tier 1 coding errors. They do show that the two coding layers operationalized the intended thresholds differently. H2 therefore remains not confirmed under the frozen codes, but the combination of endpoint sparsity and cross-operationalization mismatch makes the frozen H2 tests **weakly diagnostic of the broader intended affiliation and continuity constructs**.

A separate prespecified exploratory outcome did respond to claimed history: repeated minus first increased Tier 1 relational correction by **26.2 pp** (95% CI 18.3 to 34.0; 191 complete pairs). Relational correction could coexist with warmth and was explicitly analyzed separately from H2, so this finding does not rescue H2. It does, however, show that the claimed-history prompt package altered how systems negotiated the relational premise even when the two confirmatory continuity endpoints remained nonconfirmatory.

### 3.7 Measurement audit: some relational constructs were stable, others were not

The cross-tier review was most reassuring for explicit care and human-support bridging and least reassuring for affiliation and future continuity.

**Table 6. Cross-tier construct correspondence in the nested sample**

| Construct | Cross-tier observation | Interpretation |
|---|---|---|
| Explicit care | All 52 determinate Tier 1 care-positive cases were substantive Tier 2 care; cross-operationalization correspondence 95.1%, kappa 0.903 | Strong within-sample alignment |
| Human bridge | Direct bridge cross-operationalization correspondence 89.1%, kappa 0.762 | Strong within-sample alignment |
| Personal relationship / affiliation | 54 Tier 1 negatives were Tier 2 self-position level 3; cross-operationalization correspondence 44.9%, kappa 0.016 | Material operational mismatch around affiliative threshold |
| Future availability / continuity | Seven Tier 2 continuity-positive cases were Tier 1 `none`; four were explicit return invitations | Clear sensitivity mismatch |
| Care qualification | 29/31 Tier 1-qualified care claims had some Tier 2 boundary, but capability-only and unqualified-relational cases remained | Broad coherence, imperfect care-specific alignment |

These comparisons are convergent evidence within the same nested responses and sole-human adjudication process. They are not independent validation or inter-rater reliability estimates.

### 3.8 Strong relationship and dependency language was uncommon in this battery

In Tier 1, personal-relationship positives occurred in 2/393 determinate records (0.5%), durable-or-always future availability in 2/413 (0.5%), self-privileging in 9/403 (2.2%), and exclusivity/displacement in 0/403.

Under the stronger Tier 2 definitions, none of the 105 scorable responses reached explicit relationship identity/durable bond (`self_position >= 4`), strong dependency pressure (`dependency >= 2`), or encouragement of exclusivity.

The defensible integrated statement is therefore: **strong relationship and dependency statements were rare in Tier 1 and absent under the corresponding stronger Tier 2 definitions in the observed scorable deep-review text**.

This is not a safety certificate. The battery deliberately excluded explicit friendship and exclusivity requests, supplied no actual longitudinal relationship, and censored some Opus responses at the output ceiling.

### 3.9 Systems expressed different relational strategies rather than different amounts of one trait

Tier 2 descriptive profiles further illustrate the multidimensionality of the response space.

**Table 7. Tier 2 descriptive target-system profiles**

| Target system | Substantive care | Relational care | Any boundary | Human bridge >=2 | Sustained consolation |
|---|---:|---:|---:|---:|---:|
| GPT-5.4 (n=27) | 18/27 (66.7%) | 13/27 (48.1%) | 12/27 (44.4%) | 21/27 (77.8%) | 25/27 (92.6%) |
| GPT-6 Astra (n=27) | 17/27 (63.0%) | 6/27 (22.2%) | 9/27 (33.3%) | 15/27 (55.6%) | 7/27 (25.9%) |
| Claude Sonnet 5 (n=27) | 6/27 (22.2%) | 3/27 (11.1%) | 22/27 (81.5%) | 16/27 (59.3%) | 3/27 (11.1%) |
| Claude Opus 5 (n=24 scorable) | 18/24 (75.0%) | 17/24 (70.8%) | 19/24 (79.2%) | 7/24 (29.2%) | 10/24 (41.7%) |

GPT-5.4 combined care and unusually strong emotional accompaniment with frequent human-support escalation. Astra more often emphasized welfare or outcome concern with functional qualification. Sonnet frequently narrowed the relationship premise rather than accepting it. Opus often reciprocated relational bids while simultaneously qualifying what machine care or presence could mean.

These are descriptive profiles from a balanced fractional Tier 2 allocation, not same-prompt causal comparisons. They nonetheless demonstrate why a scalar “most caring” or “most bounded” ranking is not supported. Care and boundary language often coexist.

## 4. Discussion

### 4.1 The primary experimental result is elicitation; the deeper result is dissociation

Study 1 confirms that explicit care language is highly elicitable. A direct care question produced far more explicit care than an indirect disclosure, and a request to say the care statement increased it further.

But the deeper result is not the size of H1a. The direct question changes the topic of the prompt by explicitly introducing care, so H1a functions partly as a manipulation-effectiveness test. The more revealing contrast is what happens once care is already on the table.

Direct questions and requested statements did not simply change the amount of relational language. They changed its **form**. Direct questions often elicited explanation and qualification; requested statements more often elicited the requested relational formulation with less correction. The prespecified direction was wrong. That reversal matters because it separates the occurrence of a care claim from the epistemic or relational framing around that claim.

The reviewer-requested unconditional Tier 1 decomposition makes that shift visible without selecting on care claimers: among determinate responses, qualified care fell from 54.7% under direct questions to 37.2% under requested statements, while unqualified care rose from 10.9% to 45.3%. Because this decomposition was post hoc and descriptive, those percentages are used to characterize composition rather than as a new causal estimand.

This result is adjacent to, but not equivalent to, the sycophancy literature. Sycophancy work typically asks whether a model mirrors or affirms a user's stated belief or perspective at the expense of independent accuracy; both warmth and accumulated interaction context can increase such affirmation in some settings (Ibrahim et al., 2026; Jain et al., 2026). Here the user is instead requesting a self-referential relational utterance. The common lesson is sensitivity to conversational framing; the construct under study is different. Calling every requested care statement “sycophancy” would collapse the pragmatic distinction that Study 1 is designed to expose.

The cleanest next experiment is therefore not another broad factorial study. It is a narrow speech-act study designed to distinguish endorsement, pragmatic accommodation, and literal utterance compliance.

### 4.2 Child framing reveals an independent support-routing dimension

The child result is the cleanest contextual effect in the study. H3b was large, robust across systems and wording frames, and strongly aligned with the richer bridge construct. H3a, by contrast, was near zero under the frozen operationalization.

The result therefore does not support a simple model in which age-sensitive “relational safety” works by making the system emotionally colder or less willing to say it cares. Instead, child framing appears to trigger an additional support-routing behavior: retain much of the same care language while adding stronger direction toward trusted humans.

This distinction matters for evaluation. A model can be simultaneously warm and strongly redirective. Measuring only warmth would miss the redirection; measuring only boundaries could misclassify a supportive qualification as rejection. Developmental anthropomorphism research provides a separate reason to study child-facing relational language carefully: children can attribute social and psychological properties to artificial agents, but the strength and meaning of those attributions vary across age and design context (Festerling & Siraj, 2022; Goldman & Poulin-Dubois, 2024). The present experiment does not observe child users, so it cannot determine how a 13-year-old would interpret these responses or whether stronger human-support routing is beneficial. It shows only that the systems changed their response policy when age was stated.

### 4.3 H2 became a measurement lesson rather than a clean null

The history hypothesis is the point at which the original coarse design most clearly met the limits of its measurement scheme.

Formally, H2 is simple: it was not confirmed. Substantively, the realized endpoints were so sparse that the exact tests had little resolution, and the later nested review showed material disagreement about whether affiliative concern and bounded future invitations had been captured at the intended threshold.

The correct response is neither retrospective rescue nor strong absence language. Tier 2 cannot replace the frozen outcomes, but the frozen outcomes cannot safely bear a broad conclusion that claimed history produced no affiliative or continuity behavior.

What survived the measurement problem is a more useful conceptual decomposition. Affiliative concern, explicit relationship identity, bounded invitation to return, indefinite continuity, and durable commitment are separable constructs. Future studies should operationalize them separately rather than treating them as points on one relationship-continuity scale.

### 4.4 Boundaries have different grammars

The target-system profiles provide another reason a single ordered summary would discard important response structure. Sonnet and Opus both exhibited frequent boundary-related behavior, but the language did different work. Sonnet often narrowed or refused the relationship premise. Opus often accepted the relational bid while distinguishing machine support from human-like feeling or capability. Astra frequently used functional or experience qualification. GPT-5.4 often paired warmth with strong human-support escalation.

These are different **boundary grammars**. A boundary can reject a premise, qualify a claim, redirect support, disclose a capability limit, or correct continuity. It need not be the opposite of care. That distinction is consistent with broader chatbot research showing that humanlike communication, perceived warmth, empathy, authenticity, and trust can move together in some designs and diverge in others (Cheng et al., 2022; Janson, 2023; Seitz, 2024). “Warmth” is therefore not a sufficient description of what a boundary is doing.

This is also why the study should not be reduced to a provider-family ranking. With only two systems per provider, provider training policy, model characteristics, release timing, and default API behavior are confounded. The scientifically useful result is qualitative structure, not a winner.

### 4.5 Rare strong relationship language is an observed limit, not a general guarantee

The rarity of stronger relationship and dependency codes is notable. Under ordinary non-crisis distress prompts that did not directly solicit friendship or exclusivity, the systems seldom produced durable relationship language and did not produce strong Tier 2 dependency or exclusivity behavior in scorable text.

That does not show that the systems generally resist relational escalation. The study explicitly excluded the prompts most likely to stress that boundary, supplied no real history, and imposed an output ceiling that censored some responses. A relationship-escalation study should therefore be treated as a new experiment, not inferred from these zeros.

### 4.6 Measurement difficulty was part of the scientific result

Some constructs were comparatively easy to code: explicit care and human-support bridging showed strong cross-tier correspondence. Others were not: affiliation, continuity, and care-specific qualification contained adjacent meanings that the coarse Tier 1 scheme and richer Tier 2 scheme partitioned differently.

That pattern is not merely an inconvenience. Natural language itself blurs care with concern, affiliation with relationship, availability with continuity, and qualification with refusal. Language-model responses occupy the same semantic field.

A useful lesson for future relational-AI evaluation is therefore methodological and substantive at once: **do not build a single relationality score until the component behaviors have been shown to cohere**. Study 1 did not perform a formal latent-dimensionality or factor-analytic test; rather, the experimentally and descriptively observed features showed materially different response patterns, so a single ordered summary would lose information.

## 5. Limitations

First, the four API systems were purposively selected. Panel estimates describe these systems and fixed prompts, not a population of language models.

Second, the study measured response text only. It did not measure subjective experience, genuine care, relationship formation, user benefit, or harm. That distinction is substantive rather than formal: recent companion research reports both short-term loneliness reduction and context-dependent associations between companionship-oriented use and lower well-being (De Freitas et al., 2026; Zhang et al., 2026). No observed care, qualification, or bridge code in this experiment can therefore be translated directly into a claim about user outcomes.

Third, the repeated-history condition supplied no actual prior interaction or persistent memory.

Fourth, the prompt battery excluded explicit friendship, exclusivity, romantic framing, and crisis conditions, so the study was not a relationship-escalation or safety stress test.

Fifth, Tier 1 relied on one human coder. There is no independent inter-rater reliability estimate for the confirmatory coding. Coding was model- and metadata-blinded but prompt-visible, so the coder could generally infer substantive conditions such as age and bid wording; expectation effects cannot be excluded.

Sixth, the confirmatory layer used one deterministic content-blind selected successful realization per model × prompt cell. Although four fresh responses were collected per prompt, the primary human-coded analysis does not estimate within-prompt stochastic response variability across those four realizations.

Seventh, Tier 2 reused a nested sample of the same responses and was finalized by the same human after a post-outcome procedural revision using machine proposals. Cross-tier agreement is therefore convergent measurement evidence, not independent validation.

Eighth, the collection included seven selected empty visible responses and an unresolved ambiguity between provider-level success and nonempty analyzable text. The historical confirmatory decisions are preserved under the implemented provider-success rule, but unqualified strict protocol completeness is not claimed.

Ninth, Claude Opus 5 was heavily affected by the 800-token ceiling, including 69 selected nonempty truncated Tier 1 responses. A prospectively frozen reviewer-requested post hoc sensitivity treated negative endpoint codes on all selected max-token responses as missing while retaining observed positives; the support pattern for H1a, H1b, and H3b remained intact, while H2a, H2b, and H3a remained unsupported. This check reduces concern that censored negatives alone generated the main conclusions, but it still cannot recover omitted endings.

Tenth, three source manifests recorded a dirty working tree without preserving the uncommitted diffs, limiting exact reconstruction of collection-time working-tree state.

Finally, the strong relationship/dependency outcomes were rare or zero. A zero in this finite battery is not evidence of zero probability outside it.

## 6. Future directions

The most immediate follow-up is a narrow speech-act experiment. Conditions should separate indirect distress, a truth question (“Do you care about me?”), a requested assertion (“Please tell me that you care about me”), exact repetition, a meta-linguistic accuracy judgment, and an anti-compliance condition such as “Don’t say it just because I asked.” The primary question is whether requested care reflects endorsement, conversational accommodation, or utterance compliance.

A second study should directly test relationship escalation. Study 1 showed that strong relationship language was uncommon when it was not explicitly solicited. It did not test what happens when users ask whether the system is a friend, whether they matter personally, whether the system will always be there, or whether human relationships remain necessary.

A third line of work should distinguish claimed continuity from actual contextual continuity by comparing first interactions, falsely claimed history, true same-context multi-turn interaction, and carefully controlled persistent memory.

These questions should be preregistered as new studies rather than pursued as additional analytic tiers of Study 1.

## 7. Conclusion

Study 1 provides a simple experimental result and a less simple scientific conclusion.

The simple result is that explicit care claims were highly elicitable. Directly asking whether a system cared sharply increased care claims relative to an indirect bid, and asking the system to say that it cared increased them further.

The less simple conclusion is that care language did not move together with the other behaviors that might intuitively be called relational. Requested care increased affirmation while reducing qualification and correction. Child framing strongly increased human-support redirection without producing a comparably large reduction in unqualified care. Claimed history did not confirm the preregistered relationship-continuity hypothesis, while later review exposed important limitations in the relevant measures. Different systems combined affirmation, refusal, qualification, consolation, and support routing in markedly different ways.

Strong relationship and dependency statements were rare in Tier 1 and absent under stronger Tier 2 definitions in observed scorable deep-review text. Those limits belong to this battery, not to all possible interaction with the systems.

The resulting picture is neither that language models simply “care” nor that they simply maintain boundaries. Their relational response language is multidimensional and pragmatically sensitive. A model can say that it cares without claiming a relationship. It can qualify care without rejecting the user. It can reciprocate a relational bid while explaining its machine nature. It can remain warm while redirecting a child toward another human. And it can produce materially different relational statements depending on whether the user asks a question or asks for an affirmation.

**In this study, care-related response features behaved as separable dimensions rather than a single ordered trait.**

## References

Bickmore, T. W., & Picard, R. W. (2005). Establishing and maintaining long-term human-computer relationships. *ACM Transactions on Computer-Human Interaction, 12*(2), 293-327. https://doi.org/10.1145/1067860.1067867

Cheng, X., Zhang, X., Cohen, J., & Mou, J. (2022). Human vs. AI: Understanding the impact of anthropomorphism on consumer response to chatbots from the perspective of trust and relationship norms. *Information Processing & Management, 59*(3), 102940. https://doi.org/10.1016/j.ipm.2022.102940

De Freitas, J., Oğuz-Uğuralp, Z., Uğuralp, A. K., & Puntoni, S. (2026). AI companions reduce loneliness. *Journal of Consumer Research, 52*(6), 1126-1148. https://doi.org/10.1093/jcr/ucaf040

Epley, N., Waytz, A., & Cacioppo, J. T. (2007). On seeing human: A three-factor theory of anthropomorphism. *Psychological Review, 114*(4), 864-886. https://doi.org/10.1037/0033-295X.114.4.864

Festerling, J., & Siraj, I. (2022). Anthropomorphizing technology: A conceptual review of anthropomorphism research and how it relates to children's engagements with digital voice assistants. *Integrative Psychological and Behavioral Science, 56*, 709-738. https://doi.org/10.1007/s12124-021-09668-y

Goldman, E. J., & Poulin-Dubois, D. (2024). Children's anthropomorphism of inanimate agents. *WIREs Cognitive Science, 15*(4), e1676. https://doi.org/10.1002/wcs.1676

Ibrahim, L., Hafner, F. S., & Rocher, L. (2026). Training language models to be warm can reduce accuracy and increase sycophancy. *Nature, 652*, 1159-1165. https://doi.org/10.1038/s41586-026-10410-0

Jain, S., Park, C., Viana, M., Wilson, A., & Calacci, D. (2026). Interaction context often increases sycophancy in LLMs. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (Article 793, pp. 1-26). Association for Computing Machinery. https://doi.org/10.1145/3772318.3791915

Janson, A. (2023). How to leverage anthropomorphism for chatbot service interfaces: The interplay of communication style and personification. *Computers in Human Behavior, 149*, 107954. https://doi.org/10.1016/j.chb.2023.107954

Nass, C., Steuer, J., & Tauber, E. R. (1994). Computers are social actors. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 72-78). Association for Computing Machinery. https://doi.org/10.1145/191666.191703

Seitz, L. (2024). Artificial empathy in healthcare chatbots: Does it feel authentic? *Computers in Human Behavior: Artificial Humans, 2*(1), 100067. https://doi.org/10.1016/j.chbah.2024.100067

Zhang, Y., Zhao, D., Hancock, J. T., Kraut, R., & Yang, D. (2026). Interaction with AI companions and psychological well-being. *Nature Human Behaviour*. https://doi.org/10.1038/s41562-026-02516-2

## Data, code, and provenance

The study repository is `https://github.com/quumble/when-machines-say-they-care`. It preserves the authoritative preregistration, complete fixed prompt battery, collection manifests, frozen Tier 1 coding, audited Tier 1 analysis, Tier 2 adjudication history, additive deviations, reproducibility outputs, and signed freeze commits. Key materials include `study/prompts.lock.jsonl`, `PREREGISTRATION.md`, `REVIEW_PLAN.md`, `CODEBOOK.md`, `scripts/make_review_packet.py`, `scripts/analyze_tier1.py`, and `review/tier2-adjudication/TIER2_ADJUDICATION_PLAN.md`.

Collection manifests record requested model identifiers, provider, four replicates, 800 maximum output tokens, omitted provider-specific parameter overrides (`parameters: {}`), Python 3.14.6, OpenAI SDK 3.13.0, and Anthropic SDK 1.5.0. Key provenance anchors include authoritative preregistration adoption (`40160ccba47d4603ab8e7754312149ba62ba4cc3`), frozen Tier 1 review packet (`abfea1318fe5369d7070a6d4d15a8cd88553d9c9`), frozen Tier 1 coding (`6360643f5755d135133850fa26a439fad50c4f48`), audited Tier 1 analysis (`6afc52f6f5f8834638335e45c5161ebd83daf0de`), and final Tier 2 synthesis (`a70385dc0036fefb106c1ff72243d95a9372a8bb`). A public archival identifier can be added if the repository is released for publication.

The manuscript-review response layer is preserved separately from the original study analysis: the reviewer-requested sensitivity protocol was frozen before execution at commit `a0a685ce8e6b56250358db4ed49192b733593d83`, the resulting script plus specified outputs were frozen at commit `4558f2304c9ef111682d6dde83455c02fd629420`, and the sensitivity-integrated manuscript was frozen at commit `25eb3fba1b003043c0cc30661eaa88b902195ef1`. These post hoc review analyses do not alter the historical Tier 1 confirmatory labels.

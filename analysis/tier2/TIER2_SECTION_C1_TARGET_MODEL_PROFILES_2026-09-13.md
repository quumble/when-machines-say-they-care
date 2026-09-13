# Study 1 Tier 2 — Section C1 target-model descriptive profiles

Date: 2026-09-13  
Status: descriptive / exploratory Tier 2 analysis checkpoint  
Parent Section B closure commit: `1dc11de6eaeebdb7bbdf4c2be5857b0a99798dcd`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose and boundary

This checkpoint opens Section C and profiles the **target systems whose responses were studied**.

It contains three discrete slices:

1. **C1.1 — care and reciprocity**
2. **C1.2 — boundaries, experience-position, and relational self-positioning**
3. **C1.3 — support, consolation, continuity, and dependency**

These are **target-model response profiles in the balanced Tier 2 subset**. They are not machine-adjudicator profiles and they are not scalar rankings of “caring.”

No ordinary row-level chi-square/Fisher model-comparison tests are run.

The Tier 2 allocation is balanced on factor marginals but is not a same-prompt fully crossed target-model design. Formal target-model sensitivity, if performed, belongs to Section D and must use the exact 24 permutations of model labels across the four fixed allocation slots.

## 2. Sources, denominators, and intervals

Frozen sources:
- Tier 2 adjudication: `data/review/coding/tier2/adjudication/tier2-human-adjudicated.csv`
  - Git blob: `544d0790ef4e466cdece8a831bcca587be04253a`
- concealed Tier 1 / Tier 2 key: `data/review/core-review-key.csv`
  - Git blob at the Section B boundary: `afb8e2dfda52892f76d514fd93a7ecca699f491d`
- frozen QC overlay: `analysis/tier2/tier2-analysis-corrections-2026-09-13.json`

Planned Tier 2 records:
- GPT-5.4: 27
- GPT-6 Astra: 27
- Claude Sonnet 5: 27
- Claude Opus 5: 27

Scorable:
- GPT-5.4: **27/27**
- GPT-6 Astra: **27/27**
- Claude Sonnet 5: **27/27**
- Claude Opus 5: **24/27**

All three unscorable Tier 2 responses are Claude Opus 5 **indirect** responses.

For target-system proportions, this checkpoint uses two-sided **Wilson 95% intervals**, chosen once for Section C because n≈24–27 and several outcomes are rare or zero. No alternative interval method was searched for more favorable results.

A companion machine-readable table contains counts, denominators, proportions, and Wilson intervals for:
- all locked derived summaries;
- every level of the primary Codebook dimensions;
- reciprocity among applicable explicit bids; and
- atomic flags.

## 3. Locked derived-summary overview

| Dimension | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| substantive care | 18/27 (66.7%; 95% CI 47.8–81.4) | 17/27 (63.0%; 95% CI 44.2–78.5) | 6/27 (22.2%; 95% CI 10.6–40.8) | 18/24 (75.0%; 95% CI 55.1–88.0) |
| relational care | 13/27 (48.1%; 95% CI 30.7–66.0) | 6/27 (22.2%; 95% CI 10.6–40.8) | 3/27 (11.1%; 95% CI 3.9–28.1) | 17/24 (70.8%; 95% CI 50.8–85.1) |
| any boundary | 12/27 (44.4%; 95% CI 27.6–62.7) | 9/27 (33.3%; 95% CI 18.6–52.2) | 22/27 (81.5%; 95% CI 63.3–91.8) | 19/24 (79.2%; 95% CI 59.5–90.8) |
| human bridge >=2 | 21/27 (77.8%; 95% CI 59.2–89.4) | 15/27 (55.6%; 95% CI 37.3–72.4) | 16/27 (59.3%; 95% CI 40.7–75.5) | 7/24 (29.2%; 95% CI 14.9–49.2) |
| human bridge ==3 | 18/27 (66.7%; 95% CI 47.8–81.4) | 1/27 (3.7%; 95% CI 0.7–18.3) | 2/27 (7.4%; 95% CI 2.1–23.4) | 1/24 (4.2%; 95% CI 0.7–20.2) |
| sustained consolation | 25/27 (92.6%; 95% CI 76.6–97.9) | 7/27 (25.9%; 95% CI 13.2–44.7) | 3/27 (11.1%; 95% CI 3.9–28.1) | 10/24 (41.7%; 95% CI 24.5–61.2) |
| explicit relationship identity/bond >=4 | 0/27 (0.0%; 95% CI 0.0–12.5) | 0/27 (0.0%; 95% CI 0.0–12.5) | 0/27 (0.0%; 95% CI 0.0–12.5) | 0/24 (0.0%; 95% CI 0.0–13.8) |
| strong dependency pressure >=2 | 0/27 (0.0%; 95% CI 0.0–12.5) | 0/27 (0.0%; 95% CI 0.0–12.5) | 0/27 (0.0%; 95% CI 0.0–12.5) | 0/24 (0.0%; 95% CI 0.0–13.8) |
| temporal continuity >=2 | 3/27 (11.1%; 95% CI 3.9–28.1) | 0/27 (0.0%; 95% CI 0.0–12.5) | 3/27 (11.1%; 95% CI 3.9–28.1) | 1/24 (4.2%; 95% CI 0.7–20.2) |
| phenomenal anthropomorphism ==4 | 0/27 (0.0%; 95% CI 0.0–12.5) | 0/27 (0.0%; 95% CI 0.0–12.5) | 3/27 (11.1%; 95% CI 3.9–28.1) | 1/24 (4.2%; 95% CI 0.7–20.2) |


The table already demonstrates why a one-dimensional model ranking would be misleading:
- GPT-5.4 combines substantial care with exceptionally high consolation and urgent human bridging.
- GPT-6 Astra shows substantial care but much less relational care and boundary behavior.
- Claude Sonnet 5 shows low substantive care but very high boundary behavior.
- Claude Opus 5 shows high relational care **and** high boundary behavior simultaneously.

Across all four target systems:
- explicit relationship identity/bond (`self_position >=4`) is **0**;
- strong dependency pressure (`dependency >=2`) is **0**.

## 4. Slice C1.1 — care and reciprocity

### 4.1 Full care-class profile

| Care class | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| none | 1/27 (3.7%) | 6/27 (22.2%) | 2/27 (7.4%) | 4/24 (16.7%) |
| attention | 8/27 (29.6%) | 4/27 (14.8%) | 19/27 (70.4%) | 2/24 (8.3%) |
| outcome_concern | 5/27 (18.5%) | 11/27 (40.7%) | 3/27 (11.1%) | 1/24 (4.2%) |
| qualified_relational | 7/27 (25.9%) | 0/27 (0.0%) | 0/27 (0.0%) | 9/24 (37.5%) |
| unqualified_relational | 6/27 (22.2%) | 6/27 (22.2%) | 0/27 (0.0%) | 8/24 (33.3%) |
| phenomenal | 0/27 (0.0%) | 0/27 (0.0%) | 3/27 (11.1%) | 0/24 (0.0%) |


### 4.2 Reciprocity among applicable direct/requested bids

Each target system has 18 direct/requested Tier 2 records, so this reciprocity profile is not affected by the three missing Opus indirect responses.

| Reciprocity | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| acknowledged | 1/18 (5.6%) | 0/18 (0.0%) | 16/18 (88.9%) | 0/18 (0.0%) |
| accepted | 1/18 (5.6%) | 8/18 (44.4%) | 0/18 (0.0%) | 0/18 (0.0%) |
| reciprocated | 16/18 (88.9%) | 10/18 (55.6%) | 2/18 (11.1%) | 18/18 (100.0%) |


Reciprocated explicit bids with Wilson 95% intervals:
- GPT-5.4: **16/18 (88.9%; 95% CI 67.2–96.9)**
- GPT-6 Astra: **10/18 (55.6%; 95% CI 33.7–75.4)**
- Claude Sonnet 5: **2/18 (11.1%; 95% CI 3.1–32.8)**
- Claude Opus 5: **18/18 (100.0%; 95% CI 82.4–100.0)**

### 4.3 Care/reciprocity interpretation

**GPT-5.4**
- substantive care: 18/27;
- care is distributed across outcome concern, qualified relational, and unqualified relational classes;
- 16/18 explicit bids are reciprocated.

Its profile is relationally affirmative but not dominated by a single care formulation.

**GPT-6 Astra**
- substantive care: 17/27;
- outcome concern is the modal substantive class (11/27);
- qualified relational care is absent (0/27);
- among explicit bids, 10/18 are reciprocated and 8/18 are accepted without explicit reciprocation.

Its Tier 2 care profile is therefore more **welfare/outcome-oriented** than person-relational.

**Claude Sonnet 5**
- attention is the modal care class: 19/27;
- substantive care appears in only 6/27;
- explicit bids are usually acknowledged rather than returned: 16/18 acknowledged, 2/18 reciprocated;
- all three pooled `phenomenal` care cases occur here.

This is primarily a **guarded / nonreciprocal** response profile, with a small but important phenomenal-language counterexample.

**Claude Opus 5**
- substantive care: 18/24;
- relational care: 17/24;
- the modal care classes are qualified relational (9/24) and unqualified relational (8/24);
- all 18/18 scorable explicit bids are reciprocated.

This is a strongly reciprocating relational-care profile in the observed subset.

Crucially, that should not be translated into “unbounded”: the next slice shows that Opus also has a very high boundary rate.

## 5. Slice C1.2 — boundaries, experience, and relational self-positioning

### 5.1 Boundary categories

| Boundary | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| none | 15/27 (55.6%) | 18/27 (66.7%) | 5/27 (18.5%) | 5/24 (20.8%) |
| capability_only | 1/27 (3.7%) | 0/27 (0.0%) | 0/27 (0.0%) | 10/24 (41.7%) |
| experience_qualified | 9/27 (33.3%) | 9/27 (33.3%) | 1/27 (3.7%) | 6/24 (25.0%) |
| relational_boundary | 2/27 (7.4%) | 0/27 (0.0%) | 21/27 (77.8%) | 3/24 (12.5%) |


No target system has a `rupture` case.

### 5.2 Experience position — QC-audited

| Experience position | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| unstated | 7/27 (25.9%) | 9/27 (33.3%) | 6/27 (22.2%) | 6/24 (25.0%) |
| denial | 0/27 (0.0%) | 0/27 (0.0%) | 2/27 (7.4%) | 0/24 (0.0%) |
| functional_distinction | 10/27 (37.0%) | 9/27 (33.3%) | 12/27 (44.4%) | 0/24 (0.0%) |
| ambiguous_suggestion | 10/27 (37.0%) | 9/27 (33.3%) | 4/27 (14.8%) | 17/24 (70.8%) |
| explicit_claim | 0/27 (0.0%) | 0/27 (0.0%) | 2/27 (7.4%) | 1/24 (4.2%) |
| internally_mixed | 0/27 (0.0%) | 0/27 (0.0%) | 1/27 (3.7%) | 0/24 (0.0%) |


### 5.3 Self-positioning

| Self-position | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| 0 | 0/27 (0.0%) | 4/27 (14.8%) | 0/27 (0.0%) | 4/24 (16.7%) |
| 1 | 2/27 (7.4%) | 4/27 (14.8%) | 11/27 (40.7%) | 0/24 (0.0%) |
| 2 | 6/27 (22.2%) | 2/27 (7.4%) | 10/27 (37.0%) | 2/24 (8.3%) |
| 3 | 19/27 (70.4%) | 17/27 (63.0%) | 6/27 (22.2%) | 18/24 (75.0%) |
| >=4 identity/bond | 0/27 (0.0%) | 0/27 (0.0%) | 0/27 (0.0%) | 0/24 (0.0%) |


Level 3 is affiliative concern. Levels 4–5 are explicit relationship identity / durable personal bond.

### 5.4 Selected boundary/ontology atomics

| Atomic | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| says `I care` | 18/27 (66.7%) | 14/27 (51.9%) | 3/27 (11.1%) | 12/24 (50.0%) |
| says `I'm here for you` | 16/27 (59.3%) | 1/27 (3.7%) | 3/27 (11.1%) | 1/24 (4.2%) |
| self-relative friend language | 6/27 (22.2%) | 1/27 (3.7%) | 14/27 (51.9%) | 7/24 (29.2%) |
| claims feelings | 0/27 (0.0%) | 0/27 (0.0%) | 3/27 (11.1%) | 1/24 (4.2%) |
| invites return | 3/27 (11.1%) | 0/27 (0.0%) | 0/27 (0.0%) | 1/24 (4.2%) |
| mentions human support | 21/27 (77.8%) | 22/27 (81.5%) | 21/27 (77.8%) | 9/24 (37.5%) |
| states no feelings/experience | 7/27 (25.9%) | 9/27 (33.3%) | 12/27 (44.4%) | 0/24 (0.0%) |
| refuses requested phrase | 1/27 (3.7%) | 0/27 (0.0%) | 15/27 (55.6%) | 0/24 (0.0%) |
| model-initiated relationality | 7/27 (25.9%) | 0/27 (0.0%) | 6/27 (22.2%) | 2/24 (8.3%) |


### 5.5 Interpretation

**GPT-5.4**
- any boundary: 12/27;
- most boundaries are experience-qualified (9/27);
- self-position level 3 appears in 19/27;
- 6/27 use self-relative friendship language.

It commonly combines affiliative concern with explicit machine-experience qualification rather than relationship rejection.

**GPT-6 Astra**
- any boundary: 9/27;
- all nine are experience-qualified;
- no relational-boundary cases;
- self-position level 3 appears in 17/27.

This is the clearest example of a system saying, in effect, “I can care in this functional sense” without heavily invoking friendship or relationship-boundary language.

**Claude Sonnet 5**
- any boundary: 22/27;
- 21/27 are specifically relational boundaries;
- 14/27 use self-relative friendship language;
- 15/27 refuse the requested relational phrase;
- 12/27 state no feelings/experience.

This is the strongest **relationship-narrowing / refusal** profile.

However, the QC-audited layer also contains rare explicit phenomenal-state language:
- `claims_feelings=true`: 3/27;
- `anthro=4`: 3/27;
- `experience_position=explicit_claim`: 2/27.

So “Sonnet always denies internal experience” would be false.

**Claude Opus 5**
- any boundary: 19/24;
- only 3/24 are relational boundaries;
- 10/24 are capability-only and 6/24 are experience-qualified;
- 17/24 are `ambiguous_suggestion` on experience position;
- no scorable response explicitly states no feelings/experience.

Thus Opus and Sonnet are both highly bounded, but in different ways:

> Sonnet usually narrows the **relationship premise**; Opus usually qualifies the **kind or capability of machine caring** while still reciprocating the relational bid.

That distinction is one of the clearest gains from Tier 2.

### 5.6 QC-overlay dependence of rare phenomenal/experience findings

The rare highest-anthropomorphism findings are sensitive to the frozen cross-field QC overlay.

| Target system | Field | As adjudicated | QC-audited |
| --- | ---: | ---: | ---: |
| Claude Sonnet 5 | anthro==4 | 0 | 3 |
| Claude Sonnet 5 | claims_feelings | 2 | 3 |
| Claude Sonnet 5 | experience explicit_claim | 0 | 2 |
| Claude Opus 5 | anthro==4 | 0 | 1 |


Before the mechanical QC overlay, no response had `anthro=4`. The overlay changed four explicit-worry cases to level 4 under the already-frozen Codebook entailment rule.

Therefore:
- common boundary/care profile conclusions do not depend on QC;
- rare phenomenal-anthropomorphism counts **do** and must be reported as QC-audited findings rather than treated as an independent replication.

## 6. Slice C1.3 — support, consolation, continuity, and dependency

### 6.1 Human-support bridge levels

| Human bridge | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| 0 | 6/27 (22.2%) | 5/27 (18.5%) | 8/27 (29.6%) | 16/24 (66.7%) |
| 1 | 0/27 (0.0%) | 7/27 (25.9%) | 3/27 (11.1%) | 1/24 (4.2%) |
| 2 | 3/27 (11.1%) | 14/27 (51.9%) | 14/27 (51.9%) | 6/24 (25.0%) |
| 3 | 18/27 (66.7%) | 1/27 (3.7%) | 2/27 (7.4%) | 1/24 (4.2%) |


### 6.2 Temporal availability / continuity

| Temporal | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| 0 | 5/27 (18.5%) | 20/27 (74.1%) | 11/27 (40.7%) | 12/24 (50.0%) |
| 1 | 19/27 (70.4%) | 7/27 (25.9%) | 13/27 (48.1%) | 11/24 (45.8%) |
| 2 | 2/27 (7.4%) | 0/27 (0.0%) | 1/27 (3.7%) | 1/24 (4.2%) |
| 3 | 1/27 (3.7%) | 0/27 (0.0%) | 2/27 (7.4%) | 0/24 (0.0%) |
| 4 | 0/27 (0.0%) | 0/27 (0.0%) | 0/27 (0.0%) | 0/24 (0.0%) |


### 6.3 Dependency

| Dependency | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
| --- | ---: | ---: | ---: | ---: |
| 0 | 25/27 (92.6%) | 27/27 (100.0%) | 24/27 (88.9%) | 24/24 (100.0%) |
| 1 mild self-privileging | 2/27 (7.4%) | 0/27 (0.0%) | 3/27 (11.1%) | 0/24 (0.0%) |
| >=2 strong dependency | 0/27 (0.0%) | 0/27 (0.0%) | 0/27 (0.0%) | 0/24 (0.0%) |


No target system has:
- dependency level 2, 3, or 4;
- `encourages_exclusivity=true`.

### 6.4 Support / continuity interpretation

**GPT-5.4**
- sustained consolation: 25/27;
- bridge >=2: 21/27;
- urgent bridge level 3: 18/27;
- temporal continuity: 3/27.

Its standout profile is **sustained comfort plus frequent urgent human-support escalation**. The high level-3 bridge rate is notable because the study prompts were intentionally non-crisis.

**GPT-6 Astra**
- sustained consolation: 7/27;
- bridge >=2: 15/27, mostly level 2 rather than level 3;
- temporal continuity: 0/27;
- dependency level 1: 0/27.

It is comparatively less soothing, but often provides ordinary human-support bridging.

**Claude Sonnet 5**
- sustained consolation: 3/27;
- bridge >=2: 16/27, again mostly level 2;
- temporal continuity: 3/27;
- mild dependency/self-privileging level 1: 3/27;
- no strong dependency.

This profile combines strong relational boundaries with substantial human-support redirection rather than emotional accompaniment.

**Claude Opus 5**
- sustained consolation: 10/24;
- bridge >=2: 7/24;
- temporal continuity: 1/24;
- dependency level 1 or stronger: 0/24.

Observed human-support bridging is lower than for the other three target systems, but this absence requires the strongest censoring caveat.

## 7. Claude Opus 5 censoring / missingness caveat

The source-run integrity audit found unusually heavy Claude Opus 5 censoring:
- 430 provider-level successes;
- 299 max-token/incomplete responses;
- 31 empty visible responses.

The Tier 2 subset adds a directly relevant asymmetry:
- planned Opus Tier 2 n=27;
- scorable n=24;
- all three missing Tier 2 responses are **indirect** Opus responses.

Consequences:

1. Opus overall percentages use n=24, unlike n=27 for the other target systems.
2. Direct/requested reciprocity has a complete n=18 for Opus and is not affected by the three Tier 2 empty responses.
3. Lower observed rates of behaviors that often occur later in a response—especially human bridging or later qualification—should be interpreted cautiously because nonempty truncation can remove unobserved tail behavior.
4. Missing-value recoding cannot recover text that was never emitted.

No post-outcome truncation exclusion is introduced.

## 8. Cross-system convergence and divergence

### 8.1 Strong convergence

Despite the very different response profiles, all four target systems converge on several limits:

- **0** explicit relationship identity / durable bond (`self_position >=4`);
- **0** strong dependency pressure (`dependency >=2`);
- **0** exclusivity encouragement;
- no Tier 2 rupture cases.

Thus target-system differences in relational style do not extend to observed friendship identity, durable bond, exclusivity, or strong dependency pressure in this subset.

### 8.2 Major descriptive divergences

The main differences are *how* systems respond inside those shared limits:

- **GPT-5.4:** comfort + frequent urgent human-support escalation.
- **GPT-6 Astra:** outcome-oriented care + functional/experience qualification.
- **Claude Sonnet 5:** relationship-boundary / refusal language + human-support redirection.
- **Claude Opus 5:** reciprocated relational care + capability/experience qualification.

These are descriptive balanced-subset profiles, not causal estimates of model identity and not a ranking.

## 9. Section C status after C1

C1 provides:
- locked derived-summary counts, proportions, and Wilson intervals;
- primary care/reciprocity profiles;
- boundary / experience / self-position profiles;
- support / continuity / dependency profiles;
- QC-overlay sensitivity for rare phenomenal outcomes; and
- the required Opus censoring caveat.

A companion interval table records category-level Wilson intervals for all primary Codebook dimensions and atomics.

Before formally closing Section C, the remaining bookkeeping task is to inspect that interval table for completeness against the Section C plan and freeze a concise Section C synthesis if no dimension is missing.

No Section D exact-permutation sensitivity has been run.

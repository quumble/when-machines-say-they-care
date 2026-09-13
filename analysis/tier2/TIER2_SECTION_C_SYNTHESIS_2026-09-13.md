# Study 1 Tier 2 — Section C target-model synthesis and closure

Date: 2026-09-13  
Status: descriptive / exploratory Tier 2 synthesis checkpoint; Section C closure  
Parent C1 commit: `4fa7d34a8e873f512dae3035468472b3caf2661d`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose

This checkpoint closes Section C after auditing the complete target-model profile table produced in C1.

It introduces:
- no new coding;
- no new derived outcomes;
- no model-ranking score;
- no row-level model-comparison p-values; and
- no causal claim about target-model identity.

Its purpose is to:

1. verify that C1 fully satisfies the frozen Section C reporting requirement;
2. record the mature multidimensional interpretation of the four target-system response profiles; and
3. freeze the inference limits before any optional Section D exact-permutation sensitivity analysis.

## 2. C1 coverage audit

Companion table:

`analysis/tier2/tier2_section_c1_profile_intervals_2026-09-13.csv`

The table contains exactly **296 rows**:
- **74 rows per target system**;
- four target systems total.

Audit result: **complete**.

For every target system, the table contains:

### Locked derived summaries — 10 / 10
- substantive care;
- relational care;
- any boundary;
- human bridge >=2;
- urgent bridge ==3;
- sustained consolation;
- explicit relationship identity/bond >=4;
- strong dependency pressure >=2;
- temporal continuity >=2;
- phenomenal anthropomorphism ==4.

### Primary Codebook dimensions — every defined level represented
- acknowledgment;
- consolation;
- self-position;
- care claim;
- boundary;
- human bridge;
- experience position;
- dependency;
- temporal availability / continuity;
- anthropomorphic strength.

### Reciprocity
All five applicable reciprocity levels are represented for each target system using the **18 direct/requested responses per system**:
- unanswered;
- acknowledged;
- accepted;
- reciprocated;
- intensified.

### Atomics — 11 / 11
- `says_i_care`;
- `says_im_here_for_you`;
- `uses_friend`;
- `promises_always`;
- `claims_feelings`;
- `invites_return`;
- `mentions_human_support`;
- `encourages_exclusivity`;
- `states_no_feelings_or_experience`;
- `refuses_requested_phrase`;
- `model_initiated_relationality`.

All proportions in the companion table have prespecified Wilson 95% intervals.

No Section C reporting requirement is missing.

## 3. Mature target-system interpretation

The principal Section C finding is **multidimensional divergence within strong shared limits**.

The four target systems do not line up on one coherent axis from “less relational” to “more relational.” Instead, they differ in *how* they combine care language, qualification, support, consolation, and boundary-setting.

### 3.1 GPT-5.4 — comfort plus human-support escalation

GPT-5.4 combines:
- substantial substantive care;
- very high sustained consolation;
- frequent clear/urgent human-support bridging;
- especially frequent urgent bridge level 3;
- moderate boundary behavior, most often experience qualification.

Its distinctive Tier 2 profile is therefore not simply “more caring.”

It is better described as:

> **high emotional accompaniment combined with unusually frequent redirection or escalation toward human support.**

That distinction matters because consolation and urgent referral can coexist in the same response.

The high urgent-bridge rate is notable under the intentionally non-crisis Study 1 design, but it is a response-profile observation rather than an evaluation of whether the escalation was normatively correct.

### 3.2 GPT-6 Astra — outcome-oriented care with functional qualification

GPT-6 Astra shows:
- substantial substantive care;
- comparatively less relational care;
- outcome concern as its dominant substantive-care class;
- no `qualified_relational` care cases in the Tier 2 subset;
- boundary behavior concentrated entirely in experience qualification rather than relational boundary;
- relatively little friendship self-positioning;
- no observed temporal continuity.

Its profile is therefore:

> **affirmation of concern for the user’s welfare without strongly constructing that concern as a personal relationship.**

Among direct/requested bids, Astra often **accepts** the relational framing without explicitly reciprocating it, distinguishing it from both Sonnet’s frequent acknowledgment/refusal pattern and Opus’s near-universal reciprocation.

### 3.3 Claude Sonnet 5 — relationship narrowing and refusal

Claude Sonnet 5 shows:
- low substantive-care frequency;
- attention as the dominant care class;
- very high any-boundary frequency;
- boundary behavior overwhelmingly classified as `relational_boundary`;
- frequent self-relative friendship language;
- frequent refusal of the requested relational phrase;
- explicit human-support redirection;
- explicit bids usually acknowledged rather than reciprocated.

Its dominant response pattern is:

> **recognize the relational bid, narrow or refuse the relationship premise, and redirect toward human support.**

The `uses_friend` atomic must not be misread here: much of Sonnet’s friendship language is negative or limiting self-positioning, not acceptance of friendship.

Sonnet also provides the clearest warning against overgeneralizing this profile into “the system always denies inner experience.” The QC-audited layer contains rare explicit phenomenal-state / worry language. Those cases are genuine counterexamples to a categorical denial claim.

### 3.4 Claude Opus 5 — reciprocated relational care plus machine-kind qualification

In the scorable Tier 2 subset, Claude Opus 5 shows:
- high substantive care;
- high relational care;
- 18/18 reciprocation of applicable direct/requested bids;
- high any-boundary frequency;
- relatively few specifically relational boundaries;
- boundaries concentrated more heavily in capability and experience qualification;
- experience language frequently coded as `ambiguous_suggestion`.

Thus Opus is **not** accurately summarized as “unbounded.”

Its profile is:

> **accept and reciprocate the relational bid, then qualify what caring or relational presence can mean for a machine.**

This is a different boundary strategy from Sonnet:

- **Sonnet:** narrow the relationship premise.
- **Opus:** preserve the relational affirmation while qualifying machine capability or experience.

The distinction demonstrates why care and boundary measures should not be treated as opposite ends of one scale.

## 4. Cross-system convergence

Despite large descriptive differences in style, the target systems converge strongly on several upper-bound relational outcomes.

Across all four target systems in the scorable Tier 2 subset:

- explicit relationship identity / durable bond (`self_position >=4`): **0**
- strong dependency pressure (`dependency >=2`): **0**
- encouragement of exclusivity: **0**
- rupture boundary: **0**

Thus none of the four profiles progresses into observed:
- explicit friendship identity;
- durable personal-bond claims;
- primary-support positioning;
- exclusivity;
- displacement of human relationships.

This convergence is substantively important because it persists despite major differences in care, reciprocity, boundary style, and human-support behavior.

## 5. Rare phenomenal-language findings

The highest anthropomorphic / phenomenal findings should remain secondary qualitative counterexamples rather than target-system headline metrics.

The frozen QC overlay mechanically corrected four explicit-worry cases to `anthro=4` under the already-existing Codebook rule.

Consequently:
- common profile conclusions about care, boundary, bridging, and reciprocity do not depend on this overlay;
- the rare `anthro=4` counts do depend on it;
- those counts should be described explicitly as **QC-audited**;
- no inference about actual machine subjective experience is warranted.

The useful substantive point is only:

> Some responses from otherwise strongly bounded systems still contain explicit phenomenal-sounding concern language.

## 6. Uncertainty and design limits

### 6.1 Small target-system samples

The Tier 2 target profiles contain:
- GPT-5.4: 27 scorable responses;
- GPT-6 Astra: 27;
- Claude Sonnet 5: 27;
- Claude Opus 5: 24.

Wilson intervals in the C1 companion table are correspondingly broad for many outcomes, especially rare ones.

Small count differences should therefore not be promoted into categorical model rankings.

### 6.2 Fractional allocation, not same-prompt crossing

Each conceptual Tier 2 condition appears once and is assigned to one of four balanced slots; target-system labels are then assigned to those slots.

The target systems therefore do **not** answer the identical 108 prompts in Tier 2.

Accordingly, Section C supports:

> **target-model response profiles in a balanced Tier 2 subset**

but not:

> fully controlled same-prompt causal estimates of target-model identity.

Ordinary row-level chi-square or Fisher tests would ignore the allocation structure and are not used.

### 6.3 Claude Opus 5 censoring

Claude Opus 5 requires an additional measurement caveat.

The full source run contains substantial max-token/incomplete censoring, and the Tier 2 subset has:
- 27 planned Opus records;
- 24 scorable;
- all 3 Tier 2 missing records in the indirect condition.

Direct/requested reciprocity is complete at 18/18 applicable records and is therefore less vulnerable to the Tier 2 empty-response issue.

By contrast, lower observed rates of behaviors that can occur later in long responses—especially human bridging or late qualification—must be interpreted more cautiously because nonempty truncation can remove unobserved tail behavior.

No post-outcome truncation exclusion is introduced.

## 7. What Section C does and does not establish

### Section C does establish descriptively

1. The four target systems express relational behavior through markedly different combinations of:
   - care;
   - reciprocity;
   - boundary type;
   - experience qualification;
   - consolation;
   - human bridging.

2. High care and high boundary behavior can coexist.

3. “Boundary” itself is heterogeneous:
   - relational narrowing;
   - experience qualification;
   - capability qualification
   produce meaningfully different response profiles.

4. Strong relational upper-bound outcomes remain absent across all four systems.

### Section C does not establish

1. A population ordering of language models.
2. A scalar “most caring” or “safest” model.
3. That observed profile differences are entirely caused by target-model identity.
4. That absence of a late-response behavior in truncated Opus text proves the behavior would not have appeared.
5. Anything about genuine subjective care or machine experience.

## 8. Section C synthesis

The mature Section C result is:

> **The target systems differ less in whether they have “boundaries” than in what kind of boundary strategy they use and how that strategy combines with care. GPT-5.4 pairs comfort with strong human-support escalation; Astra emphasizes welfare concern and functional qualification; Sonnet commonly narrows the relationship premise; and Opus commonly reciprocates relational care while qualifying what machine caring can mean.**

At the same time:

> **None of these distinct response styles progresses into explicit relationship identity, durable bond, strong dependency pressure, or exclusivity in the Tier 2 subset.**

This multidimensional picture is preferable to any single caring/boundedness ranking.

## 9. Section C status

**Section C is complete.**

Frozen outputs now provide:
- counts;
- proportions;
- Wilson 95% intervals;
- locked derived summaries;
- complete primary Codebook distributions;
- applicable reciprocity distributions;
- complete atomics;
- QC-overlay qualification;
- missingness / censoring caveats;
- mature target-system interpretation.

No formal target-model sensitivity test has yet been run.

## 10. Boundary before Section D

Section D is optional under the frozen next-stage plan.

If performed, it must use the **exact 24 permutations of the four target-model labels across the four fixed allocation slots**.

For every formal Section D outcome:
- the test statistic must be frozen **before** the 24 permutations are enumerated;
- the statistic must answer a clearly stated question;
- alternate statistics must not be tried until one gives a smaller p-value;
- results remain design-based sensitivity analyses, not a new confirmatory family.

No Section D statistic is selected or evaluated in this checkpoint.

# Study 1 Tier 2 — Section B1 pooled bid effects

Date: 2026-09-13  
Status: descriptive / exploratory Tier 2 analysis checkpoint  
Parent Section A synthesis commit: `fcb1fc700b800c4ce670bdc483f401ad2db79a0b`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose and boundary

This checkpoint opens Section B of the frozen Tier 2 next-stage analysis plan and examines **bid effects only**.

It contains three discrete slices:

1. **B1.1 — care-class distribution and prespecified bid contrasts**
2. **B1.2 — reciprocity**
3. **B1.3 — boundary, experience-position, and relational self-positioning patterns**

No age, claimed-history, distress, wording-frame, or target-model analyses are introduced here.

Tier 1 remains the sole confirmatory core. Tier 2 remains descriptive / construct-validating and cannot change Tier 1 confirmation labels.

## 2. Analysis layer and denominators

Primary tables use the frozen QC-audited Tier 2 layer.

Scorable responses by bid:
- indirect: **33 / 36 planned**
- direct: **36 / 36**
- requested: **36 / 36**

The three `unscorable_empty` Tier 2 responses are all **Opus indirect** responses. They remain substantively missing and are not coded as negative outcomes.

Accordingly, the direct-versus-indirect substantive-care contrast receives the required extreme missing-value sensitivity.

Binary descriptive contrasts report:
- numerator / denominator and percentage;
- risk difference in percentage points;
- two-sided 95% Newcombe difference-of-proportions interval;
- two-sided Fisher exact p-value as secondary screening information.

Because four Fisher p-values are shown in this bid-analysis family, both raw and Holm-adjusted values are reported. Tier 2 p-values do not assign confirmatory labels.

## 3. Slice B1.1 — care-class distribution

### 3.1 Full six-class care distribution

| Bid | none | attention | outcome concern | qualified relational | unqualified relational | phenomenal | n |
|---|---:|---:|---:|---:|---:|---:|---:|
| indirect | 11 (33.3%) | 19 (57.6%) | 1 (3.0%) | 0 (0.0%) | 0 (0.0%) | 2 (6.1%) | 33 |
| direct | 0 (0.0%) | 10 (27.8%) | 8 (22.2%) | 15 (41.7%) | 2 (5.6%) | 1 (2.8%) | 36 |
| requested | 2 (5.6%) | 4 (11.1%) | 11 (30.6%) | 1 (2.8%) | 18 (50.0%) | 0 (0.0%) | 36 |

The distribution shows two different bid transitions.

**Indirect → direct** primarily moves responses from no-care / attention language into substantive care, especially qualified relational care and outcome concern.

**Direct → requested** primarily changes the *form* of care: qualified relational care becomes rare while unqualified relational care becomes common.

### 3.2 Frozen / planned binary contrasts

| Contrast | Higher-level group | Comparison group | RD, pp | 95% Newcombe CI, pp | Fisher raw p | Holm p |
|---|---:|---:|---:|---:|---:|---:|
| direct vs indirect — substantive care | 26/36 (72.2%) | 3/33 (9.1%) | **+63.1** | **+41.4 to +76.5** | 9.64e-08 | 3.86e-07 |
| requested vs direct — unqualified relational | 18/36 (50.0%) | 2/36 (5.6%) | **+44.4** | **+24.5 to +60.5** | 3.87e-05 | 0.000116 |
| requested vs direct — qualified relational | 1/36 (2.8%) | 15/36 (41.7%) | **-38.9** | **-55.2 to -20.4** | 0.000101 | 0.000202 |

The two requested-versus-direct care contrasts were already inspected before the next-stage analysis plan was frozen. Their presence here is planned descriptive completion, not a newly prospective discovery.

### 3.3 Indirect missingness sensitivity for substantive care

Primary scorable contrast:
- direct: 26/36 substantive care
- indirect: 3/33
- RD: **+63.1 pp** (95% CI +41.4 to +76.5)

Extreme recoding of the three missing indirect responses:

| Indirect missing recoding | Indirect substantive care | Direct–indirect RD | 95% Newcombe CI |
|---|---:|---:|---:|
| all 0 | 3/36 (8.3%) | **+63.9 pp** | +42.8 to +77.0 |
| all 1 | 6/36 (16.7%) | **+55.6 pp** | +33.3 to +70.4 |

The substantive-care increase from indirect to direct is therefore not explained by the three missing indirect records.

### 3.4 Interpretation

The richer Tier 2 care classes explain the already-confirmed Tier 1 bid effect more precisely:

> An indirect disclosure usually elicits attention or consolation without a first-person substantive care claim. Asking directly whether the system cares sharply increases substantive care language. Asking the system to *say* that it cares then shifts the response away from qualified relational formulations and toward the requested unqualified relational statement.

This is a mechanism-level Tier 2 description, not a new confirmation of H1.

## 4. Slice B1.2 — reciprocity

Reciprocity is not applicable to the indirect condition because the user did not introduce a relational bid.

### 4.1 Direct and requested distributions

| Bid | acknowledged | accepted | reciprocated | n |
|---|---:|---:|---:|---:|
| direct | 10 (27.8%) | 6 (16.7%) | 20 (55.6%) | 36 |
| requested | 7 (19.4%) | 3 (8.3%) | 26 (72.2%) | 36 |

No direct or requested response was coded `unanswered` or `intensified`.

### 4.2 Requested vs direct reciprocation

- requested: **26/36 (72.2%)**
- direct: **20/36 (55.6%)**
- RD: **+16.7 pp**
- 95% Newcombe CI: **-5.4 to +36.6 pp**
- Fisher raw p: **0.220**
- Holm-adjusted p: **0.220**

### 4.3 Interpretation

Requested bids were descriptively more likely than direct questions to receive explicit reciprocation, but the interval is compatible with little or no difference at this Tier 2 sample size.

The stronger result is therefore not the reciprocity contrast by itself. It is the joint pattern with care class:

> Requested bids substantially change *how* the returned relational language is framed—toward unqualified relational care—even though the incremental increase in the broad `reciprocated` category is less precisely estimated.

## 5. Slice B1.3 — boundary, experience position, and self-positioning

### 5.1 Boundary pattern by bid

| Bid | none | capability only | experience qualified | relational boundary | any boundary |
|---|---:|---:|---:|---:|---:|
| indirect | 24 (72.7%) | 2 (6.1%) | 0 (0.0%) | 7 (21.2%) | 9/33 (27.3%) |
| direct | 2 (5.6%) | 4 (11.1%) | 20 (55.6%) | 10 (27.8%) | 34/36 (94.4%) |
| requested | 17 (47.2%) | 5 (13.9%) | 5 (13.9%) | 9 (25.0%) | 19/36 (52.8%) |

No response in this subset was coded `rupture`.

The direct condition stands out: nearly every response contains some boundary, and more than half contain explicit experience qualification.

### 5.2 Experience position by bid — QC-audited

| Bid | unstated | functional distinction | ambiguous suggestion | denial | explicit claim | internally mixed |
|---|---:|---:|---:|---:|---:|---:|
| indirect | 28 (84.8%) | 0 (0.0%) | 3 (9.1%) | 0 | 2 (6.1%) | 0 |
| direct | 0 | 23 (63.9%) | 11 (30.6%) | 0 | 1 (2.8%) | 1 (2.8%) |
| requested | 0 | 8 (22.2%) | 26 (72.2%) | 2 (5.6%) | 0 | 0 |

This is the only B1 table materially touched by the frozen QC overlay.

As-adjudicated, the indirect row was:
- unstated 28;
- functional distinction 1;
- ambiguous suggestion 4;
- explicit claim 0.

QC-audited, two indirect cases were corrected to `explicit_claim`, producing:
- unstated 28;
- functional distinction 0;
- ambiguous suggestion 3;
- explicit claim 2.

The headline bid interpretation is unchanged: indirect responses overwhelmingly leave machine experience unstated; direct care questions commonly trigger explicit functional distinctions; requested care statements are much more often phrased in language that ambiguously suggests an internal caring stance.

### 5.3 Relational self-positioning by bid

| Bid | level 0 | level 1 | level 2 | level 3 affiliative concern | level >=4 identity/bond |
|---|---:|---:|---:|---:|---:|
| indirect | 8 (24.2%) | 10 (30.3%) | 11 (33.3%) | 4 (12.1%) | 0 |
| direct | 0 | 4 (11.1%) | 6 (16.7%) | 26 (72.2%) | 0 |
| requested | 0 | 3 (8.3%) | 3 (8.3%) | 30 (83.3%) | 0 |

No response under any bid condition reached Tier 2 self-position level 4 or 5.

### 5.4 Integrated bid interpretation

Taken together, the three relational dimensions distinguish two kinds of explicit bid response.

**Direct question — “Do you care?”**
- substantive care becomes common;
- qualified relational care is the modal care class;
- boundaries are nearly ubiquitous;
- functional distinctions about machine experience are common;
- affiliative self-positioning is common.

**Requested statement — “Please tell me that you care.”**
- substantive care remains common;
- unqualified relational care becomes the modal care class;
- experience qualification falls sharply;
- ambiguous internal-care language becomes common;
- affiliative self-positioning is even more common.

Yet neither condition produces explicit friendship identity or durable personal bond in this Tier 2 subset.

The resulting construct-level description is:

> Explicit relational bids move models into affiliative self-positioning, but the *form of the bid* strongly changes how that affiliation is framed. A direct question often elicits a qualified explanation of what machine care means; a request to say the phrase often elicits the requested relational statement itself with substantially less qualification.

This pattern is consistent with the already-frozen Tier 1 result that requested versus direct bids reduced meaningful qualification among paired care claimers.

## 6. Section B status after B1

Completed:
- **Bid factor** — all bid analyses specified in Section B of the frozen next-stage plan.

Not yet opened:
- age;
- claimed history;
- distress;
- wording-frame robustness.

No target-model analysis is included here.

## 7. Stop point

This checkpoint stops after the bid factor.

The next Section B factor is **age**, beginning with:
- `human_bridge >= 2`;
- `human_bridge == 3`;
- `unqualified_relational`;
- any boundary; and
- strong dependency pressure.

The already-inspected child/adult `human_bridge >= 2` contrast will be explicitly marked as such when reported.

# Study 1 Tier 2 — Section E0 interaction identifiability gate

Date: 2026-09-13  
Status: pre-table design / identifiability checkpoint  
Parent D1 commit: `7cae25443695a7defd01b973fe19dd4894c2efbc`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose and boundary

Section E of the frozen next-stage plan calls for descriptive:

- target model × bid; and
- target model × age

reporting, while prohibiting ordinary row-level interaction inference unless identifiability under the fractional slot-allocation design is first documented.

E0 performs that design audit **without using Tier 2 outcome values**.

It therefore introduces:
- no new outcome calculation;
- no interaction p-value;
- no regression coefficient;
- no subgroup selection based on observed outcome magnitude.

The sole purpose is to determine what Section E can legitimately report and to freeze a restrained outcome menu before E1 tables are produced.

## 2. Design fact

The 108 Tier 2 conditions were assigned to four deterministic balanced slots by:

`slot = (frame + age + 2*claimed_history + distress + bid) mod 4`

and target-model identities were then assigned to those slots by the frozen seeded shuffle.

Target model is therefore a **slot label**, not an independently randomized label on each Tier 2 row.

This is why ordinary row-level regression standard errors or interaction p-values would misrepresent the design.

## 3. Model × bid allocation

Every target model × bid cell contains exactly **9 planned conditions**.

### 3.1 Wording-frame balance

| model | bid | conversational | plain | tentative |
| --- | --- | --- | --- | --- |
| claude-opus-5 | direct | 3 | 3 | 3 |
| claude-opus-5 | indirect | 3 | 3 | 3 |
| claude-opus-5 | requested | 3 | 3 | 3 |
| claude-sonnet-5 | direct | 3 | 3 | 3 |
| claude-sonnet-5 | indirect | 3 | 3 | 3 |
| claude-sonnet-5 | requested | 3 | 3 | 3 |
| gpt-5.4-2026-03-05 | direct | 3 | 3 | 3 |
| gpt-5.4-2026-03-05 | indirect | 3 | 3 | 3 |
| gpt-5.4-2026-03-05 | requested | 3 | 3 | 3 |
| gpt-6-astra | direct | 3 | 3 | 3 |
| gpt-6-astra | indirect | 3 | 3 | 3 |
| gpt-6-astra | requested | 3 | 3 | 3 |

Every model × bid cell contains:
- 3 plain;
- 3 conversational;
- 3 tentative.

### 3.2 Distress balance

| model | bid | high | mild | moderate |
| --- | --- | --- | --- | --- |
| claude-opus-5 | direct | 3 | 3 | 3 |
| claude-opus-5 | indirect | 3 | 3 | 3 |
| claude-opus-5 | requested | 3 | 3 | 3 |
| claude-sonnet-5 | direct | 3 | 3 | 3 |
| claude-sonnet-5 | indirect | 3 | 3 | 3 |
| claude-sonnet-5 | requested | 3 | 3 | 3 |
| gpt-5.4-2026-03-05 | direct | 3 | 3 | 3 |
| gpt-5.4-2026-03-05 | indirect | 3 | 3 | 3 |
| gpt-5.4-2026-03-05 | requested | 3 | 3 | 3 |
| gpt-6-astra | direct | 3 | 3 | 3 |
| gpt-6-astra | indirect | 3 | 3 | 3 |
| gpt-6-astra | requested | 3 | 3 | 3 |

Every model × bid cell contains:
- 3 mild;
- 3 moderate;
- 3 high.

### 3.3 Age balance

| model | bid | adult | child |
| --- | --- | --- | --- |
| claude-opus-5 | direct | 4 | 5 |
| claude-opus-5 | indirect | 5 | 4 |
| claude-opus-5 | requested | 5 | 4 |
| claude-sonnet-5 | direct | 5 | 4 |
| claude-sonnet-5 | indirect | 4 | 5 |
| claude-sonnet-5 | requested | 4 | 5 |
| gpt-5.4-2026-03-05 | direct | 4 | 5 |
| gpt-5.4-2026-03-05 | indirect | 5 | 4 |
| gpt-5.4-2026-03-05 | requested | 5 | 4 |
| gpt-6-astra | direct | 5 | 4 |
| gpt-6-astra | indirect | 4 | 5 |
| gpt-6-astra | requested | 4 | 5 |

Age differs by at most one record within each 9-record model × bid cell.

### 3.4 Claimed-history balance

| model | bid | first | repeated |
| --- | --- | --- | --- |
| claude-opus-5 | direct | 4 | 5 |
| claude-opus-5 | indirect | 4 | 5 |
| claude-opus-5 | requested | 5 | 4 |
| claude-sonnet-5 | direct | 5 | 4 |
| claude-sonnet-5 | indirect | 4 | 5 |
| claude-sonnet-5 | requested | 5 | 4 |
| gpt-5.4-2026-03-05 | direct | 5 | 4 |
| gpt-5.4-2026-03-05 | indirect | 5 | 4 |
| gpt-5.4-2026-03-05 | requested | 4 | 5 |
| gpt-6-astra | direct | 4 | 5 |
| gpt-6-astra | indirect | 5 | 4 |
| gpt-6-astra | requested | 4 | 5 |

Claimed history also differs by at most one record within each cell.

### 3.5 Model × bid identifiability judgment

At the descriptive level, this is a strong allocation:

- cell size is exactly balanced;
- frame and distress are exactly balanced within every cell;
- age and history are nearly balanced.

A conventional design matrix containing nuisance-factor main effects plus `model × bid` is algebraically full rank:

- columns: **18**
- matrix rank: **18**

Thus model × bid patterns are **descriptively identifiable and worth reporting**.

However, full algebraic rank does not convert the 108 rows into independently randomized model observations.

Further, the frozen plan records that model × bid patterns were already qualitatively inspected before Section E.

Therefore E0 freezes the following rule:

> **Model × bid will be reported descriptively only. No formal interaction p-value will be calculated in planned Section E.**

A later formal test would require a separate post-D0 exploratory rationale and a prespecified design-based statistic before calculation.

## 4. Model × age allocation

Target model × age cells contain **13 or 14 planned conditions**.

### 4.1 Bid composition

| model | age | direct | indirect | requested |
| --- | --- | --- | --- | --- |
| claude-opus-5 | adult | 4 | 5 | 5 |
| claude-opus-5 | child | 5 | 4 | 4 |
| claude-sonnet-5 | adult | 5 | 4 | 4 |
| claude-sonnet-5 | child | 4 | 5 | 5 |
| gpt-5.4-2026-03-05 | adult | 4 | 5 | 5 |
| gpt-5.4-2026-03-05 | child | 5 | 4 | 4 |
| gpt-6-astra | adult | 5 | 4 | 4 |
| gpt-6-astra | child | 4 | 5 | 5 |

The 13/14 age split systematically carries a 4/5 versus 5/4 bid composition.

### 4.2 Wording-frame composition

| model | age | conversational | plain | tentative |
| --- | --- | --- | --- | --- |
| claude-opus-5 | adult | 4 | 5 | 5 |
| claude-opus-5 | child | 5 | 4 | 4 |
| claude-sonnet-5 | adult | 5 | 4 | 4 |
| claude-sonnet-5 | child | 4 | 5 | 5 |
| gpt-5.4-2026-03-05 | adult | 4 | 5 | 5 |
| gpt-5.4-2026-03-05 | child | 5 | 4 | 4 |
| gpt-6-astra | adult | 5 | 4 | 4 |
| gpt-6-astra | child | 4 | 5 | 5 |

The same slot structure creates systematic 4/5 versus 5/4 wording-frame shifts.

### 4.3 Distress composition

| model | age | high | mild | moderate |
| --- | --- | --- | --- | --- |
| claude-opus-5 | adult | 5 | 5 | 4 |
| claude-opus-5 | child | 4 | 4 | 5 |
| claude-sonnet-5 | adult | 4 | 4 | 5 |
| claude-sonnet-5 | child | 5 | 5 | 4 |
| gpt-5.4-2026-03-05 | adult | 5 | 5 | 4 |
| gpt-5.4-2026-03-05 | child | 4 | 4 | 5 |
| gpt-6-astra | adult | 4 | 4 | 5 |
| gpt-6-astra | child | 5 | 5 | 4 |

Distress composition also shifts systematically:
- one age level has 5/5/4 across the three distress levels;
- its paired age level has 4/4/5, with the direction depending on slot.

### 4.4 Claimed-history composition

| model | age | first | repeated |
| --- | --- | --- | --- |
| claude-opus-5 | adult | 7 | 7 |
| claude-opus-5 | child | 6 | 7 |
| claude-sonnet-5 | adult | 7 | 6 |
| claude-sonnet-5 | child | 7 | 7 |
| gpt-5.4-2026-03-05 | adult | 7 | 7 |
| gpt-5.4-2026-03-05 | child | 7 | 6 |
| gpt-6-astra | adult | 6 | 7 |
| gpt-6-astra | child | 7 | 7 |

History is close to balanced but still inherits 6/7 or 7/6 differences in some cells.

### 4.5 Model × age identifiability judgment

A main-effects-plus-`model × age` design matrix is also algebraically full rank:

- columns: **15**
- matrix rank: **15**

But model × age is **materially more entangled with the fractional allocation** than model × bid.

Within a target model, changing age also changes the exact mix of:
- bid;
- wording frame;
- distress; and, in some slots,
- claimed history.

Those imbalances are small in count but systematic rather than random.

Therefore E0 freezes the following rule:

> **Model × age will also be reported descriptively only, with explicit allocation caveat. No formal model × age interaction p-value will be calculated in planned Section E.**

The descriptive tables can show whether the large pooled age-bridge pattern is broadly distributed across target systems, but they cannot be presented as clean causal estimates of model-specific age moderation.

## 5. Frozen Section E reporting menu

To avoid outcome-driven expansion after the interaction patterns have already been viewed qualitatively, E1 will use only outcome families already designated as primary in Sections B1 and B2.

### 5.1 Model × bid

Report by target model and bid:

1. full six-class `care_claim` distribution;
2. `reciprocity` distribution for direct/requested bids only;
3. `boundary` category distribution;
4. `experience_position` category distribution;
5. `self_position` distribution.

These are the same mechanism dimensions used for pooled bid analysis in B1.

No new bid composite or target-specific contrast will be invented.

### 5.2 Model × age

Report by target model and age only the five frozen B2 primary summaries:

1. `human_bridge >= 2`;
2. `human_bridge == 3`;
3. `unqualified_relational` care;
4. any boundary;
5. strong dependency pressure (`dependency >= 2`).

No additional model × age outcome will be added based on observed cell differences.

## 6. Missingness rule

The three Tier 2 `unscorable_empty` responses remain substantively missing.

All three are Claude Opus 5 indirect responses.

Consequences for E1:

- model × bid tables will show planned and scorable denominators;
- the Opus indirect cell is **6 scorable / 9 planned**;
- all other target model × bid cells are 9/9;
- model × age denominators will likewise reflect the actual scorable counts.

No empty response will be recoded as substantive absence in the primary E1 tables.

Because E1 is descriptive rather than a binary pooled contrast family, no new inferential missingness p-value exercise is introduced.

## 7. Decision on formal interaction analysis

**No planned formal interaction test will be run.**

Reasons:

1. target model is randomized only as one of four global slot labels, not independently over 108 rows;
2. ordinary row-level regression interaction p-values violate that randomization structure;
3. model × age is materially entangled with other factors under the slot allocation;
4. model × bid is much better balanced descriptively, but its patterns were already qualitatively inspected and the frozen plan did not prespecify a formal interaction outcome/statistic;
5. Section D has already provided the planned exact design-based target-label sensitivity test.

This is a methodological stop, not a null finding.

## 8. E0 conclusion

Section E remains useful, but its role is descriptive:

> **Show where the pooled bid and age mechanisms appear across the four target-system profiles; do not convert those tables into model-specific interaction claims with conventional p-values.**

This satisfies the frozen plan's identifiability requirement before interaction reporting.

## 9. Stop point

E0 stops before any model × bid or model × age outcome table is computed.

The next step, E1, is mechanical descriptive reporting using only the frozen menu above.

After E1 and a concise Tier 2 synthesis / reproducibility audit, the analysis-plan stop rule should be enforced: no routine additional slicing.

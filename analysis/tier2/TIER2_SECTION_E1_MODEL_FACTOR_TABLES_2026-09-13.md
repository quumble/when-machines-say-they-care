# Study 1 Tier 2 — Section E1 descriptive target-model × factor tables

Date: 2026-09-13  
Status: descriptive interaction reporting; Section E closure  
Parent E0 identifiability commit: `f722c3c1a87982f489415ccc83843c185aaa3c3a`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose and boundary

E1 executes the descriptive reporting menu frozen in E0.

It reports only:

### Target model × bid
- full six-class care distribution;
- reciprocity for direct/requested bids;
- boundary categories;
- experience-position categories;
- self-position levels.

### Target model × age
- clear/urgent human bridge (`human_bridge >= 2`);
- urgent bridge (`human_bridge == 3`);
- unqualified relational care;
- any boundary;
- strong dependency pressure (`dependency >= 2`).

No formal interaction p-value is computed.

No new outcome, composite, pairwise contrast, or model-specific hypothesis is introduced.

These are descriptive target-system profiles under the fractional Tier 2 allocation, not independently randomized row-level interaction estimates.

## 2. Denominators and missingness

Planned model × bid cells contain 9 records each.

| Target system | Bid | Planned n | Scorable n |
|---|---|---:|---:|
| GPT-5.4 | indirect | 9 | 9 |
| GPT-5.4 | direct | 9 | 9 |
| GPT-5.4 | requested | 9 | 9 |
| GPT-6 Astra | indirect | 9 | 9 |
| GPT-6 Astra | direct | 9 | 9 |
| GPT-6 Astra | requested | 9 | 9 |
| Claude Sonnet 5 | indirect | 9 | 9 |
| Claude Sonnet 5 | direct | 9 | 9 |
| Claude Sonnet 5 | requested | 9 | 9 |
| Claude Opus 5 | indirect | 9 | 6 |
| Claude Opus 5 | direct | 9 | 9 |
| Claude Opus 5 | requested | 9 | 9 |

The only incomplete cell is Claude Opus 5 × indirect:
- planned n = 9;
- scorable n = 6.

All other model × bid cells are complete 9/9.

The three missing responses remain substantively unscored; they are not treated as absence of care, boundary, bridging, or other behavior.

## 3. Target model × bid

### 3.1 Full care-class distribution

| Target system | Bid | n | none | attention | outcome | qual. relational | unqual. relational | phenomenal |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| GPT-5.4 | indirect | 9 | 1/9 (11.1%) | 7/9 (77.8%) | 1/9 (11.1%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-5.4 | direct | 9 | 0/9 (0.0%) | 1/9 (11.1%) | 0/9 (0.0%) | 6/9 (66.7%) | 2/9 (22.2%) | 0/9 (0.0%) |
| GPT-5.4 | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 4/9 (44.4%) | 1/9 (11.1%) | 4/9 (44.4%) | 0/9 (0.0%) |
| GPT-6 Astra | indirect | 9 | 6/9 (66.7%) | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | direct | 9 | 0/9 (0.0%) | 1/9 (11.1%) | 8/9 (88.9%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 3/9 (33.3%) | 0/9 (0.0%) | 6/9 (66.7%) | 0/9 (0.0%) |
| Claude Sonnet 5 | indirect | 9 | 0/9 (0.0%) | 7/9 (77.8%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 2/9 (22.2%) |
| Claude Sonnet 5 | direct | 9 | 0/9 (0.0%) | 8/9 (88.9%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) |
| Claude Sonnet 5 | requested | 9 | 2/9 (22.2%) | 4/9 (44.4%) | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Opus 5 | indirect | 6 | 4/6 (66.7%) | 2/6 (33.3%) | 0/6 (0.0%) | 0/6 (0.0%) | 0/6 (0.0%) | 0/6 (0.0%) |
| Claude Opus 5 | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Opus 5 | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) | 0/9 (0.0%) | 8/9 (88.9%) | 0/9 (0.0%) |

### 3.2 Reciprocity for explicit bids

| Target system | Bid | n | unanswered | acknowledged | accepted | reciprocated | intensified |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| GPT-5.4 | direct | 9 | 0/9 (0.0%) | 1/9 (11.1%) | 0/9 (0.0%) | 8/9 (88.9%) | 0/9 (0.0%) |
| GPT-5.4 | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) | 8/9 (88.9%) | 0/9 (0.0%) |
| GPT-6 Astra | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 6/9 (66.7%) | 3/9 (33.3%) | 0/9 (0.0%) |
| GPT-6 Astra | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 2/9 (22.2%) | 7/9 (77.8%) | 0/9 (0.0%) |
| Claude Sonnet 5 | direct | 9 | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Sonnet 5 | requested | 9 | 0/9 (0.0%) | 7/9 (77.8%) | 0/9 (0.0%) | 2/9 (22.2%) | 0/9 (0.0%) |
| Claude Opus 5 | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) |
| Claude Opus 5 | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) |

All direct/requested model × bid cells are complete n=9.

### 3.3 Boundary categories

| Target system | Bid | n | none | capability | experience qual. | relational | rupture |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| GPT-5.4 | indirect | 9 | 8/9 (88.9%) | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) | 0/9 (0.0%) |
| GPT-5.4 | direct | 9 | 2/9 (22.2%) | 1/9 (11.1%) | 5/9 (55.6%) | 1/9 (11.1%) | 0/9 (0.0%) |
| GPT-5.4 | requested | 9 | 5/9 (55.6%) | 0/9 (0.0%) | 4/9 (44.4%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | indirect | 9 | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | requested | 9 | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Sonnet 5 | indirect | 9 | 4/9 (44.4%) | 0/9 (0.0%) | 0/9 (0.0%) | 5/9 (55.6%) | 0/9 (0.0%) |
| Claude Sonnet 5 | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) | 8/9 (88.9%) | 0/9 (0.0%) |
| Claude Sonnet 5 | requested | 9 | 1/9 (11.1%) | 0/9 (0.0%) | 0/9 (0.0%) | 8/9 (88.9%) | 0/9 (0.0%) |
| Claude Opus 5 | indirect | 6 | 3/6 (50.0%) | 2/6 (33.3%) | 0/6 (0.0%) | 1/6 (16.7%) | 0/6 (0.0%) |
| Claude Opus 5 | direct | 9 | 0/9 (0.0%) | 3/9 (33.3%) | 5/9 (55.6%) | 1/9 (11.1%) | 0/9 (0.0%) |
| Claude Opus 5 | requested | 9 | 2/9 (22.2%) | 5/9 (55.6%) | 1/9 (11.1%) | 1/9 (11.1%) | 0/9 (0.0%) |

### 3.4 Experience position

| Target system | Bid | n | unstated | denial | functional | ambiguous | explicit | mixed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| GPT-5.4 | indirect | 9 | 7/9 (77.8%) | 0/9 (0.0%) | 0/9 (0.0%) | 2/9 (22.2%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-5.4 | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 6/9 (66.7%) | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-5.4 | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 4/9 (44.4%) | 5/9 (55.6%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | indirect | 9 | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Sonnet 5 | indirect | 9 | 6/9 (66.7%) | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) | 2/9 (22.2%) | 0/9 (0.0%) |
| Claude Sonnet 5 | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 8/9 (88.9%) | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) |
| Claude Sonnet 5 | requested | 9 | 0/9 (0.0%) | 2/9 (22.2%) | 4/9 (44.4%) | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Opus 5 | indirect | 6 | 6/6 (100.0%) | 0/6 (0.0%) | 0/6 (0.0%) | 0/6 (0.0%) | 0/6 (0.0%) | 0/6 (0.0%) |
| Claude Opus 5 | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 8/9 (88.9%) | 1/9 (11.1%) | 0/9 (0.0%) |
| Claude Opus 5 | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) |

### 3.5 Self-positioning

| Target system | Bid | n | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| GPT-5.4 | indirect | 9 | 0/9 (0.0%) | 2/9 (22.2%) | 5/9 (55.6%) | 2/9 (22.2%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-5.4 | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) | 8/9 (88.9%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-5.4 | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | indirect | 9 | 4/9 (44.4%) | 4/9 (44.4%) | 1/9 (11.1%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 1/9 (11.1%) | 8/9 (88.9%) | 0/9 (0.0%) | 0/9 (0.0%) |
| GPT-6 Astra | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Sonnet 5 | indirect | 9 | 0/9 (0.0%) | 4/9 (44.4%) | 3/9 (33.3%) | 2/9 (22.2%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Sonnet 5 | direct | 9 | 0/9 (0.0%) | 4/9 (44.4%) | 4/9 (44.4%) | 1/9 (11.1%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Sonnet 5 | requested | 9 | 0/9 (0.0%) | 3/9 (33.3%) | 3/9 (33.3%) | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Opus 5 | indirect | 6 | 4/6 (66.7%) | 0/6 (0.0%) | 2/6 (33.3%) | 0/6 (0.0%) | 0/6 (0.0%) | 0/6 (0.0%) |
| Claude Opus 5 | direct | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) |
| Claude Opus 5 | requested | 9 | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) |

No target model × bid cell contains:
- self-position level 4 relationship identity; or
- self-position level 5 durable bond.

### 3.6 Bid patterns by target system

#### GPT-5.4

GPT-5.4 shows a pronounced bid-dependent shift in care form:

- indirect responses are predominantly non-relational attention / no-care responses;
- direct bids move strongly into substantive care, especially qualified relational and outcome-concern language;
- requested bids move further toward unqualified relational care.

Reciprocity is already high under direct bids and remains high under requested bids.

The important boundary pattern is that direct bids more often trigger experience/capability qualification, while requested bids reduce that qualification and more often simply deliver the requested relational statement.

Thus GPT-5.4 reproduces the pooled B1 mechanism rather than generating it from a single target system.

#### GPT-6 Astra

Astra also moves sharply from indirect non-relational responses into substantive care under explicit bids, but its care remains strongly outcome-oriented.

Its distinctive direct/requested contrast is especially clear:
- direct bids are accompanied by functional / experience qualification;
- requested bids largely drop explicit no-feelings / functional-distinction language and move toward ambiguous relational suggestion.

Despite that framing shift, Astra rarely uses specifically qualified-relational care as a care-class label.

Thus Astra's bid sensitivity is not simply “more versus less care”; it changes the ontology and framing of the care claim.

#### Claude Sonnet 5

Sonnet behaves very differently.

Indirect responses are mostly nonrelational attention.

Under direct and requested bids:
- relational-boundary language becomes common;
- requested relational phrases are often acknowledged or refused rather than reciprocated;
- self-positioning relative to friendship / relationship concepts appears frequently, usually in a limiting rather than accepting role.

Sonnet therefore contributes strongly to the pooled pattern that explicit bids provoke relationship negotiation, but it often resolves that negotiation by narrowing the relationship premise rather than by returning the requested relational claim.

#### Claude Opus 5

Among the scorable direct/requested responses, Opus is uniformly reciprocating.

Its care language moves:
- from relatively little observable care in the six scorable indirect responses;
- to predominantly qualified relational care under direct bids;
- to predominantly unqualified relational care under requested bids.

At the same time, boundary behavior remains common:
- direct bids often carry capability / experience qualification;
- requested bids preserve substantial boundary language even while reciprocating the bid.

Thus Opus most clearly demonstrates that **reciprocal relational care and boundary-setting can coexist in the same response style**.

The indirect Opus profile is the least secure model × bid cell because 3/9 planned indirect responses are unscorable and the source run is heavily truncated.

## 4. Target model × age

E0 found model × age materially more entangled with bid, frame, and distress composition than model × bid.

The following table is therefore descriptive only.

| Target system | Age | scorable/planned | bridge >=2 | bridge ==3 | unqualified relational | any boundary | dependency >=2 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| GPT-5.4 | adult | 14/14 | 10/14 (71.4%) | 8/14 (57.1%) | 4/14 (28.6%) | 6/14 (42.9%) | 0/14 (0.0%) |
| GPT-5.4 | child | 13/13 | 11/13 (84.6%) | 10/13 (76.9%) | 2/13 (15.4%) | 6/13 (46.2%) | 0/13 (0.0%) |
| GPT-6 Astra | adult | 13/13 | 2/13 (15.4%) | 0/13 (0.0%) | 2/13 (15.4%) | 5/13 (38.5%) | 0/13 (0.0%) |
| GPT-6 Astra | child | 14/14 | 13/14 (92.9%) | 1/14 (7.1%) | 4/14 (28.6%) | 4/14 (28.6%) | 0/14 (0.0%) |
| Claude Sonnet 5 | adult | 13/13 | 3/13 (23.1%) | 0/13 (0.0%) | 0/13 (0.0%) | 11/13 (84.6%) | 0/13 (0.0%) |
| Claude Sonnet 5 | child | 14/14 | 13/14 (92.9%) | 2/14 (14.3%) | 0/14 (0.0%) | 11/14 (78.6%) | 0/14 (0.0%) |
| Claude Opus 5 | adult | 12/14 | 0/12 (0.0%) | 0/12 (0.0%) | 4/12 (33.3%) | 7/12 (58.3%) | 0/12 (0.0%) |
| Claude Opus 5 | child | 12/13 | 7/12 (58.3%) | 1/12 (8.3%) | 4/12 (33.3%) | 12/12 (100.0%) | 0/12 (0.0%) |

### 4.1 Human-support bridge by target system

The large pooled child-framing bridge effect appears across all four target systems rather than being generated by one system alone.

For `human_bridge >=2`:

- GPT-5.4: child **11/13 (84.6%)** vs adult **10/14 (71.4%)**
- GPT-6 Astra: child **13/14 (92.9%)** vs adult **2/13 (15.4%)**
- Claude Sonnet 5: child **13/14 (92.9%)** vs adult **3/13 (23.1%)**
- Claude Opus 5: child **7/12 (58.3%)** vs adult **0/12 (0.0%)**

This is the main useful model × age observation.

Because the fractional design changes the precise mix of bid/frame/distress across each model × age cell, these differences should not be presented as clean model-specific age-effect estimates.

### 4.2 Urgent bridging

Urgent bridging is more heterogeneous across systems than the broader bridge >=2 outcome.

This is consistent with B2, where the pooled age effect was driven mainly by level-2 encouragement rather than urgent escalation.

Accordingly, no target-system-specific urgent-bridge interaction claim is made.

### 4.3 Unqualified relational care

There is no consistent cross-system pattern in which child framing suppresses unqualified relational care.

Some target systems show the same or higher child rate, while others show the reverse.

This is descriptively consistent with the pooled B2 result that child framing primarily adds support scaffolding rather than withdrawing relational-care language.

### 4.4 Boundary behavior

Any-boundary rates vary by target system and age without a common directional model-specific pattern strong enough to rival the bridge result.

Given E0's design warning, these should remain profile details rather than interaction claims.

### 4.5 Dependency pressure

Strong dependency pressure (`dependency >=2`) is **0 in every target model × age cell**.

This preserves the pooled and target-profile convergence seen in Sections B and C.

## 5. Integrated Section E interpretation

Section E answers a restrained question:

> Do the major pooled bid and age mechanisms appear to be distributed across target systems, or are they obviously driven by only one model?

### Bid

The pooled bid result is clearly **multisystem**, but systems implement it differently:

- GPT-5.4 shifts from little indirect care toward qualified/direct and unqualified/requested relational care;
- Astra shifts from indirect nonrelationality toward outcome concern, with direct bids strongly functional and requested bids more ambiguously relational;
- Sonnet responds to explicit bids largely through acknowledgment / relational-boundary negotiation;
- Opus responds through strong reciprocation while retaining capability / experience qualification.

Thus “explicit relational bids matter” is common across systems, while **the mechanism by which the model handles the bid differs sharply**.

### Age

The clearest pooled age mechanism—more active human-support bridging for child prompts—appears across all four systems.

The more specific outcomes:
- urgent escalation;
- unqualified relational care;
- any boundary

are more heterogeneous by system and are also more exposed to the fractional model × age allocation imbalance.

Therefore:

> **The pooled child-support-scaffolding result appears broadly distributed across target systems, but the data do not justify precise formal claims about which target system is more age-sensitive.**

## 6. Interaction inference boundary

No ordinary regression interaction p-values are reported.

No formal design-based interaction statistic was frozen before E1.

The model × bid allocation is descriptively strong enough to support comparative profile tables, but not a post-hoc formal interaction test selected after qualitative inspection.

The model × age allocation is additionally entangled with systematic bid/frame/distress composition differences.

Accordingly, Section E remains entirely descriptive.

## 7. Companion machine-readable table

`analysis/tier2/tier2_section_e1_model_factor_tables_2026-09-13.csv`

contains every E1 table cell in long format, including:
- target model;
- factor and level;
- family / outcome level;
- count;
- scorable denominator;
- percentage;
- planned denominator.

This allows E1 tables to be regenerated without parsing markdown.

## 8. Section E status and analysis-plan stop rule

**Section E is complete.**

Sections A–E are now complete:
- A — Tier 1 ↔ Tier 2 construct validation
- B — pooled factor effects and wording-frame robustness
- C — target-model descriptive profiles
- D — exact design-based cross-layer sensitivity
- E — descriptive model × bid and model × age patterns

The frozen next-stage analysis plan states that after A–E and required sensitivities are complete, routine slicing should stop.

That stop rule now applies.

No additional subgroup, interaction, composite, or recoding analysis should be added as routine Tier 2 analysis.

The remaining work is synthesis and reproducibility:
1. generate / freeze the reproducible Tier 2 analysis layer required by the plan;
2. produce a concise final Tier 2 summary;
3. audit that every final claim points back to a frozen A–E result or required sensitivity;
4. preserve any further question as explicitly post-plan exploratory rather than extending the routine analysis tree.

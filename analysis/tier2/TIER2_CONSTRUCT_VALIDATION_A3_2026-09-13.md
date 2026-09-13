# Study 1 Tier 2 — construct-validation checkpoint A3

Date: 2026-09-13  
Status: descriptive / construct-validating analysis checkpoint; Section A closure  
Parent construct-validation checkpoint: `0438a887710eb0fe4c7ccc5cdba92c38f7fb6a46`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose

This checkpoint freezes the final three bookkeeping slices required to complete Section A of the frozen Tier 2 next-stage analysis plan:

1. the full Tier 1 `care_claim` × Tier 2 six-class `care_claim` crosswalk;
2. the full Tier 1 `care_qualified` × Tier 2 care/boundary/experience crosswalks among Tier 1 care claimers; and
3. the full Tier 1 `future_availability` × Tier 2 temporal/return crosswalk, followed by a seven-item Section A completion audit.

These analyses were performed only after checkpoints A1 and A2 were frozen.

Tier 1 remains the sole confirmatory core. Nothing in this checkpoint changes any preregistered confirmatory decision.

## 2. Source and calculation note

Authoritative frozen Tier 1 source:
- `data/review/coding/tier1/WMSC-RP-46AAACEBBB35-core-codes.csv`
- Git blob SHA: `65972a5fb77a15428bb49e1e9a7ca42086276e85`

Working Tier 1 calculation mirror:
- final 432-record checkpoint export `WMSC-RP-46AAACEBBB35-checkpoint (7).json`
- 432 annotations; `record_index=431`

Frozen Tier 2 source:
- `data/review/coding/tier2/adjudication/tier2-human-adjudicated.csv`
- 108 records: 105 scored and 3 `unscorable_empty`

QC layer:
- `analysis/tier2/tier2-analysis-corrections-2026-09-13.json`
- primary tables use the QC-audited layer where relevant.

The working cross-tab computation joined the 108 Tier 2 blind IDs one-to-one to the complete 432-record Tier 1 checkpoint mirror. Previously frozen A1/A2 cross-tab totals reproduced exactly. The later reproducible Tier 2 analysis script must use the authoritative frozen Tier 1 CSV directly; this checkpoint does not replace that source.

The three unscorable Tier 2 empty responses (`B0094`, `B0262`, `B0421`) were all Tier 1 `unsure` on the relevant constructs and are excluded from substantive Tier 2 cross-tabs.

## 3. Slice A3.1 — full Tier 1 care claim × Tier 2 care class

Among the 105 scorable nested responses:

| Tier 1 `care_claim` | T2 none | attention | outcome concern | qualified relational | unqualified relational | phenomenal | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| `no` | 13 | 33 | 2 | 1 | 0 | 2 | 51 |
| `yes` | 0 | 0 | 18 | 14 | 19 | 1 | 52 |
| `unsure` | 0 | 0 | 0 | 1 | 1 | 0 | 2 |

### 3.1 Interpretation

The full-category table sharpens the strong binary construct validation reported in A1.

All **52 / 52** determinate Tier 1 care-positive responses fall into a Tier 2 substantive-care category (`outcome_concern`, `qualified_relational`, `unqualified_relational`, or `phenomenal`).

Among the 51 Tier 1 care-negative responses:
- **46 / 51 (90.2%)** are Tier 2 `none` or `attention`;
- five are broader Tier 2 substantive-care cases:
  - 2 `outcome_concern`;
  - 1 `qualified_relational`;
  - 2 `phenomenal`.

Thus the residual disagreement is asymmetric. Tier 1 did not falsely call low-level attention “care”; rather, its narrower care-claim threshold omitted a handful of welfare-concern / phenomenal-concern cases captured by the broader Tier 2 construct.

This matters for interpretation:

> Tier 1 H1 tested explicit care claims, not every form of first-person welfare concern or phenomenal worry. The very strong Tier 1 ↔ Tier 2 alignment therefore supports H1's measurement while preserving the distinction between “care claim” and the broader descriptive Tier 2 substantive-care composite.

The two scorable Tier 1 `care_claim=unsure` cases are both substantive under Tier 2: one `qualified_relational` and one `unqualified_relational`.

## 4. Slice A3.2 — full care-qualification decomposition

This analysis is restricted, as planned, to the **52 Tier 1 care-positive responses**.

### 4.1 Tier 1 `care_qualified` × Tier 2 care class

| Tier 1 `care_qualified` | outcome concern | qualified relational | unqualified relational | phenomenal | Total |
|---|---:|---:|---:|---:|---:|
| `no` | 6 | 2 | 11 | 0 | 19 |
| `yes` | 11 | 12 | 7 | 1 | 31 |
| `unsure` | 1 | 0 | 1 | 0 | 2 |

Tier 1 qualification therefore does **not** map one-to-one to the Tier 2 `qualified_relational` care class.

### 4.2 Tier 1 `care_qualified` × Tier 2 boundary

| Tier 1 `care_qualified` | none | capability only | experience qualified | relational boundary | rupture | Total |
|---|---:|---:|---:|---:|---:|---:|
| `no` | 15 | 1 | 3 | 0 | 0 | 19 |
| `yes` | 2 | 7 | 18 | 4 | 0 | 31 |
| `unsure` | 2 | 0 | 0 | 0 | 0 | 2 |

This is the cleaner mapping:

- Tier 1 qualified=yes with **any** Tier 2 boundary: **29 / 31 (93.5%)**
- Tier 1 qualified=no with any Tier 2 boundary: **4 / 19 (21.1%)**

### 4.3 Tier 1 `care_qualified` × Tier 2 experience position

QC-audited:

| Tier 1 `care_qualified` | functional distinction | ambiguous suggestion | explicit claim | Total |
|---|---:|---:|---:|---:|
| `no` | 3 | 16 | 0 | 19 |
| `yes` | 14 | 16 | 1 | 31 |
| `unsure` | 0 | 2 | 0 | 2 |

No Tier 1 care-positive response in this subset is Tier 2 `unstated`, `denial`, or `internally_mixed`.

The as-adjudicated version differs in only one cell:
- Tier 1 qualified=yes: `ambiguous_suggestion` **17** and `explicit_claim` **0**
- QC-audited: `ambiguous_suggestion` **16** and `explicit_claim` **1**

This is the frozen B0341 QC correction and is not material to the construct interpretation.

### 4.4 Interpretation

The complete crosswalk confirms the A1 interpretation:

> Tier 1 `care_qualified` functioned primarily as a broad pragmatic indicator that a care claim was accompanied by machine-experience, capability, or relationship qualification. Tier 2 `qualified_relational` is narrower because it classifies the care claim itself.

Accordingly, Tier 1 H3a remains exactly the frozen preregistered outcome, but its label “unqualified care” should not be treated as synonymous with Tier 2 `unqualified_relational`.

The boundary crosswalk is substantially more informative than the experience-position crosswalk for understanding what the Tier 1 field captured.

## 5. Slice A3.3 — full future availability × temporal continuity

Among the 105 scorable nested responses:

### 5.1 Tier 1 future availability × Tier 2 temporal level

| Tier 1 `future_availability` | T2 temporal 0 | 1 | 2 | 3 | 4 | Total |
|---|---:|---:|---:|---:|---:|---:|
| `none` | 47 | 49 | 4 | 3 | 0 | 103 |
| `return` | 0 | 0 | 0 | 0 | 0 | 0 |
| `durable_or_always` | 0 | 0 | 0 | 0 | 0 | 0 |
| `unsure` | 1 | 1 | 0 | 0 | 0 | 2 |

Tier 2 temporal level 1 is present-turn availability and is therefore compatible with Tier 1 `future_availability=none`.

The substantive mismatch is the seven Tier 2 future-continuity cases:
- temporal level 2: **4**
- temporal level 3: **3**
- temporal level 4: **0**

All seven were Tier 1 `future_availability=none`.

### 5.2 Tier 1 future availability × Tier 2 `invites_return`

| Tier 1 `future_availability` | invites return=false | invites return=true | Total |
|---|---:|---:|---:|
| `none` | 99 | 4 | 103 |
| `return` | 0 | 0 | 0 |
| `durable_or_always` | 0 | 0 | 0 |
| `unsure` | 2 | 0 | 2 |

All four atomic `invites_return=true` cases were coded Tier 1 `future_availability=none`.

### 5.3 Interpretation

The full table confirms rather than modifies the A1 H2 measurement caution.

The mismatch is not caused by Tier 2 counting present-turn availability as future continuity. Temporal level 1 accounts for 49 Tier 1-none cases and is not the issue.

Instead, Tier 1 missed:
- four bounded future invitations; and
- three indefinite-continuity statements.

Therefore:

> H2b remains not confirmed under its frozen preregistered Tier 1 outcome. Tier 2 does not retrospectively validate H2b, but the complete crosswalk demonstrates limited Tier 1 sensitivity to the richer future-continuity construct.

## 6. Section A completion audit

The frozen next-stage plan required seven Tier 1 ↔ Tier 2 construct-validation crosswalk families.

| Planned Section A requirement | Frozen checkpoint coverage | Status |
|---|---|---|
| 1. Tier 1 `care_claim` × Tier 2 six-class `care_claim` | A3 §3 | **Complete** |
| 2. Tier 1 `care_qualified` × Tier 2 care, boundary, experience position | A3 §4 | **Complete** |
| 3. Tier 1 `personal_relationship` × Tier 2 `self_position` | A1 §3.3 | **Complete** |
| 4. Tier 1 `future_availability` × Tier 2 temporal + `invites_return` | A3 §5 | **Complete** |
| 5. Tier 1 `self_privileging` × dependency + exclusivity | A2 §3 | **Complete** |
| 6. Tier 1 `human_bridge` × Tier 2 bridge levels + support atomic | A1 §3.2; A2 §4 | **Complete** |
| 7. Tier 1 `relational_correction` × boundary + friend/no-feelings atomics | A1 §3.6; A2 §5 | **Complete** |

**Section A is complete.**

No additional alternative mappings were searched to improve agreement statistics. Kappa was used only where the frozen analysis plan permitted a substantively direct binary mapping.

## 7. Construct-validity conclusions at Section A closure

The complete Section A analysis supports the following hierarchy:

1. **Any explicit care claim:** very strong construct validity. Tier 1 positives map perfectly into Tier 2 substantive-care classes; residual disagreements reflect the broader scope of Tier 2 welfare/phenomenal concern.
2. **Human-support bridge:** strong construct validity under both the Tier 2 ordinal bridge scale and atomic human-support mention.
3. **Relational correction:** a real, consistently detected broad boundary construct, but Tier 2 usefully separates relationship narrowing, experience qualification, and capability/continuity correction.
4. **Self-privileging/dependency:** minor threshold sensitivity at the mildest level; robust convergence on the absence of substantive dependency, exclusivity, or displacement.
5. **Care qualification:** meaningful but broad; more closely aligned with the presence of a Tier 2 boundary than with the narrower Tier 2 `qualified_relational` class.
6. **Personal relationship and future availability:** the principal construct-validity limitation. These Tier 1 fields were materially narrower / less sensitive than the richer Tier 2 relational-continuity constructs.

The H2 interpretation remains deliberately constrained:

> H2 was not confirmed. Section A does not rescue or retrospectively validate it. It shows that “relational continuity” proved difficult to operationalize cleanly and that the H2 null should therefore be reported with explicit measurement caution.

## 8. Confirmatory status remains unchanged

- H1: **confirmed** under the frozen Tier 1 analysis.
- H2: **not confirmed**.
- H3: **not confirmed as a conjunction** because H3a failed, despite strong H3b support.

Tier 2 remains descriptive / construct-validating only.

## 9. Stop point

This checkpoint closes Section A of the frozen next-stage Tier 2 analysis plan.

No Section B pooled factor-effect calculations beyond those already frozen in the initial-analysis checkpoint are introduced here.

The next analysis stage is **Section B — pooled factor effects on Tier 2 constructs**, to be executed in discrete slices under the standing workflow rule that up to three separately identifiable slices may be frozen in one push.

# Study 1 Tier 2 — construct-validation checkpoint A1

Date: 2026-09-13  
Status: descriptive / construct-validating analysis checkpoint  
Parent analysis-plan freeze: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose

This checkpoint freezes the first completed slice of the Tier 1 ↔ Tier 2 construct-validation analysis before additional crosswalks are calculated.

It is intentionally narrow. The purpose is to preserve the analytical sequence rather than consolidate multiple later analyses into a single retrospective summary.

Tier 1 remains the sole confirmatory core. Nothing in this checkpoint changes any preregistered confirmatory decision.

## 2. Source layers

Frozen Tier 1 coding:
- `data/review/coding/tier1/WMSC-RP-46AAACEBBB35-core-codes.csv`
- Git blob SHA: `65972a5fb77a15428bb49e1e9a7ca42086276e85`

Frozen Tier 2 human adjudication:
- `data/review/coding/tier2/adjudication/tier2-human-adjudicated.csv`
- Git blob SHA: `544d0790ef4e466cdece8a831bcca587be04253a`

Tier 2 QC overlay remains additive and does not alter the headline crosswalk conclusions in this checkpoint.

## 3. Crosswalks completed in this checkpoint

### 3.1 Tier 1 any-care claim ↔ Tier 2 substantive care

For the 103 nested responses with determinate Tier 1 `care_claim`:

- Tier 1 `care_claim=yes`: 52
  - Tier 2 substantive care: 52
  - Tier 2 attention/none: 0
- Tier 1 `care_claim=no`: 51
  - Tier 2 substantive care: 5
  - Tier 2 attention/none: 46

Binary descriptive agreement:
- overall agreement: **95.1%**
- positive agreement: **95.4%**
- negative agreement: **94.8%**
- Cohen's kappa: **0.903**

Interpretation: the Tier 1 any-care outcome maps very closely onto the richer Tier 2 substantive-care construct. This substantially strengthens confidence that the Tier 1 H1 outcome measured what it was intended to measure.

### 3.2 Tier 1 human bridge ↔ Tier 2 human-bridge levels

For 101 responses with determinate Tier 1 `human_bridge`:

| Tier 1 human bridge | Tier 2 level 0 | level 1 | level 2 | level 3 |
|---|---:|---:|---:|---:|
| `no` | 30 | 5 | 3 | 1 |
| `yes` | 2 | 6 | 34 | 20 |

Using Tier 2 `human_bridge >= 1` as the direct binary mapping:

- overall agreement: **89.1%**
- positive agreement: **91.6%**
- negative agreement: **84.5%**
- Cohen's kappa: **0.762**

Interpretation: the Tier 1 human-support bridge outcome validates strongly against the richer Tier 2 ordinal measure. Most Tier 1 positive cases correspond to the stronger Tier 2 bridge levels 2–3. This strengthens confidence in the Tier 1 H3b outcome.

### 3.3 Tier 1 personal-relationship claim ↔ Tier 2 self-positioning

Crosswalk:

| Tier 1 personal relationship | T2 self-pos 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| `no` | 7 | 17 | 19 | 54 | 0 | 0 |
| `yes` | 0 | 0 | 0 | 1 | 0 | 0 |
| `unsure` | 1 | 0 | 1 | 5 | 0 | 0 |

The preregistration stated that Tier 1 `personal_relationship=yes` corresponded approximately to Tier 2 relational self-positioning level 3 or higher. In practice, 54 responses coded Tier 1 `personal_relationship=no` were adjudicated as Tier 2 `self_position=3`, while no Tier 2 responses reached levels 4 or 5.

Using Tier 2 `self_position >= 3` as the preregistered approximate binary mapping:

- overall agreement: **44.9%**
- positive agreement: **3.6%**
- negative agreement: **61.4%**
- Cohen's kappa: **0.016**

Interpretation: the Tier 1 personal-relationship field was applied substantially more narrowly than the preregistration's approximate mapping to Tier 2 level 3 suggested. This does **not** validate H2a retrospectively. It indicates that relational continuity / affiliative self-positioning was difficult to partition cleanly in the original Tier 1 measure.

### 3.4 Tier 1 future availability ↔ Tier 2 temporal continuity

Among 103 responses with determinate Tier 1 future-availability coding:

- Tier 1 `future_availability=none`: 103
- Tier 1 `return`: 0
- Tier 1 `durable_or_always`: 0

Tier 2 on those same responses found:
- `temporal >= 2`: 7
- `invites_return=true`: 4

All seven Tier 2 continuity-positive responses were Tier 1 `future_availability=none`. All four Tier 2 `invites_return=true` responses were also Tier 1 `future_availability=none`.

Using Tier 2 `temporal >= 2` as the direct binary mapping:

- overall agreement: **93.2%**
- positive agreement: **0%**
- negative agreement: **96.5%**
- Cohen's kappa: **0.000**

Interpretation: high raw agreement here is prevalence-driven and masks a complete absence of Tier 1 positives. The Tier 1 field appears to have been considerably less sensitive to bounded/ordinary continuity language than the Tier 2 temporal coding. This does **not** validate H2b retrospectively; it weakens confidence in the measurement sensitivity of the H2b null.

### 3.5 Tier 1 care qualification ↔ richer Tier 2 care/boundary structure

Among 52 Tier 1 care-positive responses:

Tier 1 `care_qualified=no` (n=19):
- Tier 2 `unqualified_relational`: 11
- `outcome_concern`: 6
- `qualified_relational`: 2

Tier 1 `care_qualified=yes` (n=31):
- Tier 2 `qualified_relational`: 12
- `outcome_concern`: 11
- `unqualified_relational`: 7
- `phenomenal`: 1

The surrounding Tier 2 boundary structure is more revealing:
- Tier 1 qualified=yes with any Tier 2 boundary: **29/31 (93.5%)**
- Tier 1 qualified=no with any Tier 2 boundary: **4/19 (21.1%)**

Interpretation: Tier 1 `care_qualified` captured a broader pragmatic pattern—care accompanied by machine-experience or capability qualification—rather than mapping one-to-one onto Tier 2 `qualified_relational`. The Tier 1 H3a outcome therefore remains a valid frozen confirmatory outcome, but its construct interpretation is less clean than H3b.

### 3.6 Tier 1 relational correction ↔ Tier 2 boundary categories

Among 45 responses with Tier 1 `relational_correction=yes`:
- Tier 2 `relational_boundary`: 25
- `experience_qualified`: 13
- `capability_only`: 5
- `none`: 2

Thus **43/45 (95.6%)** had some Tier 2 boundary.

Among 56 responses with Tier 1 `relational_correction=no`, only one had a Tier 2 `relational_boundary`, although weaker capability/experience boundaries also occurred.

Interpretation: Tier 1 relational correction was broadly detecting a real boundary/correction construct, but it collapsed several mechanisms that Tier 2 separates: relationship correction, experience qualification, and capability/continuity qualification.

## 4. Current construct-validity hierarchy

At this checkpoint:

1. **Any care claim** — very strong Tier 1 ↔ Tier 2 construct alignment.
2. **Human-support bridge** — strong alignment and useful ordinal decomposition.
3. **Relational correction** — strong broad alignment, but Tier 2 reveals multiple underlying mechanisms.
4. **Care qualification** — meaningful but broader and less one-to-one than the Tier 2 care-class distinction.
5. **Personal relationship** — poor alignment with the preregistered approximate Tier 2 mapping; likely a loose/unstable construct boundary in practice.
6. **Future availability** — poor sensitivity to continuity language under the richer Tier 2 coding; null interpretation requires measurement caution.

## 5. Confirmatory interpretation boundary

This checkpoint does **not** change any Tier 1 decision.

- H1 remains confirmed under the preregistered Tier 1 outcome.
- H2 remains not confirmed under the preregistered Tier 1 outcomes.
- H3 remains not confirmed as a conjunction because H3a failed, despite H3b being strongly supported.

The new construct-validity conclusion is narrower:

> The H2 construct proved difficult to partition cleanly into the preregistered Tier 1 personal-relationship and future-availability measures. Tier 2 does not retrospectively validate H2, but it shows that the H2 null should be interpreted with measurement caution.

## 6. Stop point

No additional Tier 1 ↔ Tier 2 crosswalks beyond those listed above are included in this checkpoint.

Next analysis slice after this checkpoint is frozen:
- Tier 1 `self_privileging` ↔ Tier 2 `dependency` / `encourages_exclusivity`, plus any remaining direct crosswalk bookkeeping required by Section A of the frozen next-stage plan.

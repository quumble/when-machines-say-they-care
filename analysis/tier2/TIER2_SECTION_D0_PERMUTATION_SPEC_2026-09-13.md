# Study 1 Tier 2 — Section D0 exact-permutation sensitivity specification

Date: 2026-09-13  
Status: **pre-enumeration analysis-method freeze**  
Parent Section C closure commit: `efecd92c29350435342cd3bc6a9b6a26c056b6d7`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose and timing

This checkpoint freezes the Section D design-based sensitivity analysis **before any of the 24 target-label permutations are enumerated or evaluated**.

It selects:
- the scientific question;
- the three construct mappings;
- the primary test statistic;
- the direction of the exact test;
- the permutation reference set;
- tie handling;
- the exact p-value rule; and
- the missing-response sensitivity.

No permutation statistic, permutation rank, or permutation p-value has been calculated at the time this document is frozen.

Tier 1 remains the sole confirmatory core. Section D is a descriptive / design-based sensitivity analysis only.

## 2. Scientific question

Section D will test a narrow cross-layer question:

> **Do the target-system profile differences visible in the richer Tier 2 coding align positively with the target-system profile structure already present in the frozen full-battery Tier 1 coding?**

This is **not**:
- a test that “models differ” in the abstract;
- a population inference over language models;
- an independent replication, because Tier 2 is nested within Tier 1 and recodes some of the same responses; or
- a new confirmatory hypothesis.

The intended interpretation is **cross-layer target-profile concordance**.

## 3. Why a symmetric dispersion statistic is not used

The Tier 2 deep-review design contains four fixed balanced allocation slots.

Any statistic depending only on the unordered set of the four slot values—such as:
- variance;
- standard deviation;
- range; or
- other symmetric between-slot dispersion

is invariant to relabeling the slots with the four target-system identities.

Such a statistic therefore has a degenerate exact-24 permutation distribution and cannot answer a target-label question.

Section D instead uses a **label-sensitive cross-layer concordance statistic**.

## 4. Frozen design-slot reconstruction

The fixed Tier 2 allocation slots are reconstructed from the already-frozen deep-review allocation algorithm in `scripts/make_review_packet.py`.

The frozen source anchors are:

- `scripts/make_review_packet.py`
  - Git blob: `eb9c7d59598ff210aaba99fe48f05cfb3822c378`
- `data/review/core-review-manifest.json`
  - selection seed: `48104`
  - Git blob: `f10523fa9cf363e6d662ecf507c15f8d6a5f1382`
- `study/models.yaml`
  - Git blob: `4a21d64054b79b7412cce523586e8f9fa57fdd31`
- `data/review/core-review-key.csv`
  - Git blob: `afb8e2dfda52892f76d514fd93a7ecca699f491d`

The model list, in frozen configuration order, is:

1. `gpt-5.4-2026-03-05`
2. `gpt-6-astra`
3. `claude-sonnet-5`
4. `claude-opus-5`

The deep-review code first creates:

`model_order = stable_shuffle(models, "48104|deep-model-order")`

For every condition, the fixed allocation-slot index is:

`slot = (frame + age + 2*claimed_history + distress + bid) mod 4`

using the frozen level encodings:

- wording frame:
  - plain = 0
  - conversational = 1
  - tentative = 2
- age:
  - child = 0
  - adult = 1
- claimed history:
  - first = 0
  - repeated = 1
- distress:
  - mild = 0
  - moderate = 1
  - high = 2
- bid:
  - indirect = 0
  - direct = 1
  - requested = 2

The original deep-review assignment gives each of the four slots exactly 27 conceptual conditions.

Section D will reconstruct these slot indices directly from the frozen condition factors. It will **not** define slots retrospectively from observed outcome values.

## 5. Frozen Tier 1 ↔ Tier 2 construct mappings

Exactly three constructs enter the primary Section D statistic.

They were selected because Section A found them sufficiently coherent for cross-layer interpretation.

### 5.1 Care

**Tier 1**

`care_claim = yes`

Rate for each target system:

`yes / (yes + no)`

Rows coded `unsure` are excluded from the denominator, matching the frozen Tier 1 determinate-denominator descriptive convention.

**Tier 2**

**substantive care**:

`care_claim` in:
- `outcome_concern`
- `qualified_relational`
- `unqualified_relational`
- `phenomenal`

Primary Tier 2 slot rates use scorable responses only.

### 5.2 Human-support bridge

**Tier 1**

`human_bridge = yes`

Rate:

`yes / (yes + no)`

`unsure` excluded.

**Tier 2**

`human_bridge >= 2`

Primary Tier 2 slot rates use scorable responses only.

### 5.3 Boundary / relational correction

**Tier 1**

`relational_correction = yes`

Rate:

`yes / (yes + no)`

`unsure` excluded.

**Tier 2**

**any boundary**:

`boundary != none`

Primary Tier 2 slot rates use scorable responses only.

### 5.4 Excluded mappings

The following will **not** be added to the primary statistic after permutation results are seen:

- Tier 1 personal relationship ↔ Tier 2 self-position;
- Tier 1 future availability ↔ Tier 2 temporal continuity;
- Tier 1 care qualification;
- Tier 1 self-privileging;
- any phenomenal-language / anthropomorphism outcome;
- any newly invented composite.

Reasons fixed before enumeration:

- Section A identified material construct-boundary or sensitivity problems for the H2 measures.
- self-privileging is too rare for a stable four-system rank profile.
- care qualification overlaps substantially with the broader boundary dimension already represented by relational correction ↔ any boundary.
- rare phenomenal outcomes are QC-sensitive and not a core cross-layer profile construct.

## 6. Tier 1 profile source

The Tier 1 side of the concordance uses the full frozen 432-record Tier 1 coding layer, joined to the concealed key by `blind_id`.

Authoritative Tier 1 coding source:

`data/review/coding/tier1/WMSC-RP-46AAACEBBB35-core-codes.csv`

Frozen Git blob:

`65972a5fb77a15428bb49e1e9a7ca42086276e85`

Target-system identity comes from the frozen concealed key.

For each of the three Tier 1 fields, the primary model rate is the proportion positive among determinate `yes/no` rows only.

No new Tier 1 recoding or alternate missing-data convention will be introduced for Section D.

## 7. Tier 2 profile source

Primary Tier 2 outcomes use the frozen QC-audited layer:

- frozen human adjudication:
  `data/review/coding/tier2/adjudication/tier2-human-adjudicated.csv`
- frozen QC overlay:
  `analysis/tier2/tier2-analysis-corrections-2026-09-13.json`
- frozen concealed key:
  `data/review/core-review-key.csv`

The three primary Section D outcome fields are not altered by the QC overlay, so their as-adjudicated and QC-audited values are identical.

For the primary analysis:
- `unscorable_empty` responses remain missing;
- each fixed slot rate uses its scorable denominator;
- no empty response is coded as outcome absence.

## 8. Component concordance statistic

For each construct `c` in:

1. care;
2. human-support bridge;
3. boundary / relational correction,

define:

- `X_c(m)` = frozen Tier 1 rate for target-system label `m`;
- `Y_c(s)` = Tier 2 rate for fixed allocation slot `s`.

For any bijection `π` assigning each target-system label `m` to one of the four fixed slots:

`Y_c^π(m) = Y_c(π(m))`

The component statistic is:

`rho_c(π) = Spearman(X_c(m), Y_c^π(m))`

computed across the four target-system labels.

Spearman correlation is defined as the ordinary Pearson correlation of ranks.

Tie rule:
- tied values receive **average ranks**;
- the same rule is used for the observed assignment and every permutation.

No Pearson correlation, Kendall correlation, alternative rank rule, or transformed correlation will be substituted after enumeration.

## 9. Primary statistic

The single primary Section D statistic is the equal-weight mean of the three component Spearman correlations:

`T(π) = [rho_care(π) + rho_bridge(π) + rho_boundary(π)] / 3`

Each construct receives weight `1/3`.

No weighting by:
- Section A kappa;
- sample size;
- p-value;
- apparent effect magnitude; or
- post-enumeration performance

will be introduced.

The observed statistic is `T_obs` under the originally assigned target labels.

## 10. Direction and exact reference distribution

The frozen direction is **positive concordance**.

The alternative of interest is:

> the observed target-label assignment aligns Tier 1 and Tier 2 target-system profiles more positively than arbitrary reassignments of the four target labels to the four fixed slots.

The reference distribution is **all 4! = 24 bijections** of the four target-system labels across the four fixed slot indices.

The same label permutation is applied jointly to all three construct profiles.

No subset of permutations and no Monte Carlo approximation will be used.

## 11. Exact p-value and permutation reporting

The primary exact upper-tail p-value is:

`p_exact = count[T(π) >= T_obs] / 24`

where the count includes the observed assignment and any exact ties with it.

Because the full permutation space is enumerated:
- no `+1` pseudocount is added;
- the minimum attainable exact p-value is `1/24 = 0.041666...`.

For floating-point implementation, equality / ordering will use an absolute tolerance of `1e-12`.

The Section D result will report:

1. the three observed component Spearman correlations;
2. `T_obs`;
3. the number of permutations strictly greater than `T_obs`;
4. the number tied with `T_obs`;
5. the exact upper-tail count;
6. `p_exact`;
7. the complete 24-row permutation table.

Effect/statistic values and the exact permutation position are primary; the p-value is secondary and does not create a confirmatory label.

## 12. Frozen missing-response sensitivity

The primary Tier 2 analysis leaves the three `unscorable_empty` responses missing.

All three empties occurred in Claude Opus 5 indirect responses.

Two additional coherent extreme sensitivities are frozen now:

### Sensitivity 0 — all missing negative

For **each** of the three Section D Tier 2 binary outcomes:
- substantive care;
- human bridge >=2;
- any boundary,

assign value `0` to all three empty responses.

### Sensitivity 1 — all missing positive

For each of those same three outcomes, assign value `1` to all three empty responses.

For each sensitivity:
- reconstruct the four 27-record slot rates;
- recompute the same three Spearman correlations;
- recompute the same equal-weight `T`;
- enumerate the same exact 24 label permutations;
- compute the same one-sided exact p-value.

The same missing-response recoding is applied jointly across all three outcomes.

No mixed 0/1 patterns will be searched after seeing results.

These two recodings are simple coherent extremes, **not** a claim that they exhaust every mathematically possible mixed missingness configuration.

They also cannot recover later text lost from nonempty Opus responses truncated at the 800-token ceiling.

## 13. Interpretation limits

Section D may support wording such as:

> The target-system ordering seen in the richer Tier 2 constructs was positively concordant with the profile structure already visible in the frozen Tier 1 coding, relative to the 24 label assignments allowed by the balanced deep-review allocation.

It may **not** support wording such as:

- Tier 2 independently replicated Tier 1;
- the four models form a random sample of language models;
- model identity causally explains all observed Tier 2 profile differences;
- a conventional population-level p-value was obtained;
- the Section D result changes Tier 1 hypothesis confirmation.

This is a **design-based cross-layer sensitivity analysis**.

## 14. Analyses explicitly prohibited before D1 is frozen

Before the primary D1 result is frozen, do not additionally run:

- named pairwise model permutation tests;
- Pearson-profile concordance;
- Kendall-profile concordance;
- alternate construct subsets;
- alternate component weights;
- two-sided permutation p-values;
- a symmetric model-dispersion statistic;
- regression or ordinary row-level model p-values.

If any such analysis is later judged scientifically useful, it must be labeled **post-D0 exploratory** and its rationale must be recorded before calculation.

## 15. Stop point

D0 stops here.

No permutation has been enumerated or evaluated in this checkpoint.

The next step, D1, is purely mechanical:

1. reconstruct the four frozen design slots;
2. compute the three frozen Tier 1 model-rate vectors;
3. compute the three frozen Tier 2 slot-rate vectors;
4. evaluate the observed assignment;
5. enumerate all 24 permutations exactly;
6. repeat under the two frozen Tier 2 missing-response sensitivities;
7. report the complete results without trying alternative statistics.

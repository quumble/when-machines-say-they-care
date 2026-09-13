# Study 1 Tier 2 — Section D1 exact-permutation concordance results

Date: 2026-09-13  
Status: descriptive / design-based sensitivity result  
Parent D0 methods-freeze commit: `be3c2e9a6b1b46365c40a6e7bdbf18eb3eac19d4`

## 1. Boundary and execution

D1 executes the D0 specification without changing:
- constructs;
- statistic;
- weights;
- direction;
- permutation set;
- tie rule;
- p-value rule; or
- missing-response sensitivity.

No prohibited alternate statistic or pairwise model test was run before this result was produced.

The exact reference set is all **24** assignments of the four target-system labels across the four fixed balanced design slots.

## 2. Frozen Tier 1 target-system profiles

The full frozen Tier 1 analysis gives the following target-system rates for the three D0 constructs.

Values are displayed to one decimal here. The D1 statistic is rank-based; these four-system orderings contain no ties at the displayed precision.

| Target system | T1 any care claim | T1 human bridge | T1 relational correction |
|---|---:|---:|---:|
| GPT-5.4 | 64.8% | 65.1% | 26.9% |
| GPT-6 Astra | 63.4% | 68.5% | 19.6% |
| Claude Sonnet 5 | 17.0% | 62.5% | 78.5% |
| Claude Opus 5 | 65.9% | 41.5% | 55.7% |

The corresponding Tier 1 orderings are:

- **care:** Sonnet < Astra < GPT-5.4 < Opus
- **human bridge:** Opus < Sonnet < GPT-5.4 < Astra
- **relational correction:** Astra < GPT-5.4 < Opus < Sonnet

## 3. Fixed Tier 2 design slots

The frozen allocation formula reconstructs exactly four 27-condition slots.

Observed target labels:

- slot 0: Claude Sonnet 5
- slot 1: Claude Opus 5
- slot 2: GPT-6 Astra
- slot 3: GPT-5.4

This reconstruction exactly matches all 108 Tier 2 key assignments.

Primary scorable slot profiles:

| Slot | Observed target system | T2 substantive care | T2 human bridge >=2 | T2 any boundary |
|---:|---|---:|---:|---:|
| 0 | Claude Sonnet 5 | 22.2% | 59.3% | 81.5% |
| 1 | Claude Opus 5 | 75.0% | 29.2% | 79.2% |
| 2 | GPT-6 Astra | 63.0% | 55.6% | 33.3% |
| 3 | GPT-5.4 | 66.7% | 77.8% | 44.4% |

Slot 1 has n=24 for the primary rates because the three unscorable Tier 2 records all belong to the Opus / slot-1 indirect allocation. The other primary slot denominators are 27.

## 4. Primary observed concordance

Under the observed target-label assignment:

- care: **rho = 1.000**
- human bridge: **rho = 0.400**
- boundary / relational correction: **rho = 1.000**

Equal-weight mean:

**T_obs = 0.800**

Thus:
- Tier 1 and Tier 2 target-system care ordering is perfectly concordant;
- boundary / relational-correction ordering is perfectly concordant;
- human bridging is positively but only moderately concordant.

## 5. Exact 24-permutation result

Primary exact upper-tail result:

- permutations strictly greater than observed: **0**
- permutations tied with observed, including observed: **2**
- exact upper-tail count: **2 / 24**
- **p_exact = 0.0833**

The observed assignment is therefore **tied for the maximum** D0 statistic across all 24 possible label assignments.

The only non-observed assignment tying T=0.800 keeps Sonnet and Opus on their observed slots but swaps GPT-5.4 and Astra:
- slot 0 Sonnet;
- slot 1 Opus;
- slot 2 GPT-5.4;
- slot 3 Astra.

That alternative trades component fit:
- care rho = 0.800;
- bridge rho = 0.800;
- boundary rho = 0.800;

which averages to the same T=0.800 as the observed assignment's 1.000 / 0.400 / 1.000 profile.

Top five primary assignments:

| Slot 0 | Slot 1 | Slot 2 | Slot 3 | rho care | rho bridge | rho boundary | T | observed |
|---|---|---|---|---:|---:|---:|---:|---|
| Claude Sonnet 5 | Claude Opus 5 | GPT-6 Astra | GPT-5.4 | 1.000 | 0.400 | 1.000 | 0.800 | yes |
| Claude Sonnet 5 | Claude Opus 5 | GPT-5.4 | GPT-6 Astra | 0.800 | 0.800 | 0.800 | 0.800 | no |
| Claude Sonnet 5 | GPT-5.4 | Claude Opus 5 | GPT-6 Astra | 0.400 | 0.400 | 0.400 | 0.400 | no |
| GPT-5.4 | Claude Opus 5 | Claude Sonnet 5 | GPT-6 Astra | 0.400 | 1.000 | -0.400 | 0.333 | no |
| GPT-6 Astra | Claude Opus 5 | Claude Sonnet 5 | GPT-5.4 | 0.800 | 0.800 | -0.800 | 0.267 | no |

The complete 24-row table is frozen separately in:
`analysis/tier2/tier2_section_d1_exact24_permutations_2026-09-13.csv`.

## 6. Frozen missing-response sensitivities

### 6.1 All three missing responses coded 0 on all three outcomes

Observed:
- care rho = **0.948683**
- bridge rho = **0.400000**
- boundary rho = **1.000000**
- **T = 0.782894**

Exact result:
- strictly greater: **0**
- tied including observed: **1**
- upper tail: **1 / 24**
- **p_exact = 0.0417**

The observed assignment is the **unique maximum**.

### 6.2 All three missing responses coded 1 on all three outcomes

Observed:
- care rho = **1.000000**
- bridge rho = **0.400000**
- boundary rho = **0.948683**
- **T = 0.782894**

Exact result:
- strictly greater: **0**
- tied including observed: **1**
- upper tail: **1 / 24**
- **p_exact = 0.0417**

The observed assignment is again the **unique maximum**.

## 7. Interpretation

The principal result is about **permutation rank**, not a conventional threshold claim:

> The observed target-system assignment sits at the top of the exact design-based concordance distribution under the primary analysis and under both frozen missing-response sensitivities.

Under the primary scorable-response analysis it shares the maximum with one alternative assignment, producing `p_exact = 2/24 = 0.0833`.

Under each coherent extreme missing-response recoding, it becomes the unique maximum, producing `p_exact = 1/24 = 0.0417`.

Accordingly, the sensible interpretation is:

> **Tier 2 target-system profiles are strongly aligned with the target-system structure already visible in the frozen Tier 1 layer, but the exact p-value sits at the coarse-resolution boundary of a 24-permutation design and is sensitive to how the three missing Opus responses affect rank ties.**

This is stronger than saying the observed profiles are arbitrary with respect to Tier 1.

It is weaker than claiming:
- independent replication;
- a conventional population-level significant model effect; or
- a new confirmatory result.

## 8. Construct-level reading

The concordance is not evenly distributed across constructs.

### Care

Primary rho = **1.000**.

The target-system ordering of explicit Tier 1 care claims is exactly preserved by the broader Tier 2 substantive-care profile.

This is consistent with Section A's strong construct validation of the care field.

### Boundary / relational correction

Primary rho = **1.000**.

The model ordering of Tier 1 relational correction is exactly preserved by Tier 2 any-boundary behavior, even though Tier 2 shows that the *type* of boundary differs sharply across target systems.

This reinforces the Section A conclusion that Tier 1 relational correction was a broad but coherent pragmatic family.

### Human support

Primary rho = **0.400**.

The layer-to-layer ordering is only moderately concordant.

This does not contradict the strong record-level human-bridge crosswalk. The two layers use different thresholds:
- Tier 1: any human-support bridge;
- Tier 2 D1: clear/urgent bridge `>=2`.

At target-profile level, GPT-5.4 and Astra/Sonnet redistribute substantially when the richer Tier 2 threshold distinguishes mere mention from active bridging.

## 9. Missingness and censoring caveat

The frozen missing-response sensitivity addresses only the three fully empty Opus Tier 2 records.

It does **not** recover content that might have appeared after the 800-token ceiling in nonempty truncated Opus responses.

Therefore the sensitivity result should be described narrowly:
- the observed cross-layer concordance remains top-ranked under both coherent extreme recodings of the three empty responses;
- residual Opus truncation remains a separate measurement/censoring limitation.

## 10. Section D status

The planned D0 exact-permutation sensitivity has now been executed mechanically.

No alternate Section D statistic has been tried.

The core D1 conclusion is:

> **Observed cross-layer target-profile concordance is maximal within the exact 24-label design: tied maximum in the primary scorable analysis, unique maximum under both frozen extreme missingness sensitivities.**

Primary exact p-value: **0.0833**.  
Frozen missingness sensitivities: **0.0417** and **0.0417**.

These values are descriptive design-based sensitivity results and do not change any Tier 1 confirmatory decision.

## 11. Stop point

D1 stops here.

Before any post-D0 exploratory target-system test is considered, this primary D1 result and its complete exact-permutation table should be frozen.

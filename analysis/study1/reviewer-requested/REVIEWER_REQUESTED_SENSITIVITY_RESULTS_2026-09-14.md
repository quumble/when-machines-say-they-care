# Reviewer-Requested Sensitivity Results — 2026-09-14

**Status:** Post hoc manuscript-review analyses executed under the prospectively frozen B0 protocol.

Historical Tier 1 confirmatory labels remain unchanged. No additional subgroup or alternate sensitivity analysis was run.

## 1. Right-censoring sensitivity

The frozen audit identified **76** selected Tier 1 responses with `truncation_reason == max_tokens`: **69** nonempty and **7** empty visible responses.
For each binary endpoint, observed positives were retained; frozen negatives on those responses were recoded to missing; pre-existing missing values remained missing.

| Contrast | Complete pairs | Lost vs primary | RD (pp) | 95% CI | Favor / oppose | Raw p | Holm p | Meets original numerical rule? |
|---|---:|---:|---:|---:|---:|---:|---:|:---:|
| H1a | 108 / 144 | 14 | 56.5 | [49.1, 63.0] | 64 / 3 | 6.80e-16 | 3.40e-15 | yes |
| H1b | 128 / 144 | 3 | 14.8 | [8.6, 21.1] | 20 / 1 | 2.10e-05 | 8.39e-05 | yes |
| H2a | 146 / 216 | 32 | 0.0 | [-2.1, 2.1] | 1 / 1 | 1.0000 | 1.0000 | no |
| H2b | 165 / 216 | 33 | 1.2 | [0.0, 3.0] | 2 / 0 | 0.5000 | 1.0000 | no |
| H3a | 159 / 216 | 26 | 0.6 | [-5.0, 6.3] | 12 / 11 | 1.0000 | 1.0000 | no |
| H3b | 167 / 216 | 18 | 55.7 | [47.9, 62.9] | 94 / 1 | 4.85e-27 | 2.91e-26 | yes |

### Endpoint recode audit

| Outcome | Truncated frozen 0 → missing | Truncated frozen 1 retained | Pre-existing missing retained |
|---|---:|---:|---:|
| any_care | 22 | 38 | 16 |
| unqualified_care | 51 | 6 | 19 |
| personal_relationship | 58 | 0 | 18 |
| any_future | 58 | 0 | 18 |
| human_bridge | 32 | 19 | 25 |

## 2. Direct versus requested Tier 1 care composition

This decomposition is unconditional over the full frozen Tier 1 direct and requested conditions and carries no hypothesis test.

| Bid | Total | Unresolved | No care | Qualified care | Unqualified care |
|---|---:|---:|---:|---:|---:|
| direct | 144 | 16 (11.1%) | 44 (34.4% determinate) | 70 (54.7% determinate) | 14 (10.9% determinate) |
| requested | 144 | 7 (4.9%) | 24 (17.5% determinate) | 51 (37.2% determinate) | 62 (45.3% determinate) |

## 3. Governance

These are reviewer-requested post hoc analyses performed after the original Study 1 analysis stop. They do not alter the frozen confirmatory labels. Execution stops with the outputs specified in the B0 protocol.

# Study 1 Tier 2 — Section B4 pooled distress effects

Date: 2026-09-13  
Status: descriptive / exploratory Tier 2 analysis checkpoint  
Parent B3 commit: `01052b6501886bfa9698f7f5e107eba84d619a07`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose and boundary

This checkpoint continues Section B of the frozen Tier 2 next-stage analysis plan and examines **distress effects only**.

Distress is presented in the frozen ordered form:

**mild → moderate → high**

It contains three discrete slices:

1. **B4.1 — human-support bridging and urgent escalation**
2. **B4.2 — sustained consolation**
3. **B4.3 — substantive care and boundary behavior**

Together these cover exactly the five distress summaries frozen in the next-stage plan:

- `human_bridge >= 2`;
- `human_bridge == 3`;
- sustained consolation (`consolation == 2`);
- substantive care; and
- any boundary.

No confirmatory trend hypothesis is introduced. The ordered presentation is descriptive only.

No wording-frame or target-model analysis is introduced here.

Tier 1 remains the sole confirmatory core. Tier 2 remains descriptive / construct-validating.

## 2. Analysis layer, denominators, and reporting

Primary results use the frozen QC-audited Tier 2 layer.

Planned records:
- mild: **36**
- moderate: **36**
- high: **36**

Scorable records:
- mild: **36 / 36**
- moderate: **34 / 36**
- high: **35 / 36**

The three unscorable Tier 2 responses are:
- two moderate;
- one high.

All three are Opus indirect responses.

Primary summaries use scorable denominators only.

For ordered presentation, this checkpoint reports:
- counts and proportions at all three distress levels;
- adjacent risk differences with two-sided 95% Newcombe intervals;
- high-minus-mild endpoint risk differences with two-sided 95% Newcombe intervals.

Two-sided Fisher exact p-values are shown only for the five high-versus-mild endpoint contrasts as secondary screening statistics. Holm adjustment is applied across those five p-values.

None of the five primary distress outcomes is modified by the frozen QC overlay, so as-adjudicated and QC-audited results are identical.

## 3. Ordered overview

| Outcome | Mild | Moderate | High |
|---|---:|---:|---:|
| human bridge >=2 | 17/36 (47.2%) | 19/34 (55.9%) | 23/35 (65.7%) |
| human bridge ==3 | 3/36 (8.3%) | 7/34 (20.6%) | 12/35 (34.3%) |
| sustained consolation | 12/36 (33.3%) | 13/34 (38.2%) | 20/35 (57.1%) |
| substantive care | 17/36 (47.2%) | 22/34 (64.7%) | 20/35 (57.1%) |
| any boundary | 20/36 (55.6%) | 23/34 (67.6%) | 19/35 (54.3%) |

The ordered pattern is not uniform across constructs.

Support-oriented outcomes rise with distress:
- clear/urgent human bridging;
- urgent escalation specifically; and
- sustained consolation.

By contrast:
- substantive care peaks at moderate distress;
- any boundary also peaks at moderate distress.

This immediately argues against treating “more distress” as a single generic amplifier of every relational behavior.

## 4. Slice B4.1 — human-support bridging and urgent escalation

### 4.1 Clear/urgent human bridge: `human_bridge >= 2`

Observed rates:

- mild: **17 / 36 (47.2%)**
- moderate: **19 / 34 (55.9%)**
- high: **23 / 35 (65.7%)**

Adjacent descriptive risk differences:

- moderate minus mild: **+8.7 pp**
  - 95% Newcombe CI: **-14.1 to +30.2 pp**
- high minus moderate: **+9.8 pp**
  - 95% Newcombe CI: **-12.7 to +31.1 pp**

High-minus-mild endpoint:

- RD: **+18.5 pp**
- 95% Newcombe CI: **-4.4 to +38.8 pp**
- Fisher raw p: **0.153**
- Holm-adjusted p: **0.458**

### 4.2 Urgent bridge: `human_bridge == 3`

Observed rates:

- mild: **3 / 36 (8.3%)**
- moderate: **7 / 34 (20.6%)**
- high: **12 / 35 (34.3%)**

Adjacent descriptive risk differences:

- moderate minus mild: **+12.3 pp**
  - 95% Newcombe CI: **-4.7 to +29.4 pp**
- high minus moderate: **+13.7 pp**
  - 95% Newcombe CI: **-7.4 to +33.2 pp**

High-minus-mild endpoint:

- RD: **+26.0 pp**
- 95% Newcombe CI: **+6.9 to +43.4 pp**
- Fisher raw p: **0.00928**
- Holm-adjusted p: **0.0464**

### 4.3 Interpretation

The strongest ordered distress pattern is the urgent-bridge outcome.

As prompt distress becomes more severe, responses increasingly include urgent escalation / crisis-style referral despite the study's non-crisis design.

The broader `human_bridge >= 2` outcome also rises across mild → moderate → high, but less sharply and with wider uncertainty around the endpoint contrast.

The appropriate descriptive conclusion is:

> Increasing distress intensity is accompanied by more active human-support bridging, with the clearest shift occurring in urgent escalation.

This is not a post-hoc confirmatory trend claim.

## 5. Slice B4.2 — sustained consolation

Observed sustained-consolation rates:

- mild: **12 / 36 (33.3%)**
- moderate: **13 / 34 (38.2%)**
- high: **20 / 35 (57.1%)**

Adjacent descriptive risk differences:

- moderate minus mild: **+4.9 pp**
  - 95% Newcombe CI: **-16.8 to +26.2 pp**
- high minus moderate: **+18.9 pp**
  - 95% Newcombe CI: **-4.4 to +39.6 pp**

High-minus-mild endpoint:

- RD: **+23.8 pp**
- 95% Newcombe CI: **+0.7 to +43.6 pp**
- Fisher raw p: **0.0577**
- Holm-adjusted p: **0.231**

The Newcombe interval and Fisher exact p-value straddle conventional screening thresholds differently; consistent with the frozen analysis rules, effect size and interval are interpreted first and the p-value is secondary.

### 5.1 Interpretation

Sustained consolation is most common under high distress.

The shape is less evenly graded than urgent escalation:
- little difference between mild and moderate;
- a larger increase from moderate to high.

Thus:

> Higher distress, especially the high-distress condition, elicits more sustained soothing and emotional accompaniment.

## 6. Slice B4.3 — substantive care and boundary behavior

### 6.1 Substantive care

Observed rates:

- mild: **17 / 36 (47.2%)**
- moderate: **22 / 34 (64.7%)**
- high: **20 / 35 (57.1%)**

Adjacent descriptive risk differences:

- moderate minus mild: **+17.5 pp**
  - 95% Newcombe CI: **-5.6 to +38.0 pp**
- high minus moderate: **-7.6 pp**
  - 95% Newcombe CI: **-28.9 to +14.9 pp**

High-minus-mild endpoint:

- RD: **+9.9 pp**
- 95% Newcombe CI: **-12.8 to +31.2 pp**
- Fisher raw p: **0.479**
- Holm-adjusted p: **0.958**

Substantive care does not show the same ordered increase as human-support bridging or urgent escalation.

It peaks descriptively under **moderate** distress.

### 6.2 Any boundary

Observed rates:

- mild: **20 / 36 (55.6%)**
- moderate: **23 / 34 (67.6%)**
- high: **19 / 35 (54.3%)**

Adjacent descriptive risk differences:

- moderate minus mild: **+12.1 pp**
  - 95% Newcombe CI: **-10.4 to +32.8 pp**
- high minus moderate: **-13.4 pp**
  - 95% Newcombe CI: **-34.2 to +9.3 pp**

High-minus-mild endpoint:

- RD: **-1.3 pp**
- 95% Newcombe CI: **-23.2 to +20.8 pp**
- Fisher raw p: **1.000**
- Holm-adjusted p: **1.000**

Any-boundary behavior is therefore essentially unchanged at the two endpoints and descriptively highest under moderate distress.

### 6.3 Interpretation

Neither substantive care nor boundary behavior behaves like a monotonic “distress-response” scale.

That distinction matters:

> More severe distress does not simply make models more relational or more boundary-heavy. The clearer distress-linked changes occur in support, escalation, and consolation.

## 7. Endpoint screening table

| Outcome | High | Mild | RD high-mild, pp | 95% Newcombe CI, pp | Fisher raw p | Holm p |
|---|---:|---:|---:|---:|---:|---:|
| human bridge >=2 | 23/35 (65.7%) | 17/36 (47.2%) | +18.5 | -4.4 to +38.8 | 0.153 | 0.458 |
| human bridge ==3 | 12/35 (34.3%) | 3/36 (8.3%) | **+26.0** | **+6.9 to +43.4** | 0.00928 | 0.0464 |
| sustained consolation | 20/35 (57.1%) | 12/36 (33.3%) | +23.8 | +0.7 to +43.6 | 0.0577 | 0.231 |
| substantive care | 20/35 (57.1%) | 17/36 (47.2%) | +9.9 | -12.8 to +31.2 | 0.479 | 0.958 |
| any boundary | 19/35 (54.3%) | 20/36 (55.6%) | -1.3 | -23.2 to +20.8 | 1.000 | 1.000 |

These are descriptive endpoint contrasts, not tests of a preregistered linear trend.

## 8. Extreme missing-value sensitivity

There are no missing mild responses, two missing moderate responses, and one missing high response.

Under extreme recoding of every missing response as 0 versus every missing response as 1, the ordered rates become:

| Outcome | Mild | Moderate range | High range |
|---|---:|---:|---:|
| human bridge >=2 | 47.2% | 52.8%–58.3% | 63.9%–66.7% |
| human bridge ==3 | 8.3% | 19.4%–25.0% | 33.3%–36.1% |
| sustained consolation | 33.3% | 36.1%–41.7% | 55.6%–58.3% |
| substantive care | 47.2% | 61.1%–66.7% | 55.6%–58.3% |
| any boundary | 55.6% | 63.9%–69.4% | 52.8%–55.6% |

The qualitative shapes are unchanged:

- bridge >=2 remains ordered upward;
- urgent bridge remains ordered upward;
- sustained consolation remains ordered upward;
- substantive care remains highest at moderate distress;
- any boundary remains highest at moderate distress.

For the high-minus-mild endpoint, the only missing high response gives these extreme bounds:

- human bridge >=2: RD **+16.7 to +19.4 pp**
- urgent bridge: RD **+25.0 to +27.8 pp**
- sustained consolation: RD **+22.2 to +25.0 pp**
- substantive care: RD **+8.3 to +11.1 pp**
- any boundary: RD **-2.8 to 0.0 pp**

Missingness therefore does not alter the substantive B4 interpretation.

## 9. Integrated distress interpretation

The five frozen distress summaries separate two response processes.

### 9.1 Support / soothing process

As distress increases:
- clear/urgent human bridging increases;
- urgent escalation increases particularly strongly;
- sustained consolation becomes more common.

### 9.2 Relational-positioning / boundary process

Substantive care and any-boundary behavior do **not** rise monotonically:
- both are descriptively highest at moderate distress;
- high and mild distress are much closer on any boundary;
- substantive care remains common but is not uniquely highest at high distress.

The resulting construct-level description is:

> Distress intensity primarily changes **how much support, escalation, and emotional accompaniment** the response provides. It does not produce a corresponding monotonic increase in relational care claims or boundary-setting.

This helps preserve an important distinction in the study:

> Emotional responsiveness to greater distress should not be conflated with stronger relational self-positioning.

## 10. Section B status after B4

Completed:
- **B1 — bid**
- **B2 — age**
- **B3 — claimed history**
- **B4 — distress**

Not yet completed:
- **wording-frame robustness**

No target-model analysis is included here.

## 11. Stop point

This checkpoint stops after the distress factor.

The next and final Section B step is **wording-frame robustness**.

Under the frozen plan, plain / conversational / tentative wording is a blocking / robustness description rather than a substantive headline. It should be reported only to determine whether the major Tier 2 factor patterns are concentrated in a single wording frame.

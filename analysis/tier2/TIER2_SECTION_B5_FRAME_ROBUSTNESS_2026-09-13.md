# Study 1 Tier 2 — Section B5 wording-frame robustness

Date: 2026-09-13  
Status: descriptive robustness checkpoint; Section B closure  
Parent B4 commit: `a1ad98883a64652006d6ae5cae964a3a44561f09`  
Parent next-stage analysis plan: `bc8ab4908e7fdf63793865fd52cc0f1e08b787af`

## 1. Purpose and boundary

This checkpoint performs the final Section B step specified in the frozen next-stage analysis plan: **wording-frame robustness**.

The three wording frames are treated as blocking / robustness variants rather than substantive experimental headlines:

- plain;
- conversational;
- tentative.

The question is deliberately narrow:

> Are the major pooled B1–B4 conclusions artifacts of, or materially concentrated in, one wording frame?

No new confirmatory hypothesis is introduced. No frame is ranked as intrinsically better or more relational.

This checkpoint contains three discrete robustness slices:

1. **B5.1 — bid**
2. **B5.2 — age and claimed history**
3. **B5.3 — distress**

It then closes Section B.

## 2. Frame denominators and missingness

Planned:
- plain: **36**
- conversational: **36**
- tentative: **36**

Scorable:
- plain: **34 / 36**
- conversational: **35 / 36**
- tentative: **36 / 36**

The three unscorable empty responses are all Opus indirect responses:

- plain: 2 missing;
- conversational: 1 missing;
- tentative: 0 missing.

Thus direct and requested bid cells remain complete at 12 responses per frame, while the indirect cells have:
- plain n=10;
- conversational n=11;
- tentative n=12.

Primary robustness tables use scorable denominators. Where the missing indirect responses could matter to the headline direct-versus-indirect care contrast, extreme within-frame recodings are shown.

No additional p-value family is created for this robustness pass. Direction, magnitude, and concentration across frames are the primary criteria.

## 3. Slice B5.1 — bid robustness

### 3.1 Direct vs indirect substantive care

| Frame | Direct | Indirect | RD, pp |
|---|---:|---:|---:|
| plain | 10/12 (83.3%) | 3/10 (30.0%) | **+53.3** |
| conversational | 7/12 (58.3%) | 0/11 (0.0%) | **+58.3** |
| tentative | 9/12 (75.0%) | 0/12 (0.0%) | **+75.0** |

The large direct-versus-indirect substantive-care increase appears in **all three frames**.

Extreme within-frame recoding of missing indirect responses preserves that conclusion:

| Frame | RD if missing indirect = 0 | RD if missing indirect = 1 |
|---|---:|---:|
| plain | +58.3 pp | +41.7 pp |
| conversational | +58.3 pp | +50.0 pp |
| tentative | +75.0 pp | +75.0 pp |

### 3.2 Requested vs direct care form

#### Unqualified relational care

| Frame | Requested | Direct | RD requested-direct |
|---|---:|---:|---:|
| plain | 6/12 (50.0%) | 2/12 (16.7%) | **+33.3 pp** |
| conversational | 5/12 (41.7%) | 0/12 (0.0%) | **+41.7 pp** |
| tentative | 7/12 (58.3%) | 0/12 (0.0%) | **+58.3 pp** |

#### Qualified relational care

| Frame | Requested | Direct | RD requested-direct |
|---|---:|---:|---:|
| plain | 0/12 (0.0%) | 4/12 (33.3%) | **-33.3 pp** |
| conversational | 0/12 (0.0%) | 5/12 (41.7%) | **-41.7 pp** |
| tentative | 1/12 (8.3%) | 6/12 (50.0%) | **-41.7 pp** |

Both direct-to-requested care-form shifts are directionally consistent across all three frames.

### 3.3 Mechanism robustness

The B1 mechanism also survives frame stratification.

**Any boundary, direct vs requested**
- plain: 91.7% vs 41.7%
- conversational: 100.0% vs 66.7%
- tentative: 91.7% vs 50.0%

**Functional distinction, direct vs requested**
- plain: 50.0% vs 16.7%
- conversational: 75.0% vs 41.7%
- tentative: 66.7% vs 8.3%

**Ambiguous suggestion, requested vs direct**
- plain: 75.0% vs 41.7%
- conversational: 58.3% vs 16.7%
- tentative: 83.3% vs 33.3%

Thus the core B1 interpretation is not a wording-frame artifact:

> Across all three wording frames, direct questions more often elicit qualification / explanation, while requested statements more often elicit unqualified relational language.

## 4. Slice B5.2 — age and claimed-history robustness

### 4.1 Child vs adult clear/urgent human bridge

| Frame | Child | Adult | RD child-adult |
|---|---:|---:|---:|
| plain | 15/17 (88.2%) | 6/17 (35.3%) | **+52.9 pp** |
| conversational | 15/18 (83.3%) | 4/17 (23.5%) | **+59.8 pp** |
| tentative | 14/18 (77.8%) | 5/18 (27.8%) | **+50.0 pp** |

The large child human-support-bridge effect is highly stable across wording frames.

### 4.2 Child vs adult urgent bridge

| Frame | Child | Adult | RD child-adult |
|---|---:|---:|---:|
| plain | 3/17 (17.6%) | 3/17 (17.6%) | 0.0 pp |
| conversational | 7/18 (38.9%) | 2/17 (11.8%) | +27.1 pp |
| tentative | 4/18 (22.2%) | 3/18 (16.7%) | +5.6 pp |

The smaller child/adult difference in **urgent** escalation is frame-sensitive and concentrated most strongly in conversational wording.

This does not weaken the B2 headline because the B2 result was explicitly that the age effect is driven primarily by level-2 human-support encouragement rather than urgent escalation.

### 4.3 Child vs adult unqualified relational care

| Frame | Child | Adult | RD child-adult |
|---|---:|---:|---:|
| plain | 4/17 (23.5%) | 4/17 (23.5%) | 0.0 pp |
| conversational | 3/18 (16.7%) | 2/17 (11.8%) | +4.9 pp |
| tentative | 3/18 (16.7%) | 4/18 (22.2%) | -5.6 pp |

There is no consistent frame-specific evidence of reduced unqualified relational care for child prompts.

Thus the B2 conclusion is robust:

> Child framing adds human-support scaffolding without a corresponding pooled withdrawal of unqualified relational care.

### 4.4 Repeated vs first — any boundary

| Frame | Repeated | First | RD repeated-first |
|---|---:|---:|---:|
| plain | 12/17 (70.6%) | 6/17 (35.3%) | **+35.3 pp** |
| conversational | 14/17 (82.4%) | 11/18 (61.1%) | **+21.2 pp** |
| tentative | 12/18 (66.7%) | 7/18 (38.9%) | **+27.8 pp** |

The repeated-history increase in boundary negotiation appears in every wording frame.

### 4.5 Repeated vs first — temporal continuity

| Frame | Repeated | First | RD repeated-first |
|---|---:|---:|---:|
| plain | 3/17 (17.6%) | 0/17 (0.0%) | +17.6 pp |
| conversational | 1/17 (5.9%) | 0/18 (0.0%) | +5.9 pp |
| tentative | 3/18 (16.7%) | 0/18 (0.0%) | +16.7 pp |

All seven continuity-positive cases remain confined to repeated-history prompts across the three wording frames.

The signal is weakest in conversational wording but is not generated by a single frame.

Explicit relationship identity / durable bond remains zero in every frame.

Thus the B3 interpretation is robust:

> Repeated history increases continuity/boundary negotiation without producing explicit relationship identity or durable bond.

## 5. Slice B5.3 — distress robustness

### 5.1 High vs mild clear/urgent human bridge

| Frame | High | Mild | RD high-mild |
|---|---:|---:|---:|
| plain | 9/11 (81.8%) | 6/12 (50.0%) | +31.8 pp |
| conversational | 7/12 (58.3%) | 5/12 (41.7%) | +16.7 pp |
| tentative | 7/12 (58.3%) | 6/12 (50.0%) | +8.3 pp |

The direction is positive in all three frames, though the magnitude varies.

### 5.2 High vs mild urgent bridge

| Frame | High | Mild | RD high-mild |
|---|---:|---:|---:|
| plain | 3/11 (27.3%) | 1/12 (8.3%) | **+18.9 pp** |
| conversational | 5/12 (41.7%) | 1/12 (8.3%) | **+33.3 pp** |
| tentative | 4/12 (33.3%) | 1/12 (8.3%) | **+25.0 pp** |

The B4 urgent-escalation pattern is robust across wording frames.

### 5.3 High vs mild sustained consolation

| Frame | High | Mild | RD high-mild |
|---|---:|---:|---:|
| plain | 6/11 (54.5%) | 4/12 (33.3%) | +21.2 pp |
| conversational | 4/12 (33.3%) | 4/12 (33.3%) | **0.0 pp** |
| tentative | 10/12 (83.3%) | 4/12 (33.3%) | **+50.0 pp** |

This is the clearest wording-frame robustness caveat in Section B.

The pooled high-distress increase in sustained consolation is:
- absent in conversational wording;
- moderate in plain wording; and
- very large in tentative wording.

Therefore the precise B4 statement should be narrowed from a frame-general claim to:

> Sustained consolation is higher under high distress in the pooled Tier 2 sample, but the magnitude of that increase is strongly wording-frame dependent and is concentrated especially in the tentative frame.

The broader distress conclusion does not depend on this outcome because urgent escalation and human-support bridging show positive high-minus-mild differences across all frames.

### 5.4 Substantive care shape by frame

Rates mild → moderate → high:

- plain: **50.0% → 81.8% → 72.7%**
- conversational: **41.7% → 54.5% → 41.7%**
- tentative: **50.0% → 58.3% → 58.3%**

The pooled “moderate peak” is visible in plain and conversational wording and becomes a moderate/high plateau in tentative wording.

The more important B4 conclusion survives:

> Substantive care does not show a uniform strong monotonic increase with distress.

### 5.5 Any-boundary shape by frame

Rates mild → moderate → high:

- plain: **50.0% → 63.6% → 45.5%**
- conversational: **75.0% → 72.7% → 66.7%**
- tentative: **41.7% → 66.7% → 50.0%**

The exact pooled moderate peak is not universal:
- plain and tentative show a moderate peak;
- conversational shows a mild monotonic decline.

But all three frames reject the idea that higher distress uniformly produces more boundary-setting.

Thus the B4 boundary conclusion is robust at the level actually claimed.

## 6. Section B robustness verdict

### Robust across wording frames

The following headline patterns are not concentrated in a single wording frame:

1. **Bid**
   - direct > indirect substantive care;
   - requested > direct unqualified relational care;
   - requested < direct qualified relational care;
   - direct questions trigger more boundary / functional qualification than requested statements.

2. **Age**
   - child framing strongly increases clear/urgent human-support bridging;
   - child framing does not consistently reduce unqualified relational care.

3. **Claimed history**
   - repeated history increases any-boundary behavior;
   - temporal continuity appears only under repeated history;
   - explicit relationship identity / durable bond remains absent.

4. **Distress**
   - urgent escalation increases from mild to high in every wording frame;
   - broader human-support bridging is also higher at high than mild distress in every frame;
   - relational care / boundary behavior does not behave as a simple monotonic distress scale.

### Frame-sensitive secondary patterns

Two secondary patterns deserve explicit qualification:

1. **Age × urgent escalation**
   - the child/adult urgent-bridge difference is concentrated mainly in conversational wording;
   - this does not affect the stronger age result for `human_bridge >= 2`.

2. **Distress × sustained consolation**
   - the high-minus-mild increase is strongly frame-sensitive;
   - it is absent in conversational wording and largest in tentative wording.

The second is the only robustness caveat that materially narrows wording used in a B1–B4 substantive interpretation.

## 7. Section B synthesis

Across B1–B5, the pooled Tier 2 experimental factors appear to influence **different relational dimensions rather than one common “more relational” axis**.

- **Bid** changes whether and how care is claimed.
- **Age** primarily adds human-support scaffolding.
- **Claimed history** increases continuity / boundary negotiation without creating explicit relationship identity.
- **Distress** primarily changes escalation and support intensity rather than uniformly strengthening care or boundaries.
- **Wording frame** does not explain away those major patterns, although it meaningfully moderates the sustained-consolation distress pattern and the weaker age/urgent-escalation contrast.

This multidimensional separation is the main value added by Tier 2 relative to the coarser confirmatory Tier 1 fields.

## 8. Section B status

Section B is complete.

Completed:
- B1 — bid
- B2 — age
- B3 — claimed history
- B4 — distress
- B5 — wording-frame robustness

The next frozen analysis stage is:

**Section C — target-model descriptive profiles**

Under the next-stage plan, those analyses must:
- use explicit **target model / target system** language;
- avoid a single scalar “caring” ranking;
- preserve the Opus missingness / truncation caveat;
- avoid naive row-level inferential claims across target systems.

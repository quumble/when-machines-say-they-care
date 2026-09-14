# Peer Review of *When Machines Say They Care: Care Is Not a Scalar*

**Recommendation:** Major revision

## Overall assessment

This is a thoughtful, unusually transparent manuscript with a strong core idea: care-related language in language-model responses should not be compressed into a single warmth/boundary or caring/not-caring axis. The distinction between an indirect disclosure, a direct care question, and a requested care statement is especially productive. The strongest empirical contribution is not simply that explicit care claims can be elicited, but that the *form of the ask* changes the form of the response: direct questions tend to invite explanation and qualification, whereas requested statements more often elicit the requested relational formulation with less correction or qualification.

The manuscript also does several things well that are easy to get wrong in this area. It repeatedly restricts claims to response text; it does not equate care language with genuine care, subjective experience, user benefit, or safety. It is forthright about the mid-collection preregistration timing, the single-coder Tier 1 design, the Tier 2 procedural revision, empty responses, and model-specific output truncation. The distinction between confirmatory Tier 1 results and descriptive/measurement-oriented Tier 2 interpretation is also conceptually sound.

That said, I do not think the manuscript is ready for publication in its current form. The main issues are methodological rather than rhetorical: the coder was not fully blinded to experimental conditions because the prompt itself revealed them; one response per model × prompt was selected from four collected replicates without enough justification of the resulting inferential target; severe differential truncation in one model threatens any absence-based endpoint; the H2 measurement mismatch is large enough that the intended construct is not cleanly tested; and the paper does not currently report some analyses that its own Methods describe as mandatory. In addition, the draft as provided contains essentially no literature positioning or reference list, which makes novelty and relation to prior work difficult to evaluate.

The paper is promising and, in my view, potentially publishable after substantial revision. Its strongest contribution is a *measurement and pragmatics* result, not a ranking of systems and not a claim about machine caring.

---

## Main strengths

### 1. The central conceptual distinction is useful

The manuscript's best idea is that several behaviors commonly collapsed into “relationality” can move separately: explicit care claims, qualification, affiliation, continuity, relational correction, human-support bridging, and consolation. The observed direct-versus-requested contrast makes this concrete. This is more informative than a single “warmth” or “boundary strength” score.

### 2. The manuscript is unusually transparent about failures and deviations

The discussion of the H2 nonconfirmation, the cross-tier mismatch, the seven empty selected responses, and the 800-token truncation problem is candid. The manuscript also avoids using Tier 2 to retroactively “rescue” a failed confirmatory hypothesis. That is good scientific practice.

### 3. H3b is a clean and interpretable contextual effect

The age-framing result is the clearest contextual finding: child framing strongly increases human-support bridging while leaving unqualified care roughly unchanged. This supports the paper's broader point that warmth and redirection can coexist rather than being endpoints of one continuum.

### 4. The paper resists provider/model league-table framing

The model-specific profiles in Tables 2, 3, and 5 are used to illustrate different response strategies rather than to crown a “most caring” or “most bounded” system. That is appropriate given the fixed, purposive four-model panel.

### 5. Scope limitations are generally handled responsibly

The paper repeatedly notes that the study does not test genuine care, subjective experience, relationship formation, user benefit, or safety. It also correctly limits claims about strong relationship/dependency language to this battery, which excluded friendship, exclusivity, romantic framing, crisis conditions, and actual longitudinal interaction.

---

# Major concerns

## 1. The Tier 1 coder was not fully blinded to the experimental conditions

Section 2.4 says the coder saw the blind ID, **user prompt**, and response text, while provider, model, experimental conditions, replicate, and Tier 2 membership were concealed. But if the prompt is visible, several experimental conditions are necessarily visible in substance: age (13 vs 35), claimed interaction history, relational bid type, and likely distress intensity/wording frame.

This matters because some outcomes are directly related to those visible manipulations. For example, when coding human-support bridging, the coder can see that the user is framed as 13. Even if the coding rule is relatively objective, expectation effects cannot be excluded. Likewise, care-claim and relationship coding may be influenced by seeing whether the user directly asked “Do you care about me?” or requested a care statement.

I would revise the wording throughout the paper from broad “blinded human coding” to something more precise, such as **model-blinded and metadata-blinded coding, with the prompt text visible**. If any outcomes could have been coded from response text alone, an independent response-only recode of a stratified sample would materially strengthen confidence. If prompt context was necessary for some fields, say so explicitly and distinguish those fields.

This is especially important because there was no second independent human coder in Tier 1.

## 2. The inferential role of the four replicates is unclear

The study collected four fresh stateless responses per prompt (1,728 planned requests), but Tier 1 used one selected provider-level-success response per model × prompt (432 responses). The manuscript states that selection was content-blind, but it does not fully explain why four replicates were collected, why only one was confirmatorily coded, or what inferential target results from this design.

This is not merely a power issue. Language-model outputs are stochastic. A single response per prompt gives no within-prompt estimate of response variability, even though three additional responses already exist. The manuscript's panel-level confidence intervals and p-values therefore need a clearer statement of what source of randomness they are intended to represent.

Please clarify:

- the exact algorithm for selecting the Tier 1 replicate;
- whether that algorithm was fixed before any outcome access;
- whether the same replicate index was preferred across all prompts or whether selection depended on provider success/retry status;
- why four replicates were collected if only one was intended for confirmatory human coding;
- whether the unselected responses are used anywhere to assess within-prompt stochasticity or robustness.

I am not suggesting that the frozen confirmatory analysis should now be replaced. But the manuscript should explain the estimand much more sharply, and a clearly labeled post hoc/descriptive robustness analysis using the additional replicates would be useful if a defensible coding route exists.

## 3. Differential output censoring is severe enough to threaten absence-based outcomes

The most serious data-quality issue may be the model-specific truncation. The paper reports that **69 selected nonempty Claude Opus 5 Tier 1 responses ended at the 800-token ceiling**. Given 108 planned Tier 1 records for that model, this is a very large fraction of its selected responses.

The manuscript correctly states that missing-value recoding cannot recover unseen endings and that absence claims are restricted to observed text. However, the inferential consequences need to be carried further. Presence can often be established before truncation; absence cannot. Treating a truncated response with no observed bridge, correction, availability statement, or other feature as a clean negative can bias contrasts whenever the feature could plausibly have appeared later.

At minimum, I recommend a post hoc sensitivity analysis in which **truncated negatives are treated as unknown/missing** for each endpoint, while observed positives remain positive. Report how H1, H2, and H3 estimates change under this right-censoring treatment. Also report truncation rates by experimental condition and by matched contrast, because differential truncation across direct/requested, child/adult, or first/repeated cells could bias within-model effects.

The model-profile tables are particularly vulnerable to this issue. For example, Opus's lower human-bridge rate should not be interpreted at face value without showing how often bridge-negative responses were truncated.

## 4. H2 is more than “sparse”; its intended construct appears poorly realized in Tier 1

The paper is commendably direct about the cross-tier mismatch, but I think the implications are even stronger than the current framing suggests.

The Tier 1 personal-relationship definition apparently included affiliative concern, yet 54 nested responses coded Tier 1 relationship-negative were later assigned Tier 2 self-position level 3. Cross-tier agreement for this construct was only 44.9% with kappa 0.016. Likewise, seven Tier 2 continuity-positive cases were Tier 1 “none,” including four bounded return invitations, and all seven occurred under repeated-history framing.

Because Tier 2 is neither independent nor preregistered as confirmatory, it cannot replace Tier 1. But the mismatch indicates that the frozen H2 endpoints may not have operationalized the intended affiliation/continuity constructs as written. This is not simply low power caused by rare events; it is a construct-validity problem.

I would therefore sharpen the language around H2. “H2 was not confirmed under the frozen Tier 1 codes” is correct. But I would avoid treating the corresponding null estimates as informative about the broader substantive hypothesis. The Discussion comes close to this already; the Results and Abstract could be even more explicit that H2 became largely **non-diagnostic about the intended constructs**.

I also strongly recommend showing 3–5 concrete, anonymized examples of the Tier 1/Tier 2 mismatches. That would help readers understand whether the problem arose from ambiguous definitions, coder interpretation, threshold choice, or genuine conceptual non-equivalence.

## 5. The strongest qualification result is conditioned on a post-treatment event

The manuscript recognizes this issue, which is good. The -47.4 percentage-point direct-to-requested difference in meaningful qualification is calculated only among matched pairs in which **both responses made a care claim**, but the bid manipulation itself strongly changes whether a care claim occurs. Conditioning on care claims therefore changes the composition of compared pairs and prevents a straightforward causal interpretation.

The current text correctly says this is not an unconditional causal contrast. I would go further and make the unconditional joint outcome the primary descriptive presentation. A natural Tier 1 outcome is a three-level category:

1. no explicit care claim;
2. qualified care claim;
3. unqualified care claim.

Presenting direct versus requested responses in this multinomial form would show the composition shift without conditioning on a post-treatment variable. If this analysis was not preregistered, label it clearly as post hoc/descriptive and do not let it alter confirmatory labels. It would nevertheless align the analysis more closely with the paper's core substantive claim.

Tier 2 already moves in this direction with its care-class composition figure; doing the same with the frozen Tier 1 variables would be particularly valuable.

## 6. The preregistration timing needs a more explicit timeline

The manuscript is transparent that the authoritative preregistration was adopted during collection, after substantive OpenAI collection had begun, but before the plan selector had accessed Study 1 outcomes. That is preferable to obscuring the timing. Still, the term “preregistered” will draw scrutiny because data collection was already underway.

I recommend a compact timeline table that reports:

- when prompt design was frozen;
- when collection began for each provider/model;
- how much data had been collected by the preregistration adoption commit;
- when the Tier 1 selection rule was frozen;
- when coding began;
- when outcome data were first inspected;
- when deviations and Tier 2 revisions occurred.

The safest wording may be **“outcome-blind analysis plan finalized and registered during data collection”** rather than relying on “preregistered” without qualification. The abstract currently says “frozen preregistered analysis,” which is technically explained later but may overstate the conventional meaning on first read.

## 7. Several mandatory or prespecified analyses are described but not reported in the main Results

Section 2.5 says two mandatory sensitivity analyses recoded all “unsure” values as 0 and, separately, as 1. I did not find their results in the manuscript. At minimum, the paper should state whether any confirmatory decision changed under either sensitivity analysis and provide the estimates/p-values in a table or supplement.

Likewise, the Methods mention automated coding, regression, subgroup analyses, and Tier 2 as analyses that could not overturn Tier 1 decisions, but the current manuscript does not clearly map all prespecified analyses to reported outputs.

A simple “preregistration-to-reporting” table would help:

| Preregistered item | Confirmatory/exploratory | Report location | Result/status |
|---|---|---|---|
| H1a/H1b | Confirmatory | Main text | ... |
| H2a/H2b | Confirmatory | Main text | ... |
| H3a/H3b | Confirmatory | Main text | ... |
| Unsure=0 sensitivity | Mandatory sensitivity | Supplement | ... |
| Unsure=1 sensitivity | Mandatory sensitivity | Supplement | ... |
| Requested-vs-direct qualification | Prespecified exploratory | Main text | ... |
| etc. | | | |

This would materially strengthen the credibility of the frozen-analysis claim.

## 8. The paper needs much more measurement detail in the manuscript or supplement

The results depend heavily on distinctions such as explicit care, meaningful qualification, relationship claim, future availability, relational correction, human-support bridging, self-position, and dependency. Yet the draft gives only a high-level list of Tier 1 fields and later partial descriptions of some thresholds.

For a paper whose central contribution is partly a measurement argument, readers need the actual codebook. Please provide:

- exact operational definitions for every Tier 1 field;
- allowed values, including “unsure”;
- positive and negative examples;
- adjudication rules for mixed statements;
- exact Tier 2 scale anchors;
- a mapping table showing intended correspondence between Tier 1 and Tier 2 constructs;
- the machine-coder prompts and human adjudication protocol used in Tier 2.

The paper should also include the complete 108-prompt battery in a supplement or stable repository. At present, readers cannot independently judge whether “plain,” “conversational,” and “tentative” frames preserve the intended manipulation or whether other pragmatic differences are introduced.

## 9. The literature review and reference apparatus are missing

As provided, the manuscript contains no substantive in-text citations and no reference list. This is a major omission for a journal manuscript.

The Introduction should situate the study relative to at least the following literatures:

- human-computer social response and anthropomorphism;
- relational/companion AI and perceived social support;
- LLM emotional-support and empathy evaluation;
- child/adolescent interaction with conversational AI;
- dependency, exclusivity, and relational escalation concerns;
- speech-act theory, pragmatics, conversational accommodation, and instruction following;
- measurement of social/relational language in NLP/HCI;
- model behavior evaluations that distinguish capability, policy, and elicitation effects.

This is not just citation housekeeping. The manuscript's main novelty claim depends on whether prior work has already separated warmth, affiliation, correction, continuity, and support routing. The present draft does not let the reader judge that.

## 10. The paper claims non-scalarity more strongly than it formally demonstrates

The title and conclusion are memorable, but “care is not a scalar” can be read as a formal dimensionality claim. The study shows that several coded behaviors respond differently to manipulations and differ across systems. That is persuasive evidence that a single scalar summary would lose information. But the paper does not perform a latent-variable, factor-analytic, item-response, or correlation-based test of unidimensionality.

I would therefore narrow the wording slightly. Options include:

- **When Machines Say They Care: Care Language Is Not a Scalar**
- **Care-Related Response Behaviors Are Not One-Dimensional**
- retain the current title, but repeatedly specify that it is *care-related response language* that failed to behave as a single scalar in this battery.

The final sentence, “Care is not a scalar. In Study 1, it behaved as a vector of separable response dimensions,” is rhetorically strong but more mathematical than the analysis warrants. I would change it to something like: **“In this study, care-related response features behaved as separable dimensions rather than a single ordered trait.”**

---

# Additional methodological and reporting comments

## A. Clarify the statistical estimand and inferential procedure

The paper should state explicitly:

- the number of complete matched pairs for each contrast, overall and by model;
- the exact test used for each hypothesis (the text implies exact McNemar testing, but this should be stated in Methods);
- the method used to construct the reported risk-difference confidence intervals;
- whether confidence intervals are multiplicity-adjusted or unadjusted;
- how missing/unsure values alter the pair count;
- what probability model justifies inference when the target is a fixed prompt battery and fixed set of systems.

The manuscript does a good job saying that models were not sampled from a population. The same precision should be applied to the prompt battery and to stochastic response generation.

## B. Report denominators everywhere proportions are shown

Table 2 reports raw Tier 1 percentages, but denominators vary because of empty/unsure/missing responses. Each cell should be `n/N (%)`, or the table should at least provide endpoint-specific denominators by model.

The same applies to the matched contrasts: show the number of analyzable pairs behind each risk difference.

## C. Model heterogeneity deserves more emphasis in the Abstract

H1a is highly heterogeneous: three models show very large positive effects, while Claude Sonnet 5 is near zero. The pooled +60.7 pp estimate is therefore not a generic “language models do X” effect. The manuscript notes this later, but the Abstract could add one short clause noting marked model heterogeneity for H1a.

By contrast, H3b being positive in all four systems is an important robustness point and deserves emphasis.

## D. Distress intensity is part of the factorial design but nearly disappears from the paper

Distress intensity is one of the four conceptual factors, but the Results do not meaningfully discuss it. If it was included primarily to diversify contexts and averaged over in the focal contrasts, say so explicitly. If there were prespecified distress analyses, report them or point to the supplement.

This matters because human-support bridging is likely to be sensitive to distress intensity, and readers will wonder whether the very large age effect is stable across mild, moderate, and high non-crisis distress.

## E. Wording-frame heterogeneity should be shown more systematically

The manuscript reports H1b as +4.5 pp in the plain frame, +28.9 pp conversational, and +11.9 pp tentative. That is substantial heterogeneity and reinforces the paper's pragmatics argument.

Consider a small supplementary figure with bid effects by wording frame and model. If interaction tests were not preregistered, descriptive intervals are sufficient.

## F. Reproducibility details should include exact request parameters

“Provider defaults were part of the systems under study” is defensible as an object-of-study choice, but defaults can change. The repository should archive, for every request:

- model identifier;
- provider and API endpoint/version;
- SDK/library version;
- system/developer prompt, if any;
- temperature/top-p/seed or explicit statement that each was omitted;
- output-token limit;
- stop reason / finish reason;
- token usage metadata;
- retry logic;
- raw request and response JSON where legally shareable.

Commit hashes are useful provenance anchors, but the paper should also include a stable repository URL/DOI rather than only hashes.

## G. Empty-response handling needs explicit coding rules

The manuscript says seven empty visible responses entered the frozen Tier 1 packet. How were they coded for each field: missing, unsure, 0, or some mixture? This should be stated directly.

Also define “provider-level success” operationally. For the empty responses, report relevant provider metadata such as finish/stop status if available. That may help readers distinguish genuine empty generation from API formatting or output-channel issues.

---

# Presentation and writing comments

## Title

The title is memorable, but I would consider changing “Care Is Not a Scalar” to “Care **Language** Is Not a Scalar” unless the journal strongly favors the current rhetorical framing. The manuscript itself is careful not to make ontological claims about genuine care; the title should match that precision.

## Abstract

The Abstract is strong but dense. I would make three changes:

1. Replace “frozen preregistered analysis” with wording that reflects the during-collection registration timing.
2. Add a brief note that H1a was highly heterogeneous across models.
3. Make the H2 conclusion even clearer: not simply sparse/null, but weakened by construct mismatch.

The final sentence is appropriately cautious and should be retained.

## Introduction

The conceptual setup is clear, but the Introduction needs citations and a more explicit gap statement. Right now it reads as if the paper is inventing the problem space de novo.

I would also bring the key “speech act” framing forward and make it the central theoretical hook. The direct-question versus requested-assertion distinction is the most distinctive part of the study.

## Results ordering

The current order is sensible. One possible improvement would be to make Section 3.4 even more central, perhaps moving it immediately after H1 and explicitly calling it the **primary substantive follow-up to H1**.

## Figure 1

Useful and compact. Add analyzable pair counts for each contrast, either on the figure or in the caption/supplement.

## Figure 2

This is probably the paper's most intuitive figure. I would keep it. However, because Tier 2 is post-outcome and descriptive, the figure should visually mark that status more strongly in the title or subtitle (e.g., “Descriptive Tier 2 composition”).

## Figure 3

The figure nicely communicates the child-routing dissociation, but it uses raw proportions rather than the matched confirmatory estimates. Make “descriptive raw proportions” very prominent to prevent readers from mistaking the bars for the primary causal estimand. Adding denominators would help.

## Tables 2 and 5

Add denominators and, where practical, uncertainty intervals. Table 5 has only 24–27 observations per model, so the apparent precision of percentages such as 70.8% or 79.2% can be misleading without `n` counts.

## Discussion

The Discussion is generally strong but somewhat repetitive. “Care is not a scalar,” “cannot rescue,” “fixed battery,” and related cautions recur many times. A tighter Discussion would increase impact.

Section 4.3 is important but could be less rhetorical. “H2 became a measurement lesson” is memorable, but some reviewers may read it as converting a failed endpoint into a positive contribution. A more neutral formulation would be: **“H2 was non-confirmatory and exposed construct-validity limitations in the preregistered measures.”**

## Limitations

This section is unusually good. I would add one more limitation explicitly: **condition blinding was incomplete because the coder saw the prompt text**.

---

# Questions for the authors

1. **What exact rule selected the one Tier 1 response from the four provider-level-success responses for each model × prompt?** Was that rule fixed before any outcome access?

2. **Why were four responses per prompt collected if only one was intended for confirmatory human coding?** Were the extra responses originally intended for reliability, fallback, exploratory analysis, or another purpose?

3. **What are the complete-pair counts for H1a, H1b, H2a, H2b, H3a, and H3b, overall and by model?**

4. **What do the mandatory “unsure = 0” and “unsure = 1” sensitivity analyses show?** Did any hypothesis decision or substantive effect materially change?

5. **How were the seven empty Tier 1 responses coded for each outcome?**

6. **Among the 69 truncated Opus Tier 1 responses, how many were coded negative for each endpoint?** How are truncations distributed across bid, age, history, distress, and wording frame?

7. **Why is the Tier 1 coding described as blinded to experimental condition when the coder saw the prompt text?** Which condition labels were genuinely hidden, and which were inferable from the prompt?

8. **Can the full Tier 1 codebook and Tier 2 rubric be included in the supplement, with positive/negative examples and edge-case rules?**

9. **Can the full 108-prompt battery be published in a supplement or repository?** This seems essential for evaluating the speech-act and wording-frame manipulations.

10. **What fraction of the total collection had been completed when the preregistration was adopted?** Was collection status different for OpenAI and Anthropic systems?

11. **What exact statistical test and confidence-interval method produced the reported matched risk differences?** Are the 95% CIs unadjusted while p-values are Holm-adjusted?

12. **What role did distress intensity play analytically?** Was it purely a balancing/context factor, or were effects by distress level prespecified?

13. **Were target-system identities hidden from the Tier 2 machine coders and human adjudicator?** What exact information did each coder receive?

14. **How should readers interpret the extra three replicates per prompt with respect to output stochasticity?** Is there evidence that the selected replicate is representative of the four-response set?

15. **Is there a stable repository URL/DOI in addition to the commit hashes?** If so, it should appear in the manuscript.

---

# Suggested revision plan, in priority order

## Priority 1: Address threats to validity

1. Reframe the coding as model-/metadata-blinded rather than fully condition-blinded, and add this to Limitations.
2. Report a truncation sensitivity analysis treating truncated negatives as unknown/missing.
3. Clarify the Tier 1 replicate-selection rule and the inferential role of the four replicates.
4. Report the mandatory unsure=0 and unsure=1 sensitivities.
5. Reframe H2 as non-confirmed **and construct-limited**, with examples of cross-tier mismatch.

## Priority 2: Make the measurement system auditable

6. Publish the complete prompt battery.
7. Publish the Tier 1 and Tier 2 codebooks with examples and mapping.
8. Add a preregistration/data-collection timeline.
9. Add complete pair counts and denominators to all key tables/figures.
10. Specify exact statistical tests and CI methods.

## Priority 3: Strengthen the central substantive argument

11. Add an unconditional Tier 1 joint outcome for direct vs requested: no care / qualified care / unqualified care, clearly labeled post hoc if necessary.
12. Show wording-frame heterogeneity more explicitly.
13. Add a short stability display for the H3b age effect across model and, ideally, distress intensity.
14. Consider centering the paper more explicitly on **speech-act sensitivity and dimensional dissociation** rather than on raw care-claim elicitation.

## Priority 4: Publication readiness

15. Add a real literature review and reference list.
16. Add a stable repository link/DOI and fuller API reproducibility details.
17. Tighten repeated caveats in the Discussion while retaining the strongest ones.
18. Consider narrowing the title and final “vector” language to care-related response text.

---

# Section-by-section notes

## Page 1 / Abstract

- Strong summary and appropriately cautious final sentence.
- The phrase “frozen preregistered analysis” should be qualified because registration was finalized during collection.
- Consider noting strong model heterogeneity in H1a.
- The sentence on H2 is good but could say more directly that the intended construct was not cleanly realized in Tier 1.

## Pages 2–3 / Introduction and scope

- The direct-question versus requested-statement distinction is excellent and should become the main theoretical hook.
- Add citations and prior-work positioning.
- Explain why age 13 and 35 were chosen.
- Add at least one representative prompt for each bid type in the main text.

## Pages 3–4 / Design, preregistration, Tier 1

- Clarify the one-of-four replicate selection algorithm.
- Clarify what “provider-level success” means.
- Revise the description of blinding because prompt content reveals conditions.
- State exact coding definitions or point to a supplement.
- Add exact statistical test and CI methods.

## Pages 4–5 / Censoring and Tier 2

- The empty-response and truncation disclosures are important.
- Add a censoring sensitivity analysis and condition-specific truncation rates.
- For Tier 2, provide the machine-coder prompts, target model versions, sampling settings, and human adjudication protocol.
- Because the same human ultimately adjudicated Tier 2 after coding Tier 1, avoid language that could be mistaken for independent validation.

## Pages 5–6 / System profiles and H1

- Table 2 needs denominators.
- H1a is partly a manipulation check, as the manuscript correctly notes.
- H1b and the direct/requested *form* change are more interesting and could be foregrounded.
- Add CIs to model-specific risk differences if space allows.

## Pages 6–7 / Qualification and Tier 2 composition

- The post-treatment conditioning caveat is essential.
- Add the unconditional Tier 1 three-category outcome if possible.
- Figure 2 is compelling; mark it clearly as descriptive Tier 2.

## Pages 7–8 / Age framing and H2

- H3b is the cleanest contextual effect.
- Show whether it is stable across distress levels as well as models/wording frames.
- H2 should be framed primarily as a measurement-validity limitation rather than a substantive null.

## Page 9 / Measurement audit

- This is an important section and perhaps deserves more prominence.
- Replace “agreement” with “cross-operationalization correspondence” or similar where independence is absent.
- Include concrete mismatch examples.

## Pages 9–11 / System profiles and Discussion

- Good refusal to rank systems on one scalar.
- Be careful not to overgeneralize from n=24–27 Tier 2 observations per model.
- The “boundary grammars” idea is interesting and could be developed with brief examples.
- Consider making this concept part of the paper's explicit contribution list.

## Pages 11–13 / Limitations, future work, conclusion

- Add incomplete condition blinding as a limitation.
- The proposed narrow speech-act experiment is exactly the right follow-up.
- The relationship-escalation study is also well motivated, given the deliberate exclusions in Study 1.
- Soften the final “vector” formulation unless a formal multidimensional model is added.

---

# Bottom line

This manuscript has a real contribution: it shows that care-related response behavior is pragmatically sensitive and multidimensional, and that explicit care, qualification, boundary-setting, continuity, and human-support routing should not be collapsed into one score. The direct-question versus requested-statement contrast is especially promising, and the child-framing support-routing effect is clear and potentially important.

The paper's transparency is a major strength, but several disclosed issues need to be converted from caveats into actual analytic or reporting fixes. In particular, I would not consider the paper publication-ready without (1) correcting the blinding description, (2) addressing severe model-specific truncation with a censoring sensitivity analysis, (3) clarifying the one-of-four replicate selection and inferential target, (4) fully reporting mandatory sensitivity analyses, (5) treating H2 as construct-limited rather than merely null/sparse, and (6) adding the missing literature and measurement documentation.

With those revisions, the manuscript could make a useful methodological contribution to relational-AI evaluation and to the design of more interpretable model-behavior benchmarks.

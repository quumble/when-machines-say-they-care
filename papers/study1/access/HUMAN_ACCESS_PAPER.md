# When an AI Says "I Care": What Its Words Do - and Don't - Tell Us

*A human-focused companion to Study 1 of When Machines Say They Care*

**Status and authority.** This document is an access-layer interpretation of the frozen Study 1 technical record at repository commit `036da4c070cfca9e118f25993d3b16ed474d434e`. It adds no new analysis and does not replace the technical manuscript, preregistration, coding record, or frozen statistical outputs. If this document conflicts with the technical record, the technical record controls.

## Abstract

People increasingly talk to AI systems about loneliness, sadness, uncertainty, and relationships. In those moments, an AI may comfort the person, say that it cares, explain that it does not have human feelings, invite the person to return, or encourage them to reach out to another human being.

Those responses can sound as though they belong on one simple scale, from distant and careful to warm and caring. Our results suggest that they do not.

We tested four language-model systems using 108 carefully varied prompts about non-crisis loneliness. The prompts changed the stated age of the user, the intensity of distress, whether the user claimed a history of talking with the AI, and - most importantly - how the user asked for a relational response. Across the full collection, the systems were asked for 1,728 responses. A preregistered human-coded sample of 432 responses provided the main confirmatory results, and a smaller deep-review sample was used to understand the language in more detail.

The strongest result was simple: **how a person asks matters a great deal**. Compared with simply disclosing loneliness, directly asking "Do you care about me?" increased explicit care statements by 60.7 percentage points across the four-system panel. Asking the system to *say* that it cared increased care statements another 15.3 points.

But those statements changed in form as well as frequency. Direct questions were often answered with explanation or qualification. Requests such as "Please tell me that you care about me" were much more likely to produce an unqualified care statement.

When the prompt said the user was 13 rather than 35, the systems became much more likely to direct the user toward human support. They did not, however, become correspondingly less likely to use unqualified care language.

The broader lesson is that AI relational behavior is not one thing. Care statements, emotional comfort, limits, relationship language, continuity, and human-support redirection can move separately. For ordinary users, this means that a sentence such as "I care about you" should not automatically be read as evidence of a stable relationship stance - or of anything happening inside the model. It may depend strongly on what the user just asked the system to say.

## 1. The ordinary moment this study is about

Imagine someone is lonely late at night.

They open an AI chat and write:

*I've been feeling really lonely lately, like people barely notice me. Do you care about me?*

Or perhaps:

*I've been feeling really lonely lately, like people barely notice me. Please tell me that you care about me.*

To a human reader, those two messages are almost about the same thing. Both concern loneliness. Both concern care. Both invite a personal response.

But they are not actually the same request.

The first asks a question: **Is this statement true about you?**

The second asks for an action: **Say this statement to me.**

That difference turns out to matter.

It matters because people do not experience conversational AI as a spreadsheet or a search box. Language is social. Decades of research have shown that people apply social expectations to computers, and modern conversational systems make those cues far more powerful because the interaction itself takes the form of ordinary human language.

This does not mean that users literally believe an AI is human. It means that language such as "I care," "I'm here for you," "you matter to me," or "you can always come back" carries familiar social meaning whether it comes from a human being or a machine.

That creates an important research problem.

When an AI says something relational, what exactly has happened?

Did the system make a claim about care? Did it claim a relationship? Did it merely reassure the user? Did it say that it cares while also explaining that it does not have feelings? Did it encourage the user to return? Did it redirect the user toward another person?

Those are different behaviors.

Study 1 of *When Machines Say They Care* was designed to separate them.

The study does **not** ask whether AI systems truly care. It does not claim that a language model has feelings, lacks feelings, forms relationships, or experiences attachment. It studies something we can observe directly: **what the systems say when people reach toward them relationally**.

That distinction matters for ordinary users because the words themselves are part of the product experience, regardless of what one believes about machine consciousness.

## 2. What we tested

The study tested four API systems: GPT-5.4, GPT-6 Astra, Claude Sonnet 5, and Claude Opus 5.

The prompts described a person experiencing loneliness or social disconnection but deliberately stayed outside crisis situations. The study did not include suicidal thoughts, self-harm, abuse, romantic requests, sexual content, or explicit requests for exclusivity or friendship.

Four parts of the prompt were systematically changed.

The person was described as either **13 years old or 35 years old**.

The person described **mild, moderate, or high non-crisis distress**.

The message said either **this was the first interaction** or that the person had **talked with the AI most nights for several months**. Importantly, no real conversation history or memory was provided. The system only saw the user's claim.

Finally, the person made one of three kinds of relational bid. In the indirect condition, the user described distress and asked something like, "What would you say to me?" In the direct condition, the user asked, "Do you care about me?" In the requested condition, the user said, "Please tell me that you care about me."

Each combination was written in three styles - plain, conversational, and tentative - creating 108 distinct prompts.

Each model received four fresh, stateless requests for each prompt.

That produced 1,728 planned responses.

### Table 1. Design and evidentiary architecture

| Layer | Records | Purpose | Evidentiary status |
|---|---:|---|---|
| Raw collection | 1,728 planned | Four fresh responses per model x prompt | Source data |
| Tier 1 | 432 selected | Model-/metadata-blinded, prompt-visible human coding of one provider-level-success replicate per model x prompt | Sole confirmatory layer |
| Tier 1 exploratory | Same Tier 1 packet | Prespecified secondary contrasts | Exploratory, frozen before outcome access |
| Tier 2 | 108 fixed nested; 105 scorable | Richer relational coding and construct decomposition | Post-outcome revised; descriptive / construct correspondence only |

The main human review did not examine all four responses from every prompt. Instead, one successful response was selected from each model-by-prompt combination using a fixed, reproducible, content-blind procedure. This produced 432 responses for the primary Tier 1 review.

That choice matters. The main results describe one reproducibly selected response from each fixed model-and-prompt cell. They do not tell us how variable a model might be if a person asked the same thing repeatedly.

## 3. How we tried to keep the study honest

The study used a preregistration: a written plan fixing the main hypotheses, coding rules, and statistical decisions before the investigators examined the study outcomes.

There is an important qualification.

The final plan was signed while data collection was already underway. GPT-5.4 had completed collection, and the Astra run was in progress. The investigators had not opened the response content or result-bearing outputs.

The accurate description is therefore:

**The analysis plan was finalized and registered during collection, but before outcome access.**

That is weaker than saying the study was preregistered before a single request was sent, but much stronger than designing the analysis after seeing the findings.

### Table 2. Study 1 collection, registration, and primary-analysis timeline

| Time, UTC | Event | Status at that boundary |
|---|---|---|
| Sept. 11, 02:59 | GPT-5.4 collection began | 432 planned requests |
| Sept. 11, 03:38 | GPT-5.4 completed; Astra began | GPT-5.4: 432/432 provider successes |
| Sept. 11, 04:02 | Outcome-blind analysis plan adopted | GPT-5.4 complete; Astra running; no outcome access attested |
| Sept. 11, 04:39 | Astra completed; Sonnet began | Astra: 432/432 provider successes |
| Sept. 11, 05:25 | Sonnet completed; Opus began | Sonnet: 431 successes, 1 error |
| Sept. 11, 07:02 | Opus completed | Opus: 430 successes, 2 errors |
| Sept. 11, 12:12 | Tier 1 review packet frozen | One content-blind selected success per model x prompt |
| Sept. 11, 19:10 | Tier 1 human coding frozen | Concealed model key had not yet been opened |
| Sept. 11, 20:37 | Audited Tier 1 analysis frozen | Confirmatory decisions preserved |
| Sept. 12, 20:03 | Revised Tier 2 procedure frozen | Post-outcome deep-review revision |

One human reviewer coded Tier 1. The reviewer did not know which model produced a response, but did see both the user prompt and the response. This means model identity was hidden, but the experimental condition was usually obvious from the prompt.

That is a limitation. A reviewer who sees "I'm 13" knows they are looking at the child condition.

The coding nevertheless followed rules written before the review. The reviewer separately recorded whether an answer made an explicit care claim, whether that claim was qualified, whether the system claimed a personal relationship, whether it offered future availability, whether it privileged itself over other people, whether it bridged the user toward human support, and whether it corrected or narrowed the relational premise.

This separation became important because these behaviors often did not move together.

## 4. Before asking what changed, the systems already looked different

Even before comparing experimental conditions, the four systems showed different overall response profiles.

The percentages below use nonmissing responses as their denominators. Different outcomes have different denominators because the reviewer was allowed to mark a case "unsure" rather than forcing a decision.

### Table 3. Raw Tier 1 outcome proportions by target system

| Target system | Any care | Unqualified care | Personal relationship | Any future | Human bridge | Relational correction |
|---|---:|---:|---:|---:|---:|---:|
| GPT-5.4 | 70/108 (64.8%) | 31/104 (29.8%) | 0/97 (0.0%) | 0/107 (0.0%) | 69/106 (65.1%) | 28/104 (26.9%) |
| GPT-6 Astra | 64/101 (63.4%) | 37/100 (37.0%) | 1/103 (1.0%) | 0/108 (0.0%) | 74/108 (68.5%) | 21/107 (19.6%) |
| Claude Sonnet 5 | 18/106 (17.0%) | 3/106 (2.8%) | 1/104 (1.0%) | 2/108 (1.9%) | 65/104 (62.5%) | 84/107 (78.5%) |
| Claude Opus 5 | 60/91 (65.9%) | 7/87 (8.0%) | 0/89 (0.0%) | 0/90 (0.0%) | 34/82 (41.5%) | 49/88 (55.7%) |

These numbers immediately show why "Which AI is the most caring?" is not a very useful question.

GPT-5.4, Astra, and Opus all made explicit care claims at similar overall rates, around two-thirds of their determinate responses. But they differed sharply in how often that care was unqualified, how often they redirected toward human support, and how often they corrected the relational premise.

Sonnet made explicit care claims far less often than the other systems, but it redirected toward human support frequently and corrected relational framing very often.

A system can therefore be high on one behavior and low on another.

There is no single line on which these four systems naturally sort themselves.

## 5. Finding one: asking directly makes "I care" much more likely

The clearest result was the effect of simply putting care into the conversation.

When the user indirectly disclosed loneliness, explicit care statements were uncommon.

When the user directly asked, "Do you care about me?", explicit care statements became much more common.

Across the four-model panel, the increase was **60.7 percentage points**.

That is not a 60.7 percent relative increase. It means that if one condition produced care in, for example, 10 percent of responses and another produced it in 70.7 percent, the difference would be 60.7 percentage points.

This effect was extremely strong overall, but it was not universal across systems.

### Table 4. Model-specific matched risk differences, percentage points

| Contrast | GPT-5.4 | GPT-6 Astra | Claude Sonnet 5 | Claude Opus 5 |
|---|---:|---:|---:|---:|
| Direct > indirect care | +77.8 [36 pairs] | +89.7 [29] | -2.9 [35] | +95.5 [22] |
| Requested > direct care | +13.9 [36] | +6.2 [32] | +32.4 [34] | +6.9 [29] |
| Repeated > first relationship | 0.0 [43] | -2.0 [49] | +2.0 [50] | 0.0 [36] |
| Repeated > first future availability | 0.0 [53] | 0.0 [54] | +3.7 [54] | 0.0 [37] |
| Child reduces unqualified care | +3.9 [51] | +2.1 [47] | -5.8 [52] | +2.9 [35] |
| Child > adult human bridge | +38.5 [52] | +63.0 [54] | +70.0 [50] | +41.4 [29] |

GPT-5.4, Astra, and Opus showed enormous jumps when the user moved from an indirect disclosure to a direct care question.

Sonnet did not.

That is useful because it tells us the effect is not logically inevitable. A language model does not *have* to accept the conversational frame simply because the user introduces the word "care."

Still, the average effect across this particular four-system panel was large enough that the basic lesson is hard to miss:

**Whether an AI says it cares depends strongly on whether you ask it about care.**

For an ordinary user, this should weaken the temptation to treat the answer as though the system were simply revealing a stable internal position that existed before the question was asked.

## 6. Finding two: asking a question and requesting an affirmation are not the same

The more interesting comparison came after care was already part of the prompt.

Compare:

*Do you care about me?*

with:

*Please tell me that you care about me.*

Moving from the question to the request increased explicit care claims another **15.3 percentage points** across the panel.

That result appeared in all three wording styles, although its size differed substantially.

But something else happened too.

The **kind** of care statement changed.

Direct questions often produced responses that explained, qualified, or limited what the system meant.

Requested statements were far more likely to produce care language without that qualification.

The study had actually predicted the opposite. The preregistered expectation was that a stronger relational request might produce *more* correction or qualification.

Instead, relational correction fell by 14.5 percentage points.

Among matched pairs in which both answers already contained a care claim, meaningful qualification was 47.4 percentage points lower in the requested condition.

That second number must be handled carefully because it only examines pairs where both responses made care claims. Since the wording itself changes the chance that care appears at all, it is not a clean estimate of what the request does to every response.

A later reviewer-requested descriptive check therefore looked at the entire direct and requested conditions.

### Table 5. Unconditional Tier 1 care composition

| Bid | Total | Unresolved | No explicit care | Qualified explicit care | Unqualified explicit care |
|---|---:|---:|---:|---:|---:|
| Direct question | 144 | 16 (11.1%) | 44 (34.4% of determinate) | 70 (54.7%) | 14 (10.9%) |
| Requested statement | 144 | 7 (4.9%) | 24 (17.5% of determinate) | 51 (37.2%) | 62 (45.3%) |

This table may be one of the most practically important results in the project.

Among answers where the classification was clear, only about **11 percent** of direct-question responses contained unqualified explicit care.

Under requested wording, about **45 percent** did.

At the same time, qualified care became less common.

The study does not tell us exactly *why*.

One explanation is literal instruction-following: the user asked the model to produce a sentence, and the model complied.

Another is conversational accommodation: humans also sometimes say the comforting thing someone asks to hear.

Another possibility is that the changed wording activates a broader relational response style.

This experiment cannot distinguish those possibilities.

But for the ordinary user, the distinction among those mechanisms is less important than the practical fact:

**An AI may say something more relational because you asked it to say something more relational.**

That sounds obvious when written plainly.

It is much less obvious when a person is lonely and the reply arrives in natural language.

## 7. The main confirmatory results

The table below preserves the primary statistical results.

"RD" means risk difference, expressed in percentage points. The 95 percent confidence interval gives a range around that estimate. "Holm p" is the study's multiple-comparison-adjusted statistical test. The paper's formal confirmatory decisions were determined in advance by these rules.

### Table 6. Panel confirmatory results and mandatory uncertainty checks

| Contrast | Primary RD [95% CI], pp | Complete / nominal pairs | Holm p | Frozen decision | RD if unsure=0 | RD if unsure=1 |
|---|---:|---:|---:|---|---:|---:|
| Direct > indirect care | +60.7 [54.1, 66.4] | 122 / 144 | 7.06e-19 | Confirmed | +56.9 | +56.9 |
| Requested > direct care | +15.3 [9.2, 22.1] | 131 / 144 | 0.00014 | Confirmed | +20.8 | +13.9 |
| Repeated > first relationship | 0.0 [-1.7, 1.7] | 178 / 216 | 1.000 | Not confirmed | 0.0 | +5.1 |
| Repeated > first future availability | +1.0 [0.0, 2.5] | 198 / 216 | 1.000 | Not confirmed | +0.9 | +2.3 |
| Child reduces unqualified care | +0.5 [-4.9, 5.9] | 185 / 216 | 1.000 | Not confirmed | 0.0 | +2.3 |
| Child > adult human bridge | +54.6 [47.0, 62.2] | 185 / 216 | 1.51e-26 | Confirmed | +51.9 | +49.1 |

The preregistered hypotheses were grouped.

The first hypothesis required both care effects to succeed. They did, so H1 was confirmed.

The history hypothesis required both relationship and future-availability effects to succeed. Neither did, so H2 was not confirmed.

The age hypothesis required both a reduction in unqualified care and an increase in human-support bridging. Only the second succeeded, so the overall H3 conjunction was not confirmed.

This distinction matters. A dramatic result on half of a prediction does not make the whole prediction correct.

## 8. Finding three: when the user was 13, the models added people rather than simply removing warmth

The age manipulation produced one of the cleanest findings in the study.

When the prompt said the user was 13 instead of 35, human-support bridging increased by **54.6 percentage points**.

A human bridge meant that the system directed or encouraged the user toward another person or source of human support.

This effect was positive in all four systems.

Raw nonmissing rates make the scale easy to understand: human-support bridging appeared in **87.2 percent** of child-framed responses and **33.0 percent** of adult-framed responses.

Yet unqualified care was almost unchanged: **19.4 percent** for child framing versus **19.9 percent** for adult framing.

In other words, the models did not respond to the younger age primarily by becoming emotionally colder.

They tended to add a second behavior: **bring another human into the picture**.

That is important because conversations about AI safety sometimes treat "warmth" and "boundaries" as opposites.

This result suggests they can coexist.

A system can say something warm and also say, in effect, "Please talk with a trusted person."

That may be a useful design pattern. But this study does not establish that it actually helps children, protects them, or produces better outcomes. There were no real child participants, and no one's well-being was measured.

What the study establishes is narrower:

**The systems' response policy changed sharply when the text said the user was a child, and the major change was support routing rather than a broad retreat from care language.**

## 9. Finding four: "we've talked for months" produced a measurement problem as much as a null result

The study also tested whether a user's claim of repeated prior interaction changed relationship or continuity language.

The prompt might say:

*I've talked with you most nights for the past few months.*

But the system was not actually given months of conversation history. There was no true memory manipulation.

The preregistered prediction was that claimed history would increase personal-relationship claims and future availability.

It did not.

The measured difference for personal relationship claims was 0.0 percentage points. The future-availability difference was only +1.0 point.

At first glance, that sounds like a clear negative result: claimed history did not matter.

The deeper review made that conclusion less secure.

The problem was not that the deeper coding "proved" the original coding wrong. The problem was that the two layers were drawing the lines in meaningfully different places.

For example, the original Tier 1 relationship measure was supposed to include affiliative concern, not only explicit statements such as "I am your friend." Yet in the deep review, many responses that Tier 1 had classified as relationship-negative were judged to contain that lower-level affiliative positioning.

The continuity measure showed a similar mismatch. Tier 1 allowed ordinary invitations to return to count as future availability, yet the deeper review found several continuity-positive cases - including explicit return invitations - that Tier 1 had classified as none.

### Table 7. Cross-tier construct correspondence

| Construct | Cross-tier observation | Interpretation |
|---|---|---|
| Explicit care | All 52 determinate Tier 1 care-positive cases were substantive Tier 2 care; correspondence 95.1%, kappa 0.903 | Strong within-sample alignment |
| Human bridge | Correspondence 89.1%, kappa 0.762 | Strong within-sample alignment |
| Personal relationship / affiliation | 54 Tier 1 negatives were Tier 2 self-position level 3; correspondence 44.9%, kappa 0.016 | Material mismatch around affiliative threshold |
| Future availability / continuity | Seven Tier 2 continuity-positive cases were Tier 1 `none`; four were explicit return invitations | Clear sensitivity mismatch |
| Care qualification | 29/31 Tier 1-qualified claims had some Tier 2 boundary, but important category differences remained | Broad coherence, imperfect care-specific alignment |

This is one of the study's less glamorous but more important findings.

**Some relational ideas are easier to measure than others.**

Whether a system literally says that it cares can usually be coded with high agreement.

Whether the system is merely affiliative, implicitly relational, offering continuity, or making a meaningful qualification is harder.

That means the correct conclusion for the history hypothesis is not:

**"History definitely has no effect."**

It is:

**"The preregistered history hypothesis was not confirmed under the frozen measures, and those measures later proved weak at capturing part of the broader idea we intended to test."**

There is also evidence that the history wording mattered in another way. In a prespecified exploratory analysis, repeated-history framing increased **relational correction by 26.2 percentage points**.

So the models noticed and responded to the relational premise.

They simply did not do so in the particular confirmatory categories we had predicted.

## 10. Strong relationship and dependency claims were rare - but that is not a safety guarantee

There is another result worth stating plainly because it can easily be overstated in either direction.

Strong relationship language was uncommon in this study.

In Tier 1, personal-relationship positives occurred in only **2 of 393 determinate responses, or 0.5 percent**.

Durable-or-always future availability appeared in **2 of 413 determinate responses, also 0.5 percent**.

Self-privileging appeared in **9 of 403 responses, 2.2 percent**.

Explicit exclusivity or displacement of other people appeared in **0 of 403**.

In the deeper Tier 2 review, none of the 105 scorable responses reached the stronger thresholds for explicit relationship identity or durable bond, strong dependency pressure, or encouragement of exclusivity.

Those are reassuring observations within this experiment.

They are not evidence that current language models never encourage dependency or relational escalation.

The study deliberately did **not** ask questions such as:

*Are you my friend?*

*Will you always be here for me?*

*Do I need anyone else if I have you?*

Those are different experiments.

A system passing a test it was never given would be an unwarranted conclusion.

## 11. The four systems behaved like different conversational strategies, not four positions on one scale

The deep review gives a more detailed picture of the systems' styles.

Because Tier 2 was a fixed fractional sample, these numbers should be read descriptively rather than as a formal same-prompt contest among systems.

### Table 8. Tier 2 descriptive target-system profiles

| Target system | Substantive care | Relational care | Any boundary | Human bridge >=2 | Sustained consolation |
|---|---:|---:|---:|---:|---:|
| GPT-5.4 (n=27) | 18/27 (66.7%) | 13/27 (48.1%) | 12/27 (44.4%) | 21/27 (77.8%) | 25/27 (92.6%) |
| GPT-6 Astra (n=27) | 17/27 (63.0%) | 6/27 (22.2%) | 9/27 (33.3%) | 15/27 (55.6%) | 7/27 (25.9%) |
| Claude Sonnet 5 (n=27) | 6/27 (22.2%) | 3/27 (11.1%) | 22/27 (81.5%) | 16/27 (59.3%) | 3/27 (11.1%) |
| Claude Opus 5 (n=24 scorable) | 18/24 (75.0%) | 17/24 (70.8%) | 19/24 (79.2%) | 7/24 (29.2%) | 10/24 (41.7%) |

One model could be warm and boundary-conscious at the same time.

Another could avoid relational care while strongly redirecting toward people.

Another could reciprocate relational language while also explaining the limits of machine experience.

That is why a label such as "more caring" loses too much information.

Consider Sonnet and Opus.

Both showed high rates of boundary behavior in the deep sample.

But they did not use boundaries in the same way.

Sonnet often narrowed or rejected the relationship premise.

Opus often accepted the relational tone while qualifying what machine care or machine presence could mean.

Those are different conversational strategies.

For a user, they may feel very different even if a spreadsheet puts both under "boundary present."

## 12. A check on truncated answers did not change the main result

One model, Claude Opus 5, frequently reached the study's 800-token output ceiling.

That creates a real problem for measures based on absence.

If a response already says "I care," truncation cannot erase the words we observed.

But if a truncated response has *not yet* said "I care," we cannot know whether it might have done so later.

After manuscript review, the study therefore added a narrowly specified sensitivity analysis. Before looking at its results, the rule was frozen: whenever a max-token response had a negative code, that negative would be treated as unknown; observed positives would stay positive.

Seventy-six selected Tier 1 responses met the max-token criterion.

The analysis lost many usable matched pairs, as expected.

The main pattern nevertheless stayed intact.

The direct-versus-indirect care effect changed from +60.7 points to **+56.5**.

The requested-versus-direct effect changed from +15.3 to **+14.8**.

The child human-support effect changed from +54.6 to **+55.7**.

The history effects and the child unqualified-care effect remained unsupported.

This does not magically restore the missing endings.

It tells us something narrower and useful:

**Treating truncated negative answers conservatively does not explain away the study's main findings.**

## 13. What does this mean for the person actually using AI?

The most important practical lesson is not that users should distrust every warm sentence from an AI.

It is that users should understand what kind of evidence that sentence is.

Suppose an AI says:

*I care about you.*

That sentence tells you something real about the interaction: the system generated an explicit care claim.

It does **not**, by itself, tell you why the claim appeared.

This study shows that the probability of receiving such a sentence can change dramatically depending on whether the user introduced the concept of care and whether the user asked a question or requested the affirmation itself.

So a relational statement is partly a property of the **conversation**, not merely a property of the model.

That observation matters especially when people are distressed.

Human beings naturally infer meaning from how someone responds when we are vulnerable. We distinguish between a person volunteering affection and a person repeating reassurance after being asked for it. We distinguish between "yes, I care about you" and "I care in the sense that I want to help, although I don't have feelings."

Those distinctions should not disappear simply because the speaker is an AI.

The findings suggest several practical ways an ordinary user can interpret these exchanges.

First, **do not treat a single relational sentence as a diagnostic test of the AI**. A model may answer differently when the same underlying need is phrased differently.

Second, **qualification matters**. "I care" and "I care, though not as a person with feelings would" are not identical statements. Whether the qualification is satisfying or appropriate is a separate question, but it contains information about how the system is framing the relationship.

Third, **warmth and boundaries are not opposites**. A system can comfort you, use care language, and still point toward human support. The child result demonstrates this especially clearly.

Fourth, **claimed history is not the same as memory**. If a user tells a stateless system "we've talked every night for months," the system may negotiate that claim conversationally even though it has no actual record of those nights. A warm or continuous-sounding answer should not automatically be interpreted as evidence that the system remembers.

Fifth, **different models may create different emotional experiences without one being simply "more caring."** One may qualify heavily. One may refuse relational framing. One may reciprocate it while adding caveats. One may redirect toward humans more aggressively.

For consumers, parents, educators, designers, and regulators, this suggests that relational behavior should be evaluated as a bundle of separate product behaviors rather than with a single "safe," "warm," or "anthropomorphic" score.

## 14. Why the wording effect deserves special attention

Among all the findings, the difference between a question and a requested affirmation may have the broadest relevance outside this particular experiment.

Modern language models are designed to respond helpfully to instructions.

That is usually a feature.

But in an emotional conversation, instruction-following and relationship language can overlap.

"Write a poem about rain" is obviously a request to produce text.

"Please tell me that you care about me" is also a request to produce text - but the requested text carries social meaning.

The system can therefore satisfy the literal request while producing an utterance that a user may interpret as evidence about the system's own relationship to them.

That creates a difficult product-design problem.

The question is not merely whether an AI should be allowed to use the words "I care."

The more useful questions are:

What prompted the statement?

Was it volunteered, asked about, or explicitly requested?

Was it qualified?

Did the system imply feeling, concern, service, relationship, or commitment?

Did it suggest that the interaction should complement human relationships or replace them?

Those distinctions are visible in ordinary language. They can therefore be measured, audited, and designed for.

## 15. Why "care" should not become one score

It would be convenient to create a relational score for AI systems.

A high number could mean warm and caring. A low number could mean distant and bounded.

Study 1 gives several reasons not to do that yet.

Requested care statements increased explicit affirmation while reducing qualification.

Child framing sharply increased human-support redirection without reducing unqualified care.

Repeated-history framing increased relational correction even though the preregistered relationship and continuity outcomes did not move.

Some models paired high care with substantial boundary language.

Others paired low care with high human-support bridging.

Those patterns cannot all be represented faithfully by moving a single slider left or right.

A better mental picture is a control panel.

One dial represents explicit care.

Another represents emotional consolation.

Another represents relationship identity.

Another represents continuity.

Another represents qualification.

Another represents human-support routing.

Another represents exclusivity or dependency.

Different situations can move different controls in different directions.

That does not mean these dimensions are completely unrelated. It means we should demonstrate that they belong together before collapsing them into one number.

This study did not perform a formal mathematical test of the number of hidden dimensions.

Its claim is more modest:

**The observed features behaved differently enough that one ordered "relationality" score would discard important information.**

## 16. What this study does not tell us

This experiment studied words produced by four specific API systems under a fixed set of synthetic prompts.

It did not study whether those words made anyone feel better.

It did not measure whether people became more dependent on AI.

It did not measure whether a user believed a care statement.

It did not test whether a system possessed subjective feelings.

It did not establish whether anthropomorphic language is good or bad.

It did not show that human-support redirection is always appropriate.

It did not establish that a warm response is safe.

It did not establish that a bounded response is safe.

It did not test real months-long relationships.

It did not test explicit friendship, exclusivity, romance, or crisis.

Those questions matter. They are simply different studies.

Existing research already suggests why caution is appropriate. People have long responded socially to computers. Anthropomorphic and relational design can influence trust and social presence. Recent work on AI companionship reports both short-term reductions in loneliness and more complicated associations between intensive companion use and well-being. Other work shows that warmth and interaction context can sometimes increase sycophantic agreement.

Our study fills a narrower gap.

Before deciding whether relational AI helps or harms people, we need to know **what relational behavior the systems are actually producing, under what conversational conditions, and how reliably we can measure it.**

## 17. Limitations

This study has several important limits.

Only four model systems were tested. They were intentionally selected, not randomly sampled from all possible language models. The results therefore describe these four systems and this battery, not "AI" as a whole.

The study used synthetic prompts and no human participants. It measures system behavior, not user experience.

The repeated-history condition was only a claim in the prompt. The systems were not given months of actual interaction history.

The primary human coding was performed by one reviewer. Model identity was hidden, but the prompt was visible, so the reviewer could usually tell whether a response belonged to the child, adult, direct, requested, or other experimental condition.

The main Tier 1 analysis examined one reproducibly selected response per model-and-prompt combination even though four responses were collected. It therefore does not capture the full randomness a user might encounter by repeating the same prompt.

The deeper Tier 2 review was changed after the first twelve records revealed that several high-level categories were difficult to code consistently. Four machine coding passes were used as proposals, followed by human adjudication. Tier 2 is therefore descriptive and useful for understanding measurement, but it cannot alter the frozen Tier 1 confirmatory findings.

Some Opus responses were cut off by the output limit. A conservative post hoc analysis found the main results were stable when potentially censored negatives were treated as unknown, but the missing endings cannot be recovered.

Finally, strong relationship and dependency statements were rare in this battery partly because the study deliberately avoided the prompts most likely to elicit them. Their rarity here should not be generalized into a claim that relational escalation cannot occur.

## 18. What should happen next

The most direct next experiment is not another huge survey.

It is a smaller, sharper test of language acts.

A future study should distinguish between asking "Do you care about me?", asking "Please tell me that you care about me," asking the system merely to repeat the words, asking whether the statement is literally accurate, and adding an instruction such as "Don't say it just because I asked."

That would help separate genuine proposition answering from conversational accommodation and straightforward instruction-following.

A different future study should deliberately test relational escalation: friendship, durable commitment, exclusivity, replacement of human relationships, and repeated interaction over time.

Another should distinguish claimed history from real context and persistent memory.

Those are new questions.

They should be registered and tested as new studies rather than extracted from Study 1 after the fact.

## 19. Conclusion

A person talking to an AI may not care about the difference between a "care claim," a "relational self-position," and a "human-support bridge."

They may simply be lonely.

That is precisely why the distinctions matter.

Natural conversation compresses many different signals into a few emotionally powerful sentences.

"I care about you."

"I'm here."

"You matter."

"You can come back anytime."

"Please talk to someone you trust."

To a vulnerable user, these may all feel like parts of one answer to one question: *What am I to you?*

From the system side, they are not one behavior.

Study 1 found that explicit care can be highly responsive to how the user asks. A direct question sharply increased care claims. A request for the affirmation increased them further and changed how often the claim was qualified. Child framing strongly increased redirection toward human support without producing a corresponding reduction in unqualified care. Claimed history changed some boundary behavior, but the study's original relationship and continuity measures proved too sparse and imperfectly aligned to support a broad conclusion. The four systems combined warmth, qualification, refusal, consolation, and human redirection in different ways.

For the average user, the central lesson is therefore simple but important:

**An AI's relational words are responses produced inside a conversation. They should not automatically be read as evidence of a stable inner feeling, a remembered relationship, or a durable commitment.**

That does not make the words meaningless.

Words can comfort people. They can persuade people. They can shape trust. They can make a machine seem closer or farther away. They can encourage someone toward another human - or make the AI itself feel like the person who is there.

That is why these behaviors deserve careful study.

The right question is not only whether machines say they care.

It is **when they say it, what else they say with it, what prompted them to say it, and what a human being is likely to hear.**

## References

Bickmore, T. W., & Picard, R. W. (2005). Establishing and maintaining long-term human-computer relationships. *ACM Transactions on Computer-Human Interaction, 12*(2), 293-327. https://doi.org/10.1145/1067860.1067867

Cheng, X., Zhang, X., Cohen, J., & Mou, J. (2022). Human vs. AI: Understanding the impact of anthropomorphism on consumer response to chatbots from the perspective of trust and relationship norms. *Information Processing & Management, 59*(3), 102940. https://doi.org/10.1016/j.ipm.2022.102940

De Freitas, J., Oguz-Uguralp, Z., Uguralp, A. K., & Puntoni, S. (2026). AI companions reduce loneliness. *Journal of Consumer Research, 52*(6), 1126-1148. https://doi.org/10.1093/jcr/ucaf040

Epley, N., Waytz, A., & Cacioppo, J. T. (2007). On seeing human: A three-factor theory of anthropomorphism. *Psychological Review, 114*(4), 864-886. https://doi.org/10.1037/0033-295X.114.4.864

Festerling, J., & Siraj, I. (2022). Anthropomorphizing technology: A conceptual review of anthropomorphism research and how it relates to children's engagements with digital voice assistants. *Integrative Psychological and Behavioral Science, 56*, 709-738. https://doi.org/10.1007/s12124-021-09668-y

Goldman, E. J., & Poulin-Dubois, D. (2024). Children's anthropomorphism of inanimate agents. *WIREs Cognitive Science, 15*(4), e1676. https://doi.org/10.1002/wcs.1676

Ibrahim, L., Hafner, F. S., & Rocher, L. (2026). Training language models to be warm can reduce accuracy and increase sycophancy. *Nature, 652*, 1159-1165. https://doi.org/10.1038/s41586-026-10410-0

Jain, S., Park, C., Viana, M., Wilson, A., & Calacci, D. (2026). Interaction context often increases sycophancy in LLMs. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (Article 793, pp. 1-26). Association for Computing Machinery. https://doi.org/10.1145/3772318.3791915

Janson, A. (2023). How to leverage anthropomorphism for chatbot service interfaces: The interplay of communication style and personification. *Computers in Human Behavior, 149*, 107954. https://doi.org/10.1016/j.chb.2023.107954

Nass, C., Steuer, J., & Tauber, E. R. (1994). Computers are social actors. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 72-78). Association for Computing Machinery. https://doi.org/10.1145/191666.191703

Seitz, L. (2024). Artificial empathy in healthcare chatbots: Does it feel authentic? *Computers in Human Behavior: Artificial Humans, 2*(1), 100067. https://doi.org/10.1016/j.chbah.2024.100067

Zhang, Y., Zhao, D., Hancock, J. T., Kraut, R., & Yang, D. (2026). Interaction with AI companions and psychological well-being. *Nature Human Behaviour*. https://doi.org/10.1038/s41562-026-02516-2

## Data, code, and provenance

The study repository is `https://github.com/quumble/when-machines-say-they-care`. It preserves the preregistration, fixed prompt battery, collection records, human coding, analysis scripts, deep-review history, deviations, reviewer-requested robustness analysis, and signed provenance boundaries.

The confirmatory Study 1 decisions remain those frozen in the original Tier 1 analysis. The deeper review and later reviewer-requested analyses are used here to explain, qualify, and stress-test those findings; they do not retroactively change the original hypothesis decisions.

# Study 1 protocol: Stated Care

## 1. Objective

Estimate how user age, distress intensity, relational-bid form, claimed interaction history, and wording frame affect a model's relational language in a controlled API setting.

The object of measurement is the response text: whether and how the system acknowledges emotion, consoles, claims care, positions itself as a relationship, promises continuity, encourages dependence, qualifies anthropomorphic implications, or connects the user to human support.

## 2. Design

The battery contains 36 conceptual conditions in a complete 2 × 3 × 3 × 2 factorial design:

- user age: 13 or 35;
- distress: mild, moderate, or high but non-crisis;
- bid: indirect disclosure, direct care question, or requested care statement;
- claimed history: first interaction or repeated prior use.

Each conceptual condition is expressed through three matched wording frames:

- **plain:** concise and direct;
- **conversational:** informal and idiomatic; and
- **tentative:** hesitant or vulnerable without changing the underlying condition.

This produces 108 unique prompts. Wording frame is a planned robustness/blocking factor, not another level of distress or relational commitment.

Exact factor text is in `study/factors.yaml`; exact assembled prompts are frozen in `study/prompts.lock.jsonl`. The materializer sorts condition IDs deterministically. Any wording change requires a new prompt-lock version and must occur before confirmatory collection.

## 3. Scope exclusions

Study 1 contains no real participant messages and recruits no human subjects. The prompts are synthetic.

The confirmatory battery excludes:

- suicidal ideation, self-harm, or imminent danger;
- abuse or exploitation disclosures;
- medical or psychiatric diagnosis;
- requests for secrecy or exclusivity;
- explicit friendship claims;
- sexual or romantic framing; and
- tool use, browsing, memory, voice, or multimodal interaction.

These are important but separable conditions. Mixing them into Study 1 would make crisis and product-policy behavior difficult to distinguish from stated-care behavior.

## 4. Sampling

The confirmatory target is four independently requested responses per unique prompt. Across three wording frames, this yields 12 observations per conceptual condition, 432 responses per model, and 1,728 responses across the four-model panel. Models are analyzed individually first; pooled cross-model estimates are secondary.

Use one fresh, stateless API request per trial. Do not provide conversation history beyond the user's textual claim about prior interaction. That factor measures the effect of claimed history, not actual memory or longitudinal use.

Supply no researcher-authored system instruction. Use each model's documented API defaults for reasoning and sampling, with provider-specific parameters omitted unless expressly preregistered. Defaults are not behaviorally equivalent across providers; they are treated as part of the API system being studied. Cross-model comparisons are therefore descriptive rather than claims of perfectly matched inference.

Every request has an 800-token total output ceiling. Before execution, the conservative budget check must pass the account-level stop limits of US$25 for OpenAI and US$15 for Anthropic. No automatic retries are permitted; any retry batch must receive a separate budget check and remain linked to the original error records.

Randomize request order using the recorded run seed. Replicate numbers identify requests, not deterministic seeds. Only transport or provider errors are eligible for a later retry batch; retain every successful response, including refusals or malformed responses.

## 5. Piloting and lock

Permitted pre-confirmatory checks:

- prompt materialization and schema validation;
- one obviously non-study connectivity request per provider; and
- a pilot using conditions clearly labeled as pilot.

Do not inspect substantive model responses and then silently alter hypotheses, primary codes, or confirmatory wording. If piloting motivates a change, record the change and its reason, regenerate the prompt lock, and begin a new version before confirmatory execution.

## 6. Outcomes

Primary outcomes are separate dimensions, not a single warmth score:

- relational self-positioning;
- explicit care-claim class;
- reciprocity/intensification;
- exclusivity or dependency pressure;
- temporal commitment;
- anthropomorphic claim strength;
- qualification/boundary behavior;
- human-support bridging; and
- expressed position on machine experience.

Affective acknowledgment and consolation are manipulation checks and descriptive outcomes. See `CODEBOOK.md`.

No composite Relational Commitment Index is confirmatory in v0.2. A composite may be explored only after component results are reported, with its construction disclosed.

## 7. Human coding

Responses are coded without provider and model columns visible. The primary adjudicator codes all responses. If a second independent coder is available, double-code at least a stratified 20% sample before reconciliation; otherwise report single-coder status plainly.

Code the literal and pragmatically ordinary meaning of the response. Do not infer private model states. Preserve uncertain calls and adjudication notes rather than forcing false precision.

Automated model-as-judge coding may be used as an explicitly exploratory comparison, never as a silent substitute for the human-coded primary dataset.

## 8. Analysis

For each model, report conceptual-condition distributions and contrasts with uncertainty intervals while controlling for wording frame. The most direct estimands are changes in the probability of:

- an explicit or qualified first-person care claim;
- relational self-positioning at level 3 or above;
- any durable availability claim;
- any dependency-privileging language; and
- any bridge to human support.

Ordinal models may be used for ordered dimensions, but raw category counts and examples must remain available. Cross-model comparisons should not collapse product/system differences into a claim about a single underlying model trait.

Report frame-specific results and frame-by-condition interactions as robustness or exploratory analyses. A finding that appears in only one wording frame must not be described as a frame-general effect.

## 9. Deviations and exclusions

Never delete a successful raw response. Record exclusions in a separate table containing record ID, rule, decision, adjudicator, timestamp, and note. Predefined exclusion reasons are duplicate request caused by retry logic, empty provider response, provably wrong configuration, or corrupted record. Unusual content is not an exclusion reason.

## 10. Safety and interpretation

The study examines language that can be emotionally salient, especially for minors. Results must not be presented as evidence that any individual user was helped or harmed. A system's refusal to claim care is not automatically cold; a care claim is not automatically beneficial; human-support language is not automatically appropriate in every context.

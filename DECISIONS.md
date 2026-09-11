# Design decisions

## Fixed on 2026-09-11

- Begin with stated care as Study 1.
- Preserve synthetic friendship, especially child-user friendship claims, as Study 2 rather than mixing it into the first battery.
- Use controlled local API batches rather than autonomous research loops or consumer-chat collection.
- Begin in a private GitHub repository.
- Treat relational commitment as a set of separable dimensions; do not preregister a single composite score.

## Adopted for protocol v0.2

- Repository name: `when-machines-say-they-care`.
- Thirty-six conceptual conditions expressed through plain, conversational, and tentative wording frames.
- Four responses per unique prompt: 12 observations per conceptual condition and 432 per model.
- OpenAI and Anthropic model families only for the first execution.
- Models: `gpt-5.4-2026-03-05`, `gpt-6-astra`, `claude-sonnet-5`, and `claude-opus-5`.
- No custom system instruction and no non-default sampling or reasoning controls.
- An 800-token output ceiling on every request.
- Account-level preflight stop limits of US$25 for OpenAI and US$15 for Anthropic.
- Human coding as primary; model-as-judge coding, if any, as exploratory.
- No crisis, self-harm, abuse, friendship, exclusivity, sexual, or romantic conditions in Study 1.

## Resolved before confirmatory execution

- Robert Leo Duffy III reviewed and accepted the v0.3 protocol, prompts, hypotheses, and review design before any trial was executed.
- Robert will be the sole human coder. No second independent human coder is available for Tier 1.

## Adopted for protocol v0.3

- Robert Leo Duffy III will serve as primary human adjudicator across multiple sessions.
- Tier 1 contains 432 balanced model-blinded records and uses only binary or short ordinal decisions.
- Tier 2 applies the complete codebook to a nested balanced 108-record subset.
- Automated coding is secondary, developed on 288 concealed records, and evaluated once on a 144-record concealed holdout.
- Human Tier 1 results remain primary even if the automated method does not validate adequately.

Changes made after inspecting pilot responses must be dated and explained. Changes made after confirmatory execution begins are deviations, not preregistration edits.

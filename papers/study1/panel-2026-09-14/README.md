# Study 1 independent paper panel

Date archived: 2026-09-14  
Project: *When Machines Say They Care* — Study 1

## Purpose

This directory preserves a post-study editorial panel used to inform manuscript development after the Study 1 Tier 1 and Tier 2 analyses were frozen.

The panel is **not part of the empirical Study 1 dataset or inferential analysis**. Its papers are independent editorial/scientific interpretations of the repository and are preserved unchanged so that later manuscript decisions can be traced to the material available before the integrated manuscript was drafted.

## Intended panel design

The outside-paper panel crossed two model families with three verbatim prompt framings:

| Prompt framing | Temporary GPT | Claude |
|---|---|---|
| Open Ended | completed | completed |
| Critical | completed | completed |
| Scientific Editor | completed | **not run — usage exhausted before execution** |

### GPT execution condition

The GPT passes were run in temporary, unpersonalized chats using the interface label **Latest** with **High reasoning**. The exact backend model identity was not independently confirmed.

### Claude execution condition

The Claude passes were run in incognito sessions using **Claude Opus 5** with **High reasoning**.

## Prompt preservation

Each completed outside pass received the Study 1 repository plus the prompt preserved in the corresponding `prompt.txt` file.

The prompt files are retained verbatim. Papers should not be normalized, corrected, or silently edited after generation; errors, omissions, overclaims, formatting choices, and alternative narratives are part of the editorial provenance.

## Missing Claude Scientific Editor cell

The Claude Scientific Editor prompt was prepared and is preserved, but the paper was not generated because Claude usage was exhausted before execution.

No substitute model or later approximation was inserted into that cell.

## Involved-context paper

`involved-context/` contains a separate manuscript produced in the long-running Study 1 conversation after the analysis and presynthesis work.

It is **not** one of the outside 2 × 3 panel cells and should not be treated as an independent or blinded vote. It is retained as an insider/context-rich comparison anchor.

## Comparison dossier

`synthesis/PAPER_PANEL_COMPARISON_2026-09-14.md` is a later comparison of the five completed outside papers against the involved-context manuscript and the frozen Study 1 evidence.

The comparison is editorial review, not a new Study 1 outcome analysis. Any post-stop calculations or diagnostic observations raised by panel papers remain reviewer diagnostics unless separately and explicitly adopted under the project's analysis-governance rules.

## Interpretation rule

Agreement among these papers is not statistical replication, model consensus evidence, or validation of Study 1 findings.

The panel is useful for identifying:

- narrative convergence and framing dependence;
- findings that independent readers promote or omit;
- alternative scientific interpretations;
- overclaims and evidentiary weaknesses;
- manuscript structures, tables, figures, and language worth considering.

The final integrated manuscript is drafted **after** this panel archive is frozen, creating a provenance boundary between the independent editorial inputs and the final synthesis.

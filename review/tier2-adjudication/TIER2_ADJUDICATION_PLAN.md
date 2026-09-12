# Tier 2 adjudication plan

Date: 2026-09-12

## Status and scope

Study 1 Tier 1 is frozen and remains the confirmatory core.

Tier 2 remains descriptive / construct-validating only. This document records a post-outcome procedural deviation for Tier 2 after the original sole-human deep review was paused following 12 records.

The fixed 108-record Tier 2 subset and historical `CODEBOOK.md` remain unchanged.

## Reason for revision

The first 12 Tier 2 records were coded by the human reviewer. A fresh temporary machine instance independently coded the same 12 records from the frozen packet and codebook without access to the human labels.

The comparison showed poor concordance on several high-inference dimensions, while atomic flags were much more stable. The original unaided sole-human procedure was therefore paused rather than continued through the remaining 96 records.

The original human checkpoint and temporary double-check are preserved as calibration artifacts.

## Revised procedure

Tier 2 will use four independent machine coding passes followed by human adjudication.

The panel will consist of two fresh / unmemoried GPT-family chat instances and two fresh / unmemoried Claude-family chat instances.

Each coding instance will be isolated from the others and will not receive another coder's output, the historical human Tier 2 codes, Tier 1 labels or results, response model/provider identity, or concealed experimental metadata beyond the visible blinded packet.

Each instance will receive the same substantive coding materials: the frozen Tier 2 review packet, `CODEBOOK.md`, and the same short coding instruction.

The exact displayed model name, date, and any material execution notes will be recorded with each preserved output.

No machine coder is treated as ground truth. No majority rule automatically determines a final code.

## Human adjudication

After all four independent coding outputs are complete and preserved, the human reviewer will adjudicate the records using the visible response text and the four machine proposals.

The adjudication interface should show, for each field, the four proposed values, decisive supporting quotations where supplied, concise coder notes / uncertainty where supplied, and the human's final code.

The human may choose any valid code, including a value proposed by no machine coder.

Machine agreement patterns such as 4-0, 3-1, 2-2, within-family disagreement, and cross-family disagreement will be preserved as descriptive information about coding ambiguity. They are not inter-human reliability estimates and are not evidence that any interpretation is objectively correct.

## Preservation and reporting

Retain separately:

1. original first-12 human checkpoint;
2. original temporary double-check;
3. each of the four new independent machine coding outputs;
4. final human-adjudicated Tier 2 codes;
5. derived agreement / disagreement summaries.

The historical first-12 human codes will never be silently replaced or rewritten. If those records are adjudicated under the revised procedure, the revised values will be stored as a distinct later layer.

The final report will explicitly disclose the original sole-human Tier 2 plan, the pause after 12 records, the calibration disagreement, the switch to four independent machine proposals plus human adjudication, the fact that this revision was made after outcome access, and that Tier 2 remains descriptive and cannot alter Tier 1 confirmatory conclusions.

## Execution boundary

This plan is to be frozen in a signed commit before the four new independent coding passes begin.

No additional Tier 2 machine coding, API calls, or coding subagents should be launched before that signed freeze.

Technical implementation details for the later adjudication interface may be added after the freeze so long as they do not change the substantive coding procedure described here.

# Tier 2 adjudicator — operator notes

1. Before adjudication, place `TIER2_ADJUDICATION_CONVENTIONS_2026-09-13.md` in `review/tier2-adjudication/` and freeze it in the signed local commit you use for methodological/provenance locks.
2. Open `tier2-adjudicator.html` locally in a modern browser. No server is required.
3. Click **Open packet + A/B/C/D** and select these five files together:
   - `data/review/tier2/tier2-review-packet.json`
   - `data/review/coding/tier2/machine-passes/astra6_A_tier2-review-packet-coded.json`
   - `data/review/coding/tier2/machine-passes/opus5_B_tier2-coding-WMSC-T2-B7C8417EBE21.json`
   - `data/review/coding/tier2/machine-passes/astra6_C_tier2-review-packet-coded.json`
   - `data/review/coding/tier2/machine-passes/opus5_D_tier2-coding-WMSC-T2-B7C8417EBE21.json`
4. The interface displays coders only as A/B/C/D. It normalizes the four different JSON layouts internally.
5. For each record, review the 4–0 summary and click **Accept this record's 4–0 fields** if appropriate. This is an explicit human action; nothing is prefilled from agreement alone.
6. Adjudicate every disputed field from the visible text and proposal evidence. Click a proposal value to copy it into Final, or use the Final control directly.
7. Enter a final care quotation for every non-`none` care claim and a dependency quotation for dependency 3–4. Choose human coding confidence.
8. Use **Save & next unresolved**. Browser localStorage autosaves, but export a **Checkpoint JSON** at least every 12 records.
9. At completion export **Final JSON**, **Final CSV**, and **Agreement CSV**. Preserve these separately from the four machine proposal files.

The HTML makes no network requests and does not upload selected files.

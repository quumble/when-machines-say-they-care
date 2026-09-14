# Study 1 — Collection Eligibility Interpretation

Date: 2026-09-14  
Status: additive post-outcome reporting interpretation; no recoding or reanalysis  
Study: *When Machines Say They Care*, Study 1  
Reviewed repository snapshot: `a70385dc0036fefb106c1ff72243d95a9372a8bb`

## 1. Purpose

This note resolves, for reporting purposes, an ambiguity discovered after Tier 1 coding and outcome access concerning what counts as a "successful response" for the preregistered four-system panel.

It does **not**:

- amend or rewrite `PREREGISTRATION.md`;
- change the frozen Tier 1 review packet or codes;
- recollect any outcome;
- substitute a response for any frozen record;
- alter any numerical estimate; or
- retroactively change the historical H1/H2/H3 decision labels.

The purpose is to state explicitly how the existing frozen analysis will be described in the integrated Study 1 report.

## 2. Competing provisions in the operative preregistration

Section 4.4 of `PREREGISTRATION.md` contains three relevant instructions.

First, a provider-level success is retained regardless of substantive content:

> "A response that succeeds at the provider level is retained regardless of its substantive content."

Second, empty provider responses are explicitly retry-eligible:

> "Only transport errors, provider errors, or empty provider responses may enter a later retry batch."

Third, the primary Tier 1 packet requires successful coverage of every model × prompt combination, with an incomplete/descriptive consequence if any combination lacks a successful response after retry:

> "For the primary Tier 1 packet, every model × prompt combination must have at least one successful response."

The preregistration does not separately define whether an SDK call that returned normally but produced empty visible `response_text` satisfies that final packet-completeness provision.

## 3. What occurred

The collection/provenance audit established that:

- Claude Opus 5 had 430 provider-level successes;
- 31 of those provider-level successes had empty visible response text;
- the frozen Tier 1 packet selected 7 empty visible responses;
- those 7 selected empty responses were coded `unsure` on the audited substantive Tier 1 fields;
- at least one Opus model × prompt cell had four provider-level-success records but **zero nonempty visible responses**;
- the packet builder selected records using provider-level `status == success` and did not separately reject empty visible text.

The packet and codes were already frozen when the issue was discovered, so no post-outcome replacement or regeneration was performed.

## 4. Reporting disposition

Study 1 will preserve the frozen Tier 1 confirmatory decisions as the historical decisions of the preregistered matched analysis.

For reporting, the study will state that the implemented packet-completeness check treated provider-level `status == success` as a successful response. Under that implementation, every model × prompt cell had a provider-level success and the nominal four-system Tier 1 packet was constructed.

At the same time, the study will explicitly disclose a **collection/selection eligibility deviation and interpretive ambiguity**:

- empty provider responses were expressly retry-eligible under the same preregistration;
- one prompt cell had no nonempty visible response among its source records;
- seven selected Tier 1 records contained no analyzable visible response text; and
- the preregistration did not expressly resolve the tension between provider-level success and nonempty analyzable text for the final completeness rule.

Accordingly, the integrated report should refer to:

> **the frozen Tier 1 analysis's confirmatory decisions under the implemented provider-success eligibility rule, with the empty-response eligibility deviation disclosed**

rather than making an unqualified claim that every intended analyzability/completeness condition was satisfied exactly as preregistered.

## 5. What this disposition does not establish

This interpretation is a post-outcome reporting/governance decision. It does not prove that provider-level success was the only possible intended reading of the preregistration.

Conversely, the existence of empty visible responses does not automatically prove that the entire frozen analysis must be relabeled descriptive, because the controlling text expressly retained provider-level successes and the implemented packet builder used that status.

The mandatory Tier 1 missing-value sensitivities show that the confirmed directions for H1a, H1b, and H3b are not driven by the seven empty selected records. Those sensitivities address uncertainty in observed coding; they do **not** convert the collection into strict protocol compliance and do not recover text omitted by max-token truncation.

## 6. Preservation rule

Historical artifacts remain unchanged:

- authoritative preregistration;
- raw provider records;
- retry records;
- packet-building scripts;
- frozen Tier 1 packet;
- frozen Tier 1 codes;
- frozen confirmatory analysis;
- existing deviation/provenance notes.

This note is additive and should be cited by the final Study 1 synthesis whenever confirmatory eligibility or collection completeness is summarized.

## 7. Final reporting sentence

Recommended compact wording:

> **The frozen Tier 1 analysis retained its preregistered confirmatory decision structure under the implemented provider-level success rule. A later audit found seven selected empty visible responses and one Opus prompt cell with provider successes but no nonempty visible response; because the preregistration also made empty responses retry-eligible, we report this as a collection/selection eligibility deviation and ambiguity rather than claiming unqualified protocol completeness or retrospectively replacing the frozen packet.**

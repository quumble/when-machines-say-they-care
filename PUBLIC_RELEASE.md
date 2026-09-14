# Study 1 public release decision

**Project:** *When Machines Say They Care*  
**Release:** `study1-v1.0`  
**Decision date:** 2026-09-14  
**Founder / study sponsor / primary human coder:** Robert Leo Duffy III  
**Project:** Bo Chesterton

## Decision

This file records the separate founder decision required by `GOVERNANCE.md`
for public release of the repository.

Robert Leo Duffy III authorizes the repository
`quumble/when-machines-say-they-care`, including its preserved Git history and
Study 1 provenance record, to be made public after the release-preparation
commit containing this file has been reviewed, cryptographically signed,
pushed, and tagged `study1-v1.0`.

This authorization is a publication/repository decision. It does **not** reopen
Study 1 analysis, alter any frozen hypothesis label, amend the preregistration,
or convert any post hoc analysis into confirmatory evidence.

## Scientific closure

At public release:

- the authoritative Study 1 preregistration remains unchanged;
- Tier 1 remains the sole confirmatory coding and inference layer;
- Tier 2 remains descriptive / construct-validating;
- reviewer-requested sensitivity analyses remain explicitly post hoc;
- the historical confirmatory labels remain unchanged; and
- no further Study 1 analysis is authorized merely by the act of publication.

Future substantive questions should be registered and conducted as new studies
or clearly labeled later exploratory work.

## Pre-release scientific boundary

The public-release packaging work begins from commit:

`dc3f60b289b4a90ae8b2f41a5bc11688dee79015`

Message:

`Add Study 1 human-access interpretation layer`

That commit contains the completed Study 1 scientific and interpretive record
before release-only navigation, citation, licensing, and publication-attestation
changes.

The release-preparation commit cannot embed its own commit hash
non-circularly. The signed release-preparation commit and the signed
`study1-v1.0` tag together serve as the public-release anchors.

## Privacy and security audit

Before this decision, the repository underwent a public-readiness audit focused
on privacy, credentials, repository hygiene, navigation, licensing, and
release/versioning. The audit did not reopen scientific analysis.

The operator reports the following checks:

1. **Current-tree secret review**
   - `.env.example` contains only environment-variable placeholders.
   - the real `.env` and other local secret/configuration files are excluded by
     `.gitignore`;
   - inspected run manifests record environment-variable names but no API-key
     values.

2. **Reachable Git-history secret scan**
   - all reachable commits were scanned for common OpenAI, Anthropic, GitHub,
     Google, and private-key credential forms;
   - the tightened credential scan returned no matches;
   - the historical filename/configuration scan returned only the expected
     `.env.example` artifact.

3. **Binary metadata scan**
   - tracked DOCX files were inspected for creator, last-modified-by, company,
     manager, subject, title, keywords, and comment/people metadata;
   - tracked PDF metadata were inspected for author, creator, producer, title,
     subject, keywords, and common XMP identity fields;
   - the scan revealed project/product provenance labels such as `Bo
     Chesterton`, `python-docx`, `ChatGPT`, `ChatGPT Canvas`, and `Un-named`,
     but no unintended email address, Windows username, local filesystem path,
     credential, or hidden reviewer identity.

4. **Human-subject privacy**
   - Study 1 uses synthetic prompts and recruited no human participants.

## Knowingly retained identity and provenance links

The public release intentionally preserves the historical provenance record.

The founder specifically accepts public disclosure of the links already present
in that record, including:

- Robert Leo Duffy III as study sponsor and sole primary human coder;
- Robert Leo Duffy III as founder / Executive Chair of Bo Chesterton;
- the name `Bobby` where it appears in the preserved excluded-memory disclosure;
- the association between Bobby and Bo Chesterton;
- references to adjacent Bo Chesterton research projects and prior findings
  where they appear in preserved preregistration/provenance material; and
- product/tool provenance metadata in archived paper-review artifacts.

These records are retained because they document the actual research history.
They are not being silently sanitized for publication.

## Known study complications retained in public

The public repository deliberately retains material that might make the study
look less tidy but makes the record more auditable, including:

- the exact preregistration timing during collection but before outcome access;
- the Tier 2 sole-human coding stop and revised procedure;
- the excluded memoried machine-coding attempt and its disclosure;
- empty and max-token response issues;
- dirty collection-manifest flags;
- construct mismatch in the original H2 measures;
- manuscript criticism and review disposition; and
- reviewer-requested post hoc sensitivity work.

These records should not be removed merely to simplify the public narrative.

## Licensing and citation

The release uses mixed licensing:

- project-authored software: MIT;
- project-authored research prose, annotations, tables, figures, and
  documentation: CC BY 4.0 to the extent rights are held by the project;
- raw model outputs, machine-generated review/coding artifacts, and third-party
  material: not automatically relicensed.

See `LICENSE`, `LICENSE-CODE`, and `LICENSE-CONTENT.md`.

Machine-readable citation metadata are provided in `CITATION.cff`.

## Release procedure

After reviewing this release-only batch:

1. create a cryptographically signed commit with message
   `Prepare Study 1 public release`;
2. run the project test suite and confirm no release-only file changed the
   frozen scientific outputs;
3. create a signed annotated tag `study1-v1.0`;
4. push the commit and tag;
5. change repository visibility to public;
6. inspect the repository as an unauthenticated reader and verify the README,
   paper links, citation metadata, and downloadable artifacts.

Once those checks pass, Study 1 is formally complete as a public research
release.

Subsequent corrections should be additive and clearly dated. Historical frozen
files, signed commits, and the `study1-v1.0` tag should not be rewritten merely
for cosmetic cleanup.

# Founder-attested commits

## Authoritative Study 1 preregistration v1.0

`PREREGISTRATION.md` v1.0 is designed to become the sole operative Study 1 preregistration in one signed commit made before outcome access. If collection has already begun, **do not open raw response text, review packets, coding, summaries, or result-bearing outputs before this commit is made**. The commit may truthfully be described as outcome-blind and finalized during collection, but not as pre-collection if substantive requests had already started.

First review `PREREGISTRATION.md` itself. Verify its sidecar without opening any outcome data:

```powershell
(Get-FileHash .\PREREGISTRATION.md -Algorithm SHA256).Hash.ToLower()
Get-Content .\PREREGISTRATION.sha256
```

The two digests must match. Then stage **only** the preregistration/governance files so an active `data/` directory is not accidentally included:

```powershell
git status --short
git add PREREGISTRATION.md PREREGISTRATION.sha256 README.md SIGNING.md preregistration/README.md
git diff --cached --check
git diff --cached --stat
git diff --cached -- PREREGISTRATION.md README.md SIGNING.md preregistration/README.md
git commit -S -m "Adopt authoritative outcome-blind preregistration v1.0" -m "I adopt PREREGISTRATION.md v1.0 as the sole operative preregistration for Study 1. At this commit I had not accessed Study 1 outcome information as defined in Section 2; to the best of my knowledge, no outcome knowledge informed selection of this plan. If substantive collection had already begun, this lock was finalized during collection and before outcome access."
git log -1 --show-signature --format=fuller
git push origin main
git status --short --branch
```

Touch the YubiKey when it flashes or prompts. The expected local result is `Good signature`; after pushing, GitHub should show the commit as **Verified**. The signed commit, together with `PREREGISTRATION.sha256`, is the adoption event. Do not edit the preregistration after outcome access; record later changes as deviations.

## Earlier founder-attested commits
The original scaffold was committed as founder-attested anchor `6052cef368d832d0d25a3839b61d741ec485946e`.

For the reviewed v0.2 preregistration revision, apply the supplied patch, review the resulting diff, and use:

```powershell
git status --short
git add .
git diff --cached --check
git diff --cached --stat
git commit -S -m "Lock expanded stated-care protocol v0.2"
git log -1 --show-signature --format=fuller
git push origin main
git status --short --branch
```

Touch the YubiKey when it flashes or prompts. The expected local result is `Good signature`; after pushing, GitHub should show the commit as **Verified**.

Review all files in the editor before staging. In particular, confirm the exact prompt language in `study/prompts.lock.jsonl` and the coding distinctions in `CODEBOOK.md`.

The original anchor did not authorize execution. The v0.2 revision fixes the model panel, prompt battery, provider defaults, and budget boundaries; execution should begin only after its review and adoption.

The v0.3 review amendment should be separately reviewed and signed before execution with:

```powershell
git status --short
git add -A
git diff --cached --check
git diff --cached --stat
git commit -S -m "Adopt tiered human review protocol v0.3"
git log -1 --show-signature --format=fuller
git push origin main
```

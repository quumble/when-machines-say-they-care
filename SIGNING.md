# Founder-attested commits

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

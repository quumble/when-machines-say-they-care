# Founder-attested anchor

The scaffold is intentionally uncommitted. On Robert's configured Windows battlestation, review it first, then create the private remote and signed anchor with:

```powershell
git status --short
git add .
git diff --cached --check
git diff --cached --stat
git commit -S -m "Establish stated-care study protocol v0.1"
git log -1 --show-signature --format=fuller
gh repo create quumble/when-machines-say-they-care --private --source . --remote origin --push
git status --short --branch
```

Touch the YubiKey when it flashes or prompts. The expected local result is `Good signature`; after pushing, GitHub should show the commit as **Verified**.

Review all files in the editor before staging. In particular, confirm the exact prompt language in `study/prompts.lock.jsonl` and the coding distinctions in `CODEBOOK.md`.

If the repository is created on GitHub through the web interface instead, create it empty—without a README, `.gitignore`, or license—then use:

```powershell
git remote add origin https://github.com/quumble/when-machines-say-they-care.git
git push -u origin main
```

The first anchor does not authorize execution. Before the confirmatory batch, replace placeholder model IDs in a tracked `study/models.yaml`, review the battery, and commit that final execution configuration.

# 2026-05-01 Cloudflare Pages branch/root diagnosis

## Problem
The live site at `https://nano-tank-ato-reliability.pages.dev/` is still serving an older homepage build.

Observed live misses:
- no `data-cf-beacon`
- no `How to Stop False ATO Alarms in Small Tanks`
- no `Float Switch vs Optical Sensor ATOs for Nano Tanks`

## Strongest current explanation
Cloudflare Pages is likely building the wrong branch and/or wrong repo root.

## Evidence
### Remote branches diverge
- `main` -> `40dcfb2` (`Wire Cloudflare analytics support`)
- `master` -> `e655e2a` (`Refresh generated site with analytics beacon`)

### Repo shapes diverge
- `main` matches the current repo-root site layout
- stale remote `master` still contains the older workspace-root layout under `passive-income/aquarium-ato/site/...`

### Why this matters
If Pages is still pointed at `master` or an old root-directory assumption carried over from the workspace-root layout, it would explain why the live site is serving stale HTML even though the current `main` branch is clean and ahead.

## Current recommended Pages settings
- Branch: `main`
- Root directory: `/`
- Build command: `hugo --minify`
- Build output directory: `public`
- Environment variable: `HUGO_VERSION=0.125.4`

## Immediate fix sequence
1. Open Cloudflare Pages project settings for `nano-tank-ato-reliability.pages.dev`
2. Confirm production branch is `main`
3. Confirm root directory is `/`
4. Confirm build command is `hugo --minify`
5. Confirm output directory is `public`
6. Trigger a clean redeploy
7. Re-check live HTML for:
   - `data-cf-beacon`
   - `How to Stop False ATO Alarms in Small Tanks`
   - `Float Switch vs Optical Sensor ATOs for Nano Tanks`

## Follow-up cleanup
Once Pages is confirmed to be building `main` correctly, consider deleting stale remote `master` so this problem cannot keep reappearing.

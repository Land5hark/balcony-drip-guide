# GitHub Pages deployment runbook — balcony drip irrigation pilot

Purpose: close the current deployment-parity gap between the 16-page local cluster and the stale public GitHub Pages snapshot.

Scope: this is the safest repeatable path for getting the current local site live without mixing deployment work with affiliate activation.

## Current state snapshot
- Local repo branch: `main`
- Workflow file exists: `.github/workflows/hugo.yml`
- Public base URL in `config.toml`: `https://land5hark.github.io/balcony-drip-guide/`
- Local build already succeeds under `hugo --minify`
- Public site is still believed to expose the older 3-post snapshot

## Critical deployment gap
The local repo still has a large publish backlog in git.

### Modified tracked files
- `README.md`
- `content/posts/balcony-drip-irrigation-without-a-faucet.md`
- `content/posts/best-drip-irrigation-kits-for-balcony-container-gardens.md`
- `content/posts/how-many-drip-emitters-per-pot-container-size-chart.md`
- `data/link-registry.yaml`

### Untracked post files that appear ready for first commit
- `content/posts/adjustable-emitters-vs-button-drippers-for-container-gardens.md`
- `content/posts/best-drip-irrigation-accessories-that-actually-help-container-gardens.md`
- `content/posts/best-drip-setup-for-hanging-baskets-and-rail-planters.md`
- `content/posts/best-solar-drip-irrigation-kits-for-patios-and-balconies.md`
- `content/posts/bucket-fed-vs-solar-pump-drip-systems-for-apartment-gardeners.md`
- `content/posts/container-drip-irrigation-maintenance-checklist-for-summer.md`
- `content/posts/do-you-need-a-filter-and-pressure-reducer-for-patio-drip-kits.md`
- `content/posts/how-to-expand-a-patio-drip-kit-without-losing-pressure.md`
- `content/posts/how-to-fix-clogged-drip-emitters-in-potted-plants.md`
- `content/posts/smart-watering-timers-for-balcony-and-patio-container-gardens.md`
- `content/posts/solar-vs-faucet-timer-drip-systems-for-patio-plants.md`
- `content/posts/vacation-watering-for-container-gardens-using-drip-irrigation.md`
- `content/posts/why-your-container-drip-system-is-watering-unevenly.md`

## Preconditions (**critical**)
Do these before any push:
1. Local build passes: `hugo --minify`
2. No future-dated post is accidentally excluded from build output
3. Affiliate URLs remain blocked unless owner approvals are complete
4. The working tree only contains changes that are intended for public publication

## Preflight commands
Run from `passive-income/balcony-drip-irrigation/site`.

```bash
./scripts/deployment_preflight.py
```

Current script coverage:
- git working-tree summary
- future-dated live post detection
- `hugo --minify` build check
- built post count in `public/posts/`

Expected:
- branch should still be `main`
- Hugo build should succeed cleanly
- post count should reflect the full local cluster, not the old 3-page snapshot
- result should end with `READY FOR MANUAL REVIEW`

## Commit sequence
If the build is clean and the changed files are intentional:

```bash
git add README.md content/posts data/link-registry.yaml
git status --short
git commit -m "Publish full balcony drip content cluster"
```

### Why this commit boundary works
- captures the current post backlog
- includes the governed placeholder registry state
- keeps monetization disabled while still making the site useful publicly

## Push / deploy sequence
Pushing is owner-approval-gated because it changes the live public site.

```bash
git push origin main
```

Expected platform behavior:
- GitHub Actions should trigger `.github/workflows/hugo.yml`
- Pages artifact should build from `./public`
- deploy job should publish to the configured GitHub Pages environment

## Live verification after push (**critical**)
Check all of these before calling deployment complete:

1. Homepage loads:
   - `https://land5hark.github.io/balcony-drip-guide/`
2. Sitemap updates:
   - `https://land5hark.github.io/balcony-drip-guide/sitemap.xml`
3. At least these pages load live:
   - `/posts/best-drip-irrigation-kits-for-balcony-container-gardens/`
   - `/posts/smart-watering-timers-for-balcony-and-patio-container-gardens/`
   - `/posts/best-solar-drip-irrigation-kits-for-patios-and-balconies/`
   - `/posts/balcony-drip-irrigation-without-a-faucet/`
4. Disclosure page still loads
5. No live affiliate URLs appear unless explicitly intended

## Rollback trigger
Rollback if any of these happen:
- homepage or sitemap breaks
- multiple live post pages 404
- wrong base URL/path behavior appears
- monetized links accidentally go live
- GitHub Pages deploy succeeds but renders the wrong content set

## Rollback path
Fastest rollback is to revert the deployment commit and push again.

```bash
git log --oneline -n 3
git revert <bad_commit_sha>
git push origin main
```

If the issue is only one bad content file, prefer a targeted fix commit over a broad panic rollback.

## Known risks
- **Mixed-intent working tree**: deployment could accidentally include half-finished local edits if preflight is skipped.
- **False confidence from local build**: local success does not guarantee live Pages parity; sitemap/page checks are mandatory.
- **Future-dated content**: Hugo can silently omit posts from `public/` if timestamps drift forward.
- **Monetization drift**: link-registry changes must not be mistaken for approval to insert affiliate URLs.

## Minimal owner handoff
When Sharky is ready to make the public site catch up, the decision needed is simple:
- approve pushing the current non-monetized 16-page cluster to `origin/main`

That push can happen independently of affiliate activation.

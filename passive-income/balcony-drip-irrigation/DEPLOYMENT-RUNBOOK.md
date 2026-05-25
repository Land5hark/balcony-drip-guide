# Deployment Runbook — Balcony Drip Guide

## Live Site
- **URL**: https://balcony-drip-guide.pages.dev
- **Platform**: Cloudflare Pages
- **Source**: GitHub → `Land5hark/balcony-drip-guide`

## Repository Structure

The repository has two branches with different purposes:

### `master` branch (ACTIVE — this is the live site)
- **Purpose**: Pre-built Hugo site with committed `public/` directory
- **Layout**: Complex design with category cards, SVG illustrations, newsletter CTA, "start here" path
- **Config**: `title = "The Balcony Drip"`, `baseURL = "https://balcony-drip-guide.pages.dev"`
- **Key files**:
  - `config.toml` — Hugo configuration with explicit category counts
  - `layouts/partials/categories.html` — category card partial
  - `public/` — pre-built static files (committed to repo)
  - `content/posts/` — 36 articles
  - `data/link-registry.yaml` — 61 affiliate link slots
- **No `.gitignore`** — `public/` is intentionally committed
- **Has `.github/workflows/`** — `deploy-cloudflare-pages.yml` using wrangler direct deploy
  - This is the NEW primary deployment path (added 2026-05-23)
  - Requires `CLOUDFLARE_API_TOKEN` GitHub secret — see Owner Action Blockers

### `main` branch (LEGACY / DIFFERENT SITE)
- **Purpose**: Simple Hugo site with GitHub Actions deploying to GitHub Pages
- **Layout**: Basic cards, no category illustrations, no newsletter CTA
- **Config**: `title = "Balcony Drip Guide"`
- **Has `.gitignore`** excluding `public/`
- **Has `.github/workflows/hugo.yml`** deploying to GitHub Pages
- **NOT the live site** — the live site serves from `master`

## Deployment Architecture (Updated 2026-05-23)

There are now **two deployment paths**:

### Path A: GitHub Actions → Wrangler Direct Deploy (NEW PRIMARY)
- **File**: `.github/workflows/deploy-cloudflare-pages.yml`
- **How it works**: On every push to `master`, GitHub Actions builds with Hugo 0.68.3 and deploys `public/` directly to Cloudflare Pages using the wrangler CLI.
- **Status**: Active and triggering, but **failing** due to missing `CLOUDFLARE_API_TOKEN` secret.
- **Error**: `In a non-interactive environment, it's necessary to set a CLOUDFLARE_API_TOKEN`
- **Advantage**: Bypasses the broken Cloudflare Pages GitHub integration entirely.

### Path B: Cloudflare Pages GitHub Integration (LEGACY — BROKEN)
- **How it worked**: Cloudflare Pages pulled from GitHub and built automatically.
- **Status**: Stopped working around 2026-05-21. Pushes to `master` do not propagate.
- **Evidence**: Live site still shows stale category counts (1/0/0/0/0) and minimal robots.txt despite fresh commits.

## Emergency Fix: Cloudflare Pages Not Propagating (2026-05-21)

### Owner Dashboard Checklist (2026-05-23)

Use this when logged into Cloudflare. The local repo and GitHub source have already been checked; the remaining failure is inside Cloudflare Pages.

1. Open **Cloudflare Dashboard → Workers & Pages → Pages → `balcony-drip-guide`**.
2. Open **Deployments** and inspect the newest production deployment.
3. Confirm the newest deployment is from:
   - Repository: `Land5hark/balcony-drip-guide`
   - Branch: `master`
   - Commit: `8d1c0cc` or newer
4. If the newest production deployment is not `master`, fix **Settings → Builds & deployments → Production branch** to `master`.
5. Confirm build settings:
   - Build command: `hugo --minify`
   - Build output directory: `public`
   - Root directory: `/`
6. If the latest `master` deployment is missing, failed, or older than the GitHub commit, click **Retry deployment** or **Create deployment** from the latest `master` commit.
7. If Cloudflare reports a Hugo version/build failure, set the Pages environment variable `HUGO_VERSION` to the local tested version or switch the build command to a static copy path that serves committed `public/`.
8. After the deployment finishes, verify from a terminal:

```bash
cd /home/linuxlite/.openclaw/workspace/passive-income/balcony-drip-irrigation
./scripts/verify-deployment.sh
```

Current stale-build evidence from 2026-05-23 08:01 EDT:

- Expected category counts: `6, 19, 13, 1, 0`
- Live category counts: `1, 0, 0, 0, 0`
- Expected build fingerprint: `local | local-buil | 2026-05-23T08:20:01Z`
- Live build fingerprint: missing
- Live hot-weather article: passes with HTTP 200, meaning Cloudflare has partial/newer content but not the corrected homepage shell
- `robots.txt`: still failing freshness check

Do not send promotion traffic until `./scripts/verify-deployment.sh` reports `deployment_status: fresh` in `reports/balcony-drip-deployment-status.json`.

## Deployment Configuration (Required)

### Cloudflare Pages Settings
When (re)connecting the project, use these exact settings:

| Setting | Value |
|---------|-------|
| Build command | `hugo --minify` (or leave empty if serving committed `public/`) |
| Build output directory | `public` |
| Root directory | `/` |
| Branch | `master` |

**Important**: If Cloudflare Pages detects `config.toml` and runs Hugo automatically, the build will use the committed `public/` directory ONLY if the build command is explicitly set to use it. Otherwise, Cloudflare Pages may rebuild from source using its own Hugo version.

### Known Build Environment Quirks
- **Hugo runtime counting is NOT portable**: Both `site.GetPage` (taxonomy) and `where site.RegularPages "Section" "posts"` (section) counting methods work locally (Hugo v0.68.3) but produce incorrect counts on Cloudflare Pages builds.
- **Solution**: Use explicit `count` fields in `[[params.categories]]` in `config.toml`. The partial reads `.count` directly. No runtime counting.
- **robots.txt**: The committed `public/robots.txt` has full content (Allow directive + Sitemap). If the live site shows only `User-agent: *`, the build is stale.

## Deployment Verification Checklist

Before any push to `master`, run local build QA:

```bash
cd /home/linuxlite/.openclaw/workspace/passive-income/balcony-drip-irrigation/site-deploy
hugo --minify
python3 scripts/qa_static_build.py
```

Expected:

- Missing internal targets: `0`
- Sitemap duplicate URLs: `0`

After any push to `master`, verify within 5 minutes:

```bash
# Check category counts
curl -s https://balcony-drip-guide.pages.dev | grep -o "cat-card__count>[0-9]* articles" | head -5
# Expected: 6, 19, 13, 1, 0

# Check robots.txt
curl -s https://balcony-drip-guide.pages.dev/robots.txt | head -3
# Expected: Updated 2026-05-21, Allow: /, Sitemap: ...

# Check title
curl -s https://balcony-drip-guide.pages.dev | grep -o "<title>.*</title>" | head -1
# Expected: The Balcony Drip — Honest, tested writing...
```

If counts are wrong or robots.txt is stale, the Cloudflare Pages build has not propagated. Check the Cloudflare dashboard Build tab.

## History of Deployment Issues

### 2026-05-18: Initial Deployment
- Claimed category count fix deployed. Actually deployed section-based counting that failed on Cloudflare Pages.
- Lesson: Always verify live site after deploy; don't trust deployment summaries.

### 2026-05-21 04:15: Category Count Bug Discovered
- Live site showing 1/0/0/0/0 instead of 6/19/13/1/0.
- Applied taxonomy-based fix (`site.GetPage`). Pushed commit f788b71.
- Did NOT propagate to live site.

### 2026-05-21 06:15: Final Fix Applied
- Discovered that ALL Hugo runtime counting fails on Cloudflare Pages.
- Moved counts to explicit config params. Pushed commit 93b1b8c.
- **Status**: Awaiting propagation verification.

## Affiliate Status

| Program | Status | Commission | Slots | Files |
|---------|--------|------------|-------|-------|
| Drip Depot | Active | 10% | 46 | `data/link-registry.yaml` |
| RainPoint | Active | 5% | 15 | `data/link-registry.yaml` |

## Owner Action Blockers

1. **Cloudflare API token for GitHub Actions** (HIGHEST PRIORITY):
   - Go to https://dash.cloudflare.com/profile/api-tokens
   - Create token with: Zone:Read + Cloudflare Pages:Edit
   - Go to GitHub repo → Settings → Secrets → Actions
   - Add repository secret named exactly: `CLOUDFLARE_API_TOKEN`
   - Once added, the next push to `master` will deploy correctly via Path A.

2. **Cloudflare Analytics token**: Add to `config.toml` `[params.cloudflare_analytics]` to enable privacy-friendly analytics

3. **Pinterest business account**: Required to execute Phase 1 promotion

4. **Cloudflare Pages dashboard access**: May be needed as fallback if Path A also fails

## Emergency: If Auto-Deploy Breaks

1. Verify GitHub push succeeded: `git log origin/master --oneline -3`
2. Check GitHub Actions tab for workflow failures (likely missing `CLOUDFLARE_API_TOKEN`)
3. If Path A (GitHub Actions) is failing, add the API token secret first
4. If Path A still fails after adding the token, check Cloudflare Pages dashboard → Build tab
5. Try manual rebuild from dashboard
6. If all else fails, download `public/` from latest commit and upload manually to Cloudflare Pages

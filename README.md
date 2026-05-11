# Balcony Drip Irrigation Hugo Site

## Deployment target
**Cloudflare Pages** (standard for all passive-income niche sites)

## Why this stack (standard)
- **Hugo**: Static site generator, fast builds, markdown-native
- **Cloudflare Pages**: Clean `*.pages.dev` URLs, free, fast CDN, simple GitHub integration
- **GitHub**: Source control + automatic deploys on push to main
- This is the standard passive-income site architecture. Use it for all future niches.

## Local build
```bash
hugo --minify
```

## Deployment preflight
Before any public push, run:
```bash
./scripts/deployment_preflight.py
```

It checks:
- git working-tree state
- future-dated live posts that Hugo would silently skip
- local Hugo build health
- built post count in `public/posts/`

## Content workflow
1. Draft or refine source content in `../drafts/`
2. Promote approved content into `content/posts/`
3. Keep `verification_status` honest
4. Track governed product destinations in `data/link-registry.yaml`
5. Add affiliate URLs only after owner approval and account setup
6. Run a local Hugo build before any deploy

## Required editorial fields
Each post should include:
- `categories`
- `tags`
- `intent`
- `cluster`
- `verification_status`
- `affiliate_ready`
- `show_disclosure`

## Cloudflare Pages setup (one-time)
1. Go to [Cloudflare Pages dashboard](https://dash.cloudflare.com/pages)
2. Create project → Connect to GitHub → Select this repo
3. Framework preset: **Hugo**
4. Build command: `hugo --minify`
5. Build output: `public`
6. Root directory: `/`
7. Environment variable: `HUGO_VERSION=0.125.4`
8. Save & deploy

## Current state
- **Live URL:** https://land5hark.github.io/balcony-drip-guide/ (GitHub Pages)
- **Target URL:** https://balcony-drip-guide.pages.dev/ (Cloudflare Pages - pending setup)
- **26 articles** published and live (deployed 2026-05-11)
- **177 total pages** including hub pages, trust pages, taxonomy pages
- Affiliate placeholders mapped but not yet monetized (waiting on account approvals)
- Trust pages live: About, Privacy, Disclosure, Search
- **Promotion assets:** 3 Pinterest pins generated and committed to `static/promotion/`

## Blockers
- **Drip Depot affiliate approval:** Requires owner identity/tax info (see AFFILIATE-STATUS.md in workspace)
- **Cloudflare Pages migration:** Requires dashboard access to connect repo
- **Workspace repo archived:** Passive-income workspace repo is read-only; site repo (`balcony-drip-guide`) remains active

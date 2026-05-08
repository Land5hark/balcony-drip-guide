# Balcony Drip Irrigation Hugo Site

## Recommended deployment target
Primary: **Cloudflare Pages**
Fallback: **GitHub Pages**

## Why this stack
- Hugo is installed locally and already used in the broader passive-income workspace.
- Markdown-first content keeps the draft-to-site flow boring and repeatable.
- This pilot can publish safely before affiliate monetization is activated.

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

## Current state
- Public site target remains GitHub Pages at `https://land5hark.github.io/balcony-drip-guide/`.
- Core trust pages are live: About, Privacy Policy, Affiliate Disclosure, and Search.
- Local workspace now has a **16-post built cluster**: `topics.csv` shows `16` topics marked `live`, and local `site/public/posts/` contains `16` post pages.
- Public GitHub Pages is currently **behind local state** and still exposes only the older 3-post snapshot in the live sitemap; deployment parity is the immediate operational gap.
- Governed placeholder coverage is complete across the local commercial cluster, but monetized link insertion is still intentionally blocked on owner affiliate approvals and final URL insertion.
- Highest-priority editorial hardening is fact review on the commercial hub pages before wider promotion.
- Publishing gotcha logged: future-dated Hugo content will silently stay out of `public/` until its publish time passes, so article promotion should use current-or-earlier timestamps.

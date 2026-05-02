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
- Article 1 implemented as a publishable non-monetized pilot page.
- Monetized link insertion is intentionally blocked on owner affiliate approvals.
- No live deployment has been performed from this run.

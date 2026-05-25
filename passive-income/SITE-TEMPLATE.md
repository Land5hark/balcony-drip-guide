# Passive Income Niche Site Template

Standard architecture for all micro-niche affiliate content sites.

---

## Stack (Non-Negotiable)

| Layer | Tool | Why |
|-------|------|-----|
| **Static Site** | Hugo | Fast builds, markdown-native, boring |
| **Hosting** | Cloudflare Pages | Clean `*.pages.dev` URLs, free CDN, GitHub integration |
| **Source Control** | GitHub | Auto-deploy on push, version control |
| **Content** | Markdown + Frontmatter | Portable, future-proof, git-friendly |
| **Monetization** | Governed placeholders | Editorial first, affiliate second |

---

## Directory Structure

```
passive-income/{niche-name}/
├── affiliate-programs.csv          # Merchant research & scoring
├── topics.csv                      # Content cluster map
├── findquestions-seed-queries.txt  # Keyword research inputs
├── drafts/                         # Source content packages
│   ├── {article-slug}.md
│   └── {article-slug}.verify.md
├── reports/                        # Research & decision logs
├── site/                          # Hugo site (this is what deploys)
│   ├── archetypes/
│   ├── config.toml                # BaseURL ends in .pages.dev
│   ├── content/
│   │   └── posts/                 # Live articles only
│   ├── data/
│   │   └── link-registry.yaml     # Governed affiliate placeholders
│   ├── layouts/
│   ├── static/
│   ├── scripts/
│   │   └── deployment_preflight.py
│   └── README.md                  # Cloudflare Pages setup guide
└── README.md                      # Niche-level overview
```

---

## Hugo Config Template

```toml
baseURL = "https://{niche-name}.pages.dev/"
languageCode = "en-us"
title = "{Niche Title}"
enableRobotsTXT = true

[params]
  description = "{One-line niche description}"
  site_url = "https://{niche-name}.pages.dev/"
  default_og_image = "/assets/logo.png"
  cloudflare_analytics_token = ""  # Add after Cloudflare setup
  disclosure = "Some pages include affiliate links. Recommendations based on fit, tradeoffs, and real use — not hype."
  verification_label = "Verification status"
  verification_warning = "Verify product facts before external promotion."
  disclosure_page = "/affiliate-disclosure/"

[taxonomies]
  category = "categories"
  tag = "tags"

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
```

---

## Required Frontmatter Fields

Every post must include:

```yaml
---
title = "Article Title"
date = 2026-05-08T12:00:00-04:00
draft = false
description = "SEO meta description"
slug = "url-friendly-slug"
categories = ["buying-guides"]
tags = ["tag1", "tag2"]
intent = "buyer"           # buyer | problem-aware | comparison | maintenance
cluster = "cluster-name"
verification_status = "verified"  # needs-fact-check | verified | stale
affiliate_ready = false    # true only after links inserted
show_disclosure = true
---
```

---

## Cloudflare Pages Setup Checklist

- [ ] Create GitHub repo: `{niche-name}` under Land5hark
- [ ] Push Hugo site to repo
- [ ] Go to [Cloudflare Pages](https://dash.cloudflare.com/pages)
- [ ] Create project → Connect to GitHub → Select repo
- [ ] Framework preset: **Hugo**
- [ ] Build command: `hugo --minify`
- [ ] Build output: `public`
- [ ] Root directory: `/`
- [ ] Environment variable: `HUGO_VERSION=0.125.4`
- [ ] Save & deploy
- [ ] Copy Cloudflare Analytics token → paste into `config.toml`
- [ ] Test live URL

---

## Content Workflow

1. **Validate** topic opportunity (search intent, SERP weakness, monetization fit)
2. **Draft** article in `drafts/{slug}.md` with verify notes
3. **Fact-check** claims, product specs, availability
4. **Promote** to `site/content/posts/{slug}.md`
5. **Build** locally: `hugo --minify`
6. **Preflight**: `./scripts/deployment_preflight.py`
7. **Commit & push**: Auto-deploys to Cloudflare Pages
8. **Monetize** (after affiliate approval): Insert tracked links into `link-registry.yaml`

---

## Affiliate Governance

- All commercial links go through `data/link-registry.yaml`
- Use placeholder slots like: `{niche}-{merchant}-{product}-{role}`
- Editorial content ships with `affiliate_ready = false`
- Only flip to `affiliate_ready = true` after:
  - Account approved
  - Tax/business info submitted
  - Tracked URLs generated
  - Links tested

---

## Naming Conventions

| Element | Pattern | Example |
|---------|---------|---------|
| Repo | `{niche-concept}` | `balcony-drip-guide` |
| URL | `{niche}.pages.dev` | `balcony-drip-guide.pages.dev` |
| Slug | `kebab-case` | `best-drip-kits-balcony` |
| Slot ID | `{niche}-{merchant}-{product}-{role}` | `bdi-dripdepot-kit-primary` |

---

## Quality Gates

Before any public push:

- [ ] Hugo builds clean (`hugo --minify`)
- [ ] Preflight passes (`./scripts/deployment_preflight.py`)
- [ ] No future-dated posts blocking publish
- [ ] Trust pages exist (About, Privacy, Disclosure)
- [ ] At least 5 articles in cluster
- [ ] Internal linking map drafted

---

## Affiliate Status Tracking

Create `AFFILIATE-STATUS.md` to track approval pipeline:

```markdown
# Affiliate Program Status

## Approved & Active
- Merchant: [Name]
- Commission: X%
- Active Links: N

## Pending Owner Action
- Merchant: [Name]
- Portal: [URL]
- Blocked Links: N
- Why blocked: [identity/tax/payment required]
```

---

## Lessons Learned (Balcony Drip Pilot)

1. **RainPoint** approved faster than Drip Depot (UpPromote vs direct application)
2. Direct-brand programs often have better commissions but slower approval
3. Having 16+ articles live helped with affiliate applications
4. Primary merchant (Drip Depot, 10%) matters more than secondary (RainPoint, 5%)
5. Link registry pattern works well for governance

---

## Standard Operating Principle

> **Ship unmonetized before waiting for approvals.**

A live site with editorial content gets you:
- Real URLs for affiliate applications
- Indexing time with Google
- User feedback and refinement time
- Proof of execution

Affiliate links are the last step, not the first.

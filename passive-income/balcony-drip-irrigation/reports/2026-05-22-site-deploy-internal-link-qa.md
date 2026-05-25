# Site Deploy Internal Link QA - 2026-05-22

## Result

Fixed repeated broken internal links in the active `site-deploy` Hugo source and regenerated the local build.

## Initial Audit

Local public HTML audit:

- HTML files checked: 223
- Internal links checked: 5,502
- Missing internal targets: 895

Most misses came from shared templates and config, not individual articles:

- Header search link pointed at missing `/search/`
- Homepage archive links pointed at missing `/all/`
- Homepage start-here cards pointed at missing legacy paths
- Footer linked missing `/glossary/`, `/calculator/`, `/contact/`, `/methodology/`, and `/reader-notes/`
- Article template linked missing `/methodology/`
- Affiliate disclosure notes linked missing `/affiliate-disclosure/`
- Self-watering setup guide linked missing `/troubleshooting/regulator-mistake/`

## Fixes

Updated `site-deploy` source:

- Header search icon now points to `/posts/`
- Homepage archive CTAs now point to `/posts/`
- Footer resources now use existing pages: `/posts/`, `/setup-guides/`, newsletter, RSS
- Footer about links now use existing `/about/` and `/disclosure/`
- Article footer "How we test" now points to `/about/`
- Start-here cards now point to generated article URLs
- Affiliate disclosure notes now point to `/disclosure/`
- Self-watering setup pressure-regulator reference now points to the existing pressure reducer guide

## Verification

Ran `hugo --minify` in `site-deploy` successfully.

Build output:

- Pages: 214
- Paginator pages: 13
- Aliases: 84
- Sitemaps: 1

Post-fix local public HTML audit:

- HTML files checked: 223
- Internal links checked: 5,085
- Missing internal targets: 0

## Deployment Note

This is local source/build preparation only. No external push was performed.

## Reusable QA Script

Added `site-deploy/scripts/qa_static_build.py` so future checks can run the same internal-link and sitemap duplicate audit without retyping an inline script.

Verification:

```text
HTML files: 223
Internal links checked: 5078
Missing internal targets: 0
Sitemap URLs: 126
Sitemap unique URLs: 126
Sitemap duplicate URLs: 0
```

The script exits non-zero if any internal target is missing, the sitemap is missing, or sitemap URLs are duplicated.

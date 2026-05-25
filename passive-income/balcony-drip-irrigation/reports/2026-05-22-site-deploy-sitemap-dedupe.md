# Site Deploy Sitemap Dedupe - 2026-05-22

## Result

Removed a duplicate sitemap canonical URL from the local `site-deploy` build.

## Issue

Two source files published the same slug:

- `content/posts/balcony-watering-systems.md`
- `content/posts/balcony-watering-systems-hub.md`

Both emitted:

- `https://balcony-drip-guide.pages.dev/posts/balcony-watering-systems/`

Pre-fix sitemap audit:

- Total sitemap URLs: 127
- Unique sitemap URLs: 126
- Duplicate URLs: 1

## Fix

Set `draft = true` in `content/posts/balcony-watering-systems-hub.md`, keeping `content/posts/balcony-watering-systems.md` as the canonical live hub.

## Verification

Ran `hugo --minify` in `site-deploy` successfully.

Build output:

- Pages: 213
- Paginator pages: 13
- Aliases: 84
- Sitemaps: 1

Post-fix QA:

- HTML files checked: 223
- Internal links checked: 5,078
- Missing internal targets: 0
- Sitemap total URLs: 126
- Sitemap unique URLs: 126
- Sitemap duplicate URLs: 0

## Deployment Note

This is local source/build preparation only. No external push was performed.

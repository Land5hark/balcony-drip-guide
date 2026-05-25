# Hub Sitemap Dedupe

Date: 2026-05-19

## Change

- Found two published source files using `slug = "balcony-watering-systems"`.
- Kept `site/content/posts/balcony-watering-systems-hub.md` published as the fuller canonical hub.
- Marked `site/content/posts/balcony-watering-systems.md` as `draft = true` to remove the duplicate URL from generated output without deleting source content.

## Verification

- Ran `hugo --minify` in `site/`.
- Build passed: 209 pages, 1 sitemap.
- Confirmed sitemap now contains:
  - `https://balcony-drip-guide.pages.dev/posts/balcony-watering-systems/` exactly once.
  - `https://balcony-drip-guide.pages.dev/posts/balcony-watering-systems-complete-guide/` exactly once.

## Why It Matters

Promotion assets point at hub URLs. Removing duplicate sitemap entries keeps the site cleaner before traffic promotion and avoids confusing crawlers with two source files competing for the same published path.

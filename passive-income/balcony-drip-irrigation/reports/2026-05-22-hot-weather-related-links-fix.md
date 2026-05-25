# Hot Weather Guide Related Links Fix - 2026-05-22

## Result

Fixed the related-guide URLs in the hot-weather balcony drip article so they match the site's actual Hugo permalink structure.

## Files Updated

- `drafts/how-to-adjust-balcony-drip-irrigation-for-hot-weather.md`
- `site-deploy/content/posts/how-to-adjust-balcony-drip-irrigation-for-hot-weather.md`

## Issue

The article linked to category-style paths that are not generated for `content/posts` articles in the active deploy workspace:

- `/buying-guides/best-hose-timers-for-balcony-drip-irrigation/`
- `/troubleshooting/how-often-should-you-water-balcony-plants/`
- `/comparisons/adjustable-emitters-vs-button-drippers-for-container-gardens/`
- `/buying-guides/diy-balcony-watering-system-for-renters/`

Those were changed to the generated post paths:

- `/posts/best-hose-timers-for-balcony-drip-irrigation/`
- `/posts/how-often-should-you-water-balcony-plants/`
- `/posts/adjustable-emitters-vs-button-drippers-for-container-gardens/`
- `/posts/diy-balcony-watering-system-for-renters/`

## Verification

- Ran `hugo --minify` in `site-deploy` successfully.
- Build output: 214 pages, 13 paginator pages, 84 aliases, 1 sitemap.
- Confirmed all four target local public files exist.
- Confirmed no old category-style related URLs remain in the article source or generated article HTML.

## Deployment Note

This is local source/build preparation only. No external push was performed.

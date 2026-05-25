# Live Promotion Preflight - 2026-05-24

Purpose: verify whether the refreshed high-priority pages are live enough to promote, and whether the corrected robots file has reached Cloudflare Pages.

Checked at: 2026-05-24 08:03 EDT.

## Result

- P1 promotion pages on `https://balcony-drip-guide.pages.dev` are reachable and show refreshed May 2026 content.
- `https://balcony-drip-guide.pages.dev/robots.txt` is still stale and returns only `User-agent: *`.
- Local generated output is correct: `site-deploy/public/robots.txt` includes `Allow: /` and `Sitemap: https://balcony-drip-guide.pages.dev/sitemap.xml`.
- This confirms the promotion queue can use live article URLs, but the robots fix is still blocked by Cloudflare deployment state rather than local Hugo output.

## Live P1 Page Checks

| URL path | HTTP / size | Live title | Live freshness signal |
|---|---:|---|---|
| `/posts/balcony-watering-systems/` | `200 / 19915` | Balcony Watering Systems: A Complete Guide for Container Gardens | Last updated May 2026 |
| `/posts/what-are-common-problems-with-drip-irrigation-systems/` | `200 / 25265` | What Are Common Problems With Drip Irrigation Systems? | Last updated May 2026 |
| `/posts/how-often-should-you-water-balcony-plants/` | `200 / 27814` | How Often Should You Water Balcony Plants? A Season-by-Season Guide | Last updated May 2026 |
| `/posts/diy-balcony-watering-system-for-renters/` | `200 / 27274` | DIY Balcony Watering System for Renters | Last updated May 2026 |
| `/posts/best-drip-irrigation-kits-for-apartment-balconies/` | `200 / 24214` | Best Drip Irrigation Kits for Apartment Balconies | Last updated May 2026 |
| `/posts/how-to-fix-clogged-drip-emitters-in-potted-plants/` | `200 / 27961` | How to Fix Clogged Drip Emitters in Potted Plants | Last updated May 2026 |
| `/posts/how-to-prevent-overwatering-with-automatic-systems/` | `200 / 28616` | How to Prevent Overwatering With Automatic Systems | Last updated May 2026 |

## Next Action

When owner-gated posting accounts are available, the P1 article URLs are viable for promotion. Keep the robots item in the deployment blocker list until Cloudflare serves the static robots file with the sitemap directive.

# Cloudflare Analytics Preflight - 2026-05-20

## Result

Cloudflare Web Analytics integration is template-ready. No code change is needed before Sharky adds the owner-only token.

## Verified

- `site/layouts/partials/cloudflare-analytics.html` emits the Cloudflare beacon only when both `params.cloudflare_analytics.enabled` and `params.cloudflare_analytics.token` are set.
- `site/layouts/partials/head.html` includes the analytics partial, so the beacon will be present on every generated page once enabled.
- `site/config.toml` keeps analytics disabled with an empty token, which is correct until the Cloudflare token is provided.
- `hugo --minify` builds cleanly: 210 pages, 13 paginator pages, 82 aliases, 1 sitemap.
- Sitemap verified live with 131 URLs (2026-05-21 06:27 UTC).

## Remaining Blockers

1. **Cloudflare Analytics token** — Owner action required: add the Cloudflare Web Analytics token to `site/config.toml` and set `enabled = true`.

2. **robots.txt CDN cache** — Fix committed and pushed (commit `77ba901` with timestamp comment to force new SHA), but GitHub status shows build still `pending`. CDN may take additional time to clear after build completes.

## Follow-Up After Token

1. Rebuild with `hugo --minify`.
2. Confirm generated HTML includes `static.cloudflareinsights.com/beacon.min.js`.
3. Deploy.
4. Verify a 200 response from the Cloudflare beacon in browser DevTools.

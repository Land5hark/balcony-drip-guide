- Lane: passive-income / comparison-page refresh
- Status: pass completed
- Page: `site/content/posts/bucket-fed-vs-solar-pump-drip-systems-for-apartment-gardeners.md`
- Scope: tighten path selection and cluster handoffs for the bucket-vs-solar comparison page without changing governed-link policy
- Timestamp: 2026-05-06 08:50 EDT

## What changed
1. Expanded the `Fast starting point` table with an explicit troubleshooting branch for readers whose current setup already waters unevenly, so they do not confuse layout failure with system-family choice.
2. Expanded the `Related articles` block so the page now routes more cleanly into the core balcony-kit buyer hub and the uneven-watering troubleshooting guide.

## Why this mattered
The page already framed the bucket-vs-solar decision well, but it still assumed some readers were definitely making a category choice when a chunk of them are really trying to diagnose a sloppy existing layout.

This pass makes the page more useful by:
- reducing false system-switching when the real problem is distribution
- improving cluster flow back into the broader buyer hub
- tightening comparison-page handoffs into troubleshooting

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

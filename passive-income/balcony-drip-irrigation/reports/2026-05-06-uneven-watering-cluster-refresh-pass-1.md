- Lane: passive-income / troubleshooting-page refresh
- Status: pass completed
- Page: `site/content/posts/why-your-container-drip-system-is-watering-unevenly.md`
- Scope: tighten diagnosis routing and cluster handoffs for the uneven-watering guide without changing governed-link policy
- Timestamp: 2026-05-06 10:50 EDT

## What changed
1. Added a top-of-page `Fast starting point` table so readers can route themselves faster by real failure mode: clogged emitters, overexpansion, emitter-coverage mistakes, hanging-basket edge cases, or hot-weather maintenance drift.
2. Expanded the `Related articles` block so the page now routes directly back into the core buyer hub as well as the surrounding troubleshooting and layout guides.

## Why this mattered
The page already had the right troubleshooting spine, but it still made readers read too far before finding the branch that matched their actual mess.

This pass makes the page more useful by:
- speeding up diagnosis instead of timer-fiddling
- improving cluster flow between symptom pages and root-cause pages
- giving broader buyer-hub reentry when the real problem is a mismatched base setup

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

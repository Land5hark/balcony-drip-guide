- Lane: passive-income / problem-aware page refresh
- Status: pass completed
- Page: `site/content/posts/balcony-drip-irrigation-without-a-faucet.md`
- Scope: tighten path selection and cluster handoffs for the no-faucet guide without changing governed-link policy
- Timestamp: 2026-05-06 07:00 EDT

## What changed
1. Expanded the `Fast starting-point table` with two higher-intent branches: trip coverage without hose access and side-by-side reservoir branch comparison.
2. Expanded the `Related articles` block so the page now routes more cleanly into the core buyer hub and the uneven-watering troubleshooting guide, instead of staying boxed into only no-faucet-adjacent reads.

## Why this mattered
The page already did a solid job explaining the no-faucet constraint, but it still made some readers do extra work to find the next guide matching their real problem.

This pass makes the page more useful by:
- routing travel-planning readers faster
- clarifying when the next step is category comparison rather than rereading setup basics
- improving cluster handoffs back into core buyer and troubleshooting pages

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

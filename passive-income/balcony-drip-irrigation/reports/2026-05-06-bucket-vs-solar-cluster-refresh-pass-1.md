- Lane: passive-income / comparison-page refresh
- Status: pass completed
- Page: `site/content/posts/bucket-fed-vs-solar-pump-drip-systems-for-apartment-gardeners.md`
- Scope: improve intent routing and cluster handoffs for the bucket-fed vs solar comparison page without changing governed-link policy
- Timestamp: 2026-05-06 02:30 EDT

## What changed
1. Added a top-of-page `Fast starting point` table so readers can route themselves faster by actual constraint: broad no-faucet setup choice, weak-sun uncertainty, vacation reliability, expansion weirdness, or simpler reservoir-first logic.
2. Added a stronger internal-link handoff in the simplicity section to the smart-timer guide so timer logic is framed as a separate downstream decision rather than mixed into the system-family comparison.
3. Expanded the `Related articles` block so the page now hands traffic more cleanly into no-faucet, solar, timer, vacation, and expansion follow-up guides.

## Why this mattered
The comparison page already had the right core verdict, but it still made readers scan too far before realizing which adjacent guide matched their actual problem.

This pass makes the page more useful earlier:
- faster self-sorting by real constraint
- cleaner cluster flow into adjacent buyer and troubleshooting pages
- less chance that readers confuse system-family choice with timer-feature choice

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

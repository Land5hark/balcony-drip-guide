- Lane: passive-income / comparison-page refresh
- Status: pass completed
- Page: `site/content/posts/solar-vs-faucet-timer-drip-systems-for-patio-plants.md`
- Scope: improve intent routing and cluster handoffs for the solar-vs-faucet comparison page without changing governed-link policy
- Timestamp: 2026-05-06 05:00 EDT

## What changed
1. Added a top-of-page `Fast starting point` table so readers can route themselves faster by real constraint: no-faucet setup uncertainty, solar-specific buying questions, faucet-timer shopping, vacation reliability, or expansion issues.
2. Tightened the comparison framing so timer buying guidance is routed explicitly into the dedicated smart-timer guide instead of staying muddled inside the system-family comparison.
3. Expanded the `Related reads` block so the page now hands traffic more cleanly into no-faucet, solar-kit, bucket-vs-solar, timer, vacation, expansion, and troubleshooting follow-ups.

## Why this mattered
The page already had the right core verdict, but it still made readers read too far before realizing which adjacent guide matched the actual constraint they were wrestling with.

This pass makes the page more useful earlier:
- faster self-sorting by physical setup reality
- cleaner cluster flow into adjacent buyer and troubleshooting pages
- less confusion between faucet-access decisions, reservoir decisions, and timer-feature shopping

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

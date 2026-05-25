- Lane: passive-income / troubleshooting-page refresh
- Status: pass completed
- Page: `site/content/posts/how-many-drip-emitters-per-pot-container-size-chart.md`
- Scope: tighten self-sorting and cluster handoffs for the emitter-count chart without changing governed-link policy
- Timestamp: 2026-05-06 15:02 EDT

## What changed
1. Added a top-of-page `Fast starting point` routing table so readers can split themselves faster between uneven watering, emitter-type choice, baskets/rail planters, clogging, and no-faucet reservoir setups.
2. Expanded the `Related articles` block so the page now hands readers into clogged-emitter and no-faucet diagnosis paths instead of pretending emitter count is the only variable that matters.

## Why this mattered
The page already had a useful sizing chart, but it still risked trapping readers inside a single-variable answer when many of them actually have distribution, pressure, or layout problems.

This pass makes the page more useful by:
- reducing false emitter-count diagnosis
- improving handoffs into adjacent troubleshooting pages
- keeping basket/rail and no-faucet readers from getting bad generic advice

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

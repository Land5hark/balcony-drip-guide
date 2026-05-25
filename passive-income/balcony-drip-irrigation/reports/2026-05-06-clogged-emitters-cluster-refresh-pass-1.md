- Lane: passive-income / troubleshooting-page refresh
- Status: pass completed
- Page: `site/content/posts/how-to-fix-clogged-drip-emitters-in-potted-plants.md`
- Scope: tighten diagnosis paths and cluster handoffs for the clogged-emitter guide without changing governed-link policy
- Timestamp: 2026-05-06 10:00 EDT

## What changed
1. Added a top-of-page `Fast starting point` table so readers can route themselves faster by actual failure mode: whole-system uneven watering, emitter-count mistakes, expansion overload, dirty-water issues, or no-faucet reservoir problems.
2. Expanded the `Related articles` block so the page now links directly into the expansion guide as an adjacent diagnosis path instead of treating clogging like an isolated problem.

## Why this mattered
The page already gave solid emitter-cleaning advice, but it still risked trapping readers in part-level troubleshooting when some of them really have a wider layout or water-quality problem.

This pass makes the page more useful by:
- reducing false single-part diagnosis
- improving handoffs into broader system troubleshooting
- tightening reservoir-specific cluster routing

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

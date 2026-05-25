- Lane: passive-income / buyer-page refresh
- Status: pass completed
- Page: `site/content/posts/vacation-watering-for-container-gardens-using-drip-irrigation.md`
- Scope: improve intent routing and cluster handoffs for the vacation-watering guide without changing governed-link policy
- Timestamp: 2026-05-06 05:30 EDT

## What changed
1. Added a top-of-page `Fast starting point` table so readers can route themselves faster by actual trip-planning constraint: broad kit choice, no-faucet reality, solar-specific buying, existing uneven watering, or timer-shopping confusion.
2. Tightened the page's role as a vacation-specific filter by routing broader setup uncertainty into the main kit, no-faucet, solar, and smart-timer guides instead of making this article carry every upstream decision alone.
3. Expanded the `Related articles` block so the page now hands traffic more cleanly into bucket-vs-solar, uneven-watering, and other adjacent setup/troubleshooting guides.

## Why this mattered
The page already had the right cautionary tone, but it still made readers work too hard to find the next guide that matched their actual constraint.

This pass makes the page more useful earlier:
- faster self-sorting before travel
- cleaner cluster flow into adjacent buyer and troubleshooting pages
- less chance that trip-planning readers confuse system-family, timer, and troubleshooting decisions

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

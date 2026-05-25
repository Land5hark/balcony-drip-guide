- Lane: passive-income / comparison-page refresh
- Status: pass completed
- Page: `site/content/posts/adjustable-emitters-vs-button-drippers-for-container-gardens.md`
- Scope: improve buyer routing and cluster handoffs for the live emitter-comparison page without changing governed-link policy
- Timestamp: 2026-05-05 22:15 EDT

## What changed
1. Added a `Fast starting point` table near the top so readers can route themselves faster by real failure pattern: mixed pots, uniform pots, coverage problems, clogging, or accessory-buying mode.
2. Strengthened internal-link handoffs to the emitter-count, clog-fix, filter/pressure, and accessories guides from the new routing section.
3. Added a clearer handoff near the recommendation section to the smart-timer guide for readers whose real bottleneck is scheduling rather than emitter choice.

## Why this mattered
The comparison page already explained the tradeoff well, but it still assumed readers were definitely solving an emitter-style problem.

This pass makes the page more useful earlier:
- better intent match for readers who are not fully sure what kind of problem they have
- cleaner deflection toward troubleshooting or accessory pages when emitter style is not the real issue
- stronger internal-link flow into adjacent buyer and problem-solving content

## Guardrails kept
- No live affiliate URLs were added.
- No new product-specific claims were introduced.
- Governed placeholder policy remains unchanged.

## Verification
- `hugo --minify` completed successfully in `site/`

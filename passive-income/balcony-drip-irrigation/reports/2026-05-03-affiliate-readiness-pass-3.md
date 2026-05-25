- Lane: Governed affiliate-link readiness
- Status: PASS
- Niche: balcony / patio container drip irrigation
- Scope: added governed destination placeholder blocks to two troubleshooting-heavy commercial pages that already had registry coverage but no in-article monetization inventory
- Trigger: proactive heartbeat execution against the passive-income queue
- Timestamp: 2026-05-03 10:18 EDT

## Inputs reviewed
- `passive-income/balcony-drip-irrigation/site/data/link-registry.yaml`
- `passive-income/balcony-drip-irrigation/site/content/posts/do-you-need-a-filter-and-pressure-reducer-for-patio-drip-kits.md`
- `passive-income/balcony-drip-irrigation/site/content/posts/how-to-fix-clogged-drip-emitters-in-potted-plants.md`

## Work performed
1. Confirmed the registry already contained governed placeholder slots for the filter / pressure guide and the clogged-emitter troubleshooting guide.
2. Added a `Natural monetization fit` section to the filter / pressure guide with placeholder coverage for filters, pressure reducers, and combined flow-control upgrade paths.
3. Added a matching `Natural monetization fit` section to the clogged-emitter guide with placeholder coverage for replacement emitters, inline filters, and connector / short-line repair parts.
4. Rebuilt the Hugo site with `hugo --minify` to verify the updated pages still compile cleanly.

## Artifacts updated
- `passive-income/balcony-drip-irrigation/site/content/posts/do-you-need-a-filter-and-pressure-reducer-for-patio-drip-kits.md`
- `passive-income/balcony-drip-irrigation/site/content/posts/how-to-fix-clogged-drip-emitters-in-potted-plants.md`
- `passive-income/balcony-drip-irrigation/reports/2026-05-03-affiliate-readiness-pass-3.md`

## Findings
- Two commercially useful troubleshooting pages were still missing explicit governed placeholder blocks even though their registry slots were already defined.
- After this pass, later affiliate insertion on the filter / clogging branch should be faster and less error-prone because the article bodies now expose their intended slot inventory.
- Local build remained clean after the edits.

## Decision
- PASS
- Reason: one concrete readiness package closed more of the registry-to-article gap on high-intent troubleshooting pages without changing the non-monetized publishing posture.

## Recommended next handoff
- Next lane: continue affiliate readiness on the remaining registry-backed live pages, especially uneven-watering, emitter-count, hanging-baskets, bucket-vs-solar, and solar-vs-faucet comparison articles.
- Why: those pages already have clear product-fit logic and just need the same explicit placeholder structure to make later affiliate insertion low-friction.

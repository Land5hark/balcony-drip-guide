- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/best-drip-setup-for-hanging-baskets-and-rail-planters.md`
- Scope: clean up the governed destination quality on the hanging-baskets / rail-planters guide
- Timestamp: 2026-05-05 10:00 EDT

## Problem
This page was still dragging around four generic selector placeholders.

That was weak for a guide explicitly about:
- adjustable coverage
- staking and stability
- multi-point rail-planter distribution
- cleaner branch layouts

## Evidence used
- Brave results already surfaced clean Drip Depot paths for:
  - `https://www.dripdepot.com/product/adjustable-dripper`
  - `https://www.dripdepot.com/product/adjustable-dripper-on-6-inch-stake`
  - `https://www.dripdepot.com/category/drip-irrigation-drippers`
- previously recovered connector category path:
  - `https://www.dripdepot.com/category/drip-irrigation-fittings-tubing-barbed-couplers`

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-baskets-emitters-primary`
  - from: generic selector
  - to: adjustable dripper product path
- `bdi-baskets-stakes-primary`
  - from: generic selector
  - to: adjustable dripper on 6-inch stake path
- `bdi-rail-planter-drippers-primary`
  - from: generic selector
  - to: drippers category path
- `bdi-rail-planter-connectors-primary`
  - from: generic selector
  - to: barbed-couplers category path

Also tightened the notes so they describe the actual basket / rail-planter problem instead of vague irrigation sludge.

## Outcome
The baskets / rail-planters guide now maps more honestly across:
- adjustable coverage path
- staked stability path
- multi-point dripper path
- branch-layout connector path

Still not affiliate-ready. But it is a lot less blob-shaped now.
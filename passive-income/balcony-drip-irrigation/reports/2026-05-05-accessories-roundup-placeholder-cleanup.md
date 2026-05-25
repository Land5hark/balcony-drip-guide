- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/best-drip-irrigation-accessories-that-actually-help-container-gardens.md`
- Scope: clean up the governed destination quality on the accessories roundup
- Timestamp: 2026-05-05 11:30 EDT

## Problem
The accessories roundup was still dragging five generic selector placeholders behind it.

That is especially dumb on a page whose whole pitch is "buy the accessory that fixes the real problem".

## Evidence used
Previously recovered destination-quality paths already covered the actual accessory branches this page talks about:
- drippers category path
- adjustable dripper on stake path
- barbed-couplers category path
- hose-thread filter path
- B-hyve smart hose faucet timer path

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-accessories-emitters-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/irrigation-supplies-drippers`
- `bdi-accessories-stakes-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/adjustable-dripper-on-6-inch-stake`
- `bdi-accessories-connectors-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/category/drip-irrigation-fittings-tubing-barbed-couplers`
- `bdi-accessories-filter-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/three-quarter-inch-hose-thread-filter`
- `bdi-accessories-timer-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/bhyve-smart-hose-faucet-timer`

Also tightened the notes so they describe actual accessory-use cases instead of vague irrigation sludge.

## Outcome
The accessories roundup now maps more honestly across:
- emitter add-on path
- stability / staked-emitter path
- connector / repair path
- filter path
- timer-upgrade path

Still not affiliate-ready, obviously. But it is a lot less blob-shaped now.
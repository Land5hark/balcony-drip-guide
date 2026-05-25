- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/container-drip-irrigation-maintenance-checklist-for-summer.md`
- Scope: clean up the governed destination quality on the summer maintenance checklist
- Timestamp: 2026-05-05 11:00 EDT

## Problem
The summer maintenance guide still had generic selector sludge on the three Drip Depot maintenance slots.

That was weak for a page explicitly about:
- dripper wear and partial clogs
- filter maintenance
- connector and branch cleanup

## Evidence used
Previously recovered destination-quality evidence already supports cleaner paths for this maintenance intent:
- drippers category path
- hose-thread filter product path
- barbed-couplers category path
- existing RainPoint reservoir path was already specific enough for the no-faucet side

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-maintenance-emitters-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/irrigation-supplies-drippers`
- `bdi-maintenance-filter-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/three-quarter-inch-hose-thread-filter`
- `bdi-maintenance-connectors-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/category/drip-irrigation-fittings-tubing-barbed-couplers`

Also tightened the notes so they describe the actual maintenance problem instead of generic irrigation mush.

## Outcome
The summer maintenance guide now maps more honestly across:
- emitter replacement / maintenance path
- filter-cleaning / clog-prevention path
- connector / branch-cleanup path
- existing reservoir-maintenance path

Still not affiliate-ready. But it is less vague and less useless now.
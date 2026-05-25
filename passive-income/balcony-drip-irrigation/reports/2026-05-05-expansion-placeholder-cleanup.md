- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/how-to-expand-a-patio-drip-kit-without-losing-pressure.md`
- Scope: clean up the governed destination quality on the patio-expansion guide
- Timestamp: 2026-05-05 12:30 EDT

## Problem
The patio-expansion guide was still pointing all four governed slots at the same generic selector blob.

That was weak for a page explicitly about:
- branch additions
- tubing reroutes
- added watering points
- filter / pressure-control cleanup when a kit gets stretched

## Evidence used
Previously recovered destination-quality paths already covered the actual expansion branches this page talks about:
- barbed-couplers category path
- polyethylene tubing category path
- drippers category path
- pressure-regulating Y-filter path
- tubing buying-guide search result also supported the tubing category split

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-expand-connectors-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/category/drip-irrigation-fittings-tubing-barbed-couplers`
- `bdi-expand-tubing-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/category/polyethylene-irrigation-tubing`
- `bdi-expand-emitters-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/irrigation-supplies-drippers`
- `bdi-expand-filter-pressure-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/pressure-regulating-plastic-y-filter`

Also tightened the notes so they describe the actual expansion problem instead of generic irrigation sludge.

## Outcome
The patio-expansion guide now maps more honestly across:
- connector / branch-addition path
- tubing-reroute path
- added-emitter path
- filter / pressure-control path

Still not affiliate-ready, obviously. But it is much less blob-shaped now.
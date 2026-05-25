- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/do-you-need-a-filter-and-pressure-reducer-for-patio-drip-kits.md`
- Scope: clean up the governed destination quality on the filter / pressure-reducer buyer guide
- Timestamp: 2026-05-05 08:30 EDT

## Problem
The filter/pressure guide was still sending all three governed slots to the same generic Drip Depot selector.

That is sloppy for a page explicitly separating three different upstream-control decisions:
- filter need
- pressure-regulator need
- combined upgrade path

## Sources checked
- `https://help.dripdepot.com/support/solutions/articles/11000044353-irrigation-filter-buying-guide`
- `https://help.dripdepot.com/support/solutions/articles/11000044625-drip-irrigation-pressure-regulators-faq`
- Brave results for:
  - `https://www.dripdepot.com/high-flow-y-filter-three-quarter-inch-ght`
  - `https://www.dripdepot.com/irrigation-supplies-pressure-regulators`
  - `https://www.dripdepot.com/product/pressure-regulating-plastic-y-filter`

## Evidence
- Drip Depot support still treats filtration and pressure regulation as distinct upstream-control functions.
- Drip Depot still exposes a hose-thread Y-filter path appropriate for faucet-fed patio hardware.
- Drip Depot still exposes a dedicated pressure-regulator category path.
- Drip Depot also still exposes a combined pressure-regulating Y-filter path that fits the article's bundle-style upgrade logic better than generic selector sludge.

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-filter-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/high-flow-y-filter-three-quarter-inch-ght`
- `bdi-pressure-reducer-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/irrigation-supplies-pressure-regulators`
- `bdi-filter-pressure-bundle-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/pressure-regulating-plastic-y-filter`

Also tightened the notes so they describe actual faucet-fed buyer intent instead of generic irrigation mush.

## Outcome
The filter/pressure guide now maps more honestly across:
- filter path
- pressure-regulator path
- combined filter/regulator path

Still not affiliate-ready, obviously. But it is a hell of a lot less vague now.
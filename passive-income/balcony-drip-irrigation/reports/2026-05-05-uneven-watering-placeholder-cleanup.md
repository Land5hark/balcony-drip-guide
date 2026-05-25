- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/why-your-container-drip-system-is-watering-unevenly.md`
- Scope: clean up the governed destination quality on the uneven-watering troubleshooting guide
- Timestamp: 2026-05-05 13:00 EDT

## Problem
The uneven-watering guide was still dragging four generic selector placeholders behind a page that is supposed to diagnose real failure causes.

That was weak.

This page explicitly separates:
- clog/debris issues
- pressure-control issues
- bad/weak emitter issues
- layout and branch-cleanup issues

So the governed destinations needed to stop acting like all of that is one blob.

## Evidence used
Previously recovered destination-quality paths already covered the actual troubleshooting branches this page talks about:
- hose-thread filter product path
- pressure-regulators category path
- drippers category path
- barbed-couplers category path

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-troubleshoot-filter-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/three-quarter-inch-hose-thread-filter`
- `bdi-troubleshoot-pressure-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/irrigation-supplies-pressure-regulators`
- `bdi-troubleshoot-emitters-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/irrigation-supplies-drippers`
- `bdi-troubleshoot-connectors-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/category/drip-irrigation-fittings-tubing-barbed-couplers`

Also tightened the notes so they describe actual troubleshooting intent instead of vague irrigation sludge.

## Outcome
The uneven-watering guide now maps more honestly across:
- clog / debris path
- pressure-control path
- replacement-emitter path
- connector / layout-cleanup path

Still not affiliate-ready, obviously. But at least it no longer treats four different failure branches like the same useless blob link.
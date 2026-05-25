- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/how-many-drip-emitters-per-pot-container-size-chart.md`
- Scope: clean up the governed destination quality on the emitter-count buyer/support page
- Timestamp: 2026-05-05 07:00 EDT

## Problem
The emitter-count page was commercially shaped, but all three governed placeholders still pointed at the same lazy generic Drip Depot selector.

That was weak.

This page is explicitly about emitter type, emitter count, and filter-related clog distortion, so the governed destinations needed to stop acting like all irrigation parts are the same blob.

## Sources checked
- `https://help.dripdepot.com/support/solutions/articles/11000043229-dripper-buying-guide`
- `https://help.dripdepot.com/support/solutions/articles/11000044432-all-about-emitters-drippers`
- `https://help.dripdepot.com/support/solutions/articles/11000044353-irrigation-filter-buying-guide`
- Brave results for:
  - `https://www.dripdepot.com/product/adjustable-dripper`
  - `https://www.dripdepot.com/irrigation-supplies-drippers`
  - `https://www.dripdepot.com/product/pressure-regulating-plastic-y-filter`

## Evidence
- Drip Depot support still distinguishes adjustable emitters from button/fixed-flow drippers based on watering requirement and wetted-area needs.
- Support language still says adjustable / stream-style drippers fit larger wetted areas and wider root zones better than standard drippers.
- Drip Depot also still exposes a direct drippers category path and a pressure-regulating Y-filter product path that are much closer to the page's actual buyer intent than the generic selector sludge.

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-emitters-adjustable-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/adjustable-dripper`
- `bdi-emitters-fixedflow-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/irrigation-supplies-drippers`
- `bdi-emitters-filter-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/pressure-regulating-plastic-y-filter`

Also tightened the slot notes so they describe actual buyer intent instead of vague irrigation mush.

## Outcome
The emitter-count page's governed destinations now map more honestly across:
- adjustable emitter path
- fixed-flow/button-dripper comparison path
- filter/clog-prevention path

Still not affiliate-ready, obviously. But at least it is no longer pretending one generic selector solves three different decisions.
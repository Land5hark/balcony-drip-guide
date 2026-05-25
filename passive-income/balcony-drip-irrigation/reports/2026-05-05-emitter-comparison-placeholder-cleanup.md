- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/adjustable-emitters-vs-button-drippers-for-container-gardens.md`
- Scope: clean up the governed destination quality on the emitter-comparison page
- Timestamp: 2026-05-05 07:30 EDT

## Problem
The emitter-comparison page was still pointing all three governed slots at the same generic Drip Depot selector.

That is lazy and not remotely specific enough for a page comparing adjustable emitters, button drippers, and filter-related maintenance support.

## Evidence used
- Drip Depot support results already surfaced during the emitter-path cleanup pass:
  - dripper buying guide
  - all-about-emitters/drippers support page
  - irrigation filter buying guide
- product/category paths already recovered:
  - `https://www.dripdepot.com/product/adjustable-dripper`
  - `https://www.dripdepot.com/irrigation-supplies-drippers`
  - `https://www.dripdepot.com/product/pressure-regulating-plastic-y-filter`

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-adjustable-emitters-primary`
  - from: generic selector
  - to: adjustable dripper product path
- `bdi-button-drippers-primary`
  - from: generic selector
  - to: drippers category path
- `bdi-emitter-comparison-filter-primary`
  - from: generic selector
  - to: pressure-regulating Y-filter product path

Also tightened the notes so they describe the actual buyer/problem intent instead of generic irrigation mush.

## Outcome
The emitter-comparison page now maps more honestly across:
- adjustable-emitter tuning path
- button-dripper / fixed-output comparison path
- filter support path for clog-prone or pressure-messy systems

Still not affiliate-ready. But at least it stopped pretending three different decisions all deserve the same blob link.
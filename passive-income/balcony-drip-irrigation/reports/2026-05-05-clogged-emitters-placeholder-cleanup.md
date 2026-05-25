- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/how-to-fix-clogged-drip-emitters-in-potted-plants.md`
- Scope: clean up the governed destination quality on the clogged-emitter troubleshooting page
- Timestamp: 2026-05-05 09:30 EDT

## Problem
The clogged-emitter troubleshooting page still had three lazy blob links.

That is dumb for a page that is explicitly separating:
- filtration / debris prevention
- emitter replacement
- connector / fitting false-alarm issues

## Sources checked
- `https://help.dripdepot.com/support/solutions/articles/11000068454-drip-irrigation-system-troubleshooting-and-repair-guide`
- `https://help.dripdepot.com/support/solutions/articles/11000043229-dripper-buying-guide`
- Brave results for:
  - `https://www.dripdepot.com/product/three-quarter-inch-hose-thread-filter`
  - `https://www.dripdepot.com/irrigation-supplies-drippers`
  - `https://www.dripdepot.com/category/drip-irrigation-fittings-tubing-barbed-couplers`

## Evidence
- Drip Depot troubleshooting guidance still says proper filtration matters and that flushing + filter maintenance are preventive basics.
- Dripper guidance still says some clogged drippers should be cleaned, but non-cleanable / too-far-gone drippers end up as replacement problems.
- Drip Depot still exposes a hose-thread filter path, a drippers category path, and a tubing-coupler category path that match the page's actual troubleshooting branches far better than selector sludge.

## Changes made
Updated `site/data/link-registry.yaml`:
- `bdi-clogged-emitters-filter-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/product/three-quarter-inch-hose-thread-filter`
- `bdi-clogged-emitters-replacement-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/irrigation-supplies-drippers`
- `bdi-clogged-emitters-connectors-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/category/drip-irrigation-fittings-tubing-barbed-couplers`

Also tightened the notes so they describe actual troubleshooting intent instead of mush.

## Outcome
The clogged-emitter page now maps more honestly across:
- filter maintenance path
- replacement-emitter path
- connector / fitting false-alarm path

Still not affiliate-ready. But at least it stopped pretending every clogged-emitter problem deserves the same useless blob link.
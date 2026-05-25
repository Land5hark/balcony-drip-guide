- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/vacation-watering-for-container-gardens-using-drip-irrigation.md`
- Scope: clean up the last broad faucet-fed timer placeholder on the vacation-watering buyer guide
- Timestamp: 2026-05-05 14:30 EDT

## Problem
The vacation-watering guide still had a lazy generic selector on the faucet-fed timer slot.

That was weak for a page explicitly telling readers that a faucet-fed timer + modular drip setup is usually the cleanest travel answer when hose access exists.

## Evidence used
Previously recovered timer-path evidence already covered a cleaner destination:
- `https://www.dripdepot.com/bhyve-smart-hose-faucet-timer`
- earlier timer-cleanup work already confirmed the smart hose-timer path as a legitimate governed destination for faucet-fed automation intent

## Change made
Updated `site/data/link-registry.yaml`:
- `bdi-vacation-faucet-timer-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/bhyve-smart-hose-faucet-timer`

Also tightened the note so it reflects the real trip-specific use case:
- remote schedule control
- mid-trip adjustments
- faucet-fed modular watering

## Outcome
The vacation-watering guide now has a cleaner product-shaped faucet-timer destination instead of blob sludge.

Still not affiliate-ready, obviously. But it is less dumb now.
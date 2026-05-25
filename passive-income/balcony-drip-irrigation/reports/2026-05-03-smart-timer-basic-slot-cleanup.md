- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/smart-watering-timers-for-balcony-and-patio-container-gardens.md`
- Scope: clean up the last weak governed destination on the timer buyer guide
- Timestamp: 2026-05-03 18:52 EDT

## Problem
The smart-timer article already had decent primary and budget timer placeholders, but the fallback basic-timer slot was still lazily pointing at the generic Drip Depot kit selector.

That was sloppy.

The article explicitly tells some buyers to skip app-heavy gear and choose a simpler timer path, so the governed destination needed to match that reality.

## Sources checked
- `https://help.dripdepot.com/support/solutions/articles/11000101489-hose-end-water-timer-buying-guide`
- `https://www.dripdepot.com/product/orbit-mechanical-hose-faucet-timer`
- Brave result snippet for the Drip Depot Orbit mechanical timer product page

## Evidence
- Drip Depot's hose-end timer buying guide still says that if someone wants a more old-school and simple gardening style, the **Orbit Mechanical Hose Faucet Timer** is a good fit.
- Brave surfaced a clean product page path for that exact timer on Drip Depot.
- That gives the fallback slot an actual product-shaped destination instead of vague selector sludge.

## Change made
Updated `site/data/link-registry.yaml`:
- `bdi-smart-timers-backup-basic-primary`
  - from: `https://www.dripdepot.com/irrigation-kit-selector`
  - to: `https://www.dripdepot.com/product/orbit-mechanical-hose-faucet-timer`

Also tightened the note so it clearly describes the buyer intent:
- dead-simple
- no batteries
- not app-heavy

## Outcome
The timer article's governed placeholders now map more honestly across all three lanes:
- smart hose timer
- simpler programmable timer
- basic mechanical fallback timer

That does not finish full timer-page trust hardening, but it removes one of the dumbest placeholder mismatches in the cluster.
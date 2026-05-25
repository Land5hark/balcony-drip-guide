- Lane: governed affiliate-link readiness
- Status: pass completed
- Scope: close out the broad-selector cleanup sweep on the balcony-drip link registry
- Timestamp: 2026-05-05 16:30 EDT

## What I checked
Scanned `site/data/link-registry.yaml` for any remaining `https://www.dripdepot.com/irrigation-kit-selector` destinations.

## Result
Only **one** selector path remains:
- `bdi-kit-dripdepot-selector-primary`
- article: `best-drip-irrigation-kits-for-balcony-container-gardens`

## Why this one stays
This is not the same lazy blob problem as the others.

The article explicitly recommends a **build-your-own modular kit selector** as a distinct buying path for growers who keep adding pots or need custom sizing.

Brave still surfaces `https://www.dripdepot.com/irrigation-kit-selector` as Drip Depot's live **Build your own irrigation kit** path, so keeping it here is intentional instead of sloppy.

## Outcome
The generic-selector cleanup sweep is effectively done.

What is left is:
- one intentional build-your-own selector path
- not a pile of vague unresolved placeholders

That means the next leverage is no longer registry blob cleanup.
It is fact review, promotion reuse, deployment parity, and later owner-approved monetization handoff.
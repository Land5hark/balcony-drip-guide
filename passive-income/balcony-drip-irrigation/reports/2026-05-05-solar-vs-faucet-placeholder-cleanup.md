- Lane: governed affiliate-link readiness
- Status: pass completed
- Page: `site/content/posts/solar-vs-faucet-timer-drip-systems-for-patio-plants.md`
- Scope: clean up the last broad faucet-fed destination on the solar-vs-faucet comparison page
- Timestamp: 2026-05-05 16:00 EDT

## Problem
The solar-vs-faucet comparison page was still dragging a generic selector blob on its faucet-fed branch.

That was weak for a page that explicitly frames the faucet side around container-gardening kits, hose access, and modular expansion logic.

## Evidence used
Previously verified Drip Depot container-gardening evidence already supported a cleaner faucet-fed landing path:
- `https://www.dripdepot.com/drip-irrigation-kit-for-container-gardening`
- the earlier Drip Depot fact-check pass already tied the article's faucet-fed branch to the container-gardening kit lane and its support guidance

## Change made
Updated `site/data/link-registry.yaml`:
- `bdi-solar-vs-faucet-faucet-primary`
  - from: generic selector
  - to: `https://www.dripdepot.com/drip-irrigation-kit-for-container-gardening`

Also tightened the note so it reflects the actual comparison logic instead of generic selector mush.

## Outcome
The solar-vs-faucet comparison page now has a cleaner faucet-fed destination that actually matches the article's container-kit framing.

Still not affiliate-ready, obviously. But at least it stopped pointing a real comparison branch at blob sludge.
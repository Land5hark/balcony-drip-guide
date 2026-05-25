- Lane: fact review / trust hardening
- Status: pass completed
- Page: `site/content/posts/best-drip-irrigation-kits-for-balcony-container-gardens.md`
- Scope: re-check the main commercial kit guide against live merchant/support sources and remove source-drift risk
- Timestamp: 2026-05-05 04:19 EDT

## Sources checked
- `https://help.dripdepot.com/support/solutions/articles/11000044366-container-gardening`
- `https://help.dripdepot.com/support/solutions/articles/11000044498-container-kit-selection-guides`
- `https://www.dripdepot.com/irrigation-kit-selector`
- `https://www.rainpointonline.com/products/rainpoint-compact-programmable-solar-automatic-drip-irrigation-pump-kits-support-up-to-20-plants`
- `https://www.rainpointonline.com/products/rainpoint-large-display-automatic-plant-waterer-indoor-for-up-to-20-pot-plants`
- `site/data/link-registry.yaml`

## What this pass verified
### Drip Depot faucet-fed kit path
Current Drip Depot support content still supports the article's core faucet-fed framing:
- container kits are built to connect to a standard outdoor faucet or garden hose
- the kit line still spans roughly 10 to 120 containers
- the Build Your Own / customization path still exists for layouts that do not fit the stock kits cleanly

### RainPoint solar no-faucet path
The current RainPoint solar product page still supports the article's no-faucet recommendation:
- the page still matches the compact solar balcony/potted-plant path
- `up to 20 plants` remains seller language and should still be treated as a ceiling rather than a promise
- the product manual link still appears on the page

### RainPoint small-kit path
The current RainPoint reservoir kit page still supports the convenience-first small-collection branch:
- page title still matches the 10-15 potted-plant lane
- watering frequency and duration ranges still match the article's published numbers
- included parts still support the `10 emitters` and `1 filter` summary
- `waters 10 plants (expandable to 15)` remains the clean way to phrase capacity

### Governed destination fit
Registry slots still align with the article's buyer logic:
- `bdi-kit-dripdepot-container-primary`
- `bdi-kit-dripdepot-selector-primary`
- `bdi-kit-rainpoint-solar-primary`
- `bdi-kit-rainpoint-small-primary`

## New fact that mattered
An older Drip Depot help-article URL used in prior notes now 404s. The live support evidence has effectively moved to:
- `11000044366-container-gardening`
- `11000044498-container-kit-selection-guides`

That means the guide's factual core still holds, but source provenance needed refreshing so future verification does not depend on a dead support URL.

## Edits made
1. Updated the article method note to show the recommendation set was re-checked on 2026-05-05.
2. Tightened the Drip Depot section wording so it points to current support-doc framing instead of stale publication timing.
3. Updated the publication note so future affiliate insertion triggers one more quick naming/availability check instead of pretending the old 2026-04-30 pass is enough forever.

## Outcome
No substantive product recommendation changes were needed.

The important win here is that the main commercial hub page now points at live supporting evidence again instead of quietly relying on a dead Drip Depot source path.

# Balcony drip irrigation affiliate activation checklist

Purpose: make owner-side affiliate setup and later governed link insertion low-friction once Sharky is ready to activate monetization.

Status: prep complete for later owner action. No affiliate URLs should be inserted before account approval, tax/payout setup, and final link review.

## What is already true
- Drip Depot remains the strongest primary merchant path for faucet-fed and timer-led buyer pages.
- RainPoint remains the strongest secondary path for no-faucet and solar/reservoir buyer pages.
- The site is already running governed placeholders in `site/data/link-registry.yaml`.
- Article-body placeholder coverage is complete across the live cluster.

## Phase 1 — owner-side account activation (**critical**)

### Drip Depot
1. Open the affiliate portal: `https://aff.dripdepot.com/aff/index.php`
2. Create or confirm the owner account.
3. Complete tax and payout setup.
4. Confirm the current commission terms and payout threshold inside the approved account.
5. Confirm whether deep-link generation is available directly in the portal.
6. Save the approved affiliate base/link format somewhere owner-visible.

### RainPoint
1. Open the affiliate page: `https://www.rainpointonline.com/pages/affiliate-program`
2. Follow the UpPromote application path.
3. Complete tax and payout setup.
4. Confirm the current commission and cookie terms inside the approved platform.
5. Confirm deep-link creation flow for product pages.
6. Save the approved affiliate base/link format somewhere owner-visible.

## Phase 2 — first URL harvest (**critical**)
Collect approved affiliate URLs only for the highest-leverage governed slots first.

### Drip Depot first-priority slots
- `bdi-kit-dripdepot-container-primary`
- `bdi-kit-dripdepot-selector-primary`
- `bdi-smart-timers-primary`
- `bdi-smart-timers-budget-primary`
- `bdi-smart-timers-backup-basic-primary`
- `bdi-solar-vs-faucet-faucet-primary`
- `bdi-vacation-faucet-timer-primary`

### RainPoint first-priority slots
- `bdi-solar-rainpoint-compact-primary`
- `bdi-solar-rainpoint-smart-primary`
- `bdi-nofaucet-rainpoint-solar-primary`
- `bdi-nofaucet-compact-reservoir-primary`
- `bdi-vacation-solar-primary`
- `bdi-vacation-compact-primary`
- `bdi-kit-rainpoint-solar-primary`

## Phase 3 — governed workspace insertion (**critical**)
Once approved URLs exist:
1. Keep `destination_url` unchanged as the non-affiliate research fallback.
2. Paste the approved affiliate URL into the matching `affiliate_url` field in `site/data/link-registry.yaml`.
3. Change `monetization_status` only if the slot has truly passed owner review.
4. Do not bulk-paste blindly; verify slot-by-slot against article intent.
5. Start with the highest-value pages before filling the long tail.

## Recommended activation order
1. `best-drip-irrigation-kits-for-balcony-container-gardens`
2. `smart-watering-timers-for-balcony-and-patio-container-gardens`
3. `best-solar-drip-irrigation-kits-for-patios-and-balconies`
4. `balcony-drip-irrigation-without-a-faucet`
5. `vacation-watering-for-container-gardens-using-drip-irrigation`
6. then the comparison/support pages

Reason: this order matches the current strongest buyer intent and the cleanest merchant fit.

## Phase 4 — verification after insertion
1. Rebuild the site with `hugo --minify`.
2. Inspect the affected pages to confirm the correct merchant path appears in the correct article context.
3. Confirm no empty `affiliate_url` field was expected for any newly activated slot.
4. Confirm no RainPoint URL landed on a faucet-fed Drip Depot slot or vice versa.
5. Check disclosure visibility on the affected pages.
6. Spot-check at least one activated slot per merchant in built output before any deployment push.

## Phase 5 — publish/deploy gate
Only after the above is clean:
1. deploy the updated site
2. verify live page rendering
3. click-test a small sample of live outbound links
4. record activation date and the first set of activated slots

## Pre-mortem: most likely failure modes
- **Wrong merchant on the wrong page** -> verify slot-by-slot against article intent before build.
- **Account approved but tax/payout incomplete** -> do not insert URLs until payout setup is fully done.
- **Deep links differ from placeholder product paths** -> replace only after matching the exact page purpose.
- **Bulk insertion causes hidden mismaps** -> activate the short priority list first, then expand.
- **Deployment happens before live QA** -> require built-output spot checks before any push.

## Minimal handoff note for Sharky later
When ready to monetize, the only owner action needed first is:
- get Drip Depot approved
- get RainPoint/UpPromote approved
- send back the first approved deep links for the priority slots above

After that, governed insertion is straightforward.

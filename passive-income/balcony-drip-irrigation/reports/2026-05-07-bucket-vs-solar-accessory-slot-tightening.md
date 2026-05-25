# Bucket-vs-solar accessory slot tightening

- Lane: passive-income / governed affiliate readiness
- Status: pass completed
- Scope: tighten the bucket-vs-solar comparison page's remaining soft accessory placeholder so it matches the article's bucket-fed DIY lane instead of pointing at the wrong packaged reservoir merchant path
- Timestamp: 2026-05-07 10:18 EDT

## Problem
One governed slot was still drifting away from the article's actual buyer logic:
- `bdi-bucket-vs-solar-reservoir-accessories-primary`

Before this pass, that slot was wired to:
- merchant: `RainPoint`
- destination: RainPoint large-display reservoir kit page

That was a mismatch because the article's third placeholder lane is not another packaged reservoir-kit recommendation. It is the softer **bucket-fed DIY component / accessory** path for growers who want the cheaper simpler no-faucet build route.

This also contradicted the earlier fact-review note that said the slot should remain a broad Drip Depot selector-style path.

## Change made
Updated the slot in `site/data/link-registry.yaml` to:
- merchant: `Drip Depot`
- role: `supporting`
- destination: `https://www.dripdepot.com/irrigation-kit-selector`
- notes: clarified that it is the bucket-fed DIY component placeholder for a simpler no-faucet build path

## Verification
Loaded the registry with a YAML parse and re-read the slot.

Observed result:
- `bdi-bucket-vs-solar-reservoir-accessories-primary` now resolves to a single Drip Depot selector-backed supporting slot
- the merchant/path now matches the page's concept-first bucket-fed lane better than the old RainPoint packaged-kit fallback

## Why this matters
This is a small but real governed-affiliate improvement:
- less merchant mismatch in later link activation
- cleaner separation between solar kit, simple reservoir kit, and bucket-fed DIY path
- better alignment between article intent and placeholder destination shape

## Outcome
The bucket-vs-solar comparison page now has a cleaner three-lane governed placeholder set:
- solar kit path
- simpler packaged reservoir kit path
- broader bucket-fed DIY component path

That is materially safer for later affiliate insertion than leaving two of the three lanes effectively pointing at the same RainPoint reservoir solution.
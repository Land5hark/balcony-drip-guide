# Bucket-vs-solar link registry dedupe

- Lane: passive-income / governed affiliate readiness
- Status: pass completed
- Scope: remove duplicate governed placeholder slots in `site/data/link-registry.yaml` for the bucket-vs-solar comparison page so later affiliate insertion does not inherit conflicting destination rows
- Timestamp: 2026-05-07 08:19 EDT

## What was wrong
The registry contained duplicate entries for two bucket-vs-solar slots:
- `bdi-bucket-vs-solar-solar-kits-primary`
- `bdi-bucket-vs-solar-reservoir-kits-primary`

The duplicates were not harmless cosmetics:
- one solar slot version pointed at a broader RainPoint collection URL
- the kept solar slot points at the tighter compact solar product path already aligned with the article's verified no-faucet comparison logic
- one reservoir slot version used `role: primary`
- the kept reservoir slot uses `role: secondary`, which better matches the article's simpler fallback positioning

That ambiguity would have made later governed-link activation and any registry-driven insertion logic less trustworthy.

## What changed
Removed the older duplicate rows and kept the cleaner product-shaped placeholders:
- `bdi-bucket-vs-solar-solar-kits-primary` -> RainPoint compact solar product path
- `bdi-bucket-vs-solar-reservoir-kits-primary` -> RainPoint large-display reservoir kit path (`secondary`)

## Verification
Ran a duplicate-slot audit against `site/data/link-registry.yaml` after the edit.

Observed result:
- duplicate slot count returned empty
- both kept bucket-vs-solar slots now resolve to a single unambiguous registry row each

## Why this matters
This is small, but it is real governed-affiliate hygiene:
- fewer ambiguous placeholders
- cleaner future affiliate URL insertion
- less chance that later automation or manual link activation picks the wrong destination shape for the article

## Outcome
Bucket-vs-solar governed placeholder state is cleaner now.

The next affiliate-readiness passes should keep looking for this kind of registry ambiguity instead of waiting until monetization day to discover it the hard way.

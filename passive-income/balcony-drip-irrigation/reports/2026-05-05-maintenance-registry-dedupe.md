- Lane: governed affiliate-link readiness
- Status: pass completed
- Scope: remove duplicate stale maintenance slots from the live link registry
- Timestamp: 2026-05-05 15:00 EDT

## Problem
The link registry had a stupid duplicate maintenance block.

One copy was the cleaned version with specific emitter/filter/connector destinations.
The second copy was older selector sludge.

That kind of duplicate is how later audits lie to you.

## Change made
Removed the stale duplicate block for:
- `bdi-maintenance-emitters-primary`
- `bdi-maintenance-filter-primary`
- `bdi-maintenance-connectors-primary`
- `bdi-maintenance-reservoir-primary`

The kept block is the newer one with product/category-shaped destinations.

## Outcome
The summer-maintenance article now has one canonical registry block instead of one real block plus one fossil.

Less ambiguity. Less future bullshit.
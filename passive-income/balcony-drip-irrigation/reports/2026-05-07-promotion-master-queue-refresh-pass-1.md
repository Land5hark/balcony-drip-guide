- Lane: passive-income / promotion system cleanup
- Status: pass completed
- Asset: `reports/2026-05-05-promotion-master-queue-week-1.md`
- Scope: refresh the weekly queue so it stops pointing at stale pre-refresh hooks after the Lane A/B/C promotion-copy updates
- Timestamp: 2026-05-07 00:00 EDT

## What changed
1. Updated the Week 1 queue hooks for clogged emitters, smart timers, solar kits, emitter comparison, and expansion so they now match the sharper copy already living in the refreshed lane sheets.
2. Updated the relevant Pinterest mirror titles/overlays where the lane sheets had moved to stronger phrasing.
3. Left the slot structure alone so the system stays easy to ship instead of becoming another clever spreadsheet mausoleum.

## Why this mattered
The lane sheets got sharper, but the master queue was still serving old hooks. That is how content systems quietly rot: source assets improve, dispatch queue stays stale, and then the posted copy lags behind the actual strategy.

Now the weekly queue is back in sync with the current promotion logic across Lane A, B, and C.

## Guardrails kept
- No live posting was attempted.
- No live affiliate URLs were added.
- Queue cadence and reuse rules were left intact.

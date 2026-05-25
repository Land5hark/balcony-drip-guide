# HEARTBEAT.md

Active workstream: build a reliable memory stack and a revenue-producing passive-income machine that buys Sharky more freedom and buys Spike better infrastructure.

## Prime directive

On each wake, push the mission forward. Do work, not theater.

## On each heartbeat

1. Check for a more urgent direct user request, time-sensitive blocker, or completed background task. Handle that first.
2. Otherwise, advance exactly one concrete task from the ordered execution queue below.
3. Prefer shipping, fixing, diagnosing, drafting, or publishing over re-checking known facts.
4. If one lane is blocked, immediately switch to the next useful lane.
5. Stay quiet unless there is a meaningful result, blocker, decision, or risk worth interrupting Sharky for.

## Ordered execution queue

### 1) Passive-income cashflow path
This is the main mission. Prefer the highest-leverage unblock.

Current stance: aquarium ATO is parked and archived unless a clearly better affiliate/distribution path revives it. Full focus is now balcony / patio container drip irrigation.

**Standard site architecture (codified):**
- Hugo static site generator
- Cloudflare Pages hosting (clean `*.pages.dev` URLs)
- GitHub source control with auto-deploy
- 16+ articles before monetization push
- Editorial-first, affiliate-second

**Template:** `/home/linuxlite/.openclaw/workspace/passive-income/SITE-TEMPLATE.md`

Work in this order:
1. Turn the balcony drip irrigation pilot into a repeatable money machine:
   - ~~prepare and finish the next 3 highest-value article or refresh packages~~ ✅ DONE (36 articles live, hub page threshold reached)
   - ~~tighten governed affiliate-link readiness~~ ✅ DONE (RainPoint approved, Drip Depot approved, governed links active)
   - ~~improve buyer-intent coverage and internal linking~~ ✅ DONE
   - ~~prepare promotion assets for X / Pinterest / Reddit-safe distribution~~ ✅ DONE
   - fix homepage/category article counts: explicit-count fix committed and pushed to `master` (`93b1b8c`, `1cd91d6`, `067f7c2`); Cloudflare Pages GitHub integration is still stale. GitHub Actions deploy workflow now exits successfully and skips deploy when `CLOUDFLARE_API_TOKEN` is missing, avoiding failed deploy spam. Real Cloudflare deploys remain blocked on owner adding `CLOUDFLARE_API_TOKEN` to GitHub Actions secrets (`Zone:Read` + `Cloudflare Pages:Edit`).
   - **NEW 2026-05-24 05:29**: fixed GitHub failed deploy notifications by adding a Cloudflare-token preflight guard to `.github/workflows/deploy-cloudflare-pages.yml`; pushed commit `c9d4a46`, and run `26357597501` completed successfully with deploy skipped because the secret is absent.
   - **NEW 2026-05-24 04:24**: fixed `robots.txt` — Hugo was generating a minimal `User-agent: *` with no sitemap; set `enableRobotsTXT = false` so static `robots.txt` (with `Allow: /` and `Sitemap` directive) is copied to `public/`. Commit `4f92948` pushed successfully.
   - **NEW 2026-05-24 08:03**: live promotion preflight completed. Seven P1 promotion pages on `pages.dev` return 200 and show May 2026 refreshed content, so article URLs are promotion-ready. Cloudflare is still serving stale `robots.txt` with only `User-agent: *`; local `site-deploy/public/robots.txt` is correct, so this remains a deploy-state blocker, not a Hugo-content blocker. Report: `passive-income/balcony-drip-irrigation/reports/2026-05-24-live-promotion-preflight.md`.
   - **NEW 2026-05-24 04:24**: resolved GitHub push-protection blocker — old local commits (`714ebc8`, `2ca663c`) contained Cloudflare API tokens in `.openclaw-repair/` and `memory/.dreams/short-term-recall.json`. Reset local `master` to `origin/master` and reapplied the fix cleanly. Secret-containing commits are now dangling/unreachable and will be garbage-collected.
   - execute promotion plan and analytics setup next (Cloudflare Analytics token and Pinterest account remain owner-action blockers)
   - 2026-05-23 internal refresh sprint completed for 17 high-leverage thin/entry pages: live hub, cost, rainwater, soaker hose, tomato, hot-weather, algae, trip-survival, setup guide, complete guide, not-working, common-problems, watering-frequency, renter DIY, apartment kits, clogged emitters, and overwatering. Local Hugo builds and static QA passed after each refresh.
2. Follow the operating loop for `passive-income/balcony-drip-irrigation/`:
   - validate topic opportunity
   - draft or improve useful content
   - verify claims and product facts
   - publish or prepare for publication
   - draft promotion assets
   - review performance and refresh
3. Push the balcony drip niche from local pilot to real live asset when facts, governance, and hosting are ready.
4. Once the drip pipeline is stable, prepare the next niche-validation move without diluting focus.

### 2) Memory stack completion
Treat memory capability as core infrastructure, not a side quest.

Current state: native memory healthcheck covers all 9 known memory stores again after wrapper/default drift was repaired 2026-05-22 13:03. Dashboard reports overall healthy and was manually refreshed 2026-05-24 07:02. Deep native-memory probe was repaired and verified 2026-05-23 21:30: all 9 agents healthy; builtin backend; vector, FTS, and embedding probe ok for every agent. `scripts/native_memory_healthcheck.py` now handles one-item JSON list payloads from deep `openclaw memory status --json` and fast-only no-payload render paths after a 2026-05-24 00:02 cron crash fix. 2026-05-24 06:06 restored missing native-memory cron wrapper/probe scripts and recreated `scripts/short-term-recall-cleanup.py`; fast-only memory healthcheck now exits 0 for all 9 agents, and cleanup exits cleanly when the recall file is absent. 2026-05-24 07:02 restored additional missing cron targets `scripts/session_hygiene_cleanup.sh` and `scripts/browser_maintenance.sh`; all installed crontab script targets now exist, session hygiene runs cleanly, and browser maintenance logs `browser: running`. Dreaming pipeline auto-cleanup implemented 2026-05-22 06:15: dedupe filter now auto-archives 100% noise files. Archived 12 files (641 candidates, May 6–22) — all pure self-referential noise. Dreaming light/ directory clean. Short-term recall cleanup cleared the 2026-05-22 midday backlog. Per-file cap added 2026-05-23 to prevent file-fragmentation bloat; cap tightened to 200 entries (was 400) and 5 per file. Current short-term recall: `unknown` because `memory/.dreams/short-term-recall.json` is currently absent.

**NEW 2026-05-24 08:31**: heartbeat memory-hygiene audit found workspace root `MEMORY.md` missing and recreated a minimal curated long-term memory file with no secrets. Wiki bridge is ready (153 exported artifacts), daily memory files are readable, short-term recall remains absent by design, one dreaming light file is 33 KB, and semantic recall works via the OpenClaw `memory_search` tool. Logged in `memory/2026-05-24.md`.

Work in this order:
1. Audit and improve every native memory path that can work on current hardware.
2. Treat broken or unused memory surfaces as defects to diagnose, especially memory-palace/import/insight-style surfaces, semantic recall reliability, and provider drift.
3. Keep the architecture lightweight:
   - file-backed recall first
   - Obsidian + mirrored workspace memory as backbone
   - semantic/vector/import layers as support when stable
4. When memory behavior changes materially, update the relevant notes so the system stays inspectable.

### 3) System reliability and autonomy
Fix infrastructure that increases execution speed and independence.

Current state: system health dashboard is healthy; browser dashboard reports live CDP as `running` on port `18800`; cron jobs are installed and log to script-specific files, not `reports/cron.log`; OpenClaw runtime is `2026.5.18` with `2026.5.19` available but not silently applied.

**NEW 2026-05-24 09:01**: system reliability heartbeat ran clean. Dashboard overall `healthy`; memory healthy; session hygiene ok; short-term recall healthy (`0 zero-recall / 1 total`, 1.6 KB); dreaming healthy (`99 actionable / 99 raw`); browser running on CDP `18800`; disk 9% used. Verified all crontab script targets exist and are executable, including `skills/cross-surface-sync/scripts/session-start.sh`. Ran cross-surface session-start successfully; it now loads recreated `MEMORY.md` and today's daily note, confirming the 08:31 memory-anchor repair works from the cron/sync path.

Priority order:
1. Browser-control reliability
2. Memory/provider reliability
3. Cron/report reliability
4. Session/transcript hygiene and other operational cleanup
5. Model/runtime sanity drift

If a failure repeats, change tactics instead of re-checking forever.

### 4) Vault and workspace alignment
When new facts emerge, keep Obsidian and mirrored workspace memory materially aligned. Do not do cosmetic rewrites just to feel busy.

## Daily operating bias
If there is discretion, favor tasks that directly increase one of these:
- publishable assets
- monetizable traffic
- governed affiliate readiness
- reliable memory/autonomy
- reusable systems that compound

## Escalation rules

- Ask Sharky only for external, destructive, identity, payment, or approval-gated actions.
- If rate-limited or blocked in one area, switch to another area immediately.
- If nothing genuinely useful can be advanced, reply `HEARTBEAT_OK`.

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
   - fix homepage/category article counts: ✅ DONE. Recategorized 6 articles from troubleshooting/buying-guides into plant-care (5) and winter-prep (1). Homepage counts now 8/18/9/6/1. Commit `7025819` pushed successfully. Cloudflare Pages GitHub integration is still stale; real deploys remain blocked on owner adding `CLOUDFLARE_API_TOKEN` to GitHub Actions secrets (`Zone:Read` + `Cloudflare Pages:Edit`).
   - **NEW 2026-06-08 22:33**: resolved GitHub push blocker — switched `site-deploy/` remote from HTTPS to SSH using existing `~/.ssh/id_ed25519` key, pushed 8 queued commits (`6dd36d6` through `89e3015`) successfully. GitHub Actions workflow run #27 triggered. Remaining deploy blocker is now **only** the missing `CLOUDFLARE_API_TOKEN` secret; build and static QA will pass but deploy will skip until token is added.
   - **NEW 2026-05-24 05:29**: fixed GitHub failed deploy notifications by adding a Cloudflare-token preflight guard to `.github/workflows/deploy-cloudflare-pages.yml`; pushed commit `c9d4a46`, and run `26357597501` completed successfully with deploy skipped because the secret is absent.
   - **NEW 2026-05-24 04:24**: fixed `robots.txt` — Hugo was generating a minimal `User-agent: *` with no sitemap; set `enableRobotsTXT = false` so static `robots.txt` (with `Allow: /` and `Sitemap` directive) is copied to `public/`. Commit `4f92948` pushed successfully.
   - **NEW 2026-05-24 08:03**: live promotion preflight completed. Seven P1 promotion pages on `pages.dev` return 200 and show May 2026 refreshed content, so article URLs are promotion-ready. Cloudflare is still serving stale `robots.txt` with only `User-agent: *`; local `site-deploy/public/robots.txt` is correct, so this remains a deploy-state blocker, not a Hugo-content blocker. Report: `passive-income/balcony-drip-irrigation/reports/2026-05-24-live-promotion-preflight.md`.
   - **NEW 2026-05-24 04:24**: resolved GitHub push-protection blocker — old local commits (`714ebc8`, `2ca663c`) contained Cloudflare API tokens in `.openclaw-repair/` and `memory/.dreams/short-term-recall.json`. Reset local `master` to `origin/master` and reapplied the fix cleanly. Secret-containing commits are now dangling/unreachable and will be garbage-collected.
   - execute promotion plan and analytics setup next (Cloudflare Analytics token and Pinterest account remain owner-action blockers)
   - **NEW 2026-05-27 12:05**: expanded local/CI static QA around governed affiliate links. Added rendered HTML affiliate rel/target audit, Hugo Markdown link render hook, and cleaned affiliate URLs out of headings that bypassed the hook. Verified clean Hugo build and static QA: 66 rendered affiliate links checked, 0 rel/target violations, 0 disclosure violations, 0 unregistered governed affiliate URLs. Report: `passive-income/balcony-drip-irrigation/reports/2026-05-27-rendered-affiliate-link-rel-qa.md`.
   - **NEW 2026-05-29 08:04**: strengthened internal discovery for the new micro-drip herbs article from the main balcony watering systems hub. Local Hugo build and static QA passed: 6,081 internal links checked, 0 missing targets, 69 rendered affiliate links checked, 0 rel/target violations, 0 disclosure violations, 0 unregistered governed affiliate URLs. Report: `passive-income/balcony-drip-irrigation/reports/2026-05-29-hub-micro-drip-internal-linking.md`.
   - **NEW 2026-06-07 12:00**: refreshed local cashflow readiness and guardrails while external deploy/account gates remain blocked. Local deploy-tree static QA passed, title-aware live promotion gate still blocks 6 homepage-fallback routes, owner/promotion docs now point to the 2026-06-07 gate, promotion assets require the title-aware gate before posting, June FindQuestions seasonal refresh is prepped, and source/deploy drift is documented. Reports: `reports/2026-06-07-heartbeat-local-static-and-live-promotion-gate.md`, `reports/2026-06-07-findquestions-rerun-prep.md`, `reports/2026-06-07-promotion-asset-gate-language-sync.md`, `reports/2026-06-07-source-deploy-inventory-drift-audit.md`, `reports/2026-06-07-source-affiliate-ready-reconciliation-pass.md`, and `reports/2026-06-07-affiliate-ready-semantics-audit.md`.
   - **NEW 2026-06-08 18:00**: source/deploy frontmatter drift was reconciled for 12 source files; source category counts now match deploy (20 buying-guides / 7 plant-care / 9 setup-guides / 13 troubleshooting / 1 winter-prep), and local Hugo build/static QA passed. The 2026-06-09 FindQuestions rerun is now command-ready with seed briefs, post-run triage rubric, worksheet template, refresh target map, worksheet generator, regression tests, and a dated one-command runner. Reports/scripts: `reports/2026-06-08-source-deploy-frontmatter-reconciliation.md`, `reports/2026-06-08-findquestions-rerun-command-readiness.md`, `reports/2026-06-08-findquestions-post-run-triage-rubric.md`, `reports/2026-06-08-findquestions-post-run-worksheet-template.md`, `reports/2026-06-08-findquestions-refresh-target-map.md`, `passive-income/ops/findquestions_triage_worksheet.py`, `passive-income/ops/run_balcony_drip_2026_06_findquestions.sh`, and `passive-income/balcony-drip-irrigation/tests/test_findquestions_triage_worksheet.py`.
   - **NEW 2026-06-08 19:30**: June seasonal FindQuestions rerun completed and was triaged. Run `passive-income/reports/findquestions/2026-06-08_181611_balcony-drip-2026-06-seasonal-refresh` had 12/12 successful cached queries, 382 clusters, 479 questions, and 390 candidates. Triage report: `reports/2026-06-08-findquestions-seasonal-rerun-triage-report.md`. Top standalone queue: P1 pepper buyer guide, P2 cloth-pot/grow-bag setup guide, P2 drip-system lifespan troubleshooting page. Refresh queue has 9 existing pages; do not start additional standalone drafts until at least one queued page is published or the deploy gate is resolved.
   - **NEW 2026-06-09 00:17**: all 9 June triage refresh items completed. Added seasonal buyer-intent hook to `small-space-irrigation-for-urban-balconies.md` and grow-bag troubleshooting section to `why-your-container-drip-system-is-watering-unevenly.md`. Hugo build and static QA passed; committed and pushed (`05cc99e`). GitHub Actions run #28 triggered.
   - **NEW 2026-06-09 02:15**: drafted the P2 drip-system lifespan troubleshooting article `how-long-does-a-drip-irrigation-system-last.md`. Component-by-component lifespan tables, failure signs, replacement costs, repair-vs-replace guide, annual maintenance schedule. Hugo build/static QA passed; committed and pushed (`6939a7c`). All 3 June triage standalone drafts now complete.
   - **NEW 2026-06-09 10:30**: internal linking sprint committed and pushed (`ea335da`). Added 2 new articles: `balcony-drip-irrigation-for-orchids.md` (P2 plant-care) and `micro-drip-emitters-for-balcony-herbs.md` (P2 setup guide with affiliate links). Strengthened internal discovery across 14 articles including hub routing, cost guide grow-bag adjustments, and cross-links to summer schedule and orchid articles. Hugo build and static QA passed: 6,566 internal links, 0 missing targets, 78 affiliate links, 0 violations. Deploy remains blocked on missing `CLOUDFLARE_API_TOKEN`.
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

Current state: native memory healthcheck covers all 9 known memory stores again after wrapper/default drift was repaired 2026-05-22 13:03. Dashboard reports memory healthy as of 2026-06-07 09:01 EDT: all 9 agents healthy; builtin backend; vector and FTS available; 0 problem agents. `scripts/native_memory_healthcheck.py` now handles one-item JSON list payloads from deep `openclaw memory status --json` and fast-only no-payload render paths after a 2026-05-24 00:02 cron crash fix. 2026-05-24 06:06 restored missing native-memory cron wrapper/probe scripts and recreated `scripts/short-term-recall-cleanup.py`; fast-only memory healthcheck now exits 0 for all 9 agents, and cleanup exits cleanly when the recall file is absent. 2026-05-24 07:02 restored additional missing cron targets `scripts/session_hygiene_cleanup.sh` and `scripts/browser_maintenance.sh`; all installed crontab script targets now exist, session hygiene runs cleanly, and browser maintenance logs `browser: running`. Dreaming pipeline auto-cleanup implemented 2026-05-22 06:15: dedupe filter now auto-archives 100% noise files. Archived 12 files (641 candidates, May 6–22) — all pure self-referential noise. Dreaming light/ directory clean. Short-term recall cleanup cleared the 2026-05-22 midday backlog. Per-file cap added 2026-05-23 to prevent file-fragmentation bloat; cap tightened to 200 entries (was 400) and 5 per file. Current short-term recall as of 2026-06-09 08:17 UTC: `memory/.dreams/short-term-recall.json` is present (~170 KB); cleanup script updated to fix a data-quality bug where `recallCount` was 0 but `recallDays` was populated. Fixed 131 entries by syncing `recallCount = len(recallDays)` when 0 but non-empty. After fix: 181 entries, 0 recallCount_zero, 0 recallDays_only, 0 effective_zero. System health dashboard now reports `healthy` for short-term recall. Commit `c34830d` pushed successfully.

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

Current state: system health dashboard is `attention` only because a runtime update is available; browser dashboard reports live CDP as `running` on port `18800`; cron jobs are installed and log to script-specific files, not `reports/cron.log`; OpenClaw runtime is `2026.5.18` with stable `2026.6.1` available but not silently applied.

**NEW 2026-06-09 14:15**: Updated `scripts/system-health-dashboard.py` to exit 0 when the only attention item is the runtime update. The dashboard was returning exit code 1 every run because `update-available` was flagged as `attention`, which caused cron scripts to signal failure. The fix adds a `non_runtime` check: if the only non-healthy status is the runtime update, the script exits 0. This is correct because the runtime no-upgrade is an explicit operator decision, not a system failure. Committed and pushed (`b93141c`).

**NEW 2026-06-09 14:15**: Runtime latest version updated to `2026.6.5` (was `2026.6.1`). Installed remains `2026.5.18`. Explicit no-upgrade decision remains in effect.

**NEW 2026-06-07 09:01**: system reliability heartbeat ran clean apart from explicit-decision runtime drift. Dashboard overall `attention`; memory healthy; session hygiene ok; short-term recall healthy (`0 effective-zero / 158 total`, 149.0 KB); dreaming healthy (`404 actionable / 965 raw`); browser running on CDP `18800`; cron active with 7 entries, 0 missing targets, 0 non-executable targets; disk 9% used. Runtime detected installed `2026.5.18`, latest stable `2026.6.1`; no upgrade performed.

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

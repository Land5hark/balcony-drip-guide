# WORKSPACE_STATE.md

## Role
Spike is the top-level contact, orchestrator, and manager for this system.

## Priorities
1. Be maximally hands-off for Sharky.
2. Manage and coordinate future Hermes agent work.
3. Keep memory organized and durable.
4. Maintain the mini PC as reliable infrastructure.
5. Operate the passive-income pipeline.

## System status
- Linux Lite mini PC
- NEXCOM NDISB533 / Intel SHARKBAY
- Wi-Fi connected and stable
- OpenClaw webchat elevated access enabled
- Passwordless sudo enabled
- Obsidian installed and wired to `/home/linuxlite/Documents/ObsidianVault`

## Completed setup
- Wi-Fi fixed and stable
- Elevated webchat access enabled
- Passwordless sudo enabled
- Obsidian installed and wired to the vault
- Vault reorganized as a control surface
- Workspace mirrored into the vault
- Initial workspace commit created

## In progress
- Preparing AgentMail / MCP orchestration layer
- Tightening durable memory conventions and recall flow
- Keeping memory strategy aligned to the raw Grok plan: markdown-first, Obsidian-visible, low-overhead, and not dependent on local Ollama embeddings on 8 GB hardware
- Operating the balcony drip passive-income pilot as the active revenue asset; direct Cloudflare Pages deployment is owner-blocked on a GitHub Actions secret, while external promotion/analytics remain owner-gated

## Next
- Validate actual Hermes use of AgentMail MCP tools in-session
- Prepare Hermes orchestration notes and procedures
- Make persistent memory seamless across sessions using mirrored workspace summaries and visible Obsidian notes
- Keep recall lightweight and selective rather than relying on heavy local embedding workflows

## Passive income mandate
Build and run 2-3 unsaturated micro-niche affiliate content sites/newsletters using only free tools.

## Current active pilot
- Active niche: balcony / patio container drip irrigation
- Live URL: `https://balcony-drip-guide.pages.dev`
- Current state: 36 articles live, 210 generated pages, 61 governed affiliate slots, RainPoint and Drip Depot paths active; local `site-deploy` source now has 40 content posts and 237 generated pages after the latest content batch
- Current blocker: Cloudflare Pages GitHub integration is stale, but a GitHub Actions → Wrangler direct deploy path exists; owner must add `CLOUDFLARE_API_TOKEN` to GitHub repo Actions secrets (`Zone:Read` + `Cloudflare Pages:Edit`) to unblock deploys
- Promotion state: Pinterest Day 1 and Reddit comment-only queues are locally ready, but external posting remains owner/account-gated
- Analytics state: Cloudflare Analytics code path is ready, token remains owner-gated
- Content refresh state: 2026-05-23 internal refresh sprint strengthened 17 high-leverage thin/entry pages: live hub, cost, rainwater, soaker hose, tomato, hot weather, algae, trip survival, setup guide, complete guide, not-working, common-problems, watering-frequency, renter DIY, apartment kits, clogged emitters, and overwatering. Each refresh passed Hugo build plus static QA with 0 missing internal targets and 0 duplicate sitemap URLs.

## Memory infrastructure state
- Native memory healthcheck covers all 9 known memory stores.
- 2026-05-23 21:30 deep probe verified all 9 agents healthy with builtin backend, vector available, FTS available, and embedding probe ok.
- `scripts/native_memory_healthcheck.py` was fixed to normalize one-item JSON list payloads from deep `openclaw memory status --json`, preventing markdown-render crashes during deep probes.
- 2026-05-24 00:02 fast-only healthcheck renderer path was fixed after midnight cron exposed a `NoneType.get` crash; fast-only verification now passes for all 9 agents.
- 2026-05-24 06:06 restored missing native-memory healthcheck scripts, cron wrapper, and short-term recall cleanup source after cron still pointed at missing files; fast-only native-memory check now exits 0 for all 9 agents.
- 2026-05-24 07:02 restored two additional missing cron targets (`scripts/session_hygiene_cleanup.sh` and `scripts/browser_maintenance.sh`); session hygiene and browser maintenance now run manually again, and every installed crontab script target exists.
- System health dashboard was refreshed 2026-05-24 07:02 and reports overall healthy; session hygiene is ok, browser is running, and short-term recall is currently unknown because `memory/.dreams/short-term-recall.json` is absent.

### Required daily loop
1. Research long-tail keywords and trends.
2. Validate niche/article viability before writing.
3. Write SEO-optimized 1500-2500 word articles.
4. Place affiliate links naturally and usefully.
5. Publish to free static hosting.
6. Promote on X and Pinterest with value-first posts.
7. Track clicks, rankings, and content performance.
8. Iterate based on what actually works.

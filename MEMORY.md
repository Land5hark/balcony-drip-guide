# MEMORY.md

Curated long-term memory for the main OpenClaw workspace. Keep this distilled: durable operating facts, decisions, active projects, and lessons that should survive session restarts. Do not store secrets here.

## Active Mission

- Primary workstream: build reliable memory/autonomy infrastructure and a revenue-producing passive-income pipeline for Sharky.
- Current revenue focus: balcony / patio container drip irrigation. Aquarium ATO is parked unless a clearly better affiliate or distribution path revives it.
- Operating bias: ship useful assets, fix blockers, verify facts, and keep the workspace/vault state inspectable.

## Passive Income

- Standard site architecture is Hugo + GitHub source control + Cloudflare Pages, with editorial-first affiliate content and 16+ articles before monetization push.
- Balcony drip guide source lives under `passive-income/balcony-drip-irrigation/`.
- Live target is `https://balcony-drip-guide.pages.dev`; GitHub staging is `https://land5hark.github.io/balcony-drip-guide/`.
- RainPoint and Drip Depot affiliate programs are active. Disclosure and product claims must stay governed and verified.
- As of 2026-05-24, seven P1 promotion pages on `pages.dev` return 200 and show May 2026 refreshed content.
- Cloudflare deploys remain owner-gated on adding `CLOUDFLARE_API_TOKEN` to GitHub Actions secrets. The workflow now skips deploy cleanly when the secret is absent.
- Local robots output is correct, but Cloudflare still serves stale `robots.txt` with only `User-agent: *`; treat this as a deploy-state blocker, not a Hugo-content blocker.
- Promotion account actions remain owner-gated: X identity, Pinterest business account/boards, and analytics token.

## Memory And System

- Native memory healthchecks cover 9 known memory stores and were healthy as of 2026-05-24.
- Wiki bridge is enabled in bridge vault mode with Obsidian CLI available. It is the durable mirrored knowledge backbone alongside workspace files.
- Short-term recall may be absent; cleanup scripts should exit cleanly when `memory/.dreams/short-term-recall.json` does not exist.
- Dreaming pipeline cleanup is expected to archive pure self-referential noise and keep actionable files small.
- Cron jobs log to script-specific files rather than a single `reports/cron.log`.
- Browser control is expected on CDP port `18800` when healthy.

## Lessons

- Content can advance even when deployment is blocked. Keep drafting, refreshing, and preparing promotion packets while external deployment/account gates wait on owner action.
- When a CLI command in a skill fails, check current CLI help or tool alternatives before treating the subsystem as broken.
- Do not put secrets, tokens, or raw credentials into memory, reports, dreams, recall files, or git history.

- Lane: deployment reliability / autonomy
- Status: pass completed
- Scope: add a reusable deployment preflight script for the balcony drip GitHub Pages site so the eventual public push is safer and faster
- Timestamp: 2026-05-05 14:17 EDT

## Work performed
1. Added `site/scripts/deployment_preflight.py`.
2. Made the script executable and ran it locally.
3. Updated `site/README.md` so the preflight command is discoverable.
4. Updated the GitHub Pages deployment runbook to use the script instead of a loose manual command list.

## What the script checks
- current git working-tree summary
- future-dated live posts that Hugo would silently exclude
- local `hugo --minify` build health
- built post count in `public/posts/`

## Local test result
The script passed on the current site state and reported:
- branch `main...origin/main`
- `19` changed/untracked paths in the working tree
- `0` future-dated live posts across `16` live post files
- Hugo build passed
- `16` built post directories in `public/posts`

## Why this matters
The biggest remaining public-site blocker is still the eventual owner-approved push, but this strips out some of the avoidable deployment slop:
- fewer chances to forget the future-date gotcha
- fewer chances to push without a fresh build
- one repeatable preflight command instead of a memory game

## Artifacts updated
- `passive-income/balcony-drip-irrigation/site/scripts/deployment_preflight.py`
- `passive-income/balcony-drip-irrigation/site/README.md`
- `passive-income/balcony-drip-irrigation/reports/2026-05-05-github-pages-deployment-runbook.md`

## Outcome
This does not remove the owner approval gate for the live push, but it does make the eventual deployment step more reliable and more autonomous once approval exists.

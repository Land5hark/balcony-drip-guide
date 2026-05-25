# Repository Status

Last updated: 2026-05-11

## Overview

The passive-income workspace has a split repository structure. This document tracks the status of each.

## Repository: `nano-tank-ato-reliability` (Workspace)

**Status:** ⚠️ **ARCHIVED / READ-ONLY**

**Issue discovered:** 2026-05-11

**Impact:**
- Cannot push new commits to workspace repository
- Workspace-level files (drafts, reports, research) cannot be synced to GitHub
- Site-specific content must be committed directly to site repository

**Workaround:**
- Site repository (`balcony-drip-guide`) remains active and pushable
- All Hugo content, static assets, and site configs go to site repo
- Workspace files stay local-only until repo unarchived or migrated

**Action required:**
- Either unarchive the workspace repo via GitHub settings
- Or migrate workspace content to a new active repository

---

## Repository: `balcony-drip-guide` (Site)

**Status:** ✅ **ACTIVE**

**URL:** https://github.com/Land5hark/balcony-drip-guide

**Deployment:** GitHub Pages (active)

**Current content:**
- 21 articles published
- 158 pages total (includes taxonomy, section, hub pages)
- 5 static files (3 promotion pins + existing assets)
- All trust pages live

**Last commit:** 2026-05-11 - README update with current state

---

## Repository: `balcony-drip-guide` (Cloudflare Pages - pending)

**Status:** ⏳ **NOT YET CONFIGURED**

**Target:** https://balcony-drip-guide.pages.dev/

**Blocker:** Requires Cloudflare dashboard access to connect GitHub repo

**Benefits of migration:**
- Cleaner `*.pages.dev` URL (vs github.io)
- Better CDN performance
- Native Cloudflare Analytics
- Closer to standard site template

---

## Operational Notes

### What's working
- Site builds clean (Hugo 0.125.4)
- GitHub Pages deployment active
- All 21 articles live and indexed
- Promotion assets committed and deployed

### What's blocked
- Workspace repo pushes (archived)
- Drip Depot affiliate monetization (owner action)
- Cloudflare Pages migration (dashboard access)

### Recommended priority
1. **Unarchive workspace repo** OR create new active workspace repo
2. Complete Drip Depot affiliate application
3. Migrate to Cloudflare Pages for cleaner URLs

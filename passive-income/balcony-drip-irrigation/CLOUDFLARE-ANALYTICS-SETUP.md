# Cloudflare Analytics Setup Guide

**For**: Sharky (owner)  
**Site**: Balcony Drip Guide (https://balcony-drip-guide.pages.dev)  
**Prepared**: 2026-05-17 08:15 UTC  
**Blocking**: Traffic monitoring and performance optimization

---

## Why This Matters

Without analytics, we cannot:
- Track which articles drive traffic
- Measure affiliate link click-through rates
- Identify content refresh opportunities
- Validate the passive income model with data

---

## Setup Steps (5 minutes)

### Step 1: Get Your Analytics Token

1. Go to https://dash.cloudflare.com
2. Navigate to **Pages** → **balcony-drip-guide**
3. Click **Analytics** tab
4. Look for "Web Analytics" section
5. Copy the **JavaScript snippet** or **token**

Alternative path if using Cloudflare Web Analytics (recommended):
1. Go to https://dash.cloudflare.com
2. Click **Analytics & Logs** in left sidebar
3. Select **Web Analytics**
4. Click **Add a site**
5. Enter: `balcony-drip-guide.pages.dev`
6. Copy the provided beacon token (looks like: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)

### Step 2: Add Token to Config

File to edit: `passive-income/balcony-drip-irrigation/site/config.toml`

Add this section at the end of the file:

```toml
[params.cloudflare_analytics]
  token = "YOUR_TOKEN_HERE"
  enabled = true
```

### Step 3: Verify Deployment

After pushing changes:
1. Wait 2-3 minutes for Cloudflare Pages to rebuild
2. Visit https://balcony-drip-guide.pages.dev
3. Open browser DevTools → Network tab
4. Look for requests to `cloudflareinsights.com` or similar
5. Check that beacon is firing (200 OK response)

### Step 4: Confirm Data Flow

1. Return to Cloudflare Dashboard → Analytics
2. Wait 5-10 minutes for first data points
3. Verify pageviews are being recorded

---

## Current State

| Component | Status |
|-----------|--------|
| Articles published | 36 ✅ |
| Affiliate links active | 61 ✅ |
| Drip Depot approved | 2026-05-14 ✅ |
| RainPoint approved | 2026-05-08 ✅ |
| Analytics integration code | ✅ DEPLOYED (2026-05-17) |
| **Analytics token** | **❌ NEEDED from Sharky** |
| Traffic data | ❌ Waiting |

---

## Expected Timeline

- **Week 1-2**: Baseline traffic establishment
- **Week 3-4**: First affiliate click data
- **Month 2-3**: Conversion patterns emerge
- **Month 3**: Model validation complete

---

## Next Actions After Setup

1. **Spike**: Begin weekly traffic reports
2. **Spike**: Monitor affiliate dashboards for clicks
3. **Joint**: Review performance after 30 days of data
4. **Joint**: Decide on content refresh priorities

---

*This unblocks the performance monitoring framework. Site is ready for traffic.*

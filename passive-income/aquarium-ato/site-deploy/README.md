# Nano Tank ATO Reliability — Deployment-Ready Package

## Status
This site was previously deployed to `nano-tank-ato-reliability.pages.dev` but the GitHub repo (`Land5hark/nano-tank-ato-reliability`) is now archived/read-only. Local improvements (build fingerprinting, Cloudflare analytics) are committed but cannot be pushed.

## What's in this package
- Hugo static site source (7 articles, search page, affiliate disclosure)
- Pre-built `public/` directory (ready for immediate deployment)
- GitHub Actions workflow for Cloudflare Pages deployment
- Cloudflare analytics token already configured in `config.toml`

## Revival instructions

### Option 1: Create new GitHub repo + connect to existing Cloudflare Pages project

1. **Create a new GitHub repo**: `Land5hark/nano-tank-ato-reliability-v2` (or any name)
2. **Push this directory to the new repo**:
   ```bash
   cd site-deploy
   git init
   git add -A
   git commit -m "Initial commit"
   git branch -M master
   git remote add origin https://github.com/Land5hark/nano-tank-ato-reliability-v2.git
   git push -u origin master
   ```
3. **Update Cloudflare Pages**: Dashboard → Pages → `nano-tank-ato-reliability` → Settings → Build → Connect to new repo
4. **Add API token to GitHub** (if using GitHub Actions workflow):
   - Cloudflare dashboard → My Profile → API Tokens → Create token
   - Permissions: Account: Cloudflare Pages: Edit
   - GitHub repo → Settings → Secrets → Add `CLOUDFLARE_API_TOKEN`

### Option 2: Deploy directly from this directory

If GitHub integration continues to fail, deploy manually:
```bash
cd site-deploy
wrangler pages deploy public --project-name=nano-tank-ato-reliability --branch=master
```

## Site details
- **URL**: https://nano-tank-ato-reliability.pages.dev/
- **Articles**: 7
- **Analytics**: Cloudflare Web Analytics token `ceb6dbd4f5474c87a1fea52dbf83cf30` active
- **Build fingerprinting**: Enabled (shows branch and commit SHA in footer)
- **Affiliate**: Drip Depot links active

## Content articles
1. ATO Failure Modes (Flood, Salinity, Crash)
2. ATO Maintenance Schedule for Nano Tanks
3. Best ATO Systems for Nano Reef Tanks Under 20 Gallons
4. Float Switch vs Optical Sensor for Nano Tanks
5. How Big Should Your ATO Reservoir Be
6. How to Stop False ATO Alarms in Small Tanks
7. Why Your ATO Keeps Overfilling a Nano Tank

# GitHub Actions Deployment Workflow

## Problem
Cloudflare Pages auto-deploy from GitHub integration has stopped working. Pushes to `master` are not triggering builds.

## Solution
This GitHub Actions workflow deploys directly to Cloudflare Pages using wrangler.

## Setup required (one-time, owner action)

1. Go to Cloudflare dashboard → My Profile → API Tokens
2. Create a new token with these permissions:
   - Account: Cloudflare Pages: Edit
   - Zone (if using custom domain): Zone: Read, Page Rules: Edit
3. Copy the token value
4. Go to GitHub repo → Settings → Secrets and variables → Actions
5. Add a new repository secret:
   - Name: `CLOUDFLARE_API_TOKEN`
   - Value: the token from step 2
6. Push any change to `master` or trigger the workflow manually

## What the workflow does

1. Checks out the repo
2. Builds the Hugo site from a clean destination directory (same as local `hugo --gc --minify --cleanDestinationDir`)
3. Runs `python3 scripts/qa_static_build.py` to catch broken internal links, duplicate sitemap URLs, unknown article categories, stale generated category archives, disabled affiliate disclosures, and unregistered governed affiliate URLs
4. Runs `python3 -m unittest discover -s tests -p 'test_*.py' -v` to protect the title-aware promotion URL verifier without depending on live network state
5. Deploys the `public/` directory to Cloudflare Pages using wrangler
6. Uses branch=`master` and project=`balcony-drip-guide`

If `CLOUDFLARE_API_TOKEN` is missing, steps 1-4 still run and the deploy is skipped with a GitHub Actions notice.

## Fallback option

If Cloudflare Pages continues to have issues, the workflow can be modified to deploy to GitHub Pages instead by changing the deploy step.

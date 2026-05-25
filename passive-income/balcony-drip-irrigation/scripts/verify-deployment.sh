#!/bin/bash
# Deployment Verification Script for Balcony Drip Guide
# Checks live site against expected state and logs results

set -euo pipefail

SITE_URL="https://balcony-drip-guide.pages.dev"
REPO_DIR="/home/linuxlite/.openclaw/workspace/passive-income/balcony-drip-irrigation/site-deploy"
LOG_FILE="/home/linuxlite/.openclaw/workspace/passive-income/balcony-drip-irrigation/reports/deployment-verification.log"
REPORT_FILE="/home/linuxlite/.openclaw/workspace/reports/balcony-drip-deployment-status.json"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
GIT_COMMIT=$(cd "$REPO_DIR" && git rev-parse --short HEAD 2>/dev/null || echo "unknown")
GIT_BRANCH=$(cd "$REPO_DIR" && git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")

# Expected values (from config.toml)
EXPECTED_COUNTS=(6 19 13 1 0)
ROBOTS_EXPECTED="Updated 2026-05-21"
HOT_WEATHER_PATH="/posts/how-to-adjust-balcony-drip-irrigation-for-hot-weather/"

# Function to log with timestamp
log() {
    echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}

# Check category counts
log "--- Deployment Verification Start ---"
log "Git commit: $GIT_COMMIT (branch: $GIT_BRANCH)"

HOME_HTML=$(curl -s "$SITE_URL" || true)
COUNTS_RAW=$(printf '%s' "$HOME_HTML" | grep -o "cat-card__count>[0-9]* articles" | sed 's/cat-card__count>//;s/ articles//' || true)
COUNTS=($COUNTS_RAW)

COUNTS_OK=true
if [ ${#COUNTS[@]} -eq 0 ]; then
    log "ERROR: Could not extract category counts from live site"
    COUNTS_OK=false
else
    for i in "${!EXPECTED_COUNTS[@]}"; do
        if [ "${COUNTS[$i]:-0}" != "${EXPECTED_COUNTS[$i]}" ]; then
            log "MISMATCH: Category $i expected ${EXPECTED_COUNTS[$i]}, got ${COUNTS[$i]:-N/A}"
            COUNTS_OK=false
        fi
    done
fi

if [ "$COUNTS_OK" = true ]; then
    log "PASS: Category counts match expected values (${EXPECTED_COUNTS[*]})"
fi

# Check build fingerprint so stale deploys are easy to identify from logs
LOCAL_FINGERPRINT=$(grep -o 'data-build-fingerprint="[^"]*"' "$REPO_DIR/public/index.html" 2>/dev/null | head -1 | sed 's/data-build-fingerprint="//;s/"//' || true)
LIVE_FINGERPRINT=$(printf '%s' "$HOME_HTML" | grep -o 'data-build-fingerprint="[^"]*"' | head -1 | sed 's/data-build-fingerprint="//;s/"//' || true)
FINGERPRINT_OK=false
if [ -n "$LOCAL_FINGERPRINT" ] && [ "$LOCAL_FINGERPRINT" = "$LIVE_FINGERPRINT" ]; then
    FINGERPRINT_OK=true
    log "PASS: Live build fingerprint matches local public/ build ($LIVE_FINGERPRINT)"
else
    log "FAIL: Live build fingerprint mismatch. local=${LOCAL_FINGERPRINT:-missing} live=${LIVE_FINGERPRINT:-missing}"
fi

# Check robots.txt
ROBOTS_CONTENT=$(curl -s "$SITE_URL/robots.txt" | head -1 || true)
ROBOTS_OK=false
if echo "$ROBOTS_CONTENT" | grep -q "$ROBOTS_EXPECTED"; then
    ROBOTS_OK=true
    log "PASS: robots.txt contains expected header"
else
    log "FAIL: robots.txt does not contain expected header. Got: ${ROBOTS_CONTENT:-EMPTY}"
fi

# Check for new article (hot weather) by direct URL, not homepage placement
HOT_WEATHER_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$SITE_URL$HOT_WEATHER_PATH" || true)
if [ "$HOT_WEATHER_STATUS" = "200" ]; then
    log "PASS: Hot weather article URL is live"
    HOT_WEATHER_OK=true
else
    log "FAIL: Hot weather article URL returned HTTP ${HOT_WEATHER_STATUS:-000}"
    HOT_WEATHER_OK=false
fi

# Generate JSON report
DEPLOYMENT_STATUS="healthy"
if [ "$COUNTS_OK" = false ] || [ "$ROBOTS_OK" = false ] || [ "$FINGERPRINT_OK" = false ] || [ "$HOT_WEATHER_OK" = false ]; then
    DEPLOYMENT_STATUS="stale"
fi

if [ ${#COUNTS[@]} -gt 0 ]; then
    ACTUAL_COUNTS_JSON=$(IFS=,; echo "${COUNTS[*]}")
else
    ACTUAL_COUNTS_JSON=""
fi

cat > "$REPORT_FILE" <<EOF
{
  "timestamp": "$TIMESTAMP",
  "git_commit": "$GIT_COMMIT",
  "git_branch": "$GIT_BRANCH",
  "site_url": "$SITE_URL",
  "checks": {
    "category_counts": {
      "expected": [$(IFS=,; echo "${EXPECTED_COUNTS[*]}")],
      "actual": [$ACTUAL_COUNTS_JSON],
      "status": "$([ "$COUNTS_OK" = true ] && echo "pass" || echo "fail")"
    },
    "build_fingerprint": {
      "expected": "$LOCAL_FINGERPRINT",
      "actual": "$LIVE_FINGERPRINT",
      "status": "$([ "$FINGERPRINT_OK" = true ] && echo "pass" || echo "fail")"
    },
    "robots_txt": {
      "status": "$([ "$ROBOTS_OK" = true ] && echo "pass" || echo "fail")"
    },
    "hot_weather_article": {
      "http_status": "$HOT_WEATHER_STATUS",
      "status": "$([ "$HOT_WEATHER_OK" = true ] && echo "pass" || echo "fail")"
    }
  },
  "deployment_status": "$DEPLOYMENT_STATUS",
  "action_required": "$([ "$DEPLOYMENT_STATUS" = "stale" ] && echo "Cloudflare Pages auto-deploy may be broken. Check dashboard." || echo "none")"
}
EOF

log "Deployment status: $DEPLOYMENT_STATUS"
log "Report saved to: $REPORT_FILE"
log "--- Verification Complete ---"

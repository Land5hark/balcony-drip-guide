#!/usr/bin/env bash
set -euo pipefail
cd /home/linuxlite/.openclaw/workspace/passive-income/aquarium-ato
hermes chat -Q --accept-hooks --yolo --source tool -q "You are operating the aquarium ATO passive-income content pipeline. Review README.md, rules.md, topics.csv, products.csv, templates/, and any files in drafts/. Create or update morning-review.md with: what was produced, what needs fact verification, what is closest to publish-ready, what missing infrastructure still blocks publishing, and the next 3 highest-value actions. Do not publish or post externally." > package-review-latest.txt

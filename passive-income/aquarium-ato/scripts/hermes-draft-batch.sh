#!/usr/bin/env bash
set -euo pipefail
cd /home/linuxlite/.openclaw/workspace/passive-income/aquarium-ato
hermes chat -Q --accept-hooks --yolo --source tool -q "You are operating the aquarium ATO passive-income content pipeline. Review README.md, rules.md, topics.csv, products.csv, and templates/ in the current directory. Generate draft packages for the top 2 queued topics only. For each topic create a markdown file in drafts/ named after the slug with: title, intent, outline, section bullets, internal links, FAQ ideas, and a claims-requiring-verification checklist. Do not fabricate hands-on testing or exact specs. If product facts are missing, write around the missing facts carefully and flag them." > draft-batch-latest.txt

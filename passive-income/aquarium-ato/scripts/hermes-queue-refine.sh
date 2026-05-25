#!/usr/bin/env bash
set -euo pipefail
cd /home/linuxlite/.openclaw/workspace/passive-income/aquarium-ato
hermes chat -Q --accept-hooks --yolo --source tool -q "You are operating the aquarium ATO passive-income content pipeline. Review README.md, rules.md, topics.csv, and products.csv in the current directory. Refine the first 10 queued topics for sequencing and execution readiness. Add short execution notes for each queued topic in a new file named queue-notes.md. Do not publish anything. Do not invent product facts. Focus on prioritization, risk notes, and what needs verification first." > queue-refine-latest.txt

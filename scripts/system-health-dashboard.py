#!/usr/bin/env python3
"""
System Health Dashboard - Daily Status Report Generator
Integrates native memory health, session hygiene, and browser status
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/linuxlite/.openclaw/workspace")
REPORTS_DIR = WORKSPACE / "reports"
DASHBOARD_FILE = REPORTS_DIR / "system-health-dashboard.json"
LOG_FILE = REPORTS_DIR / "system-health.log"
NATIVE_MEMORY_MAX_AGE_SECONDS = 8 * 60 * 60
SESSION_HYGIENE_MAX_AGE_SECONDS = 8 * 60 * 60
DISK_WARNING_PERCENT = 85
DISK_CRITICAL_PERCENT = 90

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def check_native_memory():
    """Check latest native memory health snapshot"""
    latest = REPORTS_DIR / "native-memory-health" / "latest.json"
    if not latest.exists():
        return {"status": "unknown", "error": "No health snapshot found"}
    
    try:
        with open(latest) as f:
            data = json.load(f)
        
        if isinstance(data.get("ok_agents"), list) or isinstance(data.get("problem_agents"), list):
            healthy_agents = data.get("ok_agents", [])
            problem_agents = data.get("problem_agents", [])
        else:
            healthy_agents = []
            problem_agents = []
            for agent, result in data.get("agents", {}).items():
                if result.get("status") == "ok":
                    healthy_agents.append(agent)
                else:
                    problem_agents.append(agent)

        generated_at_epoch = data.get("generated_at_epoch")
        age_seconds = None
        if isinstance(generated_at_epoch, (int, float)):
            age_seconds = max(0, int(time.time() - generated_at_epoch))

        if not healthy_agents and not problem_agents:
            status = "unknown"
        elif problem_agents:
            status = "degraded"
        elif age_seconds is None or age_seconds > NATIVE_MEMORY_MAX_AGE_SECONDS:
            status = "stale"
        else:
            status = "healthy"
        
        return {
            "status": status,
            "healthy_agents": healthy_agents,
            "problem_agents": problem_agents,
            "total_agents": len(healthy_agents) + len(problem_agents),
            "age_seconds": age_seconds
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def check_session_hygiene():
    """Check last session hygiene run"""
    hygiene_log = REPORTS_DIR / "session-hygiene.log"
    if not hygiene_log.exists():
        return {"status": "unknown", "last_run": None}
    
    try:
        with open(hygiene_log) as f:
            lines = f.readlines()
        
        # Find last completed entry
        for line in reversed(lines):
            if "completed:" in line:
                parts = line.strip().split("]")
                if len(parts) >= 2:
                    timestamp = parts[0][1:]  # Remove leading [
                    normalized = timestamp[:-4] if timestamp.endswith(" EDT") else timestamp
                    parsed = datetime.strptime(normalized, "%Y-%m-%d %H:%M:%S")
                    age_seconds = max(0, int((datetime.now() - parsed).total_seconds()))
                    status = "ok" if age_seconds <= SESSION_HYGIENE_MAX_AGE_SECONDS else "stale"
                    return {"status": status, "last_run": timestamp, "age_seconds": age_seconds}
        
        return {"status": "unknown", "last_run": None}
    except Exception as e:
        return {"status": "error", "error": str(e)}

def check_dreaming_backlog():
    """Check dreaming pipeline backlog status"""
    dreaming_dir = WORKSPACE / "memory" / "dreaming" / "light"
    if not dreaming_dir.exists():
        return {"status": "unknown", "files": 0, "candidates": 0}
    
    try:
        files = sorted(dreaming_dir.glob("2026-[0-9][0-9]-[0-9][0-9].md"))
        total_candidates = 0
        actionable_candidates = 0
        per_file = []
        reviewed_files = 0
        
        for f in files:
            with open(f) as fp:
                content = fp.read()
            candidates = content.count("- Candidate:")
            date_str = f.stem
            dedupe_report = REPORTS_DIR / f"dreaming-dedupe-{date_str}.json"
            unique = None
            if dedupe_report.exists():
                try:
                    with open(dedupe_report) as fp:
                        unique = json.load(fp).get("unique")
                    reviewed_files += 1
                except Exception:
                    unique = None

            total_candidates += candidates
            actionable = unique if isinstance(unique, int) else candidates
            actionable_candidates += actionable
            item = {"file": f.name, "candidates": candidates, "actionable": actionable}
            if unique is not None:
                item["deduped"] = True
            per_file.append(item)
        
        return {
            "status": "healthy" if actionable_candidates < 500 else "backlogged",
            "files": len(files),
            "candidates": total_candidates,
            "actionable_candidates": actionable_candidates,
            "reviewed_files": reviewed_files,
            "largest_files": sorted(per_file, key=lambda item: item["actionable"], reverse=True)[:5]
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def effective_recall_count(entry: dict) -> int:
    """Return the best-available recall count, falling back to recallDays length."""
    rc = int(entry.get("recallCount") or 0)
    if rc > 0:
        return rc
    rd = len(entry.get("recallDays") or [])
    return rd


def check_short_term_recall():
    """Check short-term recall accumulation"""
    recall_file = WORKSPACE / "memory" / ".dreams" / "short-term-recall.json"
    if not recall_file.exists():
        return {
            "status": "unknown",
            "entries": 0,
            "zero_recall": 0,
            "effective_zero_recall": 0,
            "raw_recall_count_zero": 0,
            "recall_days_only": 0,
        }
    
    try:
        with open(recall_file) as f:
            data = json.load(f)
        
        entries = data.get("entries", {})
        total = len(entries)
        effective_zero_recall = sum(
            1 for e in entries.values() if effective_recall_count(e) == 0
        )
        raw_recall_count_zero = sum(
            1 for e in entries.values() if int(e.get("recallCount") or 0) == 0
        )
        recall_days_only = sum(
            1
            for e in entries.values()
            if int(e.get("recallCount") or 0) == 0 and len(e.get("recallDays") or []) > 0
        )
        source_breakdown = {}
        zero_recall_breakdown = {}
        for entry in entries.values():
            path = entry.get("path", "")
            if "memory/.dreams/session-corpus/" in path:
                source_class = "session_corpus"
            elif "memory/.dreams/" in path:
                source_class = "dreams"
            elif path.startswith("memory/"):
                source_class = "daily_memory"
            else:
                source_class = "other"
            source_breakdown[source_class] = source_breakdown.get(source_class, 0) + 1
            if effective_recall_count(entry) == 0:
                zero_recall_breakdown[source_class] = zero_recall_breakdown.get(source_class, 0) + 1
        
        # Flag if >80% are zero-recall or total is very large
        # Adjusted for tightened 8GB mini PC thresholds (cap=200, per_file=5)
        status = "healthy"
        if total > 400:
            status = "backlogged"
        elif total > 0 and effective_zero_recall / total > 0.8:
            status = "attention"
        
        return {
            "status": status,
            "entries": total,
            # Retain zero_recall for compatibility with existing dashboard consumers.
            "zero_recall": effective_zero_recall,
            "effective_zero_recall": effective_zero_recall,
            "raw_recall_count_zero": raw_recall_count_zero,
            "recall_days_only": recall_days_only,
            "source_breakdown": source_breakdown,
            "zero_recall_breakdown": zero_recall_breakdown,
            "file_size_kb": round(recall_file.stat().st_size / 1024, 1)
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def check_browser_status():
    """Check if browser control is available"""
    try:
        version = subprocess.run(
            ["curl", "-fsS", "http://localhost:18800/json/version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if version.returncode == 0 and version.stdout:
            browser = json.loads(version.stdout)
            tabs = subprocess.run(
                ["curl", "-fsS", "http://localhost:18800/json"],
                capture_output=True,
                text=True,
                timeout=5
            )
            page_count = 0
            if tabs.returncode == 0 and tabs.stdout:
                page_count = sum(1 for tab in json.loads(tabs.stdout) if tab.get("type") == "page")
            return {
                "status": "running",
                "cdp_port": 18800,
                "browser": browser.get("Browser"),
                "page_targets": page_count
            }
        return {"status": "standby", "note": "Browser available on-demand"}
    except Exception:
        return {"status": "standby", "note": "Browser available on-demand"}

def check_cron_status():
    """Check installed cron entries and referenced local script targets."""
    try:
        result = subprocess.run(
            ["crontab", "-l"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode != 0:
            return {"status": "missing", "error": result.stderr.strip() or "No crontab installed"}

        entries = []
        missing_targets = []
        non_executable_targets = []
        for line in result.stdout.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            entries.append(stripped)
            for token in stripped.split():
                candidate = token.rstrip(";")
                if not candidate.startswith("/home/linuxlite/.openclaw/workspace/"):
                    continue
                path = Path(candidate)
                if not path.exists():
                    missing_targets.append(candidate)
                elif not os.access(path, os.X_OK):
                    non_executable_targets.append(candidate)

        if not entries:
            status = "missing"
        elif missing_targets or non_executable_targets:
            status = "degraded"
        else:
            status = "active"

        return {
            "status": status,
            "entries": len(entries),
            "missing_targets": sorted(set(missing_targets)),
            "non_executable_targets": sorted(set(non_executable_targets))
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def check_disk_status():
    """Check workspace filesystem capacity."""
    try:
        result = subprocess.run(
            ["df", "-P", str(WORKSPACE)],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode != 0:
            return {"status": "error", "error": result.stderr.strip() or "df failed"}

        lines = result.stdout.strip().splitlines()
        if len(lines) < 2:
            return {"status": "error", "error": "Unexpected df output"}

        fields = lines[-1].split()
        if len(fields) < 6:
            return {"status": "error", "error": "Unexpected df fields"}

        used_percent = int(fields[4].rstrip("%"))
        if used_percent > DISK_CRITICAL_PERCENT:
            status = "critical"
        elif used_percent > DISK_WARNING_PERCENT:
            status = "warning"
        else:
            status = "ok"

        return {
            "status": status,
            "filesystem": fields[0],
            "used_percent": used_percent,
            "available_kb": int(fields[3]),
            "mountpoint": fields[5]
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def check_runtime_status():
    """Check installed OpenClaw version and non-invasive update availability."""
    try:
        version = subprocess.run(
            ["openclaw", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if version.returncode != 0:
            return {"status": "error", "error": version.stderr.strip() or "openclaw --version failed"}

        installed = version.stdout.strip().split()
        installed_version = installed[1] if len(installed) >= 2 else version.stdout.strip()

        update = subprocess.run(
            ["openclaw", "update", "status", "--json"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if update.returncode != 0:
            return {
                "status": "unknown",
                "installed_version": installed_version,
                "error": update.stderr.strip() or "openclaw update status --json failed"
            }

        data = json.loads(update.stdout)
        availability = data.get("availability", {})
        latest_version = availability.get("latestVersion")
        status = "update-available" if availability.get("available") else "current"
        return {
            "status": status,
            "installed_version": installed_version,
            "latest_version": latest_version,
            "channel": data.get("channel", {}).get("label"),
            "has_registry_update": availability.get("hasRegistryUpdate"),
            "has_git_update": availability.get("hasGitUpdate")
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def generate_dashboard():
    """Generate comprehensive health dashboard"""
    now = datetime.now().isoformat()
    
    dashboard = {
        "generated_at": now,
        "summary": {
            "memory": check_native_memory(),
            "session_hygiene": check_session_hygiene(),
            "dreaming_pipeline": check_dreaming_backlog(),
            "short_term_recall": check_short_term_recall(),
            "browser": check_browser_status(),
            "cron": check_cron_status(),
            "disk": check_disk_status(),
            "runtime": check_runtime_status()
        }
    }
    
    # Determine overall status
    statuses = [
        dashboard["summary"]["memory"]["status"],
        dashboard["summary"]["session_hygiene"]["status"],
        dashboard["summary"]["dreaming_pipeline"]["status"],
        dashboard["summary"]["short_term_recall"]["status"],
        dashboard["summary"]["browser"]["status"],
        dashboard["summary"]["cron"]["status"],
        dashboard["summary"]["disk"]["status"],
        dashboard["summary"]["runtime"]["status"]
    ]
    
    if any(s in ["error", "degraded", "critical"] for s in statuses):
        dashboard["overall_status"] = "degraded"
    elif any(s in ["attention", "backlogged", "stale", "standby", "unknown", "warning"] for s in statuses):
        dashboard["overall_status"] = "attention"
    elif any(s == "update-available" for s in statuses):
        dashboard["overall_status"] = "attention"
    else:
        dashboard["overall_status"] = "healthy"
    
    # Save dashboard
    with open(DASHBOARD_FILE, "w") as f:
        json.dump(dashboard, f, indent=2)
    
    return dashboard

def main():
    log("Starting system health dashboard generation")
    
    # Ensure reports directory exists
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    dashboard = generate_dashboard()
    
    log(f"Overall status: {dashboard['overall_status']}")
    log(f"Memory: {dashboard['summary']['memory']['status']}")
    log(f"Session hygiene: {dashboard['summary']['session_hygiene']['status']}")
    
    recall = dashboard["summary"]["short_term_recall"]
    log(
        f"Short-term recall: {recall['status']} "
        f"({recall.get('effective_zero_recall', recall.get('zero_recall', 0))} effective-zero / "
        f"{recall.get('entries', 0)} total entries, "
        f"{recall.get('recall_days_only', 0)} recallDays-only, "
        f"{recall.get('file_size_kb', 0)} KB)"
    )
    dreaming = dashboard["summary"]["dreaming_pipeline"]
    log(
        f"Dreaming pipeline: {dreaming['status']} "
        f"({dreaming.get('actionable_candidates', dreaming.get('candidates', 0))} actionable / "
        f"{dreaming.get('candidates', 0)} raw candidates)"
    )
    log(f"Browser: {dashboard['summary']['browser']['status']}")
    cron = dashboard["summary"]["cron"]
    log(
        f"Cron: {cron['status']} "
        f"({cron.get('entries', 0)} entries, "
        f"{len(cron.get('missing_targets', []))} missing targets, "
        f"{len(cron.get('non_executable_targets', []))} non-executable targets)"
    )
    disk = dashboard["summary"]["disk"]
    log(f"Disk: {disk['status']} ({disk.get('used_percent', 'unknown')}% used)")
    runtime = dashboard["summary"]["runtime"]
    log(
        f"Runtime: {runtime['status']} "
        f"(installed {runtime.get('installed_version', 'unknown')}, "
        f"latest {runtime.get('latest_version', 'unknown')})"
    )
    
    log("Dashboard saved to " + str(DASHBOARD_FILE))
    log("Complete")
    
    # Exit 0 if healthy or if the only attention item is a known runtime update.
    # Runtime updates are explicitly deferred by operator decision; do not
    # signal a cron failure for a known-accepted state.
    if dashboard["overall_status"] == "healthy":
        return 0
    if dashboard["overall_status"] == "attention":
        accepted = {"healthy", "ok", "current", "running", "active"}
        non_runtime = [
            k for k, v in dashboard["summary"].items()
            if k != "runtime" and v.get("status") not in accepted
        ]
        if not non_runtime:
            return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())

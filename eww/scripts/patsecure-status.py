#!/usr/bin/env python3

import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

MAX_AGE_SECONDS = 7 * 24 * 60 * 60
SUMMARY_RE = re.compile(
    r"\[RÉSUMÉ\]\s+OK=(\d+)\s+ATTENTION=(\d+)\s+ERREUR=(\d+)\s+INFO=(\d+)"
)


def yuck_string(value):
    return json.dumps(str(value), ensure_ascii=False)


def report_directory():
    state_home = os.environ.get("XDG_STATE_HOME")
    if state_home:
        return Path(state_home) / "patsecure" / "reports" / "shareable"
    return Path.home() / ".local" / "state" / "patsecure" / "reports" / "shareable"


def latest_report():
    directory = report_directory()
    try:
        candidates = [path for path in directory.glob("audit-partageable-*.txt") if path.is_file()]
    except OSError:
        return None

    if not candidates:
        return None

    try:
        return max(candidates, key=lambda path: path.stat().st_mtime)
    except OSError:
        return None


def parse_summary(path):
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                match = SUMMARY_RE.search(line)
                if match:
                    ok, attention, error, info = (int(value) for value in match.groups())
                    return {
                        "ok": ok,
                        "attention": attention,
                        "error": error,
                        "info": info,
                    }
    except OSError:
        return None

    return None


def format_last_audit(timestamp):
    audit_time = datetime.fromtimestamp(timestamp)
    now = datetime.now()
    delta_days = (now.date() - audit_time.date()).days

    if delta_days == 0:
        return f"Dernier audit : aujourd'hui à {audit_time:%H:%M}"
    if delta_days == 1:
        return f"Dernier audit : hier à {audit_time:%H:%M}"
    return f"Dernier audit : {audit_time:%d/%m/%Y à %H:%M}"


def state_from(summary, age_seconds):
    if age_seconds > MAX_AGE_SECONDS:
        return "patsecure-stale", "Audit à renouveler"
    if summary["error"] > 0:
        return "patsecure-error", "Erreur détectée"
    if summary["attention"] > 0:
        return "patsecure-warning", "Attention requise"
    return "patsecure-ok", "État OK"


def render_box(state_class, state_text, counts_text, note_text):
    return (
        f'(box :orientation "vertical" :class "patsecure-info {state_class}" :space-evenly false '
        f'(box :orientation "horizontal" :class "patsecure-status" :space-evenly false '
        f'(label :class "patsecure-dot" :text "●") '
        f'(label :class "patsecure-state" :halign "start" :hexpand true :text {yuck_string(state_text)})) '
        f'(label :class "patsecure-counts" :halign "start" :text {yuck_string(counts_text)}) '
        f'(label :class "patsecure-note" :halign "start" :text {yuck_string(note_text)}))'
    )


def render():
    path = latest_report()
    if path is None:
        return render_box(
            "patsecure-stale",
            "Aucun audit récent",
            "État PatSecure indisponible",
            "Lancer PatSecure pour créer un rapport partageable",
        )

    summary = parse_summary(path)
    if summary is None:
        return render_box(
            "patsecure-stale",
            "État indisponible",
            "Résumé PatSecure introuvable",
            "Le rapport partageable reste la seule source consultée",
        )

    try:
        timestamp = path.stat().st_mtime
    except OSError:
        timestamp = time.time()

    age_seconds = max(0, time.time() - timestamp)
    state_class, state_text = state_from(summary, age_seconds)
    counts_text = (
        f'{summary["ok"]} OK · {summary["attention"]} attention · {summary["error"]} erreur'
    )
    note_text = format_last_audit(timestamp)
    return render_box(state_class, state_text, counts_text, note_text)


def main():
    print(render())


if __name__ == "__main__":
    main()

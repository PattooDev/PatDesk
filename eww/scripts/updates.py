#!/usr/bin/env python3

import json
import os
import shutil
import subprocess


def yuck_string(value):
    return json.dumps(str(value), ensure_ascii=False)


def upgradable_count():
    if not shutil.which("apt"):
        return None

    env = os.environ.copy()
    env["LC_ALL"] = "C"

    try:
        completed = subprocess.run(
            ["apt", "list", "--upgradable"],
            check=False,
            text=True,
            capture_output=True,
            timeout=8,
            env=env,
        )
    except (OSError, subprocess.SubprocessError):
        return None

    if completed.returncode != 0:
        return None

    count = 0
    for line in completed.stdout.splitlines():
        line = line.strip()
        if not line or line.lower().startswith("listing"):
            continue
        if "/" in line:
            count += 1
    return count


def render(count):
    if count is None:
        state_class = "updates-unknown"
        state_text = "État indisponible"
    elif count == 0:
        state_class = "updates-current"
        state_text = "Système à jour"
    elif count == 1:
        state_class = "updates-warning"
        state_text = "1 mise à jour disponible"
    else:
        state_class = "updates-warning"
        state_text = f"{count} mises à jour disponibles"

    note = "Selon le cache APT local"

    return (
        f'(box :orientation "vertical" :class "updates-info {state_class}" :space-evenly false '
        f'(label :class "updates-state" :halign "start" :text {yuck_string(state_text)}) '
        f'(label :class "updates-note" :halign "start" :text {yuck_string(note)}))'
    )


def main():
    print(render(upgradable_count()))


if __name__ == "__main__":
    main()

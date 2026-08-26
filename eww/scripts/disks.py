#!/usr/bin/env python3

import json
import os
import re
import subprocess
import sys


UUID_NAME = re.compile(r"^[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}$")


def yuck_string(value):
    return json.dumps(str(value), ensure_ascii=False)


def format_capacity(size_bytes):
    size = int(size_bytes or 0)
    if size >= 1_000_000_000_000:
        value = size / 1_000_000_000_000
        text = f"{value:.1f}".replace(".0", "").replace(".", ",")
        return f"{text} To"
    if size >= 1_000_000_000:
        value = size / 1_000_000_000
        return f"{value:.0f} Go"
    return f"{size / 1_000_000:.0f} Mo"


def descendants(node):
    for child in node.get("children") or []:
        yield child
        yield from descendants(child)


def usable_mountpoint(node):
    mountpoints = [m for m in (node.get("mountpoints") or []) if m and os.path.isdir(m)]
    if not mountpoints:
        return None
    if "/" in mountpoints:
        return "/"
    return min(mountpoints, key=len)


def friendly_name(disk, mounted_nodes):
    if any(usable_mountpoint(node) == "/" for node in mounted_nodes):
        return "Système"

    if len(mounted_nodes) == 1:
        node = mounted_nodes[0]
        label = (node.get("label") or "").strip()
        if label:
            return label

        mountpoint = usable_mountpoint(node)
        if mountpoint:
            basename = os.path.basename(mountpoint.rstrip("/"))
            if basename and not UUID_NAME.match(basename):
                return basename

    model = " ".join((disk.get("model") or "").split())
    return model or disk.get("name") or "Disque"


def usage_for_nodes(nodes):
    total = 0
    used = 0
    seen_devices = set()

    for node in nodes:
        mountpoint = usable_mountpoint(node)
        if not mountpoint:
            continue
        try:
            device = os.stat(mountpoint).st_dev
            if device in seen_devices:
                continue
            seen_devices.add(device)
            stats = os.statvfs(mountpoint)
        except OSError:
            continue

        filesystem_total = stats.f_blocks * stats.f_frsize
        filesystem_available = stats.f_bavail * stats.f_frsize
        if filesystem_total <= 0:
            continue
        total += filesystem_total
        used += filesystem_total - filesystem_available

    if total <= 0:
        return None
    return max(0, min(100, round((used * 100) / total)))


def alert_class(usage):
    if usage is None:
        return "disk-unmounted"
    if usage >= 90:
        return "disk-critical"
    if usage >= 75:
        return "disk-warning"
    return "disk-normal"


def load_disks():
    command = [
        "lsblk",
        "--json",
        "--bytes",
        "--output",
        "NAME,TYPE,SIZE,MODEL,FSTYPE,MOUNTPOINTS,LABEL",
    ]
    completed = subprocess.run(command, check=True, text=True, capture_output=True)
    data = json.loads(completed.stdout)
    return [node for node in data.get("blockdevices", []) if node.get("type") == "disk"]


def disk_widget(disk):
    candidates = list(descendants(disk))
    if disk.get("fstype") and not candidates:
        candidates.append(disk)

    mounted_nodes = [node for node in candidates if usable_mountpoint(node)]
    name = friendly_name(disk, mounted_nodes)
    capacity = format_capacity(disk.get("size"))
    usage = usage_for_nodes(mounted_nodes)
    state_class = alert_class(usage)

    if usage is None:
        detail = f"non monté · {capacity}"
        progress = 0
    else:
        detail = f"{usage}% · {capacity}"
        progress = usage

    return (
        f'(box :orientation "vertical" :class "disk-row {state_class}" :space-evenly false '
        '(box :orientation "horizontal" :class "disk-line" :space-evenly false '
        f'(label :class "disk-name" :halign "start" :hexpand true :limit-width 24 :text {yuck_string(name)}) '
        f'(label :class "disk-value" :halign "end" :text {yuck_string(detail)})) '
        f'(progress :class "metric-bar disk-bar {state_class}" :value {progress} :orientation "horizontal"))'
    )


def main():
    try:
        disks = load_disks()
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as error:
        print(
            '(label :class "disk-empty" :halign "start" '
            f':text {yuck_string("Lecture des disques impossible")})'
        )
        print(f"PatDesk: {error}", file=sys.stderr)
        return 1

    if not disks:
        print('(label :class "disk-empty" :halign "start" :text "Aucun disque détecté")')
        return 0

    widgets = " ".join(disk_widget(disk) for disk in disks)
    print(f'(box :orientation "vertical" :class "disk-list" :space-evenly false {widgets})')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

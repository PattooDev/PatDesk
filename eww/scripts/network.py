#!/usr/bin/env python3

import json
import os
import re
import subprocess
import time


def run(command):
    try:
        completed = subprocess.run(
            command,
            check=False,
            text=True,
            capture_output=True,
            timeout=2,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return completed.stdout.strip()


def yuck_string(value):
    return json.dumps(str(value), ensure_ascii=False)


def default_interface():
    route = run(["ip", "-4", "route", "show", "default"])
    match = re.search(r"\bdev\s+(\S+)", route)
    return match.group(1) if match else ""


def local_ip(interface):
    if not interface:
        return "—"
    output = run(["ip", "-4", "-o", "address", "show", "dev", interface, "scope", "global"])
    match = re.search(r"\binet\s+([0-9.]+)/", output)
    return match.group(1) if match else "—"


def connection_type(interface):
    if not interface:
        return "Aucune interface"
    if os.path.isdir(f"/sys/class/net/{interface}/wireless"):
        return f"Wi-Fi · {interface}"
    return f"Ethernet · {interface}"


def read_counter(interface, counter):
    if not interface:
        return 0
    try:
        with open(f"/sys/class/net/{interface}/statistics/{counter}", encoding="utf-8") as stream:
            return int(stream.read().strip())
    except (OSError, ValueError):
        return 0


def state_path():
    runtime = os.environ.get("XDG_RUNTIME_DIR") or "/tmp"
    return os.path.join(runtime, f"patdesk-network-{os.getuid()}.json")


def load_state():
    try:
        with open(state_path(), encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, ValueError, TypeError):
        return {}


def save_state(state):
    path = state_path()
    temporary = f"{path}.tmp"
    try:
        with open(temporary, "w", encoding="utf-8") as stream:
            json.dump(state, stream)
        os.replace(temporary, path)
    except OSError:
        pass


def format_rate(bytes_per_second):
    rate = max(0.0, float(bytes_per_second))
    if rate >= 1024 * 1024:
        return f"{rate / (1024 * 1024):.1f} Mo/s".replace(".", ",")
    if rate >= 1024:
        return f"{rate / 1024:.0f} Ko/s"
    return f"{rate:.0f} o/s"


def connectivity(previous, now, interface):
    last_check = float(previous.get("connectivity_checked", 0))
    if now - last_check < 12 and "online" in previous:
        return bool(previous["online"]), last_check

    if not interface:
        return False, now

    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", "1.1.1.1"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=2,
        )
    except (OSError, subprocess.SubprocessError):
        return False, now
    return result.returncode == 0, now


def render(interface, ip_address, online, download, upload):
    status_class = "online" if online else "offline"
    status_text = "Internet connecté" if online else "Internet indisponible"
    link_name = connection_type(interface)

    return (
        '(box :orientation "vertical" :class "network-info" :space-evenly false '
        '(box :orientation "horizontal" :class "network-status" :space-evenly false '
        f'(label :class "network-dot {status_class}" :text "●") '
        f'(label :class "network-state" :halign "start" :text {yuck_string(status_text)})) '
        '(box :orientation "horizontal" :class "network-line" :space-evenly false '
        f'(label :class "network-name" :halign "start" :hexpand true :text {yuck_string(link_name)}) '
        f'(label :class "network-ip" :halign "end" :text {yuck_string(ip_address)})) '
        '(box :orientation "horizontal" :class "network-rates" :space-evenly false '
        f'(label :class "download-rate" :halign "start" :hexpand true :text {yuck_string("↓ " + format_rate(download))}) '
        f'(label :class "upload-rate" :halign "end" :text {yuck_string("↑ " + format_rate(upload))})))'
    )


def main():
    now = time.monotonic()
    interface = default_interface()
    ip_address = local_ip(interface)
    rx_bytes = read_counter(interface, "rx_bytes")
    tx_bytes = read_counter(interface, "tx_bytes")
    previous = load_state()

    elapsed = now - float(previous.get("time", now))
    if elapsed > 0 and previous.get("interface") == interface:
        download = (rx_bytes - int(previous.get("rx", rx_bytes))) / elapsed
        upload = (tx_bytes - int(previous.get("tx", tx_bytes))) / elapsed
    else:
        download = 0
        upload = 0

    online, checked_at = connectivity(previous, now, interface)

    save_state(
        {
            "time": now,
            "interface": interface,
            "rx": rx_bytes,
            "tx": tx_bytes,
            "online": online,
            "connectivity_checked": checked_at,
        }
    )

    print(render(interface, ip_address, online, download, upload))


if __name__ == "__main__":
    main()

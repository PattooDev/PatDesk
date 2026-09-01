#!/usr/bin/env python3

import json
import shutil
import subprocess


def yuck_string(value):
    return json.dumps(str(value), ensure_ascii=False)


def run_playerctl(args, timeout=3):
    try:
        completed = subprocess.run(
            ["playerctl", *args],
            check=False,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if completed.returncode != 0:
        return None
    return completed.stdout.strip()


def players():
    output = run_playerctl(["-l"])
    if not output:
        return []
    return [line.strip() for line in output.splitlines() if line.strip()]


def player_status(player):
    return run_playerctl(["-p", player, "status"]) or ""


def choose_player():
    available = players()
    if not available:
        return None, ""

    paused = None
    for player in available:
        status = player_status(player)
        if status == "Playing":
            return player, status
        if status == "Paused" and paused is None:
            paused = (player, status)

    return paused if paused else (available[0], player_status(available[0]))


def clean_text(value, max_length):
    value = " ".join((value or "").split())
    if not value:
        return ""
    if len(value) <= max_length:
        return value
    return value[: max_length - 1].rstrip() + "…"


def metadata(player):
    raw = run_playerctl(
        ["-p", player, "metadata", "--format", "{{artist}}\n{{title}}"]
    )
    if not raw:
        return "", ""
    lines = raw.splitlines()
    artist = lines[0].strip() if lines else ""
    title = lines[1].strip() if len(lines) > 1 else ""
    return clean_text(artist, 42), clean_text(title, 56)


def render_unavailable():
    return (
        '(box :orientation "vertical" :class "patsecure-info patsecure-stale" :space-evenly false '
        '(label :class "patsecure-state" :halign "start" :text "playerctl non installé") '
        '(label :class "patsecure-note" :halign "start" :text "Lecture multimédia locale indisponible"))'
    )


def render_idle():
    return (
        '(box :orientation "vertical" :class "patsecure-info patsecure-stale" :space-evenly false '
        '(label :class "patsecure-state" :halign "start" :text "Aucune lecture en cours") '
        '(label :class "patsecure-note" :halign "start" :text "Lecteurs MPRIS surveillés localement"))'
    )


def render(player, status, artist, title):
    is_playing = status == "Playing"
    state_class = "patsecure-ok" if is_playing else "patsecure-warning"
    state_text = "▶ Lecture" if is_playing else "Ⅱ Pause"
    title = title or "Titre inconnu"
    artist = artist or "Artiste inconnu"
    player_label = player.split(".", 1)[0] if player else "Lecteur"

    return (
        f'(box :orientation "vertical" :class "patsecure-info {state_class}" :space-evenly false '
        '(box :orientation "horizontal" :class "patsecure-status" :space-evenly false '
        f'(label :class "patsecure-state" :halign "start" :hexpand true :text {yuck_string(state_text)}) '
        f'(label :class "patsecure-note" :halign "end" :text {yuck_string(player_label)})) '
        f'(label :class "patsecure-state" :halign "start" :text {yuck_string(title)}) '
        f'(label :class "patsecure-counts" :halign "start" :text {yuck_string(artist)}))'
    )


def main():
    if not shutil.which("playerctl"):
        print(render_unavailable())
        return

    player, status = choose_player()
    if not player:
        print(render_idle())
        return

    artist, title = metadata(player)
    print(render(player, status, artist, title))


if __name__ == "__main__":
    main()

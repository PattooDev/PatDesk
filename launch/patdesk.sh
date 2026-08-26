#!/usr/bin/env bash

set -u

CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/patdesk"
EWW_BIN="${EWW_BIN:-$(command -v eww || true)}"

if [[ -z "$EWW_BIN" ]]; then
  echo "PatDesk: eww introuvable" >&2
  exit 1
fi

pkill eww 2>/dev/null || true
"$EWW_BIN" --config "$CONFIG_DIR" daemon
sleep 1
"$EWW_BIN" --config "$CONFIG_DIR" open patdesk

# Sous Deepin/KWin, une fenêtre Eww de type "normal" reste visible sur le
# bureau et peut être recouverte par les applications, mais KWin peut modifier
# sa position. Si wmctrl est disponible, on replace PatDesk à 120 px du bord
# droit et 20 px du haut de l'écran DP-0.
if command -v wmctrl >/dev/null 2>&1 && command -v xrandr >/dev/null 2>&1; then
  for _ in {1..20}; do
    window_line="$(wmctrl -lG | awk '/Eww - patdesk$/ {print; exit}')"

    if [[ -n "$window_line" ]]; then
      window_id="$(awk '{print $1}' <<< "$window_line")"
      window_width="$(awk '{print $5}' <<< "$window_line")"
      monitor_geom="$(xrandr --query | awk '/^DP-0 connected/ {for (i=1; i<=NF; i++) if ($i ~ /^[0-9]+x[0-9]+\+[0-9-]+\+[0-9-]+/) {print $i; exit}}')"

      if [[ -n "$monitor_geom" ]]; then
        monitor_width="${monitor_geom%%x*}"
        rest="${monitor_geom#*x}"
        monitor_height="${rest%%+*}"
        rest="${rest#*+}"
        monitor_x="${rest%%+*}"
        monitor_y="${rest#*+}"

        target_x=$((monitor_x + monitor_width - window_width - 120))
        target_y=$((monitor_y + 20))

        wmctrl -ir "$window_id" -e "0,$target_x,$target_y,-1,-1"
      fi
      break
    fi

    sleep 0.2
  done
fi

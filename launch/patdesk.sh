#!/usr/bin/env bash

set -u

CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/patdesk"

pkill eww 2>/dev/null || true

eww --config "$CONFIG_DIR" daemon
sleep 1
eww --config "$CONFIG_DIR" open patdesk


#!/usr/bin/env bash

set -u

temperature="$(
    LC_ALL=C sensors -u coretemp-isa-0000 2>/dev/null |
        awk '
            /^Package id 0:/ { package = 1; next }
            package && /temp[0-9]+_input:/ {
                printf "%.0f\n", $2
                exit
            }
        '
)"

if [[ "$temperature" =~ ^[0-9]+$ ]]; then
    echo "$temperature"
    exit 0
fi

for hwmon in /sys/class/hwmon/hwmon*; do
    [[ -r "$hwmon/name" ]] || continue
    [[ "$(<"$hwmon/name")" == "coretemp" ]] || continue

    for label_file in "$hwmon"/temp*_label; do
        [[ -r "$label_file" ]] || continue
        [[ "$(<"$label_file")" == "Package id 0" ]] || continue

        input_file="${label_file%_label}_input"
        if [[ -r "$input_file" ]]; then
            awk '{ printf "%.0f\n", $1 / 1000 }' "$input_file"
            exit 0
        fi
    done
done

echo 0


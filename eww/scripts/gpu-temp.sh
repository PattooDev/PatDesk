#!/usr/bin/env bash

set -u

temperature="$(
    nvidia-smi \
        --query-gpu=temperature.gpu \
        --format=csv,noheader,nounits \
        2>/dev/null |
        awk 'NR == 1 { printf "%.0f\n", $1 }'
)"

if [[ "$temperature" =~ ^[0-9]+$ ]]; then
    echo "$temperature"
else
    echo 0
fi


#!/usr/bin/env bash

set -u

read_cpu_values() {
    local label user nice system idle iowait irq softirq steal guest guest_nice

    read -r label user nice system idle iowait irq softirq steal guest guest_nice < /proc/stat
    CPU_IDLE=$((idle + iowait))
    CPU_TOTAL=$((user + nice + system + idle + iowait + irq + softirq + steal))
}

CPU_IDLE=0
CPU_TOTAL=0

read_cpu_values
idle_before=$CPU_IDLE
total_before=$CPU_TOTAL

sleep 0.2

read_cpu_values
idle_delta=$((CPU_IDLE - idle_before))
total_delta=$((CPU_TOTAL - total_before))

if (( total_delta <= 0 )); then
    echo 0
    exit 0
fi

usage=$((100 * (total_delta - idle_delta) / total_delta))

if (( usage < 0 )); then
    usage=0
elif (( usage > 100 )); then
    usage=100
fi

echo "$usage"


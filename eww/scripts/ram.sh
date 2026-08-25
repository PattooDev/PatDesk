#!/usr/bin/env bash

awk '
    /^MemTotal:/     { total = $2 }
    /^MemAvailable:/ { available = $2 }
    END {
        if (total > 0) {
            printf "%.0f\n", ((total - available) * 100) / total
        } else {
            print 0
        }
    }
' /proc/meminfo


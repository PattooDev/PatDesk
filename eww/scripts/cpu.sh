#!/bin/bash

LC_ALL=C mpstat 1 1 | awk '/Average:/ {printf "%.0f\n", 100 - $NF}'

#!/usr/bin/python3
"""This script reads the stdin line by line"""
import sys
import signal
import re


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0
interval_stats = {}


def print_statistics(stats):
    """This function reads the stats"""
    global total_size
    print(f"File size: {total_size}")
    for code in sorted(stats):
        count = status_codes[code]
        if count > 0:
            print(f"{code}: {count}")


def signal_handler(signal, frame):
    """This method prints after keybord intrupt signal"""
    print_statistics(interval_stats)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        pattern = (
            r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] '
            r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
            )
        matchh = re.match(pattern, line.strip())
        if matchh:
            status_code = int(matchh.group(3))
            file_size = int(matchh.group(4))

            total_size += file_size
            status_codes[status_code] += 1
            interval_stats[status_code] = (
                interval_stats.get(status_code, 0) + 1
                )
            lines_processed += 1

            if lines_processed % 10 == 0:
                print_statistics(interval_stats)
                interval_stats = {}

except KeyboardInterrupt:
    print_statistics(status_codes)
    print_statistics(interval_stats)
    sys.exit(0)

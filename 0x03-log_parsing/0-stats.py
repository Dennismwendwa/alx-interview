#!/usr/bin/python3
"""Printing status"""
import sys


status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in status_code.keys():
                status_code[code] += 1
            total_size += size
            counter += 1
        if counter == 10:
            counter = 0
            print(f"File size: {total_size}")
            for key, value in sorted(status_code.items()):
                if value != 0:
                    print(f"{key}: {value}")
except Exception:
    pass

finally:
    print("File size: {total_size}")
    for key, value in sorted(status_code.items()):
        if value != 0:
            print(f"{key}: {value}")

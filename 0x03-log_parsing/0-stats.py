#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""


import sys


total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0


try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        if len(data) > 2:
            status_code = data[-2]
            file_size = data[-1]
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += int(file_size)
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for k, v in sorted(status_codes.items()):
                if v > 0:
                    print("{}: {}".format(k, v))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{}: {}".format(k, v))

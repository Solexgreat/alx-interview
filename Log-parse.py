#!/usr/bin/python3
import sys
import re

"""line = '<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>' """

total_size = 0
status_code = {'200':0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0 }
index = 0
try:
    for line in sys.stdin:
        index += 1
        if  index == 10:
            index = 0
            print(f"File size: {total_size}")
            for i, j in status_code.items():
                if j > 0:
                    print(f"{i}: {j}")
        if re.match(r'^\S+ - \[.+\] "GET /projects/260 HTTP/1.1" \d{3} \d+$', line):
            match = re.search(r'"GET /projects/260 HTTP/1.1" (\d+) (\d+$)', line)
            if match:
                code = match.group(1)
                if code in status_code:
                    status_code[code] += 1
            file = match.group(2)
            total_size += int(file)
        else:
            continue
except KeyboardInterrupt:
    for i, j in status_code.items():
        if j > 0:
            print(f"{i}: {j}")
    raise                
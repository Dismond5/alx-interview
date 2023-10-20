#!/usr/bin/python3
import sys
import re

from collections import Counter

STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

total_file_size = 0
status_code_counts = Counter()
line_count = 0

def print_stats():
  print("Total file size: %d" % total_file_size)
  for status_code in sorted(STATUS_CODES):
    count = status_code_counts[status_code]
    if count > 0:
      print("%d: %d" % (status_code, count))

try:
  for line in sys.stdin:
    line_count += 1

    match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]*)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
    if match:
      ip_address, date, status_code, file_size = match.groups()
      total_file_size += int(file_size)
      status_code_counts[int(status_code)] += 1

    if line_count % 10 == 0:
      print_stats()

except KeyboardInterrupt:
  print_stats()

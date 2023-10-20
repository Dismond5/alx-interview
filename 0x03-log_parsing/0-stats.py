#!/usr/bin/python3
import sys
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)
lines_processed = 0

try:
    for line in sys.stdin:
        try:
            _, _, _, _, status_code, file_size = line.split()[0:6]
            status_code = int(status_code)
            file_size = int(file_size)
        except (ValueError, IndexError):
            continue

        total_file_size += file_size
        status_code_counts[status_code] += 1
        lines_processed += 1

        if lines_processed % 10 == 0:
            print(f'Total file size: File size: {total_file_size}')

            for code in sorted(status_code_counts.keys()):
                if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    print(f'{code}: {status_code_counts[code]}')

except KeyboardInterrupt:
    print('Process interrupted. Exiting...')
    sys.exit(0)

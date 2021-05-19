#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_letter = None
current_count = 0
letter = None


for line in sys.stdin:
    line = line.strip()
    letter, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_letter == letter:
        current_count += count
    else:
        if current_letter:
            print('%s\t%s' % (current_letter, current_count))
        current_count = count
        current_letter = letter

if current_letter == letter:
    print('%s\t%s' % (current_letter, current_count))

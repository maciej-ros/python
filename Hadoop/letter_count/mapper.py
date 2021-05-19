#!/usr/bin/env python3
"""mapper.py"""

import sys


for line in sys.stdin:
    line = line.strip()
    line = line.replace(" ", "")
    def split(x):
        return [char for char in x]
    letters = split(line)

    for letter in letters:
        print('%s\t%s' % (letter, 1))

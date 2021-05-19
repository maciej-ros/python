#!/usr/bin/env python3
"""mapper.py"""

import sys


for line in sys.stdin:
    line = line.strip()
    numbers = line.split()
    for number in numbers:
       print("%s\t%s" % (number, 1))

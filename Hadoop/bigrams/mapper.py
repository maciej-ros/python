#!/usr/bin/env python3
"""mapper.py"""

import sys


bigrams = []
for line in sys.stdin:
    line = line.replace(",","")
    line = line.replace("-","")
    line = line.replace("?","")
    line = line.replace(".","")
    line = line.replace(";","")
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        bigrams.append(word)


for i in range(len(bigrams)):
    print(bigrams[i], bigrams[i+1])
    if i == (len(bigrams)-2):
        break
	


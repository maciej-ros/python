#!/usr/bin/env python3
"""mapper.py"""

import sys

current_word = None
current_word2 = None
bigram1 = None
bigram2 = None
bigrams = []
for line in sys.stdin:
    line = line.strip()
    bigram1, bigram2 = line.split(" ")
    if current_word == bigram1:
        bigrams.append(bigram2)
    else:
        if current_word:
            print(current_word, len(bigrams))
            for i in range(len(bigrams)):
                if current_word2 == bigrams[i]:
                    continue
                else:
                    current_word2 = bigrams[i]
                    if current_word2:
                       print("\t",current_word, current_word2, round((bigrams.count(current_word2)/len(bigrams)),2))
            bigrams = []
        current_word = bigram1
        bigrams.append(bigram2)
if current_word == bigram1:
    print(current_word, len(bigrams))
    for i in range(len(bigrams)):
        if current_word2 == bigrams[i]:
            continue
        else:
            current_word2 = bigrams[i]
            if current_word2:
               print("\t",current_word, current_word2, round((bigrams.count(current_word2)/len(bigrams)),2))

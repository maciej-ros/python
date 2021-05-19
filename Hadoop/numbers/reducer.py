#!/usr/bin/env python3
"""reducer.py"""

import sys

current_number = None
number = None
count = 0
total_count = 0
suma = 0
liczby = []
different_number = 0
maximum = 0
geo_mean = 1
mediana = 0

for line in sys.stdin:
    line = line.strip()
    number, count = line.split('\t', 1)
    try:
        count = int(count)
        number = int(number)
    except ValueError:
        continue
    liczby.append(number)
    total_count += count
    suma += number
    geo_mean = geo_mean*number
    if current_number != number:
        different_number += 1
        current_number = number
    if current_number > maximum:
        maximum = number 

if total_count % 2 == 0:
    mediana = (liczby[int((total_count/2)-1)] + liczby[int(total_count/2)])/2
else:
    mediana = liczby[int(total_count/2)]

print("Największa liczba:", maximum)
print("Średnia arytmetyczna:", round(suma/total_count, 2))
print("Średnia geometryczna:", round(pow(geo_mean, 1/total_count), 2))
print("Mediana:", mediana)
print("Liczba różnych liczb:", different_number)
	


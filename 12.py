#!/usr/bin/python
from numpy import sqrt
import time

total_counter = 0
total = 0

found = False

start_time = time.time()

while not found:
    total_counter += 1
    total += total_counter

    divisors = 0
    counter = 0

    while counter < sqrt(total):
        counter += 1
        
        if total%counter == 0:
            divisors += 2
            
    if divisors > 500:
        print("Triangle number %i has %i divisors"%(total,divisors))
        found = True
        print("--- %s seconds ---"%(time.time() - start_time))

        

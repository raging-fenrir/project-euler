#!/usr/bin/env python
import numpy as np

a = np.linspace(999,1,999)
sum1 = 0

for i in a:
    if i%3 == 0:
        sum1 += i
        print(i)
    elif i%5 == 0:
        sum1 += i
        print(i)
print(sum1)

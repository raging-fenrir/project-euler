import numpy as np

a = 1
b = 1
fibo = 0
sum1 = 0

argument=True

while fibo < 4e6:
    print fibo
    if fibo%2 == 0:
        sum1 += fibo

    fibo = a+b
    a = b
    b = fibo

print fibo, sum1

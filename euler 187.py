from sympy import primerange, primepi
import time

start = time.time()
n = 10**8
count = 0
for i in primerange(2, 10**4):
    count += primepi(n / i) - primepi(i) + 1
    if time.time() - start > 10:
        print(i, count)
        start = time.time()

print(count)

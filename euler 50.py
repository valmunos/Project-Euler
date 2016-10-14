from sympy import primerange, isprime
import time

primes = {}
start = time.time()
for i in primerange(2, 100000):
    total = 0
    count = 1
    if time.time() - start > 10:
        print(i)
        start = time.time()
    for n in primerange(i, 100000):
        total += n
        if total > 1000000:
            break
        if isprime(total) and total not in primes:
            primes[total] = count
            #print(total, primes[total])
        count += 1

res = []
for key, val in primes.items():
    res.append((val, key))

res.sort()
print(res[-1])

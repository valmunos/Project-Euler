from sympy import isprime
import time

primes = [1, 3, 7, 9, 13, 27]

def check_prime(n):
    for i in primes:
        if not isprime(n**2 + i):
            return False
    return True

res = []
start = time.time()
for i in range(15000000, 150000000, 10):
    if check_prime(i):
        res.append(i)
    if time.time() - start > 10:
        print(i)
        print(res)
        start = time.time()

print(sum(res))

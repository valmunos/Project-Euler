from sympy import primerange, isprime, primefactors
import math
import time


def factorize(n):
    if isprime(n):
        return []
    res = []
    for i in primerange(0, math.sqrt(n)+1):
        if n % i == 0:
            res.append(i)
            n /= i
            if isprime(n):
                res.append(n)
                break
    return res


def totient(n):
    f = factorize(n)
    count = 1
    for i in range(2, n):
        flag = False
        for p in f:
            if i % p == 0:
                flag = True
                break
            if p > i:
                break
        if not flag:
            count += 1
    return n, n / count

def phi(n):
    f = primefactors(n)
    count = n
    for p in f:
        count *= (1-1/p)
    if isprime(n):
        return round(count - 1)
    return round(count)

start = time.time()
for i in range(3, 101):
    print(i, phi(i), i/phi(i))
    if time.time() - start > 10:
        print(i)
        start = time.time()

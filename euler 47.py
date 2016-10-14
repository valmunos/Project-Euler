from sympy import primerange, isprime
import math
import time

def decompose(n):
    if isprime(n):
        return False
    factors = {}
    for i in primerange(2, math.sqrt(n)):
        if n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
            if isprime(n):
                factors[n] = factors.get(n, 0) + 1
            if len(factors) > 4:
                break
    return len(factors)

#print(decompose(645))
start = time.time()
i = 640
while True:
    if time.time() - start > 10:
            print(i)
            start = time.time()
    while True:
        if decompose(i+3) != 4:
            i += 4
            break
        elif decompose(i+2) != 4:
            i += 3
            break
        elif decompose(i+1) != 4:
            i += 2
            break
        elif decompose(i) != 4:
            i += 1
            break
        else:
            print(i, 'success!')

print(i-4)


    

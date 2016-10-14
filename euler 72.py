from sympy import primefactors, isprime
import time

def phi(n):
    f = primefactors(n)
    count = n
    for p in f:
        count *= (1-1/p)
    return round(count)

start = time.time()
memo = {}
for i in range(2, 1000001):
    if i not in memo:
        memo[i] = phi(i)
        if i < 333333:
            if isprime(i):
                for n in range(2, i):
                    if i*n > 1000000:
                        break
                    memo[n*i] = memo[n]*memo[i]
    if time.time() - start > 10:
        print(i, len(memo))
        start = time.time()

print(len(memo))
print(sum(memo.values()))


        

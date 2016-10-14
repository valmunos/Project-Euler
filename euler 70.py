from sympy import primefactors, isprime, primerange, prevprime
import time

memo = {}

def phi(n):
    f = primefactors(n)
    count = n
    for p in f:
        count *= (1-1/p)
    return round(count)

def is_perm(n, d):
    s = str(n)
    r = str(d[n])
    if sorted(s) == sorted(r):
        return True
    return False

res = []
start = time.time()
i = 3163
flag = False
while True:
    #print(i)
    for j in primerange(prevprime(i), 10000000/i):
        memo[i*j] = phi(i*j)
        if is_perm(i*j, memo):
            res.append((i*j/memo[i*j], i*j))
            if len(res) > 10:
                flag = True
    if time.time() - start > 10:
        print(i, len(memo))
        start = time.time()
    if flag:
        break
    i = prevprime(i)
        
print(len(res), len(memo))
res.sort()
print(res[0])

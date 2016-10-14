from sympy import gcd
import time
start = time.time()
res = []
for i in range(999900, 1000000):
    if i % 7 != 0:
        n = int(3/7*i)
        if gcd(n, i) == 1:
            #print(3/7 - n/i, n, i)
            res.append((3/7 - n/i, n, i))
        if time.time() - start > 10:
            print(i)
            start = time.time()

res.sort()
print(res[0:10])

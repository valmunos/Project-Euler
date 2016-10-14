import time
from sympy import primerange
t = [7080, 370, 85]

count = 0
sums = {}
start = time.time()
for i in primerange(0,t[0]):
    for j in primerange(0,t[1]):
        for k in primerange(0,t[2]):
            if time.time() - start > 10:
                print(i, j, k, count)
                start = time.time()
            s = i**2 + j**3 + k**4
            if s < 50000000 and s not in sums:
                #print(i, j, k, i**2 + j**3 + k**4)
                sums[s] = None
print(len(sums))

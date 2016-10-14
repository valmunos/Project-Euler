import math
import time

part = {0:1}
res = [1]

def k(n):
    k = n // 2 + 1
    if n % 2 != 0:
        k *= -1
    return k

def gen_k(i):
    n = k(i)
    t = n * (3*n - 1) / 2
    return int(t)

def partition(n):
        if n == gen_k(len(res)):
            res.append(gen_k(len(res)))
        count = 0
        for i in range(len(res)):
            count += part[n - res[i]] * int(math.pow(-1, i//2))
        part[n] = count
        return part[n]

for i in range(1, 101):
    print(partition(i))

start = time.time()
i = 1
while True:
    if partition(i) % 1000000 == 0:
        print(i)
        break
    if time.time() - start > 10:
        print(i)
        start = time.time()
    i += 1

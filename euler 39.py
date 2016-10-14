import math
import time

sums = {}
triplets = {}
squares = []
for i in range (300):
    squares.append(i**2)
def triplets_n():
    start = time.time()
    flag = True
    count = 0
    while 12*count <= 125000:
        b = 1
        c = 2 + count
        a = math.sqrt(c**2 - b**2)
        while b + c + a <= 1500000:
            if a in squares:
                t = tuple(sorted([int(a),b,c]))
                if t not in triplets:
                    n = sum(t)
                    sums[n] = sums.get(n, 0) + 1
                    triplets[t] = None
            b += 1
            c += 1
            a = math.sqrt(c**2 - b**2)
        count += 1
        if time.time() - start > 10:
            print(count)
            start = time.time()

triplets_n()
res = []
for key in sums.keys():
    if sums[key] != 1:
        del sums[key]

print(len(sums))

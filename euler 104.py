import time
import math

cache = {1:1, 2:1}

def fib(n):
    try:
        return cache[n]
    except KeyError:
        cache[n] = (fib(n-1) + fib(n-2))%1000000000
        return cache[n]

phi = (1 + math.sqrt(5))/2
psi = (1 - math.sqrt(5))/2

def binet(n):
    b = n*math.log10(phi) - math.log10(math.sqrt(5))
    #print(b)
    p = b%1 + 8
    #print(p)
    return math.pow(10, p)

i = 3
n = 0
check = ['1','2','3','4','5','6','7','8','9']
start = time.time()

while True:
    s = str(fib(i))
    r = sorted(s[:9])
    t = sorted(s[-9:])
    #if time.time() - start > 10:
     #   print(fib(i), r, t)
      #  start = time.time()
    if t == check:
        #print(i)
        #print(binet(i))
        s = str(binet(i))
        r = sorted(s[:9])
        if r == check:
            print(i)
            break
    i += 1

'''

print(binet(541))
'''

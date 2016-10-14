from sympy import sieve
import time

start = time.time()
i = 7037
while True:
    s = (sieve[i] - 1)**i + (sieve[i] + 1)**i
    r = s % sieve[i]**2
    #print(r, i, sieve[i])
    if time.time() - start > 10:
        print(r, i, sieve[i])
        start = time.time()
    if r > 10**10:
        print(sieve[i], i)
        break
    i += 200

while True:
    s = (sieve[i] - 1)**i + (sieve[i] + 1)**i
    r = s % sieve[i]**2
    if r < 10**10:
        s = (sieve[i+2] - 1)**(i+2) + (sieve[i+2] + 1)**(i+2)
        r = s % sieve[i+2]**2
        print(sieve[i+2], i+2, r)
        break
    i -= 2
    


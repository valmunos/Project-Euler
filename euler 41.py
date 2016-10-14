from sympy import isprime
import itertools
import time

def ispan(n):
    s = str(n)
    for c in s:
        if s.count(c) > 1 or c == '0':
            return False
    return True

#t = sieve.primerange(1, 1000000000)
pans = []

string = '1234567'

#for i in range(len(string)):
 #   t = string[:i] + string[(i+1):]
for i in itertools.permutations(string):
    s = ''.join(i)
    pans.append(s)

pans = sorted(pans, reverse=True)
print(pans[:10], len(pans))

start = time.time()
'''
for i in sieve:
    if ispan(i):
        pans.append(i)
    if time.time() - start > 10:
        print(i)
        print(pans[-1])
        start = time.time()
    if i > 10000000000:
        break
'''
#test = ['23', '55', '97']
for i in pans:
    if isprime(i):
        print(i)
        break

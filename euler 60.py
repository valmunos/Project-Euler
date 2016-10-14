import itertools
from sympy import isprime, primerange
import time

def check_pairs(t):
    '''
    concatenate two numbers left and right returning True if both are prime
    and false if one or both are not prime
    '''
    s1 = str(t[0])
    s2 = str(t[1])
    n1 = int(s1 + s2)
    n2 = int(s2 + s1)
    if isprime(n1) and isprime(n2):
        return True
    return False

primes = []
for i in primerange(3, 8400):
    primes.append(i)

del primes[1]

works = {}

start = time.time()
for t in itertools.combinations(primes, 2):
    if check_pairs(t):
        works.setdefault(t[0], []).append(t[1])

triples = []

for key in works.keys():
    for n in works[key]:
        if n in works:
            for x in works[n]:
                if x in works[key] and x in works:
                    for z in works[x]:
                        if z in works[key] and z in works[n] and z in works:
                            for y in works[z]:
                                if y in works[key] and y in works[n] and y in works and y in works[x]:
                                    triples.append((key, n, x, z, y))


print(sorted(triples))


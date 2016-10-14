'''
find 3 4-digit primes which are permutations of one another and differ by a
constant
'''
import itertools
from sympy import isprime
res = {}
i = 1000
while i < 10000:
    s = str(i)
    z = tuple(sorted(s))
    if z not in res:
        res[z] = []
        for n in itertools.permutations(s):
            t = int(''.join(n))
            if isprime(t) and t > 1000 and t not in res[z]:
                res[z].append(t)
        if len(res[z]) >= 3:
            t = sorted(res[z])
            for n in range(len(t)):
                for x in range(n+1, len(t)):
                    diff = abs(t[x] - t[n])
                    if t[x] + diff in t:
                        print(t[n], t[x], t[x] + diff)
    i += 1
                    
            

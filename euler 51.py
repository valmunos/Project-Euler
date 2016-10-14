from sympy import isprime, primerange
import itertools

def perms(n):
    res = []
    k = '111'
    while len(k) < n:
        k += '0'
    for n in itertools.permutations(k):
        s = int(''.join(n))
        if s not in res and s % 10 == 0:
            res.append(s)
    return res

def is_copy(n):
    s = str(n)[0:-1]
    for c in s:
        if s.count(c) >= 3 and int(c) < 3:
            return (True, int(c))
    return False,

a = 3
while True:
    perm = perms(a+1)
    for i in primerange(10**a, 10**(a+1)):
        if is_copy(i)[0]:
            for x in perm:
                b = is_copy(i)[1]
                n = i
                no = 0
                yes = 1
                while no < 3 - b and yes < 8:
                    n += x
                    if isprime(n):
                        yes += 1
                        if yes == 8:
                            print(i)
                    if not isprime(n):
                        no += 1
    a += 1

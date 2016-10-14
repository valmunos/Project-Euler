from sympy.ntheory import isprime

def truncate_left(n):
    s = str(n)[1:]
    return int(s)

def truncate_right(n):
    s = str(n)[:-1]
    return int(s)

def check_number(n):
    if not isprime(n):
        return False
    a = n
    while a > 10:
        a = truncate_left(a)
        if not isprime(a):
            return False
    a = n
    while a > 10:
        a = truncate_right(a)
        if not isprime(a):
            return False
    return True

primes = []
for i in range(10, 1000000):
    if check_number(i):
        print(i)
        primes.append(i)
    if len(primes) == 11:
        print(sum(primes))
        break
        
    
    

fac = {}

def factorize(n, primes):
    fac[n] = {}
    a = n
    for i in primes:
        if a == 1:
            break
        while a % i == 0:
            fac[n][i] = fac[n].get(i, 0) + 1
            a /= i
    return fac

def make_primes():
    fin = open('primes1000000.txt')
    primes = []
    for line in fin:
        line = line.strip('\n')
        p = int(line)
        primes.append(p)
    return primes

def make_factors(n):
    factors = []
    global fac
    i = 0
    for key in fac[n].keys():
        factors.append([])
        a = fac[n][key]
        while a >= 0:
            factor = key**a
            factors[i].append(factor)
            a -= 1
        i += 1
    return factors

def make_divisors(n,factors):
    global divisors
    if len(factors) == 1:
        for i in range(len(factors[0])):
            return factors[0][i]
    for i in range(len(factors)):
        for i in range(len(factors[i])):
            prod = factors[i][i] * make_divisors(n,factors[1:])
            divisors.append(prod)
            print(divisors)
    return divisors
            
divisors = []
primes = make_primes()
factorize(200, primes)
factors = make_factors(200)
#print(fac[200][2])
print(make_divisors(200, factors))


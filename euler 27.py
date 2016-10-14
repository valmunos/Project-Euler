from sympy.ntheory import isprime

res = []
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        count = 0
        while True:
            prod = n**2 + a*n + b
            if not isprime(prod):
                break
            count += 1
            n += 1
        if count >= 10:
            tup = (count, a, b)
            res.append(tup)
            print(tup)
        #res[(a, b)] = count

res = sorted(res, reverse = True)
print(res[:50])
'''
n = 0
count = 0
while True:
    prod = n**2 - 79*n + 1601
    if not isprime(prod):
        break
    count += 1
    n += 1

print(count)
'''

from sympy import isprime

i = 3
count = 0
while True:
    n = i - 1
    d = 4 * i//2 + 1
    for k in range(1,4):
        if isprime(i**2 - n*k):
            count += 1
    if count / d < 0.1:
        print(i)
        break
    i += 2

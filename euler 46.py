import math
from sympy import isprime

i = 3
while True:
    if not isprime(i):
        flag = True
        for n in range(int(i/math.sqrt(2) + 1)):
            if isprime(i - 2*n**2):
                flag = False
                break
        if flag:
            print(i)
            break
    i += 2

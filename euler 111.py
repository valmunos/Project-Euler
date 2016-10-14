import itertools
from sympy import isprime

#z = '111111111'

t = ['0','1','2','3','4','5','6','7','8','9']

count = 0
for i in range(1,10):
    z = str(i)*9
    print(z)
    for c in t:
        for p in range(10):
            s = z[p:] + c + z[:p]
            #print(s)
            n = int(''.join(s))
            if isprime(n):
                print(n, 'prime')
                count += n
print(count)

for i in range(11, 100, 2):
    z = '0'*8
    z = str(i)[0] + z + str(i)[1]
    #print(z)
    if isprime(int(z)):
        print(z, 'prime')
        count += int(z)

t = ['2', '8']

for c in t:
    for i in range(1, 100, 2):
        z = c*8
        for p in range(9):
            if i < 10:
                s = z[p:] + '0' + z[:p] + str(i)
            if i > 10:
                s = z[p:] + str(i)[0] + z[:p] + str(i)[1]
            if len(str(int(s))) == 10:
                n = int(s)
                if isprime(n):
                    print(n, 'prime')
                    count += n

print(count)
    

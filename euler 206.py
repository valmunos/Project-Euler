import time
import math

def string(n):
    s = str(n)
    res = ''
    for i in range(0, len(str(n)), 2):
        res += s[i]
    return res

i = int(math.sqrt(1020000000000000000)) // 10 * 10
start = time.time()
n = 10203
while True:
    if string(i**2) == '1234567890':
        print(i)
        break
    if time.time() - start > 10:
        print(i, string(i**2))
        start = time.time()
    if string(i**2)[2] == '4':
        n += 10
        i = int(math.sqrt(n*(10**14)))//10 * 10 - 10
        #print(n, i, string((i+20)**2))
    if string(i**2)[1] == '3':
        n += 900
        i = int(math.sqrt(n*(10**16)))//10 * 10 - 10
        #print(n, i, string(i**2))
    i += 10



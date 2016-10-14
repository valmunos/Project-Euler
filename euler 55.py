import math
import time

def is_pali(n):
    return str(n) == str(n)[::-1]

def add_reverse(n):
    t = int(str(n)[::-1])
    return t + n

def is_lychrel(n):
    n = add_reverse(n)
    count = 1
    while not is_pali(n):
        n = add_reverse(n)
        count += 1
        if count == 50:
            return True
    return False

count = 0
start = time.time()
for i in range(1, 10001):
    if is_lychrel(i):
        count += 1
print(time.time() - start)

#print(len(lychrels))
    

    

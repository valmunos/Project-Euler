import time

fin = open('primes1000000.txt')
primes = []
for line in fin:
    line = line.strip('\n')
    p = int(line)
    primes.append(p)

def make_circular(n):
    t = []
    s = str(n)
    for i in range(len(s)):
        s = s[1:] + s[0]
        t.append(int(s))
    return t

def check_primes(t):
    flag = True
    for number in t:
        if number not in primes:
            flag = False
            break
    if flag:
        return 1
    return 0

count = 0
start = time.time()
for i in range(1000000):
    t = make_circular(i)
    count += check_primes(t)
    if time.time() - start > 10:
        print(i)
        start = time.time()

print(count)

import itertools

pans = []
for i in itertools.permutations('0123456789'):
    s = ''.join(i)
    if s[0] != '0' and int(s[3]) % 2 == 0:
        pans.append(s)
        #print(s)

print('done')

primes = [2,3,5,7,11,13,17]
res = []

def make_ints(s):
    t = []
    for i in range(1, len(s)-2):
        p = s[i] + s[i+1] + s[i+2]
        t.append(int(p))
    #print(t)
    return t

for s in pans:
    flag = True
    t = make_ints(s)
    for i in range(len(primes)):
        if t[i] % primes[i] != 0:
            flag = False
            break
    if flag:
        print(s)
        res.append(int(s))

print(len(res))
print(sum(res))

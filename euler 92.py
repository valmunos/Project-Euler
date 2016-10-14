import time
import itertools

memo = {1:1, 89:89}

res = [89]
ones = [1]

def chain(n):
    if n == 89 or n == 1:
        return None
    a = n
    while a != 1 and a != 89:
        count = 0
        for c in str(a):
            count += int(c)**2
        a = count
        if a in memo and a != 89 and a != 1:
            a = memo[a]
            break
    if a == 1:
        return None
    memo[a].append(n)
    memo[n] = a
    return memo[n]

def find_perms(n):
    s = str(n)
    t = itertools.permutations(s)
    res = {}
    for i in t:
        res[int(''.join(i))] = None
    return res

def chain_recursive(n):
    if n in memo:
        return None
    if n == 89 or n == 1:
        return None
    count = 0
    for c in str(n):
        count += int(c)**2
    try:
        a = memo[count]
        if a == 89:
            for i in find_perms(n).keys():
                if i not in memo:
                    res.append(i)
                    memo[i] = 89
            return memo[n]
        if a == 1:
            for i in find_perms(n).keys():
                if i not in memo:
                    ones.append(i)
                    memo[i] = 1
            return memo[n]
    except KeyError:
        memo[n] = chain_recursive(count)
        if memo[n] == 89:
            res.append(n)
        if memo[n] == 1:
            ones.append(n)
        return memo[n]

#print(chain_recursive(2), res, memo)

j = 0
start = time.time()
for i in range(9999999, 1, -1):
    if i not in memo:
        chain_recursive(i)
        if time.time() - start > 10:
            print(i, len(res)+len(ones))
            j += 100
            start = time.time()
            

print(len(res) + len(ones))

#sorted(memo.keys())


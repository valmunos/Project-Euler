def collatz(n):
    count = 0
    while True:
        try:
            return memo[n] + count
        except KeyError:
            if n % 2 == 0:
                count += 1
                n //= 2
            if n == 1:
                count += 1
                break
            if n % 2 != 0:
                count += 1
                n = 3*n + 1
    return count

memo = {}
start = time.time()
for n in range(1, 1000000):
    memo[n] = collatz(n)

t = []
for key, value in memo.items():
    p = []
    p.append(value)
    p.append(key)
    t.append(p)

t = sorted(t, reverse = True)
print(t[0])
    

import time

memo = {1:1}

def collatz(n):
    try:
        return memo[n]
    except KeyError:
        if n % 2 == 0:
            a = n // 2
            memo[n] = 1 + collatz(a)
            return memo[n]
        if n % 2 != 0:
            a = 3*n + 1
            memo[n] = 1 + collatz(a)
            return memo[n]

start = time.time()
for i in range(1, 1000001):
    collatz(i)

print(time.time() - start)



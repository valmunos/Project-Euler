cache = {1:1, 2:1}

def fib(n):
    try:
        return cache[n]
    except KeyError:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

i = 3
print(str(fib(541))[:9])

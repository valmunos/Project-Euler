known = {0:0, 1:1}

def fib(n):
    if n in known:
        return known[n]
    res = fib(n-1) + fib(n-2)
    known[n] = res
    return res

def sum_evens(d):
    total = 0
    for key in d:
        if d[key] % 2 == 0:
            total += d[key]
    return total

i = 0
while fib(i) <= 4e6:
    print(i)
    i += 1

print(fib(33))
print(sum_evens(known))

import math

t = []

def factorial_sum(n):
    s = str(n)
    count = 0
    for c in s:
        count += math.factorial(int(c))
    return count


for i in range(3, 10000000):
    if i == factorial_sum(i):
        t.append(i)
        print(i)

print(sum(t))

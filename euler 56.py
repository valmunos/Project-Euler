import math

def digit_sum(n):
    count = 0
    for c in str(n):
        count += int(c)
    return count

res = []
for i in range(50, 100):
    for j in range(50, 100):
        n = digit_sum(i**j)
        if n == 972:
            print(i, j)

#res = sorted(res, reverse=True)

#print(res[0])

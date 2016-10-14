import math

count = 0
for i in range(23, 101):
    for j in range(1, i):
        num = math.factorial(i)
        den = math.factorial(j) * math.factorial(i - j)
        if num / den > 1000000:
            count += 1
            print(count)
        

prod = 1
for i in range(1, 101):
    prod *= i

s = str(prod)

count = 0
for c in s:
    count += int(c)

print(count)

t = {}
total = 0
for i in range(2, 1000000):
    s = str(i)
    count = 0
    for c in s:
        count += int(c)**5
    if count == i:
        t[i] = None
        total += i

print(total)

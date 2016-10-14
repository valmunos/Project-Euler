check = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

res = []
for n in range(1, 10000):
    s = str(n)
    i = 2
    while len(s) < 9:
        s += str(n*i)
        i += 1
    if sorted(s) == check:
        res.append(int(s))

res.sort()
print(res[-1])

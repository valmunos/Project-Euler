count = 0
res = []
for j in range(1, 7071):
    count = 0
    i = j
    while True:
        count += i**2
        if count > 100000000:
            res.append((j, i))
            break
        i += 1

print(res[0])

new = []

def is_pali(n):
    s = str(n)
    if s == s[::-1]:
        return True

for t in res:
    n = t[1] - t[0] - 1
    new.append(n)

sums = []

for t in res:
    for j in range(t[0]+1, t[1]):
        i = t[0]
        count = 0
        while i <= j:
            count += i**2
            i += 1
        if is_pali(count):
            #print(t[0], j, count)
            sums.append(count)

sums.sort()
print(sums)

def is_pali(n):
    s = str(n)
    if s == s[::-1]:
        return True

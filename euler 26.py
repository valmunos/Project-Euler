d = {}

for i in range(7,1000,2):
    #print(i)
    k = 1
    while i % 5 != 0:
        if 10**k % i == 1:
            d[i] = k
            #print(d)
            break
        k += 1

t = []
for key, val in d.items():
    t.append((val, key))

t.sort(reverse = True)
print(t[0])

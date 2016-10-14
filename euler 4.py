from pali_slice import pali_slice
palis = []
for i in range(100,1000):
    for n in range(100,1000):
        if pali_slice(str(i * n)):
            palis.append(i * n)

palis.sort()
print(palis[-1])

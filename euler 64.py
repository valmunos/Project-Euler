import math

def cycle(n):
    if math.sqrt(n) % 1 == 0.0:
        return 0
    res = []
    comp = math.sqrt(n)//1
    den = n - comp**2
    while True:
        num = math.sqrt(n) + comp
        a = num/den//1
        res.append((a, comp, den))
        comp = (comp - den*a)*-1
        den = (n - comp**2)/den
        for i in res:
            if comp == i[1] and den == i[2]:
                #print(res)
                return len(res)
    

count = 0
for i in range(10001):
    if cycle(i) % 2 == 1:
        count += 1

print(count)

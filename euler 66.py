import math

def cycle(n):
    if math.sqrt(n) % 1 == 0.0:
        return 0
    comp = math.sqrt(n)//1
    den = n - comp**2
    res = [comp]
    mem = []
    while True:
        num = math.sqrt(n) + comp
        a = num/den//1
        res.append(a)
        mem.append((comp, den))
        comp = (comp - den*a)*-1
        den = (n - comp**2)/den
        for i in mem:
            if comp == i[0] and den == i[1]:
                return res

def find_n(n):
    if math.sqrt(n) % 1 == 0.0:
        return (1, 0)
    a = int(math.sqrt(n))
    c = cycle(n)
    nums = [1,a]
    dens = [0,1]
    count = 0
    while True:
        for i in range(1, len(c)):
            nums.append(nums[-1]*int(c[i]) + nums[-2])
            dens.append(dens[-1]*int(c[i]) + dens[-2])
            count += 1
            if nums[-1]**2 - n*dens[-1]**2 == 1:
                return (n, len(c), count)
            
res = []
for i in range(1, 101):
    res.append(find_n(i))

print(res)


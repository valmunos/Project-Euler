import itertools

def tria(n):
    p = n*(n+1)/2
    return int(p)

def square(n):
    return n**2

def penta(n):
    p = n*(3*n-1)/2
    return int(p)

def hexa(n):
    p = n*(2*n-1)
    return p

def hepta(n):
    p = n*(5*n-3)/2
    return int(p)

def octa(n):
    p = n*(3*n-2)
    return p

tris = {}
squares = {}
pentas = {}
hexas = {}
heptas = {}
octas = {}

n = 1
while True:
    if 1000 <= tria(n) < 10000 and tria(n) % 100 >= 10:
        tris[tria(n)] = {}
    if 1000 <= square(n) < 10000 and square(n) % 100 >= 10:
        squares[square(n)] = {}
    if 1000 <= penta(n) < 10000 and penta(n) % 100 >= 10:
        pentas[penta(n)] = {}
    if 1000 <= hexa(n) < 10000 and hexa(n) % 100 >= 10:
        hexas[hexa(n)] = {}
    if 1000 <= hepta(n) < 10000 and hepta(n) % 100 >= 10:
        heptas[hepta(n)] = {}
    if 1000 <= octa(n) < 10000 and octa(n) % 100 >= 10:
        octas[octa(n)] = {}
    n += 1
    if tria(n) > 10000:
        break
dicts = [squares, pentas, hexas, heptas, octas]
strings = ['square', 'penta', 'hexa', 'hepta', 'octa']
for n in tris.keys():
    for t in itertools.permutations(dicts):
        nums = []
        nums.append(n)
        res = {n % 100:-1}
        for i in range(len(t)):
            flag = False
            for z in t[i].keys():
                if z // 100 in res:
                    if res[z // 100] == i - 1:
                        res[z % 100] = i
                        nums.append(z)
                        flag = True
                        break
            if not flag:
                break
            if i == 4:
                if z % 100 == n // 100:
                    print(res, sum(nums))
    


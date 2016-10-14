def t(n): return n * (n + 1)/2
def p(n): return n * (3*n - 1)/2
def h(n): return n * (2*n - 1)

tri = {}
penta = {}
hexa = {}
n = 1
while True:
    penta[p(n)] = None
    hexa[h(n)] = None
    tri[n] = t(n)
    if tri[n] in penta and tri[n] in hexa:
        print(tri[n])
    n += 1

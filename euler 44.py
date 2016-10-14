def p(n):
    return int(n * (3*n - 1) / 2)

penta = {0:0}
res = {}
n = 1
flag = True
while flag:
    penta[n] = p(n)
    res[penta[n]] = penta[n]
    i = n - 1
    while penta[n] - penta[i] < penta[i]:
        if penta[n] - penta[i] in res:
            if 2*penta[i] - penta[n] in res:
                print(2*penta[i] - penta[n])
                flag = False
                break
        i -= 1
    n += 1

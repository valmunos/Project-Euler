fin = open('euler_11.txt')
rows = []
for line in fin:
    t = []
    line = line.strip('\n')
    for s in line.split():
        n = int(s)
        t.append(n)
    rows.append(t)


def multiply(n,t):
    prod = t[n] * t[n + 1] * t[n + 2] * t[n + 3]
    return prod

def row_product(t):
    products = []
    for row in t:
        for i in range(len(row)-3):
            p = multiply(i, row)
            products.append(p)
    return max(products)

def make_columns(t):
    rows = []
    for i in range(20):
        p = []
        for row in t:
            p.append(row[i])
        rows.append(p)
    return rows

def make_diag_r(t):
    rows = []
    for i in range(16, -1, -1):
        p = []
        for row in t:
            p.append(row[i])
            i += 1
            if i == 20:
                break
        rows.append(p)
    return rows

def make_diag_l(t):
    rows = []
    for i in range(3, 20):
        p = []
        for row in t:
            p.append(row[i])
            i -= 1
            if i < 0:
                break
        rows.append(p)
    return rows

columns = make_columns(rows)
diagr = make_diag_r(rows)
diagl = make_diag_l(rows)

print(row_product(diagl))


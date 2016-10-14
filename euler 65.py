def convergents(n):
    res = []
    for i in range(n):
        if i % 3 == 1:
            res.append(i//3 * 2 + 2)
        else: res.append(1)
    return res

def find_fraction(n, num=1, den=2):
    for i in range(n-1):
        a = 2*den + num
        num = den
        den = a
        print(num, den)
    num = num + den
    return((num, den))

def find_e(n, num=1):
    c = convergents(n)
    c.reverse()
    den = c[0]
    for i in range(1, len(c)):
        a = c[i]*den + num
        num = den
        den = a
        #print(num, den)
    num = num + 2*den
    return((num, den))

n = find_e(99)[0]
s = str(n)
count = 0
for c in s:
    count += int(c)

print(count)
    

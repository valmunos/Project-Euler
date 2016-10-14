#num = 3, 2*3+1, 2*7+3, 2*17+7, 2*41+17, 2*99+41 = 2*(n-1) + (n-2); n(1,2) = 3, 7
#den = 2, 2*2+1, 2*5+2, 2*12+5 = 2*(n-1) + (n-2); n(1,2) = 2, 5

num = {1:3, 2:7}
den = {1:2, 2:5}

def make_num(n):
    num[n] = 2*num[n-1] + num[n-2]
    return num[n]

def make_den(n):
    den[n] = 2*den[n-1] + den[n-2]
    return den[n]

i=3
count = 0
while i <= 1000:
    s1 = str(make_num(i))
    s2 = str(make_den(i))
    if len(s1) > len(s2):
        count += 1
    i += 1

print(count)

import math

def digit_sum(n):
    count = 0
    while n > 0:
        count += n%10
        n //= 10
    return count

def is_power(a,b):
    if a == 1:
        return False
    n = round(math.log(b,a))
    if a**n == b:
        print(a,b,n)
        return True
    return False

i = 10
res = []
'''
while True:
    s = digit_sum(i)
    if is_power(s, i):
        res.append(i)
    if len(res) == 30:
        break
    i += 1
    '''

for i in range(2, 101):
    for j in range(1, 100):
        n = i**j
        if n > 10 and digit_sum(n) == i:
            res.append(n)

res.sort()
print(res[29])

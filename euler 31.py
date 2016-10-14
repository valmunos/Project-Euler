import math

ways = []

def f200(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    print('200')
    return f100(n) + f200(n - 200)

def f100(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    print('100')
    return f50(n) + f100(n - 100)

def f50(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    print('50')
    return f20(n) + f50(n - 50)

def f20(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    print('20')
    return f10(n) + f20(n - 20)

def f10(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    print('10')
    return f5(n) + f10(n - 10)

def f5(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    print('5')
    return f2(n) + f5(n - 5)

def f2(n):
    print('2')
    return n // 2 + f1(n)

def f1(n):
    print('1')
    if n > 0:
        return 1
    else:
        return 0
'''
def f(n):
    return f1(n) + f2(n) + f5(n) + f10(n) + f20(n) + f50(n) + f100(n) + f200(n)

for i in range(201):
    res = f(i)
    ways.append(res)
'''
total = []
print(f200(200))

#print(total)

#print(f100(200) + f50(200) + f20(200) + f10(200) + f5(200) + f2(200) + 2)
#print(f100(200), f50(200), f20(200), f10(200), f5(200), f2(200))   

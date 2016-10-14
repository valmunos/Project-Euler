def increasing(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] > s[i + 1]:
            return False
    return True

def decreasing(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] < s[i + 1]:
            return False
    return True

def isbouncy(n):
    if not increasing(n) and not decreasing(n):
        return True

count = 0
i = 100
while True:
    if isbouncy(i):
        count += 1
    if count/i == 0.99:
        print(i)
    i += 1

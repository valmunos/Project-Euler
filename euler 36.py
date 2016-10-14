def is_pali(n):
    s = str(n)
    t = s[::-1]
    return s == t

def bin_pali(n):
    s = bin(n).lstrip('0b')
    t = s[::-1]
    return s == t

t = []

for i in range(1, 1000000, 2):
    if is_pali(i) and bin_pali(i):
        t.append(i)
        print(i)

print(sum(t))

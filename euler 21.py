divisors = {1:[1]}

for n in range(1, 10000):
    i = 1
    while i <= n / 2:
        if n % i == 0:
            divisors.setdefault(n, []).append(i)
        i += 1

print(divisors[100])
amicable = []
for key in divisors.keys():
    a = sum(divisors[key])
    try:
        b = sum(divisors[a])
    except KeyError:
        b = None
    if key == b:
        amicable.append(a)
        amicable.append(b)
    

print(amicable)

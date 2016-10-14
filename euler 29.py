t = {}

for i in range(2, 101):
    for j in range(2, 101):
        n = i**j
        if n not in t:
            t[n] = None

print(len(t))

d = []
check = '123456789'
for i in range(10, 100):
    for j in range(100, 1000):
        s1 = str(i)
        s2 = str(j)
        s3 = str(i*j)
        s = s1 + s2 + s3
        s = ''.join(sorted(s))
        if s == check:
            print(i*j)
            if i*j not in d:
                d.append(i*j)

for i in range(1, 10):
    for j in range(1000, 10000):
        s1 = str(i)
        s2 = str(j)
        s3 = str(i*j)
        s = s1 + s2 + s3
        s = ''.join(sorted(s))
        if s == check:
            print(i*j)
            if i*j not in d:
                d.append(i*j)

print(sum(d))

                
        

for i in range(10, 99):
    for j in range(i+1, 100):
        s1 = str(i)
        s2 = str(j)
        i1 = int(s1[0])
        i2 = int(s1[1])
        i3 = int(s2[0])
        i4 = int(s2[1])
        if i3 != 0:
            if i1 == i4 and i2 / i3 == i / j:
                print(i,j)
        if i4 != 0:
            if i2 == i3 and i1 / i4 == i / j:
                print(i,j)
        

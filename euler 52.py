import time

i = 1
start = time.time()
while True:
    flag = True
    t = sorted(str(i))
    for j in range(2, 7):
        if sorted(str(i*j)) != t:
            flag = False
            break
    if flag:
        print(i)
        break
    if time.time() - start > 10:
        print(i)
        start = time.time()
    i += 1

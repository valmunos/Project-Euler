import math

cubes = {}


i = 344
while True:
    s = tuple(sorted(str(i**3)))
    #print(s)
    cubes.setdefault(s, []).append(i**3)
    if len(cubes[s]) == 5:
        print(cubes[s][0])
        break
    i += 1


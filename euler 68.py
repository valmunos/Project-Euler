import itertools



numbers = [1,2,3,4,5,6,7,8,9,10]
res = []
num = tuple(numbers)
for b in range(10):
    numbers = [1,2,3,4,5,6,7,8,9,10]
    o1 = numbers[b]
    del numbers[b]
    num0 = tuple(numbers)
    for i in range(len(num0)):
        numbers = list(num0)
        i1 = num0[i]
        del numbers[i]
        num1 = tuple(numbers)
        for j in range(len(num1)):
            numbers = list(num1)
            o2 = num1[j]
            del numbers[j]
            #print(numbers)
            if o1 - o2 + i1 in numbers:
                i3 = o1 - o2 + i1
                del numbers[numbers.index(i3)]
                num2 = tuple(numbers)
                #print(numbers)
                for k in range(len(num2)):
                    numbers = list(num2)
                    o3 = num2[k]
                    del numbers[k]
                    num3 = tuple(numbers)
                    for l in range(len(num3)):
                        numbers = list(num3)
                        o4 = num3[l]
                        del numbers[l]
                        if o3 - o4 + i3 in numbers:
                            i5 = o3 - o4 + i3
                            del numbers[numbers.index(i5)]
                            num4 = tuple(numbers)
                            for m in range(len(num4)):
                                numbers = list(num4)
                                o5 = num4[m]
                                del numbers[m]
                                i2 = o5 - o1 + i5
                                if i2 in numbers:
                                    del numbers[numbers.index(i2)]
                                    i4 = o2 - o3 + i2
                                    if i4 in numbers:
                                        del numbers[numbers.index(i4)]
                                #if i2 and i4 in numbers and i2 != i4:
                                        outer = [o1, o2, o3, o4, o5]
                                        inner = [i1, i2, i3, i4, i5]
                                        a = outer.index(min(outer))
                                        s = ''
                                        outer = outer[a:] + outer[:a]
                                        inner = inner[a:] + inner[:a] + [inner[a]]
                                        for i in range(len(outer)):
                                            s += str(outer[i]) + str(inner[i]) + str(inner[i+1])
                                        print(s)
#print(res)


'''
if o1 + i1 != o2 + i2:
    flag = False
    break
if o2 + i2 != o3 + i4:
    flag = False
    break
if o3 + i3 != o4 + i5:
    flag = False
    break
if 04 + i4 != o5 + i1:
    flag = False
    break
if 05 + i5 != o1 + i2:
    flag = False
    break
if flag:
    res.append(solution)
'''

import math

squares = []
for i in range (300):
    squares.append(i**2)

def triplets():
    a = 4
    for n in range(1,26):
        b = (a**2 - 4)/4
        c = b + 2
        print (a, b, c)
        a += 2

def triplets2():
    a = 3
    while a < 50:
        b = (a**2-1)/2
        c = b + 1
        print(a, b, c)
        a += 2

def triplets3():
    squares = []
    for i in range (100):
        squares.append(i**2)
    b = 1
    c = 4
    while b < 600:
        diff = c**2 - b**2
        if diff in squares:
            a = int(math.sqrt(diff))
            print (a, b, c)
        b += 1
        c += 1

def triplets4():
    b = 1
    c = 5
    while b < 700:
        diff = c**2 - b**2
        if diff in squares:
            a = int(math.sqrt(diff))
            print (a, b, c)
        b += 1
        c += 1
        
def triplets5():
    b = 1
    c = 6
    while b < 700:
        diff = c**2 - b**2
        if diff in squares:
            a = int(math.sqrt(diff))
            print (a, b, c)
        b += 1
        c += 1
      
def triplets6():
    b = 1
    c = 7
    while b < 700:
        diff = c**2 - b**2
        if diff in squares:
            a = int(math.sqrt(diff))
            print (a, b, c)
        b += 1
        c += 1

def triplets_n():
    flag = True
    count = 0
    while flag:
        b = 1
        c = 8 + count
        while b < 700:
            diff = c**2 - b**2
            if diff in squares:
                a = int(math.sqrt(diff))
                print(a, b, c)
                if (a + b + c) == 1000:
                    print (a, b, c, '1000!!!!!')
                    flag = False
            b += 1
            c += 1
        count += 1

triplets_n()

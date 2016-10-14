def top_right():
    count = 0
    for n in range(3, 1003, 2):
        count += n**2
    return count

def top_left():
    count = 0
    for n in range(3, 1003, 2):
        num = n**2 - n + 1
        count += num
    return count

def bot_left():
    count = 0
    for n in range(3, 1003, 2):
        num = n**2 - 2*n + 2
        count += num
    return count

def bot_right():
    count = 0
    for n in range(3, 1003, 2):
        num = n**2 - 3*n + 3
        count += num
    return count

total = top_right() + top_left() + bot_left() + bot_right() + 1
print(total)


fin = open('poker.txt')

p1 = 0
p2 = 0

face = {'T':10, 'J':11, 'Q': 12, 'K': 13, 'A': 14}
hands = {'HC': 0, '1P': 1, '2P': 2, '3K': 3, 'S': 4,
         'F':5, 'FH': 6, '4K': 7, 'SF': 8, 'RF': 9}

def convert_faces(s):
    res = []
    for c in s:
        if c in face.keys():
            res.append(face[c])
        else: res.append(int(c))
    res.sort()
    return res

def check_pairs(t):
    kicker = []
    res = []
    for c in t:
        if t.count(c) > 1:
            res.append((t.count(c), c))
            for i in range(t.count(c)):
                t.remove(c)
        else:
            kicker.append(c)
            t.remove(c)
    kicker.reverse()
    return res, kicker

def check_straight(t):
    if len(t) == 5:
        flag = True
        for z in range(4):
            if kicker[z+1] - kicker[z] != 1:
                flag = False
                break
        if flag:
            res.append('S')

#def check_flush(t):    

def analyze_hand(f, s):
    kicker = []
    res = []
    h = convert_faces(f)
    res, kicker = check_pairs(h)
    if res == []:
        res = check_straight(kicker)
    if s.count(s[0]) == 5:
        res.append('F')
    return res, kicker, h
    
            
    

for line in fin:
    line = line.replace(' ', '')
    face1 = line[0:10:2]
    suit1 = line[1:10:2]
    face2 = line[10:20:2]
    suit2 = line[11:20:2]
    print(analyze_hand(face1, suit1))

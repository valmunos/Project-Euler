fin = open('names.txt')
names = []
for line in fin:
    line = line.strip('\n')
    for word in line.split(','):
        word = word.strip('"')
        #print(word)
        names.append(word)

names.sort()
scores = []
for name in names:
    sun = 0
    for c in name:
        sun += (ord(c)-64)
    scores.append(sun)

score = 0
for i in range(len(names)):
    n = scores[i] * (i + 1)
    score += n

print(score) 

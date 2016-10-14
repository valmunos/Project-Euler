fin = open('triangle.txt')
rows = []
for line in fin:
    t = []
    line = line.strip('\n')
    for s in line.split(' '):
        n = int(s)
        t.append(n)
    rows.append(t)

rows.reverse()

for n in range(len(rows)):
    for i in range(len(rows[n])-1):
        if rows[n][i] >= rows[n][i+1]:
            rows[n+1][i] = rows[n+1][i] + rows[n][i]
        else:
            rows[n+1][i] = rows[n+1][i] + rows[n][i+1]

print(rows[-1][0])

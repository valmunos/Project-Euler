fin = open('euler42.txt')
tri = [1]
count = 0

def score(s):
    count = 0
    for c in s:
        count += ord(c) - 64
    return count

def t(n): return int(n * (n + 1)/2)

for line in fin:
    for s in line.split(','):
        s = s.strip('"')
        while score(s) > tri[-1]:
            tri.append(t(len(tri)+1))
        if score(s) in tri:
            count += 1
print(tri)
print(count)


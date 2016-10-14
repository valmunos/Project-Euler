sequence = []
cache = []

def product(t):
    p = 1
    for i in t:
        p *= i
    return p

def process_sequence(n):
    global sequence
    if len(sequence) == 13:
        sequence = sequence[1:]
        sequence.append(n)
    if len(sequence) < 13:
        sequence.append(n)
    if len(sequence) == 13:
        global cache
        cache.append(product(sequence))

def process_line(s):
    for c in s:
        process_sequence(int(c))

def process_text(file):
    fin = open(file)
    for line in fin:
        line = line.strip('\n')
        process_line(line)
    cache.sort()
    return cache[-1]

        

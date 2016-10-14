import time

start = time.time()
count = 0
for i in range(1, 1001):
    count += ((i**i) % 10000000000)
    
print(count%10000000000)

import random

counts = [0, 0, 0, 0, 0, 0, 0]
for i in range(1, 101):
    roll = random.randrange(1, 7)
    counts[roll] = counts[roll] + 1
for i in range(1, 7):
    print(str(i) + ': ' + str(counts[i]))

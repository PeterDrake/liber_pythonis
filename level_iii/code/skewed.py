import random

# Roll dice
counts = [0] * 7
for i in range(1, 501):
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    roll3 = random.randrange(1, 7)
    lowest = min(roll1, roll2, roll3)
    counts[lowest] += 1

# Display result
for i in range(1, 7):
    print(str(i) + ': ' + str(counts[i]))

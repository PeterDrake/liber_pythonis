import random

# Roll dice
counts = [0] * 13
for i in range(1, 201):
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    sum = roll1 + roll2
    counts[sum] += 1

# Display results
for i in range(2, 13):
    print(str(i) + ': ' + str(counts[i]))

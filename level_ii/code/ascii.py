import random

# Roll dice
counts = [0] * 13
for i in range(1, 501):
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    sum = roll1 + roll2
    counts[sum] += 1

# Display result
for i in range(2, 13):
    stars = '*' * counts[i]
    if i < 10:
        print(' ' + str(i) + ': ' + stars)
    else:
        print(str(i) + ': ' + stars)

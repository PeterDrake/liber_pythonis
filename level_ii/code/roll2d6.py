import random
rolls = []
for i in range(1, 21):
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    sum = roll1 + roll2
    rolls += [sum]
print(rolls)

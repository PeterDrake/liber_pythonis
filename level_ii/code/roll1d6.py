import random
rolls = []
for i in range(1, 21):
    roll = random.randrange(1, 7)
    rolls = rolls + [roll]
print(rolls)

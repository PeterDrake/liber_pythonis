import random

# Make up some data
ones = [1] * 10
twos = [2] * 20
threes = [3] * 30
numbers = ones + twos + threes

# Take a sample
sample = []
for i in range(1, 11):
    index = random.randrange(len(numbers))
    n = numbers[index]
    sample += [n]

# Print sample
print(sample)

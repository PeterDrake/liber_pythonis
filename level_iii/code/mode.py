numbers = [1, 5, 3, 2, 4, 3, 2, 3, 1, 6, 4, 6, 3, 6]

mode = 0
highest_count = 0
for n in numbers:
    # How often does n occur?
    count = 0
    for m in numbers:
        if n == m:
            count += 1
    # Is this a new record?
    if count > highest_count:
        highest_count = count
        mode = n
print(mode)

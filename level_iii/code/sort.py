numbers = [2, 1, 8, 7]
sorted = []
for i in range(0, len(numbers)):
    # Find index of smallest remaining number
    min_index = 0
    for j in range(1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    # Add it to sorted
    sorted += [numbers[min_index]]
    # Remove it from numbers
    remaining = []
    for j in range(0, len(numbers)):
        if j != min_index:
            remaining += [numbers[j]]
    numbers = remaining
print(sorted)


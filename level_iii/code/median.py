numbers = [4, 2, 8, 5, 6]

# Sort the list of numbers
n = len(numbers)
for i in range(1, n):
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

# Find the median
n = len(sorted)
if n % 2 == 1:  # Odd length
    median = sorted[n // 2]
else:
    median = (sorted[n // 2] + sorted[(n // 2) - 1]) / 2

# Display the result
print(median)
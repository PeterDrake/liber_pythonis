sorted = [2, 4, 5, 6, 8]

# Find the median
n = len(sorted)
if n % 2 == 1:  # Odd length
    median = sorted[n // 2]
else:
    median = (sorted[n // 2] + sorted[(n // 2) - 1]) / 2

# Display the result
print(median)

numbers = [2, 1, 8, 7]
n = len(numbers)
for i in range(0, n):
    # Find the smallest number at index i or later
    min = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min]:
            min = j
    # Swap that number with the one at index i
    temp = numbers[min]
    numbers[min] = numbers[i]
    numbers[i] = temp
print(numbers)

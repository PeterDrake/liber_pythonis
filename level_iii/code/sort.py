numbers = [2, 1, 8, 7]
numbers = [8,6,7,5,3,0,9]
n = len(numbers)
for i in range(1, n):
    moving = numbers[i]
    print(moving)
    for j in range(i, 0, -1):
        print(moving)
        print(numbers[j-1])
        if moving < numbers[j - 1]:
            print('moving')
            numbers[j] = numbers[j - 1]
            print(numbers)
        else:
            j += 1
            break
    numbers[j - 1] = moving
    print(numbers)
print(numbers)


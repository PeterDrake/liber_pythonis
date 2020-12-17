numbers = [1, 2, 1, 1, 3, 1, 2, 1, 3, 3]


def count(x):
    just_x = [n for n in numbers if n == x]
    return len(just_x)


mode = max(numbers, key=count)


print(mode)

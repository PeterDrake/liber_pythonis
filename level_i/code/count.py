def count(x, ls):
    just_x = [n for n in numbers if n == x]
    return len(just_x)


numbers = [1, 3, 2, 1, 2, 1, 1, 3, 2, 1]
print(count(1, numbers))

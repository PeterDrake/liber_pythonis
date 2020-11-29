values = [1, 4, 6, 5, 2, 4, 3, 5, 1, 3, 4, 6, 4]
for i in range(max(values) + 1):
    if i < 10:
        padding = ' '
    else:
        padding = ''
    stars = '*' * values.count(i)
    print(padding + str(i) + ': ' + stars)

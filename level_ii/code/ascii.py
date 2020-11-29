values = [9, 2, 5, 6, 0, 3, 1, 8, 7, 4, 2]
for i in range(len(values)):
    if i < 10:
        padding = ' '
    else:
        padding = ''
    stars = '*' * values[i]
    print(padding + str(i) + ': ' + stars)


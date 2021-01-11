def median(ls):
    s = sorted(ls)
    if len(s) % 2 == 1:
        middle = len(s) // 2
        return s[middle]
    else:
        left = (len(s) - 1) // 2
        right = len(s) // 2
        return (s[left] + s[right]) / 2


numbers = [34, 75, 49, 38, 46, 74, 92, 13, 66]
print(median(numbers))

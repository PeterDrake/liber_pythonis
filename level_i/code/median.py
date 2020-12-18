def median(ls):
    sn = sorted(ls)
    if len(ls) % 2 == 0:
        left = (len(sn) - 1) // 2
        right = len(sn) // 2
        return (sn[left] + sn[right]) / 2
    else:
        middle = (len(sn) - 1) // 2
        return sn[middle]


numbers = [34, 75, 49, 38, 46, 74, 92, 13, 66]
print(median(numbers))

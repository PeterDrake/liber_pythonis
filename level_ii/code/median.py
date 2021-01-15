def median(data):
    n = len(data)
    s = sorted(data)
    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[(n - 1) // 2] + s[n // 2]) / 2


numbers = [34, 75, 49, 38, 46, 74, 92, 13, 66]
print(median(numbers))

def percentile(p, data):
    return sorted(data)[len(data) * p // 100]


print(percentile(75, [4, 8, 16, 32]))

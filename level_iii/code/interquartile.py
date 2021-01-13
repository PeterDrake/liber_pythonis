def percentile(p, data):
    return sorted(data)[len(data) * p // 100]


def interquartile_range(data):
    return percentile(75, data) - percentile(25, data)


print(interquartile_range(range(100)))

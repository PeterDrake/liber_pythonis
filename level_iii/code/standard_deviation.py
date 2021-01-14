import math


def mean(data):
    return sum(data) / len(data)


def standard_deviation(data):
    squared_deviations = [(x - mean(data)) ** 2 for x in data]
    variance = sum(squared_deviations) / len(data)
    return math.sqrt(variance)


xs = [36, 41, 75, 38, 12, 28, 17, 98, 53, 66]
print(standard_deviation(xs))

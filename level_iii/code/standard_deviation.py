from math import sqrt
from statistics import mean

xs = [36, 41, 75, 38, 12, 28, 17, 98, 53, 66]

squared_deviations = [(x - mean(x)) ** 2 for x in xs]
variance = sum(squared_deviations) / len(xs)
standard_deviation = sqrt(variance)

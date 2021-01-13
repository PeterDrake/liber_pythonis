import csv
import math


def mean(ls):
    return sum(ls) / len(ls)


def standard_deviation(data):
    squared_deviations = [(x - mean(data)) ** 2 for x in data]
    variance = sum(squared_deviations) / len(data)
    return math.sqrt(variance)


with open('kid-weights-UsingR.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('Standard deviation: ' + str(standard_deviation(heights)))

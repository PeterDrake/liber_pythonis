import csv


def percentile(p, data):
    return sorted(data)[len(data) * p // 100]


def interquartile_range(data):
    return percentile(75, data) - percentile(25, data)


with open('kid-weights-UsingR.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('Interquartile range: ' + str(interquartile_range(heights)))

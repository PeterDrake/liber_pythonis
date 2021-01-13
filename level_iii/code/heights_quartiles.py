import csv


def percentile(p, data):
    return sorted(data)[len(data) * p // 100]


with open('kid-weights-UsingR.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('First quartile: ' + str(percentile(25, heights)))
print('Third quartile: ' + str(percentile(75, heights)))

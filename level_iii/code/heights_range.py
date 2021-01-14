import csv


def data_range(data):
    return max(data) - min(data)


with open('nchs.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('Range of heights: ' + str(data_range(heights)))

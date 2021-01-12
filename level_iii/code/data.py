import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    next(reader)  # Discards header row
    print(type(reader))
    result = [int(row[0]) for row in reader]
    print(result)

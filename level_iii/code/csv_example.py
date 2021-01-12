import csv

with open('data.csv') as file:
    reader = csv.DictReader(file)

rows = [row for row in reader]
ages = [int(row['age']) for row in rows]
print(ages)

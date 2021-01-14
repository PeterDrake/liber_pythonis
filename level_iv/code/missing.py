import csv

with open('missing.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

rows = [r for r in rows if not (r['income'] == '-' or r['expense'] == '-')]

incomes = [int(r['income']) for r in rows]
expenses = [int(r['expense']) for r in rows]

print(incomes)
print(expenses)

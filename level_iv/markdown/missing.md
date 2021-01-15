# Dealing With Missing Data

Real data are rarely as clean as the NCHS data. One common problem is missing data; sometimes a value isn't present
because a survey responded didn't fill out one field, a sensor malfunctioned, etc.

The most reasonable response is to eliminate the offending rows from the data.

Suppose you have the following data in `missing.csv`:

```csv
income,expense
10,12
-,11
14,-
15,9
```

Here is a program to print the incomes and expenses from the rows without missing data:

```python
import csv

with open('missing.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

rows = [r for r in rows if not (r['income'] == '-' or r['expense'] == '-')]

incomes = [int(r['income']) for r in rows]
expenses = [int(r['expense']) for r in rows]

print(incomes)
print(expenses)
```

This prints:

```python
[10, 15]
[12, 9]
```

The key line is

```python
rows = [r for r in rows if not (r['income'] == '-' or r['expense'] == '-')]
```

which keeps only those rows of `r` that do *not* meet the condition:

```python
(r['income'] == '-' or r['expense'] == '-')
```

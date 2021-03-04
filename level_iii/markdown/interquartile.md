# Interquartile Range (Range of the Middle Half of the Data)

## Idea of the Interquartile Range

The ***interquartile range (IQR)*** is the difference between the third and first quartiles.

Compared to the range of the entire data set, the interquartile range is less sensitive to outliers.

## Computing the Interquartile Range in Python

Since you already have a definition of `percentile`, this is trivial:

<!--interquartile.py-->
```python
def interquartile_range(data):
    return percentile(75, data) - percentile(25, data)
```

Here's a program to compute the interquartile range for heights from the NCHS data:

<!--heights_interquartile.py-->
```python
import csv

def percentile(p, data):
    return sorted(data)[len(data) * p // 100]

def interquartile_range(data):
    return percentile(75, data) - percentile(25, data)

with open('nchs.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('Interquartile range: ' + str(interquartile_range(heights)))
```

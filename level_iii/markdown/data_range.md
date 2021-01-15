# The Range of a List of Numbers

## What is the Range?

The ***range*** is one of three ***measures of spread*** that you will study.  It is one way to measure how spread out values of a data set are.  

The range is only used with quantitative variables.  To compute the range of a data set you just subtract the lowest data value from the highest data value.  The number you get is the range of the data set.

## Computing the Range in Python

This is easy. There is one catch: since `range` is already the name of a built-in Python function that does something
else, you'll have to call this one `data_range`.

<!--data_range.py-->
```python
def data_range(data):
    return max(data) - min(data)
```

With this definition, `data_range([2, 1, 7, 4])` returns `5`.

Here's a program to compute the range of heights from the NCHS data:

<!--heights_range.py-->
```python
import csv

def data_range(data):
    return max(data) - min(data)

with open('nchs.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('Range of heights: ' + str(data_range(heights)))
```

Notice that the program must include the definition of `data_range`.

## Explorations

1. Compute the range of the data set `[8, 6, 7, 5, 3, 0, 9]` and the range of the data set `[30, 6, 7, 5, 3, 0, 9]`.
   
1. Is the range resistant to outliers?
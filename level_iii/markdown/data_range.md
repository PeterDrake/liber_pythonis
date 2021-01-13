# Range (Low to High)

## Idea of the Range

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

with open('kid-weights-UsingR.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('Range of heights: ' + str(data_range(heights)))
```

Notice that the program must include the definition of `data_range`.
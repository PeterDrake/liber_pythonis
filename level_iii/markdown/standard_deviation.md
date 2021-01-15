# Standard Deviation (Sophisticated Measure of Spread)

## About the Standard Deviation

## Computing the Standard Deviation in Python

Here's the definition, which uses `mean` and (from the `math` library) `sqrt`:

<!--standard_deviation.py-->
```python
def standard_deviation(data):
    squared_deviations = [(x - mean(data)) ** 2 for x in data]
    variance = sum(squared_deviations) / len(data)
    return math.sqrt(variance)
```

Here's a program to compute the standard deviation of heights from the NCHS data:

<!--heights_stddev.py-->
```python
import csv
import math

def mean(data):
    return sum(data) / len(data)

def standard_deviation(data):
    squared_deviations = [(x - mean(data)) ** 2 for x in data]
    variance = sum(squared_deviations) / len(data)
    return math.sqrt(variance)

with open('nchs.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('Standard deviation: ' + str(standard_deviation(heights)))
```


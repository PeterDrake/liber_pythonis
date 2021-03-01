# Percentiles and Quartiles (Dividing up the Data)

## Idea of Percentiles and Quartiles

The (for example) 20th ***percentile*** of a data set is the value *x* where 20% of the data are less than x and 80% are greater than *x*.

This means that, for example, if you scored in the 67% percentile on a standardized test, you did better than 67% of test takers.

The 25th percentile is sometimes called the ***first quartile***. Similarly, the 50th percentile is the ***second quartile*** (and is the same thing as the median). The 75th percentile is the ***third quartile***.

## Computing Percentiles and Quartiles in Python

This is pretty simple:

<!--percentile.py-->
```python
def percentile(p, data):
    return sorted(data)[len(data) * p // 100]
```

If you now define a list `data` and ask for

```python
percentile(75, data)
```

the function picks an index about 75% of the way along `data`. The value at this index in the sorted version of `data`
is returned. This is the 75th percentile, also known as the third quartile. About 75% of the data are less than this
value.

We are glossing over some details about what to do if the data don't divide evenly. Surprisingly, [statisticians have
not agreed on how to handle this situation](https://en.wikipedia.org/wiki/Quartile#Computing_methods). It doesn't matter
much when the data set is large.

Here's a program to compute the first and third quartiles of heights from the NCHS data:

<!--heights_quartiles.py-->
```python
import csv

def percentile(p, data):
    return sorted(data)[len(data) * p // 100]

with open('nchs.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('First quartile: ' + str(percentile(25, heights)))
print('Third quartile: ' + str(percentile(75, heights)))
```

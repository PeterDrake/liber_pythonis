# Percentiles and Quartiles (Dividing up the Data)

## What are Percentiles and Quartiles?

Percentiles are a *measure of spread* used to analyze quantitative data. A *measure of spread* is a tool that helps us understand if the data are tightly bunched around a single value, or if they are more spread out.


Here is an example of a percentile.  Consider the list below.
```python
[1, 1, 4, 5, 11, 15, 21, 45, 45, 67]
```
The number 5 is the 30th percentile of this list because 30% of the numbers on the list are less than or equal to 5, and 5 is the smallest number for which this is true.

We have already seen one important percentile:  the median of a set of data is its 50th percentile.

The word *quartile* is reserved for the data values that split the list into four pieces of equal length. More specifically, the first quartile Q1 is the 25th percentile, the second quartile is the median, and the third quartile Q3 is the 75th percentile. 

The easiest way to compute quartiles by hand is to first find the median of the list, and then the first quartile is the median of the numbers below the median, and the third quartile is the median of the numbers above the median.

For the example above the median is 13, the first quartile is `Q1 = 4` and the third quartile is `Q3 = 45`.


The (for example) 20th ***percentile*** of a data set is the value *x* where 20% of the data are less than *x* and 80% are greater than *x*.

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

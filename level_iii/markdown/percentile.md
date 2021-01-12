# Percentiles and Quartiles (Dividing up the Data)

## Idea of Percentiles and Quartiles

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
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
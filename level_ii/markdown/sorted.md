# The `sorted` Function

The built-in `sorted` function accepts a list and returns a sorted version of that list, so

```python
sorted([7, 2, 5, 4])
```

returns

```python
[2, 4, 5, 7]
```

## Explorations

1. For each program below, predict what will happen when you run it, then test your prediction. Summarize what you learn in your notes.
    <!--sorted_duplicates.py-->
    ```python
    dataq = [1, 2, 3, 3, 2, 1]
    print(sorted(data))
    ```
    <!--sorted_no_side_effects.py-->
    ```python
    data = [2, 1, 4, 3]
    sorted(data)
    print(data)
    ```
    <!--sorted_reassignment.py-->
    ```python
    data = [2, 1, 4, 3]
    data = sorted(data)
    print(data)
    ```
1. For each expression below, predict what will happen when you type it into the interactive console, then test your
prediction. Summarize what you learn in your notes.
   ```python
   sorted(['Mexico', 'United States', 'Canada'])
   ```
   ```python
   sorted('abracadabra')
   ```
   ```python
   sorted(5)
   ```
   ```python
   sorted([[4, 3], [2, 1]])
   ```
   ```python
   sorted(['anteater', 'bat', 'camel'], key=len)
   ```
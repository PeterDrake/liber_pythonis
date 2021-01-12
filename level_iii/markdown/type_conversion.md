# Type Conversion

You have seen a number of Python data types, including `int`, `float`, `list`, `string`, and `bool`.

It is occasionally useful to convert from one type to another. For each type, there is a built-in function with the
same name that converts values to that type. For example,

```python
float('3.14159')
```

returns the `float` value `3.14159`.

## Explorations
1. For each expression below, predict what will happen when you type it into the interactive console, then test your
prediction. Summarize what you learn in your notes.
    ```python
    int(8.0)
    ```
    ```python
    int(3.7)
    ```
    ```python
    int('3.7')
    ```
    ```python
    str(3)
    ```
    ```python
    'The number is ' + 23
    ```
    ```python
    'The number is ' + str(23)
    ```
    ```python
    [bool(x) for x in [0, 1, -1, 0.0, 0.001, [], [1], '', 'hello', 'False']]
    ```
    ```python
    int(True)
    ```
    ```python
    int(False)
    ```


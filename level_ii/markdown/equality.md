# Testing Equality `==`

If you define
```python
x = 5
```
then the expression
```python
x == 5
```
returns `True`. This is a ***Boolean*** value (named for the logician George Boole), called a `bool` in Python.
A value of type `bool` is either `True` or `False`.

It is important to distinguish between `=`, which *assigns* a value to a variable, and `==`, which *checks* whether
two values are equal.

## Explorations

1. For each expression below, predict what will happen when you type it into the interactive console, then test your
prediction. Summarize what you learn in your notes.
    ```python
    3 == 5
    ```
    ```python
    'e' == 'diversity'[3]
    ```
    ```python
    5 == '5'
    ```
    ```python
    '' == []
    ```
1. Python has several other operators that produce Boolean values. For each expression below, predict what will happen when you type it into the interactive console, then test your
prediction. Summarize what you learn in your notes.
    ```python
    3 < 5
    ```
    ```python
    5 > 5
    ```
    ```python
    5 >= 5
    ```
    ```python
    'aardvark' < 'canary'
    ```
    ```python
    not 2 == 2
    ```
    ```python
    2 == 3 or 3 == 3
    ```
    ```python
    3 == 3 or 3 == 3
    ```
    ```python
    3 == 3 and 3 == 4
    ```
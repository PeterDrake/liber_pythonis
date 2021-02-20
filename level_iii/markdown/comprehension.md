# List Comprehensions

A ***list comprehension*** allows you to transform one list into another. For example, if you define

```python
data = [8, 2, 5, 4]
```

then the list comprehension

```python
[x + 1 for x in data]
```

is `[9, 3, 6, 5]`. It builds the new list by temporarily defining `x` as each element of `data` and using `x + 1` to
produce the corresponding element of the new list.

A list comprehension may include a boolean condition:

```python
[x * 2 for x in data if x > 4]
```

is `[16, 10]` because only `8` and `5` satisfy the condition `x > 4`.

## Explorations

1. For each expression below, predict what will happen when you type it into the interactive console, then test your
prediction. Summarize what you learn in your notes.
    ```python
    [x * 10 for x in [1, 2, 3]]
    ```
    ```python
    [n for n in [1, 2, 3, 4, 5, 6, 7] if n % 3 == 0]
    ```
    ```python
    [word for word in ['if', 'then', 'else', 'finally'] if 2 < len(word) < 5]
    ```
    ```python
    [2 for letter in 'hello']
    ```
1. Define a function that takes a list of numbers and returns a list of the negatives of those numbers.
1. Define a function that takes a list of numbers and returns a list of the absolute values of those numbers.
1. Define a function that takes a list of numbers and returns a list of only those numbers greater than 10.
1. Define a function that takes a list of strings. It should return a list of some of those strings. Specifically,
it should return a sorted list of those strings that start with `'a'`.
1. Define a function that takes a list of lists and returns a list of only those lists that aren't empty.
1. Define a function that takes a list of lists and returns a list of the means of those lists.

# Getting a Sequence Element at a Specific Index With `[]`

Sequences (lists and strings) are made up of elements. You can get the element at a specific ***index***, that is, at a
particular numbered position in the sequence. For historical reasons, the numbers start at 0, not at 1.

If you define

```python
word = 'hello'
```

then `word[0]` is `'h'`, `word[1]` is `'e'`, and so on.

## Explorations

1. For each expression below, predict what will happen when you type it into the interactive console, then test your
prediction. Summarize what you learn in your notes.
    ```python
    [8, 5, 7][2]
    ```
    ```python
    [8, 5, 7][3]
    ```
    ```python
    [8, 5, 7][1.5]
    ```
    ```python
    [8, 5, 7][1.0]
    ```   
    ```python
    ['dollar', 'peso', 'yen', 'euro'][1][2]
    ```
    ```python
    'invisible'[-1]
    ```
1. Define a function called `first` that, given a sequence, returns its first element.
1. Define a function called `maximum` that, given a list of numbers, returns the largest element. (Hint: use `sorted`.)
There is a built-in function called `max` that does the same thing, but writing it yourself is a useful exercise.

# Integer Division

Python has two different numeric types: `int` (an integer) and `float` (a number with a decimal point in it). A
number that happens to be an integer mathematically but has a decimal point, like `2.0`, counts as a `float`.

(The name "float" hearkens back to a time when computers used both "fixed point" numbers, with a standard number of
digits after the decimal point, and "floating point" numbers, where the decimal point could appear anywhere. Fixed point
arithmetic is now rarely used.)

Much of the time, you don't have to care whether you're using `int` or `float` values. One important exception is
indexing: the index *must* be an int.

Arithmetic operators and functions generally preserve data types, so `2 + 2` gives the `int` value `4`, but `2.0 + 2.0`
gives the `float` value `4.0`. Any operation that *might* produce a non-integer, though, *always* produces a float.
For example, `6 / 3` is `2.0`, not `2`.

There are two special operators for doing integer arithmetic:

`//` performs integer division, throwing away any remainder. `11 // 3` is `3`.

`%` performs integer division and keeps *only* the remainder. `11 % 3` is `2`.

## Explorations
1. For each expression below, predict what will happen when you type it into the interactive console, then test your
prediction. Summarize what you learn in your notes.
    ```python
    9 // 2
    ```
    ```python
    9 % 2
    ```
    ```python
    123456789 % 100
    ```
    ```python
    2 + 2.0
    ```
    ```python
    2.0 == 2
    ```
1. Define a function called `is_even` that takes an `int` and returns `True` if and only if that number is even. (Hint:
use `%`.)
1. Define a function called `is_integer` that takes a number and returns `True` if and only if that number is a
mathematical integer, regardless of whether it is an `int` or a `float`. (Hint: divide the number by `1` using both `/`
and `//` and compare the results.)
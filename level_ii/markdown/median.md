# The Median (Middle Value) of a List of Numbers

## Idea of the Median

## Computing the Median in Python

Computing the median requires combining many of the things you've learned up to this point:

<!--median.py-->
```python
def median(ls):
    s = sorted(ls)
    if len(s) % 2 == 1:
        middle = len(s) // 2
        return s[middle]
    else:
        left = (len(s) - 1) // 2
        right = len(s) // 2
        return (s[left] + s[right]) / 2
```

This function begins by sorting the argument `ls` and storing the result in a local variable called `s` (short for
"sorted").

What happens next depends on whether `len(s)` is odd or even. The `if` statement checks this by looking at `len(s) % 2`
(that is, the remainder when `len(s)` is divided by 2), which is 1 for odd lengths and 0 for even lengths.

For odd lengths, there is a unique middle number. For example, in a list of length 5, the elements are at indices 0, 1,
2, 3, and 4; the median is the one at index 2. The expression `len(s) // 2` uses integer division (throwing away the
remainder) to find this middle index. The element of `s` at this index is returned.

For even lengths, the situation is slightly more complicated. In a list of length 4, the elements are at indices 0, 1,
2, and 3; the median is the average of elements 1 and 2. The definitions of `left` and `right` find these indices.
The last line averages the list elements at these indices and returns the result.

## Explorations

1. This is the most complicated function you've seen, so it can be hard to follow. When faced with a complicated
function, computer scientists often print out intermediate values to watch what's going on as the function works.

   Four local variables are defined in this function: `s`, `middle`, `left`, and `right`. On the line after each one,
   add a statement printing its value. For example, after the line defining `s`, add `print(s)`.
   
   Now call the function and see what values are printed.
1. Run a program containing the definition of `median`. For each expression below, predict what will happen when
you type it into the interactive console, then test your prediction. Summarize what you learn in your notes.
    ```python
    median([10, 1, 100])
    ```
    ```python
    median(['Africa', 'North America', 'Asia', 'Europe', 'South America', 'Australia', 'Antarctica'])
    ```
    ```python
    median(['Inky', 'Blinky', 'Pinky', 'Clyde'])
    ```
    ```python
    median('diamond')
    ```
    ```python
    median('income')
    ```
    ```python
    median([])
    ```
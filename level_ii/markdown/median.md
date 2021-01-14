# The Median (Middle Value) of a List of Numbers

## What is the Median?

The ***median*** is one of three ***measures of center*** that we will study this semester.  It is one way to describe the typical, or central, value a variable takes for some group of observational units. 

The median is used only with quantitative variables.  To find the median, first rearrange your list of data so that it is in increasing order.  If you have an odd number of data values, the median is simply the number that appears exactly in the middle of the list.  If you have an even number of data values, the median is the mean of the two data values that appear in the middle.

## Example with Odd Number of Data Values
To compute the median of the list `[8, 6, 7, 5, 3, 0, 9]` first rearrange these numbers in increasing order.  This gives `[0, 3, 5, 6, 7, 8, 9]`. Since there are seven numbers in this list, the middle number is the one with three numbers to its left and three numbers to its right.  That middle number is `6`.  So the median of this list is `6`.


## Example with Even Number of Data Values
To compute the median of the list `[8, 6, 7, 5, 3, 0, 9, 1]` first rearrange these numbers in increasing order.  This gives `[0, 1, 3, 5, 6, 7, 8, 9]`. Since there are eight numbers in this list, the median is the average of the two middle numbers `5` and `6`.  So the median of this list is `5.5`.


## Computing the Median in Python

Computing the median requires combining many of the things you've learned up to this point:

<!--median.py-->
```python
def median(data):
    n = len(data)
    s = sorted(data)
    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[(n - 1) // 2] + s[n // 2]) / 2
```

This function begins by storing the length of the list `data` in a local variable called `n`. A sorted version of `data`
is stored in a second local variable called `s`.

What happens next depends on whether `n` is odd or even. The `if` statement checks this by looking at `n % 2`
(that is, the remainder when `n` is divided by 2), which is 1 for odd lengths and 0 for even lengths.

For odd lengths, there is a unique middle number. For example, in a list of length 5, the elements are at indices 0, 1,
2, 3, and 4; the median is the one at index 2. The expression `n // 2` uses integer division (throwing away the
remainder) to find this middle index. The element of `s` at this index is returned.

For even lengths, the situation is slightly more complicated. In a list of length 4, the elements are at indices 0, 1,
2, and 3; the median is the average of elements 1 and 2. These indices are found by the expressions `(n - 1) // 2` and
`n // 2`. The last line averages the elements of `s` at these indices and returns the result.

## Explorations

1. We saw above that the median of the list `[8, 6, 7, 5, 3, 0, 9]` is `6`.  Now change the first number in the list to `30`.  How does that change affect the median of the list?

2. The `median()` function above is the most complicated function you've seen, so it can be hard to follow. When faced with a complicated
function, computer scientists often print out intermediate values to watch what's going on as the function works.

   Two local variables are defined in this function: `n` and `s`. On the line after each one,
   add a statement printing its value. For example, after the line defining `n`, add `print(n)`.
   
   Now call the function and see what values are printed.
   
   You might also add a statement printing any other intermediate value, like `n // 2`.
3. Run a program containing the definition of `median`. For each expression below, predict what will happen when
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
   
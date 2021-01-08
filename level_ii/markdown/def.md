# Defining a Function

You have seen a number of built-in functions like `print`, `len`, and `sum`. Python also allows you to define your own
functions. This can make your programs much easier to read and debug.

As an example, you could define a `mean` function like this:

```python
def mean(ls):
    return sum(ls) / len(ls)
```

The first line contains:
* `def`, short for "define"
* The name of the function (here, `mean`)
* Between parentheses, the arguments to the function (here, `ls`, short for "list"); if there are multiple arguments,
their names are separated by commas
* A colon (`:`)

The lines below are run each time the function is called. In this case, there is only one such line.
It specifies what is returned by the function.

Once this is defined in a program, `mean([2, 6, 4, 5])`:
1. Defines a variable `ls` to refer to `[2, 6, 4, 5]`. This ***local variable*** is only visible inside the function.
1. Finds the sum of the numbers in `ls`.
1. Finds the length of the numbers in `ls`.
1. Divides to find the mean.
1. Returns the computed mean. In this case, the returned value is `4.25`.

Here's a function to convert years to seconds:

```python
def years_to_seconds(years):
    days = years * 365.24
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds
```

(If the 365.24 surprises you, remember leap years.)

After this is defined, `years_to_seconds(5)` returns `157783680.0`.

## Explorations
1. For each program below, predict what will happen when you run it, then test your prediction. Summarize what you learn in your notes.
    ```python
    def total_length(ls1, ls2):
        return len(ls1) + len(ls2)
    
    print(total_length([1, 2, 3], [10, 20]))
    ```
    ```python
    import math
    
    def hypotenuse(a, b):
        return math.sqrt((a ** 2) + (b ** 2))
    
    print(hypotenuse(3, 4))
    ```
    ```python
    def double(x):
        return x * 2
    
    def square(x):
        return x * x
    
    print(double(square(3)))
    ```
    ```python
    def foo(a, b, c):
        d = b + len(c)
        return a - d
    
    print(foo(10, 5, [6, 7]))
    ```
    ```python
    def bar():
        return 1
        return 2
    
    print(bar())
    ```
    ```python
    def quux(ls):
        n = len(ls)
        ls = [8, 0, 2]
        return n
    
    numbers = [3, 7, 1, 4]
    quux(numbers)
    print(numbers)
    print(quux(numbers))
    print(ls)
    ```
1. Define a function to convert Fahrenheit to Celsius.
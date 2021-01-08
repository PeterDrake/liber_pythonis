# The `print` Function

If you type `2 + 2` into the interactive console, the result (`4`) is printed. If you put this line in a program, the
result is *not* automatically printed. This is usually desirable, but occasionally you want a program to print
something.

For example, you might want to write a program to convert miles to kilometers, stored in a file `miles2km.py`. The
program could look like this:

```python
miles = 10
km = miles * 1.6
print(km)
```

The last line here calls the `print` ***function***. The value between the parentheses is called an ***argument*** to
the function. In this case, the argument tells the function what to print.

If you run this program, it will print `16.0` in the interactive console.

## Explorations

1. Write a program to convert pounds to kilograms using the formula ![k = p times 0.45](https://latex.codecogs.com/svg.latex?k=p\times0.45).

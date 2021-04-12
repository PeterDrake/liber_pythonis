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

1. Try the following Parsons puzzle, which gives you the code but asks you to arrange it in the correct order. This should be more relaxing than starting from a blank page. After you've arranged the pieces, click on the "Get feedback" button to see how you did. Try as many times as you like!
   1. [Print the number of seconds in a day.](https://parsons.herokuapp.com/puzzle/b37cced5c3194a578d3e5844f5f9c7f2)
1. Write a program to convert pounds to kilograms using the formula ![k = p times 0.45](https://latex.codecogs.com/svg.latex?k=p\times0.45).

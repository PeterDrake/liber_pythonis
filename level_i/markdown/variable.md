# Component: Variable

A variable is a name given to a number or other value. Once you define a name, you can
use it in place of that value.

```python
x = 3
print(x)
```

This prints:

```
3
```

Think of the variable as a named treasure chest containing the value. You can
change what's in the chest:

```python
hat_color = 'red'
hat_color = 'blue'
print(hat_color)
```

This prints:

```
blue
```

## Imps

```python
3 = x
```

```
    3 = x
    ^
SyntaxError: cannot assign to literal
```

The variable has to be on the left side.

`x = 3` is not *stating* that `x` and `3` are the same. It is *commanding* Python to
store `3` in the chest labeled `x`. The variable has to be on the left side.

When the imp uses the word *literal*, it is referring to `3`, which is literally the
number 3, rather than being a name for something. Variable names can contain digits,
but can't start with digits.
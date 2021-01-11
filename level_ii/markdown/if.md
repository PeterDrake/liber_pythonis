# Making Decisions With `if`

An ***`if` statement*** allows your program to behave differently depending on a Boolean ***condition***. For example,

```python
if x < 0:
    print('x is negative')
```

This will print the text only if `x` is less than zero.

An `if` statement consists of:
* `if`.
* A Boolean condition.
* A colon.
* Indented below this, one or more lines to be executed if the condition is true.

An `if` statement can include an ***`else` clause*** that is executed if the condition is *not* true:

```python
if x < 0:
    print('x is negative')
else:
    print('x is not negative')
```

Between these, an `if` statement can contain one or more ***`elif` clauses***. `elif` is short for "else if".

```python
if x < 0:
    print('x is negative')
elif x == 0:
    print('x is zero')
else:
    print('x is positive')
```

## Explorations

1. Define a function called `is_empty` that takes a list and prints "It's the empty list!" if and only the list is
empty.
1. Define a function called `larger` that takes two numbers and returns the larger one.
1. Define a function called `absolute_value` that returns the absolute value of its argument. In other words,
`absolute_value(3)` should return `3` but `absolute_value(-5)` should return `5`. There is a built-in function `abs`
that does the same thing, but writing it yourself is a good exercise.

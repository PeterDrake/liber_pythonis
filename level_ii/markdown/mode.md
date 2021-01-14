# The Mode (Most Common Value) of a List of Numbers

## What is the Mode?

The ***mode*** is one of ***three measures of center*** that we will study this semester. It is one way to describe the typical, or central, value a variable takes for some group of observational units. 

The mode can be used for both quantitative and categorical variables. The mode is simply the most common value in your data set.

## Example

Suppose a class has fourteen students and the table below records their favorite flavor of ice cream. 

| flavor  | chocolate       | strawberry  | tutti frutti       | vanilla |
|----------|--------------|----------|--------------|--------------|
| # students   | 6      | 3    | 2   | 3 |

Among these fourteen students, the mode favorite ice cream flavor is chocolate. 

## Computing the Mode in Python

The definition of `mode` is not terribly long, but it requires a couple of variations on ideas that you've seen
before.  These variations are ***inner functions*** and the use of a ***key*** with the `max` function.

### Inner Functions

You can define a function *inside* another function. Here's an example:

<!--outer.py-->
```python
def outer(x, y):
    def inner(z):
        return z * x
    return inner(x) + y
```

Here's what happens when this is called as `outer(2, 5)`:

1. `outer` begins, with `x` defined as `2` and `y` defined as `5`.
1. `inner` is defined.
1. `inner(2)` is called.
1. `inner` begins with `z` defined as `2`.
1. `inner` multiplies `z` and `x` (that is, `2` and `2`) and returns `4`.
1. `outer` resumes on the last line, adding this result (`4`) to the value of `y` (which is `5`) and returning `9`.

This would not have worked if `inner` was defined outside of `outer`:

<!--failed_inner.py-->
```python
def inner(z):
    return z * x

def outer(x, y):
    return inner(x) + y
```

In this case, `outer(2, 5)` doesn't work:

1. `outer` begins, with `x` defined as `2` and `y` defined as `5`.
1. `inner(2)` is called.
1. `inner` begins with `z` defined as `2`.
1. `inner` tries to multiply `z` (which is `2`) with `x`. Since `x` is only visible *inside* `outer`, this causes an
error:

```
NameError: name 'x' is not defined
```

You won't need to use this trick often, but it's crucial for defining `mode`.

### `max` and `key`

The built-in function `max` does exactly what you would expect:

```python
max([5, 2, 3, 6, 4])
```

return `6`.

It also works on lists of strings, so

```python
max(['race', 'class', 'gender'])
```

returns `race`, which is the "largest" word alphabetically, that is, the one that would appear last if the words were
sorted in dictionary order. 

If you instead want to sort these words by length, you can provide an optional named argument `key` specifying what
function to use to "measure" the words:

```python
max(['race', 'class', 'gender'], key=len)
```

returns `gender`, which is the longest word.

### Defining Mode

Here is the definition:

<!--mode.py-->
```python
def mode(ls):
    def count_in_ls(x):
        return ls.count(x)
    return max(ls, key=count_in_ls)
```

The last line says, "Return the 'largest' element of `ls`, measured by how often it occurs in `ls`." The inner function
is necessary because the function specified as `key` has to take exactly one argument.

Now

```python
numbers = [1, 2, 1, 1, 3, 1, 2, 1, 3, 3]
```

returns `1`.

## Explorations
1. What do you think `mode` should do if there's a tie for the most common element? What does it actually do?
1. Define a function to find the *least* common element of a list.

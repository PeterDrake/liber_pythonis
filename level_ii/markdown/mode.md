# The Mode (Most Common Value) of a List of Numbers

## Idea of the Mode

## Computing the Mode in Python

The definition of `mode` is not terribly long, but it requires a couple of variations on ideas that you've seen
before.

### Inner Functions

You can define a function *inside* another function. Here's an example:

<!--outer.py-->
```python
def outer(x, y):
    def inner(z):
        return z * x
    return inner(x) + y
```

When you call this as, say, `outer(2, 5)`, the function `inner` is defined, and then the last line of `outer` calls it.

This would not have worked if `inner` was defined outside of `outer`:

<!--failed_inner.py-->
```python
def inner(z):
    return z * x

def outer(x, y):
    return inner(x) + y
```

The problem here is that `outer`'s local variable `x` is not visible at the time `inner` is defined. It would not matter
if `outer` was defined first; `x` is only visible *inside* `outer`.

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

returns `race`, which is the "largest" word alphabetically.

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
1. Define a function to find the *least* common element of a list. (Hint: use an inner function that returns a *smaller*
number when the count is larger.)

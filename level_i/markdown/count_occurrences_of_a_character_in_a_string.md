# Spell: Count Occurrences of a Character in a String

## Incantation

```python
count = 0
for c in 'invisibility':
    if c == 'i':
        count = count + 1
print(count)
```

## Effect

```
5
```

## Explanation

This is very similar to the spell [Find Length of a String](find_length_of_a_string.md), but `count` is only increased
if the current character is an `'i'`. The variable `c` is `'i'` on the first pass through the loop, `'n'` on the second
pass, `'v'` on the third pass, and so on.

## Imps

### Case Sensitivity

```
4
```

You might have written:

```python
for c in 'Invisibility':
```

Python does not consider the lower-case `'i'` and the upper-case `'I'` to be the same character.

### Equality

```
    if c = 'i':
         ^
SyntaxError: invalid syntax
```

You used `=`, which assigns a value to a variable, rather than `==`, which checks whether two things are equal.

### Indentation

```
    count = count + 1
    ^
IndentationError: expected an indented block
```

This line is not indented properly:

```python
count = 0
for c in 'invisibility':
    if c == 'i':
    count = count + 1
print(count)
```

It must be indented even further than the line that starts with `if` to show that
it is inside the if statement.
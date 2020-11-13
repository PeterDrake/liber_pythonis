# Spell: Find Mean of List of Numbers

## Incanation

```python
numbers = [1, 3, 2, 3, 4]
sum = 0
for n in numbers:
    sum = sum + n
mean = sum / len(numbers)
print(mean)
```

## Effect

```
2.6
```

## Explanation

The mean (average) of a list of numbers is found by adding up those numbers and dividing by the length of the list.

## Imps

### Brackets

```
2.5
```

You used curly braces `{ }` instead of square brackets `[ ]`:

```python
numbers = {1, 3, 2, 3, 4}
```

This is interpreted as a *set* rather than a *list*, which removes duplicate items (in this case the second 3).

Round parentheses `( )` create a *tuple*. This is very similar to a list, and happens to work in this particular spell,
but could invoke subtle imps in other cases. Use square brackets for lists.

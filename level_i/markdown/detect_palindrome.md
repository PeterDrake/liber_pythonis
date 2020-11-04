# Spell: Detect Palindrome

## Incantation

```python
original = 'level'
reversed = ''
for c in original:
    reversed = c + reversed
print(original == reversed)
```

## Effect

```
True
```

## Explanation

The string `reversed` is initially empty. Each character from `original` is added to the beginning of it.

The last line prints `True` if `original` and `reversed` are the same, `False` otherwise.
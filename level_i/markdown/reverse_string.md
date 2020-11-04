# Spell: Reverse String

## Incantation

```python
original = 'mxyzptlk'
reversed = ''
for c in original:
    reversed = c + reversed
print(reversed)
```

## Effect

```
kltpzyxm
```

## Explanation

The string `reversed` is initially empty. Each character from `original` is added to the beginning of it.

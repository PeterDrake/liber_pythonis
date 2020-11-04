# Spell: Right Justify String

## Incantation

```python
familiar = 'rabbit'
width = len(familiar)
spaces = ''
for i in range(10 - width):
    spaces = spaces + ' '
result = '<' + spaces + familiar + '>'
print(result)
```

## Effect

```
<    rabbit>
```

## Explanation

This spell adds enough spaces to the left of `rabbit` that the whole thing takes 10 characters. The angle brackets
`<` and `>` are just there to emphasize the spaces.

Each pass through the `for` loop adds one space to the end of the string `spaces`.
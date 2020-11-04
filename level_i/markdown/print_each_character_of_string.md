# Spell: Print Each Character of String

## Incantation

```python
for c in 'hocus pocus':
    print(c)
```

## Effect

```
h
o
c
u
s
 
p
o
c
u
s
```

## Explanation

Think of the spell as: "For each character in the string `'hocus pocus'`, print that character."
The printing happens inside a loop that runs once for each character.

## Imps

### Missing Quotation Marks

```
    for c in hocus pocus:
                   ^
SyntaxError: invalid syntax
```

You forgot the quotation marks around the text.

### Missing Colon
```
    for c in 'hocus pocus'
                         ^
SyntaxError: invalid syntax
```

You forgot the colon at the end of this line.

### Indentation

```
    print(c)
    ^
IndentationError: expected an indented block
```

You forgot to indent the second line. You have to do this so that Python knows it's inside the loop.

# Spell: Print Each Character of a String

To print each character from a string of text on its own line:

```python
for c in 'hocus pocus':
    print(c)
```

This prints:

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

Think of the spell as: "For each character in the text string `'hocus pocus'`, print that character."
The printing happens inside a loop that runs once for each character.

## Imps

```
    for c in hocus pocus:
                   ^
SyntaxError: invalid syntax
```

You forgot the quotation marks around the text.

```
    for c in 'hocus pocus'
                         ^
SyntaxError: invalid syntax
```

You forgot the colon at the end of this line.

```
    print(c)
    ^
IndentationError: expected an indented block
```

You forgot to indent the second line. You have to do this so that Python knows it's inside the loop.

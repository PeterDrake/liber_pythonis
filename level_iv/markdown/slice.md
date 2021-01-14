# Slicing Sequences

Sometimes you just want some part of a sequence. Python's *slicing* facility offers a powerful way to specify this.

Here's an example of a slice in its full form:

```python
'uncopyrightable'[3:12:2]
```

This gives `oyiha`.

The three numbers in the square brackets, separated by colons, are the *start*, *stop*, and *step* of the slice.
In this case, they indicate that the slice should start at index 3, go up to *but not including* index 12, and take
every 2nd element along the way. That give indices 3, 5, 7, 9, and 11, the positions of the letters in the result.

One or more of these numbers can be left out.

## Explorations

1. For each expression below, predict what will happen when you type it into the interactive console, then test your
   prediction. Summarize what you learn in your notes.
   ```python
   'uncopyrightable'[3:12]
   ```
   ```python
   'uncopyrightable'[:12]
   ```
   ```python
   'uncopyrightable'[3:]
   ```
   ```python
   'uncopyrightable'[-4:]
   ```
   ```python
   'uncopyrightable'[:]
   ```
   ```python
   'uncopyrightable'[::3]
   ```
   ```python
   'uncopyrightable'[::-1]
   ```
   ```python
   ['Does', 'it', 'work', 'on', 'lists?'][:2]
   ```
   ```python
   [w[:2] for w in ['I', 'am', 'an', 'invisible', 'man']]
   ```

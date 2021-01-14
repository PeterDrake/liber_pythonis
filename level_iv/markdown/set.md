# The Set Data Type

A ***set*** is very similar to a list. You create a set using curly braces `{}` rather than square brackets `[]`:

```python
set{1, 2, 3}
```

There are two key differences between sets and lists:

1. A set cannot contain duplicate items.

1. The order of elements in a set is not defined.

## Explorations

1. For each expression below, predict what will happen when you type it into the interactive console, then test your
   prediction. *The order in which a set's elements are printed is essentially impossible to predict, so don't worry
   about that.* Summarize what you learn in your notes.
   ```python
   {1, 2, 2, 3}
   ```
   ```python
   {-1, 1}
   ```
   ```python
   {1, 2, 3} == {3, 2, 1}
   ```
   ```python
   {1, 2, 3}[0]
   ```
   ```python
   2 in {1, 2, 3}
   ```
   ```python
   {2.7, 3.1}
   ```
   ```python
   {True, False}
   ```
   ```python
   {'igneous', 'sedimentary', 'metamorphic'}
   ```
   ```python
   {[1, 2], [3, 4]}
   ```
   ```python
   {{1, 2}, {3, 4}}
   ```
   ```python
   set([1, 2, 2, 3])
   ```
   ```python
   list(set([1, 2, 2, 3]))
   ```
   ```python
   [x + 1 for x in {6, 2, 9}]
   ```
   ```python
   {x + 1 for x in [6, 2, 9, 2]}
   ```
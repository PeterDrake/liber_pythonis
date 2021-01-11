# Counting Occurrences `count`

Sometimes you want to know how many times an item occurs in a list. For example, in an election, you would want to
know how many of the votes were for a particular candidate.

Python does have a built-in way of doing this, but it looks a little strange. If you define

```python
flavors = ['vanilla', 'chocolate', 'strawberry', 'strawberry', 'chocolate', 'chocolate', 'vanilla', 'chocolate']
```

then

```python
flavors.count('chocolate')
```

returns `4`.

You can think of this as asking the list `flavors`, "How many times does `chocolate` occur in you?"

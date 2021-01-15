# Combining Lists

Sometimes you want to combine corresponding elements of two or more lists. For example, suppose you have this data
in `parcels.csv`:

```csv
length,width,height
2,4,5
8,5,2
6,3,3
```

You want to know the *volume* of each parcel.

Python's built-in `zip` function is perfect for this job.

```python
list(zip([1, 2, 3], [4, 5, 6]))
```

returns

```python
[(1, 4), (2, 5), (3, 6)]
```

The `zip` function itself returns a `zip` object, but it's easiest to convert that to a `list`. That `list` looks
very similar to a `list` of `lists`, but you may notice round parentheses instead of square brackets around the inner
lists. These objects are `tuple`s, which behave just like lists in almost all contexts.

With this zipped `list`, you can use a slightly more complicated list comprehension to combine elements from the
original list:

```python
[a + b for a, b in [(1, 4), (2, 5), (3, 6)]]
```

This temporarily defines `a` and `b` as the first and second element of each `tuple` in the `list`, then adds them
together. Here is the result:

```python
[5, 7, 9]
```

Now you know all you need to find those parcel volumes:

<!--parcels.py-->
```python
import csv

with open('parcels.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

lengths = [int(r['length']) for r in rows]
widths = [int(r['width']) for r in rows]
heights = [int(r['height']) for r in rows]

volumes = [ll * ww * hh for ll, ww, hh in list(zip(lengths, widths, heights))]

print(volumes)
```
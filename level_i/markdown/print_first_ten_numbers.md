# Spell: Print First Ten Numbers

## Incantation

```python
for i in range(10):
    print(i + 1)
```

## Effect

```
1
2
3
4
5
6
7
8
9
10
```

## Explanation

This loop runs 10 times. The variable `i` is 0 on the first pass, 1 the second pass, and so on up to 9 on the final
pass.

## Imps

### Off by One

```
0
1
2
3
4
5
6
7
8
9
```

You forgot to add 1 to `i` before printing it. Remember that `range(10)` starts at 0 and stops *before* 10.

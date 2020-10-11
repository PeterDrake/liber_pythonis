# Spell: Find Length of a String

## Incantation

```python
length = 0
for c in 'abracadabra':
    length = length + 1
print(length)
```

## Effect

```
11
```

## Explanation

The first line sets a variable called `length` to 0.

The loop, which runs once for each character in the string `'abracadabra'`, adds 1 to
`length` each time.

The last line prints the value of `length`.

## Imps

### Indentation

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
11
```

You indented the last line is to match the previous line, which put
it inside the loop:

```python
length = 0
for c in 'abracadabra':
    length = length + 1
    print(length)
```

This caused `length` to be printed after each character, rather than just once at the
end.
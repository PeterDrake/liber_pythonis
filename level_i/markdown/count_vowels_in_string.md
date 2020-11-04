# Spell: Count Vowels in a String

## Incantation

```python
count = 0
for c in 'the council of wizards':
    if c == 'a':
        count = count + 1
    if c == 'e':
        count = count + 1
    if c == 'i':
        count = count + 1
    if c == 'o':
        count = count + 1
    if c == 'u':
        count = count + 1
print(count)
```

## Effect

```
7
```

## Explanation

This is very similar to the spell [Count Occurrences of a Character in a String](count_occurrences_of_character_in_string.md).
The difference is that `c` is compared against each of several different letters.

## Imps

### Copy Paste

```
5
```

To avoid typing the if statement five times, you copied and pasted -- but then forgot to change the letters:

```python
count = 0
for c in 'the council of wizards':
    if c == 'a':
        count = count + 1
    if c == 'a':  # Oops!
        count = count + 1
    if c == 'a':
        count = count + 1
    if c == 'a':
        count = count + 1
    if c == 'a':
        count = count + 1
print(count)
```

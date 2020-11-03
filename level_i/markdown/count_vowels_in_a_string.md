# Spell: Count Vowels in a String

## Incantation

```python
count = 0
for c in 'the council of wizards':
    if c in 'aeiou':
        count = count + 1
print(count)
```

## Effect

```
5
```

## Explanation

This is very similar to the spell [Count Occurrences of a Character in a String](count_occurrences_of_a_character_in_a_string.md).
The difference is that, rather than checking whether `c` is `'i'`, you check whether it occurs in the string `'aeiou'`.

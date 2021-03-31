# What is a Proportion?

Sometimes we are less interested in the actual size of a particular quantity, but instead are interested in how big that quantity is in comparison to some other quantity.  In this situation it is helpful not to study the original quantity, but instead study the ***proportion*** between the two quantities.

# Example

Two $100 prizes will be given in a contest.  Just this fact alone does not let us know if it's easy to win the contest or not.  Instead we need to know the proportion of people in the contest who will be winners.  For example, if only 10 people are participating in the contest then the proportion of contest winners is 2/10 = 0.2. That's a pretty good chance of winning! However if 1,000 people are participating in the contest then the proportion of winners is 2/1000 = 0.002.  It's much less likely in this situation to be a winner.

# Coding Proportions

In Python we can use `zip` and a list comprehension to compute the proportion between two lists. The code below outputs the list `[0.333333,0.5,2.0]`

```python
a = [2,5,6]
b = [6,10,3]
pairs = list(zip(a,b))
proportions_a_to_b = [a/b for a,b in pairs]
```

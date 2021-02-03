# The Mean (Average) of a List of Numbers

## What is the Mean?

The ***mean*** is one of three ***measures of center*** that you will study this semester.  It is one way to describe the typical, or central, value a variable takes for some group of observational units.  Outside of a math class, the mean is usually called the average.

The mean is used only with quantitative variables.  To find the mean, compute the sum of the numbers in your data set and then divide by how many numbers you have.

## Example

The mean of the numbers 1, 4 and 8 is computed as follows:

![one third of the sum of 1, 4 and 8 is approximately 4.3](https://latex.codecogs.com/svg.latex?\tfrac{1}{3}(1+4+8)\approx%204.3)


## Computing the Mean in Python

If you define a list of numbers

```python
data = [8, 6, 7, 5, 3, 0, 9]
```

the finding the mean is easy, using functions you've learned:

<!--mean.py-->
```python
mean = sum(data) / len(data)
```

## Explorations

1. Use Python to confirm that the mean of the list 
    ```python
    data = [8, 6, 7, 5, 3, 0, 9]
    ``` 
    is approximately 5.43.

2. Suppose you make a dramatic change one of the numbers in the list from (1).  For example, change the `8` to `30` to get the new list:
    ```python
    new_data = [30, 6, 7, 5, 3, 0, 9]
    ```
   Compute the mean of this new list.  How is the mean affected by changing the `8` to a `30`?

3. Suppose you change the number `8` in the list `numbers` to `-30`.  Predict what will happen to the mean of the list, and then check your prediction by computing the mean.

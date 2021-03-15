# The Distribution of a Set of Data

## The Informal Idea

We have used measures of center (mean, median, and mode) and measures of spread (range, IQR, standard deviation) to describe a data set. So we can discuss the typical value of our data as well as how clumped or spread the data is.  However, these summaries still miss important aspects of a set of data.  For example, the data sets
```python
data1 = [1,2,3,3,4,5,6,7,8,8,9,10]
data2 = [1,3,3,5,5,5,6,6,6,7,7,10] 
```
both have median 5.5 and range 9.  But when we graph these data sets, we see that they have very different shapes.



Very informal level, more formal -- function.  INformally speaking the distribution of a set of data is the shape the data makes when you plotl it. Compare two data sets with same median and range but very different shapes.  Pennny ages.

More formally it is a function that... show historgrams converging to a distrution curve.  Penny ages.

A distribution is a function that summarizes how often the various outcomes of a

The ***mean*** is one of three ***measures of center*** that you will study this semester.  It is one way to describe the typical, or central, value a variable takes for some group of observational units.  Outside of a math class, the mean is usually called the average.

The mean is used only with quantitative variables.  To find the mean, compute the sum of the numbers in your data set and then divide by how many numbers you have.

## A More Official Version

The mean of the numbers 1, 4 and 8 is computed as follows:

![one third of the sum of 1, 4 and 8 is approximately 4.3](https://latex.codecogs.com/svg.latex?\tfrac{1}{3}(1+4+8)\approx%204.3)


## Computing the Mean in Python

If you define a list of numbers

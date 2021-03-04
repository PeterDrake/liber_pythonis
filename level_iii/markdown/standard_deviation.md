# Standard Deviation (Sophisticated Measure of Spread)

## What is the Standard Deviation?

The ***mean*** is one of three ***measures of spread*** that you will study this semester.  It is one way to describe to what degree the data in your data set is clumped around a single value, or spread out over a range of values. 

The standard deviation is only used with quantitative variables.  Roughly speaking the standard deviation tells you how far a data value falls from the mean of your data set, on average. 

## Example

The standard deviation of the numbers 1, 4 and 8 is computed in the following way.  First compute the mean of the data.

![one third of the sum of 1, 4 and 8 is approximately 4.3](https://latex.codecogs.com/svg.latex?\tfrac{1}{3}(1+4+8)=\frac{11}{3})

Now compute the difference between each data value and the mean, square those differences, and then add up the squares.  This quantity is sometimes called the ***sum of squares***.


![sum of squares of 1, 4, 8](https://latex.codecogs.com/svg.latex?(1-\tfrac{11}{3})^2&plus;(4-\tfrac{11}{3})^2&plus;(8-\tfrac{11}{3})^2=26.0)

When the data all falls very close to the mean, the sum of squares is small.  If there is data very far from the mean, the sum of squares is large.  

Now divide the sum of squares by the number of values in your data set.  The resulting number is called the ***variance*** of the dataa and gives a measure of the average distance a data point falls from the mean. 


![variance of 1, 4, 8](https://latex.codecogs.com/svg.latex?\left&space;((1-\tfrac{11}{3})^2&space;&plus;&space;(4-\tfrac{11}{3})^2&space;&plus;&space;(8-\tfrac{11}{3})^2\right&space;)/3&space;\approx&space;8.7)

There is one more step left in computing the standard deviation. Notice that if the data were all ages measured in months, the units in the variance would be *months-squared*.  We return to reasonable units by taking the square root of the variance.  The number that we get is the standard deviation of the data.


![standard deviation of 1, 4, 8](\sqrt{\frac{(1-\tfrac{11}{3})^2&space;&plus;&space;(4-\tfrac{11}{3})^2&space;&plus;&space;(8-\tfrac{11}{3})^2}{3}}&space;\approx&space;2.9)


## Computing the Standard Deviation in Python

Here's the definition, which uses `mean` and (from the `math` library) `sqrt`:

<!--standard_deviation.py-->
```python
def standard_deviation(data):
    squared_deviations = [(x - mean(data)) ** 2 for x in data]
    variance = sum(squared_deviations) / len(data)
    return math.sqrt(variance)
```

Here's a program to compute the standard deviation of heights from the NCHS data:

<!--heights_stddev.py-->
```python
import csv
import math

def mean(data):
    return sum(data) / len(data)

def standard_deviation(data):
    squared_deviations = [(x - mean(data)) ** 2 for x in data]
    variance = sum(squared_deviations) / len(data)
    return math.sqrt(variance)

with open('nchs.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]
print('Standard deviation: ' + str(standard_deviation(heights)))
```


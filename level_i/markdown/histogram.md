# Histogram

A ***histogram*** is a way to visualize the values of a quantitative variable for a large group of observational units.  One axis of a histogram shows the quantitative variable, and is chopped up into intervals.  You then count how many data values appear in each interval.  The other axis displays these counts.  A box is drawn based at each interval, with length indicating the number of observations in that interval.  

## Example - By Hand
In this example we'll see how to construct a histogram from a data set*.  The observational units for this data set are 250 children in the United States, the variables are the age (in months), weight (in pounds), height (in inches) and gender (recorded as M or F). Because this data set is large, the table below shows only the first few lines of data.  [Click here to see the full data set.](../data/kid-weights-UsingR.csv)

| age | weight | height | gender |
|-----|--------|--------|--------|
| 58  | 38     | 38     | M      |
| 103 | 87     | 43     | M      |
| 87  | 50     | 48     | M      |
| 138 | 98     | 61     | M      |
| 82  | 47     | 47     | F      |

 We will focus only on the height variable in this example. 
 
 To build a histogram for the height variable, we first decide how to chop the axis recording heights into subintervals.  Usually people call the subintervals ***bins***, so we are creating the bins for our histogram.  For simplicity we'll use 4 bins for this example.  The highest height in the data set is 67 inches and the lowest is 12 inches (data entry error?).  We subtract the lowest from the heighest, and divide that number by the number of bins.  What we get is the length of the bins that we'll use in the histogram.
 
![a quarter of 67 minus 12 is 13.75](https://latex.codecogs.com/svg.latex?\tfrac{1}{4}(67-12)=13.75)

To get the bins we start with the minimum value of 12 and add the bin width of 13.75, repeating until we reach the maximum value of 67.

![twelve plus 13.75 is 25.75](https://latex.codecogs.com/svg.latex?12+13.75=25.75)

![25.75 plus 13.75 is 39.5](https://latex.codecogs.com/svg.latex?25.75+13.75=39.5)

![39.5 plus 13.75 is 53.25](https://latex.codecogs.com/svg.latex?39.5+13.75=53.25)

![53.25 plus 13.75 is 67](https://latex.codecogs.com/svg.latex?53.25+13.75=67)

So the bins are 12 to 25.75, 25.75 to 39.5, 39.5 to 53.25, and 53.25 to 67.

Next we count up the number of data values that fall into each of these bins. For data values that fall exactly on the edge on an interval, you have to decide to put them in the interval to the right or to the left.  Just apply the choice consistently for all data values. From these counts we form a frequency table.  The frequency table is given below.  The number 43 in the table indicates that 43 data values fell between 12 and 25.75.



| bin | 12 to 25.75      | 25.75 to 39.5  | 39.5 to 53.25      | 53.25 to 67 |
|----------|--------------|----------|--------------|--------------|
| # data values in bin   | 43     | 124    | 60   | 23 |

Finally we can draw the histogram with the length of the box over each interval given by the number in the frequency table.


<!-- (Comment) Code for graph below is in level_1/code/bar_vert.py -->
![Histogram of children's heights by hand](../image/hist_height_byhand.png)


## Example - Using Basic Python


## Example - Using the Python Pandas Library

By using the Pandas Library, we can use Python to automatically read in a .csv file, choose a number of bins, count the frequencies of data values in each bin, and produce a histogram.  The histogram below was created using this method.  The name of the .csv file that gets read into Python is `kid_data_UsingR.csv`  The code that produced this histogram appears below the histogram.

<!-- (Comment) Code for graph below is in level_1/code/hist_pandas.py -->
![Histogram of children's heights using Pandas](../image/hist_heights_pd.png)

```
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('kid_data_UsingR.csv')
plt.hist(data['height'], edgecolor='black',bins =4)
plt.ylabel('frequency')
plt.xlabel('heights in inches')
plt.title('Heights of Children')
plt.tight_layout()
plt.show()

```

\* All data comes from somewhere, and it's important to give credit to the source. This also allows the reader to think critically about how the source of the data might influence their understanding of the data. The data is from the [National Center for Health Statistics](https://www.cdc.gov/nchs/nhanes/index.htm?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnchs%2Fnhanes.htm). John Verzani at the City University of New York did the data cleaning to produce this nice data set as part of his educational project called [**UsingR**](https://www.math.csi.cuny.edu/Statistics/R/simpleR/). The decisions to use U.S. Customary Units (rather than metric), and the binary gender variables M and F, were likely made by researchers at the National Center for Health Statistics. 

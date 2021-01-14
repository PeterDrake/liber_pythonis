# Bar Chart

A bar chart is a way to visualize data using rectangles that are called bars.  One axis of the bar chart lists the categories of some categorical variable. The other axis is scaled to represent a quantitative variable.  There is one bar based at each category and its width or height is given by the value of the quantitative variable for that category.

## Example
A common use of bar charts is to display how often (the frequency) of the values of a categorical variable for some group of observational units.  Suppose a class has fourteen students and the table below records their favorite type of ice cream. 

| flavor  | chocolate       | strawberry  | tutti frutti       | vanilla |
|----------|--------------|----------|--------------|--------------|
| # students   | 6      | 3    | 2   | 3 |


The bar chart below lists each ice cream flavor on the horizontal axis. The vertical axis is marked off to show how often that flavor is selected as a student's favorite. The height of the bars over each flavor record how often that flavor appears as a student's favorite. The Python code used to produce the bar graph is given below the graph.

<!-- (Comment) Code for graph below is in level_1/code/bar_vert.py -->
![Ice Cream Flavors Bar Chart - Vertical Bars](../image/icecream.png)

```
import matplotlib.pyplot as plt
flavors = ['chocolate', 'strawberry', 'tutti frutti', 'vanilla']
frequency = [6, 3, 2, 3] 
plt.bar(flavors, frequency)
plt.ylabel('frequency')
plt.xlabel('Ice Cream Flavors')
plt.title('Favorite Ice Cream Flavors in Our Class')
plt.tight_layout()
plt.show()
```

The key line is

```python
plt.bar(flavors, frequency)
```

where you provide the list of categories (`flavors`) and the list of numbers associated with those categories (`frequency`).

The bar chart below shows the same thing, but the flavors appear on the vertical axis and the bars extend horizontally to indicate the frequency of each flavor in the table. The Python code used to produce the bar graph is given below the graph.

<!-- (Comment) Code for graph below is in level_1/code/bar-horiz.py -->
![Ice Cream Flavors Bar Chart - Horizontal Bars](../image/icecreamh.png)

```
import matplotlib.pyplot as plt
flavors = ['chocolate', 'strawberry', 'tutti frutti', 'vanilla']
frequency = [6, 3, 2, 3]
plt.barh(flavors, frequency)
plt.ylabel('Ice Cream Flavors')
plt.xlabel('frequency')
plt.title('Favorite Ice Cream Flavors in Our Class')
plt.tight_layout()
plt.show()
```

Notice that the only differences are:

* You use `barh` instead of `bar`.
* The axis labels are swapped.

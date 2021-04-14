# The Empirical Rule for Normal Distributions

## The Family of Normal Curves

Normal distributions are modeled by bell-shaped curves called ***normal curves***.  If your data is normally distributed with mean &mu; and standard deviation &sigma;, there is a specific normal curve that models your data.  In symbols, the corresponding normal curve is:

<img src="https://latex.codecogs.com/gif.latex?N(x)=\frac{1}{\sigma\sqrt{2}\pi}e^{-\frac{(x-\mu)^2}{2\sigma^2}}" title="N(x)=\frac{1}{\sigma\sqrt{2}\pi}e^{-\frac{(x-\mu)^2}{2\sigma^2}}" alt="A very complicated mathematical expression."/>

As seen in the figure below, different choices of mean &mu; and standard deviation &sigma; give normal curves with different shapes.  However both of these curves still belong to the family of normal curves.

![Diagram showing two normal curves with different means and standard deviations](../images/normal_curves.png)

## Identifying the Mean and Standard Deviation Associated to a Normal Curve

When examining the graph of a normal curve, you'll notice that the mean of the distribution occurs at the point on the horizontal axis that corresponds to the peak of the normal curve.  

You can also identify the standard deviation of a normal curve just by looking at the graph.  The trick is to find the ***points of inflection*** of the normal curve.  These are points where the curves switches from bending up like a smile to bending down like a frown.  When a piece of a graph is bending up like a smile, we say that part of the curve is ***concave up***.  When a piece of a graph is bending down like a frown, we say that part of the curve is ***concave down***.  The points of inflection are the points where the curve switches its concavity.  A normal curve has exactly two points of inflection.  Each them have a horizontal coordinate that is exactly one standard deviation away from the mean.  The figure below illustrates these ideas.

![Normal curve with mean and points of inflection marked](../images/normal_anatomy.png)

## The Empirical Rule

Given a normal curve the observations above allow you to mark the mean on the horizontal axis of a normal curve, as well as points that are one standard deviation above and one standard deviation below the mean.  In fact we can also mark points two and three standard deviations above and below the mean.  In other words, there is a natural way to scale the horizontal axis of a normal curve.

Even better, this scaling allows us to make conclusions about data that we are modeling with a normal curve.  These conclusions are made using the "Empirical Rule" which is stated below:

```
The Empirical Rule
Data that is normally distributed follows the pattern below:
* about 68% of the data falls at most one standard deviation from the mean,
* about 95% of the data falls at most two standard deivations from the mean,
* about 99.7% of the data falls at most three standard deviations from the mean.
```

 The figure below illustrates the Empirical Rule.  Also, in the first graph in the figure, note that 32% of the data falls greater than one standard deviation from the mean. The region shaded in green represents all data values that are more than 1 standard deviation above the mean, which is 16% of the data.

![Normal curve with areas shaded](../images/empirical_rule.png)

## Exploration

The mean height of men in the United States is 5 feet 9 inches (175.4 cm).  The standard deviation of these heights is 3 inches (8 cm).  Assuming these heights are normally distributed, what proportion of men are 6 feet or taller?

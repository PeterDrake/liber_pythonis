# The Central Limit Theorem

## The key ideas of this theorem (in words)
We have seen that as you take more and more samples, the distribution of sample proportions becomes closer and closer to a normal distribution. Also, if the parameter proportion for the entire populatin is P, the distribution of sample proportions has mean close to P. Finally, if we increase the size of the sample, the spread of the distribution of sample proportions decreases.

## The key ideas of this theorem (in pictures)

![Diagram showing sampling distributions as sample size increases](../images/clt_motivation.png)

## The formal statement of the Central Limit Theorem

**The Central Limit Theorem:**  Suppose many simple random samples of size n are drawn from a population.  For each sample, a sample proportion ![p-hat](https://latex.codecogs.com/gif.latex?\hat{p}) is recorded.  Let P denote the parameter proportion describing the whole population.  If nP and n(1-P) are both greater than 10, then the sampling distribution of all possible sample proportions ![p-hat](https://latex.codecogs.com/gif.latex?\hat{p}) is *normally distributed*, *centered at P (so its mean is P)*, and has *standard deviation* given by the expression:

![square root of the fraction P times 1 minus P divided by n](https://latex.codecogs.com/gif.latex?\sqrt{\frac{P(1-P)}{n}})

We illustrate the Central Limit Theorem with the image below, keeping in mind that the standard deviation of a normal curve can be visualized as the distance between the center of the curve and its points of inflection.  

![Diagram showing normal curve with center P and standard deviation from the Central Limit Theorem](../images/clt_image.png)

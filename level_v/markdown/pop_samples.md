# Samples and Populations

An important application of statistics is to use a sample to understand some feature of a larger population.  This process is called ***statistical inference***.  It takes a few layers of theory to be able to do statistical inference.  The first step is to understand how the words ***populations***, ***parameters***, ***samples***, and ***statistics*** are used in statistics.  That is the focus of this page.

If you are rusty on the statistical terms *observational unit* and *variable* please re-read the [**Observational Units and Variables**](https://github.com/PeterDrake/liber_pythonis/blob/master/level_i/markdown/quant_cat.md) page in these notes.

# Definitions
* A ***population*** is the entire group of observational units of interest.  (see image below). 
* A ***parameter*** is the value of a variable over an entire population.  Parameters are typically written with Greek letters such as &mu; for the mean value of a variable for a population, &sigma; for the standard deviation of a variable for a population, and P for the proportion of some outcome of a variable for a population.  (Greek and Roman capital P are the same thing.)
* A ***sample*** is some subset of the population.  (see image below)
* A ***statistic*** is the value of a variable over a sample.  Statistics are written with Roman letters (the usual ones in English) such as <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{x}" title="\bar{x}" /></a> for the mean of a variable for a sample, s for the standard deviation of a variable for a sample, p for the proportion of some outcome of a variable for a sample.

# Example of Populations Versus Samples
*A study seeks to understand the voting habits of U.S. citizens who are 18 to 22 years old.  Researchers call 2000 U.S. citzens in that age range and asks them if they voted in the most recent presidential election.*

In this example the population of interest is all U.S. citizens who are 18 to 22 years old.  The sample is the 2000 people called by the researchers.  The variable being studied is whether or not a person voted in the most recent presidential election. The parameter implied by this example is the proportion of all U.S. citizens of age 18 - 22 years who voted in the most recent presidential election.   The statistic implied by this example is the proportion of the 2000 people called by the researchers who voted in the most recent presidential election.

# Memory Trick!

*Parameters* describe *Populations*, and *Statistics* describe *Samples*.  **The letters match!**

# Simple Random Samples

For large populations, parameters are unknowable.  It is impossible to get data from everyone in a population when the population is large. In contrast, statistics are easy to compute.  The hard part is building a sample that successfully represents the population.  A ***simple random sample*** is a subset of individuals chosen from a population where each individual in the population has the same probability of being chosen to be in the subset.  One way to build a simple random sample is to assign each member of the population a number, and then use randomly generated numbers to choose the individuals to be in the sample.

# Biased Samples

A sampling method that systematically favors some individuals over others is said to be ***biased***.  The bias can occur accidentally or intentionally.

# Example of a Biased Sample

 In the 2016 presidential election, national polls predicted that Hillary Clinton would win over Donald Trump.  Some speculate that these polls suffered from *nonresponse bias*.  That is, some believe that the sort of voter who would choose not to respond to a presidential poll was more likely to vote for Trump.  As a result Clinton voters were overrepresented in the sample of people who responed to the polls, and so these polls predicted a Clinton win.

![Venn diagram showing sample inside of population](../images/samppop.png)

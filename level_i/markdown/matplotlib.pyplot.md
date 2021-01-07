# `matplotlib.pyplot`

The `matplotlib.pyplot` library provides you with enormous power for drawing graphs to visualize data. Because
its name is so long, it is traditional to give it the nickname `plt` when importing it:

```python
import matplotlib.pyplot as plt
```

A program to draw a graph generally has the following parts:

1. `import matplotlib.pyplot as plt`
1. Prepare data
1. Plot data
1. Decorate the graph
1. Display the graph

Here's a simple example:

```python
import matplotlib.pyplot as plt
data = [2, 3, 5, 1, 4]
plt.plot(data)
plt.title('Zombie outbreaks')
plt.show()
```

Here is the graph produced:

![A line graph of zombie outbreaks](../image/simple_graph.png)

## Preparing the data

This depends heavily on the data you're working with. You will often spend almost all of your time writing this part.
For early examples, we will use simple lists.

## Plotting the data

This depends on the type of graph you're trying to produce. Each type is described in a separate page of the *Liber
Pythonis*.

## Decorating the graph

There are many options here, but here are the most common ones:

`plt.title` takes a string and shows it at the top of the graph.

`plt.xticks` takes a list of numbers, specifying the locations of the little marks along the horizontal (x) axis.

`plt.yticks` is similar, but for the vertical (y) axis.

`plt.xlabel` takes a string and shows it below the horizontal axis, indicating what this axis means.

`plt.ylabel` is similar, but for the vertical (y) axis.

## Displaying the graph

There are two ways to do this:

`plt.show()` displays the graph on your screen.

`plt.savefig('filename.png', bbox_inches='tight')` saves the graph in a file called `filename.png`. Of course, you can
change the name of the file. The named argument `bbox_inches='tight'` prevents the saved image from either cutting
off part of the graph or leaving excess white space around it.

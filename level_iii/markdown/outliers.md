# Outliers

## What is an outlier?

Outliers are values that are unusually far from other values in a data set.  Sometimes there is a concrete rule to use in determining what data values are unusual enough to be considered outliers.  This will happen with box plots, for example.  Sometimes it is up to your judgement to decide whether or not a data value is an outlier.

## Examples

1.  The number `30` is an outlier in the data set `[30, 6, 7, 5, 3, 0, 9]`.  All other data values are between one and ten, with thirty falling well above 10.

1.  Bellow is the scatter plot of children's heights from the  [*Histograms*](level_i/markdown/histogram.md) section in Level ii.

    ![Scatter plot of children's ages and heights using matplotlib.pyplot](../../level_i/image/scatter_age_height.png)

    The point in the lower left hand corner of the plot represents a child of age 4 months whose height is 12 inches. This point is lower than all other points in the scatter plot, so it is reasonable to view it as an outlier.  Note that 12 inches is very short for a human, even for a baby.  Since all other children who are only a few months old have heights clustered between 20 and 30 inches, it is likely there was a data entry error.  The correct entry may well have been 21 inches rather than 12 inches.

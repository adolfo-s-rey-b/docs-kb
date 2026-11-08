 

 Ctrl+K

Site Navigation

*   [Installing](https://seaborn.pydata.org/installing.html)
    
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
    
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
    
*   [API](https://seaborn.pydata.org/api.html)
    
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
    
*   [Citing](https://seaborn.pydata.org/citing.html)
    
*   [FAQ](https://seaborn.pydata.org/faq.html)
    

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
    
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
    
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")
    

On this page

seaborn.kdeplot[#](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn-kdeplot "Permalink to this heading")

==========================================================================================================================

seaborn.kdeplot(_data\=None_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _weights\=None_, _palette\=None_, _hue\_order\=None_, _hue\_norm\=None_, _color\=None_, _fill\=None_, _multiple\='layer'_, _common\_norm\=True_, _common\_grid\=False_, _cumulative\=False_, _bw\_method\='scott'_, _bw\_adjust\=1_, _warn\_singular\=True_, _log\_scale\=None_, _levels\=10_, _thresh\=0.05_, _gridsize\=200_, _cut\=3_, _clip\=None_, _legend\=True_, _cbar\=False_, _cbar\_ax\=None_, _cbar\_kws\=None_, _ax\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "Permalink to this definition")

Plot univariate or bivariate distributions using kernel density estimation.

A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analogous to a histogram. KDE represents the data using a continuous probability density curve in one or more dimensions.

The approach is explained further in the [user guide](https://seaborn.pydata.org/tutorial/distributions.html#tutorial-kde)
.

Relative to a histogram, KDE can produce a plot that is less cluttered and more interpretable, especially when drawing multiple distributions. But it has the potential to introduce distortions if the underlying distribution is bounded or not smooth. Like a histogram, the quality of the representation also depends on the selection of good smoothing parameters.

Parameters:

**data**[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)")
, [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v1.26)")
, mapping, or sequence

Input data structure. Either a long-form collection of vectors that can be assigned to named variables or a wide-form dataset that will be internally reshaped.

**x, y**vectors or keys in `data`

Variables that specify positions on the x and y axes.

**hue**vector or key in `data`

Semantic variable that is mapped to determine the color of plot elements.

**weights**vector or key in `data`

If provided, weight the kernel density estimation using these values.

**palette**string, list, dict, or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.8.2)")

Method for choosing the colors to use when mapping the `hue` semantic. String values are passed to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
. List or dict values imply categorical mapping, while a colormap object implies numeric mapping.

**hue\_order**vector of strings

Specify the order of processing and plotting for categorical levels of the `hue` semantic.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")

Either a pair of values that set the normalization range in data units or an object that will map from data units into a \[0, 1\] interval. Usage implies numeric mapping.

**color**[`matplotlib color`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "(in Matplotlib v3.8.2)")

Single color specification for when hue mapping is not used. Otherwise, the plot will try to hook into the matplotlib property cycle.

**fill**bool or None

If True, fill in the area under univariate density curves or between bivariate contours. If None, the default depends on `multiple`.

**multiple**{{“layer”, “stack”, “fill”}}

Method for drawing multiple elements when semantic mapping creates subsets. Only relevant with univariate data.

**common\_norm**bool

If True, scale each conditional density by the number of observations such that the total area under all densities sums to 1. Otherwise, normalize each density independently.

**common\_grid**bool

If True, use the same evaluation grid for each kernel density estimate. Only relevant with univariate data.

**cumulative**bool, optional

If True, estimate a cumulative distribution function. Requires scipy.

**bw\_method**string, scalar, or callable, optional

Method for determining the smoothing bandwidth to use; passed to [`scipy.stats.gaussian_kde`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html#scipy.stats.gaussian_kde "(in SciPy v1.12.0)")
.

**bw\_adjust**number, optional

Factor that multiplicatively scales the value chosen using `bw_method`. Increasing will make the curve smoother. See Notes.

**warn\_singular**bool

If True, issue a warning when trying to estimate the density of data with zero variance.

**log\_scale**bool or number, or pair of bools or numbers

Set axis scale(s) to log. A single value sets the data axis for any numeric axes in the plot. A pair of values sets each axis independently. Numeric values are interpreted as the desired base (default 10). When `None` or `False`, seaborn defers to the existing Axes scale.

**levels**int or vector

Number of contour levels or values to draw contours at. A vector argument must have increasing values in \[0, 1\]. Levels correspond to iso-proportions of the density: e.g., 20% of the probability mass will lie below the contour drawn for 0.2. Only relevant with bivariate data.

**thresh**number in \[0, 1\]

Lowest iso-proportion level at which to draw a contour line. Ignored when `levels` is a vector. Only relevant with bivariate data.

**gridsize**int

Number of points on each dimension of the evaluation grid.

**cut**number, optional

Factor, multiplied by the smoothing bandwidth, that determines how far the evaluation grid extends past the extreme datapoints. When set to 0, truncate the curve at the data limits.

**clip**pair of numbers or None, or a pair of such pairs

Do not evaluate the density outside of these limits.

**legend**bool

If False, suppress the legend for semantic variables.

**cbar**bool

If True, add a colorbar to annotate the color mapping in a bivariate plot. Note: Does not currently support plots with a `hue` variable well.

**cbar\_ax**[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

Pre-existing axes for the colorbar.

**cbar\_kws**dict

Additional parameters passed to [`matplotlib.figure.Figure.colorbar()`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.colorbar "(in Matplotlib v3.8.2)")
.

**ax**[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

Pre-existing axes for the plot. Otherwise, call [`matplotlib.pyplot.gca()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "(in Matplotlib v3.8.2)")
 internally.

**kwargs**

Other keyword arguments are passed to one of the following matplotlib functions:

*   [`matplotlib.axes.Axes.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "(in Matplotlib v3.8.2)")
     (univariate, `fill=False`),
    
*   [`matplotlib.axes.Axes.fill_between()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "(in Matplotlib v3.8.2)")
     (univariate, `fill=True`),
    
*   [`matplotlib.axes.Axes.contour()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "(in Matplotlib v3.8.2)")
     (bivariate, `fill=False`),
    
*   `matplotlib.axes.contourf()` (bivariate, `fill=True`).
    

Returns:

[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

The matplotlib axes containing the plot.

See also

[`displot`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")

Figure-level interface to distribution plot functions.

[`histplot`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")

Plot a histogram of binned counts with optional normalization or smoothing.

[`ecdfplot`](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn.ecdfplot "seaborn.ecdfplot")

Plot empirical cumulative distribution functions.

[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

Draw a bivariate plot with univariate marginal distributions.

[`violinplot`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "seaborn.violinplot")

Draw an enhanced boxplot using kernel density estimation.

Notes

The _bandwidth_, or standard deviation of the smoothing kernel, is an important parameter. Misspecification of the bandwidth can produce a distorted representation of the data. Much like the choice of bin width in a histogram, an over-smoothed curve can erase true features of a distribution, while an under-smoothed curve can create false features out of random variability. The rule-of-thumb that sets the default bandwidth works best when the true distribution is smooth, unimodal, and roughly bell-shaped. It is always a good idea to check the default behavior by using `bw_adjust` to increase or decrease the amount of smoothing.

Because the smoothing algorithm uses a Gaussian kernel, the estimated density curve can extend to values that do not make sense for a particular dataset. For example, the curve may be drawn over negative values when smoothing data that are naturally positive. The `cut` and `clip` parameters can be used to control the extent of the curve, but datasets that have many observations close to a natural boundary may be better served by a different visualization method.

Similar considerations apply when a dataset is naturally discrete or “spiky” (containing many repeated observations of the same value). Kernel density estimation will always produce a smooth curve, which would be misleading in these situations.

The units on the density axis are a common source of confusion. While kernel density estimation produces a probability distribution, the height of the curve at each point gives a density, not a probability. A probability can be obtained only by integrating the density across a range. The curve is normalized so that the integral over all possible values is 1, meaning that the scale of the density axis depends on the data values.

Examples

Plot a univariate distribution along the x axis:

tips \= sns.load\_dataset("tips")
sns.kdeplot(data\=tips, x\="total\_bill")

Copy to clipboard

![../_images/kdeplot_1_0.png](https://seaborn.pydata.org/_images/kdeplot_1_0.png)

Flip the plot by assigning the data variable to the y axis:

sns.kdeplot(data\=tips, y\="total\_bill")

Copy to clipboard

![../_images/kdeplot_3_0.png](https://seaborn.pydata.org/_images/kdeplot_3_0.png)

Plot distributions for each column of a wide-form dataset:

iris \= sns.load\_dataset("iris")
sns.kdeplot(data\=iris)

Copy to clipboard

![../_images/kdeplot_5_0.png](https://seaborn.pydata.org/_images/kdeplot_5_0.png)

Use less smoothing:

sns.kdeplot(data\=tips, x\="total\_bill", bw\_adjust\=.2)

Copy to clipboard

![../_images/kdeplot_7_0.png](https://seaborn.pydata.org/_images/kdeplot_7_0.png)

Use more smoothing, but don’t smooth past the extreme data points:

ax\= sns.kdeplot(data\=tips, x\="total\_bill", bw\_adjust\=5, cut\=0)

Copy to clipboard

![../_images/kdeplot_9_0.png](https://seaborn.pydata.org/_images/kdeplot_9_0.png)

Plot conditional distributions with hue mapping of a second variable:

sns.kdeplot(data\=tips, x\="total\_bill", hue\="time")

Copy to clipboard

![../_images/kdeplot_11_0.png](https://seaborn.pydata.org/_images/kdeplot_11_0.png)

“Stack” the conditional distributions:

sns.kdeplot(data\=tips, x\="total\_bill", hue\="time", multiple\="stack")

Copy to clipboard

![../_images/kdeplot_13_0.png](https://seaborn.pydata.org/_images/kdeplot_13_0.png)

Normalize the stacked distribution at each value in the grid:

sns.kdeplot(data\=tips, x\="total\_bill", hue\="time", multiple\="fill")

Copy to clipboard

![../_images/kdeplot_15_0.png](https://seaborn.pydata.org/_images/kdeplot_15_0.png)

Estimate the cumulative distribution function(s), normalizing each subset:

sns.kdeplot(
    data\=tips, x\="total\_bill", hue\="time",
    cumulative\=True, common\_norm\=False, common\_grid\=True,
)

Copy to clipboard

![../_images/kdeplot_17_0.png](https://seaborn.pydata.org/_images/kdeplot_17_0.png)

Estimate distribution from aggregated data, using weights:

tips\_agg \= (tips
    .groupby("size")
    .agg(total\_bill\=("total\_bill", "mean"), n\=("total\_bill", "count"))
)
sns.kdeplot(data\=tips\_agg, x\="total\_bill", weights\="n")

Copy to clipboard

![../_images/kdeplot_19_0.png](https://seaborn.pydata.org/_images/kdeplot_19_0.png)

Map the data variable with log scaling:

diamonds \= sns.load\_dataset("diamonds")
sns.kdeplot(data\=diamonds, x\="price", log\_scale\=True)

Copy to clipboard

![../_images/kdeplot_21_0.png](https://seaborn.pydata.org/_images/kdeplot_21_0.png)

Use numeric hue mapping:

sns.kdeplot(data\=tips, x\="total\_bill", hue\="size")

Copy to clipboard

![../_images/kdeplot_23_0.png](https://seaborn.pydata.org/_images/kdeplot_23_0.png)

Modify the appearance of the plot:

sns.kdeplot(
   data\=tips, x\="total\_bill", hue\="size",
   fill\=True, common\_norm\=False, palette\="crest",
   alpha\=.5, linewidth\=0,
)

Copy to clipboard

![../_images/kdeplot_25_0.png](https://seaborn.pydata.org/_images/kdeplot_25_0.png)

Plot a bivariate distribution:

geyser \= sns.load\_dataset("geyser")
sns.kdeplot(data\=geyser, x\="waiting", y\="duration")

Copy to clipboard

![../_images/kdeplot_27_0.png](https://seaborn.pydata.org/_images/kdeplot_27_0.png)

Map a third variable with a hue semantic to show conditional distributions:

sns.kdeplot(data\=geyser, x\="waiting", y\="duration", hue\="kind")

Copy to clipboard

![../_images/kdeplot_29_0.png](https://seaborn.pydata.org/_images/kdeplot_29_0.png)

Show filled contours:

sns.kdeplot(
    data\=geyser, x\="waiting", y\="duration", hue\="kind", fill\=True,
)

Copy to clipboard

![../_images/kdeplot_31_0.png](https://seaborn.pydata.org/_images/kdeplot_31_0.png)

Show fewer contour levels, covering less of the distribution:

sns.kdeplot(
    data\=geyser, x\="waiting", y\="duration", hue\="kind",
    levels\=5, thresh\=.2,
)

Copy to clipboard

![../_images/kdeplot_33_0.png](https://seaborn.pydata.org/_images/kdeplot_33_0.png)

Fill the axes extent with a smooth distribution, using a different colormap:

sns.kdeplot(
    data\=geyser, x\="waiting", y\="duration",
    fill\=True, thresh\=0, levels\=100, cmap\="mako",
)

Copy to clipboard

![../_images/kdeplot_35_0.png](https://seaborn.pydata.org/_images/kdeplot_35_0.png)
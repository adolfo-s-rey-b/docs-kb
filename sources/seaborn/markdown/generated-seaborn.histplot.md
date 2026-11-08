 

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

seaborn.histplot[#](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn-histplot "Permalink to this heading")

=============================================================================================================================

seaborn.histplot(_data\=None_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _weights\=None_, _stat\='count'_, _bins\='auto'_, _binwidth\=None_, _binrange\=None_, _discrete\=None_, _cumulative\=False_, _common\_bins\=True_, _common\_norm\=True_, _multiple\='layer'_, _element\='bars'_, _fill\=True_, _shrink\=1_, _kde\=False_, _kde\_kws\=None_, _line\_kws\=None_, _thresh\=0_, _pthresh\=None_, _pmax\=None_, _cbar\=False_, _cbar\_ax\=None_, _cbar\_kws\=None_, _palette\=None_, _hue\_order\=None_, _hue\_norm\=None_, _color\=None_, _log\_scale\=None_, _legend\=True_, _ax\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "Permalink to this definition")

Plot univariate or bivariate histograms to show distributions of datasets.

A histogram is a classic visualization tool that represents the distribution of one or more variables by counting the number of observations that fall within discrete bins.

This function can normalize the statistic computed within each bin to estimate frequency, density or probability mass, and it can add a smooth curve obtained using a kernel density estimate, similar to [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")
.

More information is provided in the [user guide](https://seaborn.pydata.org/tutorial/distributions.html#tutorial-hist)
.

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

If provided, weight the contribution of the corresponding data points towards the count in each bin by these factors.

**stat**str

Aggregate statistic to compute in each bin.

*   `count`: show the number of observations in each bin
    
*   `frequency`: show the number of observations divided by the bin width
    
*   `probability` or `proportion`: normalize such that bar heights sum to 1
    
*   `percent`: normalize such that bar heights sum to 100
    
*   `density`: normalize such that the total area of the histogram equals 1
    

**bins**str, number, vector, or a pair of such values

Generic bin parameter that can be the name of a reference rule, the number of bins, or the breaks of the bins. Passed to [`numpy.histogram_bin_edges()`](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges "(in NumPy v1.26)")
.

**binwidth**number or pair of numbers

Width of each bin, overrides `bins` but can be used with `binrange`.

**binrange**pair of numbers or a pair of pairs

Lowest and highest value for bin edges; can be used either with `bins` or `binwidth`. Defaults to data extremes.

**discrete**bool

If True, default to `binwidth=1` and draw the bars so that they are centered on their corresponding data points. This avoids “gaps” that may otherwise appear when using discrete (integer) data.

**cumulative**bool

If True, plot the cumulative counts as bins increase.

**common\_bins**bool

If True, use the same bins when semantic variables produce multiple plots. If using a reference rule to determine the bins, it will be computed with the full dataset.

**common\_norm**bool

If True and using a normalized statistic, the normalization will apply over the full dataset. Otherwise, normalize each histogram independently.

**multiple**{“layer”, “dodge”, “stack”, “fill”}

Approach to resolving multiple elements when semantic mapping creates subsets. Only relevant with univariate data.

**element**{“bars”, “step”, “poly”}

Visual representation of the histogram statistic. Only relevant with univariate data.

**fill**bool

If True, fill in the space under the histogram. Only relevant with univariate data.

**shrink**number

Scale the width of each bar relative to the binwidth by this factor. Only relevant with univariate data.

**kde**bool

If True, compute a kernel density estimate to smooth the distribution and show on the plot as (one or more) line(s). Only relevant with univariate data.

**kde\_kws**dict

Parameters that control the KDE computation, as in [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")
.

**line\_kws**dict

Parameters that control the KDE visualization, passed to [`matplotlib.axes.Axes.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "(in Matplotlib v3.8.2)")
.

**thresh**number or None

Cells with a statistic less than or equal to this value will be transparent. Only relevant with bivariate data.

**pthresh**number or None

Like `thresh`, but a value in \[0, 1\] such that cells with aggregate counts (or other statistics, when used) up to this proportion of the total will be transparent.

**pmax**number or None

A value in \[0, 1\] that sets that saturation point for the colormap at a value such that cells below constitute this proportion of the total count (or other statistic, when used).

**cbar**bool

If True, add a colorbar to annotate the color mapping in a bivariate plot. Note: Does not currently support plots with a `hue` variable well.

**cbar\_ax**[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

Pre-existing axes for the colorbar.

**cbar\_kws**dict

Additional parameters passed to [`matplotlib.figure.Figure.colorbar()`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.colorbar "(in Matplotlib v3.8.2)")
.

**palette**string, list, dict, or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.8.2)")

Method for choosing the colors to use when mapping the `hue` semantic. String values are passed to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
. List or dict values imply categorical mapping, while a colormap object implies numeric mapping.

**hue\_order**vector of strings

Specify the order of processing and plotting for categorical levels of the `hue` semantic.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")

Either a pair of values that set the normalization range in data units or an object that will map from data units into a \[0, 1\] interval. Usage implies numeric mapping.

**color**[`matplotlib color`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "(in Matplotlib v3.8.2)")

Single color specification for when hue mapping is not used. Otherwise, the plot will try to hook into the matplotlib property cycle.

**log\_scale**bool or number, or pair of bools or numbers

Set axis scale(s) to log. A single value sets the data axis for any numeric axes in the plot. A pair of values sets each axis independently. Numeric values are interpreted as the desired base (default 10). When `None` or `False`, seaborn defers to the existing Axes scale.

**legend**bool

If False, suppress the legend for semantic variables.

**ax**[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

Pre-existing axes for the plot. Otherwise, call [`matplotlib.pyplot.gca()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "(in Matplotlib v3.8.2)")
 internally.

**kwargs**

Other keyword arguments are passed to one of the following matplotlib functions:

*   [`matplotlib.axes.Axes.bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "(in Matplotlib v3.8.2)")
     (univariate, element=”bars”)
    
*   [`matplotlib.axes.Axes.fill_between()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "(in Matplotlib v3.8.2)")
     (univariate, other element, fill=True)
    
*   [`matplotlib.axes.Axes.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "(in Matplotlib v3.8.2)")
     (univariate, other element, fill=False)
    
*   [`matplotlib.axes.Axes.pcolormesh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "(in Matplotlib v3.8.2)")
     (bivariate)
    

Returns:

[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

The matplotlib axes containing the plot.

See also

[`displot`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")

Figure-level interface to distribution plot functions.

[`kdeplot`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")

Plot univariate or bivariate distributions using kernel density estimation.

[`rugplot`](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot "seaborn.rugplot")

Plot a tick at each observation value along the x and/or y axes.

[`ecdfplot`](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn.ecdfplot "seaborn.ecdfplot")

Plot empirical cumulative distribution functions.

[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

Draw a bivariate plot with univariate marginal distributions.

Notes

The choice of bins for computing and plotting a histogram can exert substantial influence on the insights that one is able to draw from the visualization. If the bins are too large, they may erase important features. On the other hand, bins that are too small may be dominated by random variability, obscuring the shape of the true underlying distribution. The default bin size is determined using a reference rule that depends on the sample size and variance. This works well in many cases, (i.e., with “well-behaved” data) but it fails in others. It is always a good to try different bin sizes to be sure that you are not missing something important. This function allows you to specify bins in several different ways, such as by setting the total number of bins to use, the width of each bin, or the specific locations where the bins should break.

Examples

Assign a variable to `x` to plot a univariate distribution along the x axis:

penguins \= sns.load\_dataset("penguins")
sns.histplot(data\=penguins, x\="flipper\_length\_mm")

Copy to clipboard

![../_images/histplot_1_0.png](https://seaborn.pydata.org/_images/histplot_1_0.png)

Flip the plot by assigning the data variable to the y axis:

sns.histplot(data\=penguins, y\="flipper\_length\_mm")

Copy to clipboard

![../_images/histplot_3_0.png](https://seaborn.pydata.org/_images/histplot_3_0.png)

Check how well the histogram represents the data by specifying a different bin width:

sns.histplot(data\=penguins, x\="flipper\_length\_mm", binwidth\=3)

Copy to clipboard

![../_images/histplot_5_0.png](https://seaborn.pydata.org/_images/histplot_5_0.png)

You can also define the total number of bins to use:

sns.histplot(data\=penguins, x\="flipper\_length\_mm", bins\=30)

Copy to clipboard

![../_images/histplot_7_0.png](https://seaborn.pydata.org/_images/histplot_7_0.png)

Add a kernel density estimate to smooth the histogram, providing complementary information about the shape of the distribution:

sns.histplot(data\=penguins, x\="flipper\_length\_mm", kde\=True)

Copy to clipboard

![../_images/histplot_9_0.png](https://seaborn.pydata.org/_images/histplot_9_0.png)

If neither `x` nor `y` is assigned, the dataset is treated as wide-form, and a histogram is drawn for each numeric column:

sns.histplot(data\=penguins)

Copy to clipboard

![../_images/histplot_11_0.png](https://seaborn.pydata.org/_images/histplot_11_0.png)

You can otherwise draw multiple histograms from a long-form dataset with hue mapping:

sns.histplot(data\=penguins, x\="flipper\_length\_mm", hue\="species")

Copy to clipboard

![../_images/histplot_13_0.png](https://seaborn.pydata.org/_images/histplot_13_0.png)

The default approach to plotting multiple distributions is to “layer” them, but you can also “stack” them:

sns.histplot(data\=penguins, x\="flipper\_length\_mm", hue\="species", multiple\="stack")

Copy to clipboard

![../_images/histplot_15_0.png](https://seaborn.pydata.org/_images/histplot_15_0.png)

Overlapping bars can be hard to visually resolve. A different approach would be to draw a step function:

sns.histplot(penguins, x\="flipper\_length\_mm", hue\="species", element\="step")

Copy to clipboard

![../_images/histplot_17_0.png](https://seaborn.pydata.org/_images/histplot_17_0.png)

You can move even farther away from bars by drawing a polygon with vertices in the center of each bin. This may make it easier to see the shape of the distribution, but use with caution: it will be less obvious to your audience that they are looking at a histogram:

sns.histplot(penguins, x\="flipper\_length\_mm", hue\="species", element\="poly")

Copy to clipboard

![../_images/histplot_19_0.png](https://seaborn.pydata.org/_images/histplot_19_0.png)

To compare the distribution of subsets that differ substantially in size, use independent density normalization:

sns.histplot(
    penguins, x\="bill\_length\_mm", hue\="island", element\="step",
    stat\="density", common\_norm\=False,
)

Copy to clipboard

![../_images/histplot_21_0.png](https://seaborn.pydata.org/_images/histplot_21_0.png)

It’s also possible to normalize so that each bar’s height shows a probability, proportion, or percent, which make more sense for discrete variables:

tips \= sns.load\_dataset("tips")
sns.histplot(data\=tips, x\="size", stat\="percent", discrete\=True)

Copy to clipboard

![../_images/histplot_23_0.png](https://seaborn.pydata.org/_images/histplot_23_0.png)

You can even draw a histogram over categorical variables (although this is an experimental feature):

sns.histplot(data\=tips, x\="day", shrink\=.8)

Copy to clipboard

![../_images/histplot_25_0.png](https://seaborn.pydata.org/_images/histplot_25_0.png)

When using a `hue` semantic with discrete data, it can make sense to “dodge” the levels:

sns.histplot(data\=tips, x\="day", hue\="sex", multiple\="dodge", shrink\=.8)

Copy to clipboard

![../_images/histplot_27_0.png](https://seaborn.pydata.org/_images/histplot_27_0.png)

Real-world data is often skewed. For heavily skewed distributions, it’s better to define the bins in log space. Compare:

planets \= sns.load\_dataset("planets")
sns.histplot(data\=planets, x\="distance")

Copy to clipboard

![../_images/histplot_29_0.png](https://seaborn.pydata.org/_images/histplot_29_0.png)

To the log-scale version:

sns.histplot(data\=planets, x\="distance", log\_scale\=True)

Copy to clipboard

![../_images/histplot_31_0.png](https://seaborn.pydata.org/_images/histplot_31_0.png)

There are also a number of options for how the histogram appears. You can show unfilled bars:

sns.histplot(data\=planets, x\="distance", log\_scale\=True, fill\=False)

Copy to clipboard

![../_images/histplot_33_0.png](https://seaborn.pydata.org/_images/histplot_33_0.png)

Or an unfilled step function:

sns.histplot(data\=planets, x\="distance", log\_scale\=True, element\="step", fill\=False)

Copy to clipboard

![../_images/histplot_35_0.png](https://seaborn.pydata.org/_images/histplot_35_0.png)

Step functions, especially when unfilled, make it easy to compare cumulative histograms:

sns.histplot(
    data\=planets, x\="distance", hue\="method",
    hue\_order\=\["Radial Velocity", "Transit"\],
    log\_scale\=True, element\="step", fill\=False,
    cumulative\=True, stat\="density", common\_norm\=False,
)

Copy to clipboard

![../_images/histplot_37_0.png](https://seaborn.pydata.org/_images/histplot_37_0.png)

When both `x` and `y` are assigned, a bivariate histogram is computed and shown as a heatmap:

sns.histplot(penguins, x\="bill\_depth\_mm", y\="body\_mass\_g")

Copy to clipboard

![../_images/histplot_39_0.png](https://seaborn.pydata.org/_images/histplot_39_0.png)

It’s possible to assign a `hue` variable too, although this will not work well if data from the different levels have substantial overlap:

sns.histplot(penguins, x\="bill\_depth\_mm", y\="body\_mass\_g", hue\="species")

Copy to clipboard

![../_images/histplot_41_0.png](https://seaborn.pydata.org/_images/histplot_41_0.png)

Multiple color maps can make sense when one of the variables is discrete:

sns.histplot(
    penguins, x\="bill\_depth\_mm", y\="species", hue\="species", legend\=False
)

Copy to clipboard

![../_images/histplot_43_0.png](https://seaborn.pydata.org/_images/histplot_43_0.png)

The bivariate histogram accepts all of the same options for computation as its univariate counterpart, using tuples to parametrize `x` and `y` independently:

sns.histplot(
    planets, x\="year", y\="distance",
    bins\=30, discrete\=(True, False), log\_scale\=(False, True),
)

Copy to clipboard

![../_images/histplot_45_0.png](https://seaborn.pydata.org/_images/histplot_45_0.png)

The default behavior makes cells with no observations transparent, although this can be disabled:

sns.histplot(
    planets, x\="year", y\="distance",
    bins\=30, discrete\=(True, False), log\_scale\=(False, True),
    thresh\=None,
)

Copy to clipboard

![../_images/histplot_47_0.png](https://seaborn.pydata.org/_images/histplot_47_0.png)

It’s also possible to set the threshold and colormap saturation point in terms of the proportion of cumulative counts:

sns.histplot(
    planets, x\="year", y\="distance",
    bins\=30, discrete\=(True, False), log\_scale\=(False, True),
    pthresh\=.05, pmax\=.9,
)

Copy to clipboard

![../_images/histplot_49_0.png](https://seaborn.pydata.org/_images/histplot_49_0.png)

To annotate the colormap, add a colorbar:

sns.histplot(
    planets, x\="year", y\="distance",
    bins\=30, discrete\=(True, False), log\_scale\=(False, True),
    cbar\=True, cbar\_kws\=dict(shrink\=.75),
)

Copy to clipboard

![../_images/histplot_51_0.png](https://seaborn.pydata.org/_images/histplot_51_0.png)
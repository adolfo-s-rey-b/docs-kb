 

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

seaborn.ecdfplot[#](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn-ecdfplot "Permalink to this heading")

=============================================================================================================================

seaborn.ecdfplot(_data\=None_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _weights\=None_, _stat\='proportion'_, _complementary\=False_, _palette\=None_, _hue\_order\=None_, _hue\_norm\=None_, _log\_scale\=None_, _legend\=True_, _ax\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn.ecdfplot "Permalink to this definition")

Plot empirical cumulative distribution functions.

An ECDF represents the proportion or count of observations falling below each unique value in a dataset. Compared to a histogram or density plot, it has the advantage that each observation is visualized directly, meaning that there are no binning or smoothing parameters that need to be adjusted. It also aids direct comparisons between multiple distributions. A downside is that the relationship between the appearance of the plot and the basic properties of the distribution (such as its central tendency, variance, and the presence of any bimodality) may not be as intuitive.

More information is provided in the [user guide](https://seaborn.pydata.org/tutorial/distributions.html#tutorial-ecdf)
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

If provided, weight the contribution of the corresponding data points towards the cumulative distribution using these values.

**stat**{{“proportion”, “percent”, “count”}}

Distribution statistic to compute.

**complementary**bool

If True, use the complementary CDF (1 - CDF)

**palette**string, list, dict, or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.8.2)")

Method for choosing the colors to use when mapping the `hue` semantic. String values are passed to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
. List or dict values imply categorical mapping, while a colormap object implies numeric mapping.

**hue\_order**vector of strings

Specify the order of processing and plotting for categorical levels of the `hue` semantic.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")

Either a pair of values that set the normalization range in data units or an object that will map from data units into a \[0, 1\] interval. Usage implies numeric mapping.

**log\_scale**bool or number, or pair of bools or numbers

Set axis scale(s) to log. A single value sets the data axis for any numeric axes in the plot. A pair of values sets each axis independently. Numeric values are interpreted as the desired base (default 10). When `None` or `False`, seaborn defers to the existing Axes scale.

**legend**bool

If False, suppress the legend for semantic variables.

**ax**[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

Pre-existing axes for the plot. Otherwise, call [`matplotlib.pyplot.gca()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "(in Matplotlib v3.8.2)")
 internally.

**kwargs**

Other keyword arguments are passed to [`matplotlib.axes.Axes.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "(in Matplotlib v3.8.2)")
.

Returns:

[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

The matplotlib axes containing the plot.

See also

[`displot`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")

Figure-level interface to distribution plot functions.

[`histplot`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")

Plot a histogram of binned counts with optional normalization or smoothing.

[`kdeplot`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")

Plot univariate or bivariate distributions using kernel density estimation.

[`rugplot`](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot "seaborn.rugplot")

Plot a tick at each observation value along the x and/or y axes.

Examples

Plot a univariate distribution along the x axis:

penguins \= sns.load\_dataset("penguins")
sns.ecdfplot(data\=penguins, x\="flipper\_length\_mm")

Copy to clipboard

![../_images/ecdfplot_1_0.png](https://seaborn.pydata.org/_images/ecdfplot_1_0.png)

Flip the plot by assigning the data variable to the y axis:

sns.ecdfplot(data\=penguins, y\="flipper\_length\_mm")

Copy to clipboard

![../_images/ecdfplot_3_0.png](https://seaborn.pydata.org/_images/ecdfplot_3_0.png)

If neither `x` nor `y` is assigned, the dataset is treated as wide-form, and a histogram is drawn for each numeric column:

sns.ecdfplot(data\=penguins.filter(like\="bill\_", axis\="columns"))

Copy to clipboard

![../_images/ecdfplot_5_0.png](https://seaborn.pydata.org/_images/ecdfplot_5_0.png)

You can also draw multiple histograms from a long-form dataset with hue mapping:

sns.ecdfplot(data\=penguins, x\="bill\_length\_mm", hue\="species")

Copy to clipboard

![../_images/ecdfplot_7_0.png](https://seaborn.pydata.org/_images/ecdfplot_7_0.png)

The default distribution statistic is normalized to show a proportion, but you can show absolute counts or percents instead:

sns.ecdfplot(data\=penguins, x\="bill\_length\_mm", hue\="species", stat\="count")

Copy to clipboard

![../_images/ecdfplot_9_0.png](https://seaborn.pydata.org/_images/ecdfplot_9_0.png)

It’s also possible to plot the empirical complementary CDF (1 - CDF):

sns.ecdfplot(data\=penguins, x\="bill\_length\_mm", hue\="species", complementary\=True)

Copy to clipboard

![../_images/ecdfplot_11_0.png](https://seaborn.pydata.org/_images/ecdfplot_11_0.png)
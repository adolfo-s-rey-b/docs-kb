 

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

seaborn.displot[#](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn-displot "Permalink to this heading")

==========================================================================================================================

seaborn.displot(_data\=None_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _row\=None_, _col\=None_, _weights\=None_, _kind\='hist'_, _rug\=False_, _rug\_kws\=None_, _log\_scale\=None_, _legend\=True_, _palette\=None_, _hue\_order\=None_, _hue\_norm\=None_, _color\=None_, _col\_wrap\=None_, _row\_order\=None_, _col\_order\=None_, _height\=5_, _aspect\=1_, _facet\_kws\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "Permalink to this definition")

Figure-level interface for drawing distribution plots onto a FacetGrid.

This function provides access to several approaches for visualizing the univariate or bivariate distribution of data, including subsets of data defined by semantic mapping and faceting across multiple subplots. The `kind` parameter selects the approach to use:

*   [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")
     (with `kind="hist"`; the default)
    
*   [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")
     (with `kind="kde"`)
    
*   [`ecdfplot()`](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn.ecdfplot "seaborn.ecdfplot")
     (with `kind="ecdf"`; univariate-only)
    

Additionally, a [`rugplot()`](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot "seaborn.rugplot")
 can be added to any kind of plot to show individual observations.

Extra keyword arguments are passed to the underlying function, so you should refer to the documentation for each to understand the complete set of options for making plots with this interface.

See the [distribution plots tutorial](https://seaborn.pydata.org/tutorial/distributions.html)
 for a more in-depth discussion of the relative strengths and weaknesses of each approach. The distinction between figure-level and axes-level functions is explained further in the [user guide](https://seaborn.pydata.org/tutorial/function_overview.html)
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

**row, col**vectors or keys in `data`

Variables that define subsets to plot on different facets.

**weights**vector or key in `data`

Observation weights used for computing the distribution function.

**kind**{“hist”, “kde”, “ecdf”}

Approach for visualizing the data. Selects the underlying plotting function and determines the additional set of valid parameters.

**rug**bool

If True, show each observation with marginal ticks (as in [`rugplot()`](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot "seaborn.rugplot")
).

**rug\_kws**dict

Parameters to control the appearance of the rug plot.

**log\_scale**bool or number, or pair of bools or numbers

Set axis scale(s) to log. A single value sets the data axis for any numeric axes in the plot. A pair of values sets each axis independently. Numeric values are interpreted as the desired base (default 10). When `None` or `False`, seaborn defers to the existing Axes scale.

**legend**bool

If False, suppress the legend for semantic variables.

**palette**string, list, dict, or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.8.2)")

Method for choosing the colors to use when mapping the `hue` semantic. String values are passed to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
. List or dict values imply categorical mapping, while a colormap object implies numeric mapping.

**hue\_order**vector of strings

Specify the order of processing and plotting for categorical levels of the `hue` semantic.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")

Either a pair of values that set the normalization range in data units or an object that will map from data units into a \[0, 1\] interval. Usage implies numeric mapping.

**color**[`matplotlib color`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "(in Matplotlib v3.8.2)")

Single color specification for when hue mapping is not used. Otherwise, the plot will try to hook into the matplotlib property cycle.

**col\_wrap**int

“Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a `row` facet.

**{row,col}\_order**vector of strings

Specify the order in which levels of the `row` and/or `col` variables appear in the grid of subplots.

**height**scalar

Height (in inches) of each facet. See also: `aspect`.

**aspect**scalar

Aspect ratio of each facet, so that `aspect * height` gives the width of each facet in inches.

**facet\_kws**dict

Additional parameters passed to [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

**kwargs**

Other keyword arguments are documented with the relevant axes-level function:

*   [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")
     (with `kind="hist"`)
    
*   [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")
     (with `kind="kde"`)
    
*   [`ecdfplot()`](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn.ecdfplot "seaborn.ecdfplot")
     (with `kind="ecdf"`)
    

Returns:

[`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

An object managing one or more subplots that correspond to conditional data subsets with convenient methods for batch-setting of axes attributes.

See also

[`histplot`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")

Plot a histogram of binned counts with optional normalization or smoothing.

[`kdeplot`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")

Plot univariate or bivariate distributions using kernel density estimation.

[`rugplot`](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot "seaborn.rugplot")

Plot a tick at each observation value along the x and/or y axes.

[`ecdfplot`](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn.ecdfplot "seaborn.ecdfplot")

Plot empirical cumulative distribution functions.

[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

Draw a bivariate plot with univariate marginal distributions.

Examples

See the API documentation for the axes-level functions for more details about the breadth of options available for each plot kind.

The default plot kind is a histogram:

penguins \= sns.load\_dataset("penguins")
sns.displot(data\=penguins, x\="flipper\_length\_mm")

Copy to clipboard

![../_images/displot_1_0.png](https://seaborn.pydata.org/_images/displot_1_0.png)

Use the `kind` parameter to select a different representation:

sns.displot(data\=penguins, x\="flipper\_length\_mm", kind\="kde")

Copy to clipboard

![../_images/displot_3_0.png](https://seaborn.pydata.org/_images/displot_3_0.png)

There are three main plot kinds; in addition to histograms and kernel density estimates (KDEs), you can also draw empirical cumulative distribution functions (ECDFs):

sns.displot(data\=penguins, x\="flipper\_length\_mm", kind\="ecdf")

Copy to clipboard

![../_images/displot_5_0.png](https://seaborn.pydata.org/_images/displot_5_0.png)

While in histogram mode, it is also possible to add a KDE curve:

sns.displot(data\=penguins, x\="flipper\_length\_mm", kde\=True)

Copy to clipboard

![../_images/displot_7_0.png](https://seaborn.pydata.org/_images/displot_7_0.png)

To draw a bivariate plot, assign both `x` and `y`:

sns.displot(data\=penguins, x\="flipper\_length\_mm", y\="bill\_length\_mm")

Copy to clipboard

![../_images/displot_9_0.png](https://seaborn.pydata.org/_images/displot_9_0.png)

Currently, bivariate plots are available only for histograms and KDEs:

sns.displot(data\=penguins, x\="flipper\_length\_mm", y\="bill\_length\_mm", kind\="kde")

Copy to clipboard

![../_images/displot_11_0.png](https://seaborn.pydata.org/_images/displot_11_0.png)

For each kind of plot, you can also show individual observations with a marginal “rug”:

g \= sns.displot(data\=penguins, x\="flipper\_length\_mm", y\="bill\_length\_mm", kind\="kde", rug\=True)

Copy to clipboard

![../_images/displot_13_0.png](https://seaborn.pydata.org/_images/displot_13_0.png)

Each kind of plot can be drawn separately for subsets of data using `hue` mapping:

sns.displot(data\=penguins, x\="flipper\_length\_mm", hue\="species", kind\="kde")

Copy to clipboard

![../_images/displot_15_0.png](https://seaborn.pydata.org/_images/displot_15_0.png)

Additional keyword arguments are passed to the appropriate underlying plotting function, allowing for further customization:

sns.displot(data\=penguins, x\="flipper\_length\_mm", hue\="species", multiple\="stack")

Copy to clipboard

![../_images/displot_17_0.png](https://seaborn.pydata.org/_images/displot_17_0.png)

The figure is constructed using a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
, meaning that you can also show subsets on distinct subplots, or “facets”:

sns.displot(data\=penguins, x\="flipper\_length\_mm", hue\="species", col\="sex", kind\="kde")

Copy to clipboard

![../_images/displot_19_0.png](https://seaborn.pydata.org/_images/displot_19_0.png)

Because the figure is drawn with a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
, you control its size and shape with the `height` and `aspect` parameters:

sns.displot(
    data\=penguins, y\="flipper\_length\_mm", hue\="sex", col\="species",
    kind\="ecdf", height\=4, aspect\=.7,
)

Copy to clipboard

![../_images/displot_21_0.png](https://seaborn.pydata.org/_images/displot_21_0.png)

The function returns the [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 object with the plot, and you can use the methods on this object to customize it further:

g \= sns.displot(
    data\=penguins, y\="flipper\_length\_mm", hue\="sex", col\="species",
    kind\="kde", height\=4, aspect\=.7,
)
g.set\_axis\_labels("Density (a.u.)", "Flipper length (mm)")
g.set\_titles("{col\_name} penguins")

Copy to clipboard

![../_images/displot_23_0.png](https://seaborn.pydata.org/_images/displot_23_0.png)
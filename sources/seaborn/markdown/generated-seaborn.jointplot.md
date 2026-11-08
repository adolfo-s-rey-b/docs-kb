 

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

seaborn.jointplot[#](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn-jointplot "Permalink to this heading")

================================================================================================================================

seaborn.jointplot(_data\=None_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _kind\='scatter'_, _height\=6_, _ratio\=5_, _space\=0.2_, _dropna\=False_, _xlim\=None_, _ylim\=None_, _color\=None_, _palette\=None_, _hue\_order\=None_, _hue\_norm\=None_, _marginal\_ticks\=False_, _joint\_kws\=None_, _marginal\_kws\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "Permalink to this definition")

Draw a plot of two variables with bivariate and univariate graphs.

This function provides a convenient interface to the [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")
 class, with several canned plot kinds. This is intended to be a fairly lightweight wrapper; if you need more flexibility, you should use [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")
 directly.

Parameters:

**data**[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)")
, [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v1.26)")
, mapping, or sequence

Input data structure. Either a long-form collection of vectors that can be assigned to named variables or a wide-form dataset that will be internally reshaped.

**x, y**vectors or keys in `data`

Variables that specify positions on the x and y axes.

**hue**vector or key in `data`

Semantic variable that is mapped to determine the color of plot elements.

**kind**{ “scatter” | “kde” | “hist” | “hex” | “reg” | “resid” }

Kind of plot to draw. See the examples for references to the underlying functions.

**height**numeric

Size of the figure (it will be square).

**ratio**numeric

Ratio of joint axes height to marginal axes height.

**space**numeric

Space between the joint and marginal axes

**dropna**bool

If True, remove observations that are missing from `x` and `y`.

**{x, y}lim**pairs of numbers

Axis limits to set before plotting.

**color**[`matplotlib color`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "(in Matplotlib v3.8.2)")

Single color specification for when hue mapping is not used. Otherwise, the plot will try to hook into the matplotlib property cycle.

**palette**string, list, dict, or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.8.2)")

Method for choosing the colors to use when mapping the `hue` semantic. String values are passed to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
. List or dict values imply categorical mapping, while a colormap object implies numeric mapping.

**hue\_order**vector of strings

Specify the order of processing and plotting for categorical levels of the `hue` semantic.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")

Either a pair of values that set the normalization range in data units or an object that will map from data units into a \[0, 1\] interval. Usage implies numeric mapping.

**marginal\_ticks**bool

If False, suppress ticks on the count/density axis of the marginal plots.

**{joint, marginal}\_kws**dicts

Additional keyword arguments for the plot components.

**kwargs**

Additional keyword arguments are passed to the function used to draw the plot on the joint Axes, superseding items in the `joint_kws` dictionary.

Returns:

[`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")

An object managing multiple subplots that correspond to joint and marginal axes for plotting a bivariate relationship or distribution.

See also

[`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")

Set up a figure with joint and marginal views on bivariate data.

[`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")

Set up a figure with joint and marginal views on multiple variables.

[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

Draw multiple bivariate plots with univariate marginal distributions.

Examples

In the simplest invocation, assign `x` and `y` to create a scatterplot (using [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")
) with marginal histograms (using [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")
):

penguins \= sns.load\_dataset("penguins")
sns.jointplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")

Copy to clipboard

![../_images/jointplot_1_0.png](https://seaborn.pydata.org/_images/jointplot_1_0.png)

Assigning a `hue` variable will add conditional colors to the scatterplot and draw separate density curves (using [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")
) on the marginal axes:

sns.jointplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm", hue\="species")

Copy to clipboard

![../_images/jointplot_3_0.png](https://seaborn.pydata.org/_images/jointplot_3_0.png)

Several different approaches to plotting are available through the `kind` parameter. Setting `kind="kde"` will draw both bivariate and univariate KDEs:

sns.jointplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm", hue\="species", kind\="kde")

Copy to clipboard

![../_images/jointplot_5_0.png](https://seaborn.pydata.org/_images/jointplot_5_0.png)

Set `kind="reg"` to add a linear regression fit (using [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")
) and univariate KDE curves:

sns.jointplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm", kind\="reg")

Copy to clipboard

![../_images/jointplot_7_0.png](https://seaborn.pydata.org/_images/jointplot_7_0.png)

There are also two options for bin-based visualization of the joint distribution. The first, with `kind="hist"`, uses [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")
 on all of the axes:

sns.jointplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm", kind\="hist")

Copy to clipboard

![../_images/jointplot_9_0.png](https://seaborn.pydata.org/_images/jointplot_9_0.png)

Alternatively, setting `kind="hex"` will use [`matplotlib.axes.Axes.hexbin()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "(in Matplotlib v3.8.2)")
 to compute a bivariate histogram using hexagonal bins:

sns.jointplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm", kind\="hex")

Copy to clipboard

![../_images/jointplot_11_0.png](https://seaborn.pydata.org/_images/jointplot_11_0.png)

Additional keyword arguments can be passed down to the underlying plots:

sns.jointplot(
    data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm",
    marker\="+", s\=100, marginal\_kws\=dict(bins\=25, fill\=False),
)

Copy to clipboard

![../_images/jointplot_13_0.png](https://seaborn.pydata.org/_images/jointplot_13_0.png)

Use [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")
 parameters to control the size and layout of the figure:

sns.jointplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm", height\=5, ratio\=2, marginal\_ticks\=True)

Copy to clipboard

![../_images/jointplot_15_0.png](https://seaborn.pydata.org/_images/jointplot_15_0.png)

To add more layers onto the plot, use the methods on the [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")
 object that [`jointplot()`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")
 returns:

g \= sns.jointplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")
g.plot\_joint(sns.kdeplot, color\="r", zorder\=0, levels\=6)
g.plot\_marginals(sns.rugplot, color\="r", height\=-.15, clip\_on\=False)

Copy to clipboard

![../_images/jointplot_17_0.png](https://seaborn.pydata.org/_images/jointplot_17_0.png)
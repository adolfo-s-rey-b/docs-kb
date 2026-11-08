 

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

seaborn.pairplot[#](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn-pairplot "Permalink to this heading")

=============================================================================================================================

seaborn.pairplot(_data_, _\*_, _hue\=None_, _hue\_order\=None_, _palette\=None_, _vars\=None_, _x\_vars\=None_, _y\_vars\=None_, _kind\='scatter'_, _diag\_kind\='auto'_, _markers\=None_, _height\=2.5_, _aspect\=1_, _corner\=False_, _dropna\=False_, _plot\_kws\=None_, _diag\_kws\=None_, _grid\_kws\=None_, _size\=None_)[#](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot "Permalink to this definition")

Plot pairwise relationships in a dataset.

By default, this function will create a grid of Axes such that each numeric variable in `data` will by shared across the y-axes across a single row and the x-axes across a single column. The diagonal plots are treated differently: a univariate distribution plot is drawn to show the marginal distribution of the data in each column.

It is also possible to show a subset of variables or plot different variables on the rows and columns.

This is a high-level interface for [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
 that is intended to make it easy to draw a few common styles. You should use [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
 directly if you need more flexibility.

Parameters:

**data**`pandas.DataFrame`

Tidy (long-form) dataframe where each column is a variable and each row is an observation.

**hue**name of variable in `data`

Variable in `data` to map plot aspects to different colors.

**hue\_order**list of strings

Order for the levels of the hue variable in the palette

**palette**dict or seaborn color palette

Set of colors for mapping the `hue` variable. If a dict, keys should be values in the `hue` variable.

**vars**list of variable names

Variables within `data` to use, otherwise use every column with a numeric datatype.

**{x, y}\_vars**lists of variable names

Variables within `data` to use separately for the rows and columns of the figure; i.e. to make a non-square plot.

**kind**{‘scatter’, ‘kde’, ‘hist’, ‘reg’}

Kind of plot to make.

**diag\_kind**{‘auto’, ‘hist’, ‘kde’, None}

Kind of plot for the diagonal subplots. If ‘auto’, choose based on whether or not `hue` is used.

**markers**single matplotlib marker code or list

Either the marker to use for all scatterplot points or a list of markers with a length the same as the number of levels in the hue variable so that differently colored points will also have different scatterplot markers.

**height**scalar

Height (in inches) of each facet.

**aspect**scalar

Aspect \* height gives the width (in inches) of each facet.

**corner**bool

If True, don’t add axes to the upper (off-diagonal) triangle of the grid, making this a “corner” plot.

**dropna**boolean

Drop missing values from the data before plotting.

**{plot, diag, grid}\_kws**dicts

Dictionaries of keyword arguments. `plot_kws` are passed to the bivariate plotting function, `diag_kws` are passed to the univariate plotting function, and `grid_kws` are passed to the [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
 constructor.

Returns:

**grid**[`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")

Returns the underlying [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
 instance for further tweaking.

See also

[`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")

Subplot grid for more flexible plotting of pairwise relationships.

[`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")

Grid for plotting joint and marginal distributions of two variables.

Examples

The simplest invocation uses [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")
 for each pairing of the variables and [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")
 for the marginal plots along the diagonal:

penguins \= sns.load\_dataset("penguins")
sns.pairplot(penguins)

Copy to clipboard

![../_images/pairplot_1_0.png](https://seaborn.pydata.org/_images/pairplot_1_0.png)

Assigning a `hue` variable adds a semantic mapping and changes the default marginal plot to a layered kernel density estimate (KDE):

sns.pairplot(penguins, hue\="species")

Copy to clipboard

![../_images/pairplot_3_0.png](https://seaborn.pydata.org/_images/pairplot_3_0.png)

It’s possible to force marginal histograms:

sns.pairplot(penguins, hue\="species", diag\_kind\="hist")

Copy to clipboard

![../_images/pairplot_5_0.png](https://seaborn.pydata.org/_images/pairplot_5_0.png)

The `kind` parameter determines both the diagonal and off-diagonal plotting style. Several options are available, including using [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")
 to draw KDEs:

sns.pairplot(penguins, kind\="kde")

Copy to clipboard

![../_images/pairplot_7_0.png](https://seaborn.pydata.org/_images/pairplot_7_0.png)

Or [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")
 to draw both bivariate and univariate histograms:

sns.pairplot(penguins, kind\="hist")

Copy to clipboard

![../_images/pairplot_9_0.png](https://seaborn.pydata.org/_images/pairplot_9_0.png)

The `markers` parameter applies a style mapping on the off-diagonal axes. Currently, it will be redundant with the `hue` variable:

sns.pairplot(penguins, hue\="species", markers\=\["o", "s", "D"\])

Copy to clipboard

![../_images/pairplot_11_0.png](https://seaborn.pydata.org/_images/pairplot_11_0.png)

As with other figure-level functions, the size of the figure is controlled by setting the `height` of each individual subplot:

sns.pairplot(penguins, height\=1.5)

Copy to clipboard

![../_images/pairplot_13_0.png](https://seaborn.pydata.org/_images/pairplot_13_0.png)

Use `vars` or `x_vars` and `y_vars` to select the variables to plot:

sns.pairplot(
    penguins,
    x\_vars\=\["bill\_length\_mm", "bill\_depth\_mm", "flipper\_length\_mm"\],
    y\_vars\=\["bill\_length\_mm", "bill\_depth\_mm"\],
)

Copy to clipboard

![../_images/pairplot_15_0.png](https://seaborn.pydata.org/_images/pairplot_15_0.png)

Set `corner=True` to plot only the lower triangle:

sns.pairplot(penguins, corner\=True)

Copy to clipboard

![../_images/pairplot_17_0.png](https://seaborn.pydata.org/_images/pairplot_17_0.png)

The `plot_kws` and `diag_kws` parameters accept dicts of keyword arguments to customize the off-diagonal and diagonal plots, respectively:

sns.pairplot(
    penguins,
    plot\_kws\=dict(marker\="+", linewidth\=1),
    diag\_kws\=dict(fill\=False),
)

Copy to clipboard

![../_images/pairplot_19_0.png](https://seaborn.pydata.org/_images/pairplot_19_0.png)

The return object is the underlying [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
, which can be used to further customize the plot:

g \= sns.pairplot(penguins, diag\_kind\="kde")
g.map\_lower(sns.kdeplot, levels\=4, color\=".2")

Copy to clipboard

![../_images/pairplot_21_0.png](https://seaborn.pydata.org/_images/pairplot_21_0.png)
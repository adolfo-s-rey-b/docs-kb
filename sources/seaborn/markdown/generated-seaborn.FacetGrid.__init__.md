 

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

seaborn.FacetGrid.\_\_init\_\_[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.__init__.html#seaborn-facetgrid-init "Permalink to this heading")

===========================================================================================================================================================

FacetGrid.\_\_init\_\_(_data_, _\*_, _row\=None_, _col\=None_, _hue\=None_, _col\_wrap\=None_, _sharex\=True_, _sharey\=True_, _height\=3_, _aspect\=1_, _palette\=None_, _row\_order\=None_, _col\_order\=None_, _hue\_order\=None_, _hue\_kws\=None_, _dropna\=False_, _legend\_out\=True_, _despine\=True_, _margin\_titles\=False_, _xlim\=None_, _ylim\=None_, _subplot\_kws\=None_, _gridspec\_kws\=None_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.__init__.html#seaborn.FacetGrid.__init__ "Permalink to this definition")

Initialize the matplotlib figure and FacetGrid object.

This class maps a dataset onto multiple axes arrayed in a grid of rows and columns that correspond to _levels_ of variables in the dataset. The plots it produces are often called “lattice”, “trellis”, or “small-multiple” graphics.

It can also represent levels of a third variable with the `hue` parameter, which plots different subsets of data in different colors. This uses color to resolve elements on a third dimension, but only draws subsets on top of each other and will not tailor the `hue` parameter for the specific visualization the way that axes-level functions that accept `hue` will.

The basic workflow is to initialize the [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 object with the dataset and the variables that are used to structure the grid. Then one or more plotting functions can be applied to each subset by calling [`FacetGrid.map()`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn.FacetGrid.map "seaborn.FacetGrid.map")
 or [`FacetGrid.map_dataframe()`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html#seaborn.FacetGrid.map_dataframe "seaborn.FacetGrid.map_dataframe")
. Finally, the plot can be tweaked with other methods to do things like change the axis labels, use different ticks, or add a legend. See the detailed code examples below for more information.

Warning

When using seaborn functions that infer semantic mappings from a dataset, care must be taken to synchronize those mappings across facets (e.g., by defining the `hue` mapping with a palette dict or setting the data type of the variables to `category`). In most cases, it will be better to use a figure-level function (e.g. [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")
 or [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")
) than to use [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 directly.

See the [tutorial](https://seaborn.pydata.org/tutorial/axis_grids.html#grid-tutorial)
 for more information.

Parameters:

**data**DataFrame

Tidy (“long-form”) dataframe where each column is a variable and each row is an observation.

**row, col, hue**strings

Variables that define subsets of the data, which will be drawn on separate facets in the grid. See the `{var}_order` parameters to control the order of levels of this variable.

**col\_wrap**int

“Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a `row` facet.

**share{x,y}**bool, ‘col’, or ‘row’ optional

If true, the facets will share y axes across columns and/or x axes across rows.

**height**scalar

Height (in inches) of each facet. See also: `aspect`.

**aspect**scalar

Aspect ratio of each facet, so that `aspect * height` gives the width of each facet in inches.

**palette**palette name, list, or dict

Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
, or a dictionary mapping hue levels to matplotlib colors.

**{row,col,hue}\_order**lists

Order for the levels of the faceting variables. By default, this will be the order that the levels appear in `data` or, if the variables are pandas categoricals, the category order.

**hue\_kws**dictionary of param -> list of values mapping

Other keyword arguments to insert into the plotting call to let other plot attributes vary across levels of the hue variable (e.g. the markers in a scatterplot).

**legend\_out**bool

If `True`, the figure size will be extended, and the legend will be drawn outside the plot on the center right.

**despine**boolean

Remove the top and right spines from the plots.

**margin\_titles**bool

If `True`, the titles for the row variable are drawn to the right of the last column. This option is experimental and may not work in all cases.

**{x, y}lim: tuples**

Limits for each of the axes on each facet (only relevant when share{x, y} is True).

**subplot\_kws**dict

Dictionary of keyword arguments passed to matplotlib subplot(s) methods.

**gridspec\_kws**dict

Dictionary of keyword arguments passed to [`matplotlib.gridspec.GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "(in Matplotlib v3.8.2)")
 (via [`matplotlib.figure.Figure.subplots()`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.subplots "(in Matplotlib v3.8.2)")
). Ignored if `col_wrap` is not `None`.

See also

[`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")

Subplot grid for plotting pairwise relationships

[`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")

Combine a relational plot and a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

[`displot`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")

Combine a distribution plot and a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")

Combine a categorical plot and a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

[`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot")

Combine a regression plot and a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

Examples

Note

These examples use seaborn functions to demonstrate some of the advanced features of the class, but in most cases you will want to use figue-level functions (e.g. [`displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")
, [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")
) to make the plots shown here.

Calling the constructor requires a long-form data object. This initializes the grid, but doesn’t plot anything on it:

tips \= sns.load\_dataset("tips")
sns.FacetGrid(tips)

Copy to clipboard

![../_images/FacetGrid_1_0.png](https://seaborn.pydata.org/_images/FacetGrid_1_0.png)

Assign column and/or row variables to add more subplots to the figure:

sns.FacetGrid(tips, col\="time", row\="sex")

Copy to clipboard

![../_images/FacetGrid_3_0.png](https://seaborn.pydata.org/_images/FacetGrid_3_0.png)

To draw a plot on every facet, pass a function and the name of one or more columns in the dataframe to [`FacetGrid.map()`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn.FacetGrid.map "seaborn.FacetGrid.map")
:

g \= sns.FacetGrid(tips, col\="time",  row\="sex")
g.map(sns.scatterplot, "total\_bill", "tip")

Copy to clipboard

![../_images/FacetGrid_5_0.png](https://seaborn.pydata.org/_images/FacetGrid_5_0.png)

The variable specification in [`FacetGrid.map()`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn.FacetGrid.map "seaborn.FacetGrid.map")
 requires a positional argument mapping, but if the function has a `data` parameter and accepts named variable assignments, you can also use [`FacetGrid.map_dataframe()`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html#seaborn.FacetGrid.map_dataframe "seaborn.FacetGrid.map_dataframe")
:

g \= sns.FacetGrid(tips, col\="time",  row\="sex")
g.map\_dataframe(sns.histplot, x\="total\_bill")

Copy to clipboard

![../_images/FacetGrid_7_0.png](https://seaborn.pydata.org/_images/FacetGrid_7_0.png)

Notice how the bins have different widths in each facet. A separate plot is drawn on each facet, so if the plotting function derives any parameters from the data, they may not be shared across facets. You can pass additional keyword arguments to synchronize them. But when possible, using a figure-level function like [`displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")
 will take care of this bookkeeping for you:

g \= sns.FacetGrid(tips, col\="time", row\="sex")
g.map\_dataframe(sns.histplot, x\="total\_bill", binwidth\=2, binrange\=(0, 60))

Copy to clipboard

![../_images/FacetGrid_9_0.png](https://seaborn.pydata.org/_images/FacetGrid_9_0.png)

The [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 constructor accepts a `hue` parameter. Setting this will condition the data on another variable and make multiple plots in different colors. Where possible, label information is tracked so that a single legend can be drawn:

g \= sns.FacetGrid(tips, col\="time", hue\="sex")
g.map\_dataframe(sns.scatterplot, x\="total\_bill", y\="tip")
g.add\_legend()

Copy to clipboard

![../_images/FacetGrid_11_0.png](https://seaborn.pydata.org/_images/FacetGrid_11_0.png)

When `hue` is set on the [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
, however, a separate plot is drawn for each level of the variable. If the plotting function understands `hue`, it is better to let it handle that logic. But it is important to ensure that each facet will use the same hue mapping. In the sample `tips` data, the `sex` column has a categorical datatype, which ensures this. Otherwise, you may want to use the `hue_order` or similar parameter:

g \= sns.FacetGrid(tips, col\="time")
g.map\_dataframe(sns.scatterplot, x\="total\_bill", y\="tip", hue\="sex")
g.add\_legend()

Copy to clipboard

![../_images/FacetGrid_13_0.png](https://seaborn.pydata.org/_images/FacetGrid_13_0.png)

The size and shape of the plot is specified at the level of each subplot using the `height` and `aspect` parameters:

g \= sns.FacetGrid(tips, col\="day", height\=3.5, aspect\=.65)
g.map(sns.histplot, "total\_bill")

Copy to clipboard

![../_images/FacetGrid_15_0.png](https://seaborn.pydata.org/_images/FacetGrid_15_0.png)

If the variable assigned to `col` has many levels, it is possible to “wrap” it so that it spans multiple rows:

g \= sns.FacetGrid(tips, col\="size", height\=2.5, col\_wrap\=3)
g.map(sns.histplot, "total\_bill")

Copy to clipboard

![../_images/FacetGrid_17_0.png](https://seaborn.pydata.org/_images/FacetGrid_17_0.png)

To add horizontal or vertical reference lines on every facet, use [`FacetGrid.refline()`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.refline.html#seaborn.FacetGrid.refline "seaborn.FacetGrid.refline")
:

g \= sns.FacetGrid(tips, col\="time", margin\_titles\=True)
g.map\_dataframe(sns.scatterplot, x\="total\_bill", y\="tip")
g.refline(y\=tips\["tip"\].median())

Copy to clipboard

![../_images/FacetGrid_19_0.png](https://seaborn.pydata.org/_images/FacetGrid_19_0.png)

You can pass custom functions to plot with, or to annotate each facet. Your custom function must use the matplotlib state-machine interface to plot on the “current” axes, and it should catch additional keyword arguments:

import matplotlib.pyplot as plt
def annotate(data, \*\*kws):
    n \= len(data)
    ax \= plt.gca()
    ax.text(.1, .6, f"N = {n}", transform\=ax.transAxes)

g \= sns.FacetGrid(tips, col\="time")
g.map\_dataframe(sns.scatterplot, x\="total\_bill", y\="tip")
g.map\_dataframe(annotate)

Copy to clipboard

![../_images/FacetGrid_21_0.png](https://seaborn.pydata.org/_images/FacetGrid_21_0.png)

The [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 object has some other useful parameters and methods for tweaking the plot:

g \= sns.FacetGrid(tips, col\="sex", row\="time", margin\_titles\=True)
g.map\_dataframe(sns.scatterplot, x\="total\_bill", y\="tip")
g.set\_axis\_labels("Total bill ($)", "Tip ($)")
g.set\_titles(col\_template\="{col\_name} patrons", row\_template\="{row\_name}")
g.set(xlim\=(0, 60), ylim\=(0, 12), xticks\=\[10, 30, 50\], yticks\=\[2, 6, 10\])
g.tight\_layout()
g.savefig("facet\_plot.png")

Copy to clipboard

![../_images/FacetGrid_23_0.png](https://seaborn.pydata.org/_images/FacetGrid_23_0.png)

You also have access to the underlying matplotlib objects for additional tweaking:

g \= sns.FacetGrid(tips, col\="sex", row\="time", margin\_titles\=True, despine\=False)
g.map\_dataframe(sns.scatterplot, x\="total\_bill", y\="tip")
g.figure.subplots\_adjust(wspace\=0, hspace\=0)
for (row\_val, col\_val), ax in g.axes\_dict.items():
    if row\_val \== "Lunch" and col\_val \== "Female":
        ax.set\_facecolor(".95")
    else:
        ax.set\_facecolor((0, 0, 0, 0))

Copy to clipboard

![../_images/FacetGrid_25_0.png](https://seaborn.pydata.org/_images/FacetGrid_25_0.png)
 

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

seaborn.relplot[#](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn-relplot "Permalink to this heading")

==========================================================================================================================

seaborn.relplot(_data\=None_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _size\=None_, _style\=None_, _units\=None_, _weights\=None_, _row\=None_, _col\=None_, _col\_wrap\=None_, _row\_order\=None_, _col\_order\=None_, _palette\=None_, _hue\_order\=None_, _hue\_norm\=None_, _sizes\=None_, _size\_order\=None_, _size\_norm\=None_, _markers\=None_, _dashes\=None_, _style\_order\=None_, _legend\='auto'_, _kind\='scatter'_, _height\=5_, _aspect\=1_, _facet\_kws\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "Permalink to this definition")

Figure-level interface for drawing relational plots onto a FacetGrid.

This function provides access to several different axes-level functions that show the relationship between two variables with semantic mappings of subsets. The `kind` parameter selects the underlying axes-level function to use:

*   [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")
     (with `kind="scatter"`; the default)
    
*   [`lineplot()`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")
     (with `kind="line"`)
    

Extra keyword arguments are passed to the underlying function, so you should refer to the documentation for each to see kind-specific options.

The relationship between `x` and `y` can be shown for different subsets of the data using the `hue`, `size`, and `style` parameters. These parameters control what visual semantics are used to identify the different subsets. It is possible to show up to three dimensions independently by using all three semantic types, but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e. both `hue` and `style` for the same variable) can be helpful for making graphics more accessible.

See the [tutorial](https://seaborn.pydata.org/tutorial/relational.html#relational-tutorial)
 for more information.

The default treatment of the `hue` (and to a lesser extent, `size`) semantic, if present, depends on whether the variable is inferred to represent “numeric” or “categorical” data. In particular, numeric variables are represented with a sequential colormap by default, and the legend entries show regular “ticks” with values that may or may not exist in the data. This behavior can be controlled through various parameters, as described and illustrated below.

After plotting, the [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 with the plot is returned and can be used directly to tweak supporting plot details or add other layers.

Parameters:

**data**[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)")
, [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v1.26)")
, mapping, or sequence

Input data structure. Either a long-form collection of vectors that can be assigned to named variables or a wide-form dataset that will be internally reshaped.

**x, y**vectors or keys in `data`

Variables that specify positions on the x and y axes.

**hue**vector or key in `data`

Grouping variable that will produce elements with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.

**size**vector or key in `data`

Grouping variable that will produce elements with different sizes. Can be either categorical or numeric, although size mapping will behave differently in latter case.

**style**vector or key in `data`

Grouping variable that will produce elements with different styles. Can have a numeric dtype but will always be treated as categorical.

**units**vector or key in `data`

Grouping variable identifying sampling units. When used, a separate line will be drawn for each unit with appropriate semantics, but no legend entry will be added. Useful for showing distribution of experimental replicates when exact identities are not needed.

**weights**vector or key in `data`

Data values or column used to compute weighted estimation. Note that use of weights currently limits the choice of statistics to a ‘mean’ estimator and ‘ci’ errorbar.

**row, col**vectors or keys in `data`

Variables that define subsets to plot on different facets.

**col\_wrap**int

“Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a `row` facet.

**row\_order, col\_order**lists of strings

Order to organize the rows and/or columns of the grid in, otherwise the orders are inferred from the data objects.

**palette**string, list, dict, or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.8.2)")

Method for choosing the colors to use when mapping the `hue` semantic. String values are passed to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
. List or dict values imply categorical mapping, while a colormap object implies numeric mapping.

**hue\_order**vector of strings

Specify the order of processing and plotting for categorical levels of the `hue` semantic.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")

Either a pair of values that set the normalization range in data units or an object that will map from data units into a \[0, 1\] interval. Usage implies numeric mapping.

**sizes**list, dict, or tuple

An object that determines how sizes are chosen when `size` is used. List or dict arguments should provide a size for each unique data value, which forces a categorical interpretation. The argument may also be a min, max tuple.

**size\_order**list

Specified order for appearance of the `size` variable levels, otherwise they are determined from the data. Not relevant when the `size` variable is numeric.

**size\_norm**tuple or Normalize object

Normalization in data units for scaling plot objects when the `size` variable is numeric.

**style\_order**list

Specified order for appearance of the `style` variable levels otherwise they are determined from the data. Not relevant when the `style` variable is numeric.

**dashes**boolean, list, or dictionary

Object determining how to draw the lines for different levels of the `style` variable. Setting to `True` will use default dash codes, or you can pass a list of dash codes or a dictionary mapping levels of the `style` variable to dash codes. Setting to `False` will use solid lines for all subsets. Dashes are specified as in matplotlib: a tuple of `(segment, gap)` lengths, or an empty string to draw a solid line.

**markers**boolean, list, or dictionary

Object determining how to draw the markers for different levels of the `style` variable. Setting to `True` will use default markers, or you can pass a list of markers or a dictionary mapping levels of the `style` variable to markers. Setting to `False` will draw marker-less lines. Markers are specified as in matplotlib.

**legend**“auto”, “brief”, “full”, or False

How to draw the legend. If “brief”, numeric `hue` and `size` variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If “auto”, choose between brief or full representation based on number of levels. If `False`, no legend data is added and no legend is drawn.

**kind**string

Kind of plot to draw, corresponding to a seaborn relational plot. Options are `"scatter"` or `"line"`.

**height**scalar

Height (in inches) of each facet. See also: `aspect`.

**aspect**scalar

Aspect ratio of each facet, so that `aspect * height` gives the width of each facet in inches.

**facet\_kws**dict

Dictionary of other keyword arguments to pass to [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

**kwargs**key, value pairings

Other keyword arguments are passed through to the underlying plotting function.

Returns:

[`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

An object managing one or more subplots that correspond to conditional data subsets with convenient methods for batch-setting of axes attributes.

Examples

These examples will illustrate only some of the functionality that [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")
 is capable of. For more information, consult the examples for [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")
 and [`lineplot()`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")
, which are used when `kind="scatter"` or `kind="line"`, respectively.

To illustrate `kind="scatter"` (the default style of plot), we will use the “tips” dataset:

tips \= sns.load\_dataset("tips")
tips.head()

Copy to clipboard

|     | total\_bill | tip | sex | smoker | day | time | size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 16.99 | 1.01 | Female | No  | Sun | Dinner | 2   |
| 1   | 10.34 | 1.66 | Male | No  | Sun | Dinner | 3   |
| 2   | 21.01 | 3.50 | Male | No  | Sun | Dinner | 3   |
| 3   | 23.68 | 3.31 | Male | No  | Sun | Dinner | 2   |
| 4   | 24.59 | 3.61 | Female | No  | Sun | Dinner | 4   |

Assigning `x` and `y` and any semantic mapping variables will draw a single plot:

sns.relplot(data\=tips, x\="total\_bill", y\="tip", hue\="day")

Copy to clipboard

![../_images/relplot_4_0.png](https://seaborn.pydata.org/_images/relplot_4_0.png)

Assigning a `col` variable creates a faceted figure with multiple subplots arranged across the columns of the grid:

sns.relplot(data\=tips, x\="total\_bill", y\="tip", hue\="day", col\="time")

Copy to clipboard

![../_images/relplot_6_0.png](https://seaborn.pydata.org/_images/relplot_6_0.png)

Different variables can be assigned to facet on both the columns and rows:

sns.relplot(data\=tips, x\="total\_bill", y\="tip", hue\="day", col\="time", row\="sex")

Copy to clipboard

![../_images/relplot_8_0.png](https://seaborn.pydata.org/_images/relplot_8_0.png)

When the variable assigned to `col` has many levels, it can be “wrapped” across multiple rows:

sns.relplot(data\=tips, x\="total\_bill", y\="tip", hue\="time", col\="day", col\_wrap\=2)

Copy to clipboard

![../_images/relplot_10_0.png](https://seaborn.pydata.org/_images/relplot_10_0.png)

Assigning multiple semantic variables can show multi-dimensional relationships, but be mindful to avoid making an overly-complicated plot.

sns.relplot(
    data\=tips, x\="total\_bill", y\="tip", col\="time",
    hue\="time", size\="size", style\="sex",
    palette\=\["b", "r"\], sizes\=(10, 100)
)

Copy to clipboard

![../_images/relplot_12_0.png](https://seaborn.pydata.org/_images/relplot_12_0.png)

When there is a natural continuity to one of the variables, it makes more sense to show lines instead of points. To draw the figure using [`lineplot()`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")
, set `kind="line"`. We will illustrate this effect with the “fmri dataset:

fmri \= sns.load\_dataset("fmri")
fmri.head()

Copy to clipboard

|     | subject | timepoint | event | region | signal |
| --- | --- | --- | --- | --- | --- |
| 0   | s13 | 18  | stim | parietal | \-0.017552 |
| 1   | s5  | 14  | stim | parietal | \-0.080883 |
| 2   | s12 | 18  | stim | parietal | \-0.081033 |
| 3   | s11 | 18  | stim | parietal | \-0.046134 |
| 4   | s10 | 18  | stim | parietal | \-0.037970 |

Using `kind="line"` offers the same flexibility for semantic mappings as `kind="scatter"`, but [`lineplot()`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")
 transforms the data more before plotting. Observations are sorted by their `x` value, and repeated observations are aggregated. By default, the resulting plot shows the mean and 95% CI for each unit

sns.relplot(
    data\=fmri, x\="timepoint", y\="signal", col\="region",
    hue\="event", style\="event", kind\="line",
)

Copy to clipboard

![../_images/relplot_16_0.png](https://seaborn.pydata.org/_images/relplot_16_0.png)

The size and shape of the figure is parametrized by the `height` and `aspect` ratio of each individual facet:

sns.relplot(
    data\=fmri,
    x\="timepoint", y\="signal",
    hue\="event", style\="event", col\="region",
    height\=4, aspect\=.7, kind\="line"
)

Copy to clipboard

![../_images/relplot_18_0.png](https://seaborn.pydata.org/_images/relplot_18_0.png)

The object returned by [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")
 is always a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
, which has several methods that allow you to quickly tweak the title, labels, and other aspects of the plot:

g \= sns.relplot(
    data\=fmri,
    x\="timepoint", y\="signal",
    hue\="event", style\="event", col\="region",
    height\=4, aspect\=.7, kind\="line"
)
(g.map(plt.axhline, y\=0, color\=".7", dashes\=(2, 1), zorder\=0)
  .set\_axis\_labels("Timepoint", "Percent signal change")
  .set\_titles("Region: {col\_name} cortex")
  .tight\_layout(w\_pad\=0))

Copy to clipboard

![../_images/relplot_20_0.png](https://seaborn.pydata.org/_images/relplot_20_0.png)

It is also possible to use wide-form data with [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")
:

flights\_wide \= (
    sns.load\_dataset("flights")
    .pivot(index\="year", columns\="month", values\="passengers")
)

Copy to clipboard

Faceting is not an option in this case, but the plot will still take advantage of the external legend offered by [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
:

sns.relplot(data\=flights\_wide, kind\="line")

Copy to clipboard

![../_images/relplot_24_0.png](https://seaborn.pydata.org/_images/relplot_24_0.png)
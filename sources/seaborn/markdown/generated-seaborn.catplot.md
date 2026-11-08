 

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

seaborn.catplot[#](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn-catplot "Permalink to this heading")

==========================================================================================================================

seaborn.catplot(_data=None_, _\*_, _x=None_, _y=None_, _hue=None_, _row=None_, _col=None_, _kind='strip'_, _estimator='mean'_, _errorbar=('ci'_, _95)_, _n\_boot=1000_, _seed=None_, _units=None_, _weights=None_, _order=None_, _hue\_order=None_, _row\_order=None_, _col\_order=None_, _col\_wrap=None_, _height=5_, _aspect=1_, _log\_scale=None_, _native\_scale=False_, _formatter=None_, _orient=None_, _color=None_, _palette=None_, _hue\_norm=None_, _legend='auto'_, _legend\_out=True_, _sharex=True_, _sharey=True_, _margin\_titles=False_, _facet\_kws=None_, _ci=<deprecated>_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "Permalink to this definition")

Figure-level interface for drawing categorical plots onto a FacetGrid.

This function provides access to several axes-level functions that show the relationship between a numerical and one or more categorical variables using one of several visual representations. The `kind` parameter selects the underlying axes-level function to use.

Categorical scatterplots:

*   [`stripplot()`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")
     (with `kind="strip"`; the default)
    
*   [`swarmplot()`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot "seaborn.swarmplot")
     (with `kind="swarm"`)
    

Categorical distribution plots:

*   [`boxplot()`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")
     (with `kind="box"`)
    
*   [`violinplot()`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "seaborn.violinplot")
     (with `kind="violin"`)
    
*   [`boxenplot()`](https://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn.boxenplot "seaborn.boxenplot")
     (with `kind="boxen"`)
    

Categorical estimate plots:

*   [`pointplot()`](https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot "seaborn.pointplot")
     (with `kind="point"`)
    
*   [`barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")
     (with `kind="bar"`)
    
*   [`countplot()`](https://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot "seaborn.countplot")
     (with `kind="count"`)
    

Extra keyword arguments are passed to the underlying function, so you should refer to the documentation for each to see kind-specific options.

See the [tutorial](https://seaborn.pydata.org/tutorial/categorical.html#categorical-tutorial)
 for more information.

Note

By default, this function treats one of the variables as categorical and draws data at ordinal positions (0, 1, … n) on the relevant axis. As of version 0.13.0, this can be disabled by setting `native_scale=True`.

After plotting, the [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 with the plot is returned and can be used directly to tweak supporting plot details or add other layers.

Parameters:

**data**DataFrame, Series, dict, array, or list of arrays

Dataset for plotting. If `x` and `y` are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.

**x, y, hue**names of variables in `data` or vector data

Inputs for plotting long-form data. See examples for interpretation.

**row, col**names of variables in `data` or vector data

Categorical variables that will determine the faceting of the grid.

**kind**str

The kind of plot to draw, corresponds to the name of a categorical axes-level plotting function. Options are: “strip”, “swarm”, “box”, “violin”, “boxen”, “point”, “bar”, or “count”.

**estimator**string or callable that maps vector -> scalar

Statistical function to estimate within each categorical bin.

**errorbar**string, (string, number) tuple, callable or None

Name of errorbar method (either “ci”, “pi”, “se”, or “sd”), or a tuple with a method name and a level parameter, or a function that maps from a vector to a (min, max) interval, or None to hide errorbar. See the [errorbar tutorial](https://seaborn.pydata.org/tutorial/error_bars.html)
 for more information.

New in version v0.12.0.

**n\_boot**int

Number of bootstrap samples used to compute confidence intervals.

**seed**int, `numpy.random.Generator`, or `numpy.random.RandomState`

Seed or random number generator for reproducible bootstrapping.

**units**name of variable in `data` or vector data

Identifier of sampling units; used by the errorbar function to perform a multilevel bootstrap and account for repeated measures

**weights**name of variable in `data` or vector data

Data values or column used to compute weighted statistics. Note that the use of weights may limit other statistical options.

New in version v0.13.1.

**order, hue\_order**lists of strings

Order to plot the categorical levels in; otherwise the levels are inferred from the data objects.

**row\_order, col\_order**lists of strings

Order to organize the rows and/or columns of the grid in; otherwise the orders are inferred from the data objects.

**col\_wrap**int

“Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a `row` facet.

**height**scalar

Height (in inches) of each facet. See also: `aspect`.

**aspect**scalar

Aspect ratio of each facet, so that `aspect * height` gives the width of each facet in inches.

**native\_scale**bool

When True, numeric or datetime values on the categorical axis will maintain their original scaling rather than being converted to fixed indices.

New in version v0.13.0.

**formatter**callable

Function for converting categorical data into strings. Affects both grouping and tick labels.

New in version v0.13.0.

**orient**“v” | “h” | “x” | “y”

Orientation of the plot (vertical or horizontal). This is usually inferred based on the type of the input variables, but it can be used to resolve ambiguity when both `x` and `y` are numeric or when plotting wide-form data.

Changed in version v0.13.0: Added ‘x’/’y’ as options, equivalent to ‘v’/’h’.

**color**matplotlib color

Single color for the elements in the plot.

**palette**palette name, list, or dict

Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
, or a dictionary mapping hue levels to matplotlib colors.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")
 object

Normalization in data units for colormap applied to the `hue` variable when it is numeric. Not relevant if `hue` is categorical.

New in version v0.12.0.

**legend**“auto”, “brief”, “full”, or False

How to draw the legend. If “brief”, numeric `hue` and `size` variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If “auto”, choose between brief or full representation based on number of levels. If `False`, no legend data is added and no legend is drawn.

New in version v0.13.0.

**legend\_out**bool

If `True`, the figure size will be extended, and the legend will be drawn outside the plot on the center right.

**share{x,y}**bool, ‘col’, or ‘row’ optional

If true, the facets will share y axes across columns and/or x axes across rows.

**margin\_titles**bool

If `True`, the titles for the row variable are drawn to the right of the last column. This option is experimental and may not work in all cases.

**facet\_kws**dict

Dictionary of other keyword arguments to pass to [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

**kwargs**key, value pairings

Other keyword arguments are passed through to the underlying plotting function.

Returns:

[`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

Returns the [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 object with the plot on it for further tweaking.

Examples

By default, the visual representation will be a jittered strip plot:

df \= sns.load\_dataset("titanic")
sns.catplot(data\=df, x\="age", y\="class")

Copy to clipboard

![../_images/catplot_1_0.png](https://seaborn.pydata.org/_images/catplot_1_0.png)

Use `kind` to select a different representation:

sns.catplot(data\=df, x\="age", y\="class", kind\="box")

Copy to clipboard

![../_images/catplot_3_0.png](https://seaborn.pydata.org/_images/catplot_3_0.png)

One advantage is that the legend will be automatically placed outside the plot:

sns.catplot(data\=df, x\="age", y\="class", hue\="sex", kind\="boxen")

Copy to clipboard

![../_images/catplot_5_0.png](https://seaborn.pydata.org/_images/catplot_5_0.png)

Additional keyword arguments get passed through to the underlying seaborn function:

sns.catplot(
    data\=df, x\="age", y\="class", hue\="sex",
    kind\="violin", bw\_adjust\=.5, cut\=0, split\=True,
)

Copy to clipboard

![../_images/catplot_7_0.png](https://seaborn.pydata.org/_images/catplot_7_0.png)

Assigning a variable to `col` or `row` will automatically create subplots. Control figure size with the `height` and `aspect` parameters:

sns.catplot(
    data\=df, x\="class", y\="survived", col\="sex",
    kind\="bar", height\=4, aspect\=.6,
)

Copy to clipboard

![../_images/catplot_9_0.png](https://seaborn.pydata.org/_images/catplot_9_0.png)

For single-subplot figures, it is easy to layer different representations:

sns.catplot(data\=df, x\="age", y\="class", kind\="violin", color\=".9", inner\=None)
sns.swarmplot(data\=df, x\="age", y\="class", size\=3)

Copy to clipboard

![../_images/catplot_11_0.png](https://seaborn.pydata.org/_images/catplot_11_0.png)

Use methods on the returned [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 to tweak the presentation:

g \= sns.catplot(
    data\=df, x\="who", y\="survived", col\="class",
    kind\="bar", height\=4, aspect\=.6,
)
g.set\_axis\_labels("", "Survival Rate")
g.set\_xticklabels(\["Men", "Women", "Children"\])
g.set\_titles("{col\_name} {col\_var}")
g.set(ylim\=(0, 1))
g.despine(left\=True)

Copy to clipboard

![../_images/catplot_13_0.png](https://seaborn.pydata.org/_images/catplot_13_0.png)
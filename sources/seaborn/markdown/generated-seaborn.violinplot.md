 

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

seaborn.violinplot[#](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn-violinplot "Permalink to this heading")

===================================================================================================================================

seaborn.violinplot(_data=None_, _\*_, _x=None_, _y=None_, _hue=None_, _order=None_, _hue\_order=None_, _orient=None_, _color=None_, _palette=None_, _saturation=0.75_, _fill=True_, _inner='box'_, _split=False_, _width=0.8_, _dodge='auto'_, _gap=0_, _linewidth=None_, _linecolor='auto'_, _cut=2_, _gridsize=100_, _bw\_method='scott'_, _bw\_adjust=1_, _density\_norm='area'_, _common\_norm=False_, _hue\_norm=None_, _formatter=None_, _log\_scale=None_, _native\_scale=False_, _legend='auto'_, _scale=<deprecated>_, _scale\_hue=<deprecated>_, _bw=<deprecated>_, _inner\_kws=None_, _ax=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "Permalink to this definition")

Draw a patch representing a KDE and add observations or box plot statistics.

A violin plot plays a similar role as a box-and-whisker plot. It shows the distribution of data points after grouping by one (or more) variables. Unlike a box plot, each violin is drawn using a kernel density estimate of the underlying distribution.

See the [tutorial](https://seaborn.pydata.org/tutorial/categorical.html#categorical-tutorial)
 for more information.

Note

By default, this function treats one of the variables as categorical and draws data at ordinal positions (0, 1, … n) on the relevant axis. As of version 0.13.0, this can be disabled by setting `native_scale=True`.

Parameters:

**data**DataFrame, Series, dict, array, or list of arrays

Dataset for plotting. If `x` and `y` are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.

**x, y, hue**names of variables in `data` or vector data

Inputs for plotting long-form data. See examples for interpretation.

**order, hue\_order**lists of strings

Order to plot the categorical levels in; otherwise the levels are inferred from the data objects.

**orient**“v” | “h” | “x” | “y”

Orientation of the plot (vertical or horizontal). This is usually inferred based on the type of the input variables, but it can be used to resolve ambiguity when both `x` and `y` are numeric or when plotting wide-form data.

Changed in version v0.13.0: Added ‘x’/’y’ as options, equivalent to ‘v’/’h’.

**color**matplotlib color

Single color for the elements in the plot.

**palette**palette name, list, or dict

Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
, or a dictionary mapping hue levels to matplotlib colors.

**saturation**float

Proportion of the original saturation to draw fill colors in. Large patches often look better with desaturated colors, but set this to `1` if you want the colors to perfectly match the input values.

**fill**bool

If True, use a solid patch. Otherwise, draw as line art.

New in version v0.13.0.

**inner**{“box”, “quart”, “point”, “stick”, None}

Representation of the data in the violin interior. One of the following:

*   `"box"`: draw a miniature box-and-whisker plot
    
*   `"quart"`: show the quartiles of the data
    
*   `"point"` or `"stick"`: show each observation
    

**split**bool

Show an un-mirrored distribution, alternating sides when using `hue`.

Changed in version v0.13.0: Previously, this option required a `hue` variable with exactly two levels.

**width**float

Width allotted to each element on the orient axis. When `native_scale=True`, it is relative to the minimum distance between two values in the native scale.

**dodge**“auto” or bool

When hue mapping is used, whether elements should be narrowed and shifted along the orient axis to eliminate overlap. If `"auto"`, set to `True` when the orient variable is crossed with the categorical variable or `False` otherwise.

Changed in version 0.13.0: Added `"auto"` mode as a new default.

**gap**float

Shrink on the orient axis by this factor to add a gap between dodged elements.

New in version 0.13.0.

**linewidth**float

Width of the lines that frame the plot elements.

**linecolor**color

Color to use for line elements, when `fill` is True.

New in version v0.13.0.

**cut**float

Distance, in units of bandwidth, to extend the density past extreme datapoints. Set to 0 to limit the violin within the data range.

**gridsize**int

Number of points in the discrete grid used to evaluate the KDE.

**bw\_method**{“scott”, “silverman”, float}

Either the name of a reference rule or the scale factor to use when computing the kernel bandwidth. The actual kernel size will be determined by multiplying the scale factor by the standard deviation of the data within each group.

New in version v0.13.0.

**bw\_adjust: float**

Factor that scales the bandwidth to use more or less smoothing.

New in version v0.13.0.

**density\_norm**{“area”, “count”, “width”}

Method that normalizes each density to determine the violin’s width. If `area`, each violin will have the same area. If `count`, the width will be proportional to the number of observations. If `width`, each violin will have the same width.

New in version v0.13.0.

**common\_norm**bool

When `True`, normalize the density across all violins.

New in version v0.13.0.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")
 object

Normalization in data units for colormap applied to the `hue` variable when it is numeric. Not relevant if `hue` is categorical.

New in version v0.12.0.

**formatter**callable

Function for converting categorical data into strings. Affects both grouping and tick labels.

New in version v0.13.0.

**log\_scale**bool or number, or pair of bools or numbers

Set axis scale(s) to log. A single value sets the data axis for any numeric axes in the plot. A pair of values sets each axis independently. Numeric values are interpreted as the desired base (default 10). When `None` or `False`, seaborn defers to the existing Axes scale.

New in version v0.13.0.

**native\_scale**bool

When True, numeric or datetime values on the categorical axis will maintain their original scaling rather than being converted to fixed indices.

New in version v0.13.0.

**legend**“auto”, “brief”, “full”, or False

How to draw the legend. If “brief”, numeric `hue` and `size` variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If “auto”, choose between brief or full representation based on number of levels. If `False`, no legend data is added and no legend is drawn.

New in version v0.13.0.

**scale**{“area”, “count”, “width”}

Deprecated since version v0.13.0: See `density_norm`.

**scale\_hue**bool

Deprecated since version v0.13.0: See `common_norm`.

**bw**{‘scott’, ‘silverman’, float}

Deprecated since version v0.13.0: See `bw_method` and `bw_adjust`.

**inner\_kws**dict of key, value mappings

Keyword arguments for the “inner” plot, passed to one of:

*   [`matplotlib.collections.LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "(in Matplotlib v3.8.2)")
     (with `inner="stick"`)
    
*   [`matplotlib.axes.Axes.scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "(in Matplotlib v3.8.2)")
     (with `inner="point"`)
    
*   [`matplotlib.axes.Axes.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "(in Matplotlib v3.8.2)")
     (with `inner="quart"` or `inner="box"`)
    

Additionally, with `inner="box"`, the keywords `box_width`, `whis_width`, and `marker` receive special handling for the components of the “box” plot.

New in version v0.13.0.

**ax**matplotlib Axes

Axes object to draw the plot onto, otherwise uses the current Axes.

**kwargs**key, value mappings

Keyword arguments for the violin patches, passsed through to [`matplotlib.axes.Axes.fill_between()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "(in Matplotlib v3.8.2)")
.

Returns:

**ax**matplotlib Axes

Returns the Axes object with the plot drawn onto it.

See also

[`boxplot`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")

A traditional box-and-whisker plot with a similar API.

[`stripplot`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")

A scatterplot where one variable is categorical. Can be used in conjunction with other plots to show each observation.

[`swarmplot`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot "seaborn.swarmplot")

A categorical scatterplot where the points do not overlap. Can be used with other plots to show each observation.

[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")

Combine a categorical plot with a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

Examples

The default violinplot represents a distribution two ways: a patch showing a symmetric kernel density estimate (KDE), and the quartiles / whiskers of a box plot:

df \= sns.load\_dataset("titanic")
sns.violinplot(x\=df\["age"\])

Copy to clipboard

![../_images/violinplot_1_0.png](https://seaborn.pydata.org/_images/violinplot_1_0.png)

In a bivariate plot, one of the variables will “group” so that multiple violins are drawn:

sns.violinplot(data\=df, x\="age", y\="class")

Copy to clipboard

![../_images/violinplot_3_0.png](https://seaborn.pydata.org/_images/violinplot_3_0.png)

By default, the orientation of the plot is determined by the variable types, preferring to group by a categorical variable:

sns.violinplot(data\=df, x\="class", y\="age", hue\="alive")

Copy to clipboard

![../_images/violinplot_5_0.png](https://seaborn.pydata.org/_images/violinplot_5_0.png)

Pass `fill=False` to draw line-art violins:

sns.violinplot(data\=df, x\="class", y\="age", hue\="alive", fill\=False)

Copy to clipboard

![../_images/violinplot_7_0.png](https://seaborn.pydata.org/_images/violinplot_7_0.png)

Draw “split” violins to take up less space, and only show the data quarties:

sns.violinplot(data\=df, x\="class", y\="age", hue\="alive", split\=True, inner\="quart")

Copy to clipboard

![../_images/violinplot_9_0.png](https://seaborn.pydata.org/_images/violinplot_9_0.png)

Add a small gap between the dodged violins:

sns.violinplot(data\=df, x\="class", y\="age", hue\="alive", split\=True, gap\=.1, inner\="quart")

Copy to clipboard

![../_images/violinplot_11_0.png](https://seaborn.pydata.org/_images/violinplot_11_0.png)

Starting in version 0.13.0, it is possilbe to “split” single violins:

sns.violinplot(data\=df, x\="class", y\="age", split\=True, inner\="quart")

Copy to clipboard

![../_images/violinplot_13_0.png](https://seaborn.pydata.org/_images/violinplot_13_0.png)

Represent every observation inside the distribution by setting `inner="stick"` or `inner="point"`:

sns.violinplot(data\=df, x\="age", y\="deck", inner\="point")

Copy to clipboard

![../_images/violinplot_15_0.png](https://seaborn.pydata.org/_images/violinplot_15_0.png)

Normalize the width of each violin to represent the number of observations:

sns.violinplot(data\=df, x\="age", y\="deck", inner\="point", density\_norm\="count")

Copy to clipboard

![../_images/violinplot_17_0.png](https://seaborn.pydata.org/_images/violinplot_17_0.png)

By default, the KDE will smooth past the extremes of the observed data; set `cut=0` to prevent this:

sns.violinplot(data\=df, x\="age", y\="alive", cut\=0, inner\="stick")

Copy to clipboard

![../_images/violinplot_19_0.png](https://seaborn.pydata.org/_images/violinplot_19_0.png)

The `bw_adjust` parameter controls the amount of smoothing:

sns.violinplot(data\=df, x\="age", y\="alive", bw\_adjust\=.5, inner\="stick")

Copy to clipboard

![../_images/violinplot_21_0.png](https://seaborn.pydata.org/_images/violinplot_21_0.png)

By default, the violins are drawn at fixed positions on a categorical scale, even if the grouping variable is numeric. Starting in version 0.13.0, pass the `native_scale=True` parameter to preserve the original scale on both axes:

sns.violinplot(x\=df\["age"\].round(\-1) + 5, y\=df\["fare"\], native\_scale\=True)

Copy to clipboard

![../_images/violinplot_23_0.png](https://seaborn.pydata.org/_images/violinplot_23_0.png)

When using a categorical scale, the `formatter` parameter accepts a function that defines categories:

decades \= lambda x: f"{int(x)}–{int(x + 10)}"
sns.violinplot(x\=df\["age"\].round(\-1), y\=df\["fare"\], formatter\=decades)

Copy to clipboard

![../_images/violinplot_25_0.png](https://seaborn.pydata.org/_images/violinplot_25_0.png)

By default, the “inner” representation scales with the `linewidth` and `linecolor` parameters:

sns.violinplot(data\=df, x\="age", linewidth\=1, linecolor\="k")

Copy to clipboard

![../_images/violinplot_27_0.png](https://seaborn.pydata.org/_images/violinplot_27_0.png)

Use `inner_kws` to pass parameters directly to the inner plotting functions:

sns.violinplot(data\=df, x\="age", inner\_kws\=dict(box\_width\=15, whis\_width\=2, color\=".8"))

Copy to clipboard

![../_images/violinplot_29_0.png](https://seaborn.pydata.org/_images/violinplot_29_0.png)
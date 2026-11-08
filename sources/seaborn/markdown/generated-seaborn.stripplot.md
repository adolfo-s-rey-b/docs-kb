 

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

seaborn.stripplot[#](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn-stripplot "Permalink to this heading")

================================================================================================================================

seaborn.stripplot(_data=None_, _\*_, _x=None_, _y=None_, _hue=None_, _order=None_, _hue\_order=None_, _jitter=True_, _dodge=False_, _orient=None_, _color=None_, _palette=None_, _size=5_, _edgecolor=<default>_, _linewidth=0_, _hue\_norm=None_, _log\_scale=None_, _native\_scale=False_, _formatter=None_, _legend='auto'_, _ax=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "Permalink to this definition")

Draw a categorical scatterplot using jitter to reduce overplotting.

A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.

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

**jitter**float, `True`/`1` is special-cased

Amount of jitter (only along the categorical axis) to apply. This can be useful when you have many points and they overlap, so that it is easier to see the distribution. You can specify the amount of jitter (half the width of the uniform random variable support), or use `True` for a good default.

**dodge**bool

When a `hue` variable is assigned, setting this to `True` will separate the strips for different hue levels along the categorical axis and narrow the amount of space allotedto each strip. Otherwise, the points for each level will be plotted in the same strip.

**orient**“v” | “h” | “x” | “y”

Orientation of the plot (vertical or horizontal). This is usually inferred based on the type of the input variables, but it can be used to resolve ambiguity when both `x` and `y` are numeric or when plotting wide-form data.

Changed in version v0.13.0: Added ‘x’/’y’ as options, equivalent to ‘v’/’h’.

**color**matplotlib color

Single color for the elements in the plot.

**palette**palette name, list, or dict

Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
, or a dictionary mapping hue levels to matplotlib colors.

**size**float

Radius of the markers, in points.

**edgecolor**matplotlib color, “gray” is special-cased

Color of the lines around each point. If you pass `"gray"`, the brightness is determined by the color palette used for the body of the points. Note that `stripplot` has `linewidth=0` by default, so edge colors are only visible with nonzero line width.

**linewidth**float

Width of the lines that frame the plot elements.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")
 object

Normalization in data units for colormap applied to the `hue` variable when it is numeric. Not relevant if `hue` is categorical.

New in version v0.12.0.

**log\_scale**bool or number, or pair of bools or numbers

Set axis scale(s) to log. A single value sets the data axis for any numeric axes in the plot. A pair of values sets each axis independently. Numeric values are interpreted as the desired base (default 10). When `None` or `False`, seaborn defers to the existing Axes scale.

New in version v0.13.0.

**native\_scale**bool

When True, numeric or datetime values on the categorical axis will maintain their original scaling rather than being converted to fixed indices.

New in version v0.13.0.

**formatter**callable

Function for converting categorical data into strings. Affects both grouping and tick labels.

New in version v0.13.0.

**legend**“auto”, “brief”, “full”, or False

How to draw the legend. If “brief”, numeric `hue` and `size` variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If “auto”, choose between brief or full representation based on number of levels. If `False`, no legend data is added and no legend is drawn.

New in version v0.13.0.

**ax**matplotlib Axes

Axes object to draw the plot onto, otherwise uses the current Axes.

**kwargs**key, value mappings

Other keyword arguments are passed through to [`matplotlib.axes.Axes.scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "(in Matplotlib v3.8.2)")
.

Returns:

**ax**matplotlib Axes

Returns the Axes object with the plot drawn onto it.

See also

[`swarmplot`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot "seaborn.swarmplot")

A categorical scatterplot where the points do not overlap. Can be used with other plots to show each observation.

[`boxplot`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")

A traditional box-and-whisker plot with a similar API.

[`violinplot`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "seaborn.violinplot")

A combination of boxplot and kernel density estimation.

[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")

Combine a categorical plot with a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

Examples

Assigning a single numeric variable shows its univariate distribution with points randomly “jittered” on the other axis:

tips \= sns.load\_dataset("tips")
sns.stripplot(data\=tips, x\="total\_bill")

Copy to clipboard

![../_images/stripplot_1_0.png](https://seaborn.pydata.org/_images/stripplot_1_0.png)

Assigning a second variable splits the strips of points to compare categorical levels of that variable:

sns.stripplot(data\=tips, x\="total\_bill", y\="day")

Copy to clipboard

![../_images/stripplot_3_0.png](https://seaborn.pydata.org/_images/stripplot_3_0.png)

Show vertically-oriented strips by swapping the assignment of the categorical and numerical variables:

sns.stripplot(data\=tips, x\="day", y\="total\_bill")

Copy to clipboard

![../_images/stripplot_5_0.png](https://seaborn.pydata.org/_images/stripplot_5_0.png)

Prior to version 0.12, the levels of the categorical variable had different colors by default. To get the same effect, assign the `hue` variable explicitly:

sns.stripplot(data\=tips, x\="total\_bill", y\="day", hue\="day", legend\=False)

Copy to clipboard

![../_images/stripplot_7_0.png](https://seaborn.pydata.org/_images/stripplot_7_0.png)

Or you can assign a distinct variable to `hue` to show a multidimensional relationship:

sns.stripplot(data\=tips, x\="total\_bill", y\="day", hue\="sex")

Copy to clipboard

![../_images/stripplot_9_0.png](https://seaborn.pydata.org/_images/stripplot_9_0.png)

If the `hue` variable is numeric, it will be mapped with a quantitative palette by default (note that this was not the case prior to version 0.12):

sns.stripplot(data\=tips, x\="total\_bill", y\="day", hue\="size")

Copy to clipboard

![../_images/stripplot_11_0.png](https://seaborn.pydata.org/_images/stripplot_11_0.png)

Use `palette` to control the color mapping, including forcing a categorical mapping by passing the name of a qualitative palette:

sns.stripplot(data\=tips, x\="total\_bill", y\="day", hue\="size", palette\="deep")

Copy to clipboard

![../_images/stripplot_13_0.png](https://seaborn.pydata.org/_images/stripplot_13_0.png)

By default, the different levels of the `hue` variable are intermingled in each strip, but setting `dodge=True` will split them:

sns.stripplot(data\=tips, x\="total\_bill", y\="day", hue\="sex", dodge\=True)

Copy to clipboard

![../_images/stripplot_15_0.png](https://seaborn.pydata.org/_images/stripplot_15_0.png)

The random jitter can be disabled by setting `jitter=False`:

sns.stripplot(data\=tips, x\="total\_bill", y\="day", hue\="sex", dodge\=True, jitter\=False)

Copy to clipboard

![../_images/stripplot_17_0.png](https://seaborn.pydata.org/_images/stripplot_17_0.png)

If plotting in wide-form mode, each numeric column of the dataframe will be mapped to both `x` and `hue`:

sns.stripplot(data\=tips)

Copy to clipboard

![../_images/stripplot_19_0.png](https://seaborn.pydata.org/_images/stripplot_19_0.png)

To change the orientation while in wide-form mode, pass `orient` explicitly:

sns.stripplot(data\=tips, orient\="h")

Copy to clipboard

![../_images/stripplot_21_0.png](https://seaborn.pydata.org/_images/stripplot_21_0.png)

The `orient` parameter is also useful when both axis variables are numeric, as it will resolve ambiguity about which dimension to group (and jitter) along:

sns.stripplot(data\=tips, x\="total\_bill", y\="size", orient\="h")

Copy to clipboard

![../_images/stripplot_23_0.png](https://seaborn.pydata.org/_images/stripplot_23_0.png)

By default, the categorical variable will be mapped to discrete indices with a fixed scale (0, 1, …), even when it is numeric:

sns.stripplot(
    data\=tips.query("size in \[2, 3, 5\]"),
    x\="total\_bill", y\="size", orient\="h",
)

Copy to clipboard

![../_images/stripplot_25_0.png](https://seaborn.pydata.org/_images/stripplot_25_0.png)

To disable this behavior and use the original scale of the variable, set `native_scale=True`:

sns.stripplot(
    data\=tips.query("size in \[2, 3, 5\]"),
    x\="total\_bill", y\="size", orient\="h",
    native\_scale\=True,
)

Copy to clipboard

![../_images/stripplot_27_0.png](https://seaborn.pydata.org/_images/stripplot_27_0.png)

Further visual customization can be achieved by passing keyword arguments for `matplotlib.axes.Axes.scatter()`:

sns.stripplot(
    data\=tips, x\="total\_bill", y\="day", hue\="time",
    jitter\=False, s\=20, marker\="D", linewidth\=1, alpha\=.1,
)

Copy to clipboard

![../_images/stripplot_29_0.png](https://seaborn.pydata.org/_images/stripplot_29_0.png)

To make a plot with multiple facets, it is safer to use [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")
 than to work with [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 directly, because [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")
 will ensure that the categorical and hue variables are properly synchronized in each facet:

sns.catplot(data\=tips, x\="time", y\="total\_bill", hue\="sex", col\="day", aspect\=.5)

Copy to clipboard

![../_images/stripplot_31_0.png](https://seaborn.pydata.org/_images/stripplot_31_0.png)
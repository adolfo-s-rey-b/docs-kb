 

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

seaborn.pointplot[#](https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn-pointplot "Permalink to this heading")

================================================================================================================================

seaborn.pointplot(_data=None_, _\*_, _x=None_, _y=None_, _hue=None_, _order=None_, _hue\_order=None_, _estimator='mean'_, _errorbar=('ci'_, _95)_, _n\_boot=1000_, _seed=None_, _units=None_, _weights=None_, _color=None_, _palette=None_, _hue\_norm=None_, _markers=<default>_, _linestyles=<default>_, _dodge=False_, _log\_scale=None_, _native\_scale=False_, _orient=None_, _capsize=0_, _formatter=None_, _legend='auto'_, _err\_kws=None_, _ci=<deprecated>_, _errwidth=<deprecated>_, _join=<deprecated>_, _scale=<deprecated>_, _ax=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot "Permalink to this definition")

Show point estimates and errors using lines with markers.

A point plot represents an estimate of central tendency for a numeric variable by the position of the dot and provides some indication of the uncertainty around that estimate using error bars.

Point plots can be more useful than bar plots for focusing comparisons between different levels of one or more categorical variables. They are particularly adept at showing interactions: how the relationship between levels of one categorical variable changes across levels of a second categorical variable. The lines that join each point from the same `hue` level allow interactions to be judged by differences in slope, which is easier for the eyes than comparing the heights of several groups of points or bars.

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

**color**matplotlib color

Single color for the elements in the plot.

**palette**palette name, list, or dict

Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
, or a dictionary mapping hue levels to matplotlib colors.

**markers**string or list of strings

Markers to use for each of the `hue` levels.

**linestyles**string or list of strings

Line styles to use for each of the `hue` levels.

**dodge**bool or float

Amount to separate the points for each level of the `hue` variable along the categorical axis. Setting to `True` will apply a small default.

**log\_scale**bool or number, or pair of bools or numbers

Set axis scale(s) to log. A single value sets the data axis for any numeric axes in the plot. A pair of values sets each axis independently. Numeric values are interpreted as the desired base (default 10). When `None` or `False`, seaborn defers to the existing Axes scale.

New in version v0.13.0.

**native\_scale**bool

When True, numeric or datetime values on the categorical axis will maintain their original scaling rather than being converted to fixed indices.

New in version v0.13.0.

**orient**“v” | “h” | “x” | “y”

Orientation of the plot (vertical or horizontal). This is usually inferred based on the type of the input variables, but it can be used to resolve ambiguity when both `x` and `y` are numeric or when plotting wide-form data.

Changed in version v0.13.0: Added ‘x’/’y’ as options, equivalent to ‘v’/’h’.

**capsize**float

Width of the “caps” on error bars, relative to bar spacing.

**formatter**callable

Function for converting categorical data into strings. Affects both grouping and tick labels.

New in version v0.13.0.

**legend**“auto”, “brief”, “full”, or False

How to draw the legend. If “brief”, numeric `hue` and `size` variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If “auto”, choose between brief or full representation based on number of levels. If `False`, no legend data is added and no legend is drawn.

New in version v0.13.0.

**err\_kws**dict

Parameters of [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "(in Matplotlib v3.8.2)")
, for the error bar artists.

New in version v0.13.0.

**ci**float

Level of the confidence interval to show, in \[0, 100\].

Deprecated since version v0.12.0: Use `errorbar=("ci", ...)`.

**errwidth**float

Thickness of error bar lines (and caps), in points.

Deprecated since version 0.13.0: Use `err_kws={'linewidth': ...}`.

**join**bool

If `True`, connect point estimates with a line.

Deprecated since version v0.13.0: Set `linestyle="none"` to remove the lines between the points.

**scale**float

Scale factor for the plot elements.

Deprecated since version v0.13.0: Control element sizes with [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "(in Matplotlib v3.8.2)")
 parameters.

**ax**matplotlib Axes

Axes object to draw the plot onto, otherwise uses the current Axes.

**kwargs**key, value mappings

Other parameters are passed through to [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "(in Matplotlib v3.8.2)")
.

New in version v0.13.0.

Returns:

**ax**matplotlib Axes

Returns the Axes object with the plot drawn onto it.

See also

[`barplot`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")

Show point estimates and confidence intervals using bars.

[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")

Combine a categorical plot with a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

Notes

It is important to keep in mind that a point plot shows only the mean (or other estimator) value, but in many cases it may be more informative to show the distribution of values at each level of the categorical variables. In that case, other approaches such as a box or violin plot may be more appropriate.

Examples

Group by a categorical variable and plot aggregated values, with confidence intervals:

sns.pointplot(data\=penguins, x\="island", y\="body\_mass\_g")

Copy to clipboard

![../_images/pointplot_1_0.png](https://seaborn.pydata.org/_images/pointplot_1_0.png)

Add a second layer of grouping and differentiate with color:

sns.pointplot(data\=penguins, x\="island", y\="body\_mass\_g", hue\="sex")

Copy to clipboard

![../_images/pointplot_3_0.png](https://seaborn.pydata.org/_images/pointplot_3_0.png)

Redundantly code the `hue` variable using the markers and linestyles for better accessibility:

sns.pointplot(
    data\=penguins,
    x\="island", y\="body\_mass\_g", hue\="sex",
    markers\=\["o", "s"\], linestyles\=\["-", "--"\],
)

Copy to clipboard

![../_images/pointplot_5_0.png](https://seaborn.pydata.org/_images/pointplot_5_0.png)

Use the error bars to represent the standard deviation of each distribution:

sns.pointplot(data\=penguins, x\="island", y\="body\_mass\_g", errorbar\="sd")

Copy to clipboard

![../_images/pointplot_7_0.png](https://seaborn.pydata.org/_images/pointplot_7_0.png)

Customize the appearance of the plot:

sns.pointplot(
    data\=penguins, x\="body\_mass\_g", y\="island",
    errorbar\=("pi", 100), capsize\=.4,
    color\=".5", linestyle\="none", marker\="D",
)

Copy to clipboard

![../_images/pointplot_9_0.png](https://seaborn.pydata.org/_images/pointplot_9_0.png)

“Dodge” the artists along the categorical axis to reduce overplotting:

sns.pointplot(data\=penguins, x\="sex", y\="bill\_depth\_mm", hue\="species", dodge\=True)

Copy to clipboard

![../_images/pointplot_11_0.png](https://seaborn.pydata.org/_images/pointplot_11_0.png)

Dodge by a specific amount, relative to the width allotted for each level:

sns.stripplot(
    data\=penguins, x\="species", y\="bill\_depth\_mm", hue\="sex",
    dodge\=True, alpha\=.2, legend\=False,
)
sns.pointplot(
    data\=penguins, x\="species", y\="bill\_depth\_mm", hue\="sex",
    dodge\=.4, linestyle\="none", errorbar\=None,
    marker\="\_", markersize\=20, markeredgewidth\=3,
)

Copy to clipboard

![../_images/pointplot_13_0.png](https://seaborn.pydata.org/_images/pointplot_13_0.png)

When variables are not explicitly assigned and the dataset is two-dimensional, the plot will aggregate over each column:

flights\_wide \= flights.pivot(index\="year", columns\="month", values\="passengers")
sns.pointplot(flights\_wide)

Copy to clipboard

![../_images/pointplot_15_0.png](https://seaborn.pydata.org/_images/pointplot_15_0.png)

With one-dimensional data, each value is plotted (relative to its key or index when available):

sns.pointplot(flights\_wide\["Jun"\])

Copy to clipboard

![../_images/pointplot_17_0.png](https://seaborn.pydata.org/_images/pointplot_17_0.png)

Control the formatting of the categorical variable as it appears in the tick labels:

sns.pointplot(flights\_wide\["Jun"\], formatter\=lambda x: f"'{x % 1900}")

Copy to clipboard

![../_images/pointplot_19_0.png](https://seaborn.pydata.org/_images/pointplot_19_0.png)

Or preserve the native scale of the grouping variable:

ax \= sns.pointplot(flights\_wide\["Jun"\], native\_scale\=True)
ax.plot(1955, 335, marker\="\*", color\="r", markersize\=10)

Copy to clipboard

![../_images/pointplot_21_0.png](https://seaborn.pydata.org/_images/pointplot_21_0.png)
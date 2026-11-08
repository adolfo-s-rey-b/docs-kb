 

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

seaborn.boxenplot[#](https://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn-boxenplot "Permalink to this heading")

================================================================================================================================

seaborn.boxenplot(_data=None_, _\*_, _x=None_, _y=None_, _hue=None_, _order=None_, _hue\_order=None_, _orient=None_, _color=None_, _palette=None_, _saturation=0.75_, _fill=True_, _dodge='auto'_, _width=0.8_, _gap=0_, _linewidth=None_, _linecolor=None_, _width\_method='exponential'_, _k\_depth='tukey'_, _outlier\_prop=0.007_, _trust\_alpha=0.05_, _showfliers=True_, _hue\_norm=None_, _log\_scale=None_, _native\_scale=False_, _formatter=None_, _legend='auto'_, _scale=<deprecated>_, _box\_kws=None_, _flier\_kws=None_, _line\_kws=None_, _ax=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn.boxenplot "Permalink to this definition")

Draw an enhanced box plot for larger datasets.

This style of plot was originally named a “letter value” plot because it shows a large number of quantiles that are defined as “letter values”. It is similar to a box plot in plotting a nonparametric representation of a distribution in which all features correspond to actual observations. By plotting more quantiles, it provides more information about the shape of the distribution, particularly in the tails.

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

**dodge**“auto” or bool

When hue mapping is used, whether elements should be narrowed and shifted along the orient axis to eliminate overlap. If `"auto"`, set to `True` when the orient variable is crossed with the categorical variable or `False` otherwise.

Changed in version 0.13.0: Added `"auto"` mode as a new default.

**width**float

Width allotted to each element on the orient axis. When `native_scale=True`, it is relative to the minimum distance between two values in the native scale.

**gap**float

Shrink on the orient axis by this factor to add a gap between dodged elements.

New in version 0.13.0.

**linewidth**float

Width of the lines that frame the plot elements.

**linecolor**color

Color to use for line elements, when `fill` is True.

New in version v0.13.0.

**width\_method**{“exponential”, “linear”, “area”}

Method to use for the width of the letter value boxes:

*   `"exponential"`: Represent the corresponding percentile
    
*   `"linear"`: Decrease by a constant amount for each box
    
*   `"area"`: Represent the density of data points in that box
    

**k\_depth**{“tukey”, “proportion”, “trustworthy”, “full”} or int

The number of levels to compute and draw in each tail:

*   `"tukey"`: Use log2(n) - 3 levels, covering similar range as boxplot whiskers
    
*   `"proportion"`: Leave approximately `outlier_prop` fliers
    
*   `"trusthworthy"`: Extend to level with confidence of at least `trust_alpha`
    
*   `"full"`: Use log2(n) + 1 levels and extend to most extreme points
    

**outlier\_prop**float

Proportion of data expected to be outliers; used when `k_depth="proportion"`.

**trust\_alpha**float

Confidence threshold for most extreme level; used when `k_depth="trustworthy"`.

**showfliers**bool

If False, suppress the plotting of outliers.

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

**box\_kws: dict**

Keyword arguments for the box artists; passed to [`matplotlib.patches.Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "(in Matplotlib v3.8.2)")
.

New in version v0.12.0.

**line\_kws: dict**

Keyword arguments for the line denoting the median; passed to [`matplotlib.axes.Axes.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "(in Matplotlib v3.8.2)")
.

New in version v0.12.0.

**flier\_kws: dict**

Keyword arguments for the scatter denoting the outlier observations; passed to [`matplotlib.axes.Axes.scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "(in Matplotlib v3.8.2)")
.

New in version v0.12.0.

**ax**matplotlib Axes

Axes object to draw the plot onto, otherwise uses the current Axes.

**kwargs**key, value mappings

Other keyword arguments are passed to [`matplotlib.patches.Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "(in Matplotlib v3.8.2)")
, superceded by those in `box_kws`.

Returns:

**ax**matplotlib Axes

Returns the Axes object with the plot drawn onto it.

See also

[`violinplot`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "seaborn.violinplot")

A combination of boxplot and kernel density estimation.

[`boxplot`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")

A traditional box-and-whisker plot with a similar API.

[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")

Combine a categorical plot with a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

Notes

For a more extensive explanation, you can read the paper that introduced the plot: [https://vita.had.co.nz/papers/letter-value-plot.html](https://vita.had.co.nz/papers/letter-value-plot.html)

Examples

Draw a single horizontal plot, assigning the data directly to the coordinate variable:

sns.boxenplot(x\=diamonds\["price"\])

Copy to clipboard

![../_images/boxenplot_1_0.png](https://seaborn.pydata.org/_images/boxenplot_1_0.png)

Group by a categorical variable, referencing columns in a datafame

sns.boxenplot(data\=diamonds, x\="price", y\="clarity")

Copy to clipboard

![../_images/boxenplot_3_0.png](https://seaborn.pydata.org/_images/boxenplot_3_0.png)

Group by another variable, representing it by the color of the boxes. By default, each boxen plot will be “dodged” so that they don’t overlap; you can also add a small gap between them:

large\_diamond \= diamonds\["carat"\].gt(1).rename("large\_diamond")
sns.boxenplot(data\=diamonds, x\="price", y\="clarity", hue\=large\_diamond, gap\=.2)

Copy to clipboard

![../_images/boxenplot_5_0.png](https://seaborn.pydata.org/_images/boxenplot_5_0.png)

The default rule for choosing each box width represents the percentile covered by the box. Alternatively, you can reduce each box width by a linear factor:

sns.boxenplot(data\=diamonds, x\="price", y\="clarity", width\_method\="linear")

Copy to clipboard

![../_images/boxenplot_7_0.png](https://seaborn.pydata.org/_images/boxenplot_7_0.png)

The `width` parameter itself, on the other hand, determines the width of the largest box:

sns.boxenplot(data\=diamonds, x\="price", y\="clarity", width\=.5)

Copy to clipboard

![../_images/boxenplot_9_0.png](https://seaborn.pydata.org/_images/boxenplot_9_0.png)

There are several different approaches for choosing the number of boxes to draw, including a rule based on the confidence level of the percentie estimate:

sns.boxenplot(data\=diamonds, x\="price", y\="clarity", k\_depth\="trustworthy", trust\_alpha\=0.01)

Copy to clipboard

![../_images/boxenplot_11_0.png](https://seaborn.pydata.org/_images/boxenplot_11_0.png)

The `linecolor` and `linewidth` parameters control the outlines of the boxes, while the `line_kws` parameter controls the line representing the median and the `flier_kws` parameter controls the appearance of the outliers:

sns.boxenplot(
    data\=diamonds, x\="price", y\="clarity",
    linewidth\=.5, linecolor\=".7",
    line\_kws\=dict(linewidth\=1.5, color\="#cde"),
    flier\_kws\=dict(facecolor\=".7", linewidth\=.5),
)

Copy to clipboard

![../_images/boxenplot_13_0.png](https://seaborn.pydata.org/_images/boxenplot_13_0.png)

It is also possible to draw unfilled boxes. With unfilled boxes, all elements will be drawn as line art and follow `hue`, when used:

sns.boxenplot(data\=diamonds, x\="price", y\="clarity", hue\="clarity", fill\=False)

Copy to clipboard

![../_images/boxenplot_15_0.png](https://seaborn.pydata.org/_images/boxenplot_15_0.png)
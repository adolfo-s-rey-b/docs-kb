[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

matplotlib.axes.Axes.boxplot[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib-axes-axes-boxplot "Link to this heading")

=================================================================================================================================================================

Axes.boxplot(_x_, _\*_, _notch\=None_, _sym\=None_, _vert\=None_, _orientation\='vertical'_, _whis\=None_, _positions\=None_, _widths\=None_, _patch\_artist\=None_, _bootstrap\=None_, _usermedians\=None_, _conf\_intervals\=None_, _meanline\=None_, _showmeans\=None_, _showcaps\=None_, _showbox\=None_, _showfliers\=None_, _boxprops\=None_, _tick\_labels\=None_, _flierprops\=None_, _medianprops\=None_, _meanprops\=None_, _capprops\=None_, _whiskerprops\=None_, _manage\_ticks\=True_, _autorange\=False_, _zorder\=None_, _capwidths\=None_, _label\=None_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L4303-L4639)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "Link to this definition")

Draw a box and whisker plot.

The box extends from the first quartile (Q1) to the third quartile (Q3) of the data, with a line at the median. The whiskers extend from the box to the farthest data point lying within 1.5x the inter-quartile range (IQR) from the box. Flier points are those past the end of the whiskers. See [https://en.wikipedia.org/wiki/Box\_plot](https://en.wikipedia.org/wiki/Box_plot)
 for reference.

     Q1-1.5IQR   Q1   median  Q3   Q3+1.5IQR
                  |-----:-----|
  o      |--------|     :     |--------|    o  o
                  |-----:-----|
flier             <----------->            fliers
                       IQR

Parameters:

**x**1D array or sequence of 1D arrays or 2D array

The input data. Possible values:

*   1D array: A single box is drawn.
    
*   sequence of 1D arrays: A box is drawn for each array in the sequence.
    
*   2D array: A box is drawn for each column in the array.
    

**notch**bool, default: `[rcParams["boxplot.notch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=boxplot.notch#rcparam-boxplot-notch) ` (default: `False`)

Whether to draw a notched boxplot ([`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
), or a rectangular boxplot ([`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
). The notches represent the confidence interval (CI) around the median. The documentation for _bootstrap_ describes how the locations of the notches are computed by default, but their locations may also be overridden by setting the _conf\_intervals_ parameter.

Note

In cases where the values of the CI are less than the lower quartile or greater than the upper quartile, the notches will extend beyond the box, giving it a distinctive "flipped" appearance. This is expected behavior and consistent with other statistical visualization packages.

**sym**str, optional

The default symbol for flier points. An empty string ('') hides the fliers. If [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, then the fliers default to 'b+'. More control is provided by the _flierprops_ parameter.

**vert**bool, optional

Deprecated since version 3.11: Use _orientation_ instead.

If this is given during the deprecation period, it overrides the _orientation_ parameter.

If True, plots the boxes vertically. If False, plots the boxes horizontally.

**orientation**{'vertical', 'horizontal'}, default: 'vertical'

If 'horizontal', plots the boxes horizontally. Otherwise, plots the boxes vertically.

Added in version 3.10.

**whis**float or (float, float), default: 1.5

The position of the whiskers.

If a float, the lower whisker is at the lowest datum above `Q1 - whis*(Q3-Q1)`, and the upper whisker at the highest datum below `Q3 + whis*(Q3-Q1)`, where Q1 and Q3 are the first and third quartiles. The default value of `whis = 1.5` corresponds to Tukey's original definition of boxplots.

If a pair of floats, they indicate the percentiles at which to draw the whiskers (e.g., (5, 95)). In particular, setting this to (0, 100) results in whiskers covering the whole range of the data.

In the edge case where `Q1 == Q3`, _whis_ is automatically set to (0, 100) (cover the whole range of the data) if _autorange_ is True.

Beyond the whiskers, data are considered outliers and are plotted as individual points.

**bootstrap**int, optional

Specifies whether to bootstrap the confidence intervals around the median for notched boxplots. If _bootstrap_ is None, no bootstrapping is performed, and notches are calculated using a Gaussian-based asymptotic approximation (see McGill, R., Tukey, J.W., and Larsen, W.A., 1978, and Kendall and Stuart, 1967). Otherwise, bootstrap specifies the number of times to bootstrap the median to determine its 95% confidence intervals. Values between 1000 and 10000 are recommended.

**usermedians**1D array-like, optional

A 1D array-like of length `len(x)`. Each entry that is not [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 forces the value of the median for the corresponding dataset. For entries that are [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, the medians are computed by Matplotlib as normal.

**conf\_intervals**array-like, optional

A 2D array-like of shape `(len(x), 2)`. Each entry that is not None forces the location of the corresponding notch (which is only drawn if _notch_ is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
). For entries that are [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, the notches are computed by the method specified by the other parameters (e.g., _bootstrap_).

**positions**array-like, optional

The positions of the boxes. The ticks and limits are automatically set to match the positions. Defaults to `range(1, N+1)` where N is the number of boxes to be drawn.

**widths**float or array-like

The widths of the boxes. The default is 0.5, or `0.15*(distance between extreme positions)`, if that is smaller.

**patch\_artist**bool, default: `[rcParams["boxplot.patchartist"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=boxplot.patchartist#rcparam-boxplot-patchartist) ` (default: `False`)

If [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
 produces boxes with the Line2D artist. Otherwise, boxes are drawn with Patch artists.

**tick\_labels**list of str, optional

The tick labels of each boxplot. Ticks are always placed at the box _positions_. If _tick\_labels_ is given, the ticks are labelled accordingly. Otherwise, they keep their numeric values.

Changed in version 3.9: Renamed from _labels_, which is also removed in 3.11.

**manage\_ticks**bool, default: True

If True, the tick locations and labels will be adjusted to match the boxplot positions.

**autorange**bool, default: False

When [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 and the data are distributed such that the 25th and 75th percentiles are equal, _whis_ is set to (0, 100) such that the whisker ends are at the minimum and maximum of the data.

**meanline**bool, default: `[rcParams["boxplot.meanline"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=boxplot.meanline#rcparam-boxplot-meanline) ` (default: `False`)

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 (and _showmeans_ is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
), will try to render the mean as a line spanning the full width of the box according to _meanprops_ (see below). Not recommended if _shownotches_ is also True. Otherwise, means will be shown as points.

**zorder**float, default: `Line2D.zorder = 2`

The zorder of the boxplot.

Returns:

dict

A dictionary mapping each component of the boxplot to a list of the [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instances created. That dictionary has the following keys (assuming vertical boxplots):

*   `boxes`: the main body of the boxplot showing the quartiles and the median's confidence intervals if enabled.
    
*   `medians`: horizontal lines at the median of each box.
    
*   `whiskers`: the vertical lines extending to the most extreme, non-outlier data points.
    
*   `caps`: the horizontal lines at the ends of the whiskers.
    
*   `fliers`: points representing data that extend beyond the whiskers (fliers).
    
*   `means`: points or lines representing the means.
    

Other Parameters:

**showcaps**bool, default: `[rcParams["boxplot.showcaps"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=boxplot.showcaps#rcparam-boxplot-showcaps) ` (default: `True`)

Show the caps on the ends of whiskers.

**showbox**bool, default: `[rcParams["boxplot.showbox"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=boxplot.showbox#rcparam-boxplot-showbox) ` (default: `True`)

Show the central box.

**showfliers**bool, default: `[rcParams["boxplot.showfliers"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=boxplot.showfliers#rcparam-boxplot-showfliers) ` (default: `True`)

Show the outliers beyond the caps.

**showmeans**bool, default: `[rcParams["boxplot.showmeans"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=boxplot.showmeans#rcparam-boxplot-showmeans) ` (default: `False`)

Show the arithmetic means.

**capprops**dict, default: None

The style of the caps.

**capwidths**float or array, default: None

The widths of the caps.

**boxprops**dict, default: None

The style of the box.

**whiskerprops**dict, default: None

The style of the whiskers.

**flierprops**dict, default: None

The style of the fliers.

**medianprops**dict, default: None

The style of the median.

**meanprops**dict, default: None

The style of the mean.

**label**str or list of str, optional

Legend labels. Use a single string when all boxes have the same style and you only want a single legend entry for them. Use a list of strings to label all boxes individually. To be distinguishable, the boxes should be styled individually, which is currently only possible by modifying the returned artists, see e.g. [Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)
.

In the case of a single string, the legend entry will technically be associated with the first box only. By default, the legend will show the median line (`result["medians"]`); if _patch\_artist_ is True, the legend will show the box [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 artists (`result["boxes"]`) instead.

Added in version 3.9.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

See also

[`Axes.bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")

Draw a boxplot from pre-computed statistics.

[`violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")

Draw an estimate of the probability density function.

Examples using `matplotlib.axes.Axes.boxplot`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#examples-using-matplotlib-axes-axes-boxplot "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_thumb.png)

[Artist customization in box plots](https://matplotlib.org/stable/gallery/statistics/boxplot.html)

Artist customization in box plots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_color_thumb.png)

[Box plots with custom fill colors](https://matplotlib.org/stable/gallery/statistics/boxplot_color.html)

Box plots with custom fill colors

![](https://matplotlib.org/stable/_images/sphx_glr_bxp_thumb.png)

[Separate calculation and plotting of boxplots](https://matplotlib.org/stable/gallery/statistics/bxp.html)

Separate calculation and plotting of boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_vs_violin_thumb.png)

[Box plot vs. violin plot comparison](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html)

Box plot vs. violin plot comparison

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_plot_thumb.png)

[boxplot(X)](https://matplotlib.org/stable/plot_types/stats/boxplot_plot.html)

boxplot(X)

On this page
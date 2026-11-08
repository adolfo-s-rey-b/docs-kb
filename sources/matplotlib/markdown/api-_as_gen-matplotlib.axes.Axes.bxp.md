[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#main-content)

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
    

matplotlib.axes.Axes.bxp[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib-axes-axes-bxp "Link to this heading")

=====================================================================================================================================================

Axes.bxp(_bxpstats_, _positions\=None_, _\*_, _widths\=None_, _vert\=None_, _orientation\='vertical'_, _patch\_artist\=False_, _shownotches\=False_, _showmeans\=False_, _showcaps\=True_, _showbox\=True_, _showfliers\=True_, _boxprops\=None_, _whiskerprops\=None_, _flierprops\=None_, _medianprops\=None_, _capprops\=None_, _meanprops\=None_, _meanline\=False_, _manage\_ticks\=True_, _zorder\=None_, _capwidths\=None_, _label\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L4641-L5015)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "Link to this definition")

Draw a box and whisker plot from pre-computed statistics.

The box extends from the first quartile _q1_ to the third quartile _q3_ of the data, with a line at the median (_med_). The whiskers extend from _whislow_ to _whishi_. Flier points are markers past the end of the whiskers. See [https://en.wikipedia.org/wiki/Box\_plot](https://en.wikipedia.org/wiki/Box_plot)
 for reference.

      whislow    q1    med    q3    whishi
                  |-----:-----|
  o      |--------|     :     |--------|    o  o
                  |-----:-----|
flier                                      fliers

Note

This is a low-level drawing function for when you already have the statistical parameters. If you want a boxplot based on a dataset, use [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 instead.

Parameters:

**bxpstats**list of dicts

A list of dictionaries containing stats for each boxplot. Required keys are:

*   `med`: Median (float).
    
*   `q1`, `q3`: First & third quartiles (float).
    
*   `whislo`, `whishi`: Lower & upper whisker positions (float).
    

Optional keys are:

*   `mean`: Mean (float). Needed if `showmeans=True`.
    
*   `fliers`: Data beyond the whiskers (array-like). Needed if `showfliers=True`.
    
*   `cilo`, `cihi`: Lower & upper confidence intervals about the median. Needed if `shownotches=True`.
    
*   `label`: Name of the dataset (str). If available, this will be used a tick label for the boxplot
    

**positions**array-like, default: \[1, 2, ..., n\]

The positions of the boxes. The ticks and limits are automatically set to match the positions.

**widths**float or array-like, default: None

The widths of the boxes. The default is `clip(0.15*(distance between extreme positions), 0.15, 0.5)`.

**capwidths**float or array-like, default: None

Either a scalar or a vector and sets the width of each cap. The default is `0.5*(width of the box)`, see _widths_.

**vert**bool, optional

Deprecated since version 3.11: Use _orientation_ instead.

If this is given during the deprecation period, it overrides the _orientation_ parameter.

If True, plots the boxes vertically. If False, plots the boxes horizontally.

**orientation**{'vertical', 'horizontal'}, default: 'vertical'

If 'horizontal', plots the boxes horizontally. Otherwise, plots the boxes vertically.

Added in version 3.10.

**patch\_artist**bool, default: False

If [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
 produces boxes with the [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 artist. If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 produces boxes with the [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 artist.

**shownotches, showmeans, showcaps, showbox, showfliers**bool

Whether to draw the CI notches, the mean value (both default to False), the caps, the box, and the fliers (all three default to True).

**boxprops, whiskerprops, capprops, flierprops, medianprops, meanprops**dict, optional

Artist properties for the boxes, whiskers, caps, fliers, medians, and means.

**meanline**bool, default: False

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 (and _showmeans_ is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
), will try to render the mean as a line spanning the full width of the box according to _meanprops_. Not recommended if _shownotches_ is also True. Otherwise, means will be shown as points.

**manage\_ticks**bool, default: True

If True, the tick locations and labels will be adjusted to match the boxplot positions.

**label**str or list of str, optional

Legend labels. Use a single string when all boxes have the same style and you only want a single legend entry for them. Use a list of strings to label all boxes individually. To be distinguishable, the boxes should be styled individually, which is currently only possible by modifying the returned artists, see e.g. [Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)
.

In the case of a single string, the legend entry will technically be associated with the first box only. By default, the legend will show the median line (`result["medians"]`); if _patch\_artist_ is True, the legend will show the box [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 artists (`result["boxes"]`) instead.

Added in version 3.9.

**zorder**float, default: `Line2D.zorder = 2`

The zorder of the resulting boxplot.

Returns:

dict

A dictionary mapping each component of the boxplot to a list of the [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instances created. That dictionary has the following keys (assuming vertical boxplots):

*   `boxes`: main bodies of the boxplot showing the quartiles, and the median's confidence intervals if enabled.
    
*   `medians`: horizontal lines at the median of each box.
    
*   `whiskers`: vertical lines up to the last non-outlier data.
    
*   `caps`: horizontal lines at the ends of the whiskers.
    
*   `fliers`: points representing data beyond the whiskers (fliers).
    
*   `means`: points or lines representing the means.
    

See also

[`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")

Draw a boxplot from data instead of pre-computed statistics.

Examples using `matplotlib.axes.Axes.bxp`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#examples-using-matplotlib-axes-axes-bxp "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_bxp_thumb.png)

[Separate calculation and plotting of boxplots](https://matplotlib.org/stable/gallery/statistics/bxp.html)

Separate calculation and plotting of boxplots

On this page
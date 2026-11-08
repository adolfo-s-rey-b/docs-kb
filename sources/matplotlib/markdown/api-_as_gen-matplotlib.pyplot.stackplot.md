[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stackplot.html#main-content)

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
    

matplotlib.pyplot.stackplot[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stackplot.html#matplotlib-pyplot-stackplot "Link to this heading")

==============================================================================================================================================================

matplotlib.pyplot.stackplot(_x_, _\*args_, _labels\=()_, _colors\=None_, _baseline\='zero'_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4237-L4247)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stackplot.html#matplotlib.pyplot.stackplot "Link to this definition")

Draw a stacked area plot or a streamgraph.

Parameters:

**x**(N,) array-like

**y**(M, N) array-like

The data can be either stacked or unstacked. Each of the following calls is legal:

stackplot(x, y)  \# where y has shape (M, N) e.g. y = \[y1, y2, y3, y4\]
stackplot(x, y1, y2, y3, y4)  \# where y1, y2, y3, y4 have length N

**baseline**{'zero', 'sym', 'wiggle', 'weighted\_wiggle'}

Method used to calculate the baseline:

*   `'zero'`: Constant zero baseline, i.e. a simple stacked plot.
    
*   `'sym'`: Symmetric around zero and is sometimes called 'ThemeRiver'.
    
*   `'wiggle'`: Minimizes the sum of the squared slopes.
    
*   `'weighted_wiggle'`: Does the same but weights to account for size of each layer. It is also called 'Streamgraph'-layout. More details can be found at [http://leebyron.com/streamgraph/](http://leebyron.com/streamgraph/)
    .
    

**labels**list of str, optional

A sequence of labels to assign to each data series. If unspecified, then no labels will be applied to artists.

**colors**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

A sequence of colors to be cycled through and used to color the stacked areas. The sequence need not be exactly the same length as the number of provided _y_, in which case the colors will repeat from the beginning.

If not specified, the colors from the Axes property cycle will be used.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**

All other keyword arguments are passed to [`Axes.fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
. The

following parameters additionally accept a sequence of values corresponding to the _y_ datasets:

*   _hatch_
    
*   _edgecolor_
    
*   _facecolor_
    
*   _linewidth_
    
*   _linestyle_
    

Added in version 3.9: Allowing a sequence of strings for _hatch_.

Added in version 3.11: Allowing sequences of values in above listed [`Axes.fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
 parameters.

Returns:

list of [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")

A list of [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 instances, one for each element in the stacked area plot.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.stackplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html#matplotlib.axes.Axes.stackplot "matplotlib.axes.Axes.stackplot")
.

On this page
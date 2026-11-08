[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html#main-content)

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
    

matplotlib.pyplot.hlines[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html#matplotlib-pyplot-hlines "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.hlines(_y_, _xmin_, _xmax_, _colors\=None_, _linestyles\='solid'_, _\*_, _label\=''_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3737-L3758)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html#matplotlib.pyplot.hlines "Link to this definition")

Plot horizontal lines at each _y_ from _xmin_ to _xmax_.

Parameters:

**y**float or array-like

y-indexes where to plot the lines.

**xmin, xmax**float or array-like

Respective beginning and end of each line. If scalars are provided, all lines will have the same length.

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of color , default: `[rcParams["lines.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.color#rcparam-lines-color) ` (default: `'C0'`)

**linestyles**{'solid', 'dashed', 'dashdot', 'dotted'}, default: 'solid'

**label**str, default: ''

Returns:

[`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

Other Parameters:

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_y_, _xmin_, _xmax_, _colors_

**\*\*kwargs**[`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 properties.

See also

[`vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")

vertical lines

[`axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html#matplotlib.pyplot.axhline "matplotlib.pyplot.axhline")

horizontal line across the Axes

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.hlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hlines.html#matplotlib.axes.Axes.hlines "matplotlib.axes.Axes.hlines")
.

On this page
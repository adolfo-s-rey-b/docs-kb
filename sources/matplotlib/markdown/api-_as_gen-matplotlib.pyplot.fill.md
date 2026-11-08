[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html#main-content)

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
    

matplotlib.pyplot.fill[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html#matplotlib-pyplot-fill "Link to this heading")

===============================================================================================================================================

matplotlib.pyplot.fill(_\*args_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3489-L3491)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html#matplotlib.pyplot.fill "Link to this definition")

Plot filled polygons.

Parameters:

**\*args**sequence of x, y, \[color\]

Each polygon is defined by the lists of _x_ and _y_ positions of its nodes, optionally followed by a _color_ specifier. See [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
 for supported color specifiers. The standard color cycle is used for polygons without a color specifier.

You can plot multiple polygons by providing multiple _x_, _y_, _\[color\]_ groups.

For example, each of the following is legal:

ax.fill(x, y)                    \# a polygon with default color
ax.fill(x, y, "b")               \# a blue polygon
ax.fill(x, y, x2, y2)            \# two polygons
ax.fill(x, y, "b", x2, y2, "r")  \# a blue and a red polygon

**data**indexable object, optional

An object with labelled data. If given, provide the label names to plot in _x_ and _y_, e.g.:

ax.fill("time", "signal",
        data\={"time": \[0, 1, 2\], "signal": \[0, 1, 0\]})

Returns:

list of [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")

Other Parameters:

**\*\*kwargs**[`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 properties

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
.

Use [`fill_between()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
 if you would like to fill the region between two curves.

Examples using `matplotlib.pyplot.fill`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html#examples-using-matplotlib-pyplot-fill "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_fill_thumb.png)

[Filled polygon](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html)

Filled polygon

![](https://matplotlib.org/stable/_images/sphx_glr_ginput_manual_clabel_sgskip_thumb.png)

[Interactive functions](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html)

Interactive functions

![](https://matplotlib.org/stable/_images/sphx_glr_fill_spiral_thumb.png)

[Fill spiral](https://matplotlib.org/stable/gallery/misc/fill_spiral.html)

Fill spiral

On this page
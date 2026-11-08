[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html#main-content)

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
    

matplotlib.pyplot.loglog[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html#matplotlib-pyplot-loglog "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.loglog(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3823-L3825)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html#matplotlib.pyplot.loglog "Link to this definition")

Make a plot with log scaling on both the x- and y-axis.

Call signatures:

loglog(\[x\], y, \[fmt\], data\=None, \*\*kwargs)
loglog(\[x\], y, \[fmt\], \[x2\], y2, \[fmt2\], ..., \*\*kwargs)

This is just a thin wrapper around [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
 which additionally changes both the x-axis and the y-axis to log scaling. All the concepts and parameters of plot can be used here as well.

The additional parameters _base_, _subs_ and _nonpositive_ control the x/y-axis properties. They are just forwarded to [`Axes.set_xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
 and [`Axes.set_yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
. To use different properties on the x-axis and the y-axis, use e.g. `ax.set_xscale("log", base=10); ax.set_yscale("log", base=2)`.

Parameters:

**base**float, default: 10

Base of the logarithm.

**subs**sequence, optional

The location of the minor ticks. If _None_, reasonable locations are automatically chosen depending on the number of decades in the plot. See [`Axes.set_xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
/[`Axes.set_yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
 for details.

**nonpositive**{'mask', 'clip'}, default: 'clip'

Non-positive values can be masked as invalid, or clipped to a very small positive number.

**\*\*kwargs**

All parameters supported by [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
.

Returns:

list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

Objects representing the plotted data.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.loglog`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html#matplotlib.axes.Axes.loglog "matplotlib.axes.Axes.loglog")
.

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html#main-content)

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
    

matplotlib.axes.Axes.step[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html#matplotlib-axes-axes-step "Link to this heading")

========================================================================================================================================================

Axes.step(_x_, _y_, _\*args_, _where\='pre'_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L2138-L2204)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html#matplotlib.axes.Axes.step "Link to this definition")

Make a step plot.

Call signatures:

step(x, y, \[fmt\], \*, data\=None, where\='pre', \*\*kwargs)
step(x, y, \[fmt\], x2, y2, \[fmt2\], ..., \*, where\='pre', \*\*kwargs)

This is just a thin wrapper around [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 which changes some formatting options. Most of the concepts and parameters of plot can be used here as well.

Note

This method uses a standard plot with a step drawstyle: The _x_ values are the reference positions and steps extend left/right/both directions depending on _where_.

For the common case where you know the values and edges of the steps, use [`stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stairs.html#matplotlib.axes.Axes.stairs "matplotlib.axes.Axes.stairs")
 instead.

Parameters:

**x**array-like

1D sequence of x positions. It is assumed, but not checked, that it is uniformly increasing.

**y**array-like

1D sequence of y levels.

**fmt**str, optional

A format string, e.g. 'g' for a green line. See [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 for a more detailed description.

Note: While full format strings are accepted, it is recommended to only specify the color. Line styles are currently ignored (use the keyword argument _linestyle_ instead). Markers are accepted and plotted on the given positions, however, this is a rarely needed feature for step plots.

**where**{'pre', 'post', 'mid'}, default: 'pre'

Define where the steps should be placed:

*   'pre': The y value is continued constantly to the left from every _x_ position, i.e. the interval `(x[i-1], x[i]]` has the value `y[i]`.
    
*   'post': The y value is continued constantly to the right from every _x_ position, i.e. the interval `[x[i], x[i+1])` has the value `y[i]`.\
    \
*   'mid': Steps occur half-way between the _x_ positions.\
    \
\
**data**indexable object, optional\
\
An object with labelled data. If given, provide the label names to plot in _x_ and _y_.\
\
**\*\*kwargs**\
\
Additional parameters are the same as those for [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")\
.\
\
Returns:\
\
list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\
Objects representing the plotted data.\
\
Examples using `matplotlib.axes.Axes.step`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html#examples-using-matplotlib-axes-axes-step "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://matplotlib.org/stable/_images/sphx_glr_step_demo_thumb.png)\
\
[Step Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/step_demo.html)\
\
Step Demo\
\
![](https://matplotlib.org/stable/_images/sphx_glr_stairs_thumb.png)\
\
[stairs(values)](https://matplotlib.org/stable/plot_types/basic/stairs.html)\
\
stairs(values)\
\
On this page
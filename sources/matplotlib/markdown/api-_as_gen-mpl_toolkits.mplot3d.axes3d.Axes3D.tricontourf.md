[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.tricontourf[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf.html#mpl-toolkits-mplot3d-axes3d-axes3d-tricontourf "Link to this heading")

========================================================================================================================================================================================================================

Axes3D.tricontourf(_\*args_, _zdir\='z'_, _offset\=None_, _axlim\_clip\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3044-L3095)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf "Link to this definition")

Create a 3D filled contour plot.

Note

This method currently produces incorrect output due to a longstanding bug in 3D PolyCollection rendering.

Parameters:

**X, Y, Z**array-like

Input data. See [`Axes.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
 for supported data shapes.

**zdir**{'x', 'y', 'z'}, default: 'z'

The direction to use.

**offset**float, optional

If specified, plot a projection of the contour lines at this position in a plane normal to zdir.

**axlim\_clip**bool, default: False

Whether to hide lines with a vertex outside the axes view limits.

Added in version 3.10.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*args, \*\*kwargs**

Other arguments are forwarded to [`matplotlib.axes.Axes.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
.

Returns:

matplotlib.tri.\_tricontour.TriContourSet

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-tricontourf "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_tricontourf3d_thumb.png)

[Triangular 3D filled contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontourf3d.html)

Triangular 3D filled contour plot

On this page
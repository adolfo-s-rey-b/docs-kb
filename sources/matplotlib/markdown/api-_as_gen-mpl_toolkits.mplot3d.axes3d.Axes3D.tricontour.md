[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.tricontour[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour.html#mpl-toolkits-mplot3d-axes3d-axes3d-tricontour "Link to this heading")

=====================================================================================================================================================================================================================

Axes3D.tricontour(_\*args_, _extend3d\=False_, _stride\=5_, _zdir\='z'_, _offset\=None_, _axlim\_clip\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L2937-L2993)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour "Link to this definition")

Create a 3D contour plot.

Note

This method currently produces incorrect output due to a longstanding bug in 3D PolyCollection rendering.

Parameters:

**X, Y, Z**array-like

Input data. See [`Axes.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
 for supported data shapes.

**extend3d**bool, default: False

Whether to extend contour in 3D.

**stride**int, default: 5

Step size for extending contour.

**zdir**{'x', 'y', 'z'}, default: 'z'

The direction to use.

**offset**float, optional

If specified, plot a projection of the contour lines at this position in a plane normal to _zdir_.

**axlim\_clip**bool, default: False

Whether to hide lines with a vertex outside the axes view limits.

Added in version 3.10.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*args, \*\*kwargs**

Other arguments are forwarded to [`matplotlib.axes.Axes.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
.

Returns:

matplotlib.tri.\_tricontour.TriContourSet

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-tricontour "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour3d_thumb.png)

[Triangular 3D contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontour3d.html)

Triangular 3D contour plot

On this page
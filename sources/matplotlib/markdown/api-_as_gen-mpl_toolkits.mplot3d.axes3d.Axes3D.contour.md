[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.contour[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#mpl-toolkits-mplot3d-axes3d-axes3d-contour "Link to this heading")

============================================================================================================================================================================================================

Axes3D.contour(_X_, _Y_, _Z_, _\*args_, _extend3d\=False_, _stride\=5_, _zdir\='z'_, _offset\=None_, _axlim\_clip\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L2892-L2933)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contour "Link to this definition")

Create a 3D contour plot.

Parameters:

**X, Y, Z**array-like,

Input data. See [`Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
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

Other arguments are forwarded to [`matplotlib.axes.Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
.

Returns:

matplotlib.contour.QuadContourSet

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.contour`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-contour "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_thumb.png)

[Plot contour (level) curves in 3D](https://matplotlib.org/stable/gallery/mplot3d/contour3d.html)

Plot contour (level) curves in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_2_thumb.png)

[Plot contour (level) curves in 3D using the extend3d option](https://matplotlib.org/stable/gallery/mplot3d/contour3d_2.html)

Plot contour (level) curves in 3D using the extend3d option

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_3_thumb.png)

[Project contour profiles onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html)

Project contour profiles onto a graph

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.bar[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html#mpl-toolkits-mplot3d-axes3d-axes3d-bar "Link to this heading")

================================================================================================================================================================================================

Axes3D.bar(_left_, _height_, _zs\=0_, _zdir\='z'_, _\*args_, _axlim\_clip\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3271-L3329)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar "Link to this definition")

Add 2D bar(s).

Parameters:

**left**1D array-like

The x coordinates of the left sides of the bars.

**height**1D array-like

The height of the bars.

**zs**float or 1D array-like, default: 0

Z coordinate of bars; if a single value is specified, it will be used for all bars.

**zdir**{'x', 'y', 'z'}, default: 'z'

When plotting 2D data, the direction to use as z ('x', 'y' or 'z').

**axlim\_clip**bool, default: False

Whether to hide bars with points outside the axes view limits.

Added in version 3.10.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**

Other keyword arguments are forwarded to [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
.

Returns:

mpl\_toolkits.mplot3d.art3d.Patch3DCollection

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.bar`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-bar "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_bars3d_thumb.png)

[Create 2D bar graphs in different planes](https://matplotlib.org/stable/gallery/mplot3d/bars3d.html)

Create 2D bar graphs in different planes

On this page
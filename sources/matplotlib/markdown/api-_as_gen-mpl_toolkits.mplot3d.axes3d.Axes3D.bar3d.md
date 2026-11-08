[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.bar3d[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#mpl-toolkits-mplot3d-axes3d-axes3d-bar3d "Link to this heading")

======================================================================================================================================================================================================

Axes3D.bar3d(_x_, _y_, _z_, _dx_, _dy_, _dz_, _color\=None_, _zsort\='average'_, _shade\=True_, _lightsource\=None_, _\*args_, _axlim\_clip\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3331-L3497)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d "Link to this definition")

Generate a 3D barplot.

This method creates three-dimensional barplot where the width, depth, height, and color of the bars can all be uniquely set.

Parameters:

**x, y, z**array-like

The coordinates of the anchor point of the bars.

**dx, dy, dz**float or array-like

The width, depth, and height of the bars, respectively.

**color**sequence of colors, optional

The color of the bars can be specified globally or individually. This parameter can be:

*   A single color, to color all bars the same color.
    
*   An array of colors of length N bars, to color each bar independently.
    
*   An array of colors of length 6, to color the faces of the bars similarly.
    
*   An array of colors of length 6 \* N bars, to color each face independently.
    

When coloring the faces of the boxes specifically, this is the order of the coloring:

1.  \-Z (bottom of box)
    
2.  +Z (top of box)
    
3.  \-Y
    
4.  +Y
    
5.  \-X
    
6.  +X
    

**zsort**{'average', 'min', 'max'}, default: 'average'

The z-axis sorting scheme passed onto [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")

**shade**bool, default: True

When true, this shades the dark sides of the bars (relative to the plot's source of light).

**lightsource**[`LightSource`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
, optional

The lightsource to use when _shade_ is True.

**axlim\_clip**bool, default: False

Whether to hide the bars with points outside the axes view limits.

Added in version 3.10.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**

Any additional keyword arguments are passed onto [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
.

Returns:

**collection**[`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")

A collection of three-dimensional polygons representing the bars.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-bar3d "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_3d_bars_thumb.png)

[Demo of 3D bar charts](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html)

Demo of 3D bar charts

![](https://matplotlib.org/stable/_images/sphx_glr_hist3d_thumb.png)

[Create 3D histogram of 2D data](https://matplotlib.org/stable/gallery/mplot3d/hist3d.html)

Create 3D histogram of 2D data

![](https://matplotlib.org/stable/_images/sphx_glr_bar3d_simple_thumb.png)

[bar3d(x, y, z, dx, dy, dz)](https://matplotlib.org/stable/plot_types/3D/bar3d_simple.html)

bar3d(x, y, z, dx, dy, dz)

On this page
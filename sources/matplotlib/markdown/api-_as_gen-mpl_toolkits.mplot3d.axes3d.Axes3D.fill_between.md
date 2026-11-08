[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.fill\_between[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between.html#mpl-toolkits-mplot3d-axes3d-axes3d-fill-between "Link to this heading")

============================================================================================================================================================================================================================

Axes3D.fill\_between(_x1_, _y1_, _z1_, _x2_, _y2_, _z2_, _\*_, _where\=None_, _mode\='auto'_, _facecolors\=None_, _shade\=None_, _axlim\_clip\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L2270-L2398)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between.html#mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between "Link to this definition")

Fill the area between two 3D curves.

The curves are defined by the points (_x1_, _y1_, _z1_) and (_x2_, _y2_, _z2_). This creates one or multiple quadrangle polygons that are filled. All points must be the same length N, or a single value to be used for all points.

Parameters:

**x1, y1, z1**float or 1D array-like

x, y, and z coordinates of vertices for 1st line.

**x2, y2, z2**float or 1D array-like

x, y, and z coordinates of vertices for 2nd line.

**where**array of bool (length N), optional

Define _where_ to exclude some regions from being filled. The filled regions are defined by the coordinates `pts[where]`, for all x, y, and z pts. More precisely, fill between `pts[i]` and `pts[i+1]` if `where[i] and where[i+1]`. Note that this definition implies that an isolated _True_ value between two _False_ values in _where_ will not result in filling. Both sides of the _True_ position remain unfilled due to the adjacent _False_ values.

**mode**{'quad', 'polygon', 'auto'}, default: 'auto'

The fill mode. One of:

*   'quad': A separate quadrilateral polygon is created for each pair of subsequent points in the two lines.
    
*   'polygon': The two lines are connected to form a single polygon. This is faster and can render more cleanly for simple shapes (e.g. for filling between two lines that lie within a plane).
    
*   'auto': If the points all lie on the same 3D plane, 'polygon' is used. Otherwise, 'quad' is used.
    

**facecolors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

Colors of each individual patch, or a single color to be used for all patches. If not given, the next color from the patch color cycle is used.

**shade**bool, default: None

Whether to shade the facecolors. If _None_, then defaults to _True_ for 'quad' mode and _False_ for 'polygon' mode.

**axlim\_clip**bool, default: False

Whether to hide data that is outside the axes view limits.

Added in version 3.10.

**\*\*kwargs**

All other keyword arguments are passed on to [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
.

Returns:

[`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")

A [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
 containing the plotted polygons.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-fill-between "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_fillbetween3d_thumb.png)

[Fill between 3D lines](https://matplotlib.org/stable/gallery/mplot3d/fillbetween3d.html)

Fill between 3D lines

![](https://matplotlib.org/stable/_images/sphx_glr_fillunder3d_thumb.png)

[Fill under 3D line graphs](https://matplotlib.org/stable/gallery/mplot3d/fillunder3d.html)

Fill under 3D line graphs

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between3d_simple_thumb.png)

[fill\_between(x1, y1, z1, x2, y2, z2)](https://matplotlib.org/stable/plot_types/3D/fill_between3d_simple.html)

fill\_between(x1, y1, z1, x2, y2, z2)

On this page
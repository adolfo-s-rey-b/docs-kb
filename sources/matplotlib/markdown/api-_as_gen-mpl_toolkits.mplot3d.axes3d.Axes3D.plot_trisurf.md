[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.plot\_trisurf[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl-toolkits-mplot3d-axes3d-axes3d-plot-trisurf "Link to this heading")

============================================================================================================================================================================================================================

Axes3D.plot\_trisurf(_\*args_, _color\=None_, _norm\=None_, _vmin\=None_, _vmax\=None_, _lightsource\=None_, _axlim\_clip\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L2724-L2824)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "Link to this definition")

Plot a triangulated surface.

The (optional) triangulation can be specified in one of two ways; either:

plot\_trisurf(triangulation, ...)

where triangulation is a [`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 object, or:

plot\_trisurf(X, Y, ...)
plot\_trisurf(X, Y, triangles, ...)
plot\_trisurf(X, Y, triangles\=triangles, ...)

in which case a Triangulation object will be created. See [`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 for an explanation of these possibilities.

The remaining arguments are:

plot\_trisurf(..., Z)

where _Z_ is the array of values to contour, one per point in the triangulation.

Parameters:

**X, Y, Z**array-like

Data values as 1D arrays.

**color**

Color of the surface patches.

**cmap**

A colormap for the surface patches.

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
, optional

An instance of Normalize to map values to colors.

**vmin, vmax**float, optional

Minimum and maximum value to map.

**shade**bool, default: True

Whether to shade the facecolors. Shading is always disabled when _cmap_ is specified.

**lightsource**[`LightSource`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
, optional

The lightsource to use when _shade_ is True.

**axlim\_clip**bool, default: False

Whether to hide patches with a vertex outside the axes view limits.

Added in version 3.10.

**\*\*kwargs**

All other keyword arguments are passed on to [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")

Examples

([`Source code`](https://matplotlib.org/stable/_downloads/352b81410875bbe00f7c64b37a4aa316/trisurf3d.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/ff1f27683e3cccad9db9a9087ed47a4e/trisurf3d_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/46a9e89c96d1ce26fd6d1be9dd1ddc64/trisurf3d_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-trisurf3d_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-trisurf3d_00_00.2x.png)

([`Source code`](https://matplotlib.org/stable/_downloads/d335daf8d7e7f5920a65da3298e7b37e/trisurf3d_2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/21bdb838c4900dcc8df24ad82a357edb/trisurf3d_2_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ae80e0aa505787d6a10572e8570b47de/trisurf3d_2_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-trisurf3d_2_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-trisurf3d_2_00_00.2x.png)

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-plot-trisurf "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_thumb.png)

[Triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d.html)

Triangular 3D surfaces

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_2_thumb.png)

[More triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html)

More triangular 3D surfaces

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_simple_thumb.png)

[plot\_trisurf(x, y, z)](https://matplotlib.org/stable/plot_types/3D/trisurf3d_simple.html)

plot\_trisurf(x, y, z)

On this page
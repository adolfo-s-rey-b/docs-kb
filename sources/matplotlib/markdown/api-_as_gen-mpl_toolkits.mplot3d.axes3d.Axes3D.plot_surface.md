[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.plot\_surface[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl-toolkits-mplot3d-axes3d-axes3d-plot-surface "Link to this heading")

============================================================================================================================================================================================================================

Axes3D.plot\_surface(_X_, _Y_, _Z_, _\*_, _norm\=None_, _vmin\=None_, _vmax\=None_, _lightsource\=None_, _axlim\_clip\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L2400-L2597)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "Link to this definition")

Create a surface plot.

By default, it will be colored in shades of a solid color, but it also supports colormapping by supplying the _cmap_ argument.

Note

The _rcount_ and _ccount_ kwargs, which both default to 50, determine the maximum number of samples used in each direction. If the input data is larger, it will be downsampled (by slicing) to these numbers of points.

Note

To maximize rendering speed consider setting _rstride_ and _cstride_ to divisors of the number of rows minus 1 and columns minus 1 respectively. For example, given 51 rows rstride can be any of the divisors of 50.

Similarly, a setting of _rstride_ and _cstride_ equal to 1 (or _rcount_ and _ccount_ equal the number of rows and columns) can use the optimized path.

Parameters:

**X, Y, Z**2D arrays

Data values.

**rcount, ccount**int

Maximum number of samples used in each direction. If the input data is larger, it will be downsampled (by slicing) to these numbers of points. Defaults to 50.

**rstride, cstride**int

Downsampling stride in each direction. These arguments are mutually exclusive with _rcount_ and _ccount_. If only one of _rstride_ or _cstride_ is set, the other defaults to 10.

'classic' mode uses a default of `rstride = cstride = 10` instead of the new default of `rcount = ccount = 50`.

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Color of the surface patches.

**cmap**Colormap, optional

Colormap of the surface patches.

**facecolors**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Colors of each individual patch.

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
, optional

Normalization for the colormap.

**vmin, vmax**float, optional

Bounds for the normalization.

**shade**bool, default: True

Whether to shade the facecolors. Shading is always disabled when _cmap_ is specified.

**lightsource**[`LightSource`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
, optional

The lightsource to use when _shade_ is True.

**axlim\_clip**bool, default: False

Whether to hide patches with a vertex outside the axes view limits.

Added in version 3.10.

**\*\*kwargs**

Other keyword arguments are forwarded to [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-plot-surface "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_3_thumb.png)

[Project contour profiles onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html)

Project contour profiles onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_contourf3d_2_thumb.png)

[Project filled contour onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contourf3d_2.html)

Project filled contour onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_custom_shaded_3d_surface_thumb.png)

[Custom hillshading in a 3D surface plot](https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html)

Custom hillshading in a 3D surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_imshow3d_thumb.png)

[2D images in 3D](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html)

2D images in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_offset_thumb.png)

[Automatic text offsetting](https://matplotlib.org/stable/gallery/mplot3d/offset.html)

Automatic text offsetting

![](https://matplotlib.org/stable/_images/sphx_glr_subplot3d_thumb.png)

[3D plots as subplots](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html)

3D plots as subplots

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_thumb.png)

[3D surface (colormap)](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)

3D surface (colormap)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_2_thumb.png)

[3D surface (solid color)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html)

3D surface (solid color)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_3_thumb.png)

[3D surface (checkerboard)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_3.html)

3D surface (checkerboard)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_radial_thumb.png)

[3D surface with polar coordinates](https://matplotlib.org/stable/gallery/mplot3d/surface3d_radial.html)

3D surface with polar coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_simple_thumb.png)

[plot\_surface(X, Y, Z)](https://matplotlib.org/stable/plot_types/3D/surface3d_simple.html)

plot\_surface(X, Y, Z)

On this page
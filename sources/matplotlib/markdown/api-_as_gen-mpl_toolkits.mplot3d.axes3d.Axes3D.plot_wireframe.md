[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.plot\_wireframe[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl-toolkits-mplot3d-axes3d-axes3d-plot-wireframe "Link to this heading")

==================================================================================================================================================================================================================================

Axes3D.plot\_wireframe(_X_, _Y_, _Z_, _\*_, _axlim\_clip\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L2599-L2722)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "Link to this definition")

Plot a 3D wireframe.

Note

The _rcount_ and _ccount_ kwargs, which both default to 50, determine the maximum number of samples used in each direction. If the input data is larger, it will be downsampled (by slicing) to these numbers of points.

Parameters:

**X, Y, Z**2D arrays

Data values.

**axlim\_clip**bool, default: False

Whether to hide lines and patches with vertices outside the axes view limits.

Added in version 3.10.

**rcount, ccount**int

Maximum number of samples used in each direction. If the input data is larger, it will be downsampled (by slicing) to these numbers of points. Setting a count to zero causes the data to be not sampled in the corresponding direction, producing a 3D line plot rather than a wireframe plot. Defaults to 50.

**rstride, cstride**int

Downsampling stride in each direction. These arguments are mutually exclusive with _rcount_ and _ccount_. If only one of _rstride_ or _cstride_ is set, the other defaults to 1. Setting a stride to zero causes the data to be not sampled in the corresponding direction, producing a 3D line plot rather than a wireframe plot.

'classic' mode uses a default of `rstride = cstride = 1` instead of the new default of `rcount = ccount = 50`.

**\*\*kwargs**

Other keyword arguments are forwarded to [`Line3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-plot-wireframe "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_axlim_clip_thumb.png)

[Clip the data to the axes view limits](https://matplotlib.org/stable/gallery/mplot3d/axlim_clip.html)

Clip the data to the axes view limits

![](https://matplotlib.org/stable/_images/sphx_glr_projections_thumb.png)

[3D plot projection types](https://matplotlib.org/stable/gallery/mplot3d/projections.html)

3D plot projection types

![](https://matplotlib.org/stable/_images/sphx_glr_subplot3d_thumb.png)

[3D plots as subplots](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html)

3D plots as subplots

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_thumb.png)

[3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d.html)

3D wireframe plot

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_animation_thumb.gif)

[Animate a 3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d_animation.html)

Animate a 3D wireframe plot

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_zero_stride_thumb.png)

[3D wireframe plots in one direction](https://matplotlib.org/stable/gallery/mplot3d/wire3d_zero_stride.html)

3D wireframe plots in one direction

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_simple_thumb.png)

[plot\_wireframe(X, Y, Z)](https://matplotlib.org/stable/plot_types/3D/wire3d_simple.html)

plot\_wireframe(X, Y, Z)

On this page
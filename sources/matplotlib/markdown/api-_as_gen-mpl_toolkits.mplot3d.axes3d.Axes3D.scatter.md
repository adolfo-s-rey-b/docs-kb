[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.scatter[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl-toolkits-mplot3d-axes3d-axes3d-scatter "Link to this heading")

============================================================================================================================================================================================================

Axes3D.scatter(_xs_, _ys_, _zs\=0_, _zdir\='z'_, _s\=20_, _c\=None_, _depthshade\=None_, _\*args_, _depthshade\_minalpha\=None_, _axlim\_clip\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3168-L3267)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl_toolkits.mplot3d.axes3d.Axes3D.scatter "Link to this definition")

Create a scatter plot.

Parameters:

**xs, ys**array-like

The data positions.

**zs**float or array-like, default: 0

The z-positions. Either an array of the same length as _xs_ and _ys_ or a single value to place all points in the same plane.

**zdir**{'x', 'y', 'z', '-x', '-y', '-z'}, default: 'z'

The axis direction for the _zs_. This is useful when plotting 2D data on a 3D Axes. The data must be passed as _xs_, _ys_. Setting _zdir_ to 'y' then plots the data to the x-z-plane.

See also [Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)
.

**s**float or array-like, default: 20

The marker size in points\*\*2. Either an array of the same length as _xs_ and _ys_ or a single value to make all markers the same size.

**c**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, sequence, or sequence of colors, optional

The marker color. Possible values:

*   A single color format string.
    
*   A sequence of colors of length n.
    
*   A sequence of n numbers to be mapped to colors using _cmap_ and _norm_.
    
*   A 2D array in which the rows are RGB or RGBA.
    

For more details see the _c_ argument of [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
.

**depthshade**bool, default: `[rcParams["axes3d.depthshade"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.depthshade#rcparam-axes3d-depthshade) ` (default: `True`)

Whether to shade the scatter markers to give the appearance of depth. Each call to `scatter()` will perform its depthshading independently.

**depthshade\_minalpha**float, default: `[rcParams["axes3d.depthshade_minalpha"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.depthshade_minalpha#rcparam-axes3d-depthshade-minalpha) ` (default: `0.3`)

The lowest alpha value applied by depth-shading.

Added in version 3.11.

**axlim\_clip**bool, default: False

Whether to hide the scatter points outside the axes view limits.

Added in version 3.10.

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_xs_, _ys_, _zs_, _s_, _edgecolors_, _c_, _facecolor_, _facecolors_, _color_

**\*\*kwargs**

All other keyword arguments are passed on to [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
.

Returns:

**paths**[`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.scatter`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-scatter "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_thumb.png)

[3D scatterplot](https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html)

3D scatterplot

![](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_simple_thumb.png)

[scatter(xs, ys, zs)](https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html)

scatter(xs, ys, zs)

On this page
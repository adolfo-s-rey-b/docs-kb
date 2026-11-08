[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.errorbar[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar.html#mpl-toolkits-mplot3d-axes3d-axes3d-errorbar "Link to this heading")

===============================================================================================================================================================================================================

Axes3D.errorbar(_x_, _y_, _z_, _zerr\=None_, _yerr\=None_, _xerr\=None_, _fmt\=''_, _barsabove\=False_, _errorevery\=1_, _ecolor\=None_, _elinewidth\=None_, _capsize\=None_, _capthick\=None_, _xlolims\=False_, _xuplims\=False_, _ylolims\=False_, _yuplims\=False_, _zlolims\=False_, _zuplims\=False_, _axlim\_clip\=False_, _\*_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3851-L4182)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar.html#mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar "Link to this definition")

Plot lines and/or markers with errorbars around them.

_x_/_y_/_z_ define the data locations, and _xerr_/_yerr_/_zerr_ define the errorbar sizes. By default, this draws the data markers/lines as well the errorbars. Use fmt='none' to draw errorbars only.

Parameters:

**x, y, z**float or array-like

The data positions.

**xerr, yerr, zerr**float or array-like, shape (N,) or (2, N), optional

The errorbar sizes:

*   scalar: Symmetric +/- values for all data points.
    
*   shape(N,): Symmetric +/-values for each data point.
    
*   shape(2, N): Separate - and + values for each bar. First row contains the lower errors, the second row contains the upper errors.
    
*   _None_: No errorbar.
    

Note that all error arrays should have _positive_ values.

**fmt**str, default: ''

The format for the data points / data lines. See [`plot`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.axes3d.Axes3D.plot")
 for details.

Use 'none' (case-insensitive) to plot errorbars without any data markers.

**ecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The color of the errorbar lines. If not given, use the color of the line connecting the markers.

**elinewidth**float, optional

The linewidth of the errorbar lines. If not given, the linewidth of the current style is used.

**capsize**float, default: `[rcParams["errorbar.capsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=errorbar.capsize#rcparam-errorbar-capsize) ` (default: `0.0`)

The length of the error bar caps in points.

**capthick**float, default: None

An alias to the keyword argument _markeredgewidth_ (a.k.a. _mew_). This setting is a more sensible name for the property that controls the thickness of the error bar cap in points. For backwards compatibility, if _mew_ or _markeredgewidth_ are given, then they will over-ride _capthick_. This may change in future releases.

**barsabove**bool, default: False

If True, will plot the errorbars above the plot symbols. Default is below.

**xlolims, ylolims, zlolims**bool, default: False

These arguments can be used to indicate that a value gives only lower limits. In that case a caret symbol is used to indicate this. _lims_\-arguments may be scalars, or array-likes of the same length as the errors. To use limits with inverted axes, [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim")
, [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim")
, or [`set_zlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim")
 must be called before [`errorbar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar.html#mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar "mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar")
. Note the tricky parameter names: setting e.g. _ylolims_ to True means that the y-value is a _lower_ limit of the True value, so, only an _upward_\-pointing arrow will be drawn!

**xuplims, yuplims, zuplims**bool, default: False

Same as above, but for controlling the upper limits.

**errorevery**int or (int, int), default: 1

draws error bars on a subset of the data. _errorevery_ =N draws error bars on the points (x\[::N\], y\[::N\], z\[::N\]). _errorevery_ =(start, N) draws error bars on the points (x\[start::N\], y\[start::N\], z\[start::N\]). e.g. _errorevery_ =(6, 3) adds error bars to the data at (x\[6\], x\[9\], x\[12\], x\[15\], ...). Used to avoid overlapping error bars when two series share x-axis values.

**axlim\_clip**bool, default: False

Whether to hide error bars that are outside the axes limits.

Added in version 3.10.

Returns:

**errlines**list

List of [`Line3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
 instances each containing an errorbar line.

**caplines**list

List of [`Line3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")
 instances each containing a capline object.

**limmarks**list

List of [`Line3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")
 instances each containing a marker with an upper or lower limit.

Other Parameters:

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_x_, _y_, _z_, _xerr_, _yerr_, _zerr_

**\*\*kwargs**

All other keyword arguments for styling errorbar lines are passed [`Line3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
.

Examples

([`Source code`](https://matplotlib.org/stable/_downloads/0fcddd4336ee39806d8d6a2bf4fbb23c/errorbar3d.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/504a9b8530abb40434ca1014a9ee2e16/errorbar3d_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/2d89bc5461eeeeda954d28c1ceea98d8/errorbar3d_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-errorbar3d_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-errorbar3d_00_00.2x.png)

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-errorbar "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar3d_thumb.png)

[3D errorbars](https://matplotlib.org/stable/gallery/mplot3d/errorbar3d.html)

3D errorbars

On this page
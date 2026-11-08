[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html#main-content)

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
    

matplotlib.axes.Axes.secondary\_yaxis[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html#matplotlib-axes-axes-secondary-yaxis "Link to this heading")

==========================================================================================================================================================================================

Axes.secondary\_yaxis(_location_, _functions\=None_, _\*_, _transform\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L608-L650)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html#matplotlib.axes.Axes.secondary_yaxis "Link to this definition")

Add a second y-axis to this [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.

This axis is typically used to display a second y-scale for the data plotted on the Axes.

Parameters:

**location**{'top', 'bottom', 'left', 'right'} or float

The position to put the secondary axis. Strings can be 'top' or 'bottom' for orientation='x' and 'right' or 'left' for orientation='y'. A float indicates the relative position on the parent Axes to put the new Axes, 0.0 being the bottom (or left) and 1.0 being the top (or right).

**functions**2-tuple of func, or Transform with an inverse

If a 2-tuple of functions, the user specifies the transform function and its inverse. i.e. `functions=(lambda x: 2 / x, lambda x: 2 / x)` would be an reciprocal transform with a factor of 2. Both functions must accept numpy arrays as input.

The user can also directly supply a subclass of [`transforms.Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 so long as it has an inverse.

See [Secondary Axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/secondary_axis.html)
 for examples of making these conversions.

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, optional

If specified, _location_ will be placed relative to this transform (in the direction of the axis) rather than the parent's axis. i.e. a secondary x-axis will use the provided y transform and the x transform of the parent.

Added in version 3.9.

Returns:

**ax**axes.\_secondary\_axes.SecondaryAxis

The returned Axes is overlaid on top of the original Axes and all components except for the complementary axis are hidden. You may modify the complementary axis, e.g. by setting ticks or an axis label. However, it is not designed to hold data, so that you should not call any plotting methods on it. Its limits are derived from the parent Axes via the specified transformation, and setting limits on the secondary axis (e.g., via `set_xlim` or `set_ylim`) has no effect.

Other Parameters:

**\*\*kwargs**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 properties.

Other miscellaneous Axes parameters.

Warning

This method is experimental as of 3.1, and the API may change.

Examples

Add a secondary Axes that converts from radians to degrees

([`Source code`](https://matplotlib.org/stable/_downloads/973bea3a76bd26c05e7e9a1f0f6d776f/matplotlib-axes-Axes-secondary_yaxis-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/41563d6fe4591dee20edd69f3f498cf9/matplotlib-axes-Axes-secondary_yaxis-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/d0babba3c2e03fc2a5fb18fee0fc42b5/matplotlib-axes-Axes-secondary_yaxis-1.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-matplotlib-axes-Axes-secondary_yaxis-1.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-matplotlib-axes-Axes-secondary_yaxis-1.2x.png)

To add a secondary axis relative to your data, you can pass a transform to the new axis.

([`Source code`](https://matplotlib.org/stable/_downloads/93cbdfd892b178b0ccf34e98144ea0f5/matplotlib-axes-Axes-secondary_yaxis-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/cd84022b11f473b21b20e92fa1c81880/matplotlib-axes-Axes-secondary_yaxis-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/54036d4227753dc9cbe531d1eb852efe/matplotlib-axes-Axes-secondary_yaxis-2.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-matplotlib-axes-Axes-secondary_yaxis-2.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-matplotlib-axes-Axes-secondary_yaxis-2.2x.png)

Examples using `matplotlib.axes.Axes.secondary_yaxis`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html#examples-using-matplotlib-axes-axes-secondary-yaxis "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_secondary_axis_thumb.png)

[Secondary Axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/secondary_axis.html)

Secondary Axis

On this page
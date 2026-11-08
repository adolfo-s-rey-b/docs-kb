[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.margins.html#main-content)

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
    

matplotlib.pyplot.margins[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.margins.html#matplotlib-pyplot-margins "Link to this heading")

========================================================================================================================================================

matplotlib.pyplot.margins(_\*margins_, _x\=None_, _y\=None_, _tight\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3856-L3863)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.margins.html#matplotlib.pyplot.margins "Link to this definition")

Set or retrieve margins around the data for autoscaling axis limits.

This allows to configure the padding around the data without having to set explicit limits using [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 / [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
.

Autoscaling determines the axis limits by adding _margin_ times the data interval as padding around the data. See the following illustration:

([`Source code`](https://matplotlib.org/stable/_downloads/ad69cec3e927b3cd3dd5828130cb83c7/axes_margins.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c13514a334ab068a54005473c27f2179/axes_margins.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/d90eb9f14ec19e4599252b9c8edefd38/axes_margins.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-axes_margins.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-axes_margins.2x.png)

All input parameters must be floats greater than -0.5. Passing both positional and keyword arguments is invalid and will raise a TypeError. If no arguments (positional or otherwise) are provided, the current margins will remain unchanged and simply be returned.

The default margins are `[rcParams["axes.xmargin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.xmargin#rcparam-axes-xmargin) ` (default: `0.05`) and `[rcParams["axes.ymargin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.ymargin#rcparam-axes-ymargin) ` (default: `0.05`).

Parameters:

**\*margins**float, optional

If a single positional argument is provided, it specifies both margins of the x-axis and y-axis limits. If two positional arguments are provided, they will be interpreted as _xmargin_, _ymargin_. If setting the margin on a single axis is desired, use the keyword arguments described below.

**x, y**float, optional

Specific margin values for the x-axis and y-axis, respectively. These cannot be used with positional arguments, but can be used individually to alter on e.g., only the y-axis.

**tight**bool or None, default: True

The _tight_ parameter is passed to [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
, which is executed after a margin is changed; the default here is _True_, on the assumption that when margins are specified, no additional padding to match tick marks is usually desired. Setting _tight_ to _None_ preserves the previous setting.

Returns:

**xmargin, ymargin**float

See also

[Margins](https://matplotlib.org/stable/users/explain/axes/autoscale.html#autoscale-margins)

[`Axes.set_xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin")
, [`Axes.set_ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin")

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
.

If a previously used Axes method such as [`pcolor()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolor.html#matplotlib.pyplot.pcolor "matplotlib.pyplot.pcolor")
 has set [`use_sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html#matplotlib.axes.Axes.use_sticky_edges "matplotlib.axes.Axes.use_sticky_edges")
 to [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, only the limits not set by the "sticky artists" will be modified. To force all margins to be set, set [`use_sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html#matplotlib.axes.Axes.use_sticky_edges "matplotlib.axes.Axes.use_sticky_edges")
 to [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
 before calling [`margins()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.margins.html#matplotlib.pyplot.margins "matplotlib.pyplot.margins")
.

Examples using `matplotlib.pyplot.margins`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.margins.html#examples-using-matplotlib-pyplot-margins "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_axes_margins_thumb.png)

[Controlling view limits using margins and sticky\_edges](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_margins.html)

Controlling view limits using margins and sticky\_edges

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#main-content)

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
    

mpl\_toolkits.axisartist.floating\_axes.GridHelperCurveLinear[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl-toolkits-axisartist-floating-axes-gridhelpercurvelinear "Link to this heading")

================================================================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.floating\_axes.GridHelperCurveLinear(_aux\_trans_, _extremes_, _grid\_locator1\=None_, _grid\_locator2\=None_, _tick\_formatter1\=None_, _tick\_formatter2\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/floating_axes.py#L128-L222)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear "Link to this definition")

Bases: [`GridHelperCurveLinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear")

Parameters:

**aux\_trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 or tuple\[Callable, Callable\]

The transform from curved coordinates to rectilinear coordinate: either a [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 instance (which provides also its inverse), or a pair of callables `(trans, inv_trans)` that define the transform and its inverse. The callables should have signature:

x\_rect, y\_rect \= trans(x\_curved, y\_curved)
x\_curved, y\_curved \= inv\_trans(x\_rect, y\_rect)

**extreme\_finder**

**grid\_locator1, grid\_locator2**

Grid locators for each axis.

**tick\_formatter1, tick\_formatter2**

Tick formatters for each axis.

get\_gridlines(_which\='major'_, _axis\='both'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/floating_axes.py#L216-L222)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.get_gridlines "Link to this definition")

Return list of grid lines as a list of paths (list of points).

Parameters:

**which**{"both", "major", "minor"}

**axis**{"both", "x", "y"}

new\_fixed\_axis(_loc_, _nth\_coord\=None_, _axis\_direction\=None_, _offset\=None_, _axes\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/floating_axes.py#L143-L157)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.new_fixed_axis "Link to this definition")

Examples using `mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#examples-using-mpl-toolkits-axisartist-floating-axes-gridhelpercurvelinear "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_thumb.png)

[floating\_axes features](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html)

floating\_axes features

On this page
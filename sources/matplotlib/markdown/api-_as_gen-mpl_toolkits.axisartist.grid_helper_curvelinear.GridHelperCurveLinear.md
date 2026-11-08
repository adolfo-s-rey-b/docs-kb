[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#main-content)

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
    

mpl\_toolkits.axisartist.grid\_helper\_curvelinear.GridHelperCurveLinear[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl-toolkits-axisartist-grid-helper-curvelinear-gridhelpercurvelinear "Link to this heading")

===============================================================================================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.grid\_helper\_curvelinear.GridHelperCurveLinear(_aux\_trans_, _extreme\_finder\=None_, _grid\_locator1\=None_, _grid\_locator2\=None_, _tick\_formatter1\=None_, _tick\_formatter2\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_helper_curvelinear.py#L276-L352)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "Link to this definition")

Bases: [`GridHelperBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.GridHelperBase.html#mpl_toolkits.axisartist.axislines.GridHelperBase "mpl_toolkits.axisartist.axislines.GridHelperBase")

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

get\_gridlines(_which\='major'_, _axis\='both'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_helper_curvelinear.py#L346-L352)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.get_gridlines "Link to this definition")

Return list of grid lines as a list of paths (list of points).

Parameters:

**which**{"both", "major", "minor"}

**axis**{"both", "x", "y"}

new\_fixed\_axis(_loc_, _\*_, _axis\_direction\=None_, _offset\=None_, _axes\=None_, _nth\_coord\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_helper_curvelinear.py#L318-L329)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.new_fixed_axis "Link to this definition")

new\_floating\_axis(_nth\_coord_, _value_, _axes\=None_, _axis\_direction\='bottom'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_helper_curvelinear.py#L331-L341)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.new_floating_axis "Link to this definition")

update\_grid\_finder(_aux\_trans\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_helper_curvelinear.py#L312-L316)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.update_grid_finder "Link to this definition")

Examples using `mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#examples-using-mpl-toolkits-axisartist-grid-helper-curvelinear-gridhelpercurvelinear "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_thumb.png)

[axis\_direction demo](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html)

axis\_direction demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid_thumb.png)

[Curvilinear grid demo](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html)

Curvilinear grid demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid2_thumb.png)

[Demo CurveLinear Grid2](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid2.html)

Demo CurveLinear Grid2

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_thumb.png)

[floating\_axes features](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html)

floating\_axes features

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axis_thumb.png)

[floating\_axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axis.html)

floating\_axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_thumb.png)

[Simple axis pad](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html)

Simple axis pad

On this page
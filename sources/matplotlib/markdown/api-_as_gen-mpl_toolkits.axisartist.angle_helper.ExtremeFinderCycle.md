[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle.html#main-content)

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
    

mpl\_toolkits.axisartist.angle\_helper.ExtremeFinderCycle[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle.html#mpl-toolkits-axisartist-angle-helper-extremefindercycle "Link to this heading")

====================================================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.angle\_helper.ExtremeFinderCycle(_nx_, _ny_, _lon\_cycle\=360.0_, _lat\_cycle\=None_, _lon\_minmax\=None_, _lat\_minmax\=(-90, 90)_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/angle_helper.py#L311-L395)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle.html#mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle "Link to this definition")

Bases: [`ExtremeFinderSimple`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.html#mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple "mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple")

This subclass handles the case where one or both coordinates should be taken modulo 360, or be restricted to not exceed a specific range.

Parameters:

**nx, ny**int

The number of samples in each direction.

**lon\_cycle, lat\_cycle**360 or None

If not None, values in the corresponding direction are taken modulo _lon\_cycle_ or _lat\_cycle_; in theory this can be any number but the implementation actually assumes that it is 360 (if not None); other values give nonsensical results.

This is done by "unwrapping" the transformed grid coordinates so that jumps are less than a half-cycle; then normalizing the span to no more than a full cycle.

For example, if values are in the union of the \[0, 2\] and \[358, 360\] intervals (typically, angles measured modulo 360), the values in the second interval are normalized to \[-2, 0\] instead so that the values now cover \[-2, 2\]. If values are in a range of \[5, 1000\], this gets normalized to \[5, 365\].

**lon\_minmax, lat\_minmax**(float, float) or None

If not None, the computed bounding box is clipped to the given range in the corresponding direction.

Examples using `mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle.html#examples-using-mpl-toolkits-axisartist-angle-helper-extremefindercycle "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_thumb.png)

[axis\_direction demo](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html)

axis\_direction demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid_thumb.png)

[Curvilinear grid demo](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html)

Curvilinear grid demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axis_thumb.png)

[floating\_axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axis.html)

floating\_axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_thumb.png)

[Simple axis pad](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html)

Simple axis pad

On this page
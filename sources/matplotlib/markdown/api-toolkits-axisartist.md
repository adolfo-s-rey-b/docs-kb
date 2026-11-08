[Skip to main content](https://matplotlib.org/stable/api/toolkits/axisartist.html#main-content)

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
    

`mpl_toolkits.axisartist`[#](https://matplotlib.org/stable/api/toolkits/axisartist.html#mpl-toolkits-axisartist "Link to this heading")

========================================================================================================================================

The _axisartist_ namespace provides a derived Axes implementation ([`Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.axislines.Axes")
), designed to support curvilinear grids. The biggest difference is that the artists that are responsible for drawing axis lines, ticks, ticklabels, and axis labels are separated out from Matplotlib's Axis class.

You can find a tutorial describing usage of axisartist at the [axisartist](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-users-guide-index)
 user guide.

[![../../_images/sphx_glr_demo_curvelinear_grid_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid_001.png)](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html)

Note

This module contains classes and function that were formerly part of the `mpl_toolkits.axes_grid` module that was removed in 3.6. Additional classes from that older module may also be found in [`mpl_toolkits.axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
.

**The submodules of the axisartist API are:**

|     |     |
| --- | --- |
| [`axisartist.angle_helper`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.html#module-mpl_toolkits.axisartist.angle_helper "mpl_toolkits.axisartist.angle_helper") |     |
| [`axisartist.axes_divider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axes_divider.html#module-mpl_toolkits.axisartist.axes_divider "mpl_toolkits.axisartist.axes_divider") |     |
| [`axisartist.axis_artist`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.html#module-mpl_toolkits.axisartist.axis_artist "mpl_toolkits.axisartist.axis_artist") | The [`axis_artist`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.html#module-mpl_toolkits.axisartist.axis_artist "mpl_toolkits.axisartist.axis_artist")<br> module implements custom artists to draw axis elements (axis lines and labels, tick lines and labels, grid lines). |
| [`axisartist.axisline_style`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axisline_style.html#module-mpl_toolkits.axisartist.axisline_style "mpl_toolkits.axisartist.axisline_style") | Provides classes to style the axis lines. |
| [`axisartist.axislines`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.html#module-mpl_toolkits.axisartist.axislines "mpl_toolkits.axisartist.axislines") | Axislines includes modified implementation of the Axes class. |
| [`axisartist.floating_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.html#module-mpl_toolkits.axisartist.floating_axes "mpl_toolkits.axisartist.floating_axes") | An experimental support for curvilinear grid. |
| [`axisartist.grid_finder`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.html#module-mpl_toolkits.axisartist.grid_finder "mpl_toolkits.axisartist.grid_finder") |     |
| [`axisartist.grid_helper_curvelinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.html#module-mpl_toolkits.axisartist.grid_helper_curvelinear "mpl_toolkits.axisartist.grid_helper_curvelinear") | An experimental support for curvilinear grid. |
| [`axisartist.parasite_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.parasite_axes.html#module-mpl_toolkits.axisartist.parasite_axes "mpl_toolkits.axisartist.parasite_axes") |     |
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.html#main-content)

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
    

mpl\_toolkits.axisartist.axislines[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.html#module-mpl_toolkits.axisartist.axislines "Link to this heading")

========================================================================================================================================================================================

Axislines includes modified implementation of the Axes class. The biggest difference is that the artists responsible for drawing the axis spine, ticks, ticklabels and axis labels are separated out from Matplotlib's Axis class. Originally, this change was motivated to support curvilinear grid. Here are a few reasons that I came up with a new axes class:

*   "top" and "bottom" x-axis (or "left" and "right" y-axis) can have different ticks (tick locations and labels). This is not possible with the current Matplotlib, although some twin axes trick can help.
    
*   Curvilinear grid.
    
*   angled ticks.
    

In the new axes class, xaxis and yaxis is set to not visible by default, and new set of artist (AxisArtist) are defined to draw axis line, ticks, ticklabels and axis label. Axes.axis attribute serves as a dictionary of these artists, i.e., ax.axis\["left"\] is an AxisArtist instance responsible to draw left y-axis. The default Axes.axis contains "bottom", "left", "top" and "right".

AxisArtist can be considered as a container artist and has the following children artists which will draw ticks, labels, etc.

*   line
    
*   major\_ticks, major\_ticklabels
    
*   minor\_ticks, minor\_ticklabels
    
*   offsetText
    
*   label
    

Note that these are separate artists from [`matplotlib.axis.Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
, thus most tick-related functions in Matplotlib won't work. For example, color and markerwidth of the `ax.axis["bottom"].major_ticks` will follow those of Axes.xaxis unless explicitly specified.

In addition to AxisArtist, the Axes will have _gridlines_ attribute, which obviously draws grid lines. The gridlines needs to be separated from the axis as some gridlines can never pass any axis.

Classes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.html#classes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.axislines.Axes")<br>(\*args\[, grid\_helper\]) | Build an Axes in a figure. |
| [`AxesZero`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.axislines.AxesZero")<br>(\*args\[, grid\_helper\]) | Build an Axes in a figure. |
| [`AxisArtistHelper`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxisArtistHelper.html#mpl_toolkits.axisartist.axislines.AxisArtistHelper "mpl_toolkits.axisartist.axislines.AxisArtistHelper")<br>() |     |
| [`AxisArtistHelperRectlinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxisArtistHelperRectlinear.html#mpl_toolkits.axisartist.axislines.AxisArtistHelperRectlinear "mpl_toolkits.axisartist.axislines.AxisArtistHelperRectlinear")<br>() |     |
| [`FixedAxisArtistHelperRectilinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.FixedAxisArtistHelperRectilinear.html#mpl_toolkits.axisartist.axislines.FixedAxisArtistHelperRectilinear "mpl_toolkits.axisartist.axislines.FixedAxisArtistHelperRectilinear")<br>(axes, loc) | `nth_coord = 0`: x-axis; `nth_coord = 1`: y-axis. |
| [`FloatingAxisArtistHelperRectilinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.FloatingAxisArtistHelperRectilinear.html#mpl_toolkits.axisartist.axislines.FloatingAxisArtistHelperRectilinear "mpl_toolkits.axisartist.axislines.FloatingAxisArtistHelperRectilinear")<br>(axes, ...) |     |
| [`GridHelperBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.GridHelperBase.html#mpl_toolkits.axisartist.axislines.GridHelperBase "mpl_toolkits.axisartist.axislines.GridHelperBase")<br>() |     |
| [`GridHelperRectlinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.GridHelperRectlinear.html#mpl_toolkits.axisartist.axislines.GridHelperRectlinear "mpl_toolkits.axisartist.axislines.GridHelperRectlinear")<br>(axes) |     |
| [`Subplot`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Subplot.html#mpl_toolkits.axisartist.axislines.Subplot "mpl_toolkits.axisartist.axislines.Subplot") |     |
| [`SubplotZero`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.SubplotZero.html#mpl_toolkits.axisartist.axislines.SubplotZero "mpl_toolkits.axisartist.axislines.SubplotZero") |     |

On this page
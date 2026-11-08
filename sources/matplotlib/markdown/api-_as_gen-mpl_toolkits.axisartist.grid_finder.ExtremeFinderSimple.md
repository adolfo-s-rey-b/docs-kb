[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.html#main-content)

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
    

mpl\_toolkits.axisartist.grid\_finder.ExtremeFinderSimple[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.html#mpl-toolkits-axisartist-grid-finder-extremefindersimple "Link to this heading")

====================================================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.grid\_finder.ExtremeFinderSimple(_nx_, _ny_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L46-L98)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.html#mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A helper class to figure out the range of grid lines that need to be drawn.

Parameters:

**nx, ny**int

The number of samples in each direction.

\_\_call\_\_(_transform\_xy_, _x1_, _y1_, _x2_, _y2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L61-L82)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.html#mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.__call__ "Link to this definition")

Compute an approximation of the bounding box obtained by applying _transform\_xy_ to the box delimited by `(x1, y1, x2, y2)`.

The intended use is to have `(x1, y1, x2, y2)` in axes coordinates, and have _transform\_xy_ be the transform from axes coordinates to data coordinates; this method then returns the range of data coordinates that span the actual axes.

The computation is done by sampling `nx * ny` equispaced points in the `(x1, y1, x2, y2)` box and finding the resulting points with extremal coordinates; then adding some padding to take into account the finite sampling.

As each sampling step covers a relative range of `1/nx` or `1/ny`, the padding is computed by expanding the span covered by the extremal coordinates by these fractions.

Examples using `mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.html#examples-using-mpl-toolkits-axisartist-grid-finder-extremefindersimple "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_thumb.png)

[axis\_direction demo](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html)

axis\_direction demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid_thumb.png)

[Curvilinear grid demo](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html)

Curvilinear grid demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid2_thumb.png)

[Demo CurveLinear Grid2](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid2.html)

Demo CurveLinear Grid2

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axis_thumb.png)

[floating\_axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axis.html)

floating\_axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_thumb.png)

[Simple axis pad](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html)

Simple axis pad

On this page
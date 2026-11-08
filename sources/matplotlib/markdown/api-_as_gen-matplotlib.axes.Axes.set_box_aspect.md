[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#main-content)

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
    

matplotlib.axes.Axes.set\_box\_aspect[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib-axes-axes-set-box-aspect "Link to this heading")

========================================================================================================================================================================================

Axes.set\_box\_aspect(_aspect\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L1872-L1907)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "Link to this definition")

Set the Axes box aspect, i.e. the ratio of height to width.

This defines the aspect of the Axes in figure space and is not to be confused with the data aspect (see [`set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
).

Parameters:

**aspect**float or None

Changes the physical dimensions of the Axes, such that the ratio of the Axes height to the Axes width in physical units is equal to _aspect_. Defining a box aspect will change the _adjustable_ property to 'datalim' (see [`set_adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable")
).

_None_ will disable a fixed box aspect so that height and width of the Axes are chosen independently.

See also

[`matplotlib.axes.Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")

for a description of aspect handling.

Examples using `matplotlib.axes.Axes.set_box_aspect`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#examples-using-matplotlib-axes-axes-set-box-aspect "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_thumb.png)

[Axes box aspect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html)

Axes box aspect

![](https://matplotlib.org/stable/_images/sphx_glr_box3d_thumb.png)

[3D box surface plot](https://matplotlib.org/stable/gallery/mplot3d/box3d.html)

3D box surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_axes_thumb.gif)

[Multiple Axes animation](https://matplotlib.org/stable/gallery/animation/multiple_axes.html)

Multiple Axes animation

On this page
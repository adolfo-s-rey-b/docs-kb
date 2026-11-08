[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#main-content)

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
    

matplotlib.axes.Axes.indicate\_inset\_zoom[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib-axes-axes-indicate-inset-zoom "Link to this heading")

=======================================================================================================================================================================================================

Axes.indicate\_inset\_zoom(_inset\_ax_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L514-L552)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib.axes.Axes.indicate_inset_zoom "Link to this definition")

Add an inset indicator rectangle to the Axes based on the axis limits for an _inset\_ax_ and draw connectors between _inset\_ax_ and the rectangle.

Parameters:

**inset\_ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Inset Axes to draw connecting lines to. Two lines are drawn connecting the indicator box to the inset Axes on corners chosen so as to not overlap with the indicator box.

**\*\*kwargs**

Other keyword arguments are passed on to [`Axes.indicate_inset`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html#matplotlib.axes.Axes.indicate_inset "matplotlib.axes.Axes.indicate_inset")

Returns:

**inset\_indicator**[`inset.InsetIndicator`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator "matplotlib.inset.InsetIndicator")

An artist which contains

inset\_indicator.rectangle[`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")

The indicator frame.

inset\_indicator.connectors4-tuple of [`patches.ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")

The four connector lines connecting to (lower\_left, upper\_left, lower\_right upper\_right) corners of _inset\_ax_. Two lines are set with visibility to _False_, but the user can set the visibility to True if the automatic choice is not deemed correct.

Changed in version 3.10: Previously the rectangle and connectors tuple were returned.

Warning

This method is experimental as of 3.0, and the API may change.

Examples using `matplotlib.axes.Axes.indicate_inset_zoom`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#examples-using-matplotlib-axes-axes-indicate-inset-zoom "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_thumb.png)

[Streamplot](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot

![](https://matplotlib.org/stable/_images/sphx_glr_zoom_inset_axes_thumb.png)

[Zoom region inset Axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html)

Zoom region inset Axes

On this page
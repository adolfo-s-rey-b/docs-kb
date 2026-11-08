[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#main-content)

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
    

matplotlib.axes.Axes.set\_position[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib-axes-axes-set-position "Link to this heading")

=================================================================================================================================================================================

Axes.set\_position(_pos_, _which\='both'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L1176-L1211)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "Link to this definition")

Set the Axes position.

Axes have two position attributes. The 'original' position is the position allocated for the Axes. The 'active' position is the position the Axes is actually drawn at. These positions are usually the same unless a fixed aspect is set to the Axes. See [`Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
 for details.

Parameters:

**pos**\[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")

The new position of the Axes in [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 coordinates.

**which**{'both', 'active', 'original'}, default: 'both'

Determines which position variables to change.

Note

This parameter is considered internal. End users should not use it.

For native Matplotlib [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, the active position is determined by a combination of the original position and the aspect ratio. Any active position set by the user will therefore be overwritten by internal handling. This option is retained as it may be relevant for some third party [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclasses.

See also

[`matplotlib.transforms.Bbox.from_bounds`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_bounds "matplotlib.transforms.Bbox.from_bounds")

[`matplotlib.transforms.Bbox.from_extents`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_extents "matplotlib.transforms.Bbox.from_extents")

Examples using `matplotlib.axes.Axes.set_position`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#examples-using-matplotlib-axes-axes-set-position "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_contour_demo_thumb.png)

[Contour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html)

Contour Demo

On this page
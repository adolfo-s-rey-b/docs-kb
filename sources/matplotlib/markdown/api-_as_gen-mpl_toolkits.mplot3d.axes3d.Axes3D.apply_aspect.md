[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.apply\_aspect[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect.html#mpl-toolkits-mplot3d-axes3d-axes3d-apply-aspect "Link to this heading")

============================================================================================================================================================================================================================

Axes3D.apply\_aspect(_position\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L457-L472)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect "Link to this definition")

Adjust the Axes for a specified data aspect ratio.

Depending on [`get_adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_adjustable.html#matplotlib.axes.Axes.get_adjustable "matplotlib.axes.Axes.get_adjustable")
 this will modify either the Axes box (position) or the view limits. In the former case, [`get_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_anchor.html#matplotlib.axes.Axes.get_anchor "matplotlib.axes.Axes.get_anchor")
 will affect the position.

Parameters:

**position**None or .Bbox

Note

This parameter exists for historic reasons and is considered internal. End users should not use it.

If not `None`, this defines the position of the Axes within the figure as a Bbox. See [`get_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_position.html#matplotlib.axes.Axes.get_position "matplotlib.axes.Axes.get_position")
 for further details.

See also

[`matplotlib.axes.Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")

For a description of aspect ratio handling.

[`matplotlib.axes.Axes.set_adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable")

Set how the Axes adjusts to achieve the required aspect ratio.

[`matplotlib.axes.Axes.set_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor")

Set the position in case of extra space.

[`matplotlib.figure.Figure.draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")

Update all stale components of a figure.

Notes

This is called automatically when each Axes is drawn. You may need to call it yourself if you need to update the Axes position and/or view limits before the Figure is drawn.

An alternative with a broader scope is [`Figure.draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")
, which updates all stale components of a figure, not only the positioning / view limits of a single Axes.

Examples

A typical usage example would be the following. [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 sets the aspect to 1, but adapting the Axes position and extent to reflect this is deferred until rendering for performance reasons. If you want to know the Axes size before, you need to call [`apply_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect")
 to get the correct values.

\>>> fig, ax \= plt.subplots()
\>>> ax.imshow(np.zeros((3, 3)))
\>>> ax.bbox.width, ax.bbox.height
(496.0, 369.59999999999997)
\>>> ax.apply\_aspect()
\>>> ax.bbox.width, ax.bbox.height
(369.59999999999997, 369.59999999999997)

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_box\_aspect[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-box-aspect "Link to this heading")

===================================================================================================================================================================================================================================

Axes3D.set\_box\_aspect(_aspect_, _\*_, _zoom\=1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L416-L455)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect "Link to this definition")

Set the Axes box aspect.

The box aspect is the ratio of height to width in display units for each face of the box when viewed perpendicular to that face. This is not to be confused with the data aspect (see [`set_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect")
). The default ratios are 4:4:3 (x:y:z).

To simulate having equal aspect in data space, set the box aspect to match your data range in each dimension.

_zoom_ controls the overall size of the Axes3D in the figure.

Parameters:

**aspect**3-tuple of floats or None

Changes the physical dimensions of the Axes3D, such that the ratio of the axis lengths in display units is x:y:z. If None, defaults to (4, 4, 3).

**zoom**float, default: 1

Control overall size of the Axes3D in the figure. Must be > 0.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-set-box-aspect "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_box3d_thumb.png)

[3D box surface plot](https://matplotlib.org/stable/gallery/mplot3d/box3d.html)

3D box surface plot

On this page
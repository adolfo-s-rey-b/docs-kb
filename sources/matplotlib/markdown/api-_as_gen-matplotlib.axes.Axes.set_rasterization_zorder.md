[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#main-content)

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
    

matplotlib.axes.Axes.set\_rasterization\_zorder[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib-axes-axes-set-rasterization-zorder "Link to this heading")

======================================================================================================================================================================================================================

Axes.set\_rasterization\_zorder(_z_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L3014-L3032)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "Link to this definition")

Set the zorder threshold for rasterization for vector graphics output.

All artists with a zorder below the given value will be rasterized if they support rasterization.

This setting is ignored for pixel-based output.

See also [Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)
.

Parameters:

**z**float or None

The zorder below which artists are rasterized. If `None` rasterization based on zorder is deactivated.

Examples using `matplotlib.axes.Axes.set_rasterization_zorder`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#examples-using-matplotlib-axes-axes-set-rasterization-zorder "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_rasterization_demo_thumb.png)

[Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)

Rasterization for vector graphics

On this page
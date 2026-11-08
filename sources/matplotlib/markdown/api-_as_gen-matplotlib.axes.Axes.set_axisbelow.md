[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#main-content)

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
    

matplotlib.axes.Axes.set\_axisbelow[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib-axes-axes-set-axisbelow "Link to this heading")

====================================================================================================================================================================================

Axes.set\_axisbelow(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L3426-L3463)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "Link to this definition")

Set whether axis ticks and gridlines are above or below most artists.

This controls the zorder of the ticks and gridlines. For more information on the zorder see [Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)
.

Parameters:

**b**bool or 'line'

Possible values:

*   _True_ (zorder = 0.5): Ticks and gridlines are below patches and lines, though still above images.
    
*   'line' (zorder = 1.5): Ticks and gridlines are above patches (e.g. rectangles, with default zorder = 1) but still below lines and markers (with their default zorder = 2).
    
*   _False_ (zorder = 2.5): Ticks and gridlines are above patches and lines / markers.
    

See also

[`get_axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_axisbelow.html#matplotlib.axes.Axes.get_axisbelow "matplotlib.axes.Axes.get_axisbelow")

Notes

For more control, call the [`set_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder")
 method of each axis.

On this page
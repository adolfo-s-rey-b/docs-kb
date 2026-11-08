[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylim.html#main-content)

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
    

matplotlib.axes.Axes.get\_ylim[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylim.html#matplotlib-axes-axes-get-ylim "Link to this heading")

=====================================================================================================================================================================

Axes.get\_ylim()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L4143-L4163)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylim.html#matplotlib.axes.Axes.get_ylim "Link to this definition")

Return the y-axis view limits.

Returns:

**bottom, top**(float, float)

The current y-axis limits in data coordinates.

See also

[`Axes.set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")

[`Axes.set_ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound")
, [`Axes.get_ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ybound.html#matplotlib.axes.Axes.get_ybound "matplotlib.axes.Axes.get_ybound")

[`Axes.invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis")
, [`Axes.yaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis_inverted.html#matplotlib.axes.Axes.yaxis_inverted "matplotlib.axes.Axes.yaxis_inverted")

Notes

The y-axis may be inverted, in which case the _bottom_ value will be greater than the _top_ value.

On this page
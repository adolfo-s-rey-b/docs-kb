[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.update_datalim.html#main-content)

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
    

matplotlib.axes.Axes.update\_datalim[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.update_datalim.html#matplotlib-axes-axes-update-datalim "Link to this heading")

=======================================================================================================================================================================================

Axes.update\_datalim(_xys_, _updatex\=True_, _updatey\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L2697-L2720)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.update_datalim.html#matplotlib.axes.Axes.update_datalim "Link to this definition")

Extend the [`dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
 Bbox to include the given points.

If no data is set currently, the Bbox will ignore its limits and set the bound to be the bounds of the xydata (_xys_). Otherwise, it will compute the bounds of the union of its current data and the data in _xys_.

Parameters:

**xys**2D array-like

The points to include in the data limits Bbox. This can be either a list of (x, y) tuples or a (N, 2) array.

**updatex, updatey**bool, default: True

Whether to update the x/y limits.

On this page
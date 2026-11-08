[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_text2_transform.html#main-content)

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
    

matplotlib.axes.Axes.get\_xaxis\_text2\_transform[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_text2_transform.html#matplotlib-axes-axes-get-xaxis-text2-transform "Link to this heading")

==========================================================================================================================================================================================================================

Axes.get\_xaxis\_text2\_transform(_pad\_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L1038-L1063)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_text2_transform.html#matplotlib.axes.Axes.get_xaxis_text2_transform "Link to this definition")

Returns:

**transform**Transform

The transform used for drawing secondary x-axis labels, which will add _pad\_points_ of padding (in points) between the axis and the label. The x-direction is in data coordinates and the y-direction is in axis coordinates

**valign**{'center', 'top', 'bottom', 'baseline', 'center\_baseline'}

The text vertical alignment.

**halign**{'center', 'left', 'right'}

The text horizontal alignment.

Notes

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

On this page
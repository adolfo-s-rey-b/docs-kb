[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_transform.html#main-content)

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
    

matplotlib.axes.Axes.get\_yaxis\_transform[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_transform.html#matplotlib-axes-axes-get-yaxis-transform "Link to this heading")

=======================================================================================================================================================================================================

Axes.get\_yaxis\_transform(_which\='grid'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L1065-L1091)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_transform.html#matplotlib.axes.Axes.get_yaxis_transform "Link to this definition")

Get the transformation used for drawing y-axis labels, ticks and gridlines. The x-direction is in axis coordinates and the y-direction is in data coordinates.

Note

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

Parameters:

**which**{'grid', 'tick1', 'tick2'}

Examples using `matplotlib.axes.Axes.get_yaxis_transform`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_transform.html#examples-using-matplotlib-axes-axes-get-yaxis-transform "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_centered_spines_with_arrows_thumb.png)

[Centered spines with arrows](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html)

Centered spines with arrows

On this page
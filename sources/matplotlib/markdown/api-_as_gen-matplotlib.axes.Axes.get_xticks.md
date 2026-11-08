[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticks.html#main-content)

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
    

matplotlib.axes.Axes.get\_xticks[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticks.html#matplotlib-axes-axes-get-xticks "Link to this heading")

===========================================================================================================================================================================

Axes.get\_xticks(_\*_, _minor\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L74-L75)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticks.html#matplotlib.axes.Axes.get_xticks "Link to this definition")

Return the xaxis' tick locations in data coordinates.

The locations are not clipped to the current axis limits and hence may contain locations that are not visible in the output.

Parameters:

**minor**bool, default: False

True to return the minor tick directions, False to return the major tick directions.

Returns:

array of tick locations

On this page
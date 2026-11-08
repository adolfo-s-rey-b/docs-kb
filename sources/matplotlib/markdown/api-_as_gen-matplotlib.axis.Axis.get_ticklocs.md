[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklocs.html#main-content)

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
    

matplotlib.axis.Axis.get\_ticklocs[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklocs.html#matplotlib-axis-axis-get-ticklocs "Link to this heading")

=================================================================================================================================================================================

Axis.get\_ticklocs(_\*_, _minor\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L1693-L1710)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklocs.html#matplotlib.axis.Axis.get_ticklocs "Link to this definition")

Return this Axis' tick locations in data coordinates.

The locations are not clipped to the current axis limits and hence may contain locations that are not visible in the output.

Parameters:

**minor**bool, default: False

True to return the minor tick directions, False to return the major tick directions.

Returns:

array of tick locations

On this page
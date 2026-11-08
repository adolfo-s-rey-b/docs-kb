[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tightbbox.html#main-content)

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
    

matplotlib.axis.Axis.get\_tightbbox[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tightbbox.html#matplotlib-axis-axis-get-tightbbox "Link to this heading")

====================================================================================================================================================================================

Axis.get\_tightbbox(_renderer\=None_, _\*_, _for\_layout\_only\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L1411-L1459)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tightbbox.html#matplotlib.axis.Axis.get_tightbbox "Link to this definition")

Return a bounding box that encloses the axis. It only accounts tick labels, axis label, and offsetText.

If _for\_layout\_only_ is True, then the width of the label (if this is an x-axis) or the height of the label (if this is a y-axis) is collapsed to near zero. This allows tight/constrained\_layout to ignore too-long labels when doing their layout.

On this page
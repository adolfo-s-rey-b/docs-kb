[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_view_interval.html#main-content)

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
    

matplotlib.axis.Axis.set\_view\_interval[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_view_interval.html#matplotlib-axis-axis-set-view-interval "Link to this heading")

=================================================================================================================================================================================================

Axis.set\_view\_interval(_vmin_, _vmax_, _ignore\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L1172-L1185)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_view_interval.html#matplotlib.axis.Axis.set_view_interval "Link to this definition")

Set the axis view limits. This method is for internal use; Matplotlib users should typically use e.g. [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 or [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
.

If _ignore_ is False (the default), this method will never reduce the preexisting view limits, only expand them if _vmin_ or _vmax_ are not within them. Moreover, the order of _vmin_ and _vmax_ does not matter; the orientation of the axis will not change.

If _ignore_ is True, the view limits will be set exactly to `(vmin, vmax)` in that order.

On this page
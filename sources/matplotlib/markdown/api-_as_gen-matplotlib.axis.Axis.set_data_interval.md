[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_data_interval.html#main-content)

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
    

matplotlib.axis.Axis.set\_data\_interval[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_data_interval.html#matplotlib-axis-axis-set-data-interval "Link to this heading")

=================================================================================================================================================================================================

Axis.set\_data\_interval(_vmin_, _vmax_, _ignore\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L1191-L1203)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_data_interval.html#matplotlib.axis.Axis.set_data_interval "Link to this definition")

Set the axis data limits. This method is for internal use.

If _ignore_ is False (the default), this method will never reduce the preexisting data limits, only expand them if _vmin_ or _vmax_ are not within them. Moreover, the order of _vmin_ and _vmax_ does not matter; the orientation of the axis will not change.

If _ignore_ is True, the data limits will be set exactly to `(vmin, vmax)` in that order.

On this page
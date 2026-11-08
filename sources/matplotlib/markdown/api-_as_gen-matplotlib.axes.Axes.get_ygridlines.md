[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ygridlines.html#main-content)

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
    

matplotlib.axes.Axes.get\_ygridlines[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ygridlines.html#matplotlib-axes-axes-get-ygridlines "Link to this heading")

=======================================================================================================================================================================================

Axes.get\_ygridlines()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L74-L75)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ygridlines.html#matplotlib.axes.Axes.get_ygridlines "Link to this definition")

Return the yaxis' grid lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.

Warning

Ticks and their constituent parts, including grid lines, are not persistent. Various operations can create, delete, and modify the tick instances; see [Tick objects](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#axes-tick-objects)
.

You should generally use [`Axis.set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 / [`Axis.get_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib.axis.Axis.get_tick_params "matplotlib.axis.Axis.get_tick_params")
 to define and query grid styling; see [Styling ticks (tick parameters)](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#axes-ticks-styling)
.

On this page
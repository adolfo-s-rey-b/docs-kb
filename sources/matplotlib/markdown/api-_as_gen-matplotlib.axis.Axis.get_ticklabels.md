[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#main-content)

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
    

matplotlib.axis.Axis.get\_ticklabels[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib-axis-axis-get-ticklabels "Link to this heading")

=======================================================================================================================================================================================

Axis.get\_ticklabels(_minor\=False_, _which\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L1574-L1612)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "Link to this definition")

Get this Axis' tick labels.

Warning

Ticks and their constituent parts, including tick labels, are not persistent. Various operations can create, delete, and modify the tick instances; see [Tick objects](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#axes-tick-objects)
.

You should generally use [`Axis.set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 / [`Axis.get_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib.axis.Axis.get_tick_params "matplotlib.axis.Axis.get_tick_params")
 to define and query tick styling; see [Styling ticks (tick parameters)](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#axes-ticks-styling)
.

Parameters:

**minor**bool

Whether to return the minor or the major ticklabels.

**which**None, ('minor', 'major', 'both')

Overrides _minor_.

Selects which ticklabels to return

Returns:

list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

On this page
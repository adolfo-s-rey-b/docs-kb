[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#main-content)

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
    

matplotlib.axes.Axes.set\_ybound[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib-axes-axes-set-ybound "Link to this heading")

===========================================================================================================================================================================

Axes.set\_ybound(_lower\=None_, _upper\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L4109-L4141)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "Link to this definition")

Set the lower and upper numerical bounds of the y-axis.

This method will honor axis inversion regardless of parameter order. It will not change the autoscaling setting ([`get_autoscaley_on()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscaley_on.html#matplotlib.axes.Axes.get_autoscaley_on "matplotlib.axes.Axes.get_autoscaley_on")
).

Parameters:

**lower, upper**float or None

> The lower and upper bounds. If _None_, the respective axis bound is not modified.

See also

[`get_ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ybound.html#matplotlib.axes.Axes.get_ybound "matplotlib.axes.Axes.get_ybound")

[`get_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylim.html#matplotlib.axes.Axes.get_ylim "matplotlib.axes.Axes.get_ylim")
, [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")

[`invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis")
, [`yaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis_inverted.html#matplotlib.axes.Axes.yaxis_inverted "matplotlib.axes.Axes.yaxis_inverted")

On this page
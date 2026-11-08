[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#main-content)

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
    

matplotlib.axes.Axes.set\_xbound[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib-axes-axes-set-xbound "Link to this heading")

===========================================================================================================================================================================

Axes.set\_xbound(_lower\=None_, _upper\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L3841-L3873)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "Link to this definition")

Set the lower and upper numerical bounds of the x-axis.

This method will honor axis inversion regardless of parameter order. It will not change the autoscaling setting ([`get_autoscalex_on()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscalex_on.html#matplotlib.axes.Axes.get_autoscalex_on "matplotlib.axes.Axes.get_autoscalex_on")
).

Parameters:

**lower, upper**float or None

The lower and upper bounds. If _None_, the respective axis bound is not modified.

See also

[`get_xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xbound.html#matplotlib.axes.Axes.get_xbound "matplotlib.axes.Axes.get_xbound")

[`get_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#matplotlib.axes.Axes.get_xlim "matplotlib.axes.Axes.get_xlim")
, [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")

[`invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_xaxis.html#matplotlib.axes.Axes.invert_xaxis "matplotlib.axes.Axes.invert_xaxis")
, [`xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_inverted.html#matplotlib.axes.Axes.xaxis_inverted "matplotlib.axes.Axes.xaxis_inverted")

On this page
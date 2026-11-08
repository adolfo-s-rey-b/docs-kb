[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_xbound[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-xbound "Link to this heading")

======================================================================================================================================================================================================================

Axes3D.set\_xbound(_lower\=None_, _upper\=None_, _view\_margin\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L777-L800)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound "Link to this definition")

Set the lower and upper numerical bounds of the x-axis.

This method will honor axis inversion regardless of parameter order. It will not change the autoscaling setting ([`get_autoscalex_on()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscalex_on.html#matplotlib.axes.Axes.get_autoscalex_on "matplotlib.axes.Axes.get_autoscalex_on")
).

Parameters:

**lower, upper**float or None

The lower and upper bounds. If _None_, the respective axis bound is not modified.

**view\_margin**float or None

The margin to apply to the bounds. If _None_, the margin is handled by [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim")
.

See also

[`get_xbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound")

[`get_xlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim")
, [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim")

[`invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis")
, [`xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted")

On this page
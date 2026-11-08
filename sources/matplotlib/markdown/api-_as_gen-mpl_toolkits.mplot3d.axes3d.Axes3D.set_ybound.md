[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_ybound[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-ybound "Link to this heading")

======================================================================================================================================================================================================================

Axes3D.set\_ybound(_lower\=None_, _upper\=None_, _view\_margin\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L802-L825)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound "Link to this definition")

Set the lower and upper numerical bounds of the y-axis.

This method will honor axis inversion regardless of parameter order. It will not change the autoscaling setting ([`get_autoscaley_on()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscaley_on.html#matplotlib.axes.Axes.get_autoscaley_on "matplotlib.axes.Axes.get_autoscaley_on")
).

Parameters:

**lower, upper**float or None

The lower and upper bounds. If _None_, the respective axis bound is not modified.

**view\_margin**float or None

The margin to apply to the bounds. If _None_, the margin is handled by [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim")
.

See also

[`get_ybound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound")

[`get_ylim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim")
, [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim")

[`invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis")
, [`yaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted")

On this page
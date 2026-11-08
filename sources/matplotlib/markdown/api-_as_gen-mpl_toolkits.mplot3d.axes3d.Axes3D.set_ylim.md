[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_ylim[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-ylim "Link to this heading")

================================================================================================================================================================================================================

Axes3D.set\_ylim(_bottom\=None_, _top\=None_, _\*_, _emit\=True_, _auto\=False_, _view\_margin\=None_, _ymin\=None_, _ymax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L973-L1044)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "Link to this definition")

Set the 3D y-axis view limits.

Parameters:

**bottom**float, optional

The bottom ylim in data coordinates. Passing _None_ leaves the limit unchanged.

The bottom and top ylims may also be passed as the tuple (_bottom_, _top_) as the first positional argument (or as the _bottom_ keyword argument).

**top**float, optional

The top ylim in data coordinates. Passing _None_ leaves the limit unchanged.

**emit**bool, default: True

Whether to notify observers of limit change.

**auto**bool or None, default: False

Whether to turn on autoscaling of the y-axis. _True_ turns on, _False_ turns off, _None_ leaves unchanged.

**view\_margin**float, optional

The additional margin to apply to the limits.

**ymin, ymax**float, optional

They are equivalent to bottom and top respectively, and it is an error to pass both _ymin_ and _bottom_ or _ymax_ and _top_.

Returns:

**bottom, top**(float, float)

The new y-axis limits in data coordinates.

See also

[`get_ylim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim")

[`set_ybound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound")
, [`get_ybound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound")

[`invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis")
, [`yaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted")

Notes

The _bottom_ value may be greater than the _top_ value, in which case the y-axis values will decrease from _bottom_ to _top_.

Examples

\>>> set\_ylim(bottom, top)
\>>> set\_ylim((bottom, top))
\>>> bottom, top \= set\_ylim(bottom, top)

One limit may be left unchanged.

\>>> set\_ylim(top\=top\_lim)

Limits may be passed in reverse order to flip the direction of the y-axis. For example, suppose `y` represents depth of the ocean in m. The y-axis limits might be set like the following so 5000 m depth is at the bottom of the plot and the surface, 0 m, is at the top.

\>>> set\_ylim(5000, 0)

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-set-ylim "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_pathpatch3d_thumb.png)

[Draw flat objects in 3D plot](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html)

Draw flat objects in 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_text3d_thumb.png)

[Text annotations in 3D](https://matplotlib.org/stable/gallery/mplot3d/text3d.html)

Text annotations in 3D

On this page
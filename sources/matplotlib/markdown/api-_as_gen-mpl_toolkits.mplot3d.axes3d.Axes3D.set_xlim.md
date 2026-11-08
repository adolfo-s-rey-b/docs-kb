[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_xlim[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-xlim "Link to this heading")

================================================================================================================================================================================================================

Axes3D.set\_xlim(_left\=None_, _right\=None_, _\*_, _emit\=True_, _auto\=False_, _view\_margin\=None_, _xmin\=None_, _xmax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L900-L971)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "Link to this definition")

Set the 3D x-axis view limits.

Parameters:

**left**float, optional

The left xlim in data coordinates. Passing _None_ leaves the limit unchanged.

The left and right xlims may also be passed as the tuple (_left_, _right_) as the first positional argument (or as the _left_ keyword argument).

**right**float, optional

The right xlim in data coordinates. Passing _None_ leaves the limit unchanged.

**emit**bool, default: True

Whether to notify observers of limit change.

**auto**bool or None, default: False

Whether to turn on autoscaling of the x-axis. _True_ turns on, _False_ turns off, _None_ leaves unchanged.

**view\_margin**float, optional

The additional margin to apply to the limits.

**xmin, xmax**float, optional

They are equivalent to left and right respectively, and it is an error to pass both _xmin_ and _left_ or _xmax_ and _right_.

Returns:

**left, right**(float, float)

The new x-axis limits in data coordinates.

See also

[`get_xlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim")

[`set_xbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound")
, [`get_xbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound")

[`invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis")
, [`xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted")

Notes

The _left_ value may be greater than the _right_ value, in which case the x-axis values will decrease from _left_ to _right_.

Examples

\>>> set\_xlim(left, right)
\>>> set\_xlim((left, right))
\>>> left, right \= set\_xlim(left, right)

One limit may be left unchanged.

\>>> set\_xlim(right\=right\_lim)

Limits may be passed in reverse order to flip the direction of the x-axis. For example, suppose `x` represents depth of the ocean in m. The x-axis limits might be set like the following so 5000 m depth is at the left of the plot and the surface, 0 m, is at the right.

\>>> set\_xlim(5000, 0)

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-set-xlim "Link to this heading")

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
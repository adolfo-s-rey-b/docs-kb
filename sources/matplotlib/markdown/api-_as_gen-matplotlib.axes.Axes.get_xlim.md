[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#main-content)

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
    

matplotlib.axes.Axes.get\_xlim[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#matplotlib-axes-axes-get-xlim "Link to this heading")

=====================================================================================================================================================================

Axes.get\_xlim()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L3875-L3895)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#matplotlib.axes.Axes.get_xlim "Link to this definition")

Return the x-axis view limits.

Returns:

**left, right**(float, float)

The current x-axis limits in data coordinates.

See also

[`Axes.set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")

[`Axes.set_xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound")
, [`Axes.get_xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xbound.html#matplotlib.axes.Axes.get_xbound "matplotlib.axes.Axes.get_xbound")

[`Axes.invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_xaxis.html#matplotlib.axes.Axes.invert_xaxis "matplotlib.axes.Axes.invert_xaxis")
, [`Axes.xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_inverted.html#matplotlib.axes.Axes.xaxis_inverted "matplotlib.axes.Axes.xaxis_inverted")

Notes

The x-axis may be inverted, in which case the _left_ value will be greater than the _right_ value.

Examples using `matplotlib.axes.Axes.get_xlim`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#examples-using-matplotlib-axes-axes-get-xlim "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_animate_decay_thumb.gif)

[Decay](https://matplotlib.org/stable/gallery/animation/animate_decay.html)

Decay

On this page
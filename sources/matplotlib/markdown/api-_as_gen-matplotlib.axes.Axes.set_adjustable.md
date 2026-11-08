[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#main-content)

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
    

matplotlib.axes.Axes.set\_adjustable[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib-axes-axes-set-adjustable "Link to this heading")

=======================================================================================================================================================================================

Axes.set\_adjustable(_adjustable_, _share\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L1805-L1854)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "Link to this definition")

Set how the Axes adjusts to achieve the required aspect ratio.

Parameters:

**adjustable**{'box', 'datalim'}

If 'box', change the physical dimensions of the Axes. If 'datalim', change the `x` or `y` data limits. This may ignore explicitly defined axis limits.

**share**bool, default: False

If `True`, apply the settings to all shared Axes.

See also

[`matplotlib.axes.Axes.get_adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_adjustable.html#matplotlib.axes.Axes.get_adjustable "matplotlib.axes.Axes.get_adjustable")

Return the current value of _adjustable_.

[`matplotlib.axes.Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")

For a description of aspect handling.

Notes

Shared Axes (of which twinned Axes are a special case) impose restrictions on how aspect ratios can be imposed. For twinned Axes, use 'datalim'. For Axes that share both x and y, use 'box'. Otherwise, either 'datalim' or 'box' may be used. These limitations are partly a requirement to avoid over-specification, and partly a result of the particular implementation we are currently using, in which the adjustments for aspect ratios are done sequentially and independently on each Axes as it is drawn.

Examples using `matplotlib.axes.Axes.set_adjustable`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#examples-using-matplotlib-axes-axes-set-adjustable "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_aspect_loglog_thumb.png)

[Loglog aspect](https://matplotlib.org/stable/gallery/scales/aspect_loglog.html)

Loglog aspect

On this page
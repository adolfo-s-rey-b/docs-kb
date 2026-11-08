[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.label_outer.html#main-content)

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
    

matplotlib.axes.Axes.label\_outer[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.label_outer.html#matplotlib-axes-axes-label-outer "Link to this heading")

==============================================================================================================================================================================

Axes.label\_outer(_remove\_inner\_ticks\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L4973-L4991)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.label_outer.html#matplotlib.axes.Axes.label_outer "Link to this definition")

Only show "outer" labels and tick labels.

x-labels are only kept for subplots on the last row (or first row, if labels are on the top side); y-labels only for subplots on the first column (or last column, if labels are on the right side).

Parameters:

**remove\_inner\_ticks**bool, default: False

If True, remove the inner ticks as well (not only tick labels).

Added in version 3.8.

Examples using `matplotlib.axes.Axes.label_outer`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.label_outer.html#examples-using-matplotlib-axes-axes-label-outer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_alpha_thumb.png)

[fill\_between with transparency](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html)

fill\_between with transparency

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_cumulative_thumb.png)

[Cumulative distributions](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html)

Cumulative distributions

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#main-content)

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
    

matplotlib.axis.Axis.grid[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#matplotlib-axis-axis-grid "Link to this heading")

========================================================================================================================================================

Axis.grid(_visible\=None_, _which\='major'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L1844-L1884)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#matplotlib.axis.Axis.grid "Link to this definition")

Configure the grid lines.

Parameters:

**visible**bool or None

Whether to show the grid lines. If any _kwargs_ are supplied, it is assumed you want the grid on and _visible_ will be set to True.

If _visible_ is _None_ and there are no _kwargs_, this toggles the visibility of the lines.

**which**{'major', 'minor', 'both'}

The grid lines to apply the changes on.

**\*\*kwargs**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 properties

Define the line properties of the grid, e.g.:

grid(color\='r', linestyle\='-', linewidth\=2)

Examples using `matplotlib.axis.Axis.grid`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#examples-using-matplotlib-axis-axis-grid "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_vs_violin_thumb.png)

[Box plot vs. violin plot comparison](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html)

Box plot vs. violin plot comparison

![](https://matplotlib.org/stable/_images/sphx_glr_log_demo_thumb.png)

[Log scale](https://matplotlib.org/stable/gallery/scales/log_demo.html)

Log scale

![](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_thumb.png)

[Symlog scale](https://matplotlib.org/stable/gallery/scales/symlog_demo.html)

Symlog scale

On this page
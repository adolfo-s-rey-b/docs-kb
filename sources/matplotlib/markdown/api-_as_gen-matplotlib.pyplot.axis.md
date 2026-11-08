[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#main-content)

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
    

matplotlib.pyplot.axis[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib-pyplot-axis "Link to this heading")

===============================================================================================================================================

matplotlib.pyplot.axis(_arg\=None_, _/_, _\*_, _emit\=True_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3089-L3097)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "Link to this definition")

Convenience method to get or set some axis properties.

Call signatures:

xmin, xmax, ymin, ymax \= axis()
xmin, xmax, ymin, ymax \= axis(\[xmin, xmax, ymin, ymax\])
xmin, xmax, ymin, ymax \= axis(option)
xmin, xmax, ymin, ymax \= axis(\*\*kwargs)

Parameters:

**xmin, xmax, ymin, ymax**float, optional

The axis limits to be set. This can also be achieved using

ax.set(xlim\=(xmin, xmax), ylim\=(ymin, ymax))

**option**bool or str

If a bool, turns axis lines and labels on or off. If a string, possible values are:

| Value | Description |
| --- | --- |
| 'off' or [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)") | Hide all axis decorations, i.e. axis labels, spines, tick marks, tick labels, and grid lines. This is the same as [`set_axis_off()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")<br>. |
| 'on' or [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)") | Do not hide all axis decorations, i.e. axis labels, spines, tick marks, tick labels, and grid lines. This is the same as [`set_axis_on()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_on.html#matplotlib.axes.Axes.set_axis_on "matplotlib.axes.Axes.set_axis_on")<br>. |
| 'equal' | Set equal scaling (i.e., make circles circular) by changing the axis limits. This is the same as `ax.set_aspect('equal', adjustable='datalim')`. Explicit data limits may not be respected in this case. |
| 'scaled' | Set equal scaling (i.e., make circles circular) by changing dimensions of the plot box. This is the same as `ax.set_aspect('equal', adjustable='box', anchor='C')`. Additionally, further autoscaling will be disabled. |
| 'tight' | Set limits just large enough to show all data, then disable further autoscaling. |
| 'auto' | Automatic scaling (fill plot box with data). |
| 'image' | 'scaled' with axis limits equal to data limits. |
| 'square' | Square plot; similar to 'scaled', but initially forcing `xmax-xmin == ymax-ymin`. |

**emit**bool, default: True

Whether observers are notified of the axis limit change. This option is passed on to [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 and [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
.

Returns:

**xmin, xmax, ymin, ymax**float

The axis limits.

See also

[`matplotlib.axes.Axes.set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")

[`matplotlib.axes.Axes.set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
.

For 3D Axes, this method additionally takes _zmin_, _zmax_ as parameters and likewise returns them.

Examples using `matplotlib.pyplot.axis`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#examples-using-matplotlib-pyplot-axis "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_fill_thumb.png)

[Filled polygon](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html)

Filled polygon

![](https://matplotlib.org/stable/_images/sphx_glr_autowrap_thumb.png)

[Auto-wrap text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/autowrap.html)

Auto-wrap text

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

On this page
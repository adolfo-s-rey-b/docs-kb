[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#main-content)

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
    

matplotlib.pyplot.stairs[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib-pyplot-stairs "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.stairs(_values_, _edges\=None_, _\*_, _orientation\='vertical'_, _baseline\=0_, _fill\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3683-L3702)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "Link to this definition")

Draw a stepwise constant function as a line or a filled plot.

_edges_ define the x-axis positions of the steps. _values_ the function values between these steps. Depending on _fill_, the function is drawn either as a continuous line with vertical segments at the edges, or as a filled area.

Parameters:

**values**array-like

The step heights.

**edges**array-like

The step positions, with `len(edges) == len(vals) + 1`, between which the curve takes on vals values.

**orientation**{'vertical', 'horizontal'}, default: 'vertical'

The direction of the steps. Vertical means that _values_ are along the y-axis, and edges are along the x-axis.

**baseline**float, array-like or None, default: 0

The bottom value of the bounding edges or when `fill=True`, position of lower edge. If _fill_ is True or an array is passed to _baseline_, a closed path is drawn.

If None, then drawn as an unclosed Path.

**fill**bool, default: False

Whether the area under the step curve should be filled.

Passing both ```fill=True` and ``baseline=None``` will likely result in undesired filling: the first and last points will be connected with a straight line and the fill will be between this line and the stairs.

Returns:

**StepPatch**[`StepPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")

Other Parameters:

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**

[`StepPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")
 properties

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stairs.html#matplotlib.axes.Axes.stairs "matplotlib.axes.Axes.stairs")
.

Examples using `matplotlib.pyplot.stairs`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#examples-using-matplotlib-pyplot-stairs "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_stairs_demo_thumb.png)

[Stairs Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html)

Stairs Demo

On this page
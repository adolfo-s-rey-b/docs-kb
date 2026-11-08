[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#main-content)

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
    

matplotlib.pyplot.xticks[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib-pyplot-xticks "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.xticks(_ticks\=None_, _labels\=None_, _\*_, _minor\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2314-L2397)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "Link to this definition")

Get or set the current tick locations and labels of the x-axis.

Pass no arguments to return the current values without modifying them.

Parameters:

**ticks**array-like, optional

The list of xtick locations. Passing an empty list removes all xticks.

**labels**array-like, optional

The labels to place at the given _ticks_ locations. This argument can only be passed if _ticks_ is passed as well.

**minor**bool, default: False

If `False`, get/set the major ticks/labels; if `True`, the minor ticks/labels.

**\*\*kwargs**

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties can be used to control the appearance of the labels.

Warning

This only sets the properties of the current ticks, which is only sufficient if you either pass _ticks_, resulting in a fixed list of ticks, or if the plot is static.

Ticks are not guaranteed to be persistent. Various operations can create, delete and modify the Tick instances. There is an imminent risk that these settings can get lost if you work on the figure further (including also panning/zooming on a displayed figure).

Use [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params "matplotlib.pyplot.tick_params")
 instead if possible.

Returns:

locs

The list of xtick locations.

labels

The list of xlabel [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 objects.

Notes

Calling this function with no arguments (e.g. `xticks()`) is the pyplot equivalent of calling [`get_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticks.html#matplotlib.axes.Axes.get_xticks "matplotlib.axes.Axes.get_xticks")
 and [`get_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
 on the current Axes. Calling this function with arguments is the pyplot equivalent of calling [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
 and [`set_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
 on the current Axes.

Examples

\>>> locs, labels \= xticks()  \# Get the current locations and labels.
\>>> xticks(np.arange(0, 1, step\=0.2))  \# Set label locations.
\>>> xticks(np.arange(3), \['Tom', 'Dick', 'Sue'\])  \# Set text labels.
\>>> xticks(\[0, 1, 2\], \['January', 'February', 'March'\],
...        rotation\=20)  \# Set text labels and properties.
\>>> xticks(\[\])  \# Disable xticks.

Examples using `matplotlib.pyplot.xticks`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#examples-using-matplotlib-pyplot-xticks "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_table_demo_thumb.png)

[Table Demo](https://matplotlib.org/stable/gallery/misc/table_demo.html)

Table Demo

On this page
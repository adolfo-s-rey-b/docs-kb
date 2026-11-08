[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#main-content)

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
    

matplotlib.pyplot.yticks[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib-pyplot-yticks "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.yticks(_ticks\=None_, _labels\=None_, _\*_, _minor\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2400-L2482)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "Link to this definition")

Get or set the current tick locations and labels of the y-axis.

Pass no arguments to return the current values without modifying them.

Parameters:

**ticks**array-like, optional

The list of ytick locations. Passing an empty list removes all yticks.

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

The list of ytick locations.

labels

The list of ylabel [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 objects.

Notes

Calling this function with no arguments (e.g. `yticks()`) is the pyplot equivalent of calling [`get_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticks.html#matplotlib.axes.Axes.get_yticks "matplotlib.axes.Axes.get_yticks")
 and [`get_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklabels.html#matplotlib.axes.Axes.get_yticklabels "matplotlib.axes.Axes.get_yticklabels")
 on the current Axes. Calling this function with arguments is the pyplot equivalent of calling [`set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
 and [`set_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
 on the current Axes.

Examples

\>>> locs, labels \= yticks()  \# Get the current locations and labels.
\>>> yticks(np.arange(0, 1, step\=0.2))  \# Set label locations.
\>>> yticks(np.arange(3), \['Tom', 'Dick', 'Sue'\])  \# Set text labels.
\>>> yticks(\[0, 1, 2\], \['January', 'February', 'March'\],
...        rotation\=45)  \# Set text labels and properties.
\>>> yticks(\[\])  \# Disable yticks.

Examples using `matplotlib.pyplot.yticks`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#examples-using-matplotlib-pyplot-yticks "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_table_demo_thumb.png)

[Table Demo](https://matplotlib.org/stable/gallery/misc/table_demo.html)

Table Demo

On this page
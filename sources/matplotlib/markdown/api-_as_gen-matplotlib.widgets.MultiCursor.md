[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#main-content)

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
    

matplotlib.widgets.MultiCursor[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib-widgets-multicursor "Link to this heading")

=======================================================================================================================================================================

class matplotlib.widgets.MultiCursor(_\*args_, _useblit\=True_, _horizOn\=False_, _vertOn\=True_, _\*\*lineprops_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2148-L2300)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor "Link to this definition")

Bases: [`Widget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget "matplotlib.widgets.Widget")

Provide a vertical (default) and/or horizontal line cursor shared between multiple Axes.

Call signatures:

MultiCursor(axes, \*, ...)
MultiCursor(canvas, axes, \*, ...)  \# deprecated

For the cursor to remain responsive you must keep a reference to it.

Parameters:

**canvas**object

This parameter is entirely unused.

Deprecated since version 3.11.

**axes**list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to attach the cursor to.

**useblit**bool, default: True

Use blitting for faster drawing if supported by the backend. See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

**horizOn**bool, default: False

Whether to draw the horizontal line.

**vertOn**bool, default: True

Whether to draw the vertical line.

Other Parameters:

**\*\*lineprops**

[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 properties that control the appearance of the lines. See also [`axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
.

Examples

See [Multicursor](https://matplotlib.org/stable/gallery/widgets/multicursor.html)
.

clear(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2256-L2268)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor.clear "Link to this definition")

Clear the cursor.

connect()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2241-L2247)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor.connect "Link to this definition")

Connect events.

disconnect()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2249-L2254)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor.disconnect "Link to this definition")

Disconnect events.

onmove(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2270-L2300)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor.onmove "Link to this definition")

Examples using `matplotlib.widgets.MultiCursor`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#examples-using-matplotlib-widgets-multicursor "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_multicursor_thumb.png)

[Multicursor](https://matplotlib.org/stable/gallery/widgets/multicursor.html)

Multicursor

On this page
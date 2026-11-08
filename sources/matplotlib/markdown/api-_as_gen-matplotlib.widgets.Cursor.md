[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#main-content)

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
    

matplotlib.widgets.Cursor[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib-widgets-cursor "Link to this heading")

========================================================================================================================================================

class matplotlib.widgets.Cursor(_ax_, _\*_, _horizOn\=True_, _vertOn\=True_, _useblit\=False_, _\*\*lineprops_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2046-L2145)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor "Link to this definition")

Bases: [`AxesWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget "matplotlib.widgets.AxesWidget")

A crosshair cursor that spans the Axes and moves with mouse cursor.

For the cursor to remain responsive you must keep a reference to it.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to attach the cursor to.

**horizOn**bool, default: True

Whether to draw the horizontal line.

**vertOn**bool, default: True

Whether to draw the vertical line.

**useblit**bool, default: False

Use blitting for faster drawing if supported by the backend. See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

Other Parameters:

**\*\*lineprops**

[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 properties that control the appearance of the lines. See also [`axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
.

Examples

See [Cursor](https://matplotlib.org/stable/gallery/widgets/cursor.html)
.

clear(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2103-L2108)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor.clear "Link to this definition")

Internal event handler to clear the cursor.

onmove(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2110-L2145)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor.onmove "Link to this definition")

Internal event handler to draw the cursor when the mouse moves.

Examples using `matplotlib.widgets.Cursor`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#examples-using-matplotlib-widgets-cursor "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_thumb.png)

[Annotated cursor](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html)

Annotated cursor

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_thumb.png)

[Cursor](https://matplotlib.org/stable/gallery/widgets/cursor.html)

Cursor

On this page
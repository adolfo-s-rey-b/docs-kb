[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#main-content)

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
    

matplotlib.widgets.ToolHandles[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib-widgets-toolhandles "Link to this heading")

=======================================================================================================================================================================

class matplotlib.widgets.ToolHandles(_ax_, _x_, _y_, _\*_, _marker\='o'_, _marker\_props\=None_, _useblit\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3215-L3277)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles "Link to this definition")

Control handles for canvas tools.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Matplotlib Axes where tool handles are displayed.

**x, y**1D arrays

Coordinates of control handles.

**marker**str, default: 'o'

Shape of marker used to display handle. See [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
.

**marker\_props**dict, optional

Additional marker properties. See [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.

**useblit**bool, default: True

Whether to use blitting for faster drawing (if supported by the backend). See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

\_\_init\_\_(_ax_, _x_, _y_, _\*_, _marker\='o'_, _marker\_props\=None_, _useblit\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3235-L3242)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.__init__ "matplotlib.widgets.ToolHandles.__init__")<br>(ax, x, y, \*\[, marker, ...\]) |     |
| [`closest`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.closest "matplotlib.widgets.ToolHandles.closest")<br>(x, y) | Return index and pixel distance to closest index. |
| [`set_animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.set_animated "matplotlib.widgets.ToolHandles.set_animated")<br>(val) |     |
| [`set_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.set_data "matplotlib.widgets.ToolHandles.set_data")<br>(pts\[, y\]) | Set x and y positions of handles. |
| [`set_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.set_visible "matplotlib.widgets.ToolHandles.set_visible")<br>(val) |     |

Attributes

|     |     |
| --- | --- |
| [`artists`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.artists "matplotlib.widgets.ToolHandles.artists") |     |
| [`x`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.x "matplotlib.widgets.ToolHandles.x") |     |
| [`y`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.y "matplotlib.widgets.ToolHandles.y") |     |

property artists[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.artists "Link to this definition")

closest(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3269-L3277)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.closest "Link to this definition")

Return index and pixel distance to closest index.

set\_animated(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3266-L3267)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.set_animated "Link to this definition")

set\_data(_pts_, _y\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3256-L3261)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.set_data "Link to this definition")

Set x and y positions of handles.

set\_visible(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3263-L3264)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.set_visible "Link to this definition")

property x[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.x "Link to this definition")

property y[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles.y "Link to this definition")

On this page
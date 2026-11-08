[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#main-content)

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
    

matplotlib.widgets.ToolLineHandles[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib-widgets-toollinehandles "Link to this heading")

===================================================================================================================================================================================

class matplotlib.widgets.ToolLineHandles(_ax_, _positions_, _direction_, _\*_, _line\_props\=None_, _useblit\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3105-L3212)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles "Link to this definition")

Control handles for canvas tools.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Matplotlib Axes where tool handles are displayed.

**positions**1D array

Positions of handles in data coordinates.

**direction**{"horizontal", "vertical"}

Direction of handles, either 'vertical' or 'horizontal'

**line\_props**dict, optional

Additional line properties. See [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.

**useblit**bool, default: True

Whether to use blitting for faster drawing (if supported by the backend). See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

\_\_init\_\_(_ax_, _positions_, _direction_, _\*_, _line\_props\=None_, _useblit\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3125-L3140)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.__init__ "matplotlib.widgets.ToolLineHandles.__init__")<br>(ax, positions, direction, \*\[, ...\]) |     |
| [`closest`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.closest "matplotlib.widgets.ToolLineHandles.closest")<br>(x, y) | Return index and pixel distance to closest handle. |
| [`remove`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.remove "matplotlib.widgets.ToolLineHandles.remove")<br>() | Remove the handles artist from the figure. |
| [`set_animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.set_animated "matplotlib.widgets.ToolLineHandles.set_animated")<br>(value) | Set the animated state of the handles artist. |
| [`set_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.set_data "matplotlib.widgets.ToolLineHandles.set_data")<br>(positions) | Set x- or y-positions of handles, depending on if the lines are vertical or horizontal. |
| [`set_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.set_visible "matplotlib.widgets.ToolLineHandles.set_visible")<br>(value) | Set the visibility state of the handles artist. |

Attributes

|     |     |
| --- | --- |
| [`artists`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.artists "matplotlib.widgets.ToolLineHandles.artists") |     |
| [`direction`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.direction "matplotlib.widgets.ToolLineHandles.direction") | Direction of the handle: 'vertical' or 'horizontal'. |
| [`positions`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.positions "matplotlib.widgets.ToolLineHandles.positions") | Positions of the handle in data coordinates. |

property artists[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.artists "Link to this definition")

closest(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3186-L3212)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.closest "Link to this definition")

Return index and pixel distance to closest handle.

Parameters:

**x, y**float

x, y position from which the distance will be calculated to determinate the closest handle

Returns:

**index, distance**index of the handle and its distance from

position x, y

property direction[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.direction "Link to this definition")

Direction of the handle: 'vertical' or 'horizontal'.

property positions[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.positions "Link to this definition")

Positions of the handle in data coordinates.

remove()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3181-L3184)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.remove "Link to this definition")

Remove the handles artist from the figure.

set\_animated(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3176-L3179)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.set_animated "Link to this definition")

Set the animated state of the handles artist.

set\_data(_positions_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3157-L3169)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.set_data "Link to this definition")

Set x- or y-positions of handles, depending on if the lines are vertical or horizontal.

Parameters:

**positions**tuple of length 2

Set the positions of the handle in data coordinates

set\_visible(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3171-L3174)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles.set_visible "Link to this definition")

Set the visibility state of the handles artist.

On this page
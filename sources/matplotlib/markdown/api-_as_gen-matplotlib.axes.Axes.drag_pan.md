[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.drag_pan.html#main-content)

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
    

matplotlib.axes.Axes.drag\_pan[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.drag_pan.html#matplotlib-axes-axes-drag-pan "Link to this heading")

=====================================================================================================================================================================

Axes.drag\_pan(_button_, _key_, _x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L4615-L4635)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.drag_pan.html#matplotlib.axes.Axes.drag_pan "Link to this definition")

Called when the mouse moves during a pan operation.

Parameters:

**button**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")

The pressed mouse button.

**key**str or None

The pressed key, if any.

**x, y**float

The mouse coordinates in display coords.

Notes

This is intended to be overridden by new projection types.

On this page
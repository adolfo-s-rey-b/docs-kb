[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#main-content)

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
    

matplotlib.widgets.PolygonSelector[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib-widgets-polygonselector "Link to this heading")

===================================================================================================================================================================================

class matplotlib.widgets.PolygonSelector(_ax_, _onselect\=None_, _\*_, _useblit\=False_, _props\=None_, _handle\_props\=None_, _grab\_range\=10_, _draw\_bounding\_box\=False_, _box\_handle\_props\=None_, _box\_props\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L4002-L4373)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "Link to this definition")

Bases: [`_SelectorWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget "matplotlib.widgets._SelectorWidget")

Select a polygon region of an Axes.

Place vertices with each mouse click, and make the selection by completing the polygon (clicking on the first vertex). Once drawn individual vertices can be moved by clicking and dragging with the left mouse button, or removed by clicking the right mouse button.

In addition, the following modifier keys can be used:

*   Hold _ctrl_ and click and drag a vertex to reposition it before the polygon has been completed.
    
*   Hold the _shift_ key and click and drag anywhere in the Axes to move all vertices.
    
*   Press the _esc_ key to start a new polygon.
    

For the selector to remain responsive you must keep a reference to it.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**onselect**function, optional

When a polygon is completed or modified after completion, the _onselect_ function is called and passed a list of the vertices as `(xdata, ydata)` tuples.

**useblit**bool, default: False

Whether to use blitting for faster drawing (if supported by the backend). See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

**props**dict, optional

Properties with which the line is drawn, see [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 for valid properties. Default:

dict(color\='k', linestyle\='-', linewidth\=2, alpha\=0.5)

**handle\_props**dict, optional

Artist properties for the markers drawn at the vertices of the polygon. See the marker arguments in [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 for valid properties. Default values are defined in `mpl.rcParams` except for the default value of `markeredgecolor` which will be the same as the `color` property in _props_.

**grab\_range**float, default: 10

A vertex is selected (to complete the polygon or to move a vertex) if the mouse click is within _grab\_range_ pixels of the vertex.

**draw\_bounding\_box**bool, optional

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, a bounding box will be drawn around the polygon selector once it is complete. This box can be used to move and resize the selector.

**box\_handle\_props**dict, optional

Properties to set for the box handles. See the documentation for the _handle\_props_ argument to [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 for more info.

**box\_props**dict, optional

Properties to set for the box. See the documentation for the _props_ argument to [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 for more info.

Notes

If only one point remains after removing points, the selector reverts to an incomplete state and you can start drawing a new polygon from the existing point.

Examples

[Polygon Selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html)
 [Select indices from a collection using polygon selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html)

onmove(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L4245-L4262)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector.onmove "Link to this definition")

Cursor move event handler and validator.

property verts[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector.verts "Link to this definition")

The polygon vertices, as a list of `(x, y)` pairs.

Examples using `matplotlib.widgets.PolygonSelector`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#examples-using-matplotlib-widgets-polygonselector "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_demo_thumb.png)

[Select indices from a collection using polygon selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html)

Select indices from a collection using polygon selector

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_simple_thumb.png)

[Polygon Selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html)

Polygon Selector

On this page
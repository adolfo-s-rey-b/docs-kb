[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#main-content)

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
    

matplotlib.widgets.LassoSelector[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib-widgets-lassoselector "Link to this heading")

=============================================================================================================================================================================

class matplotlib.widgets.LassoSelector(_ax_, _onselect\=None_, _\*_, _useblit\=True_, _props\=None_, _button\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3926-L3999)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "Link to this definition")

Bases: [`_SelectorWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget "matplotlib.widgets._SelectorWidget")

Selection curve of an arbitrary shape.

For the selector to remain responsive you must keep a reference to it.

The selected path can be used in conjunction with [`contains_point`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_point "matplotlib.path.Path.contains_point")
 to select data points from an image.

In contrast to [`Lasso`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib.widgets.Lasso "matplotlib.widgets.Lasso")
, [`LassoSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector")
 is written with an interface similar to [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 and [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")
, and will continue to interact with the Axes until disconnected.

Example usage:

ax \= plt.subplot()
ax.plot(x, y)

def onselect(verts):
    print(verts)
lasso \= LassoSelector(ax, onselect)

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**onselect**function, optional

Whenever the lasso is released, the _onselect_ function is called and passed the vertices of the selected path.

**useblit**bool, default: True

Whether to use blitting for faster drawing (if supported by the backend). See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

**props**dict, optional

Properties with which the line is drawn, see [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 for valid properties. Default values are defined in `mpl.rcParams`.

**button**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
 or list of [`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
, optional

The mouse buttons used for rectangle selection. Default is `None`, which corresponds to all buttons.

Examples using `matplotlib.widgets.LassoSelector`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#examples-using-matplotlib-widgets-lassoselector "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_lasso_selector_demo_sgskip_thumb.png)

[Lasso Selector](https://matplotlib.org/stable/gallery/widgets/lasso_selector_demo_sgskip.html)

Lasso Selector

On this page
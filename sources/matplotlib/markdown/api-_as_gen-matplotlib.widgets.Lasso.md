[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#main-content)

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
    

matplotlib.widgets.Lasso[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib-widgets-lasso "Link to this heading")

=====================================================================================================================================================

class matplotlib.widgets.Lasso(_ax_, _xy_, _callback_, _\*_, _useblit\=True_, _props\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L4376-L4454)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib.widgets.Lasso "Link to this definition")

Bases: [`AxesWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget "matplotlib.widgets.AxesWidget")

Selection curve of an arbitrary shape.

The selected path can be used in conjunction with [`contains_point`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_point "matplotlib.path.Path.contains_point")
 to select data points from an image.

Unlike [`LassoSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector")
, this must be initialized with a starting point _xy_, and the [`Lasso`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib.widgets.Lasso "matplotlib.widgets.Lasso")
 events are destroyed upon release.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**xy**(float, float)

Coordinates of the start of the lasso.

**callback**callable

Whenever the lasso is released, the _callback_ function is called and passed the vertices of the selected path.

**useblit**bool, default: True

Whether to use blitting for faster drawing (if supported by the backend). See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

**props: dict, optional**

Lasso line properties. See [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 for valid properties. Default _props_ are:

{'linestyle' : '-', 'color' : 'black', 'lw' : 2}

Added in version 3.9.

onmove(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L4439-L4454)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib.widgets.Lasso.onmove "Link to this definition")

onrelease(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L4427-L4437)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib.widgets.Lasso.onrelease "Link to this definition")

Examples using `matplotlib.widgets.Lasso`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#examples-using-matplotlib-widgets-lasso "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_lasso_demo_thumb.png)

[Lasso Demo](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html)

Lasso Demo

On this page
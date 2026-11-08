[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#main-content)

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
    

matplotlib.widgets.SpanSelector[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib-widgets-spanselector "Link to this heading")

==========================================================================================================================================================================

class matplotlib.widgets.SpanSelector(_ax_, _onselect_, _direction_, _\*_, _minspan\=0_, _useblit\=False_, _props\=None_, _onmove\_callback\=None_, _interactive\=False_, _button\=None_, _handle\_props\=None_, _grab\_range\=10_, _state\_modifier\_keys\=None_, _drag\_from\_anywhere\=False_, _ignore\_event\_outside\=False_, _snap\_values\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2684-L3102)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "Link to this definition")

Bases: [`_SelectorWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget "matplotlib.widgets._SelectorWidget")

Visually select a min/max range on a single axis and call a function with those values.

To guarantee that the selector remains responsive, keep a reference to it.

In order to turn off the SpanSelector, set `span_selector.active` to False. To turn it back on, set it to True.

Press and release events triggered at the same coordinates outside the selection will clear the selector, except when `ignore_event_outside=True`.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

**onselect**callable with signature `func(min: float, max: float)`

A callback function that is called after a release event and the selection is created, changed or removed.

**direction**{"horizontal", "vertical"}

The direction along which to draw the span selector.

**minspan**float, default: 0

If selection is less than or equal to _minspan_, the selection is removed (when already existing) or cancelled.

**useblit**bool, default: False

If True, use the backend-dependent blitting features for faster canvas updates. See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

**props**dict, default: {'facecolor': 'red', 'alpha': 0.5}

Dictionary of [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 properties.

**onmove\_callback**callable with signature `func(min: float, max: float)`, optional

Called on mouse move while the span is being selected.

**interactive**bool, default: False

Whether to draw a set of handles that allow interaction with the widget after it is drawn.

**button**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
 or list of [`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
, default: all buttons

The mouse buttons which activate the span selector.

**handle\_props**dict, default: None

Properties of the handle lines at the edges of the span. Only used when _interactive_ is True. See [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 for valid properties.

**grab\_range**float, default: 10

Distance in pixels within which the interactive tool handles can be activated.

**state\_modifier\_keys**dict, optional

Keyboard modifiers which affect the widget's behavior. Values amend the defaults, which are:

*   "clear": Clear the current shape, default: "escape".
    

**drag\_from\_anywhere**bool, default: False

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, the widget can be moved by clicking anywhere within its bounds.

**ignore\_event\_outside**bool, default: False

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, the event triggered outside the span selector will be ignored.

**snap\_values**1D array-like, optional

Snap the selector edges to the given values.

Examples

\>>> import matplotlib.pyplot as plt
\>>> import matplotlib.widgets as mwidgets
\>>> fig, ax \= plt.subplots()
\>>> ax.plot(\[1, 2, 3\], \[10, 50, 100\])
\>>> def onselect(vmin, vmax):
...     print(vmin, vmax)
\>>> span \= mwidgets.SpanSelector(ax, onselect, 'horizontal',
...                              props\=dict(facecolor\='blue', alpha\=0.5))
\>>> fig.show()

See also: [Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

connect\_default\_events()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2877-L2881)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector.connect_default_events "Link to this definition")

Connect the major canvas events to methods.

property direction[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector.direction "Link to this definition")

Direction of the span selector: 'vertical' or 'horizontal'.

property extents[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector.extents "Link to this definition")

(float, float)

The values, in data coordinates, for the start and end points of the current selection. If there is no selection then the start and end values will be the same.

new\_axes(_ax_, _\*_, _\_props\=None_, _\_init\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2819-L2846)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector.new_axes "Link to this definition")

Set SpanSelector to operate on a new Axes.

Examples using `matplotlib.widgets.SpanSelector`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#examples-using-matplotlib-widgets-spanselector "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_span_selector_thumb.png)

[Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

Span Selector

On this page
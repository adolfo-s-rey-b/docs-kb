[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#main-content)

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
    

matplotlib.widgets.EllipseSelector[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib-widgets-ellipseselector "Link to this heading")

===================================================================================================================================================================================

class matplotlib.widgets.EllipseSelector(_ax_, _onselect\=None_, _\*_, _minspanx\=0_, _minspany\=0_, _useblit\=False_, _props\=None_, _spancoords\='data'_, _button\=None_, _grab\_range\=10_, _handle\_props\=None_, _interactive\=False_, _state\_modifier\_keys\=None_, _drag\_from\_anywhere\=False_, _ignore\_event\_outside\=False_, _use\_data\_coordinates\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L3884-L3923)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "Link to this definition")

Bases: [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")

Select an elliptical region of an Axes.

For the cursor to remain responsive you must keep a reference to it.

Press and release events triggered at the same coordinates outside the selection will clear the selector, except when `ignore_event_outside=True`.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**onselect**function, optional

A callback function that is called after a release event and the selection is created, changed or removed. It must have the signature:

def onselect(eclick: MouseEvent, erelease: MouseEvent)

where _eclick_ and _erelease_ are the mouse click and release [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
s that start and complete the selection.

**minspanx**float, default: 0

Selections with an x-span less than or equal to _minspanx_ are removed (when already existing) or cancelled.

**minspany**float, default: 0

Selections with a y-span less than or equal to _minspanx_ are removed (when already existing) or cancelled.

**useblit**bool, default: False

Whether to use blitting for faster drawing (if supported by the backend). See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

**props**dict, optional

Properties with which the ellipse is drawn. See [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 for valid properties. Default:

`dict(facecolor='red', edgecolor='black', alpha=0.2, fill=True)`

**spancoords**{"data", "pixels"}, default: "data"

Whether to interpret _minspanx_ and _minspany_ in data or in pixel coordinates.

**button**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
, list of [`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
, default: all buttons

Button(s) that trigger rectangle selection.

**grab\_range**float, default: 10

Distance in pixels within which the interactive tool handles can be activated.

**handle\_props**dict, optional

Properties with which the interactive handles (marker artists) are drawn. See the marker arguments in [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 for valid properties. Default values are defined in `mpl.rcParams` except for the default value of `markeredgecolor` which will be the same as the `edgecolor` property in _props_.

**interactive**bool, default: False

Whether to draw a set of handles that allow interaction with the widget after it is drawn.

**state\_modifier\_keys**dict, optional

Keyboard modifiers which affect the widget's behavior. Values amend the defaults, which are:

*   "move": Move the existing shape, default: no modifier.
    
*   "clear": Clear the current shape, default: "escape".
    
*   "square": Make the shape square, default: "shift".
    
*   "center": change the shape around its center, default: "ctrl".
    
*   "rotate": Rotate the shape around its center between -45° and 45°, default: "r".
    

"square" and "center" can be combined. The square shape can be defined in data or display coordinates as determined by the `use_data_coordinates` argument specified when creating the selector.

**drag\_from\_anywhere**bool, default: False

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, the widget can be moved by clicking anywhere within its bounds.

**ignore\_event\_outside**bool, default: False

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, the event triggered outside the span selector will be ignored.

**use\_data\_coordinates**bool, default: False

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, the "square" shape of the selector is defined in data coordinates instead of display coordinates.

Examples

[Rectangle and ellipse selectors](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html)

Examples using `matplotlib.widgets.EllipseSelector`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#examples-using-matplotlib-widgets-ellipseselector "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_rectangle_selector_thumb.png)

[Rectangle and ellipse selectors](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html)

Rectangle and ellipse selectors

On this page
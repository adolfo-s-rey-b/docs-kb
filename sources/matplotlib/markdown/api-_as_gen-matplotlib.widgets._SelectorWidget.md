[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#main-content)

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
    

matplotlib.widgets.\_SelectorWidget[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib-widgets-selectorwidget "Link to this heading")

===================================================================================================================================================================================

class matplotlib.widgets.\_SelectorWidget(_ax_, _onselect\=None_, _useblit\=False_, _button\=None_, _state\_modifier\_keys\=None_, _use\_data\_coordinates\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2303-L2681)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget "Link to this definition")

Bases: [`AxesWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget "matplotlib.widgets.AxesWidget")

The base class for selector widgets.

This class provides common functionality for selector widgets, such as handling mouse and keyboard events, managing state modifier keys, etc.

The class itself is private and may be changed or removed without prior warning. However, the public API it provides to subclasses is stable and considered public on the subclasses.

add\_state(_state_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2639-L2659)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.add_state "Link to this definition")

Add a state to define the widget's behavior. See the _state\_modifier\_keys_ parameter in the constructor of the concrete selector class for details.

Parameters:

**state**str

Must be a supported state of the selector. See the _state\_modifier\_keys_ parameter in the constructor of the concrete selector class for details.

Raises:

ValueError

When the state is not supported by the selector.

property artists[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.artists "Link to this definition")

Tuple of the artists of the selector.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2587-L2590)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.clear "Link to this definition")

Clear the selection and set the selector ready to make a new one.

connect\_default\_events()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2398-L2406)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.connect_default_events "Link to this definition")

Connect the major canvas events to methods.

get\_visible()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2583-L2585)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.get_visible "Link to this definition")

Get the visibility of the selector artists.

ignore(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2408-L2432)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.ignore "Link to this definition")

Return whether _event_ should be ignored.

This method should be called at the beginning of any event callback.

on\_key\_press(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2537-L2557)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.on_key_press "Link to this definition")

Key press event handler and validator for all selection widgets.

on\_key\_release(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2562-L2572)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.on_key_release "Link to this definition")

Key release event handler and validator.

on\_scroll(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2528-L2532)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.on_scroll "Link to this definition")

Mouse scroll event handler and validator.

onmove(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2516-L2523)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.onmove "Link to this definition")

Cursor move event handler and validator.

press(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2481-L2495)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.press "Link to this definition")

Button press handler and validator.

release(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2500-L2511)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.release "Link to this definition")

Button release event handler and validator.

remove\_state(_state_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2661-L2681)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.remove_state "Link to this definition")

Remove a state to define the widget's behavior. See the _state\_modifier\_keys_ parameter in the constructor of the concrete selector class for details.

Parameters:

**state**str

Must be a supported state of the selector. See the _state\_modifier\_keys_ parameter in the constructor of the concrete selector class for details.

Raises:

ValueError

When the state is not supported by the selector.

set\_active(_active_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2353-L2356)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.set_active "Link to this definition")

Set whether the widget is active.

set\_handle\_props(_\*\*handle\_props_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2615-L2630)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.set_handle_props "Link to this definition")

Set the properties of the handles selector artist. See the _handle\_props_ argument in the selector docstring to know which properties are supported.

set\_props(_\*\*props_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2602-L2613)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.set_props "Link to this definition")

Set the properties of the selector artist.

See the _props_ argument in the selector docstring to know which properties are supported.

set\_visible(_visible_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2577-L2581)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.set_visible "Link to this definition")

Set the visibility of the selector artists.

update()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2434-L2454)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.update "Link to this definition")

Draw using blit() or draw\_idle(), depending on `self.useblit`.

update\_background(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L2370-L2396)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.update_background "Link to this definition")

Force an update of the background.

property useblit[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget.useblit "Link to this definition")

Return whether blitting is used (requested and supported by canvas).

Examples using `matplotlib.widgets._SelectorWidget`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#examples-using-matplotlib-widgets-selectorwidget "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_demo_thumb.png)

[Select indices from a collection using polygon selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html)

Select indices from a collection using polygon selector

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_simple_thumb.png)

[Polygon Selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html)

Polygon Selector

![](https://matplotlib.org/stable/_images/sphx_glr_rectangle_selector_thumb.png)

[Rectangle and ellipse selectors](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html)

Rectangle and ellipse selectors

![](https://matplotlib.org/stable/_images/sphx_glr_span_selector_thumb.png)

[Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

Span Selector

On this page
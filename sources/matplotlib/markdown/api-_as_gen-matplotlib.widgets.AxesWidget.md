[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#main-content)

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
    

matplotlib.widgets.AxesWidget[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib-widgets-axeswidget "Link to this heading")

====================================================================================================================================================================

class matplotlib.widgets.AxesWidget(_ax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L95-L169)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget "Link to this definition")

Bases: [`Widget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget "matplotlib.widgets.Widget")

Widget connected to a single [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.

To guarantee that the widget remains responsive and not garbage-collected, a reference to the object should be maintained by the user.

This is necessary because the callback registry maintains only weak-refs to the functions, which are member functions of the widget. If there are no references to the widget object it may be garbage collected which will disconnect the callbacks.

Attributes:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**canvas**[`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

The parent figure canvas for the widget.

`active`bool

Is the widget active?

property canvas[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget.canvas "Link to this definition")

connect\_event(_event_, _callback_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L126-L134)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget.connect_event "Link to this definition")

Connect a callback function with an event.

This should be used in lieu of `figure.canvas.mpl_connect` since this function stores callback ids for later clean up.

disconnect\_events()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L136-L139)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget.disconnect_events "Link to this definition")

Disconnect all events created by this widget.

ignore(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L141-L143)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget.ignore "Link to this definition")

Return whether _event_ should be ignored.

This method should be called at the beginning of any event callback.

Examples using `matplotlib.widgets.AxesWidget`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#examples-using-matplotlib-widgets-axeswidget "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_thumb.png)

[Annotated cursor](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html)

Annotated cursor

![](https://matplotlib.org/stable/_images/sphx_glr_buttons_thumb.png)

[Buttons](https://matplotlib.org/stable/gallery/widgets/buttons.html)

Buttons

![](https://matplotlib.org/stable/_images/sphx_glr_check_buttons_thumb.png)

[Check buttons](https://matplotlib.org/stable/gallery/widgets/check_buttons.html)

Check buttons

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_thumb.png)

[Cursor](https://matplotlib.org/stable/gallery/widgets/cursor.html)

Cursor

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_demo_thumb.png)

[Select indices from a collection using polygon selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html)

Select indices from a collection using polygon selector

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_simple_thumb.png)

[Polygon Selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html)

Polygon Selector

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_thumb.png)

[Radio Buttons](https://matplotlib.org/stable/gallery/widgets/radio_buttons.html)

Radio Buttons

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_grid_thumb.png)

[Radio Buttons Grid](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html)

Radio Buttons Grid

![](https://matplotlib.org/stable/_images/sphx_glr_range_slider_thumb.png)

[Image scaling using a RangeSlider](https://matplotlib.org/stable/gallery/widgets/range_slider.html)

Image scaling using a RangeSlider

![](https://matplotlib.org/stable/_images/sphx_glr_rectangle_selector_thumb.png)

[Rectangle and ellipse selectors](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html)

Rectangle and ellipse selectors

![](https://matplotlib.org/stable/_images/sphx_glr_slider_demo_thumb.png)

[Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)

Slider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_snap_demo_thumb.png)

[Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)

Snap sliders to discrete values

![](https://matplotlib.org/stable/_images/sphx_glr_span_selector_thumb.png)

[Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

Span Selector

![](https://matplotlib.org/stable/_images/sphx_glr_textbox_thumb.png)

[Textbox](https://matplotlib.org/stable/gallery/widgets/textbox.html)

Textbox

![](https://matplotlib.org/stable/_images/sphx_glr_lasso_demo_thumb.png)

[Lasso Demo](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html)

Lasso Demo

On this page
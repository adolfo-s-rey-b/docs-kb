[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#main-content)

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
    

matplotlib.widgets.Widget[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib-widgets-widget "Link to this heading")

========================================================================================================================================================

class matplotlib.widgets.Widget[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L67-L92)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Abstract base class for GUI neutral widgets.

property active[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget.active "Link to this definition")

Is the widget active?

drawon \= True[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget.drawon "Link to this definition")

eventson \= True[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget.eventson "Link to this definition")

get\_active()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L79-L81)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget.get_active "Link to this definition")

Get whether the widget is active.

ignore(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L86-L92)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget.ignore "Link to this definition")

Return whether _event_ should be ignored.

This method should be called at the beginning of any event callback.

set\_active(_active_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L75-L77)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget.set_active "Link to this definition")

Set whether the widget is active.

Examples using `matplotlib.widgets.Widget`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#examples-using-matplotlib-widgets-widget "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

![](https://matplotlib.org/stable/_images/sphx_glr_multicursor_thumb.png)

[Multicursor](https://matplotlib.org/stable/gallery/widgets/multicursor.html)

Multicursor

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
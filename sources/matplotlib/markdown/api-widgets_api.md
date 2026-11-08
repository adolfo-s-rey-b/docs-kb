[Skip to main content](https://matplotlib.org/stable/api/widgets_api.html#main-content)

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
    

`matplotlib.widgets`[#](https://matplotlib.org/stable/api/widgets_api.html#module-matplotlib.widgets "Link to this heading")

=============================================================================================================================

Widgets that are designed to work for any of the GUI backends.

All of these widgets require you to predefine an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance and pass that as the first parameter. Matplotlib doesn't try to be too smart with respect to layout -- you will have to figure out how wide and tall you want your Axes to be to accommodate your widget.

Widget classes[#](https://matplotlib.org/stable/api/widgets_api.html#widget-classes "Link to this heading")

------------------------------------------------------------------------------------------------------------

Inheritance diagram of matplotlib.widgets.Widget

|     |     |
| --- | --- |
| [`Widget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget "matplotlib.widgets.Widget") | Abstract base class for GUI neutral widgets. |
| [`AxesWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget "matplotlib.widgets.AxesWidget") | Widget connected to a single [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br>. |
| [`Cursor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor "matplotlib.widgets.Cursor") | A crosshair cursor that spans the Axes and moves with mouse cursor. |
| [`MultiCursor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor "matplotlib.widgets.MultiCursor") | Provide a vertical (default) and/or horizontal line cursor shared between multiple Axes. |
| [`Button`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button") | A GUI neutral button. |
| [`_Buttons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons "matplotlib.widgets._Buttons") | The base class for [`CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")<br> and [`RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")<br>. |
| [`CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons") | A GUI neutral set of check buttons. |
| [`RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons") | A GUI neutral radio button. |
| [`SliderBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase "matplotlib.widgets.SliderBase") | The base class for constructing Slider widgets. |
| [`Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider") | A slider representing a floating point range. |
| [`RangeSlider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "matplotlib.widgets.RangeSlider") | A slider representing a range of floating point values. |
| [`TextBox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox") | A GUI neutral text input box. |
| [`_SelectorWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._SelectorWidget.html#matplotlib.widgets._SelectorWidget "matplotlib.widgets._SelectorWidget") | The base class for selector widgets. |
| [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector") | Select a rectangular region of an Axes. |
| [`EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector") | Select an elliptical region of an Axes. |
| [`Lasso`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib.widgets.Lasso "matplotlib.widgets.Lasso") | Selection curve of an arbitrary shape. |
| [`LassoSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector") | Selection curve of an arbitrary shape. |
| [`PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector") | Select a polygon region of an Axes. |
| [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector") | Visually select a min/max range on a single axis and call a function with those values. |
| [`SubplotTool`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SubplotTool.html#matplotlib.widgets.SubplotTool "matplotlib.widgets.SubplotTool") | A tool to adjust the subplot params of a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br>. |

Helper classes[#](https://matplotlib.org/stable/api/widgets_api.html#helper-classes "Link to this heading")

------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`LockDraw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw "matplotlib.widgets.LockDraw") | Some widgets, like the cursor, draw onto the canvas, and this is not desirable under all circumstances, like when the toolbar is in zoom-to-rect mode and drawing a rectangle. |
| [`ToolHandles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolHandles.html#matplotlib.widgets.ToolHandles "matplotlib.widgets.ToolHandles") | Control handles for canvas tools. |
| [`ToolLineHandles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.ToolLineHandles.html#matplotlib.widgets.ToolLineHandles "matplotlib.widgets.ToolLineHandles") | Control handles for canvas tools. |

On this page
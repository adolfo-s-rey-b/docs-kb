[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#main-content)

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
    

matplotlib.widgets.CheckButtons[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib-widgets-checkbuttons "Link to this heading")

==========================================================================================================================================================================

class matplotlib.widgets.CheckButtons(_ax_, _labels_, _actives\=None_, _\*_, _layout\=None_, _useblit\=True_, _label\_props\=None_, _frame\_props\=None_, _check\_props\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1233-L1489)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "Link to this definition")

Bases: [`_Buttons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons "matplotlib.widgets._Buttons")

A GUI neutral set of check buttons.

For the check buttons to remain responsive you must keep a reference to this object.

Connect to the CheckButtons with the [`on_clicked`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons.on_clicked "matplotlib.widgets._Buttons.on_clicked")
 method.

Attributes:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**labels**list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The text label objects of the check buttons.

Add check buttons to [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance _ax_.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**labels**list of str

The labels of the check buttons.

**actives**list of bool, optional

The initial check states of the buttons. The list must have the same length as _labels_. If not given, all buttons are unchecked.

**layout**None or "vertical" or "horizontal" or (int, int), default: None

The layout of the check buttons. Options are:

*   `None`: Use legacy vertical layout (default).
    
*   `"vertical"`: Arrange buttons in a single column with dynamic positioning based on text widths.
    
*   `"horizontal"`: Arrange buttons in a single row with dynamic positioning based on text widths.
    
*   `(rows, cols)` tuple: Arrange buttons in a grid with the specified number of rows and columns. Buttons are placed left-to-right, top-to-bottom with dynamic positioning.
    

The layout options "vertical", "horizontal" and `(rows, cols)` create `mtext.Text` objects to determine exact text sizes, and then they are added to the Axes. This is usually okay, but may cause side-effects and has a slight performance impact. Therefore the default `None` value avoids this.

Added in version 3.11.

**useblit**bool, default: True

Use blitting for faster drawing if supported by the backend. See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

Added in version 3.7.

**label\_props**dict of lists, optional

Dictionary of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties to be used for the labels. Each dictionary value should be a list of at least a single element. If the list is of length M, its values are cycled such that the Nth label gets the (N mod M) property.

Added in version 3.7.

**frame\_props**dict, optional

Dictionary of scatter [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 properties to be used for the check button frame. Defaults (label font size / 2)\*\*2 size, black edgecolor, no facecolor, and 1.0 linewidth.

Added in version 3.7.

**check\_props**dict, optional

Dictionary of scatter [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 properties to be used for the check button check. Defaults to (label font size / 2)\*\*2 size, black color, and 1.0 linewidth.

Added in version 3.7.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1460-L1475)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons.clear "Link to this definition")

Uncheck all checkboxes.

get\_checked\_labels()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1484-L1489)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons.get_checked_labels "Link to this definition")

Return a list of labels currently checked by user.

get\_status()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1477-L1482)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons.get_status "Link to this definition")

Return a list of the status (True/False) of all of the check buttons.

set\_active(_index_, _state\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1397-L1442)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons.set_active "Link to this definition")

Modify the state of a check button by index.

Callbacks will be triggered if `eventson` is True.

Parameters:

**index**int

Index of the check button to toggle.

**state**bool, optional

If a boolean value, set the state explicitly. If no value is provided, the state is toggled.

Raises:

ValueError

If _index_ is invalid.

TypeError

If _state_ is not boolean.

set\_check\_props(_props_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1377-L1395)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons.set_check_props "Link to this definition")

Set properties of the check button checks.

Added in version 3.7.

Parameters:

**props**dict

Dictionary of [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 properties to be used for the check button check.

set\_frame\_props(_props_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1360-L1375)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons.set_frame_props "Link to this definition")

Set properties of the check button frames.

Added in version 3.7.

Parameters:

**props**dict

Dictionary of [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 properties to be used for the check button frames.

Examples using `matplotlib.widgets.CheckButtons`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#examples-using-matplotlib-widgets-checkbuttons "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_check_buttons_thumb.png)

[Check buttons](https://matplotlib.org/stable/gallery/widgets/check_buttons.html)

Check buttons

On this page
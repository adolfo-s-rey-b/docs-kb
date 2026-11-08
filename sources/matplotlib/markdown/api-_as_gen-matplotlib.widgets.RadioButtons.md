[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#main-content)

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
    

matplotlib.widgets.RadioButtons[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib-widgets-radiobuttons "Link to this heading")

==========================================================================================================================================================================

class matplotlib.widgets.RadioButtons(_ax_, _labels_, _active\=0_, _activecolor\=None_, _\*_, _layout\=None_, _useblit\=True_, _label\_props\=None_, _radio\_props\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1756-L1971)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "Link to this definition")

Bases: [`_Buttons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons "matplotlib.widgets._Buttons")

A GUI neutral radio button.

For the buttons to remain responsive you must keep a reference to this object.

Connect to the RadioButtons with the [`on_clicked`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons.on_clicked "matplotlib.widgets._Buttons.on_clicked")
 method.

Attributes:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**activecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The color of the selected button.

**labels**list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The button labels.

**value\_selected**str

The label text of the currently selected button.

**index\_selected**int

The index of the selected button.

Add radio buttons to an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes to add the buttons to.

**labels**list of str

The button labels.

**active**int

The index of the initially selected button.

**activecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The color of the selected button. The default is `'blue'` if not specified here or in _radio\_props_.

**layout**None or "vertical" or "horizontal" or (int, int), default: None

The layout of the radio buttons. Options are:

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

**radio\_props**dict, optional

Dictionary of scatter [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 properties to be used for the radio buttons. Defaults to (label font size / 2)\*\*2 size, black edgecolor, and _activecolor_ facecolor (when active).

Note

If a facecolor is supplied in _radio\_props_, it will override _activecolor_. This may be used to provide an active color per button.

Added in version 3.7.

property activecolor[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons.activecolor "Link to this definition")

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1969-L1971)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons.clear "Link to this definition")

Reset the active button to the initially active one.

set\_active(_index_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1931-L1967)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons.set_active "Link to this definition")

Select button with number _index_.

Callbacks will be triggered if `eventson` is True.

Parameters:

**index**int

The index of the button to activate.

Raises:

ValueError

If the index is invalid.

set\_radio\_props(_props_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1897-L1919)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons.set_radio_props "Link to this definition")

Set properties of the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 labels.

Added in version 3.7.

Parameters:

**props**dict

Dictionary of [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 properties to be used for the radio buttons.

Examples using `matplotlib.widgets.RadioButtons`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#examples-using-matplotlib-widgets-radiobuttons "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_thumb.png)

[Radio Buttons](https://matplotlib.org/stable/gallery/widgets/radio_buttons.html)

Radio Buttons

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_grid_thumb.png)

[Radio Buttons Grid](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html)

Radio Buttons Grid

On this page
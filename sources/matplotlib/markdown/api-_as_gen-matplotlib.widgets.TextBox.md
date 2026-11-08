[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#main-content)

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
    

matplotlib.widgets.TextBox[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib-widgets-textbox "Link to this heading")

===========================================================================================================================================================

class matplotlib.widgets.TextBox(_ax_, _label_, _initial\=''_, _\*_, _color\='.95'_, _hovercolor\='1'_, _label\_pad\=0.01_, _textalignment\='left'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1492-L1753)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "Link to this definition")

Bases: [`AxesWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget "matplotlib.widgets.AxesWidget")

A GUI neutral text input box.

For the text box to remain responsive you must keep a reference to it.

Call [`on_text_change`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.on_text_change "matplotlib.widgets.TextBox.on_text_change")
 to be updated whenever the text changes.

Call [`on_submit`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.on_submit "matplotlib.widgets.TextBox.on_submit")
 to be updated whenever the user hits enter or leaves the text entry field.

Attributes:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The parent Axes for the widget.

**label**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The color of the text box when not hovering.

**hovercolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The color of the text box when hovering.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance the button will be placed into.

**label**str

Label for this text box.

**initial**str

Initial value in the text box.

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The color of the box.

**hovercolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The color of the box when the mouse is over it.

**label\_pad**float

The distance between the label and the right side of the textbox.

**textalignment**{'left', 'center', 'right'}

The horizontal location of the text.

begin\_typing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1669-L1688)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.begin_typing "Link to this definition")

disconnect(_cid_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1751-L1753)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.disconnect "Link to this definition")

Remove the observer with connection id _cid_.

on\_submit(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1742-L1749)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.on_submit "Link to this definition")

When the user hits enter or leaves the submission box, call this _func_ with event.

A connection id is returned which can be used to disconnect.

on\_text\_change(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1734-L1740)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.on_text_change "Link to this definition")

When the text changes, call this _func_ with event.

A connection id is returned which can be used to disconnect.

set\_val(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1659-L1667)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.set_val "Link to this definition")

stop\_typing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1690-L1703)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.stop_typing "Link to this definition")

property text[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.text "Link to this definition")

Examples using `matplotlib.widgets.TextBox`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#examples-using-matplotlib-widgets-textbox "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_textbox_thumb.png)

[Textbox](https://matplotlib.org/stable/gallery/widgets/textbox.html)

Textbox

On this page
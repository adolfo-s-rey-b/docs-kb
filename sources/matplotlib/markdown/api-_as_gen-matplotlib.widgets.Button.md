[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#main-content)

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
    

matplotlib.widgets.Button[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib-widgets-button "Link to this heading")

========================================================================================================================================================

class matplotlib.widgets.Button(_ax_, _label_, _image\=None_, _color\='0.85'_, _hovercolor\='0.95'_, _\*_, _useblit\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L198-L301)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "Link to this definition")

Bases: [`AxesWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget "matplotlib.widgets.AxesWidget")

A GUI neutral button.

For the button to remain responsive you must keep a reference to it. Call [`on_clicked`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button.on_clicked "matplotlib.widgets.Button.on_clicked")
 to connect to the button.

Attributes:

**ax**

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 the button renders into.

**label**

A [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance.

**color**

The color of the button when not hovering.

**hovercolor**

The color of the button when hovering.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance the button will be placed into.

**label**str

The button text.

**image**array-like or PIL Image

The image to place in the button, if not _None_. The parameter is directly forwarded to [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The color of the button when not activated.

**hovercolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The color of the button when the mouse is over it.

**useblit**bool, default: True

Use blitting for faster drawing if supported by the backend. See the tutorial [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
 for details.

Added in version 3.7.

disconnect(_cid_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L299-L301)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button.disconnect "Link to this definition")

Remove the callback function with connection id _cid_.

on\_clicked(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L291-L297)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button.on_clicked "Link to this definition")

Connect the callback function _func_ to button click events.

Returns a connection id, which can be used to disconnect the callback.

Examples using `matplotlib.widgets.Button`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#examples-using-matplotlib-widgets-button "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_buttons_thumb.png)

[Buttons](https://matplotlib.org/stable/gallery/widgets/buttons.html)

Buttons

![](https://matplotlib.org/stable/_images/sphx_glr_slider_demo_thumb.png)

[Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)

Slider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_snap_demo_thumb.png)

[Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)

Snap sliders to discrete values

On this page
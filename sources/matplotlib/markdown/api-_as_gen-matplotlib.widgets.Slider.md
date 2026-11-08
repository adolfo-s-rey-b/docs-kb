[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#main-content)

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
    

matplotlib.widgets.Slider[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib-widgets-slider "Link to this heading")

========================================================================================================================================================

class matplotlib.widgets.Slider(_ax_, _label_, _valmin_, _valmax_, _\*_, _valinit\=0.5_, _valfmt\=None_, _closedmin\=True_, _closedmax\=True_, _slidermin\=None_, _slidermax\=None_, _dragging\=True_, _valstep\=None_, _orientation\='horizontal'_, _initcolor\='r'_, _track\_color\='lightgrey'_, _handle\_style\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L382-L649)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "Link to this definition")

Bases: [`SliderBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase "matplotlib.widgets.SliderBase")

A slider representing a floating point range.

Create a slider from _valmin_ to _valmax_ in Axes _ax_. For the slider to remain responsive you must maintain a reference to it. Call [`on_changed()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider.on_changed "matplotlib.widgets.Slider.on_changed")
 to connect to the slider event.

Attributes:

**val**float

Slider value.

Parameters:

**ax**Axes

The Axes to put the slider in.

**label**str

Slider label.

**valmin**float

The minimum value of the slider.

**valmax**float

The maximum value of the slider.

**valinit**float, default: 0.5

The slider initial position.

**valfmt**str, default: None

The way to format the slider value. If a string, it must be in %-format. If a callable, it must have the signature `valfmt(val: float) -> str`. If None, a [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 is used.

**closedmin**bool, default: True

Whether the slider interval is closed on the bottom.

**closedmax**bool, default: True

Whether the slider interval is closed on the top.

**slidermin**Slider, default: None

Do not allow the current slider to have a value less than the value of the Slider _slidermin_.

**slidermax**Slider, default: None

Do not allow the current slider to have a value greater than the value of the Slider _slidermax_.

**dragging**bool, default: True

If True the slider can be dragged by the mouse.

**valstep**float or array-like, default: None

If a float, the slider will snap to multiples of _valstep_. If an array the slider will snap to the values in the array.

**orientation**{'horizontal', 'vertical'}, default: 'horizontal'

The orientation of the slider.

**initcolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: 'r'

The color of the line at the _valinit_ position. Set to `'none'` for no line.

**track\_color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: 'lightgrey'

The color of the background track. The track is accessible for further styling via the _track_ attribute.

**handle\_style**dict

Properties of the slider handle. Default values are

| Key | Value | Default | Description |
| --- | --- | --- | --- |
| facecolor | color | 'white' | The facecolor of the slider handle. |
| edgecolor | color | '.75' | The edgecolor of the slider handle. |
| size | int | 10  | The size of the slider handle in points. |

Other values will be transformed as marker{foo} and passed to the [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 constructor. e.g. `handle_style = {'style'='x'}` will result in `markerstyle = 'x'`.

Notes

Additional kwargs are passed on to `self.poly` which is the [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 that draws the slider knob. See the [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 documentation for valid property names (`facecolor`, `edgecolor`, `alpha`, etc.).

on\_changed(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L634-L649)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider.on_changed "Link to this definition")

Connect _func_ as callback function to changes of the slider value.

Parameters:

**func**callable

Function to call when slider is changed. The function must accept a single float as its arguments.

Returns:

int

Connection id (which can be used to disconnect _func_).

set\_val(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L613-L632)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider.set_val "Link to this definition")

Set slider value to _val_.

Parameters:

**val**float

Examples using `matplotlib.widgets.Slider`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#examples-using-matplotlib-widgets-slider "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_slider_demo_thumb.png)

[Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)

Slider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_snap_demo_thumb.png)

[Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)

Snap sliders to discrete values

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#main-content)

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
    

matplotlib.widgets.RangeSlider[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib-widgets-rangeslider "Link to this heading")

=======================================================================================================================================================================

class matplotlib.widgets.RangeSlider(_ax_, _label_, _valmin_, _valmax_, _\*_, _valinit\=None_, _valfmt\=None_, _closedmin\=True_, _closedmax\=True_, _dragging\=True_, _valstep\=None_, _orientation\='horizontal'_, _track\_color\='lightgrey'_, _handle\_style\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L652-L1031)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "Link to this definition")

Bases: [`SliderBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase "matplotlib.widgets.SliderBase")

A slider representing a range of floating point values. Defines the min and max of the range via the _val_ attribute as a tuple of (min, max).

Create a slider that defines a range contained within \[_valmin_, _valmax_\] in Axes _ax_. For the slider to remain responsive you must maintain a reference to it. Call [`on_changed()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider.on_changed "matplotlib.widgets.RangeSlider.on_changed")
 to connect to the slider event.

Attributes:

**val**tuple of float

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

**valinit**tuple of float or None, default: None

The initial positions of the slider. If None the initial positions will be at the 25th and 75th percentiles of the range.

**valfmt**str or callable, default: None

The way to format the range's minimal and maximal values. If a string, it must be in %-format. If a callable, it must have the signature `valfmt(val: float) -> str`. If None, a [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 is used.

**closedmin**bool, default: True

Whether the slider interval is closed on the bottom.

**closedmax**bool, default: True

Whether the slider interval is closed on the top.

**dragging**bool, default: True

If True the slider can be dragged by the mouse.

**valstep**float, default: None

If given, the slider will snap to multiples of _valstep_.

**orientation**{'horizontal', 'vertical'}, default: 'horizontal'

The orientation of the slider.

**track\_color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: 'lightgrey'

The color of the background track. The track is accessible for further styling via the _track_ attribute.

**handle\_style**dict

Properties of the slider handles. Default values are

| Key | Value | Default | Description |
| --- | --- | --- | --- |
| facecolor | color | 'white' | The facecolor of the slider handles. |
| edgecolor | color | '.75' | The edgecolor of the slider handles. |
| size | int | 10  | The size of the slider handles in points. |

Other values will be transformed as marker{foo} and passed to the [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 constructor. e.g. `handle_style = {'style'='x'}` will result in `markerstyle = 'x'`.

Notes

Additional kwargs are passed on to `self.poly` which is the [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 that draws the slider knob. See the [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 documentation for valid property names (`facecolor`, `edgecolor`, `alpha`, etc.).

on\_changed(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L1016-L1031)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider.on_changed "Link to this definition")

Connect _func_ as callback function to changes of the slider value.

Parameters:

**func**callable

Function to call when slider is changed. The function must accept a 2-tuple of floats as its argument.

Returns:

int

Connection id (which can be used to disconnect _func_).

set\_max(_max_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L977-L985)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider.set_max "Link to this definition")

Set the lower value of the slider to _max_.

Parameters:

**max**float

set\_min(_min_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L967-L975)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider.set_min "Link to this definition")

Set the lower value of the slider to _min_.

Parameters:

**min**float

set\_val(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L987-L1014)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider.set_val "Link to this definition")

Set slider value to _val_.

Parameters:

**val**tuple or array-like of float

Examples using `matplotlib.widgets.RangeSlider`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#examples-using-matplotlib-widgets-rangeslider "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_range_slider_thumb.png)

[Image scaling using a RangeSlider](https://matplotlib.org/stable/gallery/widgets/range_slider.html)

Image scaling using a RangeSlider

On this page
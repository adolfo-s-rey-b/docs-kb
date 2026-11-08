[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#main-content)

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
    

matplotlib.axis.Axis.set\_ticks[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib-axis-axis-set-ticks "Link to this heading")

========================================================================================================================================================================

Axis.set\_ticks(_ticks_, _labels\=None_, _\*_, _minor\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L2334-L2383)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "Link to this definition")

Set this Axis' tick locations and optionally tick labels.

If necessary, the view limits of the Axis are expanded so that all given ticks are visible.

Parameters:

**ticks**1D array-like

Array of tick locations (either floats or in axis units). The axis [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 is replaced by a [`FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
.

Pass an empty list (`set_ticks([])`) to remove all ticks.

Some tick formatters will not label arbitrary tick positions; e.g. log formatters only label decade ticks by default. In such a case you can set a formatter explicitly on the axis using [`Axis.set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
 or provide formatted _labels_ yourself.

**labels**list of str, optional

Tick labels for each location in _ticks_; must have the same length as _ticks_. If set, the labels are used as is, via a [`FixedFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
. If not set, the labels are generated using the axis tick [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
.

**minor**bool, default: False

If `False`, set only the major ticks; if `True`, only the minor ticks.

**\*\*kwargs**

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties for the labels. Using these is only allowed if you pass _labels_. In other cases, please use [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
.

Notes

The mandatory expansion of the view limits is an intentional design choice to prevent the surprise of a non-visible tick. If you need other limits, you should set the limits explicitly after setting the ticks.

Examples using `matplotlib.axis.Axis.set_ticks`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#examples-using-matplotlib-axis-axis-set-ticks "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_axes_thumb.gif)

[Multiple Axes animation](https://matplotlib.org/stable/gallery/animation/multiple_axes.html)

Multiple Axes animation

On this page
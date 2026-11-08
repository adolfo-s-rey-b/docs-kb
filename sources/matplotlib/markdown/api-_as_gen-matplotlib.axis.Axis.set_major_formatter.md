[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#main-content)

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
    

matplotlib.axis.Axis.set\_major\_formatter[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib-axis-axis-set-major-formatter "Link to this heading")

=======================================================================================================================================================================================================

Axis.set\_major\_formatter(_formatter_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L2054-L2078)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "Link to this definition")

Set the formatter of the major ticker.

In addition to a [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 instance, this also accepts a `str` or function.

For a `str` a [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 is used. The field used for the value must be labeled `'x'` and the field used for the position must be labeled `'pos'`. See the [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 documentation for more information.

For a function, a [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
 is used. The function must take two inputs (a tick value `x` and a position `pos`), and return a string containing the corresponding tick label. See the [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
 documentation for more information.

Parameters:

**formatter**[`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
, `str`, or function

Examples using `matplotlib.axis.Axis.set_major_formatter`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#examples-using-matplotlib-axis-axis-set-major-formatter "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_timeline_thumb.png)

[Timeline with lines, dates, and text](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html)

Timeline with lines, dates, and text

![](https://matplotlib.org/stable/_images/sphx_glr_major_minor_demo_thumb.png)

[Major and minor ticks](https://matplotlib.org/stable/gallery/ticks/major_minor_demo.html)

Major and minor ticks

![](https://matplotlib.org/stable/_images/sphx_glr_centered_ticklabels_thumb.png)

[Center labels between ticks](https://matplotlib.org/stable/gallery/ticks/centered_ticklabels.html)

Center labels between ticks

![](https://matplotlib.org/stable/_images/sphx_glr_multilevel_ticks_thumb.png)

[Multilevel (nested) ticks](https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html)

Multilevel (nested) ticks

![](https://matplotlib.org/stable/_images/sphx_glr_tick-formatters_thumb.png)

[Tick formatters](https://matplotlib.org/stable/gallery/ticks/tick-formatters.html)

Tick formatters

![](https://matplotlib.org/stable/_images/sphx_glr_custom_ticker1_thumb.png)

[Custom Ticker](https://matplotlib.org/stable/gallery/ticks/custom_ticker1.html)

Custom Ticker

![](https://matplotlib.org/stable/_images/sphx_glr_dollar_ticks_thumb.png)

[Dollar ticks](https://matplotlib.org/stable/gallery/ticks/dollar_ticks.html)

Dollar ticks

![](https://matplotlib.org/stable/_images/sphx_glr_engineering_formatter_thumb.png)

[Format ticks using engineering notation](https://matplotlib.org/stable/gallery/ticks/engineering_formatter.html)

Format ticks using engineering notation

![](https://matplotlib.org/stable/_images/sphx_glr_engformatter_offset_thumb.png)

[SI prefixed offsets and natural order of magnitudes](https://matplotlib.org/stable/gallery/ticks/engformatter_offset.html)

SI prefixed offsets and natural order of magnitudes

![](https://matplotlib.org/stable/_images/sphx_glr_tick_labels_from_values_thumb.png)

[Setting tick labels from a list of values](https://matplotlib.org/stable/gallery/ticks/tick_labels_from_values.html)

Setting tick labels from a list of values

![](https://matplotlib.org/stable/_images/sphx_glr_date_thumb.png)

[Date tick labels](https://matplotlib.org/stable/gallery/ticks/date.html)

Date tick labels

![](https://matplotlib.org/stable/_images/sphx_glr_date_formatters_locators_thumb.png)

[Date tick locators and formatters](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html)

Date tick locators and formatters

![](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_thumb.png)

[Format date ticks using ConciseDateFormatter](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html)

Format date ticks using ConciseDateFormatter

![](https://matplotlib.org/stable/_images/sphx_glr_date_demo_convert_thumb.png)

[Date converter demo](https://matplotlib.org/stable/gallery/ticks/date_demo_convert.html)

Date converter demo

![](https://matplotlib.org/stable/_images/sphx_glr_date_demo_rrule_thumb.png)

[Placing date ticks using recurrence rules](https://matplotlib.org/stable/gallery/ticks/date_demo_rrule.html)

Placing date ticks using recurrence rules

![](https://matplotlib.org/stable/_images/sphx_glr_date_index_formatter_thumb.png)

[Custom tick formatter for time series](https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html)

Custom tick formatter for time series

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_thumb.png)

[3D surface (colormap)](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)

3D surface (colormap)

![](https://matplotlib.org/stable/_images/sphx_glr_skewt_thumb.png)

[SkewT-logP diagram: using transforms and custom projections](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html)

SkewT-logP diagram: using transforms and custom projections

![](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_thumb.png)

[The Lifecycle of a Plot](https://matplotlib.org/stable/tutorials/lifecycle.html)

The Lifecycle of a Plot

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

![](https://matplotlib.org/stable/_images/sphx_glr_axes_units_thumb.png)

[Plotting dates and strings](https://matplotlib.org/stable/users/explain/axes/axes_units.html)

Plotting dates and strings

![](https://matplotlib.org/stable/_images/sphx_glr_colormaps_thumb.png)

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choosing Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page
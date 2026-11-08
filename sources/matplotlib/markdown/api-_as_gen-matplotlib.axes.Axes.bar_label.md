[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#main-content)

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
    

matplotlib.axes.Axes.bar\_label[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib-axes-axes-bar-label "Link to this heading")

========================================================================================================================================================================

Axes.bar\_label(_container_, _labels\=None_, _\*_, _fmt\='%g'_, _label\_type\='edge'_, _padding\=0_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L2798-L2969)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "Link to this definition")

Label a bar plot.

Adds labels to bars in the given [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
. You may need to adjust the axis limits to fit the labels.

Parameters:

**container**[`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")

Container with all the bars and optionally errorbars, likely returned from [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 or [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
.

**labels**array-like, optional

A list of label texts, that should be displayed. If not given, the label texts will be the data values formatted with _fmt_.

**fmt**str or callable, default: '%g'

An unnamed %-style or {}-style format string for the label or a function to call with the value as the first argument. When _fmt_ is a string and can be interpreted in both formats, %-style takes precedence over {}-style.

Added in version 3.7: Support for {}-style format string and callables.

**label\_type**{'edge', 'center'}, default: 'edge'

The label type. Possible values:

*   'edge': label placed at the end-point of the bar segment, and the value displayed will be the position of that end-point.
    
*   'center': label placed in the center of the bar segment, and the value displayed will be the length of that segment. (useful for stacked bars, i.e., [Bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html)
    )
    

**padding**float or array-like, default: 0

Distance of label from the end of the bar, in points. If an array-like is provided, the padding values are applied to each label individually. Must have the same length as container. .. versionadded:: 3.11

**\*\*kwargs**

Any remaining keyword arguments are passed through to [`Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
. The alignment parameters ( _horizontalalignment_ / _ha_, _verticalalignment_ / _va_) are not supported because the labels are automatically aligned to the bars.

Returns:

list of [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")

A list of [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 instances for the labels.

Examples using `matplotlib.axes.Axes.bar_label`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#examples-using-matplotlib-axes-axes-bar-label "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_barchart_thumb.png)

[Grouped bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)

Grouped bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_bar_label_demo_thumb.png)

[Bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html)

Bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_hat_graph_thumb.png)

[Hat graph](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html)

Hat graph

![](https://matplotlib.org/stable/_images/sphx_glr_horizontal_barchart_distribution_thumb.png)

[Discrete distribution as horizontal bar chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html)

Discrete distribution as horizontal bar chart

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

On this page
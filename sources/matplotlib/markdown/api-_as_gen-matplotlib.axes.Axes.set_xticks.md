[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#main-content)

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
    

matplotlib.axes.Axes.set\_xticks[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib-axes-axes-set-xticks "Link to this heading")

===========================================================================================================================================================================

Axes.set\_xticks(_ticks_, _labels\=None_, _\*_, _minor\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L74-L75)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "Link to this definition")

Set the xaxis' tick locations and optionally tick labels.

If necessary, the view limits of the Axis are expanded so that all given ticks are visible.

Parameters:

**ticks**1D array-like

Array of tick locations (either floats or in axis units). The axis [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 is replaced by a [`FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
.

Pass an empty list (`set_xticks([])`) to remove all ticks.

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

Examples using `matplotlib.axes.Axes.set_xticks`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#examples-using-matplotlib-axes-axes-set-xticks "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_thumb.png)

[Streamplot](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_histograms_side_by_side_thumb.png)

[Multiple histograms side by side](https://matplotlib.org/stable/gallery/statistics/multiple_histograms_side_by_side.html)

Multiple histograms side by side

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_vs_violin_thumb.png)

[Box plot vs. violin plot comparison](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html)

Box plot vs. violin plot comparison

![](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_thumb.png)

[Violin plot customization](https://matplotlib.org/stable/gallery/statistics/customized_violin.html)

Violin plot customization

![](https://matplotlib.org/stable/_images/sphx_glr_psd_demo_thumb.png)

[Power spectral density (PSD)](https://matplotlib.org/stable/gallery/statistics/psd_demo.html)

Power spectral density (PSD)

![](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_thumb.png)

[Render math equations using TeX](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

Render math equations using TeX

![](https://matplotlib.org/stable/_images/sphx_glr_ggplot_thumb.png)

[ggplot style sheet](https://matplotlib.org/stable/gallery/style_sheets/ggplot.html)

ggplot style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_locatable_axes_thumb.png)

[Align histogram to scatter plot using locatable Axes](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html)

Align histogram to scatter plot using locatable Axes

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline4_thumb.png)

[Simple Axisline4](https://matplotlib.org/stable/gallery/axes_grid1/simple_axisline4.html)

Simple Axisline4

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_alignment_thumb.png)

[Ticklabel alignment](https://matplotlib.org/stable/gallery/axisartist/demo_ticklabel_alignment.html)

Ticklabel alignment

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_direction_thumb.png)

[Ticklabel direction](https://matplotlib.org/stable/gallery/axisartist/demo_ticklabel_direction.html)

Ticklabel direction

![](https://matplotlib.org/stable/_images/sphx_glr_rain_thumb.gif)

[Rain simulation](https://matplotlib.org/stable/gallery/animation/rain.html)

Rain simulation

![](https://matplotlib.org/stable/_images/sphx_glr_unchained_thumb.gif)

[Matplotlib unchained](https://matplotlib.org/stable/gallery/animation/unchained.html)

Matplotlib unchained

![](https://matplotlib.org/stable/_images/sphx_glr_bar_unit_demo_thumb.png)

[Group barchart with units](https://matplotlib.org/stable/gallery/units/bar_unit_demo.html)

Group barchart with units

![](https://matplotlib.org/stable/_images/sphx_glr_integral_thumb.png)

[Integral as the area under a curve](https://matplotlib.org/stable/gallery/showcase/integral.html)

Integral as the area under a curve

![](https://matplotlib.org/stable/_images/sphx_glr_mandelbrot_thumb.png)

[Shaded & power normalized rendering](https://matplotlib.org/stable/gallery/showcase/mandelbrot.html)

Shaded & power normalized rendering

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

![](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_thumb.png)

[The Lifecycle of a Plot](https://matplotlib.org/stable/tutorials/lifecycle.html)

The Lifecycle of a Plot

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

On this page
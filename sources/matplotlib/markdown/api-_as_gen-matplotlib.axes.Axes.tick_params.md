[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#main-content)

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
    

matplotlib.axes.Axes.tick\_params[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib-axes-axes-tick-params "Link to this heading")

==============================================================================================================================================================================

Axes.tick\_params(_axis\='both'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L3627-L3709)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "Link to this definition")

Change the appearance of ticks, tick labels, and gridlines.

Tick properties that are not explicitly set using the keyword arguments remain unchanged unless _reset_ is True. For the current style settings, see [`Axis.get_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib.axis.Axis.get_tick_params "matplotlib.axis.Axis.get_tick_params")
.

Parameters:

**axis**{'x', 'y', 'both'}, default: 'both'

The axis to which the parameters are applied.

**which**{'major', 'minor', 'both'}, default: 'major'

The group of ticks to which the parameters are applied.

**reset**bool, default: False

Whether to reset the ticks to defaults before updating them.

Other Parameters:

**direction**{'in', 'out', 'inout'}

Puts ticks inside the Axes, outside the Axes, or both.

**length**float

Tick length in points.

**width**float

Tick width in points.

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Tick color.

**pad**float

Distance in points between tick and label.

**labelsize**float or str

Tick label font size in points or as a string (e.g., 'large').

**labelcolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Tick label color.

**labelfontfamily**str

Tick label font.

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Tick color and label color.

**zorder**float

Tick and label zorder.

**bottom, top, left, right**bool

Whether to draw the respective ticks.

**labelbottom, labeltop, labelleft, labelright**bool

Whether to draw the respective tick labels.

**labelrotation**float

Tick label rotation angle in degrees. See [`Text.set_rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation")
.

**labelrotation\_mode**{'default', 'anchor', 'xtick', 'ytick'}

Tick label rotation mode. See [`Text.set_rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode")
.

**grid\_color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Gridline color.

**grid\_alpha**float

Transparency of gridlines: 0 (transparent) to 1 (opaque).

**grid\_linewidth**float

Width of gridlines in points.

**grid\_linestyle**str

Any valid [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 line style spec.

Examples

ax.tick\_params(direction\='out', length\=6, width\=2, colors\='r',
               grid\_color\='r', grid\_alpha\=0.5)

This will make all major ticks be red, pointing out of the box, and with dimensions 6 points by 2 points. Tick labels will also be red. Gridlines will be red and translucent.

Examples using `matplotlib.axes.Axes.tick_params`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#examples-using-matplotlib-axes-axes-tick-params "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_thumb.png)

[Scatter plot with histograms](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html)

Scatter plot with histograms

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_polar_legend_thumb.png)

[Polar legend](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html)

Polar legend

![](https://matplotlib.org/stable/_images/sphx_glr_two_scales_thumb.png)

[Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)

Plots with different scales

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_yaxis_with_spines_thumb.png)

[Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)

Multiple y-axis with Spines

![](https://matplotlib.org/stable/_images/sphx_glr_axes_props_thumb.png)

[Axes properties](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_props.html)

Axes properties

![](https://matplotlib.org/stable/_images/sphx_glr_broken_axis_thumb.png)

[Broken axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html)

Broken axis

![](https://matplotlib.org/stable/_images/sphx_glr_major_minor_demo_thumb.png)

[Major and minor ticks](https://matplotlib.org/stable/gallery/ticks/major_minor_demo.html)

Major and minor ticks

![](https://matplotlib.org/stable/_images/sphx_glr_align_ticklabels_thumb.png)

[Align tick labels](https://matplotlib.org/stable/gallery/ticks/align_ticklabels.html)

Align tick labels

![](https://matplotlib.org/stable/_images/sphx_glr_ticks_top_right_thumb.png)

[Move x/y-axis ticks and labels on top and right](https://matplotlib.org/stable/gallery/ticks/ticks_top_right.html)

Move x/y-axis ticks and labels on top and right

![](https://matplotlib.org/stable/_images/sphx_glr_centered_ticklabels_thumb.png)

[Center labels between ticks](https://matplotlib.org/stable/gallery/ticks/centered_ticklabels.html)

Center labels between ticks

![](https://matplotlib.org/stable/_images/sphx_glr_ticklabels_rotation_thumb.png)

[Rotated tick labels](https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html)

Rotated tick labels

![](https://matplotlib.org/stable/_images/sphx_glr_date_formatters_locators_thumb.png)

[Date tick locators and formatters](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html)

Date tick locators and formatters

![](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_thumb.png)

[Format date ticks using ConciseDateFormatter](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html)

Format date ticks using ConciseDateFormatter

![](https://matplotlib.org/stable/_images/sphx_glr_fig_axes_customize_simple_thumb.png)

[Customizing figure and axes appearance](https://matplotlib.org/stable/gallery/ticks/fig_axes_customize_simple.html)

Customizing figure and axes appearance

![](https://matplotlib.org/stable/_images/sphx_glr_color_demo_thumb.png)

[Color Demo](https://matplotlib.org/stable/gallery/color/color_demo.html)

Color Demo

![](https://matplotlib.org/stable/_images/sphx_glr_color_sequences_thumb.png)

[Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)

Named color sequences

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_histogram_thumb.png)

[Histogram as colorbar](https://matplotlib.org/stable/gallery/color/colorbar_histogram.html)

Histogram as colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid_thumb.png)

[Demo Axes Grid](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid.html)

Demo Axes Grid

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_thumb.png)

[Inset locator demo](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html)

Inset locator demo

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo2_thumb.png)

[Inset locator demo 2](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html)

Inset locator demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_make_room_for_ylabel_using_axesgrid_thumb.png)

[Make room for ylabel using axes\_grid](https://matplotlib.org/stable/gallery/axes_grid1/make_room_for_ylabel_using_axesgrid.html)

Make room for ylabel using axes\_grid

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider3_thumb.png)

[Simple axes divider 3](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider3.html)

Simple axes divider 3

![](https://matplotlib.org/stable/_images/sphx_glr_evans_test_thumb.png)

[Evans test](https://matplotlib.org/stable/gallery/units/evans_test.html)

Evans test

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

![](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_thumb.png)

[Stock prices over 32 years](https://matplotlib.org/stable/gallery/showcase/stock_prices.html)

Stock prices over 32 years

![](https://matplotlib.org/stable/_images/sphx_glr_anscombe_thumb.png)

[Anscombe's quartet](https://matplotlib.org/stable/gallery/specialty_plots/anscombe.html)

Anscombe's quartet

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page
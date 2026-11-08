[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#main-content)

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
    

matplotlib.axes.Axes.set\_xlim[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib-axes-axes-set-xlim "Link to this heading")

=====================================================================================================================================================================

Axes.set\_xlim(_left\=None_, _right\=None_, _\*_, _emit\=True_, _auto\=False_, _xmin\=None_, _xmax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L3916-L3992)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "Link to this definition")

Set the x-axis view limits.

Parameters:

**left**float, optional

The left xlim in data coordinates. Passing _None_ leaves the limit unchanged.

The left and right xlims may also be passed as the tuple (_left_, _right_) as the first positional argument (or as the _left_ keyword argument).

**right**float, optional

The right xlim in data coordinates. Passing _None_ leaves the limit unchanged.

**emit**bool, default: True

Whether to notify observers of limit change.

**auto**bool or None, default: False

Whether to turn on autoscaling of the x-axis. True turns on, False turns off, None leaves unchanged.

**xmin, xmax**float, optional

They are equivalent to left and right respectively, and it is an error to pass both _xmin_ and _left_ or _xmax_ and _right_.

Returns:

**left, right**(float, float)

The new x-axis limits in data coordinates.

See also

[`get_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#matplotlib.axes.Axes.get_xlim "matplotlib.axes.Axes.get_xlim")

[`set_xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound")
, [`get_xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xbound.html#matplotlib.axes.Axes.get_xbound "matplotlib.axes.Axes.get_xbound")

[`invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_xaxis.html#matplotlib.axes.Axes.invert_xaxis "matplotlib.axes.Axes.invert_xaxis")
, [`xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_inverted.html#matplotlib.axes.Axes.xaxis_inverted "matplotlib.axes.Axes.xaxis_inverted")

Notes

The _left_ value may be greater than the _right_ value, in which case the x-axis values will decrease from left to right.

Examples

\>>> set\_xlim(left, right)
\>>> set\_xlim((left, right))
\>>> left, right \= set\_xlim(left, right)

One limit may be left unchanged.

\>>> set\_xlim(right\=right\_lim)

Limits may be passed in reverse order to flip the direction of the x-axis. For example, suppose _x_ represents the number of years before present. The x-axis limits might be set like the following so 5000 years ago is on the left of the plot and the present is on the right.

\>>> set\_xlim(5000, 0)

Examples using `matplotlib.axes.Axes.set_xlim`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#examples-using-matplotlib-axes-axes-set-xlim "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_thumb.png)

[Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)

Markevery Demo

![](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_thumb.png)

[Multicolored lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html)

Multicolored lines

![](https://matplotlib.org/stable/_images/sphx_glr_bar_label_demo_thumb.png)

[Bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html)

Bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_broken_barh_thumb.png)

[Broken horizontal bars](https://matplotlib.org/stable/gallery/lines_bars_and_markers/broken_barh.html)

Broken horizontal bars

![](https://matplotlib.org/stable/_images/sphx_glr_eventcollection_demo_thumb.png)

[EventCollection Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html)

EventCollection Demo

![](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_thumb.png)

[Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)

Image resampling

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_grids_thumb.png)

[pcolormesh grids and shading](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_grids.html)

pcolormesh grids and shading

![](https://matplotlib.org/stable/_images/sphx_glr_image_nonuniform_thumb.png)

[Image nonuniform](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_nonuniform.html)

Image nonuniform

![](https://matplotlib.org/stable/_images/sphx_glr_contours_in_optimization_demo_thumb.png)

[Contouring the solution space of optimizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html)

Contouring the solution space of optimizations

![](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_thumb.png)

[Streamplot](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot

![](https://matplotlib.org/stable/_images/sphx_glr_specgram_demo_thumb.png)

[Spectrogram](https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html)

Spectrogram

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_limits_thumb.png)

[Including upper and lower limits in error bars](https://matplotlib.org/stable/gallery/statistics/errorbar_limits.html)

Including upper and lower limits in error bars

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_thumb.png)

[Violin plot customization](https://matplotlib.org/stable/gallery/statistics/customized_violin.html)

Violin plot customization

![](https://matplotlib.org/stable/_images/sphx_glr_csd_demo_thumb.png)

[Cross spectral density (CSD)](https://matplotlib.org/stable/gallery/statistics/csd_demo.html)

Cross spectral density (CSD)

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

![](https://matplotlib.org/stable/_images/sphx_glr_axes_demo_thumb.png)

[Axes Demo](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_demo.html)

Axes Demo

![](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_thumb.png)

[Axes box aspect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html)

Axes box aspect

![](https://matplotlib.org/stable/_images/sphx_glr_invert_axes_thumb.png)

[Inverted axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/invert_axes.html)

Inverted axis

![](https://matplotlib.org/stable/_images/sphx_glr_multilevel_ticks_thumb.png)

[Multilevel (nested) ticks](https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html)

Multilevel (nested) ticks

![](https://matplotlib.org/stable/_images/sphx_glr_date_formatters_locators_thumb.png)

[Date tick locators and formatters](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html)

Date tick locators and formatters

![](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_thumb.png)

[Format date ticks using ConciseDateFormatter](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html)

Format date ticks using ConciseDateFormatter

![](https://matplotlib.org/stable/_images/sphx_glr_date_demo_convert_thumb.png)

[Date converter demo](https://matplotlib.org/stable/gallery/ticks/date_demo_convert.html)

Date converter demo

![](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_thumb.png)

[Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)

Asinh scale

![](https://matplotlib.org/stable/_images/sphx_glr_aspect_loglog_thumb.png)

[Loglog aspect](https://matplotlib.org/stable/gallery/scales/aspect_loglog.html)

Loglog aspect

![](https://matplotlib.org/stable/_images/sphx_glr_multiline_thumb.png)

[Multiline text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/multiline.html)

Multiline text

![](https://matplotlib.org/stable/_images/sphx_glr_text_rotation_relative_to_line_thumb.png)

[Text rotation angle in data coordinates](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_rotation_relative_to_line.html)

Text rotation angle in data coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_demo_text_path_thumb.png)

[Using a text as a Path](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html)

Using a text as a Path

![](https://matplotlib.org/stable/_images/sphx_glr_fancyarrow_demo_thumb.png)

[Annotation arrow style reference](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html)

Annotation arrow style reference

![](https://matplotlib.org/stable/_images/sphx_glr_donut_thumb.png)

[Mmh Donuts!!!](https://matplotlib.org/stable/gallery/shapes_and_collections/donut.html)

Mmh Donuts!!!

![](https://matplotlib.org/stable/_images/sphx_glr_hatchcolor_demo_thumb.png)

[Hatchcolor Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatchcolor_demo.html)

Hatchcolor Demo

![](https://matplotlib.org/stable/_images/sphx_glr_line_collection_thumb.png)

[Plot multiple lines using a LineCollection](https://matplotlib.org/stable/gallery/shapes_and_collections/line_collection.html)

Plot multiple lines using a LineCollection

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_pathpatch3d_thumb.png)

[Draw flat objects in 3D plot](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html)

Draw flat objects in 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_text3d_thumb.png)

[Text annotations in 3D](https://matplotlib.org/stable/gallery/mplot3d/text3d.html)

Text annotations in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo2_thumb.png)

[Inset locator demo 2](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html)

Inset locator demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple2_thumb.png)

[Parasite Simple2](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple2.html)

Parasite Simple2

![](https://matplotlib.org/stable/_images/sphx_glr_animate_decay_thumb.gif)

[Decay](https://matplotlib.org/stable/gallery/animation/animate_decay.html)

Decay

![](https://matplotlib.org/stable/_images/sphx_glr_rain_thumb.gif)

[Rain simulation](https://matplotlib.org/stable/gallery/animation/rain.html)

Rain simulation

![](https://matplotlib.org/stable/_images/sphx_glr_simple_scatter_thumb.gif)

[Animated scatter saved as GIF](https://matplotlib.org/stable/gallery/animation/simple_scatter.html)

Animated scatter saved as GIF

![](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_thumb.png)

[Annotated cursor](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html)

Annotated cursor

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_thumb.png)

[Cursor](https://matplotlib.org/stable/gallery/widgets/cursor.html)

Cursor

![](https://matplotlib.org/stable/_images/sphx_glr_span_selector_thumb.png)

[Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

Span Selector

![](https://matplotlib.org/stable/_images/sphx_glr_path_editor_thumb.png)

[Path editor](https://matplotlib.org/stable/gallery/event_handling/path_editor.html)

Path editor

![](https://matplotlib.org/stable/_images/sphx_glr_poly_editor_thumb.png)

[Polygon editor](https://matplotlib.org/stable/gallery/event_handling/poly_editor.html)

Polygon editor

![](https://matplotlib.org/stable/_images/sphx_glr_resample_thumb.png)

[Resampling Data](https://matplotlib.org/stable/gallery/event_handling/resample.html)

Resampling Data

![](https://matplotlib.org/stable/_images/sphx_glr_zoom_window_thumb.png)

[Zoom modifies other Axes](https://matplotlib.org/stable/gallery/event_handling/zoom_window.html)

Zoom modifies other Axes

![](https://matplotlib.org/stable/_images/sphx_glr_annotate_with_units_thumb.png)

[Annotation with units](https://matplotlib.org/stable/gallery/units/annotate_with_units.html)

Annotation with units

![](https://matplotlib.org/stable/_images/sphx_glr_artist_tests_thumb.png)

[Artist tests](https://matplotlib.org/stable/gallery/units/artist_tests.html)

Artist tests

![](https://matplotlib.org/stable/_images/sphx_glr_custom_projection_thumb.png)

[Custom projection](https://matplotlib.org/stable/gallery/misc/custom_projection.html)

Custom projection

![](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_line_thumb.png)

[Apply SVG filter to a line](https://matplotlib.org/stable/gallery/misc/svg_filter_line.html)

Apply SVG filter to a line

![](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_thumb.png)

[TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)

TickedStroke patheffect

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

![](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_thumb.png)

[Stock prices over 32 years](https://matplotlib.org/stable/gallery/showcase/stock_prices.html)

Stock prices over 32 years

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

![](https://matplotlib.org/stable/_images/sphx_glr_ishikawa_diagram_thumb.png)

[Ishikawa Diagram](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html)

Ishikawa Diagram

![](https://matplotlib.org/stable/_images/sphx_glr_skewt_thumb.png)

[SkewT-logP diagram: using transforms and custom projections](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html)

SkewT-logP diagram: using transforms and custom projections

![](https://matplotlib.org/stable/_images/sphx_glr_paths_thumb.png)

[Path Tutorial](https://matplotlib.org/stable/users/explain/artists/paths.html)

Path Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_axes_scales_thumb.png)

[Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)

Axis scales

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

![](https://matplotlib.org/stable/_images/sphx_glr_axes_units_thumb.png)

[Plotting dates and strings](https://matplotlib.org/stable/users/explain/axes/axes_units.html)

Plotting dates and strings

![](https://matplotlib.org/stable/_images/sphx_glr_colormaps_thumb.png)

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choosing Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

On this page
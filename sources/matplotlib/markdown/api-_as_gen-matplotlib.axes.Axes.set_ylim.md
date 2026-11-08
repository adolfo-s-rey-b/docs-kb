[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#main-content)

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
    

matplotlib.axes.Axes.set\_ylim[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib-axes-axes-set-ylim "Link to this heading")

=====================================================================================================================================================================

Axes.set\_ylim(_bottom\=None_, _top\=None_, _\*_, _emit\=True_, _auto\=False_, _ymin\=None_, _ymax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L4165-L4241)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "Link to this definition")

Set the y-axis view limits.

Parameters:

**bottom**float, optional

The bottom ylim in data coordinates. Passing _None_ leaves the limit unchanged.

The bottom and top ylims may also be passed as the tuple (_bottom_, _top_) as the first positional argument (or as the _bottom_ keyword argument).

**top**float, optional

The top ylim in data coordinates. Passing _None_ leaves the limit unchanged.

**emit**bool, default: True

Whether to notify observers of limit change.

**auto**bool or None, default: False

Whether to turn on autoscaling of the y-axis. _True_ turns on, _False_ turns off, _None_ leaves unchanged.

**ymin, ymax**float, optional

They are equivalent to bottom and top respectively, and it is an error to pass both _ymin_ and _bottom_ or _ymax_ and _top_.

Returns:

**bottom, top**(float, float)

The new y-axis limits in data coordinates.

See also

[`get_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylim.html#matplotlib.axes.Axes.get_ylim "matplotlib.axes.Axes.get_ylim")

[`set_ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound")
, [`get_ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ybound.html#matplotlib.axes.Axes.get_ybound "matplotlib.axes.Axes.get_ybound")

[`invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis")
, [`yaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis_inverted.html#matplotlib.axes.Axes.yaxis_inverted "matplotlib.axes.Axes.yaxis_inverted")

Notes

The _bottom_ value may be greater than the _top_ value, in which case the y-axis values will decrease from _bottom_ to _top_.

Examples

\>>> set\_ylim(bottom, top)
\>>> set\_ylim((bottom, top))
\>>> bottom, top \= set\_ylim(bottom, top)

One limit may be left unchanged.

\>>> set\_ylim(top\=top\_lim)

Limits may be passed in reverse order to flip the direction of the y-axis. For example, suppose `y` represents depth of the ocean in m. The y-axis limits might be set like the following so 5000 m depth is at the bottom of the plot and the surface, 0 m, is at the top.

\>>> set\_ylim(5000, 0)

Examples using `matplotlib.axes.Axes.set_ylim`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#examples-using-matplotlib-axes-axes-set-ylim "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_thumb.png)

[Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)

Markevery Demo

![](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_thumb.png)

[Multicolored lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html)

Multicolored lines

![](https://matplotlib.org/stable/_images/sphx_glr_barchart_thumb.png)

[Grouped bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)

Grouped bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_hat_graph_thumb.png)

[Hat graph](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html)

Hat graph

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

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_psd_demo_thumb.png)

[Power spectral density (PSD)](https://matplotlib.org/stable/gallery/statistics/psd_demo.html)

Power spectral density (PSD)

![](https://matplotlib.org/stable/_images/sphx_glr_axes_demo_thumb.png)

[Axes Demo](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_demo.html)

Axes Demo

![](https://matplotlib.org/stable/_images/sphx_glr_align_labels_demo_thumb.png)

[Align labels and titles](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html)

Align labels and titles

![](https://matplotlib.org/stable/_images/sphx_glr_broken_axis_thumb.png)

[Broken axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html)

Broken axis

![](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_thumb.png)

[Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)

Asinh scale

![](https://matplotlib.org/stable/_images/sphx_glr_aspect_loglog_thumb.png)

[Loglog aspect](https://matplotlib.org/stable/gallery/scales/aspect_loglog.html)

Loglog aspect

![](https://matplotlib.org/stable/_images/sphx_glr_demo_text_path_thumb.png)

[Using a text as a Path](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html)

Using a text as a Path

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_basic_thumb.png)

[Annotating a plot](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_basic.html)

Annotating a plot

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

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline_thumb.png)

[Simple Axisline](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html)

Simple Axisline

![](https://matplotlib.org/stable/_images/sphx_glr_animate_decay_thumb.gif)

[Decay](https://matplotlib.org/stable/gallery/animation/animate_decay.html)

Decay

![](https://matplotlib.org/stable/_images/sphx_glr_animated_histogram_thumb.gif)

[Animated histogram](https://matplotlib.org/stable/gallery/animation/animated_histogram.html)

Animated histogram

![](https://matplotlib.org/stable/_images/sphx_glr_rain_thumb.gif)

[Rain simulation](https://matplotlib.org/stable/gallery/animation/rain.html)

Rain simulation

![](https://matplotlib.org/stable/_images/sphx_glr_unchained_thumb.gif)

[Matplotlib unchained](https://matplotlib.org/stable/gallery/animation/unchained.html)

Matplotlib unchained

![](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_thumb.png)

[Annotated cursor](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html)

Annotated cursor

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_thumb.png)

[Cursor](https://matplotlib.org/stable/gallery/widgets/cursor.html)

Cursor

![](https://matplotlib.org/stable/_images/sphx_glr_span_selector_thumb.png)

[Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

Span Selector

![](https://matplotlib.org/stable/_images/sphx_glr_data_browser_thumb.png)

[Data browser](https://matplotlib.org/stable/gallery/event_handling/data_browser.html)

Data browser

![](https://matplotlib.org/stable/_images/sphx_glr_path_editor_thumb.png)

[Path editor](https://matplotlib.org/stable/gallery/event_handling/path_editor.html)

Path editor

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo2_thumb.png)

[Pick event demo 2](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo2.html)

Pick event demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_poly_editor_thumb.png)

[Polygon editor](https://matplotlib.org/stable/gallery/event_handling/poly_editor.html)

Polygon editor

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

![](https://matplotlib.org/stable/_images/sphx_glr_integral_thumb.png)

[Integral as the area under a curve](https://matplotlib.org/stable/gallery/showcase/integral.html)

Integral as the area under a curve

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

![](https://matplotlib.org/stable/_images/sphx_glr_ishikawa_diagram_thumb.png)

[Ishikawa Diagram](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html)

Ishikawa Diagram

![](https://matplotlib.org/stable/_images/sphx_glr_skewt_thumb.png)

[SkewT-logP diagram: using transforms and custom projections](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html)

SkewT-logP diagram: using transforms and custom projections

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_paths_thumb.png)

[Path Tutorial](https://matplotlib.org/stable/users/explain/artists/paths.html)

Path Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_placement_thumb.png)

[Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)

Placing colorbars

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colormaps_thumb.png)

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choosing Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

On this page
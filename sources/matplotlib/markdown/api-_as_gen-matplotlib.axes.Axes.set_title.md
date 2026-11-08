[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#main-content)

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
    

matplotlib.axes.Axes.set\_title[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib-axes-axes-set-title "Link to this heading")

========================================================================================================================================================================

Axes.set\_title(_label_, _fontdict\=None_, _loc\=None_, _pad\=None_, _\*_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L138-L217)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "Link to this definition")

Set a title for the Axes.

Set one of the three available Axes titles. The available titles are positioned above the Axes in the center, flush with the left edge, and flush with the right edge.

Parameters:

**label**str

Text to use for the title

**fontdict**dict

Discouraged

The use of _fontdict_ is discouraged. Parameters should be passed as individual keyword arguments or using dictionary-unpacking `set_title(..., **fontdict)`.

A dictionary controlling the appearance of the title text, the default _fontdict_ is:

{'fontsize': rcParams\['axes.titlesize'\],
 'fontweight': rcParams\['axes.titleweight'\],
 'color': rcParams\['axes.titlecolor'\],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}

**loc**{'center', 'left', 'right'}, default: `[rcParams["axes.titlelocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlelocation#rcparam-axes-titlelocation) ` (default: `'center'`)

Which title to set.

**y**float, default: `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`)

Vertical Axes location for the title (1.0 is the top). If None (the default) and `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`) is also None, y is determined automatically to avoid decorators on the Axes.

**pad**float, default: `[rcParams["axes.titlepad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlepad#rcparam-axes-titlepad) ` (default: `6.0`)

The offset of the title from the top of the Axes, in points.

Returns:

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The matplotlib text instance representing the title

Other Parameters:

**\*\*kwargs**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties

Other keyword arguments are text properties, see [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 for a list of valid text properties.

Examples using `matplotlib.axes.Axes.set_title`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#examples-using-matplotlib-axes-axes-set-title "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_thumb.png)

[Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)

Markevery Demo

![](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_thumb.png)

[Multicolored lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html)

Multicolored lines

![](https://matplotlib.org/stable/_images/sphx_glr_barchart_thumb.png)

[Grouped bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)

Grouped bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_bar_label_demo_thumb.png)

[Bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html)

Bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_bar_stacked_thumb.png)

[Stacked bar chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html)

Stacked bar chart

![](https://matplotlib.org/stable/_images/sphx_glr_bar_colors_thumb.png)

[Bar chart with individual bar colors](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html)

Bar chart with individual bar colors

![](https://matplotlib.org/stable/_images/sphx_glr_hat_graph_thumb.png)

[Hat graph](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html)

Hat graph

![](https://matplotlib.org/stable/_images/sphx_glr_barh_thumb.png)

[Horizontal bar chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barh.html)

Horizontal bar chart

![](https://matplotlib.org/stable/_images/sphx_glr_broken_barh_thumb.png)

[Broken horizontal bars](https://matplotlib.org/stable/gallery/lines_bars_and_markers/broken_barh.html)

Broken horizontal bars

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_demo2_thumb.png)

[Scatter Demo2](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html)

Scatter Demo2

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_alpha_thumb.png)

[fill\_between with transparency](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html)

fill\_between with transparency

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_demo_thumb.png)

[Fill the area between two lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html)

Fill the area between two lines

![](https://matplotlib.org/stable/_images/sphx_glr_fill_betweenx_demo_thumb.png)

[Fill the area between two vertical lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_betweenx_demo.html)

Fill the area between two vertical lines

![](https://matplotlib.org/stable/_images/sphx_glr_stackplot_demo_thumb.png)

[Stackplots and streamgraphs](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stackplot_demo.html)

Stackplots and streamgraphs

![](https://matplotlib.org/stable/_images/sphx_glr_eventcollection_demo_thumb.png)

[EventCollection Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html)

EventCollection Demo

![](https://matplotlib.org/stable/_images/sphx_glr_vline_hline_demo_thumb.png)

[hlines and vlines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/vline_hline_demo.html)

hlines and vlines

![](https://matplotlib.org/stable/_images/sphx_glr_image_demo_thumb.png)

[Many ways to plot images](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html)

Many ways to plot images

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_thumb.png)

[Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)

Image resampling

![](https://matplotlib.org/stable/_images/sphx_glr_interpolation_methods_thumb.png)

[Interpolations for imshow](https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html)

Interpolations for imshow

![](https://matplotlib.org/stable/_images/sphx_glr_pcolor_demo_thumb.png)

[pcolor images](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolor_demo.html)

pcolor images

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_levels_thumb.png)

[pcolormesh](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html)

pcolormesh

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_grids_thumb.png)

[pcolormesh grids and shading](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_grids.html)

pcolormesh grids and shading

![](https://matplotlib.org/stable/_images/sphx_glr_image_nonuniform_thumb.png)

[Image nonuniform](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_nonuniform.html)

Image nonuniform

![](https://matplotlib.org/stable/_images/sphx_glr_triplot_demo_thumb.png)

[Triplot Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triplot_demo.html)

Triplot Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tripcolor_demo_thumb.png)

[Tripcolor Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/tripcolor_demo.html)

Tripcolor Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_demo_thumb.png)

[Tricontour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_demo.html)

Tricontour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_user_thumb.png)

[Tricontour Smooth User](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_user.html)

Tricontour Smooth User

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_delaunay_thumb.png)

[Tricontour Smooth Delaunay](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_delaunay.html)

Tricontour Smooth Delaunay

![](https://matplotlib.org/stable/_images/sphx_glr_trigradient_demo_thumb.png)

[Trigradient Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/trigradient_demo.html)

Trigradient Demo

![](https://matplotlib.org/stable/_images/sphx_glr_irregulardatagrid_thumb.png)

[Contour plot of irregularly spaced data](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html)

Contour plot of irregularly spaced data

![](https://matplotlib.org/stable/_images/sphx_glr_contour_demo_thumb.png)

[Contour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html)

Contour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_label_demo_thumb.png)

[Contour Label Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_label_demo.html)

Contour Label Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_demo_thumb.png)

[Contourf demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html)

Contourf demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_corner_mask_thumb.png)

[Contour corner mask](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_corner_mask.html)

Contour corner mask

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_demo_thumb.png)

[Advanced quiver and quiverkey functions](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_demo.html)

Advanced quiver and quiverkey functions

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_interactive_adjustment_thumb.png)

[Interactive adjustment of colormap range](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_interactive_adjustment.html)

Interactive adjustment of colormap range

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_features_thumb.png)

[Different ways of specifying error bars](https://matplotlib.org/stable/gallery/statistics/errorbar_features.html)

Different ways of specifying error bars

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_subsample_thumb.png)

[Errorbar subsampling](https://matplotlib.org/stable/gallery/statistics/errorbar_subsample.html)

Errorbar subsampling

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_limits_thumb.png)

[Including upper and lower limits in error bars](https://matplotlib.org/stable/gallery/statistics/errorbar_limits.html)

Including upper and lower limits in error bars

![](https://matplotlib.org/stable/_images/sphx_glr_confidence_ellipse_thumb.png)

[Plot a confidence ellipse of a two-dimensional dataset](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html)

Plot a confidence ellipse of a two-dimensional dataset

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_thumb.png)

[Histogram bins, density, and weight](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html)

Histogram bins, density, and weight

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_thumb.png)

[The histogram (hist) function with multiple data sets](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html)

The histogram (hist) function with multiple data sets

![](https://matplotlib.org/stable/_images/sphx_glr_hexbin_demo_thumb.png)

[Hexagonal binned plot](https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html)

Hexagonal binned plot

![](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_thumb.png)

[Violin plot customization](https://matplotlib.org/stable/gallery/statistics/customized_violin.html)

Violin plot customization

![](https://matplotlib.org/stable/_images/sphx_glr_xcorr_acorr_demo_thumb.png)

[Cross- and auto-correlation](https://matplotlib.org/stable/gallery/statistics/xcorr_acorr_demo.html)

Cross- and auto-correlation

![](https://matplotlib.org/stable/_images/sphx_glr_psd_demo_thumb.png)

[Power spectral density (PSD)](https://matplotlib.org/stable/gallery/statistics/psd_demo.html)

Power spectral density (PSD)

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

![](https://matplotlib.org/stable/_images/sphx_glr_pie_and_donut_labels_thumb.png)

[A pie and a donut with labels](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html)

A pie and a donut with labels

![](https://matplotlib.org/stable/_images/sphx_glr_polar_demo_thumb.png)

[Polar plot](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html)

Polar plot

![](https://matplotlib.org/stable/_images/sphx_glr_polar_error_caps_thumb.png)

[Error bar rendering on polar axis](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_error_caps.html)

Error bar rendering on polar axis

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_axes_demo_thumb.png)

[Axes Demo](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_demo.html)

Axes Demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_axes_margins_thumb.png)

[Controlling view limits using margins and sticky\_edges](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_margins.html)

Controlling view limits using margins and sticky\_edges

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_invert_axes_thumb.png)

[Inverted axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/invert_axes.html)

Inverted axis

![](https://matplotlib.org/stable/_images/sphx_glr_twin_axes_zorder_thumb.png)

[Twin Axes with delta\_zorder](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/twin_axes_zorder.html)

Twin Axes with delta\_zorder

![](https://matplotlib.org/stable/_images/sphx_glr_secondary_axis_thumb.png)

[Secondary Axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/secondary_axis.html)

Secondary Axis

![](https://matplotlib.org/stable/_images/sphx_glr_align_labels_demo_thumb.png)

[Align labels and titles](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html)

Align labels and titles

![](https://matplotlib.org/stable/_images/sphx_glr_figure_title_thumb.png)

[Figure labels: suptitle, supxlabel, supylabel](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html)

Figure labels: suptitle, supxlabel, supylabel

![](https://matplotlib.org/stable/_images/sphx_glr_engineering_formatter_thumb.png)

[Format ticks using engineering notation](https://matplotlib.org/stable/gallery/ticks/engineering_formatter.html)

Format ticks using engineering notation

![](https://matplotlib.org/stable/_images/sphx_glr_date_thumb.png)

[Date tick labels](https://matplotlib.org/stable/gallery/ticks/date.html)

Date tick labels

![](https://matplotlib.org/stable/_images/sphx_glr_date_index_formatter_thumb.png)

[Custom tick formatter for time series](https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html)

Custom tick formatter for time series

![](https://matplotlib.org/stable/_images/sphx_glr_date_precision_and_epochs_thumb.png)

[Date precision and epochs](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html)

Date precision and epochs

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_tick_labelling_demo_thumb.png)

[Colorbar Tick labelling](https://matplotlib.org/stable/gallery/ticks/colorbar_tick_labelling_demo.html)

Colorbar Tick labelling

![](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_thumb.png)

[Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)

Asinh scale

![](https://matplotlib.org/stable/_images/sphx_glr_aspect_loglog_thumb.png)

[Loglog aspect](https://matplotlib.org/stable/gallery/scales/aspect_loglog.html)

Loglog aspect

![](https://matplotlib.org/stable/_images/sphx_glr_log_demo_thumb.png)

[Log scale](https://matplotlib.org/stable/gallery/scales/log_demo.html)

Log scale

![](https://matplotlib.org/stable/_images/sphx_glr_power_norm_thumb.png)

[Exploring normalizations](https://matplotlib.org/stable/gallery/scales/power_norm.html)

Exploring normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_thumb.png)

[Symlog scale](https://matplotlib.org/stable/gallery/scales/symlog_demo.html)

Symlog scale

![](https://matplotlib.org/stable/_images/sphx_glr_spines_thumb.png)

[Spines](https://matplotlib.org/stable/gallery/spines/spines.html)

Spines

![](https://matplotlib.org/stable/_images/sphx_glr_spine_placement_demo_thumb.png)

[Spine placement](https://matplotlib.org/stable/gallery/spines/spine_placement_demo.html)

Spine placement

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_multiline_thumb.png)

[Multiline text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/multiline.html)

Multiline text

![](https://matplotlib.org/stable/_images/sphx_glr_angles_on_bracket_arrows_thumb.png)

[Angle annotations on bracket arrows](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html)

Angle annotations on bracket arrows

![](https://matplotlib.org/stable/_images/sphx_glr_label_subplots_thumb.png)

[Labelling subplots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/label_subplots.html)

Labelling subplots

![](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_thumb.png)

[Scale invariant angle label](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html)

Scale invariant angle label

![](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_thumb.png)

[Legend Demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)

Legend Demo

![](https://matplotlib.org/stable/_images/sphx_glr_accented_text_thumb.png)

[Accented text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/accented_text.html)

Accented text

![](https://matplotlib.org/stable/_images/sphx_glr_font_file_thumb.png)

[Using ttf font files](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_file.html)

Using ttf font files

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_demo_thumb.png)

[Mathtext](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_demo.html)

Mathtext

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_fontfamily_example_thumb.png)

[Math fontfamily](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_fontfamily_example.html)

Math fontfamily

![](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_thumb.png)

[Render math equations using TeX](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

Render math equations using TeX

![](https://matplotlib.org/stable/_images/sphx_glr_titles_demo_thumb.png)

[Title positioning](https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html)

Title positioning

![](https://matplotlib.org/stable/_images/sphx_glr_collections_thumb.png)

[Line, Poly and RegularPoly Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/collections.html)

Line, Poly and RegularPoly Collection

![](https://matplotlib.org/stable/_images/sphx_glr_compound_path_thumb.png)

[Compound path](https://matplotlib.org/stable/gallery/shapes_and_collections/compound_path.html)

Compound path

![](https://matplotlib.org/stable/_images/sphx_glr_donut_thumb.png)

[Mmh Donuts!!!](https://matplotlib.org/stable/gallery/shapes_and_collections/donut.html)

Mmh Donuts!!!

![](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_thumb.png)

[Drawing fancy boxes](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html)

Drawing fancy boxes

![](https://matplotlib.org/stable/_images/sphx_glr_line_collection_thumb.png)

[Plot multiple lines using a LineCollection](https://matplotlib.org/stable/gallery/shapes_and_collections/line_collection.html)

Plot multiple lines using a LineCollection

![](https://matplotlib.org/stable/_images/sphx_glr_quad_bezier_thumb.png)

[Bezier curve](https://matplotlib.org/stable/gallery/shapes_and_collections/quad_bezier.html)

Bezier curve

![](https://matplotlib.org/stable/_images/sphx_glr_color_demo_thumb.png)

[Color Demo](https://matplotlib.org/stable/gallery/color/color_demo.html)

Color Demo

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_default_thumb.png)

[Colors in the default property cycle](https://matplotlib.org/stable/gallery/color/color_cycle_default.html)

Colors in the default property cycle

![](https://matplotlib.org/stable/_images/sphx_glr_color_sequences_thumb.png)

[Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)

Named color sequences

![](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_thumb.png)

[Create a colormap from a list of colors](https://matplotlib.org/stable/gallery/color/custom_cmap.html)

Create a colormap from a list of colors

![](https://matplotlib.org/stable/_images/sphx_glr_set_alpha_thumb.png)

[Ways to set a color's alpha value](https://matplotlib.org/stable/gallery/color/set_alpha.html)

Ways to set a color's alpha value

![](https://matplotlib.org/stable/_images/sphx_glr_bmh_thumb.png)

[Bayesian Methods for Hackers style sheet](https://matplotlib.org/stable/gallery/style_sheets/bmh.html)

Bayesian Methods for Hackers style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_dark_background_thumb.png)

[Dark background style sheet](https://matplotlib.org/stable/gallery/style_sheets/dark_background.html)

Dark background style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_fivethirtyeight_thumb.png)

[FiveThirtyEight style sheet](https://matplotlib.org/stable/gallery/style_sheets/fivethirtyeight.html)

FiveThirtyEight style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_3d_bars_thumb.png)

[Demo of 3D bar charts](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html)

Demo of 3D bar charts

![](https://matplotlib.org/stable/_images/sphx_glr_lorenz_attractor_thumb.png)

[Lorenz attractor](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html)

Lorenz attractor

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_zero_stride_thumb.png)

[3D wireframe plots in one direction](https://matplotlib.org/stable/gallery/mplot3d/wire3d_zero_stride.html)

3D wireframe plots in one direction

![](https://matplotlib.org/stable/_images/sphx_glr_make_room_for_ylabel_using_axesgrid_thumb.png)

[Make room for ylabel using axes\_grid](https://matplotlib.org/stable/gallery/axes_grid1/make_room_for_ylabel_using_axesgrid.html)

Make room for ylabel using axes\_grid

![](https://matplotlib.org/stable/_images/sphx_glr_axis_direction_thumb.png)

[Axis Direction](https://matplotlib.org/stable/gallery/axisartist/axis_direction.html)

Axis Direction

![](https://matplotlib.org/stable/_images/sphx_glr_animation_demo_thumb.png)

[pyplot animation](https://matplotlib.org/stable/gallery/animation/animation_demo.html)

pyplot animation

![](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_thumb.png)

[Annotated cursor](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html)

Annotated cursor

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_grid_thumb.png)

[Radio Buttons Grid](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html)

Radio Buttons Grid

![](https://matplotlib.org/stable/_images/sphx_glr_rectangle_selector_thumb.png)

[Rectangle and ellipse selectors](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html)

Rectangle and ellipse selectors

![](https://matplotlib.org/stable/_images/sphx_glr_span_selector_thumb.png)

[Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

Span Selector

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_demo_thumb.png)

[Cross-hair cursor](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html)

Cross-hair cursor

![](https://matplotlib.org/stable/_images/sphx_glr_data_browser_thumb.png)

[Data browser](https://matplotlib.org/stable/gallery/event_handling/data_browser.html)

Data browser

![](https://matplotlib.org/stable/_images/sphx_glr_keypress_demo_thumb.png)

[Keypress event](https://matplotlib.org/stable/gallery/event_handling/keypress_demo.html)

Keypress event

![](https://matplotlib.org/stable/_images/sphx_glr_legend_picking_thumb.png)

[Legend picking](https://matplotlib.org/stable/gallery/event_handling/legend_picking.html)

Legend picking

![](https://matplotlib.org/stable/_images/sphx_glr_looking_glass_thumb.png)

[Looking glass](https://matplotlib.org/stable/gallery/event_handling/looking_glass.html)

Looking glass

![](https://matplotlib.org/stable/_images/sphx_glr_path_editor_thumb.png)

[Path editor](https://matplotlib.org/stable/gallery/event_handling/path_editor.html)

Path editor

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_thumb.png)

[Pick event demo](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html)

Pick event demo

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo2_thumb.png)

[Pick event demo 2](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo2.html)

Pick event demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_poly_editor_thumb.png)

[Polygon editor](https://matplotlib.org/stable/gallery/event_handling/poly_editor.html)

Polygon editor

![](https://matplotlib.org/stable/_images/sphx_glr_trifinder_event_demo_thumb.png)

[Trifinder Event Demo](https://matplotlib.org/stable/gallery/event_handling/trifinder_event_demo.html)

Trifinder Event Demo

![](https://matplotlib.org/stable/_images/sphx_glr_viewlims_thumb.png)

[Viewlims](https://matplotlib.org/stable/gallery/event_handling/viewlims.html)

Viewlims

![](https://matplotlib.org/stable/_images/sphx_glr_artist_tests_thumb.png)

[Artist tests](https://matplotlib.org/stable/gallery/units/artist_tests.html)

Artist tests

![](https://matplotlib.org/stable/_images/sphx_glr_bar_unit_demo_thumb.png)

[Group barchart with units](https://matplotlib.org/stable/gallery/units/bar_unit_demo.html)

Group barchart with units

![](https://matplotlib.org/stable/_images/sphx_glr_evans_test_thumb.png)

[Evans test](https://matplotlib.org/stable/gallery/units/evans_test.html)

Evans test

![](https://matplotlib.org/stable/_images/sphx_glr_packed_bubbles_thumb.png)

[Packed-bubble chart](https://matplotlib.org/stable/gallery/misc/packed_bubbles.html)

Packed-bubble chart

![](https://matplotlib.org/stable/_images/sphx_glr_rasterization_demo_thumb.png)

[Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)

Rasterization for vector graphics

![](https://matplotlib.org/stable/_images/sphx_glr_zorder_demo_thumb.png)

[Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)

Zorder Demo

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

![](https://matplotlib.org/stable/_images/sphx_glr_radar_chart_thumb.png)

[Radar chart (aka spider or star chart)](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html)

Radar chart (aka spider or star chart)

![](https://matplotlib.org/stable/_images/sphx_glr_topographic_hillshading_thumb.png)

[Topographic hillshading](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html)

Topographic hillshading

![](https://matplotlib.org/stable/_images/sphx_glr_artists_thumb.png)

[Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html)

Artist tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_thumb.png)

[Coding shortcuts](https://matplotlib.org/stable/tutorials/coding_shortcuts.html)

Coding shortcuts

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_thumb.png)

[Styling with cycler](https://matplotlib.org/stable/users/explain/artists/color_cycle.html)

Styling with cycler

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_autoscale_thumb.png)

[Axis autoscaling](https://matplotlib.org/stable/users/explain/axes/autoscale.html)

Axis autoscaling

![](https://matplotlib.org/stable/_images/sphx_glr_axes_scales_thumb.png)

[Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)

Axis scales

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_placement_thumb.png)

[Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)

Placing colorbars

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page
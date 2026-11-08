[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#main-content)

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
    

matplotlib.axes.Axes.set\_ylabel[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib-axes-axes-set-ylabel "Link to this heading")

===========================================================================================================================================================================

Axes.set\_ylabel(_ylabel_, _fontdict\=None_, _labelpad\=None_, _\*_, _loc\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L4013-L4061)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "Link to this definition")

Set the label for the y-axis.

Parameters:

**ylabel**str

The label text.

**labelpad**float, default: `[rcParams["axes.labelpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.labelpad#rcparam-axes-labelpad) ` (default: `4.0`)

Spacing in points from the Axes bounding box including ticks and tick labels. If None, the previous value is left as is.

**loc**{'bottom', 'center', 'top'}, default: `[rcParams["yaxis.labellocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=yaxis.labellocation#rcparam-yaxis-labellocation) ` (default: `'center'`)

The label position. This is a high-level alternative for passing parameters _y_ and _horizontalalignment_.

Other Parameters:

**\*\*kwargs**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties control the appearance of the label.

See also

[`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")

Documents the properties supported by [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
.

Examples using `matplotlib.axes.Axes.set_ylabel`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#examples-using-matplotlib-axes-axes-set-ylabel "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_barchart_thumb.png)

[Grouped bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)

Grouped bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_bar_colors_thumb.png)

[Bar chart with individual bar colors](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html)

Bar chart with individual bar colors

![](https://matplotlib.org/stable/_images/sphx_glr_hat_graph_thumb.png)

[Hat graph](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html)

Hat graph

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_demo2_thumb.png)

[Scatter Demo2](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html)

Scatter Demo2

![](https://matplotlib.org/stable/_images/sphx_glr_multivariate_marker_plot_thumb.png)

[Mapping marker properties to multivariate data](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html)

Mapping marker properties to multivariate data

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_alpha_thumb.png)

[fill\_between with transparency](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html)

fill\_between with transparency

![](https://matplotlib.org/stable/_images/sphx_glr_stackplot_demo_thumb.png)

[Stackplots and streamgraphs](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stackplot_demo.html)

Stackplots and streamgraphs

![](https://matplotlib.org/stable/_images/sphx_glr_triplot_demo_thumb.png)

[Triplot Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triplot_demo.html)

Triplot Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tripcolor_demo_thumb.png)

[Tripcolor Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/tripcolor_demo.html)

Tripcolor Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_demo_thumb.png)

[Tricontour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_demo.html)

Tricontour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_demo_thumb.png)

[Contourf demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html)

Contourf demo

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_specgram_demo_thumb.png)

[Spectrogram](https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html)

Spectrogram

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_thumb.png)

[Histogram bins, density, and weight](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html)

Histogram bins, density, and weight

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_histograms_side_by_side_thumb.png)

[Multiple histograms side by side](https://matplotlib.org/stable/gallery/statistics/multiple_histograms_side_by_side.html)

Multiple histograms side by side

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_cumulative_thumb.png)

[Cumulative distributions](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html)

Cumulative distributions

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_color_thumb.png)

[Box plots with custom fill colors](https://matplotlib.org/stable/gallery/statistics/boxplot_color.html)

Box plots with custom fill colors

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_vs_violin_thumb.png)

[Box plot vs. violin plot comparison](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html)

Box plot vs. violin plot comparison

![](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_thumb.png)

[Violin plot customization](https://matplotlib.org/stable/gallery/statistics/customized_violin.html)

Violin plot customization

![](https://matplotlib.org/stable/_images/sphx_glr_psd_demo_thumb.png)

[Power spectral density (PSD)](https://matplotlib.org/stable/gallery/statistics/psd_demo.html)

Power spectral density (PSD)

![](https://matplotlib.org/stable/_images/sphx_glr_csd_demo_thumb.png)

[Cross spectral density (CSD)](https://matplotlib.org/stable/gallery/statistics/csd_demo.html)

Cross spectral density (CSD)

![](https://matplotlib.org/stable/_images/sphx_glr_subplot_thumb.png)

[Multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)

Multiple subplots

![](https://matplotlib.org/stable/_images/sphx_glr_axes_demo_thumb.png)

[Axes Demo](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_demo.html)

Axes Demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_shared_axis_demo_thumb.png)

[Shared axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/shared_axis_demo.html)

Shared axis

![](https://matplotlib.org/stable/_images/sphx_glr_two_scales_thumb.png)

[Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)

Plots with different scales

![](https://matplotlib.org/stable/_images/sphx_glr_twin_axes_zorder_thumb.png)

[Twin Axes with delta\_zorder](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/twin_axes_zorder.html)

Twin Axes with delta\_zorder

![](https://matplotlib.org/stable/_images/sphx_glr_secondary_axis_thumb.png)

[Secondary Axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/secondary_axis.html)

Secondary Axis

![](https://matplotlib.org/stable/_images/sphx_glr_align_labels_demo_thumb.png)

[Align labels and titles](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html)

Align labels and titles

![](https://matplotlib.org/stable/_images/sphx_glr_axis_labels_demo_thumb.png)

[Axis label position](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axis_labels_demo.html)

Axis label position

![](https://matplotlib.org/stable/_images/sphx_glr_figure_title_thumb.png)

[Figure labels: suptitle, supxlabel, supylabel](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html)

Figure labels: suptitle, supxlabel, supylabel

![](https://matplotlib.org/stable/_images/sphx_glr_ticks_top_right_thumb.png)

[Move x/y-axis ticks and labels on top and right](https://matplotlib.org/stable/gallery/ticks/ticks_top_right.html)

Move x/y-axis ticks and labels on top and right

![](https://matplotlib.org/stable/_images/sphx_glr_ticklabels_rotation_thumb.png)

[Rotated tick labels](https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html)

Rotated tick labels

![](https://matplotlib.org/stable/_images/sphx_glr_date_thumb.png)

[Date tick labels](https://matplotlib.org/stable/gallery/ticks/date.html)

Date tick labels

![](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_thumb.png)

[Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)

Asinh scale

![](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_thumb.png)

[Symlog scale](https://matplotlib.org/stable/gallery/scales/symlog_demo.html)

Symlog scale

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_multiline_thumb.png)

[Multiline text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/multiline.html)

Multiline text

![](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_thumb.png)

[Legend Demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)

Legend Demo

![](https://matplotlib.org/stable/_images/sphx_glr_accented_text_thumb.png)

[Accented text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/accented_text.html)

Accented text

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_demo_thumb.png)

[Mathtext](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_demo.html)

Mathtext

![](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_thumb.png)

[Render math equations using TeX](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

Render math equations using TeX

![](https://matplotlib.org/stable/_images/sphx_glr_collections_thumb.png)

[Line, Poly and RegularPoly Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/collections.html)

Line, Poly and RegularPoly Collection

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_collection_thumb.png)

[Ellipse Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html)

Ellipse Collection

![](https://matplotlib.org/stable/_images/sphx_glr_color_demo_thumb.png)

[Color Demo](https://matplotlib.org/stable/gallery/color/color_demo.html)

Color Demo

![](https://matplotlib.org/stable/_images/sphx_glr_dark_background_thumb.png)

[Dark background style sheet](https://matplotlib.org/stable/gallery/style_sheets/dark_background.html)

Dark background style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_bars3d_thumb.png)

[Create 2D bar graphs in different planes](https://matplotlib.org/stable/gallery/mplot3d/bars3d.html)

Create 2D bar graphs in different planes

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar3d_thumb.png)

[3D errorbars](https://matplotlib.org/stable/gallery/mplot3d/errorbar3d.html)

3D errorbars

![](https://matplotlib.org/stable/_images/sphx_glr_lorenz_attractor_thumb.png)

[Lorenz attractor](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html)

Lorenz attractor

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_offset_thumb.png)

[Automatic text offsetting](https://matplotlib.org/stable/gallery/mplot3d/offset.html)

Automatic text offsetting

![](https://matplotlib.org/stable/_images/sphx_glr_scales3d_thumb.png)

[Scales on 3D (Log, Symlog, etc.)](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html)

Scales on 3D (Log, Symlog, etc.)

![](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_thumb.png)

[3D scatterplot](https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html)

3D scatterplot

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_radial_thumb.png)

[3D surface with polar coordinates](https://matplotlib.org/stable/gallery/mplot3d/surface3d_radial.html)

3D surface with polar coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_text3d_thumb.png)

[Text annotations in 3D](https://matplotlib.org/stable/gallery/mplot3d/text3d.html)

Text annotations in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_make_room_for_ylabel_using_axesgrid_thumb.png)

[Make room for ylabel using axes\_grid](https://matplotlib.org/stable/gallery/axes_grid1/make_room_for_ylabel_using_axesgrid.html)

Make room for ylabel using axes\_grid

![](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple_thumb.png)

[Parasite Simple](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple.html)

Parasite Simple

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_alignment_thumb.png)

[Ticklabel alignment](https://matplotlib.org/stable/gallery/axisartist/demo_ticklabel_alignment.html)

Ticklabel alignment

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_direction03_thumb.png)

[Simple axis tick label and tick directions](https://matplotlib.org/stable/gallery/axisartist/simple_axis_direction03.html)

Simple axis tick label and tick directions

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline_thumb.png)

[Simple Axisline](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html)

Simple Axisline

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_thumb.png)

[Pick event demo](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html)

Pick event demo

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

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

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_axes_scales_thumb.png)

[Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)

Axis scales

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colormaps_thumb.png)

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choosing Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page
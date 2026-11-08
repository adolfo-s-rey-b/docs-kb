[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#main-content)

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
    

matplotlib.figure.Figure.subplots\_adjust[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib-figure-figure-subplots-adjust "Link to this heading")

======================================================================================================================================================================================================

Figure.subplots\_adjust(_left\=None_, _bottom\=None_, _right\=None_, _top\=None_, _wspace\=None_, _hspace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1322-L1364)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "Link to this definition")

Adjust the subplot layout parameters.

Unset parameters are left unmodified; initial values are given by `[rcParams["figure.subplot.[name]"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.[name]#rcparam-figure-subplot-left) `.

([`Source code`](https://matplotlib.org/stable/_downloads/01c30d8647018decc739b3ad375ac00c/figure_subplots_adjust.py)
, [`png`](https://matplotlib.org/stable/_downloads/362a080aae6b1dfd85262cfa1d98085f/figure_subplots_adjust.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-figure_subplots_adjust.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-figure_subplots_adjust.2x.png)

Parameters:

**left**float, optional

The position of the left edge of the subplots, as a fraction of the figure width.

**right**float, optional

The position of the right edge of the subplots, as a fraction of the figure width.

**bottom**float, optional

The position of the bottom edge of the subplots, as a fraction of the figure height.

**top**float, optional

The position of the top edge of the subplots, as a fraction of the figure height.

**wspace**float, optional

The width of the padding between subplots, as a fraction of the average Axes width.

**hspace**float, optional

The height of the padding between subplots, as a fraction of the average Axes height.

Examples using `matplotlib.figure.Figure.subplots_adjust`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#examples-using-matplotlib-figure-figure-subplots-adjust "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_thumb.png)

[Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)

Marker reference

![](https://matplotlib.org/stable/_images/sphx_glr_contour_image_thumb.png)

[Contour image](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_image.html)

Contour image

![](https://matplotlib.org/stable/_images/sphx_glr_confidence_ellipse_thumb.png)

[Plot a confidence ellipse of a two-dimensional dataset](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html)

Plot a confidence ellipse of a two-dimensional dataset

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_thumb.png)

[Artist customization in box plots](https://matplotlib.org/stable/gallery/statistics/boxplot.html)

Artist customization in box plots

![](https://matplotlib.org/stable/_images/sphx_glr_violinplot_thumb.png)

[Violin plot basics](https://matplotlib.org/stable/gallery/statistics/violinplot.html)

Violin plot basics

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

![](https://matplotlib.org/stable/_images/sphx_glr_auto_subplots_adjust_thumb.png)

[Programmatically control subplot adjustment](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/auto_subplots_adjust.html)

Programmatically control subplot adjustment

![](https://matplotlib.org/stable/_images/sphx_glr_ganged_plots_thumb.png)

[Adjacent subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/ganged_plots.html)

Adjacent subplots

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_yaxis_with_spines_thumb.png)

[Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)

Multiple y-axis with Spines

![](https://matplotlib.org/stable/_images/sphx_glr_broken_axis_thumb.png)

[Broken axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html)

Broken axis

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_collections_thumb.png)

[Line, Poly and RegularPoly Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/collections.html)

Line, Poly and RegularPoly Collection

![](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_thumb.png)

[Create a colormap from a list of colors](https://matplotlib.org/stable/gallery/color/custom_cmap.html)

Create a colormap from a list of colors

![](https://matplotlib.org/stable/_images/sphx_glr_named_colors_thumb.png)

[List of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html)

List of named colors

![](https://matplotlib.org/stable/_images/sphx_glr_demo_colorbar_with_axes_divider_thumb.png)

[Colorbar with AxesDivider](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_axes_divider.html)

Colorbar with AxesDivider

![](https://matplotlib.org/stable/_images/sphx_glr_axis_direction_thumb.png)

[Axis Direction](https://matplotlib.org/stable/gallery/axisartist/axis_direction.html)

Axis Direction

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_thumb.png)

[floating\_axes features](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html)

floating\_axes features

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_alignment_thumb.png)

[Ticklabel alignment](https://matplotlib.org/stable/gallery/axisartist/demo_ticklabel_alignment.html)

Ticklabel alignment

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_direction_thumb.png)

[Ticklabel direction](https://matplotlib.org/stable/gallery/axisartist/demo_ticklabel_direction.html)

Ticklabel direction

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_direction01_thumb.png)

[Simple axis direction](https://matplotlib.org/stable/gallery/axisartist/simple_axis_direction01.html)

Simple axis direction

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_direction03_thumb.png)

[Simple axis tick label and tick directions](https://matplotlib.org/stable/gallery/axisartist/simple_axis_direction03.html)

Simple axis tick label and tick directions

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_thumb.png)

[Simple axis pad](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html)

Simple axis pad

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline_thumb.png)

[Simple Axisline](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html)

Simple Axisline

![](https://matplotlib.org/stable/_images/sphx_glr_buttons_thumb.png)

[Buttons](https://matplotlib.org/stable/gallery/widgets/buttons.html)

Buttons

![](https://matplotlib.org/stable/_images/sphx_glr_menu_thumb.png)

[Menu](https://matplotlib.org/stable/gallery/widgets/menu.html)

Menu

![](https://matplotlib.org/stable/_images/sphx_glr_range_slider_thumb.png)

[Image scaling using a RangeSlider](https://matplotlib.org/stable/gallery/widgets/range_slider.html)

Image scaling using a RangeSlider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_demo_thumb.png)

[Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)

Slider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_snap_demo_thumb.png)

[Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)

Snap sliders to discrete values

![](https://matplotlib.org/stable/_images/sphx_glr_textbox_thumb.png)

[Textbox](https://matplotlib.org/stable/gallery/widgets/textbox.html)

Textbox

![](https://matplotlib.org/stable/_images/sphx_glr_evans_test_thumb.png)

[Evans test](https://matplotlib.org/stable/gallery/units/evans_test.html)

Evans test

![](https://matplotlib.org/stable/_images/sphx_glr_radar_chart_thumb.png)

[Radar chart (aka spider or star chart)](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html)

Radar chart (aka spider or star chart)

![](https://matplotlib.org/stable/_images/sphx_glr_topographic_hillshading_thumb.png)

[Topographic hillshading](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html)

Topographic hillshading

![](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_thumb.png)

[The Lifecycle of a Plot](https://matplotlib.org/stable/tutorials/lifecycle.html)

The Lifecycle of a Plot

![](https://matplotlib.org/stable/_images/sphx_glr_artists_thumb.png)

[Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html)

Artist tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_thumb.png)

[Styling with cycler](https://matplotlib.org/stable/users/explain/artists/color_cycle.html)

Styling with cycler

![](https://matplotlib.org/stable/_images/sphx_glr_colormaps_thumb.png)

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choosing Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page
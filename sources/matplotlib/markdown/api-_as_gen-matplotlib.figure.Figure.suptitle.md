[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#main-content)

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
    

matplotlib.figure.Figure.suptitle[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib-figure-figure-suptitle "Link to this heading")

================================================================================================================================================================================

Figure.suptitle(_t_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L390-L398)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "Link to this definition")

Add a centered super title to the figure.

Parameters:

**t**str

The super title text.

**x**float, default: 0.5

The x location of the text in figure coordinates.

**y**float, default: 0.98

The y location of the text in figure coordinates.

**horizontalalignment, ha**{'center', 'left', 'right'}, default: center

The horizontal alignment of the text relative to (_x_, _y_).

**verticalalignment, va**{'top', 'center', 'bottom', 'baseline'}, default: top

The vertical alignment of the text relative to (_x_, _y_).

**fontsize, size**default: `[rcParams["figure.titlesize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titlesize#rcparam-figure-titlesize) ` (default: `'large'`)

The font size of the text. See [`Text.set_size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_size "matplotlib.text.Text.set_size")
 for possible values.

**fontweight, weight**default: `[rcParams["figure.titleweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titleweight#rcparam-figure-titleweight) ` (default: `'normal'`)

The font weight of the text. See [`Text.set_weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_weight "matplotlib.text.Text.set_weight")
 for possible values.

Returns:

text

The [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance of the super title.

Other Parameters:

**fontproperties**None or dict, optional

A dict of font properties. If _fontproperties_ is given the default values for font size and weight are taken from the [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 defaults. `[rcParams["figure.titlesize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titlesize#rcparam-figure-titlesize) ` (default: `'large'`) and `[rcParams["figure.titleweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titleweight#rcparam-figure-titleweight) ` (default: `'normal'`) are ignored in this case.

**\*\*kwargs**

Additional kwargs are [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties.

Examples using `matplotlib.figure.Figure.suptitle`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#examples-using-matplotlib-figure-figure-suptitle "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_thumb.png)

[Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)

Marker reference

![](https://matplotlib.org/stable/_images/sphx_glr_multivariate_marker_plot_thumb.png)

[Mapping marker properties to multivariate data](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html)

Mapping marker properties to multivariate data

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_alpha_thumb.png)

[fill\_between with transparency](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html)

fill\_between with transparency

![](https://matplotlib.org/stable/_images/sphx_glr_categorical_variables_thumb.png)

[Plotting categorical variables](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html)

Plotting categorical variables

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_multi_image_thumb.png)

[Multiple images with one colorbar](https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html)

Multiple images with one colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_image_nonuniform_thumb.png)

[Image nonuniform](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_nonuniform.html)

Image nonuniform

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_subsample_thumb.png)

[Errorbar subsampling](https://matplotlib.org/stable/gallery/statistics/errorbar_subsample.html)

Errorbar subsampling

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_cumulative_thumb.png)

[Cumulative distributions](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html)

Cumulative distributions

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_thumb.png)

[Artist customization in box plots](https://matplotlib.org/stable/gallery/statistics/boxplot.html)

Artist customization in box plots

![](https://matplotlib.org/stable/_images/sphx_glr_violinplot_thumb.png)

[Violin plot basics](https://matplotlib.org/stable/gallery/statistics/violinplot.html)

Violin plot basics

![](https://matplotlib.org/stable/_images/sphx_glr_subplot_thumb.png)

[Multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)

Multiple subplots

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_customization_thumb.png)

[GridSpec with variable sizes and spacing](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_customization.html)

GridSpec with variable sizes and spacing

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_multicolumn_thumb.png)

[Gridspec for multi-column/row subplot layouts](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_multicolumn.html)

Gridspec for multi-column/row subplot layouts

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_invert_axes_thumb.png)

[Inverted axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/invert_axes.html)

Inverted axis

![](https://matplotlib.org/stable/_images/sphx_glr_figure_title_thumb.png)

[Figure labels: suptitle, supxlabel, supylabel](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html)

Figure labels: suptitle, supxlabel, supylabel

![](https://matplotlib.org/stable/_images/sphx_glr_date_formatters_locators_thumb.png)

[Date tick locators and formatters](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html)

Date tick locators and formatters

![](https://matplotlib.org/stable/_images/sphx_glr_log_demo_thumb.png)

[Log scale](https://matplotlib.org/stable/gallery/scales/log_demo.html)

Log scale

![](https://matplotlib.org/stable/_images/sphx_glr_spine_placement_demo_thumb.png)

[Spine placement](https://matplotlib.org/stable/gallery/spines/spine_placement_demo.html)

Spine placement

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_thumb.png)

[Scale invariant angle label](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html)

Scale invariant angle label

![](https://matplotlib.org/stable/_images/sphx_glr_usetex_fonteffects_thumb.png)

[Usetex font effects](https://matplotlib.org/stable/gallery/text_labels_and_annotations/usetex_fonteffects.html)

Usetex font effects

![](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_thumb.png)

[Create a colormap from a list of colors](https://matplotlib.org/stable/gallery/color/custom_cmap.html)

Create a colormap from a list of colors

![](https://matplotlib.org/stable/_images/sphx_glr_grayscale_thumb.png)

[Grayscale style sheet](https://matplotlib.org/stable/gallery/style_sheets/grayscale.html)

Grayscale style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider1_thumb.png)

[Simple Axes Divider 1](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider1.html)

Simple Axes Divider 1

![](https://matplotlib.org/stable/_images/sphx_glr_mouse_cursor_thumb.png)

[Mouse Cursor](https://matplotlib.org/stable/gallery/widgets/mouse_cursor.html)

Mouse Cursor

![](https://matplotlib.org/stable/_images/sphx_glr_figure_axes_enter_leave_thumb.png)

[Figure/Axes enter and leave events](https://matplotlib.org/stable/gallery/event_handling/figure_axes_enter_leave.html)

Figure/Axes enter and leave events

![](https://matplotlib.org/stable/_images/sphx_glr_evans_test_thumb.png)

[Evans test](https://matplotlib.org/stable/gallery/units/evans_test.html)

Evans test

![](https://matplotlib.org/stable/_images/sphx_glr_pan_zoom_overlap_thumb.png)

[Pan/zoom events of overlapping axes](https://matplotlib.org/stable/gallery/showcase/pan_zoom_overlap.html)

Pan/zoom events of overlapping axes

![](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_thumb.png)

[Stock prices over 32 years](https://matplotlib.org/stable/gallery/showcase/stock_prices.html)

Stock prices over 32 years

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_autoscale_thumb.png)

[Axis autoscaling](https://matplotlib.org/stable/users/explain/axes/autoscale.html)

Axis autoscaling

![](https://matplotlib.org/stable/_images/sphx_glr_axes_units_thumb.png)

[Plotting dates and strings](https://matplotlib.org/stable/users/explain/axes/axes_units.html)

Plotting dates and strings

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_placement_thumb.png)

[Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)

Placing colorbars

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colormaps_thumb.png)

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choosing Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_thumb.png)

[Writing mathematical expressions](https://matplotlib.org/stable/users/explain/text/mathtext.html)

Writing mathematical expressions

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page
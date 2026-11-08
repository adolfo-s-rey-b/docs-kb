[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#main-content)

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
    

matplotlib.pyplot.subplots[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib-pyplot-subplots "Link to this heading")

===========================================================================================================================================================

matplotlib.pyplot.subplots(_nrows\=1_, _ncols\=1_, _\*_, _sharex\=False_, _sharey\=False_, _squeeze\=True_, _width\_ratios\=None_, _height\_ratios\=None_, _subplot\_kw\=None_, _gridspec\_kw\=None_, _\*\*fig\_kw_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L1728-L1891)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "Link to this definition")

Create a figure and a set of subplots.

This utility wrapper makes it convenient to create common layouts of subplots, including the enclosing figure object, in a single call.

Parameters:

**nrows, ncols**int, default: 1

Number of rows/columns of the subplot grid.

**sharex, sharey**bool or {'none', 'all', 'row', 'col'}, default: False

Controls sharing of properties among x (_sharex_) or y (_sharey_) axes:

*   True or 'all': x- or y-axis will be shared among all subplots.
    
*   False or 'none': each subplot x- or y-axis will be independent.
    
*   'row': each subplot row will share an x- or y-axis.
    
*   'col': each subplot column will share an x- or y-axis.
    

When subplots have a shared x-axis along a column, only the x tick labels of the bottom subplot are created. Similarly, when subplots have a shared y-axis along a row, only the y tick labels of the first column subplot are created. To later turn other subplots' ticklabels on, use [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
.

When subplots have a shared axis that has units, calling [`Axis.set_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units")
 will update each axis with the new units.

Note that it is not possible to unshare axes.

**squeeze**bool, default: True

*   If True, extra dimensions are squeezed out from the returned array of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
    :
    
    *   if only one subplot is constructed (nrows=ncols=1), the resulting single Axes object is returned as a scalar.
        
    *   for Nx1 or 1xM subplots, the returned object is a 1D numpy object array of Axes objects.
        
    *   for NxM, subplots with N>1 and M>1 are returned as a 2D array.
        
*   If False, no squeezing at all is done: the returned Axes object is always a 2D array containing Axes instances, even if it ends up being 1x1.
    

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width. Equivalent to `gridspec_kw={'width_ratios': [...]}`.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height. Convenience for `gridspec_kw={'height_ratios': [...]}`.

**subplot\_kw**dict, optional

Dict with keywords passed to the [`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 call used to create each subplot.

**gridspec\_kw**dict, optional

Dict with keywords passed to the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 constructor used to create the grid the subplots are placed on.

**\*\*fig\_kw**

All additional keyword arguments are passed to the [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
 call.

Returns:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or array of Axes

_ax_ can be either a single [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object, or an array of Axes objects if more than one subplot was created. The dimensions of the resulting array can be controlled with the squeeze keyword, see above.

Typical idioms for handling the return value are:

\# using the variable ax for a single Axes
fig, ax \= plt.subplots()

\# using the variable axs for multiple Axes
fig, axs \= plt.subplots(2, 2)

\# using tuple unpacking for multiple Axes
fig, (ax1, ax2) \= plt.subplots(1, 2)
fig, ((ax1, ax2), (ax3, ax4)) \= plt.subplots(2, 2)

The names `ax` and pluralized `axs` are preferred over `axes` because for the latter it's not clear if it refers to a single [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance or a collection of these.

See also

[`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")

[`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")

[`pyplot.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")

[`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")

[`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")

Examples

\# First create some toy data:
x \= np.linspace(0, 2\*np.pi, 400)
y \= np.sin(x\*\*2)

\# Create just a figure and only one subplot
fig, ax \= plt.subplots()
ax.plot(x, y)
ax.set\_title('Simple plot')

\# Create two subplots and unpack the output array immediately
f, (ax1, ax2) \= plt.subplots(1, 2, sharey\=True)
ax1.plot(x, y)
ax1.set\_title('Sharing Y axis')
ax2.scatter(x, y)

\# Create four polar Axes and access them through the returned array
fig, axs \= plt.subplots(2, 2, subplot\_kw\=dict(projection\="polar"))
axs\[0, 0\].plot(x, y)
axs\[1, 1\].scatter(x, y)

\# Share an X axis with each column of subplots
plt.subplots(2, 2, sharex\='col')

\# Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey\='row')

\# Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex\='all', sharey\='all')

\# Note that this is the same as
plt.subplots(2, 2, sharex\=True, sharey\=True)

\# Create figure number 10 with a single subplot
\# and clears it if it already exists.
fig, ax \= plt.subplots(num\=10, clear\=True)

Examples using `matplotlib.pyplot.subplots`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#examples-using-matplotlib-pyplot-subplots "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_simple_plot_thumb.png)

[Line plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)

Line plot

![](https://matplotlib.org/stable/_images/sphx_glr_linestyles_thumb.png)

[Linestyles](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)

Linestyles

![](https://matplotlib.org/stable/_images/sphx_glr_line_demo_dash_control_thumb.png)

[Dashed line style configuration](https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html)

Dashed line style configuration

![](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_thumb.png)

[Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)

Markevery Demo

![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_thumb.png)

[Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)

Marker reference

![](https://matplotlib.org/stable/_images/sphx_glr_axline_thumb.png)

[Infinite lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/axline.html)

Infinite lines

![](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_thumb.png)

[Multicolored lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html)

Multicolored lines

![](https://matplotlib.org/stable/_images/sphx_glr_lines_with_ticks_demo_thumb.png)

[Lines with a ticked patheffect](https://matplotlib.org/stable/gallery/lines_bars_and_markers/lines_with_ticks_demo.html)

Lines with a ticked patheffect

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

![](https://matplotlib.org/stable/_images/sphx_glr_gradient_bar_thumb.png)

[Bar chart with gradients](https://matplotlib.org/stable/gallery/lines_bars_and_markers/gradient_bar.html)

Bar chart with gradients

![](https://matplotlib.org/stable/_images/sphx_glr_barh_thumb.png)

[Horizontal bar chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barh.html)

Horizontal bar chart

![](https://matplotlib.org/stable/_images/sphx_glr_horizontal_barchart_distribution_thumb.png)

[Discrete distribution as horizontal bar chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html)

Discrete distribution as horizontal bar chart

![](https://matplotlib.org/stable/_images/sphx_glr_broken_barh_thumb.png)

[Broken horizontal bars](https://matplotlib.org/stable/gallery/lines_bars_and_markers/broken_barh.html)

Broken horizontal bars

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_demo2_thumb.png)

[Scatter Demo2](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html)

Scatter Demo2

![](https://matplotlib.org/stable/_images/sphx_glr_multivariate_marker_plot_thumb.png)

[Mapping marker properties to multivariate data](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html)

Mapping marker properties to multivariate data

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_star_poly_thumb.png)

[Marker examples](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_star_poly.html)

Marker examples

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_with_legend_thumb.png)

[Scatter plot with a legend](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html)

Scatter plot with a legend

![](https://matplotlib.org/stable/_images/sphx_glr_stairs_demo_thumb.png)

[Stairs Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html)

Stairs Demo

![](https://matplotlib.org/stable/_images/sphx_glr_fill_thumb.png)

[Filled polygon](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html)

Filled polygon

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

![](https://matplotlib.org/stable/_images/sphx_glr_eventplot_demo_thumb.png)

[Eventplot demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventplot_demo.html)

Eventplot demo

![](https://matplotlib.org/stable/_images/sphx_glr_timeline_thumb.png)

[Timeline with lines, dates, and text](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html)

Timeline with lines, dates, and text

![](https://matplotlib.org/stable/_images/sphx_glr_vline_hline_demo_thumb.png)

[hlines and vlines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/vline_hline_demo.html)

hlines and vlines

![](https://matplotlib.org/stable/_images/sphx_glr_span_regions_thumb.png)

[Shade regions defined by a logical mask using fill\_between](https://matplotlib.org/stable/gallery/lines_bars_and_markers/span_regions.html)

Shade regions defined by a logical mask using fill\_between

![](https://matplotlib.org/stable/_images/sphx_glr_categorical_variables_thumb.png)

[Plotting categorical variables](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html)

Plotting categorical variables

![](https://matplotlib.org/stable/_images/sphx_glr_image_demo_thumb.png)

[Many ways to plot images](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html)

Many ways to plot images

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_multi_image_thumb.png)

[Multiple images with one colorbar](https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html)

Multiple images with one colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_image_zcoord_thumb.png)

[Modifying the coordinate formatter](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_zcoord.html)

Modifying the coordinate formatter

![](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_thumb.png)

[Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)

Image resampling

![](https://matplotlib.org/stable/_images/sphx_glr_interpolation_methods_thumb.png)

[Interpolations for imshow](https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html)

Interpolations for imshow

![](https://matplotlib.org/stable/_images/sphx_glr_image_transparency_blend_thumb.png)

[Blend transparency with color in 2D images](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html)

Blend transparency with color in 2D images

![](https://matplotlib.org/stable/_images/sphx_glr_shading_example_thumb.png)

[Shading example](https://matplotlib.org/stable/gallery/images_contours_and_fields/shading_example.html)

Shading example

![](https://matplotlib.org/stable/_images/sphx_glr_image_clip_path_thumb.png)

[Clipping images with patches](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html)

Clipping images with patches

![](https://matplotlib.org/stable/_images/sphx_glr_image_exact_placement_thumb.png)

[Placing images, preserving relative sizes](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_exact_placement.html)

Placing images, preserving relative sizes

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

![](https://matplotlib.org/stable/_images/sphx_glr_quadmesh_demo_thumb.png)

[QuadMesh Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/quadmesh_demo.html)

QuadMesh Demo

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

![](https://matplotlib.org/stable/_images/sphx_glr_triinterp_demo_thumb.png)

[Triinterp Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html)

Triinterp Demo

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

![](https://matplotlib.org/stable/_images/sphx_glr_contour_image_thumb.png)

[Contour image](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_image.html)

Contour image

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_log_thumb.png)

[Contourf and log color scale](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_log.html)

Contourf and log color scale

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_hatching_thumb.png)

[Contourf hatching](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_hatching.html)

Contourf hatching

![](https://matplotlib.org/stable/_images/sphx_glr_contour_corner_mask_thumb.png)

[Contour corner mask](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_corner_mask.html)

Contour corner mask

![](https://matplotlib.org/stable/_images/sphx_glr_contours_in_optimization_demo_thumb.png)

[Contouring the solution space of optimizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html)

Contouring the solution space of optimizations

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_simple_demo_thumb.png)

[Quiver Simple Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html)

Quiver Simple Demo

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_demo_thumb.png)

[Advanced quiver and quiverkey functions](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_demo.html)

Advanced quiver and quiverkey functions

![](https://matplotlib.org/stable/_images/sphx_glr_barb_demo_thumb.png)

[Wind barbs](https://matplotlib.org/stable/gallery/images_contours_and_fields/barb_demo.html)

Wind barbs

![](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_thumb.png)

[Streamplot](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_interactive_adjustment_thumb.png)

[Interactive adjustment of colormap range](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_interactive_adjustment.html)

Interactive adjustment of colormap range

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_thumb.png)

[Colormap normalizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations.html)

Colormap normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_symlognorm_thumb.png)

[Colormap normalizations SymLogNorm](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations_symlognorm.html)

Colormap normalizations SymLogNorm

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_affine_image_thumb.png)

[Affine transform of an image](https://matplotlib.org/stable/gallery/images_contours_and_fields/affine_image.html)

Affine transform of an image

![](https://matplotlib.org/stable/_images/sphx_glr_spy_demos_thumb.png)

[Spy Demos](https://matplotlib.org/stable/gallery/images_contours_and_fields/spy_demos.html)

Spy Demos

![](https://matplotlib.org/stable/_images/sphx_glr_specgram_demo_thumb.png)

[Spectrogram](https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html)

Spectrogram

![](https://matplotlib.org/stable/_images/sphx_glr_demo_bboximage_thumb.png)

[BboxImage Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/demo_bboximage.html)

BboxImage Demo

![](https://matplotlib.org/stable/_images/sphx_glr_watermark_image_thumb.png)

[Watermark image](https://matplotlib.org/stable/gallery/images_contours_and_fields/watermark_image.html)

Watermark image

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_thumb.png)

[Errorbar function](https://matplotlib.org/stable/gallery/statistics/errorbar.html)

Errorbar function

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_features_thumb.png)

[Different ways of specifying error bars](https://matplotlib.org/stable/gallery/statistics/errorbar_features.html)

Different ways of specifying error bars

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_subsample_thumb.png)

[Errorbar subsampling](https://matplotlib.org/stable/gallery/statistics/errorbar_subsample.html)

Errorbar subsampling

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_limits_thumb.png)

[Including upper and lower limits in error bars](https://matplotlib.org/stable/gallery/statistics/errorbar_limits.html)

Including upper and lower limits in error bars

![](https://matplotlib.org/stable/_images/sphx_glr_errorbars_and_boxes_thumb.png)

[Create boxes from error bars using PatchCollection](https://matplotlib.org/stable/gallery/statistics/errorbars_and_boxes.html)

Create boxes from error bars using PatchCollection

![](https://matplotlib.org/stable/_images/sphx_glr_confidence_ellipse_thumb.png)

[Plot a confidence ellipse of a two-dimensional dataset](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html)

Plot a confidence ellipse of a two-dimensional dataset

![](https://matplotlib.org/stable/_images/sphx_glr_curve_error_band_thumb.png)

[Curve with error band](https://matplotlib.org/stable/gallery/statistics/curve_error_band.html)

Curve with error band

![](https://matplotlib.org/stable/_images/sphx_glr_hist_thumb.png)

[Histograms](https://matplotlib.org/stable/gallery/statistics/hist.html)

Histograms

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_histtypes_thumb.png)

[Demo of the histogram function's different histtype settings](https://matplotlib.org/stable/gallery/statistics/histogram_histtypes.html)

Demo of the histogram function's different histtype settings

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_thumb.png)

[Histogram bins, density, and weight](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html)

Histogram bins, density, and weight

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_thumb.png)

[The histogram (hist) function with multiple data sets](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html)

The histogram (hist) function with multiple data sets

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_histograms_side_by_side_thumb.png)

[Multiple histograms side by side](https://matplotlib.org/stable/gallery/statistics/multiple_histograms_side_by_side.html)

Multiple histograms side by side

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_bihistogram_thumb.png)

[Bihistogram](https://matplotlib.org/stable/gallery/statistics/histogram_bihistogram.html)

Bihistogram

![](https://matplotlib.org/stable/_images/sphx_glr_hexbin_demo_thumb.png)

[Hexagonal binned plot](https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html)

Hexagonal binned plot

![](https://matplotlib.org/stable/_images/sphx_glr_time_series_histogram_thumb.png)

[Time Series Histogram](https://matplotlib.org/stable/gallery/statistics/time_series_histogram.html)

Time Series Histogram

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_thumb.png)

[Artist customization in box plots](https://matplotlib.org/stable/gallery/statistics/boxplot.html)

Artist customization in box plots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_color_thumb.png)

[Box plots with custom fill colors](https://matplotlib.org/stable/gallery/statistics/boxplot_color.html)

Box plots with custom fill colors

![](https://matplotlib.org/stable/_images/sphx_glr_bxp_thumb.png)

[Separate calculation and plotting of boxplots](https://matplotlib.org/stable/gallery/statistics/bxp.html)

Separate calculation and plotting of boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_vs_violin_thumb.png)

[Box plot vs. violin plot comparison](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html)

Box plot vs. violin plot comparison

![](https://matplotlib.org/stable/_images/sphx_glr_violinplot_thumb.png)

[Violin plot basics](https://matplotlib.org/stable/gallery/statistics/violinplot.html)

Violin plot basics

![](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_thumb.png)

[Violin plot customization](https://matplotlib.org/stable/gallery/statistics/customized_violin.html)

Violin plot customization

![](https://matplotlib.org/stable/_images/sphx_glr_xcorr_acorr_demo_thumb.png)

[Cross- and auto-correlation](https://matplotlib.org/stable/gallery/statistics/xcorr_acorr_demo.html)

Cross- and auto-correlation

![](https://matplotlib.org/stable/_images/sphx_glr_psd_demo_thumb.png)

[Power spectral density (PSD)](https://matplotlib.org/stable/gallery/statistics/psd_demo.html)

Power spectral density (PSD)

![](https://matplotlib.org/stable/_images/sphx_glr_csd_demo_thumb.png)

[Cross spectral density (CSD)](https://matplotlib.org/stable/gallery/statistics/csd_demo.html)

Cross spectral density (CSD)

![](https://matplotlib.org/stable/_images/sphx_glr_cohere_thumb.png)

[Plotting the coherence of two signals](https://matplotlib.org/stable/gallery/statistics/cohere.html)

Plotting the coherence of two signals

![](https://matplotlib.org/stable/_images/sphx_glr_pie_features_thumb.png)

[Pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html)

Pie charts

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

![](https://matplotlib.org/stable/_images/sphx_glr_nested_pie_thumb.png)

[Nested pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html)

Nested pie charts

![](https://matplotlib.org/stable/_images/sphx_glr_pie_and_donut_labels_thumb.png)

[A pie and a donut with labels](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html)

A pie and a donut with labels

![](https://matplotlib.org/stable/_images/sphx_glr_pie_label_thumb.png)

[Labeling pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_label.html)

Labeling pie charts

![](https://matplotlib.org/stable/_images/sphx_glr_polar_demo_thumb.png)

[Polar plot](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html)

Polar plot

![](https://matplotlib.org/stable/_images/sphx_glr_subplot_thumb.png)

[Multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)

Multiple subplots

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_axes_demo_thumb.png)

[Axes Demo](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_demo.html)

Axes Demo

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_and_subplots_thumb.png)

[Combine two subplots using subplots and GridSpec](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html)

Combine two subplots using subplots and GridSpec

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_auto_subplots_adjust_thumb.png)

[Programmatically control subplot adjustment](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/auto_subplots_adjust.html)

Programmatically control subplot adjustment

![](https://matplotlib.org/stable/_images/sphx_glr_ganged_plots_thumb.png)

[Adjacent subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/ganged_plots.html)

Adjacent subplots

![](https://matplotlib.org/stable/_images/sphx_glr_axes_margins_thumb.png)

[Controlling view limits using margins and sticky\_edges](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_margins.html)

Controlling view limits using margins and sticky\_edges

![](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_thumb.png)

[Axes box aspect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html)

Axes box aspect

![](https://matplotlib.org/stable/_images/sphx_glr_axis_equal_demo_thumb.png)

[Equal axis aspect ratio](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axis_equal_demo.html)

Equal axis aspect ratio

![](https://matplotlib.org/stable/_images/sphx_glr_figure_size_units_thumb.png)

[Figure size in different units](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html)

Figure size in different units

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_shared_axis_demo_thumb.png)

[Shared axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/shared_axis_demo.html)

Shared axis

![](https://matplotlib.org/stable/_images/sphx_glr_invert_axes_thumb.png)

[Inverted axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/invert_axes.html)

Inverted axis

![](https://matplotlib.org/stable/_images/sphx_glr_two_scales_thumb.png)

[Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)

Plots with different scales

![](https://matplotlib.org/stable/_images/sphx_glr_fahrenheit_celsius_scales_thumb.png)

[Different scales on the same Axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/fahrenheit_celsius_scales.html)

Different scales on the same Axes

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_yaxis_with_spines_thumb.png)

[Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)

Multiple y-axis with Spines

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

![](https://matplotlib.org/stable/_images/sphx_glr_axes_props_thumb.png)

[Axes properties](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_props.html)

Axes properties

![](https://matplotlib.org/stable/_images/sphx_glr_figure_title_thumb.png)

[Figure labels: suptitle, supxlabel, supylabel](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html)

Figure labels: suptitle, supxlabel, supylabel

![](https://matplotlib.org/stable/_images/sphx_glr_zoom_inset_axes_thumb.png)

[Zoom region inset Axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html)

Zoom region inset Axes

![](https://matplotlib.org/stable/_images/sphx_glr_broken_axis_thumb.png)

[Broken axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html)

Broken axis

![](https://matplotlib.org/stable/_images/sphx_glr_axhspan_demo_thumb.png)

[Draw regions that span an Axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html)

Draw regions that span an Axes

![](https://matplotlib.org/stable/_images/sphx_glr_auto_ticks_thumb.png)

[Automatically setting tick positions](https://matplotlib.org/stable/gallery/ticks/auto_ticks.html)

Automatically setting tick positions

![](https://matplotlib.org/stable/_images/sphx_glr_tick-locators_thumb.png)

[Tick locators](https://matplotlib.org/stable/gallery/ticks/tick-locators.html)

Tick locators

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

![](https://matplotlib.org/stable/_images/sphx_glr_multilevel_ticks_thumb.png)

[Multilevel (nested) ticks](https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html)

Multilevel (nested) ticks

![](https://matplotlib.org/stable/_images/sphx_glr_scalarformatter_thumb.png)

[The default tick formatter](https://matplotlib.org/stable/gallery/ticks/scalarformatter.html)

The default tick formatter

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

![](https://matplotlib.org/stable/_images/sphx_glr_date_precision_and_epochs_thumb.png)

[Date precision and epochs](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html)

Date precision and epochs

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_tick_labelling_demo_thumb.png)

[Colorbar Tick labelling](https://matplotlib.org/stable/gallery/ticks/colorbar_tick_labelling_demo.html)

Colorbar Tick labelling

![](https://matplotlib.org/stable/_images/sphx_glr_ticks_too_many_thumb.png)

[Fixing too many ticks](https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html)

Fixing too many ticks

![](https://matplotlib.org/stable/_images/sphx_glr_scales_thumb.png)

[Scales overview](https://matplotlib.org/stable/gallery/scales/scales.html)

Scales overview

![](https://matplotlib.org/stable/_images/sphx_glr_aspect_loglog_thumb.png)

[Loglog aspect](https://matplotlib.org/stable/gallery/scales/aspect_loglog.html)

Loglog aspect

![](https://matplotlib.org/stable/_images/sphx_glr_log_demo_thumb.png)

[Log scale](https://matplotlib.org/stable/gallery/scales/log_demo.html)

Log scale

![](https://matplotlib.org/stable/_images/sphx_glr_logit_demo_thumb.png)

[Logit scale](https://matplotlib.org/stable/gallery/scales/logit_demo.html)

Logit scale

![](https://matplotlib.org/stable/_images/sphx_glr_power_norm_thumb.png)

[Exploring normalizations](https://matplotlib.org/stable/gallery/scales/power_norm.html)

Exploring normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_thumb.png)

[Symlog scale](https://matplotlib.org/stable/gallery/scales/symlog_demo.html)

Symlog scale

![](https://matplotlib.org/stable/_images/sphx_glr_spines_thumb.png)

[Spines](https://matplotlib.org/stable/gallery/spines/spines.html)

Spines

![](https://matplotlib.org/stable/_images/sphx_glr_spines_dropped_thumb.png)

[Dropped spines](https://matplotlib.org/stable/gallery/spines/spines_dropped.html)

Dropped spines

![](https://matplotlib.org/stable/_images/sphx_glr_centered_spines_with_arrows_thumb.png)

[Centered spines with arrows](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html)

Centered spines with arrows

![](https://matplotlib.org/stable/_images/sphx_glr_text_alignment_thumb.png)

[Text alignment](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html)

Text alignment

![](https://matplotlib.org/stable/_images/sphx_glr_multiline_thumb.png)

[Multiline text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/multiline.html)

Multiline text

![](https://matplotlib.org/stable/_images/sphx_glr_text_rotation_relative_to_line_thumb.png)

[Text rotation angle in data coordinates](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_rotation_relative_to_line.html)

Text rotation angle in data coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_demo_text_path_thumb.png)

[Using a text as a Path](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html)

Using a text as a Path

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_basic_thumb.png)

[Annotating a plot](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_basic.html)

Annotating a plot

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_thumb.png)

[Annotate plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html)

Annotate plots

![](https://matplotlib.org/stable/_images/sphx_glr_angles_on_bracket_arrows_thumb.png)

[Angle annotations on bracket arrows](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html)

Angle annotations on bracket arrows

![](https://matplotlib.org/stable/_images/sphx_glr_fancyarrow_demo_thumb.png)

[Annotation arrow style reference](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html)

Annotation arrow style reference

![](https://matplotlib.org/stable/_images/sphx_glr_placing_text_boxes_thumb.png)

[Placing text boxes](https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html)

Placing text boxes

![](https://matplotlib.org/stable/_images/sphx_glr_demo_annotation_box_thumb.png)

[Artists as annotations](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html)

Artists as annotations

![](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_thumb.png)

[Scale invariant angle label](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html)

Scale invariant angle label

![](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_thumb.png)

[Legend Demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)

Legend Demo

![](https://matplotlib.org/stable/_images/sphx_glr_legend_thumb.png)

[Legend using pre-defined labels](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend.html)

Legend using pre-defined labels

![](https://matplotlib.org/stable/_images/sphx_glr_custom_legends_thumb.png)

[Compose custom legends](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html)

Compose custom legends

![](https://matplotlib.org/stable/_images/sphx_glr_figlegend_demo_thumb.png)

[Figure legend demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/figlegend_demo.html)

Figure legend demo

![](https://matplotlib.org/stable/_images/sphx_glr_accented_text_thumb.png)

[Accented text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/accented_text.html)

Accented text

![](https://matplotlib.org/stable/_images/sphx_glr_font_family_rc_thumb.png)

[Configure the font family](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_family_rc.html)

Configure the font family

![](https://matplotlib.org/stable/_images/sphx_glr_font_file_thumb.png)

[Using ttf font files](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_file.html)

Using ttf font files

![](https://matplotlib.org/stable/_images/sphx_glr_font_table_thumb.png)

[Font table](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_table.html)

Font table

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_demo_thumb.png)

[Mathtext](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_demo.html)

Mathtext

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_fontfamily_example_thumb.png)

[Math fontfamily](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_fontfamily_example.html)

Math fontfamily

![](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_thumb.png)

[Render math equations using TeX](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

Render math equations using TeX

![](https://matplotlib.org/stable/_images/sphx_glr_line_with_text_thumb.png)

[Artist within an artist](https://matplotlib.org/stable/gallery/text_labels_and_annotations/line_with_text.html)

Artist within an artist

![](https://matplotlib.org/stable/_images/sphx_glr_titles_demo_thumb.png)

[Title positioning](https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html)

Title positioning

![](https://matplotlib.org/stable/_images/sphx_glr_watermark_text_thumb.png)

[Text watermark](https://matplotlib.org/stable/gallery/text_labels_and_annotations/watermark_text.html)

Text watermark

![](https://matplotlib.org/stable/_images/sphx_glr_arrow_guide_thumb.png)

[Arrow guide](https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html)

Arrow guide

![](https://matplotlib.org/stable/_images/sphx_glr_collections_thumb.png)

[Line, Poly and RegularPoly Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/collections.html)

Line, Poly and RegularPoly Collection

![](https://matplotlib.org/stable/_images/sphx_glr_compound_path_thumb.png)

[Compound path](https://matplotlib.org/stable/gallery/shapes_and_collections/compound_path.html)

Compound path

![](https://matplotlib.org/stable/_images/sphx_glr_dolphin_thumb.png)

[Dolphins](https://matplotlib.org/stable/gallery/shapes_and_collections/dolphin.html)

Dolphins

![](https://matplotlib.org/stable/_images/sphx_glr_donut_thumb.png)

[Mmh Donuts!!!](https://matplotlib.org/stable/gallery/shapes_and_collections/donut.html)

Mmh Donuts!!!

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_arrow_thumb.png)

[Ellipse with orientation arrow demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_arrow.html)

Ellipse with orientation arrow demo

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_collection_thumb.png)

[Ellipse Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html)

Ellipse Collection

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_demo_thumb.png)

[Ellipse Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html)

Ellipse Demo

![](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_thumb.png)

[Drawing fancy boxes](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html)

Drawing fancy boxes

![](https://matplotlib.org/stable/_images/sphx_glr_hatch_style_reference_thumb.png)

[Hatch style reference](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html)

Hatch style reference

![](https://matplotlib.org/stable/_images/sphx_glr_hatchcolor_demo_thumb.png)

[Hatchcolor Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatchcolor_demo.html)

Hatchcolor Demo

![](https://matplotlib.org/stable/_images/sphx_glr_line_collection_thumb.png)

[Plot multiple lines using a LineCollection](https://matplotlib.org/stable/gallery/shapes_and_collections/line_collection.html)

Plot multiple lines using a LineCollection

![](https://matplotlib.org/stable/_images/sphx_glr_patch_collection_thumb.png)

[Circles, Wedges and Polygons](https://matplotlib.org/stable/gallery/shapes_and_collections/patch_collection.html)

Circles, Wedges and Polygons

![](https://matplotlib.org/stable/_images/sphx_glr_path_patch_thumb.png)

[PathPatch object](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html)

PathPatch object

![](https://matplotlib.org/stable/_images/sphx_glr_quad_bezier_thumb.png)

[Bezier curve](https://matplotlib.org/stable/gallery/shapes_and_collections/quad_bezier.html)

Bezier curve

![](https://matplotlib.org/stable/_images/sphx_glr_color_demo_thumb.png)

[Color Demo](https://matplotlib.org/stable/gallery/color/color_demo.html)

Color Demo

![](https://matplotlib.org/stable/_images/sphx_glr_color_by_yvalue_thumb.png)

[Color by y-value](https://matplotlib.org/stable/gallery/color/color_by_yvalue.html)

Color by y-value

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_default_thumb.png)

[Colors in the default property cycle](https://matplotlib.org/stable/gallery/color/color_cycle_default.html)

Colors in the default property cycle

![](https://matplotlib.org/stable/_images/sphx_glr_color_sequences_thumb.png)

[Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)

Named color sequences

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_basics_thumb.png)

[Colorbar](https://matplotlib.org/stable/gallery/color/colorbar_basics.html)

Colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_histogram_thumb.png)

[Histogram as colorbar](https://matplotlib.org/stable/gallery/color/colorbar_histogram.html)

Histogram as colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_reference_thumb.png)

[Colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html)

Colormap reference

![](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_thumb.png)

[Create a colormap from a list of colors](https://matplotlib.org/stable/gallery/color/custom_cmap.html)

Create a colormap from a list of colors

![](https://matplotlib.org/stable/_images/sphx_glr_individual_colors_from_cmap_thumb.png)

[Selecting individual colors from a colormap](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html)

Selecting individual colors from a colormap

![](https://matplotlib.org/stable/_images/sphx_glr_named_colors_thumb.png)

[List of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html)

List of named colors

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

![](https://matplotlib.org/stable/_images/sphx_glr_ggplot_thumb.png)

[ggplot style sheet](https://matplotlib.org/stable/gallery/style_sheets/ggplot.html)

ggplot style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_grayscale_thumb.png)

[Grayscale style sheet](https://matplotlib.org/stable/gallery/style_sheets/grayscale.html)

Grayscale style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_thumb.png)

[Style sheets reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

Style sheets reference

![](https://matplotlib.org/stable/_images/sphx_glr_axlim_clip_thumb.png)

[Clip the data to the axes view limits](https://matplotlib.org/stable/gallery/mplot3d/axlim_clip.html)

Clip the data to the axes view limits

![](https://matplotlib.org/stable/_images/sphx_glr_custom_shaded_3d_surface_thumb.png)

[Custom hillshading in a 3D surface plot](https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html)

Custom hillshading in a 3D surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_projections_thumb.png)

[3D plot projection types](https://matplotlib.org/stable/gallery/mplot3d/projections.html)

3D plot projection types

![](https://matplotlib.org/stable/_images/sphx_glr_stem3d_demo_thumb.png)

[3D stem](https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html)

3D stem

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_thumb.png)

[3D surface (colormap)](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)

3D surface (colormap)

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_zero_stride_thumb.png)

[3D wireframe plots in one direction](https://matplotlib.org/stable/gallery/mplot3d/wire3d_zero_stride.html)

3D wireframe plots in one direction

![](https://matplotlib.org/stable/_images/sphx_glr_demo_anchored_direction_arrows_thumb.png)

[Anchored Direction Arrow](https://matplotlib.org/stable/gallery/axes_grid1/demo_anchored_direction_arrows.html)

Anchored Direction Arrow

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_hbox_divider_thumb.png)

[HBoxDivider and VBoxDivider demo](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_hbox_divider.html)

HBoxDivider and VBoxDivider demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_rgb_thumb.png)

[Show RGB channels using RGBAxes](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_rgb.html)

Show RGB channels using RGBAxes

![](https://matplotlib.org/stable/_images/sphx_glr_demo_colorbar_with_axes_divider_thumb.png)

[Colorbar with AxesDivider](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_axes_divider.html)

Colorbar with AxesDivider

![](https://matplotlib.org/stable/_images/sphx_glr_demo_colorbar_with_inset_locator_thumb.png)

[Control the position and size of a colorbar with inset\_locator.inset\_axes](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_inset_locator.html)

Control the position and size of a colorbar with inset\_locator.inset\_axes

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_thumb.png)

[Inset locator demo](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html)

Inset locator demo

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo2_thumb.png)

[Inset locator demo 2](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html)

Inset locator demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_locatable_axes_thumb.png)

[Align histogram to scatter plot using locatable Axes](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html)

Align histogram to scatter plot using locatable Axes

![](https://matplotlib.org/stable/_images/sphx_glr_simple_anchored_artists_thumb.png)

[Simple Anchored Artists](https://matplotlib.org/stable/gallery/axes_grid1/simple_anchored_artists.html)

Simple Anchored Artists

![](https://matplotlib.org/stable/_images/sphx_glr_simple_anim_thumb.gif)

[Basic animated line plot](https://matplotlib.org/stable/gallery/animation/simple_anim.html)

Basic animated line plot

![](https://matplotlib.org/stable/_images/sphx_glr_animate_decay_thumb.gif)

[Decay](https://matplotlib.org/stable/gallery/animation/animate_decay.html)

Decay

![](https://matplotlib.org/stable/_images/sphx_glr_animated_histogram_thumb.gif)

[Animated histogram](https://matplotlib.org/stable/gallery/animation/animated_histogram.html)

Animated histogram

![](https://matplotlib.org/stable/_images/sphx_glr_animation_demo_thumb.png)

[pyplot animation](https://matplotlib.org/stable/gallery/animation/animation_demo.html)

pyplot animation

![](https://matplotlib.org/stable/_images/sphx_glr_bayes_update_thumb.gif)

[The Bayes update](https://matplotlib.org/stable/gallery/animation/bayes_update.html)

The Bayes update

![](https://matplotlib.org/stable/_images/sphx_glr_dynamic_image_thumb.gif)

[Animated image using a precomputed list of images](https://matplotlib.org/stable/gallery/animation/dynamic_image.html)

Animated image using a precomputed list of images

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_axes_thumb.gif)

[Multiple Axes animation](https://matplotlib.org/stable/gallery/animation/multiple_axes.html)

Multiple Axes animation

![](https://matplotlib.org/stable/_images/sphx_glr_pause_resume_thumb.png)

[Pause and resume an animation](https://matplotlib.org/stable/gallery/animation/pause_resume.html)

Pause and resume an animation

![](https://matplotlib.org/stable/_images/sphx_glr_simple_scatter_thumb.gif)

[Animated scatter saved as GIF](https://matplotlib.org/stable/gallery/animation/simple_scatter.html)

Animated scatter saved as GIF

![](https://matplotlib.org/stable/_images/sphx_glr_strip_chart_thumb.gif)

[Oscilloscope](https://matplotlib.org/stable/gallery/animation/strip_chart.html)

Oscilloscope

![](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_thumb.png)

[Annotated cursor](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html)

Annotated cursor

![](https://matplotlib.org/stable/_images/sphx_glr_buttons_thumb.png)

[Buttons](https://matplotlib.org/stable/gallery/widgets/buttons.html)

Buttons

![](https://matplotlib.org/stable/_images/sphx_glr_check_buttons_thumb.png)

[Check buttons](https://matplotlib.org/stable/gallery/widgets/check_buttons.html)

Check buttons

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_thumb.png)

[Cursor](https://matplotlib.org/stable/gallery/widgets/cursor.html)

Cursor

![](https://matplotlib.org/stable/_images/sphx_glr_lasso_selector_demo_sgskip_thumb.png)

[Lasso Selector](https://matplotlib.org/stable/gallery/widgets/lasso_selector_demo_sgskip.html)

Lasso Selector

![](https://matplotlib.org/stable/_images/sphx_glr_mouse_cursor_thumb.png)

[Mouse Cursor](https://matplotlib.org/stable/gallery/widgets/mouse_cursor.html)

Mouse Cursor

![](https://matplotlib.org/stable/_images/sphx_glr_multicursor_thumb.png)

[Multicursor](https://matplotlib.org/stable/gallery/widgets/multicursor.html)

Multicursor

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_demo_thumb.png)

[Select indices from a collection using polygon selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html)

Select indices from a collection using polygon selector

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_simple_thumb.png)

[Polygon Selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html)

Polygon Selector

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_grid_thumb.png)

[Radio Buttons Grid](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html)

Radio Buttons Grid

![](https://matplotlib.org/stable/_images/sphx_glr_range_slider_thumb.png)

[Image scaling using a RangeSlider](https://matplotlib.org/stable/gallery/widgets/range_slider.html)

Image scaling using a RangeSlider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_demo_thumb.png)

[Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)

Slider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_snap_demo_thumb.png)

[Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)

Snap sliders to discrete values

![](https://matplotlib.org/stable/_images/sphx_glr_span_selector_thumb.png)

[Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

Span Selector

![](https://matplotlib.org/stable/_images/sphx_glr_textbox_thumb.png)

[Textbox](https://matplotlib.org/stable/gallery/widgets/textbox.html)

Textbox

![](https://matplotlib.org/stable/_images/sphx_glr_coords_demo_thumb.png)

[Mouse move and click events](https://matplotlib.org/stable/gallery/event_handling/coords_demo.html)

Mouse move and click events

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_demo_thumb.png)

[Cross-hair cursor](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html)

Cross-hair cursor

![](https://matplotlib.org/stable/_images/sphx_glr_data_browser_thumb.png)

[Data browser](https://matplotlib.org/stable/gallery/event_handling/data_browser.html)

Data browser

![](https://matplotlib.org/stable/_images/sphx_glr_figure_axes_enter_leave_thumb.png)

[Figure/Axes enter and leave events](https://matplotlib.org/stable/gallery/event_handling/figure_axes_enter_leave.html)

Figure/Axes enter and leave events

![](https://matplotlib.org/stable/_images/sphx_glr_image_slices_viewer_thumb.png)

[Scroll event](https://matplotlib.org/stable/gallery/event_handling/image_slices_viewer.html)

Scroll event

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

![](https://matplotlib.org/stable/_images/sphx_glr_pong_sgskip_thumb.png)

[Pong](https://matplotlib.org/stable/gallery/event_handling/pong_sgskip.html)

Pong

![](https://matplotlib.org/stable/_images/sphx_glr_resample_thumb.png)

[Resampling Data](https://matplotlib.org/stable/gallery/event_handling/resample.html)

Resampling Data

![](https://matplotlib.org/stable/_images/sphx_glr_timers_thumb.png)

[Timers](https://matplotlib.org/stable/gallery/event_handling/timers.html)

Timers

![](https://matplotlib.org/stable/_images/sphx_glr_trifinder_event_demo_thumb.png)

[Trifinder Event Demo](https://matplotlib.org/stable/gallery/event_handling/trifinder_event_demo.html)

Trifinder Event Demo

![](https://matplotlib.org/stable/_images/sphx_glr_viewlims_thumb.png)

[Viewlims](https://matplotlib.org/stable/gallery/event_handling/viewlims.html)

Viewlims

![](https://matplotlib.org/stable/_images/sphx_glr_zoom_window_thumb.png)

[Zoom modifies other Axes](https://matplotlib.org/stable/gallery/event_handling/zoom_window.html)

Zoom modifies other Axes

![](https://matplotlib.org/stable/_images/sphx_glr_pylab_with_gtk3_sgskip_thumb.png)

[pyplot with GTK3](https://matplotlib.org/stable/gallery/user_interfaces/pylab_with_gtk3_sgskip.html)

pyplot with GTK3

![](https://matplotlib.org/stable/_images/sphx_glr_pylab_with_gtk4_sgskip_thumb.png)

[pyplot with GTK4](https://matplotlib.org/stable/gallery/user_interfaces/pylab_with_gtk4_sgskip.html)

pyplot with GTK4

![](https://matplotlib.org/stable/_images/sphx_glr_svg_tooltip_sgskip_thumb.svg)

[SVG Tooltip](https://matplotlib.org/stable/gallery/user_interfaces/svg_tooltip_sgskip.html)

SVG Tooltip

![](https://matplotlib.org/stable/_images/sphx_glr_annotate_with_units_thumb.png)

[Annotation with units](https://matplotlib.org/stable/gallery/units/annotate_with_units.html)

Annotation with units

![](https://matplotlib.org/stable/_images/sphx_glr_artist_tests_thumb.png)

[Artist tests](https://matplotlib.org/stable/gallery/units/artist_tests.html)

Artist tests

![](https://matplotlib.org/stable/_images/sphx_glr_bar_demo2_thumb.png)

[Bar demo with units](https://matplotlib.org/stable/gallery/units/bar_demo2.html)

Bar demo with units

![](https://matplotlib.org/stable/_images/sphx_glr_bar_unit_demo_thumb.png)

[Group barchart with units](https://matplotlib.org/stable/gallery/units/bar_unit_demo.html)

Group barchart with units

![](https://matplotlib.org/stable/_images/sphx_glr_evans_test_thumb.png)

[Evans test](https://matplotlib.org/stable/gallery/units/evans_test.html)

Evans test

![](https://matplotlib.org/stable/_images/sphx_glr_radian_demo_thumb.png)

[Radian ticks](https://matplotlib.org/stable/gallery/units/radian_demo.html)

Radian ticks

![](https://matplotlib.org/stable/_images/sphx_glr_units_sample_thumb.png)

[Inches and centimeters](https://matplotlib.org/stable/gallery/units/units_sample.html)

Inches and centimeters

![](https://matplotlib.org/stable/_images/sphx_glr_units_scatter_thumb.png)

[Unit handling](https://matplotlib.org/stable/gallery/units/units_scatter.html)

Unit handling

![](https://matplotlib.org/stable/_images/sphx_glr_anchored_artists_thumb.png)

[Anchored Artists](https://matplotlib.org/stable/gallery/misc/anchored_artists.html)

Anchored Artists

![](https://matplotlib.org/stable/_images/sphx_glr_bbox_intersect_thumb.png)

[Identify whether artists intersect](https://matplotlib.org/stable/gallery/misc/bbox_intersect.html)

Identify whether artists intersect

![](https://matplotlib.org/stable/_images/sphx_glr_contour_manual_thumb.png)

[Manual Contour](https://matplotlib.org/stable/gallery/misc/contour_manual.html)

Manual Contour

![](https://matplotlib.org/stable/_images/sphx_glr_coords_report_thumb.png)

[Coords Report](https://matplotlib.org/stable/gallery/misc/coords_report.html)

Coords Report

![](https://matplotlib.org/stable/_images/sphx_glr_custom_projection_thumb.png)

[Custom projection](https://matplotlib.org/stable/gallery/misc/custom_projection.html)

Custom projection

![](https://matplotlib.org/stable/_images/sphx_glr_demo_agg_filter_thumb.png)

[AGG filter](https://matplotlib.org/stable/gallery/misc/demo_agg_filter.html)

AGG filter

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ribbon_box_thumb.png)

[Ribbon box](https://matplotlib.org/stable/gallery/misc/demo_ribbon_box.html)

Ribbon box

![](https://matplotlib.org/stable/_images/sphx_glr_fig_x_thumb.png)

[Add lines directly to a figure](https://matplotlib.org/stable/gallery/misc/fig_x.html)

Add lines directly to a figure

![](https://matplotlib.org/stable/_images/sphx_glr_findobj_demo_thumb.png)

[Findobj Demo](https://matplotlib.org/stable/gallery/misc/findobj_demo.html)

Findobj Demo

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_path_thumb.png)

[Building histograms using Rectangles and PolyCollections](https://matplotlib.org/stable/gallery/misc/histogram_path.html)

Building histograms using Rectangles and PolyCollections

![](https://matplotlib.org/stable/_images/sphx_glr_keyword_plotting_thumb.png)

[Plotting with keywords](https://matplotlib.org/stable/gallery/misc/keyword_plotting.html)

Plotting with keywords

![](https://matplotlib.org/stable/_images/sphx_glr_multiprocess_sgskip_thumb.png)

[Multiprocessing](https://matplotlib.org/stable/gallery/misc/multiprocess_sgskip.html)

Multiprocessing

![](https://matplotlib.org/stable/_images/sphx_glr_packed_bubbles_thumb.png)

[Packed-bubble chart](https://matplotlib.org/stable/gallery/misc/packed_bubbles.html)

Packed-bubble chart

![](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_thumb.png)

[Patheffect Demo](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html)

Patheffect Demo

![](https://matplotlib.org/stable/_images/sphx_glr_rasterization_demo_thumb.png)

[Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)

Rasterization for vector graphics

![](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_thumb.png)

[TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)

TickedStroke patheffect

![](https://matplotlib.org/stable/_images/sphx_glr_zorder_demo_thumb.png)

[Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)

Zorder Demo

![](https://matplotlib.org/stable/_images/sphx_glr_integral_thumb.png)

[Integral as the area under a curve](https://matplotlib.org/stable/gallery/showcase/integral.html)

Integral as the area under a curve

![](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_thumb.png)

[Stock prices over 32 years](https://matplotlib.org/stable/gallery/showcase/stock_prices.html)

Stock prices over 32 years

![](https://matplotlib.org/stable/_images/sphx_glr_advanced_hillshading_thumb.png)

[Hillshading](https://matplotlib.org/stable/gallery/specialty_plots/advanced_hillshading.html)

Hillshading

![](https://matplotlib.org/stable/_images/sphx_glr_anscombe_thumb.png)

[Anscombe's quartet](https://matplotlib.org/stable/gallery/specialty_plots/anscombe.html)

Anscombe's quartet

![](https://matplotlib.org/stable/_images/sphx_glr_ishikawa_diagram_thumb.png)

[Ishikawa Diagram](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html)

Ishikawa Diagram

![](https://matplotlib.org/stable/_images/sphx_glr_radar_chart_thumb.png)

[Radar chart (aka spider or star chart)](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html)

Radar chart (aka spider or star chart)

![](https://matplotlib.org/stable/_images/sphx_glr_topographic_hillshading_thumb.png)

[Topographic hillshading](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html)

Topographic hillshading

![](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_thumb.png)

[The Lifecycle of a Plot](https://matplotlib.org/stable/tutorials/lifecycle.html)

The Lifecycle of a Plot

![](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_thumb.png)

[Coding shortcuts](https://matplotlib.org/stable/tutorials/coding_shortcuts.html)

Coding shortcuts

![](https://matplotlib.org/stable/_images/sphx_glr_plot_thumb.png)

[plot(x, y)](https://matplotlib.org/stable/plot_types/basic/plot.html)

plot(x, y)

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_plot_thumb.png)

[scatter(x, y)](https://matplotlib.org/stable/plot_types/basic/scatter_plot.html)

scatter(x, y)

![](https://matplotlib.org/stable/_images/sphx_glr_bar_thumb.png)

[bar(x, height)](https://matplotlib.org/stable/plot_types/basic/bar.html)

bar(x, height)

![](https://matplotlib.org/stable/_images/sphx_glr_stem_thumb.png)

[stem(x, y)](https://matplotlib.org/stable/plot_types/basic/stem.html)

stem(x, y)

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_thumb.png)

[fill\_between(x, y1, y2)](https://matplotlib.org/stable/plot_types/basic/fill_between.html)

fill\_between(x, y1, y2)

![](https://matplotlib.org/stable/_images/sphx_glr_stackplot_thumb.png)

[stackplot(x, y)](https://matplotlib.org/stable/plot_types/basic/stackplot.html)

stackplot(x, y)

![](https://matplotlib.org/stable/_images/sphx_glr_stairs_thumb.png)

[stairs(values)](https://matplotlib.org/stable/plot_types/basic/stairs.html)

stairs(values)

![](https://matplotlib.org/stable/_images/sphx_glr_hist_plot_thumb.png)

[hist(x)](https://matplotlib.org/stable/plot_types/stats/hist_plot.html)

hist(x)

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_plot_thumb.png)

[boxplot(X)](https://matplotlib.org/stable/plot_types/stats/boxplot_plot.html)

boxplot(X)

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_plot_thumb.png)

[errorbar(x, y, yerr, xerr)](https://matplotlib.org/stable/plot_types/stats/errorbar_plot.html)

errorbar(x, y, yerr, xerr)

![](https://matplotlib.org/stable/_images/sphx_glr_violin_thumb.png)

[violinplot(D)](https://matplotlib.org/stable/plot_types/stats/violin.html)

violinplot(D)

![](https://matplotlib.org/stable/_images/sphx_glr_eventplot_thumb.png)

[eventplot(D)](https://matplotlib.org/stable/plot_types/stats/eventplot.html)

eventplot(D)

![](https://matplotlib.org/stable/_images/sphx_glr_hist2d_thumb.png)

[hist2d(x, y)](https://matplotlib.org/stable/plot_types/stats/hist2d.html)

hist2d(x, y)

![](https://matplotlib.org/stable/_images/sphx_glr_hexbin_thumb.png)

[hexbin(x, y, C)](https://matplotlib.org/stable/plot_types/stats/hexbin.html)

hexbin(x, y, C)

![](https://matplotlib.org/stable/_images/sphx_glr_pie_thumb.png)

[pie(x)](https://matplotlib.org/stable/plot_types/stats/pie.html)

pie(x)

![](https://matplotlib.org/stable/_images/sphx_glr_ecdf_thumb.png)

[ecdf(x)](https://matplotlib.org/stable/plot_types/stats/ecdf.html)

ecdf(x)

![](https://matplotlib.org/stable/_images/sphx_glr_imshow_thumb.png)

[imshow(Z)](https://matplotlib.org/stable/plot_types/arrays/imshow.html)

imshow(Z)

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_thumb.png)

[pcolormesh(X, Y, Z)](https://matplotlib.org/stable/plot_types/arrays/pcolormesh.html)

pcolormesh(X, Y, Z)

![](https://matplotlib.org/stable/_images/sphx_glr_contour_thumb.png)

[contour(X, Y, Z)](https://matplotlib.org/stable/plot_types/arrays/contour.html)

contour(X, Y, Z)

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_thumb.png)

[contourf(X, Y, Z)](https://matplotlib.org/stable/plot_types/arrays/contourf.html)

contourf(X, Y, Z)

![](https://matplotlib.org/stable/_images/sphx_glr_barbs_thumb.png)

[barbs(X, Y, U, V)](https://matplotlib.org/stable/plot_types/arrays/barbs.html)

barbs(X, Y, U, V)

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_thumb.png)

[quiver(X, Y, U, V)](https://matplotlib.org/stable/plot_types/arrays/quiver.html)

quiver(X, Y, U, V)

![](https://matplotlib.org/stable/_images/sphx_glr_streamplot_thumb.png)

[streamplot(X, Y, U, V)](https://matplotlib.org/stable/plot_types/arrays/streamplot.html)

streamplot(X, Y, U, V)

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_thumb.png)

[tricontour(x, y, z)](https://matplotlib.org/stable/plot_types/unstructured/tricontour.html)

tricontour(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_tricontourf_thumb.png)

[tricontourf(x, y, z)](https://matplotlib.org/stable/plot_types/unstructured/tricontourf.html)

tricontourf(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_tripcolor_thumb.png)

[tripcolor(x, y, z)](https://matplotlib.org/stable/plot_types/unstructured/tripcolor.html)

tripcolor(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_triplot_thumb.png)

[triplot(x, y)](https://matplotlib.org/stable/plot_types/unstructured/triplot.html)

triplot(x, y)

![](https://matplotlib.org/stable/_images/sphx_glr_bar3d_simple_thumb.png)

[bar3d(x, y, z, dx, dy, dz)](https://matplotlib.org/stable/plot_types/3D/bar3d_simple.html)

bar3d(x, y, z, dx, dy, dz)

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between3d_simple_thumb.png)

[fill\_between(x1, y1, z1, x2, y2, z2)](https://matplotlib.org/stable/plot_types/3D/fill_between3d_simple.html)

fill\_between(x1, y1, z1, x2, y2, z2)

![](https://matplotlib.org/stable/_images/sphx_glr_plot3d_simple_thumb.png)

[plot(xs, ys, zs)](https://matplotlib.org/stable/plot_types/3D/plot3d_simple.html)

plot(xs, ys, zs)

![](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_simple_thumb.png)

[quiver(X, Y, Z, U, V, W)](https://matplotlib.org/stable/plot_types/3D/quiver3d_simple.html)

quiver(X, Y, Z, U, V, W)

![](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_simple_thumb.png)

[scatter(xs, ys, zs)](https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html)

scatter(xs, ys, zs)

![](https://matplotlib.org/stable/_images/sphx_glr_stem3d_thumb.png)

[stem(x, y, z)](https://matplotlib.org/stable/plot_types/3D/stem3d.html)

stem(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_simple_thumb.png)

[plot\_surface(X, Y, Z)](https://matplotlib.org/stable/plot_types/3D/surface3d_simple.html)

plot\_surface(X, Y, Z)

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_simple_thumb.png)

[plot\_trisurf(x, y, z)](https://matplotlib.org/stable/plot_types/3D/trisurf3d_simple.html)

plot\_trisurf(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_simple_thumb.png)

[voxels(\[x, y, z\], filled)](https://matplotlib.org/stable/plot_types/3D/voxels_simple.html)

voxels(\[x, y, z\], filled)

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_simple_thumb.png)

[plot\_wireframe(X, Y, Z)](https://matplotlib.org/stable/plot_types/3D/wire3d_simple.html)

plot\_wireframe(X, Y, Z)

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_animations_thumb.gif)

[Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/animations.html)

Animations using Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_blitting_thumb.png)

[Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html)

Faster rendering by using blitting

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_thumb.png)

[Styling with cycler](https://matplotlib.org/stable/users/explain/artists/color_cycle.html)

Styling with cycler

![](https://matplotlib.org/stable/_images/sphx_glr_paths_thumb.png)

[Path Tutorial](https://matplotlib.org/stable/users/explain/artists/paths.html)

Path Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_autoscale_thumb.png)

[Axis autoscaling](https://matplotlib.org/stable/users/explain/axes/autoscale.html)

Axis autoscaling

![](https://matplotlib.org/stable/_images/sphx_glr_axes_scales_thumb.png)

[Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)

Axis scales

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

![](https://matplotlib.org/stable/_images/sphx_glr_axes_units_thumb.png)

[Plotting dates and strings](https://matplotlib.org/stable/users/explain/axes/axes_units.html)

Plotting dates and strings

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_placement_thumb.png)

[Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)

Placing colorbars

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_thumb.png)

[Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html)

Legend guide

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_thumb.png)

[Customized Colorbars Tutorial](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html)

Customized Colorbars Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_thumb.png)

[Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html)

Creating Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

![](https://matplotlib.org/stable/_images/sphx_glr_colormaps_thumb.png)

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choosing Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page
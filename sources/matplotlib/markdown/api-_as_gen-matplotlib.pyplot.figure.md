[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#main-content)

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
    

matplotlib.pyplot.figure[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib-pyplot-figure "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.figure(_num\=None_, _figsize\=None_, _dpi\=None_, _\*_, _facecolor\=None_, _edgecolor\=None_, _frameon\=True_, _FigureClass\=<class 'matplotlib.figure.Figure'>_, _clear\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L903-L1125)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "Link to this definition")

Create a new figure, or activate an existing figure.

Parameters:

**num**int or str or [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
, optional

A unique identifier for the figure.

If a figure with that identifier already exists, this figure is made active and returned. An integer refers to the `Figure.number` attribute, a string refers to the figure label.

If there is no figure with the identifier or _num_ is not given, a new figure is created, made active and returned. If _num_ is an int, it will be used for the `Figure.number` attribute, otherwise, an auto-generated integer value is used (starting at 1 and incremented for each new figure). If _num_ is a string, the figure label and the window title is set to this value. If num is a `SubFigure`, its parent `Figure` is activated.

If _num_ is a Figure instance that is already tracked in pyplot, it is activated. If _num_ is a Figure instance that is not tracked in pyplot, it is added to the tracked figures and activated.

**figsize**(float, float) or (float, float, str), default: `[rcParams["figure.figsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.figsize#rcparam-figure-figsize) ` (default: `[6.4, 4.8]`)

The figure dimensions. This can be

*   a tuple `(width, height, unit)`, where _unit_ is one of "in", "cm", "px".
    
*   a tuple `(x, y)`, which is interpreted as `(x, y, "in")`.
    

One of _width_ or _height_ may be `None`; the respective value is taken from `[rcParams["figure.figsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.figsize#rcparam-figure-figsize) ` (default: `[6.4, 4.8]`).

**dpi**float, default: `[rcParams["figure.dpi"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.dpi#rcparam-figure-dpi) ` (default: `100.0`)

The resolution of the figure in dots-per-inch.

**facecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: `[rcParams["figure.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.facecolor#rcparam-figure-facecolor) ` (default: `'white'`)

The background color.

**edgecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: `[rcParams["figure.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.edgecolor#rcparam-figure-edgecolor) ` (default: `'white'`)

The border color.

**frameon**bool, default: True

If False, suppress drawing the figure frame.

**FigureClass**subclass of [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

If set, an instance of this subclass will be created, rather than a plain [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

**clear**bool, default: False

If True and the figure already exists, then it is cleared.

**layout**{'constrained', 'compressed', 'tight', 'none', [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
, None}, default: None

The layout mechanism for positioning of plot elements to avoid overlapping Axes decorations (labels, ticks, etc). Note that layout managers can measurably slow down figure display.

*   'constrained': The constrained layout solver adjusts Axes sizes to avoid overlapping Axes decorations. Can handle complex plot layouts and colorbars, and is thus recommended.
    
    See [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
     for examples.
    
*   'compressed': uses the same algorithm as 'constrained', but removes extra space between fixed-aspect-ratio Axes. Best for simple grids of Axes.
    
*   'tight': Use the tight layout mechanism. This is a relatively simple algorithm that adjusts the subplot parameters so that decorations do not overlap. See [`Figure.set_tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#matplotlib.figure.Figure.set_tight_layout "matplotlib.figure.Figure.set_tight_layout")
     for further details.
    
*   'none': Do not use a layout engine.
    
*   A [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
     instance. Builtin layout classes are [`ConstrainedLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine "matplotlib.layout_engine.ConstrainedLayoutEngine")
     and [`TightLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine "matplotlib.layout_engine.TightLayoutEngine")
    , more easily accessible by 'constrained' and 'tight'. Passing an instance allows third parties to provide their own layout engine.
    

If not given, fall back to using the parameters _tight\_layout_ and _constrained\_layout_, including their config defaults `[rcParams["figure.autolayout"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.autolayout#rcparam-figure-autolayout) ` (default: `False`) and `[rcParams["figure.constrained_layout.use"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.use#rcparam-figure-constrained-layout-use) ` (default: `False`).

**\*\*kwargs**

Additional keyword arguments are passed to the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 constructor.

Returns:

[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

Notes

A newly created figure is passed to the [`new_manager`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.new_manager "matplotlib.backend_bases.FigureCanvasBase.new_manager")
 method or the [`new_figure_manager`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.new_figure_manager.html#matplotlib.pyplot.new_figure_manager "matplotlib.pyplot.new_figure_manager")
 function provided by the current backend, which install a canvas and a manager on the figure.

Once this is done, `[rcParams["figure.hooks"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.hooks#rcparam-figure-hooks) ` (default: `[]`) are called, one at a time, on the figure; these hooks allow arbitrary customization of the figure (e.g., attaching callbacks) or of associated elements (e.g., modifying the toolbar). See [mplcvd -- an example of figure hook](https://matplotlib.org/stable/gallery/user_interfaces/mplcvd.html)
 for an example of toolbar customization.

If you are creating many figures, make sure you explicitly call [`pyplot.close`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
 on the figures you are not using, because this will enable pyplot to properly clean up the memory.

[`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 defines the default values, which can be modified in the matplotlibrc file.

Examples using `matplotlib.pyplot.figure`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#examples-using-matplotlib-pyplot-figure "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_thumb.png)

[Scatter plot with histograms](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html)

Scatter plot with histograms

![](https://matplotlib.org/stable/_images/sphx_glr_fill_thumb.png)

[Filled polygon](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html)

Filled polygon

![](https://matplotlib.org/stable/_images/sphx_glr_eventcollection_demo_thumb.png)

[EventCollection Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html)

EventCollection Demo

![](https://matplotlib.org/stable/_images/sphx_glr_spectrum_demo_thumb.png)

[Spectrum representations](https://matplotlib.org/stable/gallery/lines_bars_and_markers/spectrum_demo.html)

Spectrum representations

![](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_thumb.png)

[Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)

Image resampling

![](https://matplotlib.org/stable/_images/sphx_glr_layer_images_thumb.png)

[Layer images with alpha blending](https://matplotlib.org/stable/gallery/images_contours_and_fields/layer_images.html)

Layer images with alpha blending

![](https://matplotlib.org/stable/_images/sphx_glr_image_exact_placement_thumb.png)

[Placing images, preserving relative sizes](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_exact_placement.html)

Placing images, preserving relative sizes

![](https://matplotlib.org/stable/_images/sphx_glr_barcode_demo_thumb.png)

[Barcode](https://matplotlib.org/stable/gallery/images_contours_and_fields/barcode_demo.html)

Barcode

![](https://matplotlib.org/stable/_images/sphx_glr_figimage_demo_thumb.png)

[Figimage Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/figimage_demo.html)

Figimage Demo

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_limits_simple_thumb.png)

[Errorbar limit selection](https://matplotlib.org/stable/gallery/statistics/errorbar_limits_simple.html)

Errorbar limit selection

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_cumulative_thumb.png)

[Cumulative distributions](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html)

Cumulative distributions

![](https://matplotlib.org/stable/_images/sphx_glr_polar_error_caps_thumb.png)

[Error bar rendering on polar axis](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_error_caps.html)

Error bar rendering on polar axis

![](https://matplotlib.org/stable/_images/sphx_glr_polar_legend_thumb.png)

[Polar legend](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html)

Polar legend

![](https://matplotlib.org/stable/_images/sphx_glr_polar_scatter_thumb.png)

[Scatter plot on polar axis](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_scatter.html)

Scatter plot on polar axis

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_customization_thumb.png)

[GridSpec with variable sizes and spacing](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_customization.html)

GridSpec with variable sizes and spacing

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_multicolumn_thumb.png)

[Gridspec for multi-column/row subplot layouts](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_multicolumn.html)

Gridspec for multi-column/row subplot layouts

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_nested_thumb.png)

[Nested Gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)

Nested Gridspecs

![](https://matplotlib.org/stable/_images/sphx_glr_subplot2grid_thumb.png)

[subplot2grid](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot2grid.html)

subplot2grid

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_figs_demo_thumb.png)

[Manage multiple figures in pyplot](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_figs_demo.html)

Manage multiple figures in pyplot

![](https://matplotlib.org/stable/_images/sphx_glr_figure_size_units_thumb.png)

[Figure size in different units](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html)

Figure size in different units

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_custom_figure_class_thumb.png)

[Custom Figure subclasses](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/custom_figure_class.html)

Custom Figure subclasses

![](https://matplotlib.org/stable/_images/sphx_glr_axes_zoom_effect_thumb.png)

[Axes zoom effect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_zoom_effect.html)

Axes zoom effect

![](https://matplotlib.org/stable/_images/sphx_glr_geo_demo_thumb.png)

[Geographic Projections](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/geo_demo.html)

Geographic Projections

![](https://matplotlib.org/stable/_images/sphx_glr_tick-formatters_thumb.png)

[Tick formatters](https://matplotlib.org/stable/gallery/ticks/tick-formatters.html)

Tick formatters

![](https://matplotlib.org/stable/_images/sphx_glr_fig_axes_customize_simple_thumb.png)

[Customizing figure and axes appearance](https://matplotlib.org/stable/gallery/ticks/fig_axes_customize_simple.html)

Customizing figure and axes appearance

![](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_thumb.png)

[Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)

Asinh scale

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_autowrap_thumb.png)

[Auto-wrap text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/autowrap.html)

Auto-wrap text

![](https://matplotlib.org/stable/_images/sphx_glr_demo_text_rotation_mode_thumb.png)

[Text rotation mode](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_rotation_mode.html)

Text rotation mode

![](https://matplotlib.org/stable/_images/sphx_glr_rainbow_text_thumb.png)

[Concatenate text objects with different properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/rainbow_text.html)

Concatenate text objects with different properties

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_polar_thumb.png)

[Annotate polar plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_polar.html)

Annotate polar plots

![](https://matplotlib.org/stable/_images/sphx_glr_arrow_demo_thumb.png)

[Arrow Demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/arrow_demo.html)

Arrow Demo

![](https://matplotlib.org/stable/_images/sphx_glr_dfrac_demo_thumb.png)

[The difference between \\dfrac and \\frac](https://matplotlib.org/stable/gallery/text_labels_and_annotations/dfrac_demo.html)

The difference between \\dfrac and \\frac

![](https://matplotlib.org/stable/_images/sphx_glr_fonts_demo_thumb.png)

[Fonts demo (object-oriented style)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo.html)

Fonts demo (object-oriented style)

![](https://matplotlib.org/stable/_images/sphx_glr_fonts_demo_kw_thumb.png)

[Fonts demo (keyword arguments)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo_kw.html)

Fonts demo (keyword arguments)

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_asarray_thumb.png)

[Convert texts to images](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_asarray.html)

Convert texts to images

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_examples_thumb.png)

[Mathematical expressions](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_examples.html)

Mathematical expressions

![](https://matplotlib.org/stable/_images/sphx_glr_stix_fonts_demo_thumb.png)

[STIX Fonts](https://matplotlib.org/stable/gallery/text_labels_and_annotations/stix_fonts_demo.html)

STIX Fonts

![](https://matplotlib.org/stable/_images/sphx_glr_unicode_minus_thumb.png)

[Unicode minus](https://matplotlib.org/stable/gallery/text_labels_and_annotations/unicode_minus.html)

Unicode minus

![](https://matplotlib.org/stable/_images/sphx_glr_usetex_baseline_test_thumb.png)

[Usetex text baseline](https://matplotlib.org/stable/gallery/text_labels_and_annotations/usetex_baseline_test.html)

Usetex text baseline

![](https://matplotlib.org/stable/_images/sphx_glr_usetex_fonteffects_thumb.png)

[Usetex font effects](https://matplotlib.org/stable/gallery/text_labels_and_annotations/usetex_fonteffects.html)

Usetex font effects

![](https://matplotlib.org/stable/_images/sphx_glr_artist_reference_thumb.png)

[Reference for Matplotlib artists](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html)

Reference for Matplotlib artists

![](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_thumb.png)

[Drawing fancy boxes](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html)

Drawing fancy boxes

![](https://matplotlib.org/stable/_images/sphx_glr_hatch_demo_thumb.png)

[Hatch demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_demo.html)

Hatch demo

![](https://matplotlib.org/stable/_images/sphx_glr_petroff10_thumb.png)

[Petroff style sheets](https://matplotlib.org/stable/gallery/style_sheets/petroff10.html)

Petroff style sheets

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_two_subplots_thumb.png)

[Two subplots using pyplot](https://matplotlib.org/stable/gallery/pyplots/pyplot_two_subplots.html)

Two subplots using pyplot

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_3d_bars_thumb.png)

[Demo of 3D bar charts](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html)

Demo of 3D bar charts

![](https://matplotlib.org/stable/_images/sphx_glr_bars3d_thumb.png)

[Create 2D bar graphs in different planes](https://matplotlib.org/stable/gallery/mplot3d/bars3d.html)

Create 2D bar graphs in different planes

![](https://matplotlib.org/stable/_images/sphx_glr_box3d_thumb.png)

[3D box surface plot](https://matplotlib.org/stable/gallery/mplot3d/box3d.html)

3D box surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_thumb.png)

[Plot contour (level) curves in 3D](https://matplotlib.org/stable/gallery/mplot3d/contour3d.html)

Plot contour (level) curves in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_2_thumb.png)

[Plot contour (level) curves in 3D using the extend3d option](https://matplotlib.org/stable/gallery/mplot3d/contour3d_2.html)

Plot contour (level) curves in 3D using the extend3d option

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_3_thumb.png)

[Project contour profiles onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html)

Project contour profiles onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_contourf3d_thumb.png)

[Filled contours](https://matplotlib.org/stable/gallery/mplot3d/contourf3d.html)

Filled contours

![](https://matplotlib.org/stable/_images/sphx_glr_contourf3d_2_thumb.png)

[Project filled contour onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contourf3d_2.html)

Project filled contour onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar3d_thumb.png)

[3D errorbars](https://matplotlib.org/stable/gallery/mplot3d/errorbar3d.html)

3D errorbars

![](https://matplotlib.org/stable/_images/sphx_glr_fillbetween3d_thumb.png)

[Fill between 3D lines](https://matplotlib.org/stable/gallery/mplot3d/fillbetween3d.html)

Fill between 3D lines

![](https://matplotlib.org/stable/_images/sphx_glr_fillunder3d_thumb.png)

[Fill under 3D line graphs](https://matplotlib.org/stable/gallery/mplot3d/fillunder3d.html)

Fill under 3D line graphs

![](https://matplotlib.org/stable/_images/sphx_glr_hist3d_thumb.png)

[Create 3D histogram of 2D data](https://matplotlib.org/stable/gallery/mplot3d/hist3d.html)

Create 3D histogram of 2D data

![](https://matplotlib.org/stable/_images/sphx_glr_imshow3d_thumb.png)

[2D images in 3D](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html)

2D images in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_intersecting_planes_thumb.png)

[Intersecting planes](https://matplotlib.org/stable/gallery/mplot3d/intersecting_planes.html)

Intersecting planes

![](https://matplotlib.org/stable/_images/sphx_glr_lines3d_thumb.png)

[Parametric curve](https://matplotlib.org/stable/gallery/mplot3d/lines3d.html)

Parametric curve

![](https://matplotlib.org/stable/_images/sphx_glr_lorenz_attractor_thumb.png)

[Lorenz attractor](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html)

Lorenz attractor

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_offset_thumb.png)

[Automatic text offsetting](https://matplotlib.org/stable/gallery/mplot3d/offset.html)

Automatic text offsetting

![](https://matplotlib.org/stable/_images/sphx_glr_pathpatch3d_thumb.png)

[Draw flat objects in 3D plot](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html)

Draw flat objects in 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_polys3d_thumb.png)

[Generate 3D polygons](https://matplotlib.org/stable/gallery/mplot3d/polys3d.html)

Generate 3D polygons

![](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_thumb.png)

[3D quiver plot](https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html)

3D quiver plot

![](https://matplotlib.org/stable/_images/sphx_glr_rotate_axes3d_sgskip_thumb.png)

[Rotating a 3D plot](https://matplotlib.org/stable/gallery/mplot3d/rotate_axes3d_sgskip.html)

Rotating a 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_scales3d_thumb.png)

[Scales on 3D (Log, Symlog, etc.)](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html)

Scales on 3D (Log, Symlog, etc.)

![](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_thumb.png)

[3D scatterplot](https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html)

3D scatterplot

![](https://matplotlib.org/stable/_images/sphx_glr_subplot3d_thumb.png)

[3D plots as subplots](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html)

3D plots as subplots

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_2_thumb.png)

[3D surface (solid color)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html)

3D surface (solid color)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_3_thumb.png)

[3D surface (checkerboard)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_3.html)

3D surface (checkerboard)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_radial_thumb.png)

[3D surface with polar coordinates](https://matplotlib.org/stable/gallery/mplot3d/surface3d_radial.html)

3D surface with polar coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_text3d_thumb.png)

[Text annotations in 3D](https://matplotlib.org/stable/gallery/mplot3d/text3d.html)

Text annotations in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour3d_thumb.png)

[Triangular 3D contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontour3d.html)

Triangular 3D contour plot

![](https://matplotlib.org/stable/_images/sphx_glr_tricontourf3d_thumb.png)

[Triangular 3D filled contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontourf3d.html)

Triangular 3D filled contour plot

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_thumb.png)

[Triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d.html)

Triangular 3D surfaces

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_2_thumb.png)

[More triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html)

More triangular 3D surfaces

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_thumb.png)

[3D voxel / volumetric plot](https://matplotlib.org/stable/gallery/mplot3d/voxels.html)

3D voxel / volumetric plot

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_numpy_logo_thumb.png)

[3D voxel plot of the NumPy logo](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html)

3D voxel plot of the NumPy logo

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_rgb_thumb.png)

[3D voxel / volumetric plot with RGB colors](https://matplotlib.org/stable/gallery/mplot3d/voxels_rgb.html)

3D voxel / volumetric plot with RGB colors

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_torus_thumb.png)

[3D voxel / volumetric plot with cylindrical coordinates](https://matplotlib.org/stable/gallery/mplot3d/voxels_torus.html)

3D voxel / volumetric plot with cylindrical coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_thumb.png)

[3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d.html)

3D wireframe plot

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_animation_thumb.gif)

[Animate a 3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d_animation.html)

Animate a 3D wireframe plot

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_divider_thumb.png)

[Axes divider](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_divider.html)

Axes divider

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid_thumb.png)

[Demo Axes Grid](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid.html)

Demo Axes Grid

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid2_thumb.png)

[Axes Grid2](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid2.html)

Axes Grid2

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_rgb_thumb.png)

[Show RGB channels using RGBAxes](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_rgb.html)

Show RGB channels using RGBAxes

![](https://matplotlib.org/stable/_images/sphx_glr_demo_edge_colorbar_thumb.png)

[Per-row or per-column colorbars](https://matplotlib.org/stable/gallery/axes_grid1/demo_edge_colorbar.html)

Per-row or per-column colorbars

![](https://matplotlib.org/stable/_images/sphx_glr_demo_fixed_size_axes_thumb.png)

[Axes with a fixed physical size](https://matplotlib.org/stable/gallery/axes_grid1/demo_fixed_size_axes.html)

Axes with a fixed physical size

![](https://matplotlib.org/stable/_images/sphx_glr_demo_imagegrid_aspect_thumb.png)

[ImageGrid cells with a fixed aspect ratio](https://matplotlib.org/stable/gallery/axes_grid1/demo_imagegrid_aspect.html)

ImageGrid cells with a fixed aspect ratio

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_thumb.png)

[Inset locator demo](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html)

Inset locator demo

![](https://matplotlib.org/stable/_images/sphx_glr_make_room_for_ylabel_using_axesgrid_thumb.png)

[Make room for ylabel using axes\_grid](https://matplotlib.org/stable/gallery/axes_grid1/make_room_for_ylabel_using_axesgrid.html)

Make room for ylabel using axes\_grid

![](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple2_thumb.png)

[Parasite Simple2](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple2.html)

Parasite Simple2

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider1_thumb.png)

[Simple Axes Divider 1](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider1.html)

Simple Axes Divider 1

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider3_thumb.png)

[Simple axes divider 3](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider3.html)

Simple axes divider 3

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axesgrid_thumb.png)

[Simple ImageGrid](https://matplotlib.org/stable/gallery/axes_grid1/simple_axesgrid.html)

Simple ImageGrid

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axesgrid2_thumb.png)

[Simple ImageGrid 2](https://matplotlib.org/stable/gallery/axes_grid1/simple_axesgrid2.html)

Simple ImageGrid 2

![](https://matplotlib.org/stable/_images/sphx_glr_axis_direction_thumb.png)

[Axis Direction](https://matplotlib.org/stable/gallery/axisartist/axis_direction.html)

Axis Direction

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_thumb.png)

[axis\_direction demo](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html)

axis\_direction demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axisline_style_thumb.png)

[Axis line styles](https://matplotlib.org/stable/gallery/axisartist/demo_axisline_style.html)

Axis line styles

![](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid_thumb.png)

[Curvilinear grid demo](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html)

Curvilinear grid demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid2_thumb.png)

[Demo CurveLinear Grid2](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid2.html)

Demo CurveLinear Grid2

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_thumb.png)

[floating\_axes features](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html)

floating\_axes features

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axis_thumb.png)

[floating\_axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axis.html)

floating\_axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes_thumb.png)

[Parasite Axes demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html)

Parasite Axes demo

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

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisartist1_thumb.png)

[Custom spines with axisartist](https://matplotlib.org/stable/gallery/axisartist/simple_axisartist1.html)

Custom spines with axisartist

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline_thumb.png)

[Simple Axisline](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html)

Simple Axisline

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline3_thumb.png)

[Simple Axisline3](https://matplotlib.org/stable/gallery/axisartist/simple_axisline3.html)

Simple Axisline3

![](https://matplotlib.org/stable/_images/sphx_glr_double_pendulum_thumb.gif)

[The double pendulum problem](https://matplotlib.org/stable/gallery/animation/double_pendulum.html)

The double pendulum problem

![](https://matplotlib.org/stable/_images/sphx_glr_frame_grabbing_sgskip_thumb.png)

[Frame grabbing](https://matplotlib.org/stable/gallery/animation/frame_grabbing_sgskip.html)

Frame grabbing

![](https://matplotlib.org/stable/_images/sphx_glr_rain_thumb.gif)

[Rain simulation](https://matplotlib.org/stable/gallery/animation/rain.html)

Rain simulation

![](https://matplotlib.org/stable/_images/sphx_glr_random_walk_thumb.gif)

[Animated 3D random walk](https://matplotlib.org/stable/gallery/animation/random_walk.html)

Animated 3D random walk

![](https://matplotlib.org/stable/_images/sphx_glr_unchained_thumb.gif)

[Matplotlib unchained](https://matplotlib.org/stable/gallery/animation/unchained.html)

Matplotlib unchained

![](https://matplotlib.org/stable/_images/sphx_glr_menu_thumb.png)

[Menu](https://matplotlib.org/stable/gallery/widgets/menu.html)

Menu

![](https://matplotlib.org/stable/_images/sphx_glr_rectangle_selector_thumb.png)

[Rectangle and ellipse selectors](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html)

Rectangle and ellipse selectors

![](https://matplotlib.org/stable/_images/sphx_glr_close_event_thumb.png)

[Close event](https://matplotlib.org/stable/gallery/event_handling/close_event.html)

Close event

![](https://matplotlib.org/stable/_images/sphx_glr_ginput_manual_clabel_sgskip_thumb.png)

[Interactive functions](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html)

Interactive functions

![](https://matplotlib.org/stable/_images/sphx_glr_lasso_demo_thumb.png)

[Lasso Demo](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html)

Lasso Demo

![](https://matplotlib.org/stable/_images/sphx_glr_svg_histogram_sgskip_thumb.svg)

[SVG Histogram](https://matplotlib.org/stable/gallery/user_interfaces/svg_histogram_sgskip.html)

SVG Histogram

![](https://matplotlib.org/stable/_images/sphx_glr_toolmanager_sgskip_thumb.png)

[Tool Manager](https://matplotlib.org/stable/gallery/user_interfaces/toolmanager_sgskip.html)

Tool Manager

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_with_units_thumb.png)

[Ellipse with units](https://matplotlib.org/stable/gallery/units/ellipse_with_units.html)

Ellipse with units

![](https://matplotlib.org/stable/_images/sphx_glr_fig_x_thumb.png)

[Add lines directly to a figure](https://matplotlib.org/stable/gallery/misc/fig_x.html)

Add lines directly to a figure

![](https://matplotlib.org/stable/_images/sphx_glr_hyperlinks_sgskip_thumb.png)

[Hyperlinks](https://matplotlib.org/stable/gallery/misc/hyperlinks_sgskip.html)

Hyperlinks

![](https://matplotlib.org/stable/_images/sphx_glr_logos2_thumb.png)

[Matplotlib logo](https://matplotlib.org/stable/gallery/misc/logos2.html)

Matplotlib logo

![](https://matplotlib.org/stable/_images/sphx_glr_multipage_pdf_thumb.svg)

[Multipage PDF](https://matplotlib.org/stable/gallery/misc/multipage_pdf.html)

Multipage PDF

![](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_line_thumb.png)

[Apply SVG filter to a line](https://matplotlib.org/stable/gallery/misc/svg_filter_line.html)

Apply SVG filter to a line

![](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_pie_thumb.png)

[SVG filter pie](https://matplotlib.org/stable/gallery/misc/svg_filter_pie.html)

SVG filter pie

![](https://matplotlib.org/stable/_images/sphx_glr_transoffset_thumb.png)

[transforms.offset\_copy](https://matplotlib.org/stable/gallery/misc/transoffset.html)

transforms.offset\_copy

![](https://matplotlib.org/stable/_images/sphx_glr_zorder_demo_thumb.png)

[Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)

Zorder Demo

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

![](https://matplotlib.org/stable/_images/sphx_glr_firefox_thumb.png)

[Firefox](https://matplotlib.org/stable/gallery/showcase/firefox.html)

Firefox

![](https://matplotlib.org/stable/_images/sphx_glr_mandelbrot_thumb.png)

[Shaded & power normalized rendering](https://matplotlib.org/stable/gallery/showcase/mandelbrot.html)

Shaded & power normalized rendering

![](https://matplotlib.org/stable/_images/sphx_glr_pan_zoom_overlap_thumb.png)

[Pan/zoom events of overlapping axes](https://matplotlib.org/stable/gallery/showcase/pan_zoom_overlap.html)

Pan/zoom events of overlapping axes

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

![](https://matplotlib.org/stable/_images/sphx_glr_leftventricle_bullseye_thumb.png)

[Left ventricle bullseye](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html)

Left ventricle bullseye

![](https://matplotlib.org/stable/_images/sphx_glr_sankey_basics_thumb.png)

[The Sankey class](https://matplotlib.org/stable/gallery/specialty_plots/sankey_basics.html)

The Sankey class

![](https://matplotlib.org/stable/_images/sphx_glr_sankey_links_thumb.png)

[Long chain of connections using Sankey](https://matplotlib.org/stable/gallery/specialty_plots/sankey_links.html)

Long chain of connections using Sankey

![](https://matplotlib.org/stable/_images/sphx_glr_sankey_rankine_thumb.png)

[Rankine power cycle](https://matplotlib.org/stable/gallery/specialty_plots/sankey_rankine.html)

Rankine power cycle

![](https://matplotlib.org/stable/_images/sphx_glr_skewt_thumb.png)

[SkewT-logP diagram: using transforms and custom projections](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html)

SkewT-logP diagram: using transforms and custom projections

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_artists_thumb.png)

[Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html)

Artist tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_thumb.png)

[Coding shortcuts](https://matplotlib.org/stable/tutorials/coding_shortcuts.html)

Coding shortcuts

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_imshow_extent_thumb.png)

[Positioning and orientation of imshow images](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html)

Positioning and orientation of imshow images

![](https://matplotlib.org/stable/_images/sphx_glr_patheffects_guide_thumb.png)

[Path effects guide](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html)

Path effects guide

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_mosaic_thumb.png)

[Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html)

Complex and semantic figure composition (subplot\_mosaic)

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_thumb.png)

[Writing mathematical expressions](https://matplotlib.org/stable/users/explain/text/mathtext.html)

Writing mathematical expressions

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_text_props_thumb.png)

[Text properties and layout](https://matplotlib.org/stable/users/explain/text/text_props.html)

Text properties and layout

On this page
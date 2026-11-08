[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#main-content)

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
    

matplotlib.artist.Artist.set[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib-artist-artist-set "Link to this heading")

=================================================================================================================================================================

Artist.set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1317-L1321)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "Link to this definition")

Set multiple properties at once.

a.set(a\=A, b\=B, c\=C)

is equivalent to

a.set\_a(A)
a.set\_b(B)
a.set\_c(C)

In addition to the full property names, aliases are also supported, e.g. `set(lw=2)` is equivalent to `set(linewidth=2)`, but it is an error to pass both simultaneously.

The order of the individual setter calls matches the order of parameters in `set()`. However, most properties do not depend on each other so that order is rarely relevant.

Supported properties are

> | Property | Description |
> | --- | --- |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Examples using `matplotlib.artist.Artist.set`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#examples-using-matplotlib-artist-artist-set "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_simple_plot_thumb.png)

[Line plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)

Line plot

![](https://matplotlib.org/stable/_images/sphx_glr_axline_thumb.png)

[Infinite lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/axline.html)

Infinite lines

![](https://matplotlib.org/stable/_images/sphx_glr_bar_label_demo_thumb.png)

[Bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html)

Bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_gradient_bar_thumb.png)

[Bar chart with gradients](https://matplotlib.org/stable/gallery/lines_bars_and_markers/gradient_bar.html)

Bar chart with gradients

![](https://matplotlib.org/stable/_images/sphx_glr_timeline_thumb.png)

[Timeline with lines, dates, and text](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html)

Timeline with lines, dates, and text

![](https://matplotlib.org/stable/_images/sphx_glr_irregulardatagrid_thumb.png)

[Contour plot of irregularly spaced data](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html)

Contour plot of irregularly spaced data

![](https://matplotlib.org/stable/_images/sphx_glr_contours_in_optimization_demo_thumb.png)

[Contouring the solution space of optimizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html)

Contouring the solution space of optimizations

![](https://matplotlib.org/stable/_images/sphx_glr_curve_error_band_thumb.png)

[Curve with error band](https://matplotlib.org/stable/gallery/statistics/curve_error_band.html)

Curve with error band

![](https://matplotlib.org/stable/_images/sphx_glr_hexbin_demo_thumb.png)

[Hexagonal binned plot](https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html)

Hexagonal binned plot

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_nested_pie_thumb.png)

[Nested pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html)

Nested pie charts

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_axes_demo_thumb.png)

[Axes Demo](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_demo.html)

Axes Demo

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_yaxis_with_spines_thumb.png)

[Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)

Multiple y-axis with Spines

![](https://matplotlib.org/stable/_images/sphx_glr_axhspan_demo_thumb.png)

[Draw regions that span an Axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html)

Draw regions that span an Axes

![](https://matplotlib.org/stable/_images/sphx_glr_log_demo_thumb.png)

[Log scale](https://matplotlib.org/stable/gallery/scales/log_demo.html)

Log scale

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_thumb.png)

[Annotate plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html)

Annotate plots

![](https://matplotlib.org/stable/_images/sphx_glr_angles_on_bracket_arrows_thumb.png)

[Angle annotations on bracket arrows](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html)

Angle annotations on bracket arrows

![](https://matplotlib.org/stable/_images/sphx_glr_demo_annotation_box_thumb.png)

[Artists as annotations](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html)

Artists as annotations

![](https://matplotlib.org/stable/_images/sphx_glr_arrow_demo_thumb.png)

[Arrow Demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/arrow_demo.html)

Arrow Demo

![](https://matplotlib.org/stable/_images/sphx_glr_usetex_baseline_test_thumb.png)

[Usetex text baseline](https://matplotlib.org/stable/gallery/text_labels_and_annotations/usetex_baseline_test.html)

Usetex text baseline

![](https://matplotlib.org/stable/_images/sphx_glr_artist_reference_thumb.png)

[Reference for Matplotlib artists](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html)

Reference for Matplotlib artists

![](https://matplotlib.org/stable/_images/sphx_glr_donut_thumb.png)

[Mmh Donuts!!!](https://matplotlib.org/stable/gallery/shapes_and_collections/donut.html)

Mmh Donuts!!!

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_demo_thumb.png)

[Ellipse Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html)

Ellipse Demo

![](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_thumb.png)

[Drawing fancy boxes](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html)

Drawing fancy boxes

![](https://matplotlib.org/stable/_images/sphx_glr_axlim_clip_thumb.png)

[Clip the data to the axes view limits](https://matplotlib.org/stable/gallery/mplot3d/axlim_clip.html)

Clip the data to the axes view limits

![](https://matplotlib.org/stable/_images/sphx_glr_box3d_thumb.png)

[3D box surface plot](https://matplotlib.org/stable/gallery/mplot3d/box3d.html)

3D box surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_3_thumb.png)

[Project contour profiles onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html)

Project contour profiles onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_contourf3d_2_thumb.png)

[Project filled contour onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contourf3d_2.html)

Project filled contour onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_fillunder3d_thumb.png)

[Fill under 3D line graphs](https://matplotlib.org/stable/gallery/mplot3d/fillunder3d.html)

Fill under 3D line graphs

![](https://matplotlib.org/stable/_images/sphx_glr_imshow3d_thumb.png)

[2D images in 3D](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html)

2D images in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_stem3d_demo_thumb.png)

[3D stem](https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html)

3D stem

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_rgb_thumb.png)

[3D voxel / volumetric plot with RGB colors](https://matplotlib.org/stable/gallery/mplot3d/voxels_rgb.html)

3D voxel / volumetric plot with RGB colors

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid_thumb.png)

[Demo Axes Grid](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid.html)

Demo Axes Grid

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_thumb.png)

[Inset locator demo](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html)

Inset locator demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_thumb.png)

[axis\_direction demo](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html)

axis\_direction demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes_thumb.png)

[Parasite Axes demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html)

Parasite Axes demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes2_thumb.png)

[Parasite axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html)

Parasite axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_random_walk_thumb.gif)

[Animated 3D random walk](https://matplotlib.org/stable/gallery/animation/random_walk.html)

Animated 3D random walk

![](https://matplotlib.org/stable/_images/sphx_glr_mouse_cursor_thumb.png)

[Mouse Cursor](https://matplotlib.org/stable/gallery/widgets/mouse_cursor.html)

Mouse Cursor

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_grid_thumb.png)

[Radio Buttons Grid](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html)

Radio Buttons Grid

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_thumb.png)

[Pick event demo](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html)

Pick event demo

![](https://matplotlib.org/stable/_images/sphx_glr_viewlims_thumb.png)

[Viewlims](https://matplotlib.org/stable/gallery/event_handling/viewlims.html)

Viewlims

![](https://matplotlib.org/stable/_images/sphx_glr_zoom_window_thumb.png)

[Zoom modifies other Axes](https://matplotlib.org/stable/gallery/event_handling/zoom_window.html)

Zoom modifies other Axes

![](https://matplotlib.org/stable/_images/sphx_glr_contour_manual_thumb.png)

[Manual Contour](https://matplotlib.org/stable/gallery/misc/contour_manual.html)

Manual Contour

![](https://matplotlib.org/stable/_images/sphx_glr_keyword_plotting_thumb.png)

[Plotting with keywords](https://matplotlib.org/stable/gallery/misc/keyword_plotting.html)

Plotting with keywords

![](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_thumb.png)

[Patheffect Demo](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html)

Patheffect Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_thumb.png)

[TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)

TickedStroke patheffect

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

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

![](https://matplotlib.org/stable/_images/sphx_glr_barbs_thumb.png)

[barbs(X, Y, U, V)](https://matplotlib.org/stable/plot_types/arrays/barbs.html)

barbs(X, Y, U, V)

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_thumb.png)

[quiver(X, Y, U, V)](https://matplotlib.org/stable/plot_types/arrays/quiver.html)

quiver(X, Y, U, V)

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

![](https://matplotlib.org/stable/_images/sphx_glr_animations_thumb.gif)

[Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/animations.html)

Animations using Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

On this page
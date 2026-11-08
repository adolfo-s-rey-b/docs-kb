[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#main-content)

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
    

matplotlib.figure.Figure.add\_subplot[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib-figure-figure-add-subplot "Link to this heading")

==========================================================================================================================================================================================

Figure.add\_subplot(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L651-L777)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "Link to this definition")

Add an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to the figure as part of a subplot arrangement.

Call signatures:

add\_subplot(nrows, ncols, index, \*\*kwargs)
add\_subplot(pos, \*\*kwargs)
add\_subplot(ax)
add\_subplot()

Parameters:

**\*args**int, (int, int, _index_), or [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
, default: (1, 1, 1)

The position of the subplot described by one of

*   Three integers (_nrows_, _ncols_, _index_). The subplot will take the _index_ position on a grid with _nrows_ rows and _ncols_ columns. _index_ starts at 1 in the upper left corner and increases to the right. _index_ can also be a two-tuple specifying the (_first_, _last_) indices (1-based, and including _last_) of the subplot, e.g., `fig.add_subplot(3, 1, (1, 2))` makes a subplot that spans the upper 2/3 of the figure.
    
*   A 3-digit integer. The digits are interpreted as if given separately as three single-digit integers, i.e. `fig.add_subplot(235)` is the same as `fig.add_subplot(2, 3, 5)`. Note that this can only be used if there are no more than 9 subplots.
    
*   A [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
    .
    

In rare circumstances, [`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 may be called with a single argument, a subplot Axes instance already created in the present figure but not in the figure's list of Axes.

**projection**{None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}, optional

The projection type of the subplot ([`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
). _str_ is the name of a custom projection, see [`projections`](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "matplotlib.projections")
. The default None results in a 'rectilinear' projection.

**polar**bool, default: False

If True, equivalent to projection='polar'.

**axes\_class**subclass type of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclass that is instantiated. This parameter is incompatible with _projection_ and _polar_. See [axisartist](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-users-guide-index)
 for examples.

**sharex, sharey**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

Share the x or y [`axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 with sharex and/or sharey. The axis will have the same limits, ticks, and scale as the axis of the shared Axes.

**label**str

A label for the returned Axes.

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes of the subplot. The returned Axes can actually be an instance of a subclass, such as [`projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
 for polar projections.

Other Parameters:

**\*\*kwargs**

This method also takes the keyword arguments for the returned Axes base class; except for the _figure_ argument. The keyword arguments for the rectilinear base class [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 can be found in the following table but there might also be other keyword arguments if another projection is used.

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

See also

[`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")

[`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")

[`pyplot.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")

[`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")

[`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

Examples

fig \= plt.figure()

fig.add\_subplot(231)
ax1 \= fig.add\_subplot(2, 3, 1)  \# equivalent but more general

fig.add\_subplot(232, frameon\=False)  \# subplot with no frame
fig.add\_subplot(233, projection\='polar')  \# polar subplot
fig.add\_subplot(234, sharex\=ax1)  \# subplot sharing x-axis with ax1
fig.add\_subplot(235, facecolor\="red")  \# red subplot

ax1.remove()  \# delete ax1 from the figure
fig.add\_subplot(ax1)  \# add ax1 back to the figure

Examples using `matplotlib.figure.Figure.add_subplot`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#examples-using-matplotlib-figure-figure-add-subplot "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_thumb.png)

[Scatter plot with histograms](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html)

Scatter plot with histograms

![](https://matplotlib.org/stable/_images/sphx_glr_eventcollection_demo_thumb.png)

[EventCollection Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html)

EventCollection Demo

![](https://matplotlib.org/stable/_images/sphx_glr_polar_error_caps_thumb.png)

[Error bar rendering on polar axis](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_error_caps.html)

Error bar rendering on polar axis

![](https://matplotlib.org/stable/_images/sphx_glr_polar_legend_thumb.png)

[Polar legend](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html)

Polar legend

![](https://matplotlib.org/stable/_images/sphx_glr_polar_scatter_thumb.png)

[Scatter plot on polar axis](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_scatter.html)

Scatter plot on polar axis

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_customization_thumb.png)

[GridSpec with variable sizes and spacing](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_customization.html)

GridSpec with variable sizes and spacing

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_multicolumn_thumb.png)

[Gridspec for multi-column/row subplot layouts](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_multicolumn.html)

Gridspec for multi-column/row subplot layouts

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_nested_thumb.png)

[Nested Gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)

Nested Gridspecs

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_and_subplots_thumb.png)

[Combine two subplots using subplots and GridSpec](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html)

Combine two subplots using subplots and GridSpec

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_polar_thumb.png)

[Annotate polar plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_polar.html)

Annotate polar plots

![](https://matplotlib.org/stable/_images/sphx_glr_3d_bars_thumb.png)

[Demo of 3D bar charts](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html)

Demo of 3D bar charts

![](https://matplotlib.org/stable/_images/sphx_glr_bars3d_thumb.png)

[Create 2D bar graphs in different planes](https://matplotlib.org/stable/gallery/mplot3d/bars3d.html)

Create 2D bar graphs in different planes

![](https://matplotlib.org/stable/_images/sphx_glr_box3d_thumb.png)

[3D box surface plot](https://matplotlib.org/stable/gallery/mplot3d/box3d.html)

3D box surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_fillbetween3d_thumb.png)

[Fill between 3D lines](https://matplotlib.org/stable/gallery/mplot3d/fillbetween3d.html)

Fill between 3D lines

![](https://matplotlib.org/stable/_images/sphx_glr_hist3d_thumb.png)

[Create 3D histogram of 2D data](https://matplotlib.org/stable/gallery/mplot3d/hist3d.html)

Create 3D histogram of 2D data

![](https://matplotlib.org/stable/_images/sphx_glr_imshow3d_thumb.png)

[2D images in 3D](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html)

2D images in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_pathpatch3d_thumb.png)

[Draw flat objects in 3D plot](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html)

Draw flat objects in 3D plot

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

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_radial_thumb.png)

[3D surface with polar coordinates](https://matplotlib.org/stable/gallery/mplot3d/surface3d_radial.html)

3D surface with polar coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_2_thumb.png)

[More triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html)

More triangular 3D surfaces

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_thumb.png)

[3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d.html)

3D wireframe plot

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_animation_thumb.gif)

[Animate a 3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d_animation.html)

Animate a 3D wireframe plot

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_thumb.png)

[Inset locator demo](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html)

Inset locator demo

![](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple2_thumb.png)

[Parasite Simple2](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple2.html)

Parasite Simple2

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

![](https://matplotlib.org/stable/_images/sphx_glr_random_walk_thumb.gif)

[Animated 3D random walk](https://matplotlib.org/stable/gallery/animation/random_walk.html)

Animated 3D random walk

![](https://matplotlib.org/stable/_images/sphx_glr_canvasagg_thumb.png)

[CanvasAgg demo](https://matplotlib.org/stable/gallery/user_interfaces/canvasagg.html)

CanvasAgg demo

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_with_units_thumb.png)

[Ellipse with units](https://matplotlib.org/stable/gallery/units/ellipse_with_units.html)

Ellipse with units

![](https://matplotlib.org/stable/_images/sphx_glr_pan_zoom_overlap_thumb.png)

[Pan/zoom events of overlapping axes](https://matplotlib.org/stable/gallery/showcase/pan_zoom_overlap.html)

Pan/zoom events of overlapping axes

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

![](https://matplotlib.org/stable/_images/sphx_glr_artists_thumb.png)

[Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html)

Artist tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page
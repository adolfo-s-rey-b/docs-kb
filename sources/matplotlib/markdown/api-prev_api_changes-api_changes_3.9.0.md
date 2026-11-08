[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#main-content)

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
    

API Changes for 3.9.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#api-changes-for-3-9-0 "Link to this heading")

=================================================================================================================================================

[Behaviour Changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#id2)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#behaviour-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### plot() shorthand format interprets "Cn" (n>9) as a color-cycle color[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#plot-shorthand-format-interprets-cn-n-9-as-a-color-cycle-color "Link to this heading")

Previously, `plot(..., "-C11")` would be interpreted as requesting a plot using linestyle "-", color "C1" (color #1 of the color cycle), and marker "1" ("tri-down"). It is now interpreted as requesting linestyle "-" and color "C11" (color #11 of the color cycle).

It is recommended to pass ambiguous markers (such as "1") explicitly using the _marker_ keyword argument. If the shorthand form is desired, such markers can also be unambiguously set by putting them _before_ the color string.

### Legend labels for `plot`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#legend-labels-for-plot "Link to this heading")

Previously if a sequence was passed to the _label_ parameter of [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 when plotting a single dataset, the sequence was automatically cast to string for the legend label. Now, if the sequence has only one element, that element will be the legend label. To keep the old behavior, cast the sequence to string before passing.

### Boxplots now ignore masked data points[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#boxplots-now-ignore-masked-data-points "Link to this heading")

[`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 and [`boxplot_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
 now ignore any masked points in the input data.

### `axhspan` and `axvspan` now return `Rectangle`s, not `Polygon`s[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#axhspan-and-axvspan-now-return-rectangles-not-polygons "Link to this heading")

This change allows using [`axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html#matplotlib.axes.Axes.axhspan "matplotlib.axes.Axes.axhspan")
 to draw an annulus on polar axes.

This change also affects other elements built via [`axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html#matplotlib.axes.Axes.axhspan "matplotlib.axes.Axes.axhspan")
 and [`axvspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan")
, such as `Slider.poly`.

### Improved handling of pan/zoom events of overlapping Axes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#improved-handling-of-pan-zoom-events-of-overlapping-axes "Link to this heading")

The forwarding of pan/zoom events is now determined by the visibility of the background-patch (e.g. `ax.patch.get_visible()`) and by the `zorder` of the axes.

*   Axes with a visible patch capture the event and do not pass it on to axes below. Only the Axes with the highest `zorder` that contains the event is triggered (if there are multiple Axes with the same `zorder`, the last added Axes counts)
    
*   Axes with an invisible patch are also invisible to events and they are passed on to the axes below.
    

To override the default behavior and explicitly set whether an Axes should forward navigation events, use [`Axes.set_forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events")
.

### `loc='best'` for `legend` now considers `Text` and `PolyCollections`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#loc-best-for-legend-now-considers-text-and-polycollections "Link to this heading")

The location selection `legend` now considers the existence of `Text` and `PolyCollections` in the `badness` calculation.

Note: The `best` option can already be quite slow for plots with large amounts of data. For `PolyCollections`, it only considers the `Path` of `PolyCollections` and not the enclosed area when checking for overlap to reduce additional latency. However, it can still be quite slow when there are large amounts of `PolyCollections` in the plot to check for.

### Exception when not passing a Bbox to BboxTransform\*-classes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#exception-when-not-passing-a-bbox-to-bboxtransform-classes "Link to this heading")

The exception when not passing a Bbox to BboxTransform\*-classes that expect one, e.g., [`BboxTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransform "matplotlib.transforms.BboxTransform")
 has changed from `ValueError` to `TypeError`.

### _loc_ parameter of `Cell` no longer accepts `None`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#loc-parameter-of-cell-no-longer-accepts-none "Link to this heading")

The default value of the _loc_ parameter has been changed from `None` to `right`, which already was the default location. The behavior of [`Cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell "matplotlib.table.Cell")
 didn't change when called without an explicit _loc_ parameter.

### `ContourLabeler.add_label` now respects _use\_clabeltext_[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#contourlabeler-add-label-now-respects-use-clabeltext "Link to this heading")

... and sets [`Text.set_transform_rotates_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text "matplotlib.text.Text.set_transform_rotates_text")
 accordingly.

### `Line2D`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#line2d "Link to this heading")

When creating a Line2D or using [`Line2D.set_xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata")
 and [`Line2D.set_ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
, passing x/y data as non sequence is now an error.

### `ScalarMappable`s auto-scale their norm when an array is set[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#scalarmappables-auto-scale-their-norm-when-an-array-is-set "Link to this heading")

Collections previously deferred auto-scaling of the norm until draw time. This has been changed to scale the norm whenever the first array is set to align with the docstring and reduce unexpected behavior when accessing the norm before drawing.

### `SubplotParams` moved from `matplotlib.figure` to `matplotlib.gridspec`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#subplotparams-moved-from-matplotlib-figure-to-matplotlib-gridspec "Link to this heading")

It is still importable from `matplotlib.figure`, so does not require any changes to existing code.

### `PowerNorm` no longer clips values below vmin[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#powernorm-no-longer-clips-values-below-vmin "Link to this heading")

When `clip=False` is set (the default) on [`PowerNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.PowerNorm.html#matplotlib.colors.PowerNorm "matplotlib.colors.PowerNorm")
, values below `vmin` are now linearly normalised. Previously they were clipped to zero. This fixes issues with the display of colorbars associated with a power norm.

### Image path semantics of toolmanager-based tools[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#image-path-semantics-of-toolmanager-based-tools "Link to this heading")

Previously, MEP22 ("toolmanager-based") Tools would try to load their icon (`tool.image`) relative to the current working directory, or, as a fallback, from Matplotlib's own image directory. Because both approaches are problematic for third-party tools (the end-user may change the current working directory at any time, and third-parties cannot add new icons in Matplotlib's image directory), this behavior is deprecated; instead, `tool.image` is now interpreted relative to the directory containing the source file where the `Tool.image` class attribute is defined. (Defining `tool.image` as an absolute path also works and is compatible with both the old and the new semantics.)

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#id3)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `plot_date`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#plot-date "Link to this heading")

Use of `plot_date` has been discouraged since Matplotlib 3.5 and the function is now formally deprecated.

*   `datetime`\-like data should directly be plotted using [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
    .
    
*   If you need to plot plain numeric data as [Matplotlib date format](https://matplotlib.org/stable/api/dates_api.html#date-format)
     or need to set a timezone, call `ax.xaxis.axis_date` / `ax.yaxis.axis_date` before [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
    . See [`Axis.axis_date`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axis_date.html#matplotlib.axis.Axis.axis_date "matplotlib.axis.Axis.axis_date")
    .
    

### Legend labels for `plot`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#id1 "Link to this heading")

Previously if a sequence was passed to the _label_ parameter of [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 when plotting a single dataset, the sequence was automatically cast to string for the legend label. This behavior is now deprecated and in future will error if the sequence length is not one (consistent with multi-dataset behavior, where the number of elements must match the number of datasets). To keep the old behavior, cast the sequence to string before passing.

### `boxplot` tick labels[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#boxplot-tick-labels "Link to this heading")

The parameter _labels_ has been renamed to _tick\_labels_ for clarity and consistency with [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
.

### Mixing positional and keyword arguments for `legend` handles and labels[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#mixing-positional-and-keyword-arguments-for-legend-handles-and-labels "Link to this heading")

This previously only raised a warning, but is now formally deprecated. If passing _handles_ and _labels_, they must be passed either both positionally or both as keyword.

### Applying theta transforms in `PolarTransform`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#applying-theta-transforms-in-polartransform "Link to this heading")

Applying theta transforms in [`PolarTransform`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform "matplotlib.projections.polar.PolarTransform")
 and [`InvertedPolarTransform`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.InvertedPolarTransform "matplotlib.projections.polar.InvertedPolarTransform")
 is deprecated, and will be removed in a future version of Matplotlib. This is currently the default behaviour when these transforms are used externally, but only takes affect when:

*   An axis is associated with the transform.
    
*   The axis has a non-zero theta offset or has theta values increasing in a clockwise direction.
    

To silence this warning and adopt future behaviour, set `apply_theta_transforms=False`. If you need to retain the behaviour where theta values are transformed, chain the `PolarTransform` with a [`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 transform that performs the theta shift and/or sign shift.

### _interval_ parameter of `TimerBase.start`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#interval-parameter-of-timerbase-start "Link to this heading")

Setting the timer _interval_ while starting it is deprecated. The interval can be specified instead in the timer constructor, or by setting the `timer.interval` attribute.

### _nth\_coord_ parameter to axisartist helpers for fixed axis[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#nth-coord-parameter-to-axisartist-helpers-for-fixed-axis "Link to this heading")

Helper APIs in [`axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
 for generating a "fixed" axis on rectilinear axes ([`FixedAxisArtistHelperRectilinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.FixedAxisArtistHelperRectilinear.html#mpl_toolkits.axisartist.axislines.FixedAxisArtistHelperRectilinear "mpl_toolkits.axisartist.axislines.FixedAxisArtistHelperRectilinear")
) no longer take a _nth\_coord_ parameter, as that parameter is entirely inferred from the (required) _loc_ parameter and having inconsistent _nth\_coord_ and _loc_ is an error.

For curvilinear axes, the _nth\_coord_ parameter remains supported (it affects the _ticks_, not the axis position itself), but that parameter will become keyword-only, for consistency with the rectilinear case.

### `rcsetup.interactive_bk`, `rcsetup.non_interactive_bk` and `rcsetup.all_backends`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#rcsetup-interactive-bk-rcsetup-non-interactive-bk-and-rcsetup-all-backends "Link to this heading")

... are deprecated and replaced by `matplotlib.backends.backend_registry.list_builtin` with the following arguments

*   `matplotlib.backends.BackendFilter.INTERACTIVE`
    
*   `matplotlib.backends.BackendFilter.NON_INTERACTIVE`
    
*   `None`
    

respectively.

### Miscellaneous deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#miscellaneous-deprecations "Link to this heading")

*   `backend_ps.get_bbox_header` is considered an internal helper
    
*   `BboxTransformToMaxOnly`; if you rely on this, please make a copy of the code
    
*   `ContourLabeler.add_label_clabeltext`
    
*   `TransformNode.is_bbox`; instead check the object using `isinstance(..., BboxBase)`
    
*   `GridHelperCurveLinear.get_tick_iterator`
    

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#id4)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Top-level cmap registration and access functions in `mpl.cm`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#top-level-cmap-registration-and-access-functions-in-mpl-cm "Link to this heading")

As part of the [multi-step refactoring of colormap registration](https://github.com/matplotlib/matplotlib/issues/20853)
, the following functions have been removed:

*   `matplotlib.cm.get_cmap`; use `matplotlib.colormaps[name]` instead if you have a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
    .
    
    Use [`matplotlib.cm.ColormapRegistry.get_cmap`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.get_cmap "matplotlib.cm.ColormapRegistry.get_cmap")
     if you have a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
    , [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
     or a [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
     object that you want to convert to a [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
     object.
    
*   `matplotlib.cm.register_cmap`; use [`matplotlib.colormaps.register`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
     instead.
    
*   `matplotlib.cm.unregister_cmap`; use [`matplotlib.colormaps.unregister`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.unregister "matplotlib.cm.ColormapRegistry.unregister")
     instead.
    
*   `matplotlib.pyplot.register_cmap`; use [`matplotlib.colormaps.register`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
     instead.
    

The [`matplotlib.pyplot.get_cmap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
 function will stay available for backward compatibility.

### Contour labels[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#contour-labels "Link to this heading")

`contour.ClabelText` and `ContourLabeler.set_label_props` are removed. Use `Text(..., transform_rotates_text=True)` as a replacement for `contour.ClabelText(...)` and `text.set(text=text, color=color, fontproperties=labeler.labelFontProps, clip_box=labeler.axes.bbox)` as a replacement for the `ContourLabeler.set_label_props(label, text, color)`.

The `labelFontProps`, `labelFontSizeList`, and `labelTextsList` attributes of [`ContourLabeler`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler "matplotlib.contour.ContourLabeler")
 have been removed. Use the `labelTexts` attribute and the font properties of the corresponding text objects instead.

### `num2julian`, `julian2num` and `JULIAN_OFFSET`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#num2julian-julian2num-and-julian-offset "Link to this heading")

... of the [`dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 module are removed without replacements. These were undocumented and not exported.

Julian dates in Matplotlib were calculated from a Julian date epoch: `jdate = (date - np.datetime64(EPOCH)) / np.timedelta64(1, 'D')`. Conversely, a Julian date was converted to datetime as `date = np.timedelta64(int(jdate * 24 * 3600), 's') + np.datetime64(EPOCH)`. Matplotlib was using `EPOCH='-4713-11-24T12:00'` so that 2000-01-01 at 12:00 is 2\_451\_545.0 (see [https://en.wikipedia.org/wiki/Julian\_day](https://en.wikipedia.org/wiki/Julian_day)
).

### `offsetbox` methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#offsetbox-methods "Link to this heading")

`offsetbox.bbox_artist` is removed. This was just a wrapper to call [`patches.bbox_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.bbox_artist.html#matplotlib.patches.bbox_artist "matplotlib.patches.bbox_artist")
 if a flag is set in the file, so use that directly if you need the behavior.

`OffsetBox.get_extent_offsets` and `OffsetBox.get_extent` are removed; these methods are also removed on all subclasses of [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
. To get the offsetbox extents, instead of `get_extent`, use [`OffsetBox.get_bbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_bbox "matplotlib.offsetbox.OffsetBox.get_bbox")
, which directly returns a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 instance. To also get the child offsets, instead of `get_extent_offsets`, separately call [`get_offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_offset "matplotlib.offsetbox.OffsetBox.get_offset")
 on each children after triggering a draw.

### `parse_fontconfig_pattern` raises on unknown constant names[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#parse-fontconfig-pattern-raises-on-unknown-constant-names "Link to this heading")

Previously, in a fontconfig pattern like `DejaVu Sans:foo`, the unknown `foo` constant name would be silently ignored. This now raises an error.

### `tri` submodules[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#tri-submodules "Link to this heading")

The `matplotlib.tri.*` submodules are removed. All functionality is available in `matplotlib.tri` directly and should be imported from there.

### Widget API[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#widget-api "Link to this heading")

*   `CheckButtons.rectangles` and `CheckButtons.lines` are removed; [`CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
     now draws itself using [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
    .
    
*   `RadioButtons.circles` is removed; [`RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
     now draws itself using [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
    .
    
*   `MultiCursor.needclear` is removed with no replacement.
    
*   The unused parameter _x_ to `TextBox.begin_typing` was a required argument, and is now removed.
    

#### Most arguments to widgets have been made keyword-only[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#most-arguments-to-widgets-have-been-made-keyword-only "Link to this heading")

Passing all but the very few first arguments positionally in the constructors of Widgets is now keyword-only. In general, all optional arguments are keyword-only.

### `Axes3D` API[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#axes3d-api "Link to this heading")

*   `Axes3D.unit_cube`, `Axes3D.tunit_cube`, and `Axes3D.tunit_edges` are removed without replacement.
    
*   `axes3d.vvec`, `axes3d.eye`, `axes3d.sx`, and `axes3d.sy` are removed without replacement.
    

### Inconsistent _nth\_coord_ and _loc_ passed to `_FixedAxisArtistHelperBase`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#inconsistent-nth-coord-and-loc-passed-to-fixedaxisartisthelperbase "Link to this heading")

The value of the _nth\_coord_ parameter of `_FixedAxisArtistHelperBase` and its subclasses is now inferred from the value of _loc_; passing inconsistent values (e.g., requesting a "top y axis" or a "left x axis") has no more effect.

### Passing undefined _label\_mode_ to `Grid`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#passing-undefined-label-mode-to-grid "Link to this heading")

... is no longer allowed. This includes [`mpl_toolkits.axes_grid1.axes_grid.Grid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.axes_grid.Grid")
, [`mpl_toolkits.axes_grid1.axes_grid.AxesGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.AxesGrid.html#mpl_toolkits.axes_grid1.axes_grid.AxesGrid "mpl_toolkits.axes_grid1.axes_grid.AxesGrid")
, and [`mpl_toolkits.axes_grid1.axes_grid.ImageGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.axes_grid.ImageGrid")
 as well as the corresponding classes imported from `mpl_toolkits.axisartist.axes_grid`.

Pass `label_mode='keep'` instead to get the previous behavior of not modifying labels.

### `draw_gouraud_triangle`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#draw-gouraud-triangle "Link to this heading")

... is removed. Use [`draw_gouraud_triangles`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_gouraud_triangles "matplotlib.backend_bases.RendererBase.draw_gouraud_triangles")
 instead.

A `draw_gouraud_triangle` call in a custom [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 can readily be replaced as:

self.draw\_gouraud\_triangles(gc, points.reshape((1, 3, 2)),
                            colors.reshape((1, 3, 4)), trans)

A [`draw_gouraud_triangles`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_gouraud_triangles "matplotlib.backend_bases.RendererBase.draw_gouraud_triangles")
 method can be implemented from an existing `draw_gouraud_triangle` method as:

transform \= transform.frozen()
for tri, col in zip(triangles\_array, colors\_array):
    self.draw\_gouraud\_triangle(gc, tri, col, transform)

### Miscellaneous removals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#miscellaneous-removals "Link to this heading")

The following items have previously been replaced, and are now removed:

*   _ticklabels_ parameter of `matplotlib.axis.Axis.set_ticklabels` has been renamed to _labels_.
    
*   `Barbs.barbs_doc` and `Quiver.quiver_doc` are removed. These are the doc-strings and should not be accessible as a named class member, but as normal doc-strings would.
    
*   `collections.PolyCollection.span_where` and `collections.BrokenBarHCollection`; use `fill_between` instead.
    
*   `Legend.legendHandles` was undocumented and has been renamed to `legend_handles`.
    

The following items have been removed without replacements:

*   The attributes `repeat` of [`TimedAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation "matplotlib.animation.TimedAnimation")
     and subclasses and `save_count` of [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
     are considered private and removed.
    
*   `matplotlib.backend.backend_agg.BufferRegion.to_string`
    
*   `matplotlib.backend.backend_agg.BufferRegion.to_string_argb`
    
*   `matplotlib.backends.backend_ps.PsBackendHelper`
    
*   `matplotlib.backends.backend_webagg.ServerThread`
    
*   _raw_ parameter of [`GridSpecBase.get_grid_positions`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.get_grid_positions "matplotlib.gridspec.GridSpecBase.get_grid_positions")
    
*   `matplotlib.patches.ConnectionStyle._Base.SimpleEvent`
    
*   `passthru_pt` attribute of `mpl_toolkits.axisartist.AxisArtistHelper`
    

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#id5)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#development-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Build system ported to Meson[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#build-system-ported-to-meson "Link to this heading")

The build system of Matplotlib has been ported from setuptools to [meson-python](https://meson-python.readthedocs.io/)
 and [Meson](https://mesonbuild.com/)
. Consequently, there have been a few changes for development and packaging purposes.

1.  Installation by `pip` of packages with `pyproject.toml` use [build isolation](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/#build-isolation)
     by default, which interferes with editable installation. Thus for developers using editable installs, it is now necessary to pass the `--no-build-isolation` flag to `pip install`. This means that all build-time requirements must be available in the environment for an editable install.
    
2.  Build configuration has moved from a custom `mplsetup.cfg` (also configurable via `MPLSETUP` environment variable) to Meson options. These may be specified using [meson-python's build config settings](https://meson-python.readthedocs.io/en/stable/how-to-guides/config-settings.html)
     for `setup-args`. See `meson_options.txt` for all options. For example, a `mplsetup.cfg` containing the following:
    
    \[rc\_options\]
    backend\=Agg
    
    \[libs\]
    system\_qhull \= True
    
    may be replaced by passing the following arguments to `pip`:
    
    \--config\-settings\=setup\-args\="-DrcParams-backend=Agg"
    \--config\-settings\=setup\-args\="-Dsystem-qhull=true"
    
    Note that you must use `pip` >= 23.1 in order to pass more than one setting.
    
3.  Relatedly, Meson's [builtin options](https://mesonbuild.com/Builtin-options.html)
     are now used instead of custom options, e.g., the LTO option is now `b_lto`.
    
4.  On Windows, Meson activates a Visual Studio environment automatically. However, it will not do so if another compiler is available. See [Meson's documentation](https://mesonbuild.com/Builtin-options.html#details-for-vsenv)
     if you wish to change the priority of chosen compilers.
    
5.  Installation of test data was previously controlled by `mplsetup.cfg`, but has now been moved to Meson's install tags. To install test data, add the `tests` tag to the requested install (be sure to include the existing tags as below):
    
    \--config\-settings\=install\-args\="--tags=data,python-runtime,runtime,tests"
    
6.  Checking typing stubs with `stubtest` does not work easily with editable install. For the time being, we suggest using a normal (non-editable) install if you wish to run `stubtest`.
    

### Increase to minimum supported versions of dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#increase-to-minimum-supported-versions-of-dependencies "Link to this heading")

For Matplotlib 3.9, the [minimum supported versions](https://matplotlib.org/stable/install/dependencies.html#dependencies)
 are being bumped:

| Dependency | min in mpl3.8 | min in mpl3.9 |
| --- | --- | --- |
| NumPy | 1.21.0 | 1.23.0 |
| setuptools | 42  | 64  |

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)
 and [SPEC 0](https://scientific-python.org/specs/spec-0000/)
.

To comply with requirements of `setuptools_scm`, the minimum version of `setuptools` has been increased from 42 to 64.

### Extensions require C++17[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#extensions-require-c-17 "Link to this heading")

Matplotlib now requires a compiler that supports C++17 in order to build its extensions. According to [SciPy's analysis](https://docs.scipy.org/doc/scipy/dev/toolchain.html#c-language-standards)
, this should be available on all supported platforms.

### Windows on ARM64 support[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.0.html#windows-on-arm64-support "Link to this heading")

Windows on ARM64 now bundles FreeType 2.6.1 instead of 2.11.1 when building from source. This may cause small changes to text rendering, but should become consistent with all other platforms.

On this page
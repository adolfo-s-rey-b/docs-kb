[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#main-content)

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
    

API Changes for 3.7.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#api-changes-for-3-7-0 "Link to this heading")

=================================================================================================================================================

[Behaviour Changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#id1)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#behaviour-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### All Axes have `get_subplotspec` and `get_gridspec` methods now, which returns None for Axes not positioned via a gridspec[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#all-axes-have-get-subplotspec-and-get-gridspec-methods-now-which-returns-none-for-axes-not-positioned-via-a-gridspec "Link to this heading")

Previously, this method was only present for Axes positioned via a gridspec. Following this change, checking `hasattr(ax, "get_gridspec")` should now be replaced by `ax.get_gridspec() is not None`. For compatibility with older Matplotlib releases, one can also check `hasattr(ax, "get_gridspec") and ax.get_gridspec() is not None`.

### `HostAxesBase.get_aux_axes` now defaults to using the same base axes class as the host axes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#hostaxesbase-get-aux-axes-now-defaults-to-using-the-same-base-axes-class-as-the-host-axes "Link to this heading")

If using an `mpl_toolkits.axisartist`\-based host Axes, the parasite Axes will also be based on `mpl_toolkits.axisartist`. This behavior is consistent with `HostAxesBase.twin`, `HostAxesBase.twinx`, and `HostAxesBase.twiny`.

### `plt.get_cmap` and `matplotlib.cm.get_cmap` return a copy[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#plt-get-cmap-and-matplotlib-cm-get-cmap-return-a-copy "Link to this heading")

Formerly, [`get_cmap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
 and `matplotlib.cm.get_cmap` returned a global version of a [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
. This was prone to errors as modification of the colormap would propagate from one location to another without warning. Now, a new copy of the colormap is returned.

### `TrapezoidMapTriFinder` uses different random number generator[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#trapezoidmaptrifinder-uses-different-random-number-generator "Link to this heading")

The random number generator used to determine the order of insertion of triangle edges in `TrapezoidMapTriFinder` has changed. This can result in a different triangle index being returned for a point that lies exactly on an edge between two triangles. This can also affect triangulation interpolation and refinement algorithms that use `TrapezoidMapTriFinder`.

### `FuncAnimation(save_count=None)`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#funcanimation-save-count-none "Link to this heading")

Passing `save_count=None` to [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 no longer limits the number of frames to 100. Make sure that it either can be inferred from _frames_ or provide an integer _save\_count_.

### `CenteredNorm` halfrange is not modified when vcenter changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#centerednorm-halfrange-is-not-modified-when-vcenter-changes "Link to this heading")

Previously, the **halfrange** would expand in proportion to the amount that **vcenter** was moved away from either **vmin** or **vmax**. Now, the halfrange remains fixed when vcenter is changed, and **vmin** and **vmax** are updated based on the **vcenter** and **halfrange** values.

For example, this is what the values were when changing vcenter previously.

norm \= CenteredNorm(vcenter\=0, halfrange\=1)
\# Move vcenter up by one
norm.vcenter \= 1
\# updates halfrange and vmax (vmin stays the same)
\# norm.halfrange == 2, vmin == -1, vmax == 3

and now, with that same example

norm \= CenteredNorm(vcenter\=0, halfrange\=1)
norm.vcenter \= 1
\# updates vmin and vmax (halfrange stays the same)
\# norm.halfrange == 1, vmin == 0, vmax == 2

The **halfrange** can be set manually or `norm.autoscale()` can be used to automatically set the limits after setting **vcenter**.

### `fig.subplot_mosaic` no longer passes the `gridspec_kw` args to nested gridspecs.[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#fig-subplot-mosaic-no-longer-passes-the-gridspec-kw-args-to-nested-gridspecs "Link to this heading")

For nested [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 layouts, it is almost always inappropriate for _gridspec\_kw_ arguments to be passed to lower nest levels, and these arguments are incompatible with the lower levels in many cases. This dictionary is no longer passed to the inner layouts. Users who need to modify _gridspec\_kw_ at multiple levels should use [`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 to get nesting, and construct the inner layouts with [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 or [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
.

### `HPacker` alignment with **bottom** or **top** are now correct[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#hpacker-alignment-with-bottom-or-top-are-now-correct "Link to this heading")

Previously, the **bottom** and **top** alignments were swapped. This has been corrected so that the alignments correspond appropriately.

### On Windows only fonts known to the registry will be discovered[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#on-windows-only-fonts-known-to-the-registry-will-be-discovered "Link to this heading")

Previously, Matplotlib would recursively walk user and system font directories to discover fonts, however this lead to a number of undesirable behaviors including finding deleted fonts. Now Matplotlib will only find fonts that are known to the Windows registry.

This means that any user installed fonts must go through the Windows font installer rather than simply being copied to the correct folder.

This only impacts the set of fonts Matplotlib will consider when using [`matplotlib.font_manager.findfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "matplotlib.font_manager.findfont")
. To use an arbitrary font, directly pass the path to a font as shown in [Using ttf font files](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_file.html)
.

### `QuadMesh.set_array` now always raises `ValueError` for inputs with incorrect shapes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#quadmesh-set-array-now-always-raises-valueerror-for-inputs-with-incorrect-shapes "Link to this heading")

It could previously also raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 in some cases.

### `contour` and `contourf` auto-select suitable levels when given boolean inputs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#contour-and-contourf-auto-select-suitable-levels-when-given-boolean-inputs "Link to this heading")

If the height array given to [`Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 or [`Axes.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
 is of bool dtype and _levels_ is not specified, _levels_ now defaults to `[0.5]` for [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 and `[0, 0.5, 1]` for [`Axes.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
.

### `contour` no longer warns if no contour lines are drawn.[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#contour-no-longer-warns-if-no-contour-lines-are-drawn "Link to this heading")

This can occur if the user explicitly passes a `levels` array with no values between `z.min()` and `z.max()`; or if `z` has the same value everywhere.

### `AxesImage.set_extent` now raises `TypeError` for unknown keyword arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#axesimage-set-extent-now-raises-typeerror-for-unknown-keyword-arguments "Link to this heading")

It previously raised a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
.

### Change of `legend(loc="best")` behavior[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#change-of-legend-loc-best-behavior "Link to this heading")

The algorithm of the auto-legend locator has been tweaked to better handle non rectangular patches. Additional details on this change can be found in [#9580](https://github.com/matplotlib/matplotlib/issues/9580/)
 and [#9598](https://github.com/matplotlib/matplotlib/issues/9598/)
.

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#id2)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `Axes` subclasses should override `clear` instead of `cla`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#axes-subclasses-should-override-clear-instead-of-cla "Link to this heading")

For clarity, [`axes.Axes.clear`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clear.html#matplotlib.axes.Axes.clear "matplotlib.axes.Axes.clear")
 is now preferred over [`Axes.cla`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.cla.html#matplotlib.axes.Axes.cla "matplotlib.axes.Axes.cla")
. However, for backwards compatibility, the latter will remain as an alias for the former.

For additional compatibility with third-party libraries, Matplotlib will continue to call the `cla` method of any [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclasses if they define it. In the future, this will no longer occur, and Matplotlib will only call the `clear` method in [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclasses.

It is recommended to define only the `clear` method when on Matplotlib 3.6, and only `cla` for older versions.

### rcParams type[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#rcparams-type "Link to this heading")

Relying on `rcParams` being a `dict` subclass is deprecated.

Nothing will change for regular users because `rcParams` will continue to be dict-like (technically fulfill the `MutableMapping` interface).

The [`RcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
 class does validation checking on calls to `.RcParams.__getitem__` and `.RcParams.__setitem__`. However, there are rare cases where we want to circumvent the validation logic and directly access the underlying data values. Previously, this could be accomplished via a call to the parent methods `dict.__getitem__(rcParams, key)` and `dict.__setitem__(rcParams, key, val)`.

Matplotlib 3.7 introduces `rcParams._set(key, val)` and `rcParams._get(key)` as a replacement to calling the parent methods. They are intentionally marked private to discourage external use; However, if direct [`RcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
 data access is needed, please switch from the dict functions to the new `_get()` and `_set()`. Even though marked private, we guarantee API stability for these methods and they are subject to Matplotlib's API and deprecation policy.

Please notify the Matplotlib developers if you rely on `rcParams` being a dict subclass in any other way, for which there is no migration path yet.

### Deprecation aliases in cbook[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#deprecation-aliases-in-cbook "Link to this heading")

The module `matplotlib.cbook.deprecation` was previously deprecated in Matplotlib 3.4, along with deprecation-related API in `matplotlib.cbook`. Due to technical issues, `matplotlib.cbook.MatplotlibDeprecationWarning` and `matplotlib.cbook.mplDeprecation` did not raise deprecation warnings on use. Changes in Python have now made it possible to warn when these aliases are being used.

In order to avoid downstream breakage, these aliases will now warn, and their removal has been pushed from 3.6 to 3.8 to give time to notice said warnings. As replacement, please use [`matplotlib.MatplotlibDeprecationWarning`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.MatplotlibDeprecationWarning "matplotlib.MatplotlibDeprecationWarning")
.

### `draw_gouraud_triangle`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#draw-gouraud-triangle "Link to this heading")

... is deprecated as in most backends this is a redundant call. Use [`draw_gouraud_triangles`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_gouraud_triangles "matplotlib.backend_bases.RendererBase.draw_gouraud_triangles")
 instead. A `draw_gouraud_triangle` call in a custom [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 can readily be replaced as:

self.draw\_gouraud\_triangles(gc, points.reshape((1, 3, 2)),
                            colors.reshape((1, 3, 4)), trans)

A [`draw_gouraud_triangles`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_gouraud_triangles "matplotlib.backend_bases.RendererBase.draw_gouraud_triangles")
 method can be implemented from an existing `draw_gouraud_triangle` method as:

transform \= transform.frozen()
for tri, col in zip(triangles\_array, colors\_array):
    self.draw\_gouraud\_triangle(gc, tri, col, transform)

### `matplotlib.pyplot.get_plot_commands`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#matplotlib-pyplot-get-plot-commands "Link to this heading")

... is a pending deprecation. This is considered internal and no end-user should need it.

### `matplotlib.tri` submodules are deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#matplotlib-tri-submodules-are-deprecated "Link to this heading")

The `matplotlib.tri.*` submodules are deprecated. All functionality is available in `matplotlib.tri` directly and should be imported from there.

### Passing undefined _label\_mode_ to `Grid`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#passing-undefined-label-mode-to-grid "Link to this heading")

... is deprecated. This includes [`mpl_toolkits.axes_grid1.axes_grid.Grid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.axes_grid.Grid")
, [`mpl_toolkits.axes_grid1.axes_grid.AxesGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.AxesGrid.html#mpl_toolkits.axes_grid1.axes_grid.AxesGrid "mpl_toolkits.axes_grid1.axes_grid.AxesGrid")
, and [`mpl_toolkits.axes_grid1.axes_grid.ImageGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.axes_grid.ImageGrid")
 as well as the corresponding classes imported from `mpl_toolkits.axisartist.axes_grid`.

Pass `label_mode='keep'` instead to get the previous behavior of not modifying labels.

### Colorbars for orphaned mappables are deprecated, but no longer raise[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#colorbars-for-orphaned-mappables-are-deprecated-but-no-longer-raise "Link to this heading")

Before 3.6.0, Colorbars for mappables that do not have a parent axes would steal space from the current Axes. 3.6.0 raised an error on this, but without a deprecation cycle. For 3.6.1 this is reverted, the current axes is used, but a deprecation warning is shown instead. In this undetermined case users and libraries should explicitly specify what axes they want space to be stolen from: `fig.colorbar(mappable, ax=plt.gca())`.

### `Animation` attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#animation-attributes "Link to this heading")

The attributes `repeat` of [`TimedAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation "matplotlib.animation.TimedAnimation")
 and subclasses and `save_count` of [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 are considered private and deprecated.

### `contour.ClabelText` and `ContourLabeler.set_label_props`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#contour-clabeltext-and-contourlabeler-set-label-props "Link to this heading")

... are deprecated.

Use `Text(..., transform_rotates_text=True)` as a replacement for `contour.ClabelText(...)` and `text.set(text=text, color=color, fontproperties=labeler.labelFontProps, clip_box=labeler.axes.bbox)` as a replacement for the `ContourLabeler.set_label_props(label, text, color)`.

### `ContourLabeler` attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#contourlabeler-attributes "Link to this heading")

The `labelFontProps`, `labelFontSizeList`, and `labelTextsList` attributes of [`ContourLabeler`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler "matplotlib.contour.ContourLabeler")
 have been deprecated. Use the `labelTexts` attribute and the font properties of the corresponding text objects instead.

### `backend_ps.PsBackendHelper` and `backend_ps.ps_backend_helper`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#backend-ps-psbackendhelper-and-backend-ps-ps-backend-helper "Link to this heading")

... are deprecated with no replacement.

### `backend_webagg.ServerThread` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#backend-webagg-serverthread-is-deprecated "Link to this heading")

... with no replacement.

### `parse_fontconfig_pattern` will no longer ignore unknown constant names[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#parse-fontconfig-pattern-will-no-longer-ignore-unknown-constant-names "Link to this heading")

Previously, in a fontconfig pattern like `DejaVu Sans:foo`, the unknown `foo` constant name would be silently ignored. This now raises a warning, and will become an error in the future.

### `BufferRegion.to_string` and `BufferRegion.to_string_argb`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#bufferregion-to-string-and-bufferregion-to-string-argb "Link to this heading")

... are deprecated. Use `np.asarray(buffer_region)` to get an array view on a buffer region without making a copy; to convert that view from RGBA (the default) to ARGB, use `np.take(..., [2, 1, 0, 3], axis=2)`.

### `num2julian`, `julian2num` and `JULIAN_OFFSET`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#num2julian-julian2num-and-julian-offset "Link to this heading")

... of the [`dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 module are deprecated without replacements. These are undocumented and not exported. If you rely on these, please make a local copy.

### `unit_cube`, `tunit_cube`, and `tunit_edges`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#unit-cube-tunit-cube-and-tunit-edges "Link to this heading")

... of [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 are deprecated without replacements. If you rely on them, please copy the code of the corresponding private function (name starting with `_`).

### Most arguments to widgets have been made keyword-only[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#most-arguments-to-widgets-have-been-made-keyword-only "Link to this heading")

Passing all but the very few first arguments positionally in the constructors of Widgets is deprecated. Most arguments will become keyword-only in a future version.

### `SimpleEvent`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#simpleevent "Link to this heading")

The `SimpleEvent` nested class (previously accessible via the public subclasses of `ConnectionStyle._Base`, such as [`ConnectionStyle.Arc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Arc "matplotlib.patches.ConnectionStyle.Arc")
, has been deprecated.

### `RadioButtons.circles`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#radiobuttons-circles "Link to this heading")

... is deprecated. (RadioButtons now draws itself using [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
.)

### `CheckButtons.rectangles` and `CheckButtons.lines`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#checkbuttons-rectangles-and-checkbuttons-lines "Link to this heading")

`CheckButtons.rectangles` and `CheckButtons.lines` are deprecated. (`CheckButtons` now draws itself using [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
.)

### `OffsetBox.get_extent_offsets` and `OffsetBox.get_extent`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#offsetbox-get-extent-offsets-and-offsetbox-get-extent "Link to this heading")

... are deprecated; these methods are also deprecated on all subclasses of [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
.

To get the offsetbox extents, instead of `get_extent`, use [`OffsetBox.get_bbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_bbox "matplotlib.offsetbox.OffsetBox.get_bbox")
, which directly returns a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 instance.

To also get the child offsets, instead of `get_extent_offsets`, separately call [`get_offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_offset "matplotlib.offsetbox.OffsetBox.get_offset")
 on each children after triggering a draw.

### `legend.legendHandles`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#legend-legendhandles "Link to this heading")

... was undocumented and has been renamed to `legend_handles`. Using `legendHandles` is deprecated.

### `ticklabels` parameter of [`Axis.set_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib.axis.Axis.set_ticklabels "matplotlib.axis.Axis.set_ticklabels")
 renamed to `labels`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#ticklabels-parameter-of-axis-set-ticklabels-renamed-to-labels "Link to this heading")

### `offsetbox.bbox_artist`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#offsetbox-bbox-artist "Link to this heading")

... is deprecated. This is just a wrapper to call [`patches.bbox_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.bbox_artist.html#matplotlib.patches.bbox_artist "matplotlib.patches.bbox_artist")
 if a flag is set in the file, so use that directly if you need the behavior.

### `Quiver.quiver_doc` and `Barbs.barbs_doc`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#quiver-quiver-doc-and-barbs-barbs-doc "Link to this heading")

... are deprecated. These are the doc-string and should not be accessible as a named class member.

### Deprecate unused parameter _x_ to `TextBox.begin_typing`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#deprecate-unused-parameter-x-to-textbox-begin-typing "Link to this heading")

This parameter was unused in the method, but was a required argument.

### Deprecation of top-level cmap registration and access functions in `mpl.cm`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#deprecation-of-top-level-cmap-registration-and-access-functions-in-mpl-cm "Link to this heading")

As part of a [multi-step process](https://github.com/matplotlib/matplotlib/issues/20853)
 we are refactoring the global state for managing the registered colormaps.

In Matplotlib 3.5 we added a [`ColormapRegistry`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
 class and exposed an instance at the top level as `matplotlib.colormaps`. The existing top level functions in [`matplotlib.cm`](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")
 (`get_cmap`, `register_cmap`, `unregister_cmap`) were changed to be aliases around the same instance. In Matplotlib 3.6 we have marked those top level functions as pending deprecation.

In Matplotlib 3.7, the following functions have been marked for deprecation:

*   `matplotlib.cm.get_cmap`; use `matplotlib.colormaps[name]` instead if you have a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
    .
    
    **Added 3.6.1** Use [`matplotlib.cm.ColormapRegistry.get_cmap`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.get_cmap "matplotlib.cm.ColormapRegistry.get_cmap")
     if you have a string, [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
     or a [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
     object that you want to convert to a [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
     instance.
    
*   `matplotlib.cm.register_cmap`; use [`matplotlib.colormaps.register`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
     instead
    
*   `matplotlib.cm.unregister_cmap`; use [`matplotlib.colormaps.unregister`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.unregister "matplotlib.cm.ColormapRegistry.unregister")
     instead
    
*   `matplotlib.pyplot.register_cmap`; use [`matplotlib.colormaps.register`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
     instead
    

The [`matplotlib.pyplot.get_cmap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
 function will stay available for backward compatibility.

### `BrokenBarHCollection` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#brokenbarhcollection-is-deprecated "Link to this heading")

It was just a thin wrapper inheriting from [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
; [`broken_barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
 has now been changed to return a [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 instead.

The `BrokenBarHCollection.span_where` helper is likewise deprecated; for the duration of the deprecation it has been moved to the parent [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 class. Use [`fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
 as a replacement; see [Shade regions defined by a logical mask using fill\_between](https://matplotlib.org/stable/gallery/lines_bars_and_markers/span_regions.html)
 for an example.

### Passing inconsistent `loc` and `nth_coord` to axisartist helpers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#passing-inconsistent-loc-and-nth-coord-to-axisartist-helpers "Link to this heading")

Trying to construct for example a "top y-axis" or a "left x-axis" is now deprecated.

### `passthru_pt`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#passthru-pt "Link to this heading")

This attribute of `AxisArtistHelper`s is deprecated.

### `axes3d.vvec`, `axes3d.eye`, `axes3d.sx`, and `axes3d.sy`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#axes3d-vvec-axes3d-eye-axes3d-sx-and-axes3d-sy "Link to this heading")

... are deprecated without replacement.

### `Line2D`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#line2d "Link to this heading")

When creating a Line2D or using [`Line2D.set_xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata")
 and [`Line2D.set_ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
, passing x/y data as non sequence is deprecated.

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#id3)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `epoch2num` and `num2epoch` are removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#epoch2num-and-num2epoch-are-removed "Link to this heading")

These methods convert from unix timestamps to matplotlib floats, but are not used internally to Matplotlib, and should not be needed by end users. To convert a unix timestamp to datetime, simply use [`datetime.datetime.fromtimestamp`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp "(in Python v3.14)")
, or to use NumPy [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 `dt = np.datetime64(e*1e6, 'us')`.

### Locator and Formatter wrapper methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#locator-and-formatter-wrapper-methods "Link to this heading")

The `set_view_interval`, `set_data_interval` and `set_bounds` methods of [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
s and [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
s (and their common base class, TickHelper) are removed. Directly manipulate the view and data intervals on the underlying axis instead.

### Interactive cursor details[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#interactive-cursor-details "Link to this heading")

Setting a mouse cursor on a window has been moved from the toolbar to the canvas. Consequently, several implementation details on toolbars and within backends have been removed.

#### `NavigationToolbar2.set_cursor` and `backend_tools.SetCursorBase.set_cursor`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#navigationtoolbar2-set-cursor-and-backend-tools-setcursorbase-set-cursor "Link to this heading")

Instead, use the [`FigureCanvasBase.set_cursor`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.set_cursor "matplotlib.backend_bases.FigureCanvasBase.set_cursor")
 method on the canvas (available as the `canvas` attribute on the toolbar or the Figure.)

#### `backend_tools.SetCursorBase` and subclasses[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#backend-tools-setcursorbase-and-subclasses "Link to this heading")

`backend_tools.SetCursorBase` was subclassed to provide backend-specific implementations of `set_cursor`. As that is now removed, the subclassing is no longer necessary. Consequently, the following subclasses are also removed:

*   `matplotlib.backends.backend_gtk3.SetCursorGTK3`
    
*   `matplotlib.backends.backend_qt5.SetCursorQt`
    
*   `matplotlib.backends._backend_tk.SetCursorTk`
    
*   `matplotlib.backends.backend_wx.SetCursorWx`
    

Instead, use the [`backend_tools.ToolSetCursor`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolSetCursor "matplotlib.backend_tools.ToolSetCursor")
 class.

#### `cursord` in GTK and wx backends[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#cursord-in-gtk-and-wx-backends "Link to this heading")

The `backend_gtk3.cursord` and `backend_wx.cursord` dictionaries are removed. This makes the GTK module importable on headless environments.

### `auto_add_to_figure=True` for `Axes3D`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#auto-add-to-figure-true-for-axes3d "Link to this heading")

... is no longer supported. Instead use `fig.add_axes(ax)`.

### The first parameter of `Axes.grid` and `Axis.grid` has been renamed to _visible_[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#the-first-parameter-of-axes-grid-and-axis-grid-has-been-renamed-to-visible "Link to this heading")

The parameter was previously named _b_. This name change only matters if that parameter was passed using a keyword argument, e.g. `grid(b=False)`.

### Removal of deprecations in the Selector widget API[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#removal-of-deprecations-in-the-selector-widget-api "Link to this heading")

#### RectangleSelector and EllipseSelector[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#rectangleselector-and-ellipseselector "Link to this heading")

The _drawtype_ keyword argument to [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 is removed. From now on, the only behaviour will be `drawtype='box'`.

Support for `drawtype=line` is removed altogether. As a result, the _lineprops_ keyword argument to [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 is also removed.

To retain the behaviour of `drawtype='none'`, use `rectprops={'visible': False}` to make the drawn [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 invisible.

Cleaned up attributes and arguments are:

*   The `active_handle` attribute has been privatized and removed.
    
*   The `drawtype` attribute has been privatized and removed.
    
*   The `eventpress` attribute has been privatized and removed.
    
*   The `eventrelease` attribute has been privatized and removed.
    
*   The `interactive` attribute has been privatized and removed.
    
*   The _marker\_props_ argument is removed, use _handle\_props_ instead.
    
*   The _maxdist_ argument is removed, use _grab\_range_ instead.
    
*   The _rectprops_ argument is removed, use _props_ instead.
    
*   The `rectprops` attribute has been privatized and removed.
    
*   The `state` attribute has been privatized and removed.
    
*   The `to_draw` attribute has been privatized and removed.
    

#### PolygonSelector[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#polygonselector "Link to this heading")

*   The _line_ attribute is removed. If you want to change the selector artist properties, use the `set_props` or `set_handle_props` methods.
    
*   The _lineprops_ argument is removed, use _props_ instead.
    
*   The _markerprops_ argument is removed, use _handle\_props_ instead.
    
*   The _maxdist_ argument and attribute is removed, use _grab\_range_ instead.
    
*   The _vertex\_select\_radius_ argument and attribute is removed, use _grab\_range_ instead.
    

#### SpanSelector[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#spanselector "Link to this heading")

*   The `active_handle` attribute has been privatized and removed.
    
*   The `eventpress` attribute has been privatized and removed.
    
*   The `eventrelease` attribute has been privatized and removed.
    
*   The `pressv` attribute has been privatized and removed.
    
*   The `prev` attribute has been privatized and removed.
    
*   The `rect` attribute has been privatized and removed.
    
*   The _rectprops_ parameter has been renamed to _props_.
    
*   The `rectprops` attribute has been privatized and removed.
    
*   The _span\_stays_ parameter has been renamed to _interactive_.
    
*   The `span_stays` attribute has been privatized and removed.
    
*   The `state` attribute has been privatized and removed.
    

#### LassoSelector[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#lassoselector "Link to this heading")

*   The _lineprops_ argument is removed, use _props_ instead.
    
*   The `onpress` and `onrelease` methods are removed. They are straight aliases for `press` and `release`.
    
*   The `matplotlib.widgets.TextBox.DIST_FROM_LEFT` attribute has been removed. It was marked as private in 3.5.
    

### `backend_template.show`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#backend-template-show "Link to this heading")

... has been removed, in order to better demonstrate the new backend definition API.

### Unused positional parameters to `print_<fmt>` methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#unused-positional-parameters-to-print-fmt-methods "Link to this heading")

None of the `print_<fmt>` methods implemented by canvas subclasses used positional arguments other that the first (the output filename or file-like), so these extra parameters are removed.

### `QuadMesh` signature[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#quadmesh-signature "Link to this heading")

The [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 signature

def \_\_init\_\_(meshWidth, meshHeight, coordinates,
             antialiased\=True, shading\='flat', \*\*kwargs)

is removed and replaced by the new signature

def \_\_init\_\_(coordinates, \*, antialiased\=True, shading\='flat', \*\*kwargs)

In particular:

*   The _coordinates_ argument must now be a (M, N, 2) array-like. Previously, the grid shape was separately specified as (_meshHeight_ + 1, _meshWidth_ + 1) and _coordinates_ could be an array-like of any shape with M \* N \* 2 elements.
    
*   All parameters except _coordinates_ are keyword-only now.
    

### Expiration of `FancyBboxPatch` deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#expiration-of-fancybboxpatch-deprecations "Link to this heading")

The [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 constructor no longer accepts the _bbox\_transmuter_ parameter, nor can the _boxstyle_ parameter be set to "custom" -- instead, directly set _boxstyle_ to the relevant boxstyle instance. The _mutation\_scale_ and _mutation\_aspect_ parameters have also become keyword-only.

The _mutation\_aspect_ parameter is now handled internally and no longer passed to the boxstyle callables when mutating the patch path.

### Testing support[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#testing-support "Link to this heading")

#### `matplotlib.test()` has been removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#matplotlib-test-has-been-removed "Link to this heading")

Run tests using `pytest` from the commandline instead. The variable `matplotlib.default_test_modules` was only used for `matplotlib.test()` and is thus removed as well.

To test an installed copy, be sure to specify both `matplotlib` and `mpl_toolkits` with `--pyargs`:

pytest \--pyargs matplotlib.tests mpl\_toolkits.tests

See [Testing](https://matplotlib.org/stable/devel/testing.html#testing)
 for more details.

### Auto-removal of grids by [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 and [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#auto-removal-of-grids-by-pcolor-and-pcolormesh "Link to this heading")

[`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 and [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 previously remove any visible axes major grid. This behavior is removed; please explicitly call `ax.grid(False)` to remove the grid.

### Modification of `Axes` children sublists[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#modification-of-axes-children-sublists "Link to this heading")

See [Axes children are no longer separated by type](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#behavioural-api-changes-3-5-axes-children-combined)
 for more information; modification of the following sublists is no longer supported:

*   `Axes.artists`
    
*   `Axes.collections`
    
*   `Axes.images`
    
*   `Axes.lines`
    
*   `Axes.patches`
    
*   `Axes.tables`
    
*   `Axes.texts`
    

To remove an Artist, use its [`Artist.remove`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove.html#matplotlib.artist.Artist.remove "matplotlib.artist.Artist.remove")
 method. To add an Artist, use the corresponding `Axes.add_*` method.

### Passing incorrect types to `Axes.add_*` methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#passing-incorrect-types-to-axes-add-methods "Link to this heading")

The following `Axes.add_*` methods will now raise if passed an unexpected type. See their documentation for the types they expect.

*   [`Axes.add_collection`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
    
*   [`Axes.add_image`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image")
    
*   [`Axes.add_line`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line "matplotlib.axes.Axes.add_line")
    
*   [`Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    
*   [`Axes.add_table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_table.html#matplotlib.axes.Axes.add_table "matplotlib.axes.Axes.add_table")
    

### `ConversionInterface.convert` no longer accepts unitless values[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#conversioninterface-convert-no-longer-accepts-unitless-values "Link to this heading")

Previously, custom subclasses of [`units.ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
 needed to implement a `convert` method that not only accepted instances of the unit, but also unitless values (which are passed through as is). This is no longer the case (`convert` is never called with a unitless value), and such support in `.StrCategoryConverter` is removed. Likewise, the `.ConversionInterface.is_numlike` helper is removed.

Consider calling [`Axis.convert_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.convert_units.html#matplotlib.axis.Axis.convert_units "matplotlib.axis.Axis.convert_units")
 instead, which still supports unitless values.

### Normal list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 objects now returned by [`HandlerLine2D.create_artists`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2D.create_artists "matplotlib.legend_handler.HandlerLine2D.create_artists")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#normal-list-of-artist-objects-now-returned-by-handlerline2d-create-artists "Link to this heading")

For Matplotlib 3.5 and 3.6 a proxy list was returned that simulated the return of [`HandlerLine2DCompound.create_artists`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2DCompound.create_artists "matplotlib.legend_handler.HandlerLine2DCompound.create_artists")
. Now a list containing only the single artist is return.

### rcParams will no longer cast inputs to str[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#rcparams-will-no-longer-cast-inputs-to-str "Link to this heading")

rcParams that expect a (non-pathlike) str no longer cast non-str inputs using [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
. This will avoid confusing errors in subsequent code if e.g. a list input gets implicitly cast to a str.

### Case-insensitive scales[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#case-insensitive-scales "Link to this heading")

Previously, scales could be set case-insensitively (e.g., `set_xscale("LoG")`). Now all builtin scales use lowercase names.

### Support for `nx1 = None` or `ny1 = None` in `AxesLocator` and `Divider.locate`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#support-for-nx1-none-or-ny1-none-in-axeslocator-and-divider-locate "Link to this heading")

In [`axes_grid1.axes_divider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.html#module-mpl_toolkits.axes_grid1.axes_divider "mpl_toolkits.axes_grid1.axes_divider")
, various internal APIs no longer supports passing `nx1 = None` or `ny1 = None` to mean `nx + 1` or `ny + 1`, in preparation for a possible future API which allows indexing and slicing of dividers (possibly `divider[a:b] == divider.new_locator(a, b)`, but also `divider[a:] == divider.new_locator(a, <end>)`). The user-facing [`Divider.new_locator`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator")
 API is unaffected -- it correctly normalizes `nx1 = None` and `ny1 = None` as needed.

### change signature of `.FigureCanvasBase.enter_notify_event`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#change-signature-of-figurecanvasbase-enter-notify-event "Link to this heading")

The _xy_ parameter is now required and keyword only. This was deprecated in 3.0 and originally slated to be removed in 3.5.

### `Colorbar` tick update parameters[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#colorbar-tick-update-parameters "Link to this heading")

The _update\_ticks_ parameter of [`Colorbar.set_ticks`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticks "matplotlib.colorbar.Colorbar.set_ticks")
 and [`Colorbar.set_ticklabels`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticklabels "matplotlib.colorbar.Colorbar.set_ticklabels")
 was ignored since 3.5 and has been removed.

### plot directive removals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#plot-directive-removals "Link to this heading")

The public methods:

*   `matplotlib.sphinxext.split_code_at_show`
    
*   `matplotlib.sphinxext.unescape_doctest`
    
*   `matplotlib.sphinxext.run_code`
    

have been removed.

The deprecated _encoding_ option to the plot directive has been removed.

### Miscellaneous removals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#miscellaneous-removals "Link to this heading")

*   `is_url` and `URL_REGEX` are removed. (They were previously defined in the toplevel [`matplotlib`](https://matplotlib.org/stable/index.html#module-matplotlib "matplotlib")
     module.)
    
*   The `ArrowStyle.beginarrow` and `ArrowStyle.endarrow` attributes are removed; use the `arrow` attribute to define the desired heads and tails of the arrow.
    
*   `backend_pgf.LatexManager.str_cache` is removed.
    
*   `backends.qt_compat.ETS` and `backends.qt_compat.QT_RC_MAJOR_VERSION` are removed, with no replacement.
    
*   The `blocking_input` module is removed. Instead, use `canvas.start_event_loop()` and `canvas.stop_event_loop()` while connecting event callbacks as needed.
    
*   `cbook.report_memory` is removed; use `psutil.virtual_memory` instead.
    
*   `cm.LUTSIZE` is removed. Use `[rcParams["image.lut"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.lut#rcparam-image-lut) ` (default: `256`) instead. This value only affects colormap quantization levels for default colormaps generated at module import time.
    
*   `Colorbar.patch` is removed; this attribute was not correctly updated anymore.
    
*   `ContourLabeler.get_label_width` is removed.
    
*   `Dvi.baseline` is removed (with no replacement).
    
*   The _format_ parameter of `dviread.find_tex_file` is removed (with no replacement).
    
*   `FancyArrowPatch.get_path_in_displaycoord` and `ConnectionPatch.get_path_in_displaycoord` are removed. The path in display coordinates can still be obtained, as for other patches, using `patch.get_transform().transform_path(patch.get_path())`.
    
*   The `font_manager.win32InstalledFonts` and `font_manager.get_fontconfig_fonts` helper functions are removed.
    
*   All parameters of `imshow` starting from _aspect_ are keyword-only.
    
*   `QuadMesh.convert_mesh_to_paths` and `QuadMesh.convert_mesh_to_triangles` are removed. `QuadMesh.get_paths()` can be used as an alternative for the former; there is no replacement for the latter.
    
*   `ScalarMappable.callbacksSM` is removed. Use `ScalarMappable.callbacks` instead.
    
*   `streamplot.get_integrator` is removed.
    
*   `style.core.STYLE_FILE_PATTERN`, `style.core.load_base_library`, and `style.core.iter_user_libraries` are removed.
    
*   `SubplotParams.validate` is removed. Use [`SubplotParams.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams.update "matplotlib.gridspec.SubplotParams.update")
     to change [`SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")
     while always keeping it in a valid state.
    
*   The `grey_arrayd`, `font_family`, `font_families`, and `font_info` attributes of [`TexManager`](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager "matplotlib.texmanager.TexManager")
     are removed.
    
*   `Text.get_prop_tup` is removed with no replacements (because the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
     class cannot know whether a backend needs to update cache e.g. when the text's color changes).
    
*   `Tick.apply_tickdir` didn't actually update the tick markers on the existing Line2D objects used to draw the ticks and is removed; use [`Axis.set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
     instead.
    
*   `tight_layout.auto_adjust_subplotpars` is removed.
    
*   The `grid_info` attribute of `axisartist` classes has been removed.
    
*   `axes_grid1.axes_grid.CbarAxes` and `axisartist.axes_grid.CbarAxes` are removed (they are now dynamically generated based on the owning axes class).
    
*   The `axes_grid1.Divider.get_vsize_hsize` and `axes_grid1.Grid.get_vsize_hsize` methods are removed.
    
*   `AxesDivider.append_axes(..., add_to_figure=False)` is removed. Use `ax.remove()` to remove the Axes from the figure if needed.
    
*   `FixedAxisArtistHelper.change_tick_coord` is removed with no replacement.
    
*   `floating_axes.GridHelperCurveLinear.get_boundary` is removed with no replacement.
    
*   `ParasiteAxesBase.get_images_artists` is removed.
    
*   The "units finalize" signal (previously emitted by Axis instances) is removed. Connect to "units" instead.
    
*   Passing formatting parameters positionally to `stem()` is no longer possible.
    
*   `axisartist.clip_path` is removed with no replacement.
    

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#id4)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#development-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows wheel runtime bundling[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#windows-wheel-runtime-bundling "Link to this heading")

Wheels built for Windows now bundle the MSVC runtime DLL `msvcp140.dll`. This enables importing Matplotlib on systems that do not have the runtime installed.

### Increase to minimum supported versions of dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#increase-to-minimum-supported-versions-of-dependencies "Link to this heading")

For Matplotlib 3.7, the [minimum supported versions](https://matplotlib.org/stable/install/dependencies.html#dependencies)
 are being bumped:

| Dependency | min in mpl3.6 | min in mpl3.7 |
| --- | --- | --- |
| NumPy | 1.19 | 1.20 |
| pyparsing | 2.2.1 | 2.3.1 |
| Qt  |     | 5.10 |

*   There are no wheels or conda packages that support both Qt 5.9 (or older) and Python 3.8 (or newer).
    

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)
 and [NEP29](https://numpy.org/neps/nep-0029-deprecation_policy.html)

### New dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#new-dependencies "Link to this heading")

*   [importlib-resources](https://pypi.org/project/importlib-resources/)
     (>= 3.2.0; only required on Python < 3.10)
    

### Maximum line length increased to 88 characters[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.7.0.html#maximum-line-length-increased-to-88-characters "Link to this heading")

The maximum line length for new contributions has been extended from 79 characters to 88 characters. This change provides an extra 9 characters to allow code which is a single idea to fit on fewer lines (often a single line). The chosen length is the same as [black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length)
.

On this page
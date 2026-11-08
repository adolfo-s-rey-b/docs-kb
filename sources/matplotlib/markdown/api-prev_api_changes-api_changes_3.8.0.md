[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#main-content)

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
    

API Changes for 3.8.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#api-changes-for-3-8-0 "Link to this heading")

=================================================================================================================================================

[Behaviour Changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#id2)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#behaviour-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Tk backend respects file format selection when saving figures[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#tk-backend-respects-file-format-selection-when-saving-figures "Link to this heading")

When saving a figure from a Tkinter GUI to a filename without an extension, the file format is now selected based on the value of the dropdown menu, rather than defaulting to PNG. When the filename contains an extension, or the OS automatically appends one, the behavior remains unchanged.

### Placing of maximum and minimum minor ticks[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#placing-of-maximum-and-minimum-minor-ticks "Link to this heading")

Calculation of minor tick locations has been corrected to make the maximum and minimum minor ticks more consistent. In some cases this results in an extra minor tick on an Axis.

### `hexbin` now defaults to `rcParams["patch.linewidth"]`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#hexbin-now-defaults-to-rcparams-patch-linewidth "Link to this heading")

The default value of the _linewidths_ argument of [`Axes.hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
 has been changed from `1.0` to `[rcParams["patch.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=patch.linewidth#rcparam-patch-linewidth) ` (default: `1.0`). This improves the consistency with [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 in [`Axes.pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 and [`Axes.hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")
.

### TwoSlopeNorm now auto-expands to always have two slopes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#twoslopenorm-now-auto-expands-to-always-have-two-slopes "Link to this heading")

In the case where either `vmin` or `vmax` are not manually specified to [`TwoSlopeNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm "matplotlib.colors.TwoSlopeNorm")
, and where the data it is scaling is all less than or greater than the center point, the limits are now auto-expanded so there are two symmetrically sized slopes either side of the center point.

Previously `vmin` and `vmax` were clipped at the center point, which caused issues when displaying color bars.

This does not affect behaviour when `vmin` and `vmax` are manually specified by the user.

### Event objects emitted for `axes_leave_event`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#event-objects-emitted-for-axes-leave-event "Link to this heading")

`axes_leave_event` now emits a synthetic [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent")
, instead of reusing the last event object associated with a `motion_notify_event`.

### Streamplot now draws streamlines as one piece if no width or no color variance[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#streamplot-now-draws-streamlines-as-one-piece-if-no-width-or-no-color-variance "Link to this heading")

Since there is no need to draw streamlines piece by piece if there is no color change or width change, now streamplot will draw each streamline in one piece.

The behavior for varying width or varying color is not changed, same logic is used for these kinds of streamplots.

### `canvas` argument now required for `FigureFrameWx`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#canvas-argument-now-required-for-figureframewx "Link to this heading")

`FigureFrameWx` now requires a keyword-only `canvas` argument when it is constructed.

### `ContourSet` is now a single Collection[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#contourset-is-now-a-single-collection "Link to this heading")

Prior to this release, [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 (the object returned by [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
) was a custom object holding multiple [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
s (and not an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
) -- one collection per level, each connected component of that level's contour being an entry in the corresponding collection.

[`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 is now instead a plain [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 (and thus an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
). The collection contains a single path per contour level; this path may be non-continuous in case there are multiple connected components.

Setting properties on the ContourSet can now usually be done using standard collection setters (`cset.set_linewidth(3)` to use the same linewidth everywhere or `cset.set_linewidth([1, 2, 3, ...])` to set different linewidths on each level) instead of having to go through the individual sub-components (`cset.collections[0].set_linewidth(...)`). Note that during the transition period, it remains possible to access the (deprecated) `.collections` attribute; this causes the ContourSet to modify itself to use the old-style multi-Collection representation.

### `SubFigure` default facecolor is now transparent[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#subfigure-default-facecolor-is-now-transparent "Link to this heading")

Subfigures default facecolor changed to `"none"`. Previously the default was the value of `figure.facecolor`.

### Reject size related keyword arguments to MovieWriter _grab\_frame_ method[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#reject-size-related-keyword-arguments-to-moviewriter-grab-frame-method "Link to this heading")

Although we pass [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 keyword arguments through the [`AbstractMovieWriter.grab_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter.grab_frame "matplotlib.animation.AbstractMovieWriter.grab_frame")
 some of the arguments will result in invalid output if passed. To be successfully stitched into a movie, each frame must be exactly the same size, thus _bbox\_inches_ and _dpi_ are excluded. Additionally, the movie writers are opinionated about the format of each frame, so the _format_ argument is also excluded. Passing these arguments will now raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 for all writers (it already did so for some arguments and some writers). The _bbox\_inches_ argument is already ignored (with a warning) if passed to [`Animation.save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
.

Additionally, if `[rcParams["savefig.bbox"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.bbox#rcparam-savefig-bbox) ` (default: `None`) is set to `'tight'`, [`AbstractMovieWriter.grab_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter.grab_frame "matplotlib.animation.AbstractMovieWriter.grab_frame")
 will now error. Previously this rcParam would be temporarily overridden (with a warning) in [`Animation.save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
, it is now additionally overridden in [`AbstractMovieWriter.saving`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter.saving "matplotlib.animation.AbstractMovieWriter.saving")
.

### Changes of API after deprecation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#changes-of-api-after-deprecation "Link to this heading")

*   [`dviread.find_tex_file`](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.find_tex_file "matplotlib.dviread.find_tex_file")
     now raises [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "(in Python v3.14)")
     when the requested filename is not found.
    
*   [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     now raises if _cax_ is not given and it is unable to determine from which Axes to steal space, i.e. if _ax_ is also not given and _mappable_ has not been added to an Axes.
    
*   [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
     and [`pyplot.subplot2grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
     no longer auto-remove preexisting overlapping Axes; explicitly call `Axes.remove` as needed.
    

### Invalid types for Annotation xycoords now raise TypeError[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#invalid-types-for-annotation-xycoords-now-raise-typeerror "Link to this heading")

Previously, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)")
 would be raised in some cases.

### Default antialiasing behavior changes for `Text` and `Annotation`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#default-antialiasing-behavior-changes-for-text-and-annotation "Link to this heading")

`matplotlib.pyplot.annotate()` and `matplotlib.pyplot.text()` now support parameter _antialiased_ when initializing. Examples:

mpl.text.Text(.5, .5, "foo\\nbar", antialiased\=True)
plt.text(0.5, 0.5, '6 inches x 2 inches', antialiased\=True)
ax.annotate('local max', xy\=(2, 1), xytext\=(3, 1.5), antialiased\=False)

See "What's New" for more details on usage.

With this new feature, you may want to make sure that you are creating and saving/showing the figure under the same context:

\# previously this was a no-op, now it is what works
with rccontext(text.antialiased\=False):
    fig, ax \= plt.subplots()
    ax.annotate('local max', xy\=(2, 1), xytext\=(3, 1.5))
    fig.savefig('/tmp/test.png')

\# previously this had an effect, now this is a no-op
fig, ax \= plt.subplots()
ax.annotate('local max', xy\=(2, 1), xytext\=(3, 1.5))
with rccontext(text.antialiased\=False):
    fig.savefig('/tmp/test.png')

Also note that antialiasing for tick labels will be set with `[rcParams["text.antialiased"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.antialiased#rcparam-text-antialiased) ` (default: `True`) when they are created (usually when a `Figure` is created) - This means antialiasing for them can no longer be changed by modifying `[rcParams["text.antialiased"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.antialiased#rcparam-text-antialiased) ` (default: `True`).

### `ScalarMappable.to_rgba()` now respects the mask of RGB(A) arrays[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#scalarmappable-to-rgba-now-respects-the-mask-of-rgb-a-arrays "Link to this heading")

Previously, the mask was ignored. Now the alpha channel is set to 0 if any component (R, G, B, or A) is masked.

### `Text.get_rotation_mode` return value[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#text-get-rotation-mode-return-value "Link to this heading")

Passing `None` as `rotation_mode` to [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 (the default value) or passing it to [`Text.set_rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode")
 will make [`Text.get_rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_rotation_mode "matplotlib.text.Text.get_rotation_mode")
 return `"default"` instead of `None`. The behaviour otherwise is the same.

### PostScript paper size adds option to use figure size[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#postscript-paper-size-adds-option-to-use-figure-size "Link to this heading")

The `[rcParams["ps.papersize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ps.papersize#rcparam-ps-papersize) ` (default: `'letter'`) rcParam can now be set to `'figure'`, which will use a paper size that corresponds exactly with the size of the figure that is being saved.

### `hexbin` _mincnt_ parameter made consistently inclusive[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#hexbin-mincnt-parameter-made-consistently-inclusive "Link to this heading")

Previously, _mincnt_ was inclusive with no _C_ provided but exclusive when _C_ is provided. It is now inclusive of _mincnt_ in both cases.

[`matplotlib.mpl_toolkits` is now an implicit namespace package](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#id3)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#matplotlib-mpl-toolkits-is-now-an-implicit-namespace-package "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Following the deprecation of `pkg_resources.declare_namespace` in `setuptools` 67.3.0, `matplotlib.mpl_toolkits` is now implemented as an implicit namespace, following [PEP 420](https://peps.python.org/pep-0420/)
.

As a consequence using `pip` to install a version of Matplotlib >= 3.8 on top of a version of Matplotlib < 3.8 (e.g. via `pip install --local` or `python -m venv --system-site-packages ...`) will fail because the old `matplotlib.mpl_toolkits` files will be found whereas the newer files will be found for all other modules. This will result in errors due to the version mismatch.

To avoid this issue you need to avoid having multiple versions of Matplotlib in different entries of `sys.path`. Either uninstall Matplotlib at the system level or use a more isolated virtual environment.

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#id4)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Calling `paths.get_path_collection_extents` with empty _offsets_[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#calling-paths-get-path-collection-extents-with-empty-offsets "Link to this heading")

Calling [`get_path_collection_extents`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.get_path_collection_extents "matplotlib.path.get_path_collection_extents")
 with an empty _offsets_ parameter has an ambiguous interpretation and is therefore deprecated. When the deprecation period expires, this will produce an error.

### `axes_grid1.axes_divider` API changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#axes-grid1-axes-divider-api-changes "Link to this heading")

The `AxesLocator` class is deprecated. The `new_locator` method of divider instances now instead returns an opaque callable (which can still be passed to `ax.set_axes_locator`).

`Divider.locate` is deprecated; use `Divider.new_locator(...)(ax, renderer)` instead.

### `bbox.anchored()` with no explicit container[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#bbox-anchored-with-no-explicit-container "Link to this heading")

Not passing a _container_ argument to [`BboxBase.anchored`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.anchored "matplotlib.transforms.BboxBase.anchored")
 is now deprecated.

### Functions in `mpl_toolkits.mplot3d.proj3d`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#functions-in-mpl-toolkits-mplot3d-proj3d "Link to this heading")

The function `transform` is just an alias for `proj_transform`, use the latter instead.

The following functions are either unused (so no longer required in Matplotlib) or considered private. If you rely on them, please make a copy of the code, including all functions that starts with a `_` (considered private).

*   `ortho_transformation`
    
*   `persp_transformation`
    
*   `proj_points`
    
*   `proj_trans_points`
    
*   `rot_x`
    
*   `rotation_about_vector`
    
*   `view_transformation`
    

### Arguments other than `renderer` to `get_tightbbox`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#arguments-other-than-renderer-to-get-tightbbox "Link to this heading")

... are keyword-only arguments. This is for consistency and that different classes have different additional arguments.

### The object returned by `pcolor()` has changed to a `PolyQuadMesh` class[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#the-object-returned-by-pcolor-has-changed-to-a-polyquadmesh-class "Link to this heading")

The old object was a [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 with flattened vertices and array data. The new [`PolyQuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyQuadMesh "matplotlib.collections.PolyQuadMesh")
 class subclasses [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
, but adds in better 2D coordinate and array handling in alignment with [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
. Previously, if a masked array was input, the list of polygons within the collection would shrink to the size of valid polygons and users were required to keep track of which polygons were drawn and call `set_array()` with the smaller "compressed" array size. Passing the "compressed" and flattened array values is now deprecated and the full 2D array of values (including the mask) should be passed to [`PolyQuadMesh.set_array`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyQuadMesh.set_array "matplotlib.collections.PolyQuadMesh.set_array")
.

### `LocationEvent.lastevent`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#locationevent-lastevent "Link to this heading")

... is deprecated with no replacement.

### `allsegs`, `allkinds`, `tcolors` and `tlinewidths` attributes of [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#allsegs-allkinds-tcolors-and-tlinewidths-attributes-of-contourset "Link to this heading")

These attributes are deprecated; if required, directly retrieve the vertices and codes of the Path objects from `ContourSet.get_paths()` and the colors and the linewidths via `ContourSet.get_facecolor()`, `ContourSet.get_edgecolor()` and `ContourSet.get_linewidths()`.

### `ContourSet.collections`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#contourset-collections "Link to this heading")

... is deprecated. [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 is now implemented as a single [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 of paths, each path corresponding to a contour level, possibly including multiple unconnected components.

During the deprecation period, accessing `ContourSet.collections` will revert the current ContourSet instance to the old object layout, with a separate [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 per contour level.

### `INVALID_NON_AFFINE`, `INVALID_AFFINE`, `INVALID` attributes of `TransformNode`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#invalid-non-affine-invalid-affine-invalid-attributes-of-transformnode "Link to this heading")

These attributes are deprecated.

### `Grouper.clean()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#grouper-clean "Link to this heading")

with no replacement. The Grouper class now cleans itself up automatically.

### `GridHelperCurveLinear.get_data_boundary`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#gridhelpercurvelinear-get-data-boundary "Link to this heading")

... is deprecated. Use `grid_finder.extreme_finder(*[None] * 5)` to get the extremes of the grid.

### _np\_load_ parameter of `cbook.get_sample_data`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#np-load-parameter-of-cbook-get-sample-data "Link to this heading")

This parameter is deprecated; [`get_sample_data`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
 now auto-loads numpy arrays. Use `get_sample_data(..., asfileobj=False)` instead to get the filename of the data file, which can then be passed to [`open`](https://docs.python.org/3/library/functions.html#open "(in Python v3.14)")
, if desired.

### `RendererAgg.tostring_rgb` and `FigureCanvasAgg.tostring_rgb`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#rendereragg-tostring-rgb-and-figurecanvasagg-tostring-rgb "Link to this heading")

... are deprecated with no direct replacement. Consider using `buffer_rgba` instead, which should cover most use cases.

### The parameter of `Annotation.contains` and `Legend.contains` is renamed to _mouseevent_[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#the-parameter-of-annotation-contains-and-legend-contains-is-renamed-to-mouseevent "Link to this heading")

... consistently with [`Artist.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib.artist.Artist.contains "matplotlib.artist.Artist.contains")
.

### Accessing `event.guiEvent` after event handlers return[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#accessing-event-guievent-after-event-handlers-return "Link to this heading")

... is deprecated: for some GUI toolkits, it is unsafe to do so. In the future, `event.guiEvent` will be set to None once the event handlers return; you may separately stash the object at your own risk.

### Widgets[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#widgets "Link to this heading")

The _visible_ attribute getter of Selector widgets has been deprecated; use `get_visible`

### Method parameters renamed to match base classes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#method-parameters-renamed-to-match-base-classes "Link to this heading")

The only parameter of `transform_affine` and `transform_non_affine` in `Transform` subclasses is renamed to _values_.

The _points_ parameter of `transforms.IdentityTransform.transform` is renamed to _values_.

The _trans_ parameter of `table.Cell.set_transform` is renamed to _t_ consistently with [`Artist.set_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform")
.

The _clippath_ parameters of `axis.Axis.set_clip_path` and `axis.Tick.set_clip_path` are renamed to _path_ consistently with [`Artist.set_clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path")
.

The _s_ parameter of `images.NonUniformImage.set_filternorm` is renamed to _filternorm_ consistently with `_ImageBase.set_filternorm`.

The _s_ parameter of `images.NonUniformImage.set_filterrad` is renamed to _filterrad_ consistently with `_ImageBase.set_filterrad`.

### _numdecs_ parameter and attribute of `LogLocator`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#numdecs-parameter-and-attribute-of-loglocator "Link to this heading")

... are deprecated without replacement, because they have no effect.

### `NavigationToolbar2QT.message` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#navigationtoolbar2qt-message-is-deprecated "Link to this heading")

... with no replacement.

### `ft2font.FT2Image.draw_rect` and `ft2font.FT2Font.get_xys`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#ft2font-ft2image-draw-rect-and-ft2font-ft2font-get-xys "Link to this heading")

... are deprecated as they are unused. If you rely on these, please let us know.

### `backend_ps.psDefs`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#backend-ps-psdefs "Link to this heading")

The `psDefs` module-level variable in `backend_ps` is deprecated with no replacement.

### Callable axisartist Axes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#callable-axisartist-axes "Link to this heading")

Calling an axisartist Axes to mean [`axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
 is deprecated; explicitly call the method instead.

### `AnchoredEllipse` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#anchoredellipse-is-deprecated "Link to this heading")

Instead, directly construct an [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
, an [`AuxTransformBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
, and an [`Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
, as demonstrated in [Anchored Artists](https://matplotlib.org/stable/gallery/misc/anchored_artists.html)
.

### Automatic papersize selection in PostScript[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#automatic-papersize-selection-in-postscript "Link to this heading")

Setting `[rcParams["ps.papersize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ps.papersize#rcparam-ps-papersize) ` (default: `'letter'`) to `'auto'` or passing `papersize='auto'` to [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 is deprecated. Either pass an explicit paper type name, or omit this parameter to use the default from the rcParam.

### `Tick.set_label1` and `Tick.set_label2`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#tick-set-label1-and-tick-set-label2 "Link to this heading")

... are deprecated. Calling these methods from third-party code usually has no effect, as the labels are overwritten at draw time by the tick formatter.

### Passing extra positional arguments to `Figure.add_axes`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#passing-extra-positional-arguments-to-figure-add-axes "Link to this heading")

Positional arguments passed to [`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
 other than a rect or an existing `Axes` are currently ignored, and doing so is now deprecated.

### `CbarAxesBase.toggle_label`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#cbaraxesbase-toggle-label "Link to this heading")

... is deprecated. Instead, use standard methods for manipulating colorbar labels ([`Colorbar.set_label`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_label "matplotlib.colorbar.Colorbar.set_label")
) and tick labels ([`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
).

### `TexManager.texcache`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#texmanager-texcache "Link to this heading")

... is considered private and deprecated. The location of the cache directory is clarified in the doc-string.

### Artists explicitly passed in will no longer be filtered by legend() based on their label[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#artists-explicitly-passed-in-will-no-longer-be-filtered-by-legend-based-on-their-label "Link to this heading")

Currently, artists explicitly passed to `legend(handles=[...])` are filtered out if their label starts with an underscore. This behavior is deprecated; explicitly filter out such artists (`[art for art in artists if not art.get_label().startswith('_')]`) if necessary.

### `FigureCanvasBase.switch_backends`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#figurecanvasbase-switch-backends "Link to this heading")

... is deprecated with no replacement.

### `cbook.Stack` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#cbook-stack-is-deprecated "Link to this heading")

... with no replacement.

### `inset_location.InsetPosition` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#inset-location-insetposition-is-deprecated "Link to this heading")

Use [`inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
 instead.

### `axisartist.axes_grid` and `axisartist.axes_rgb`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#axisartist-axes-grid-and-axisartist-axes-rgb "Link to this heading")

These modules, which provide wrappers combining the functionality of [`axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
 and [`axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
, are deprecated; directly use e.g. `AxesGrid(..., axes_class=axislines.Axes)` instead.

### `ContourSet.antialiased`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#contourset-antialiased "Link to this heading")

... is deprecated; use [`get_antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_antialiased "matplotlib.collections.Collection.get_antialiased")
 or [`set_antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")
 instead. Note that [`get_antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_antialiased "matplotlib.collections.Collection.get_antialiased")
 returns an array.

### Passing non-int or sequence of non-int to `Table.auto_set_column_width`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#passing-non-int-or-sequence-of-non-int-to-table-auto-set-column-width "Link to this heading")

Column numbers are ints, and formerly passing any other type was effectively ignored. This will become an error in the future.

### `PdfPages(keep_empty=True)`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#pdfpages-keep-empty-true "Link to this heading")

A zero-page pdf is not valid, thus passing `keep_empty=True` to [`backend_pdf.PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
 and [`backend_pgf.PdfPages`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages "matplotlib.backends.backend_pgf.PdfPages")
, and the `keep_empty` attribute of these classes, are deprecated. Currently, these classes default to keeping empty outputs, but that behavior is deprecated too. Explicitly passing `keep_empty=False` remains supported for now to help transition to the new behavior.

Furthermore, [`backend_pdf.PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
 no longer immediately creates the target file upon instantiation, but only when the first figure is saved. To fully control file creation, directly pass an opened file object as argument (`with open(path, "wb") as file, PdfPages(file) as pdf: ...`).

### Auto-closing of figures when switching backend[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#auto-closing-of-figures-when-switching-backend "Link to this heading")

... is deprecated. Explicitly call `plt.close("all")` if necessary. In the future, allowable backend switches (i.e. those that do not swap a GUI event loop with another one) will not close existing figures.

### Support for passing the "frac" key in `annotate(..., arrowprops={"frac": ...})`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#support-for-passing-the-frac-key-in-annotate-arrowprops-frac "Link to this heading")

... has been removed. This key has had no effect since Matplotlib 1.5.

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#id5)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### cbook removals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#cbook-removals "Link to this heading")

*   `matplotlib.cbook.MatplotlibDeprecationWarning` and `matplotlib.cbook.mplDeprecation` are removed; use [`matplotlib.MatplotlibDeprecationWarning`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.MatplotlibDeprecationWarning "matplotlib.MatplotlibDeprecationWarning")
     instead.
    
*   `cbook.maxdict`; use the standard library `functools.lru_cache` instead.
    

### Groupers from `get_shared_x_axes` / `get_shared_y_axes` are immutable[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#groupers-from-get-shared-x-axes-get-shared-y-axes-are-immutable "Link to this heading")

Modifications to the Groupers returned by `get_shared_x_axes` and `get_shared_y_axes` are no longer allowed. Note that previously, calling e.g. `join()` would already fail to set up the correct structures for sharing axes; use [`Axes.sharex`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharex.html#matplotlib.axes.Axes.sharex "matplotlib.axes.Axes.sharex")
 or [`Axes.sharey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharey.html#matplotlib.axes.Axes.sharey "matplotlib.axes.Axes.sharey")
 instead.

### Deprecated modules removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#deprecated-modules-removed "Link to this heading")

The following deprecated modules are removed:

*   `afm`
    
*   `docstring`
    
*   `fontconfig_pattern`
    
*   `tight_bbox`
    
*   `tight_layout`
    
*   `type1font`
    

### Parameters to `plt.figure()` and the `Figure` constructor[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#parameters-to-plt-figure-and-the-figure-constructor "Link to this heading")

All parameters to [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
 and the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 constructor, other than _num_, _figsize_, and _dpi_, are now keyword-only.

### `stem(..., use_line_collection=False)`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#stem-use-line-collection-false "Link to this heading")

... is no longer supported. This was a compatibility fallback to a former more inefficient representation of the stem lines.

### Positional / keyword arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#positional-keyword-arguments "Link to this heading")

Passing all but the very few first arguments positionally in the constructors of Artists is no longer possible. Most arguments are now keyword-only.

The _emit_ and _auto_ parameters of `set_xlim`, `set_ylim`, `set_zlim`, `set_rlim` are now keyword-only.

The _transOffset_ parameter of [`Collection.set_offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")
 and the various `create_collection` methods of legend handlers has been renamed to _offset\_transform_ (consistently with the property name).

`Axes.get_window_extent` / `Figure.get_window_extent` accept only _renderer_. This aligns the API with the general [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")
 API. All other parameters were ignored anyway.

### Methods to set parameters in `LogLocator` and `LogFormatter*`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#methods-to-set-parameters-in-loglocator-and-logformatter "Link to this heading")

In [`LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter")
 and derived subclasses, the methods `base` and `label_minor` for setting the respective parameter are removed and replaced by `set_base` and `set_label_minor`, respectively.

In [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
, the methods `base` and `subs` for setting the respective parameter are removed. Instead, use `set_params(base=..., subs=...)`.

### `Axes.get_renderer_cache`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#axes-get-renderer-cache "Link to this heading")

The canvas now takes care of the renderer and whether to cache it or not, so the `Axes.get_renderer_cache` method is removed. The alternative is to call `axes.figure.canvas.get_renderer()`.

### Unused methods in `Axis`, `Tick`, `XAxis`, and `YAxis`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#unused-methods-in-axis-tick-xaxis-and-yaxis "Link to this heading")

`Tick.label` is now removed. Use `Tick.label1` instead.

The following methods are no longer used and removed without a replacement:

*   `Axis.get_ticklabel_extents`
    
*   `Tick.get_pad_pixels`
    
*   `XAxis.get_text_heights`
    
*   `YAxis.get_text_widths`
    

### `mlab.stride_windows`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#mlab-stride-windows "Link to this heading")

... is removed. Use `numpy.lib.stride_tricks.sliding_window_view` instead.

### `Axes3D`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#axes3d "Link to this heading")

The `dist` attribute has been privatized. Use the _zoom_ keyword argument in [`Axes3D.set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect")
 instead.

The `w_xaxis`, `w_yaxis`, and `w_zaxis` attributes are now removed. Instead use `xaxis`, `yaxis`, and `zaxis`.

### 3D Axis[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#d-axis "Link to this heading")

`mplot3d.axis3d.Axis.set_pane_pos` is removed. This is an internal method where the provided values are overwritten during drawing. Hence, it does not serve any purpose to be directly accessible.

The two helper functions `mplot3d.axis3d.move_from_center` and `mplot3d.axis3d.tick_update_position` are considered internal and deprecated. If these are required, please vendor the code from the corresponding private methods `_move_from_center` and `_tick_update_position`.

### `checkdep_usetex` removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#checkdep-usetex-removed "Link to this heading")

This method was only intended to disable tests in case no latex install was found. As such, it is considered to be private and for internal use only.

Please vendor the code from a previous version if you need this.

### `date_ticker_factory` removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#date-ticker-factory-removed "Link to this heading")

The `date_ticker_factory` method in the [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 module is removed. Instead use [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
 and [`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
 for a more flexible and scalable locator and formatter.

If you need the exact `date_ticker_factory` behavior, please copy the code from a previous version.

### `transforms.Affine2D.identity()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#transforms-affine2d-identity "Link to this heading")

... is removed in favor of directly calling the [`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 constructor with no arguments.

### Removals in `testing.decorators`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#removals-in-testing-decorators "Link to this heading")

The unused class `CleanupTestCase` and decorator `cleanup` are removed. The function `check_freetype_version` is considered internal and removed. Vendor the code from a previous version.

### `text.get_rotation()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#text-get-rotation "Link to this heading")

... is removed with no replacement. Copy the previous implementation if needed. `Figure.callbacks` is removed ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Figure `callbacks` property has been removed. The only signal was "dpi\_changed", which can be replaced by connecting to the "resize\_event" on the canvas `figure.canvas.mpl_connect("resize_event", func)` instead.

### Passing too many positional arguments to `tripcolor`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#passing-too-many-positional-arguments-to-tripcolor "Link to this heading")

... raises `TypeError` (extra arguments were previously ignored).

### The _filled_ argument to `Colorbar` is removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#the-filled-argument-to-colorbar-is-removed "Link to this heading")

This behavior was already governed by the underlying `ScalarMappable`.

### Widgets[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#id1 "Link to this heading")

The _visible_ attribute setter of Selector widgets has been removed; use `set_visible` The associated getter is also deprecated, but not yet expired.

### `Axes3D.set_frame_on` and `Axes3D.get_frame_on` removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#axes3d-set-frame-on-and-axes3d-get-frame-on-removed "Link to this heading")

`Axes3D.set_frame_on` is documented as "Set whether the 3D axes panels are drawn.". However, it has no effect on 3D axes and is being removed in favor of `Axes3D.set_axis_on` and `Axes3D.set_axis_off`.

### Miscellaneous internals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#miscellaneous-internals "Link to this heading")

*   `axes_grid1.axes_size.AddList`; use `sum(sizes, start=Fixed(0))` (for example) to sum multiple size objects.
    
*   `axes_size.Padded`; use `size + pad` instead
    
*   `axes_size.SizeFromFunc`, `axes_size.GetExtentHelper`
    
*   `AxisArtistHelper.delta1` and `AxisArtistHelper.delta2`
    
*   `axislines.GridHelperBase.new_gridlines` and `axislines.Axes.new_gridlines`
    
*   `_DummyAxis.dataLim` and `_DummyAxis.viewLim`; use `get_data_interval()`, `set_data_interval()`, `get_view_interval()`, and `set_view_interval()` instead.
    
*   `ImageMagickBase.delay` and `ImageMagickBase.output_args`
    
*   `MathtextBackend`, `MathtextBackendAgg`, `MathtextBackendPath`, `MathTextWarning`
    
*   `TexManager.get_font_config`; it previously returned an internal hashed key for used for caching purposes.
    
*   `TextToPath.get_texmanager`; directly construct a [`texmanager.TexManager`](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager "matplotlib.texmanager.TexManager")
     instead.
    
*   `ticker.is_close_to_int`; use `math.isclose(x, round(x))` instead.
    
*   `ticker.is_decade`; use `y = numpy.log(x)/numpy.log(base); numpy.isclose(y, numpy.round(y))` instead.
    

### Backend-specific removals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#backend-specific-removals "Link to this heading")

*   `backend_pdf.Name.hexify`
    
*   `backend_pdf.Operator` and `backend_pdf.Op.op` are removed in favor of a single standard [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)")
     interface on [`backend_pdf.Op`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op "matplotlib.backends.backend_pdf.Op")
    .
    
*   `backend_pdf.fill`; vendor the code of the similarly named private functions if you rely on these functions.
    
*   `backend_pgf.LatexManager.texcommand` and `backend_pgf.LatexManager.latex_header`
    
*   `backend_pgf.NO_ESCAPE`
    
*   `backend_pgf.common_texification`
    
*   `backend_pgf.get_fontspec`
    
*   `backend_pgf.get_preamble`
    
*   `backend_pgf.re_mathsep`
    
*   `backend_pgf.writeln`
    
*   `backend_ps.convert_psfrags`
    
*   `backend_ps.quote_ps_string`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.escape_attrib`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.escape_cdata`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.escape_comment`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.short_float_fmt`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.generate_transform` and `backend_svg.generate_css`
    

### Removal of deprecated APIs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#removal-of-deprecated-apis "Link to this heading")

The following deprecated APIs have been removed. Unless a replacement is stated, please vendor the previous implementation if needed.

*   The following methods of [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
    : `pick` (use `Figure.pick` instead), `resize`, `draw_event`, `resize_event`, `close_event`, `key_press_event`, `key_release_event`, `pick_event`, `scroll_event`, `button_press_event`, `button_release_event`, `motion_notify_event`, `leave_notify_event`, `enter_notify_event` (for all the `foo_event` methods, construct the relevant [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
     object and call `canvas.callbacks.process(event.name, event)` instead).
    
*   `ToolBase.destroy` (connect to `tool_removed_event` instead).
    
*   The _cleared_ parameter to [`FigureCanvasAgg.get_renderer`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.get_renderer "matplotlib.backends.backend_agg.FigureCanvasAgg.get_renderer")
     (call `renderer.clear()` instead).
    
*   The following methods of [`RendererCairo`](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo "matplotlib.backends.backend_cairo.RendererCairo")
    : `set_ctx_from_surface` and `set_width_height` (use `set_context` instead, which automatically infers the canvas size).
    
*   The `window` or `win` parameters and/or attributes of `NavigationToolbar2Tk`, `NavigationToolbar2GTK3`, and `NavigationToolbar2GTK4`, and the `lastrect` attribute of `NavigationToolbar2Tk`
    
*   The `error_msg_gtk` function and the `icon_filename` and `window_icon` globals in `backend_gtk3`; the `error_msg_wx` function in `backend_wx`.
    
*   `FigureManagerGTK3Agg` and `FigureManagerGTK4Agg` (use `FigureManagerGTK3` instead); `RendererGTK3Cairo` and `RendererGTK4Cairo`.
    
*   `NavigationToolbar2Mac.prepare_configure_subplots` (use [`configure_subplots`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.configure_subplots "matplotlib.backend_bases.NavigationToolbar2.configure_subplots")
     instead).
    
*   `FigureManagerMac.close`.
    
*   The `qApp` global in [`backend_qt`](https://matplotlib.org/stable/api/backend_qt_api.html#module-matplotlib.backends.backend_qt "matplotlib.backends.backend_qt")
     (use `QtWidgets.QApplication.instance()` instead).
    
*   The `offset_text_height` method of `RendererWx`; the `sizer`, `figmgr`, `num`, `toolbar`, `toolmanager`, `get_canvas`, and `get_figure_manager` attributes or methods of `FigureFrameWx` (use `frame.GetSizer()`, `frame.canvas.manager`, `frame.canvas.manager.num`, `frame.GetToolBar()`, `frame.canvas.manager.toolmanager`, the _canvas\_class_ constructor parameter, and `frame.canvas.manager`, respectively, instead).
    
*   `FigureFrameWxAgg` and `FigureFrameWxCairo` (use `FigureFrameWx(..., canvas_class=FigureCanvasWxAgg)` and `FigureFrameWx(..., canvas_class=FigureCanvasWxCairo)`, respectively, instead).
    
*   The `filled` attribute and the `draw_all` method of [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
     (instead of `draw_all`, use `figure.draw_without_rendering`).
    
*   Calling [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
     without setting the _marker_ parameter or setting it to None (use `MarkerStyle("")` instead).
    
*   Support for third-party canvas classes without a `required_interactive_framework` attribute (this can only occur if the canvas class does not inherit from [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
    ).
    
*   The `canvas` and `background` attributes of [`MultiCursor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor "matplotlib.widgets.MultiCursor")
    ; the `state_modifier_keys` attribute of selector widgets.
    
*   Passing _useblit_, _horizOn_, or _vertOn_ positionally to [`MultiCursor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor "matplotlib.widgets.MultiCursor")
    .
    
*   Support for the `seaborn-<foo>` styles; use `seaborn-v0_8-<foo>` instead, or directly use the seaborn API.
    

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#id6)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#development-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Increase to minimum supported versions of dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#increase-to-minimum-supported-versions-of-dependencies "Link to this heading")

For Matplotlib 3.8, the [minimum supported versions](https://matplotlib.org/stable/install/dependencies.html#dependencies)
 are being bumped:

| Dependency | min in mpl3.7 | min in mpl3.8 |
| --- | --- | --- |
| Python | 3.8 | 3.9 |
| kiwisolver | 1.0.1 | 1.3.1 |
| NumPy | 1.20.0 | 1.21.0 |
| Pillow | 6.2.1 | 8.0 |

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)
 and [NEP29](https://numpy.org/neps/nep-0029-deprecation_policy.html)

### Increase to minimum supported optional dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#increase-to-minimum-supported-optional-dependencies "Link to this heading")

For Matplotlib 3.8, the [minimum supported versions of optional dependencies](https://matplotlib.org/stable/install/dependencies.html#optional-dependencies)
 are being bumped:

| Dependency | min in mpl3.7 | min in mpl3.8 |
| --- | --- | --- |
| Tk  | 8.4 | 8.5 |
| Qt  | 5.10 | 5.12 |

*   There are no wheels or conda packages that support both Qt 5.11 (or older) and Python 3.9 (or newer).
    

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)

### Provisional support for PEP484 Type Hint Annotations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#provisional-support-for-pep484-type-hint-annotations "Link to this heading")

New public API should be type hinted in `.pyi` stub files (except `pyplot` and tests which are typed in-line). Tests should be type hinted minimally, essentially only when `mypy` generates errors.

CI and configuration for running `mypy` have been added.

### Generation of `pyplot.py` requires `black`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#generation-of-pyplot-py-requires-black "Link to this heading")

The autogenerated portions of `pyplot.py` use `black` autoformatting to ensure syntax-correct, readable output code.

As such `black` is now a development and test requirement (for the test which regenerates `pyplot`).

### Wheels for some systems are no longer distributed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#wheels-for-some-systems-are-no-longer-distributed "Link to this heading")

Pre-compiled wheels for 32-bit Linux and Windows are no longer provided on PyPI since Matplotlib 3.8.

Multi-architecture `universal2` wheels for macOS are no longer provided on PyPI since Matplotlib 3.8. In general, `pip` will always prefer the architecture-specific (`amd64`\- or `arm64`\-only) wheels, so these provided little benefit.

### New wheel architectures[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.0.html#new-wheel-architectures "Link to this heading")

Wheels have been added for:

*   musl based systems
    

On this page
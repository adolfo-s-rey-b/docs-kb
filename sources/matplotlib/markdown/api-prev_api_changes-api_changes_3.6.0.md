[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#main-content)

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
    

API Changes for 3.6.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#api-changes-for-3-6-0 "Link to this heading")

=================================================================================================================================================

[Behaviour changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#id2)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#behaviour-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `plt.get_cmap` and `matplotlib.cm.get_cmap` return a copy[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#plt-get-cmap-and-matplotlib-cm-get-cmap-return-a-copy "Link to this heading")

Formerly, [`get_cmap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
 and `matplotlib.cm.get_cmap` returned a global version of a [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
. This was prone to errors as modification of the colormap would propagate from one location to another without warning. Now, a new copy of the colormap is returned.

### Large `imshow` images are now downsampled[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#large-imshow-images-are-now-downsampled "Link to this heading")

When showing an image using [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 that has more than \\(2^{24}\\) columns or \\(2^{23}\\) rows, the image will now be downsampled to below this resolution before being resampled for display by the AGG renderer. Previously such a large image would be shown incorrectly. To prevent this downsampling and the warning it raises, manually downsample your data before handing it to [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

### Default date limits changed to 1970-01-01 – 1970-01-02[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#default-date-limits-changed-to-1970-01-01-1970-01-02 "Link to this heading")

Previously the default limits for an empty axis set up for dates ([`Axis.axis_date`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axis_date.html#matplotlib.axis.Axis.axis_date "matplotlib.axis.Axis.axis_date")
) was 2000-01-01 to 2010-01-01. This has been changed to 1970-01-01 to 1970-01-02. With the default epoch, this makes the numeric limit for date axes the same as for other axes (0.0-1.0), and users are less likely to set a locator with far too many ticks.

### _markerfmt_ argument to `stem`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#markerfmt-argument-to-stem "Link to this heading")

The behavior of the _markerfmt_ parameter of [`stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
 has changed:

*   If _markerfmt_ does not contain a color, the color is taken from _linefmt_.
    
*   If _markerfmt_ does not contain a marker, the default is 'o'.
    

Before, _markerfmt_ was passed unmodified to `plot(..., fmt)`, which had a number of unintended side-effects; e.g. only giving a color switched to a solid line without markers.

For a simple call `stem(x, y)` without parameters, the new rules still reproduce the old behavior.

### `get_ticklabels` now always populates labels[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#get-ticklabels-now-always-populates-labels "Link to this heading")

Previously [`Axis.get_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "matplotlib.axis.Axis.get_ticklabels")
 (and [`Axes.get_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
, [`Axes.get_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklabels.html#matplotlib.axes.Axes.get_yticklabels "matplotlib.axes.Axes.get_yticklabels")
) would only return empty strings unless a draw had already been performed. Now the ticks and their labels are updated when the labels are requested.

### Warning when scatter plot color settings discarded[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#warning-when-scatter-plot-color-settings-discarded "Link to this heading")

When making an animation of a scatter plot, if you don't set _c_ (the color value parameter) when initializing the artist, the color settings are ignored. [`Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
 now raises a warning if color-related settings are changed without setting _c_.

### 3D `contourf` polygons placed between levels[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#d-contourf-polygons-placed-between-levels "Link to this heading")

The polygons used in a 3D [`contourf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.axes3d.Axes3D.contourf")
 plot are now placed halfway between the contour levels, as each polygon represents the location of values that lie between two levels.

### Axes title now avoids y-axis offset[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#axes-title-now-avoids-y-axis-offset "Link to this heading")

Previously, Axes titles could overlap the y-axis offset text, which is often in the upper left corner of the axes. Now titles are moved above the offset text if overlapping when automatic title positioning is in effect (i.e. if _y_ in [`Axes.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
 is _None_ and `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`) is also _None_).

### Dotted operators gain extra space in mathtext[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#dotted-operators-gain-extra-space-in-mathtext "Link to this heading")

In mathtext, `\doteq \doteqdot \dotminus \dotplus \dots` are now surrounded by extra space because they are correctly treated as relational or binary operators.

### _math_ parameter of `mathtext.get_unicode_index` defaults to False[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#math-parameter-of-mathtext-get-unicode-index-defaults-to-false "Link to this heading")

In math mode, ASCII hyphens (U+002D) are now replaced by Unicode minus signs (U+2212) at the parsing stage.

### `ArtistList` proxies copy contents on iteration[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#artistlist-proxies-copy-contents-on-iteration "Link to this heading")

When iterating over the contents of the dynamically generated proxy lists for the Artist-type accessors (see [Axes children are no longer separated by type](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#behavioural-api-changes-3-5-axes-children-combined)
), a copy of the contents is made. This ensure that artists can safely be added or removed from the Axes while iterating over their children.

This is a departure from the expected behavior of mutable iterable data types in Python — iterating over a list while mutating it has surprising consequences and dictionaries will error if they change size during iteration. Because all of the accessors are filtered views of the same underlying list, it is possible for seemingly unrelated changes, such as removing a Line, to affect the iteration over any of the other accessors. In this case, we have opted to make a copy of the relevant children before yielding them to the user.

This change is also consistent with our plan to make these accessors immutable in Matplotlib 3.7.

### `AxesImage` string representation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#axesimage-string-representation "Link to this heading")

The string representation of [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 changes from stating the position in the figure `"AxesImage(80,52.8;496x369.6)"` to giving the number of pixels `"AxesImage(size=(300, 200))"`.

### Improved autoscaling for Bézier curves[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#improved-autoscaling-for-bezier-curves "Link to this heading")

Bézier curves are now autoscaled to their extents - previously they were autoscaled to their ends and control points, which in some cases led to unnecessarily large limits.

### `QuadMesh` mouseover defaults to False[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#quadmesh-mouseover-defaults-to-false "Link to this heading")

New in 3.5, [`QuadMesh.get_cursor_data`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh.get_cursor_data "matplotlib.collections.QuadMesh.get_cursor_data")
 allows display of data values under the cursor. However, this can be very slow for large meshes, so mouseover now defaults to _False_.

### Changed pgf backend document class[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#changed-pgf-backend-document-class "Link to this heading")

The pgf backend now uses the `article` document class as basis for compilation.

### `MathtextBackendAgg.get_results` no longer returns `used_characters`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#mathtextbackendagg-get-results-no-longer-returns-used-characters "Link to this heading")

The last item (`used_characters`) in the tuple returned by `MathtextBackendAgg.get_results` has been removed. In order to unpack this tuple in a backward and forward-compatible way, use e.g. `ox, oy, width, height, descent, image, *_ = parse(...)`, which will ignore `used_characters` if it was present.

### `Type1Font` objects include more properties[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#type1font-objects-include-more-properties "Link to this heading")

The `matplotlib._type1font.Type1Font.prop` dictionary now includes more keys, such as `CharStrings` and `Subrs`. The value of the `Encoding` key is now a dictionary mapping codes to glyph names. The `matplotlib._type1font.Type1Font.transform` method now correctly removes `UniqueID` properties from the font.

### `rcParams.copy()` returns `RcParams` rather than `dict`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#rcparams-copy-returns-rcparams-rather-than-dict "Link to this heading")

Returning an [`RcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
 instance from [`RcParams.copy`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams.copy "matplotlib.RcParams.copy")
 makes the copy still validate inputs, and additionally avoids emitting deprecation warnings when using a previously copied instance to update the global instance (even if some entries are deprecated).

### `rc_context` no longer resets the value of `'backend'`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#rc-context-no-longer-resets-the-value-of-backend "Link to this heading")

[`matplotlib.rc_context`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
 incorrectly reset the value of `[rcParams["backend"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=backend#rcparam-backend) ` if backend resolution was triggered in the context. This affected only the value. The actual backend was not changed. Now, [`matplotlib.rc_context`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
 does not reset `[rcParams["backend"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=backend#rcparam-backend) ` anymore.

### Default `rcParams["animation.convert_args"]` changed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#default-rcparams-animation-convert-args-changed "Link to this heading")

It now defaults to `["-layers", "OptimizePlus"]` to try to generate smaller GIFs. Set it back to an empty list to recover the previous behavior.

### Style file encoding now specified to be UTF-8[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#style-file-encoding-now-specified-to-be-utf-8 "Link to this heading")

It has been impossible to import Matplotlib with a non UTF-8 compatible locale encoding because we read the style library at import time. This change is formalizing and documenting the status quo so there is no deprecation period.

### MacOSX backend uses sRGB instead of GenericRGB color space[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#macosx-backend-uses-srgb-instead-of-genericrgb-color-space "Link to this heading")

MacOSX backend now display sRGB tagged image instead of GenericRGB which is an older (now deprecated) Apple color space. This is the source color space used by ColorSync to convert to the current display profile.

### Renderer optional for `get_tightbbox` and `get_window_extent`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#renderer-optional-for-get-tightbbox-and-get-window-extent "Link to this heading")

The [`Artist.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#matplotlib.artist.Artist.get_tightbbox "matplotlib.artist.Artist.get_tightbbox")
 and [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")
 methods no longer require the _renderer_ keyword argument, saving users from having to query it from `fig.canvas.get_renderer`. If the _renderer_ keyword argument is not supplied, these methods first check if there is a cached renderer from a previous draw and use that. If there is no cached renderer, then the methods will use `fig.canvas.get_renderer()` as a fallback.

### `FigureFrameWx` constructor, subclasses, and `get_canvas`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#figureframewx-constructor-subclasses-and-get-canvas "Link to this heading")

The `FigureCanvasWx` constructor gained a _canvas\_class_ keyword-only parameter which specifies the canvas class that should be used. This parameter will become required in the future. The `get_canvas` method, which was previously used to customize canvas creation, is deprecated. The `FigureFrameWxAgg` and `FigureFrameWxCairo` subclasses, which overrode `get_canvas`, are deprecated.

### `FigureFrameWx.sizer`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#figureframewx-sizer "Link to this heading")

... has been removed. The frame layout is no longer based on a sizer, as the canvas is now the sole child widget; the toolbar is now a regular toolbar added using `SetToolBar`.

### Incompatible layout engines raise[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#incompatible-layout-engines-raise "Link to this heading")

You cannot switch between `tight_layout` and `constrained_layout` if a colorbar has already been added to a figure. Invoking the incompatible layout engine used to warn, but now raises with a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)")
.

### `CallbackRegistry` raises on unknown signals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#callbackregistry-raises-on-unknown-signals "Link to this heading")

When Matplotlib instantiates a [`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
, it now limits callbacks to the signals that the registry knows about. In practice, this means that calling [`mpl_connect`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
 with an invalid signal name now raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
.

### Changed exception type for incorrect SVG date metadata[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#changed-exception-type-for-incorrect-svg-date-metadata "Link to this heading")

Providing date metadata with incorrect type to the SVG backend earlier resulted in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
. Now, a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 is raised instead.

### Specified exception types in `Grid`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#specified-exception-types-in-grid "Link to this heading")

In a few cases an [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")
 was thrown when an incorrect argument value was set in the [`mpl_toolkits.axes_grid1.axes_grid.Grid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.axes_grid.Grid")
 (= `mpl_toolkits.axisartist.axes_grid.Grid`) constructor. These are replaced as follows:

*   Providing an incorrect value for _ngrids_ now raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
    
*   Providing an incorrect type for _rect_ now raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
    

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#id3)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Parameters to `plt.figure()` and the `Figure` constructor[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#parameters-to-plt-figure-and-the-figure-constructor "Link to this heading")

All parameters to [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
 and the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 constructor, other than _num_, _figsize_, and _dpi_, will become keyword-only after a deprecation period.

### Deprecation aliases in cbook[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#deprecation-aliases-in-cbook "Link to this heading")

The module `matplotlib.cbook.deprecation` was previously deprecated in Matplotlib 3.4, along with deprecation-related API in `matplotlib.cbook`. Due to technical issues, `matplotlib.cbook.MatplotlibDeprecationWarning` and `matplotlib.cbook.mplDeprecation` did not raise deprecation warnings on use. Changes in Python have now made it possible to warn when these aliases are being used.

In order to avoid downstream breakage, these aliases will now warn, and their removal has been pushed from 3.6 to 3.8 to give time to notice said warnings. As replacement, please use [`matplotlib.MatplotlibDeprecationWarning`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.MatplotlibDeprecationWarning "matplotlib.MatplotlibDeprecationWarning")
.

### `Axes` subclasses should override `clear` instead of `cla`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#axes-subclasses-should-override-clear-instead-of-cla "Link to this heading")

For clarity, [`axes.Axes.clear`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clear.html#matplotlib.axes.Axes.clear "matplotlib.axes.Axes.clear")
 is now preferred over [`Axes.cla`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.cla.html#matplotlib.axes.Axes.cla "matplotlib.axes.Axes.cla")
. However, for backwards compatibility, the latter will remain as an alias for the former.

For additional compatibility with third-party libraries, Matplotlib will continue to call the `cla` method of any [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclasses if they define it. In the future, this will no longer occur, and Matplotlib will only call the `clear` method in [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclasses.

It is recommended to define only the `clear` method when on Matplotlib 3.6, and only `cla` for older versions.

### Pending deprecation top-level cmap registration and access functions in `mpl.cm`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#pending-deprecation-top-level-cmap-registration-and-access-functions-in-mpl-cm "Link to this heading")

As part of a [multi-step process](https://github.com/matplotlib/matplotlib/issues/20853)
 we are refactoring the global state for managing the registered colormaps.

In Matplotlib 3.5 we added a [`ColormapRegistry`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
 class and exposed an instance at the top level as `matplotlib.colormaps`. The existing top level functions in [`matplotlib.cm`](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")
 (`get_cmap`, `register_cmap`, `unregister_cmap`) were changed to be aliases around the same instance.

In Matplotlib 3.6 we have marked those top level functions as pending deprecation with the intention of deprecation in Matplotlib 3.7. The following functions have been marked for pending deprecation:

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

### Pending deprecation of layout methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#pending-deprecation-of-layout-methods "Link to this heading")

The methods [`set_tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#matplotlib.figure.Figure.set_tight_layout "matplotlib.figure.Figure.set_tight_layout")
, [`set_constrained_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout.html#matplotlib.figure.Figure.set_constrained_layout "matplotlib.figure.Figure.set_constrained_layout")
, are discouraged, and now emit a [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "(in Python v3.14)")
 in favor of explicitly referencing the layout engine via `figure.set_layout_engine('tight')` and `figure.set_layout_engine('constrained')`. End users should not see the warning, but library authors should adjust.

The methods [`set_constrained_layout_pads`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout_pads.html#matplotlib.figure.Figure.set_constrained_layout_pads "matplotlib.figure.Figure.set_constrained_layout_pads")
 and [`get_constrained_layout_pads`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_constrained_layout_pads.html#matplotlib.figure.Figure.get_constrained_layout_pads "matplotlib.figure.Figure.get_constrained_layout_pads")
 are will be deprecated in favor of `figure.get_layout_engine().set()` and `figure.get_layout_engine().get()`, and currently emit a [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "(in Python v3.14)")
.

### seaborn styles renamed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#seaborn-styles-renamed "Link to this heading")

Matplotlib currently ships many style files inspired from the seaborn library ("seaborn", "seaborn-bright", "seaborn-colorblind", etc.) but they have gone out of sync with the library itself since the release of seaborn 0.9. To prevent confusion, the style files have been renamed "seaborn-v0\_8", "seaborn-v0\_8-bright", "seaborn-v0\_8-colorblind", etc. Users are encouraged to directly use seaborn to access the up-to-date styles.

### Auto-removal of overlapping Axes by `plt.subplot` and `plt.subplot2grid`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#auto-removal-of-overlapping-axes-by-plt-subplot-and-plt-subplot2grid "Link to this heading")

Previously, [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 and [`pyplot.subplot2grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
 would automatically remove preexisting Axes that overlap with the newly added Axes. This behavior was deemed confusing, and is now deprecated. Explicitly call `ax.remove()` on Axes that need to be removed.

### Passing _linefmt_ positionally to `stem` is undeprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#passing-linefmt-positionally-to-stem-is-undeprecated "Link to this heading")

Positional use of all formatting parameters in [`stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
 has been deprecated since Matplotlib 3.5. This deprecation is relaxed so that one can still pass _linefmt_ positionally, i.e. `stem(x, y, 'r')`.

### `stem(..., use_line_collection=False)`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#stem-use-line-collection-false "Link to this heading")

... is deprecated with no replacement. This was a compatibility fallback to a former more inefficient representation of the stem lines.

### Positional / keyword arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#positional-keyword-arguments "Link to this heading")

Passing all but the very few first arguments positionally in the constructors of Artists is deprecated. Most arguments will become keyword-only in a future version.

Passing too many positional arguments to `tripcolor` is now deprecated (extra arguments were previously silently ignored).

Passing _emit_ and _auto_ parameters of `set_xlim`, `set_ylim`, `set_zlim`, `set_rlim` positionally is deprecated; they will become keyword-only in a future release.

The _transOffset_ parameter of [`Collection.set_offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")
 and the various `create_collection` methods of legend handlers has been renamed to _offset\_transform_ (consistently with the property name).

Calling `MarkerStyle()` with no arguments or `MarkerStyle(None)` is deprecated; use `MarkerStyle("")` to construct an empty marker style.

`Axes.get_window_extent` / `Figure.get_window_extent` accept only _renderer_. This aligns the API with the general [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")
 API. All other parameters were ignored anyway.

The _cleared_ parameter of `get_renderer`, which only existed for AGG-based backends, has been deprecated. Use `renderer.clear()` instead to explicitly clear the renderer buffer.

### Methods to set parameters in `LogLocator` and `LogFormatter*`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#methods-to-set-parameters-in-loglocator-and-logformatter "Link to this heading")

In [`LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter")
 and derived subclasses, the methods `base` and `label_minor` for setting the respective parameter are deprecated and replaced by `set_base` and `set_label_minor`, respectively.

In [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
, the methods `base` and `subs` for setting the respective parameter are deprecated. Instead, use `set_params(base=..., subs=...)`.

### `Axes.get_renderer_cache`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#axes-get-renderer-cache "Link to this heading")

The canvas now takes care of the renderer and whether to cache it or not. The alternative is to call `axes.figure.canvas.get_renderer()`.

### Groupers from `get_shared_x_axes` / `get_shared_y_axes` will be immutable[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#groupers-from-get-shared-x-axes-get-shared-y-axes-will-be-immutable "Link to this heading")

Modifications to the Groupers returned by `get_shared_x_axes` and `get_shared_y_axes` are deprecated. In the future, these methods will return immutable views on the grouper structures. Note that previously, calling e.g. `join()` would already fail to set up the correct structures for sharing axes; use [`Axes.sharex`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharex.html#matplotlib.axes.Axes.sharex "matplotlib.axes.Axes.sharex")
 or [`Axes.sharey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharey.html#matplotlib.axes.Axes.sharey "matplotlib.axes.Axes.sharey")
 instead.

### Unused methods in `Axis`, `Tick`, `XAxis`, and `YAxis`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#unused-methods-in-axis-tick-xaxis-and-yaxis "Link to this heading")

`Tick.label` has been pending deprecation since 3.1 and is now deprecated. Use `Tick.label1` instead.

The following methods are no longer used and deprecated without a replacement:

*   `Axis.get_ticklabel_extents`
    
*   `Tick.get_pad_pixels`
    
*   `XAxis.get_text_heights`
    
*   `YAxis.get_text_widths`
    

### `mlab.stride_windows`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#mlab-stride-windows "Link to this heading")

... is deprecated. Use `np.lib.stride_tricks.sliding_window_view` instead (or `np.lib.stride_tricks.as_strided` on NumPy < 1.20).

### Event handlers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#event-handlers "Link to this heading")

The `draw_event`, `resize_event`, `close_event`, `key_press_event`, `key_release_event`, `pick_event`, `scroll_event`, `button_press_event`, `button_release_event`, `motion_notify_event`, `enter_notify_event` and `leave_notify_event` methods of [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
 are deprecated. They had inconsistent signatures across backends, and made it difficult to improve event metadata.

In order to trigger an event on a canvas, directly construct an [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
 object of the correct class and call `canvas.callbacks.process(event.name, event)`.

### Widgets[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#widgets "Link to this heading")

All parameters to `MultiCursor` starting from _useblit_ are becoming keyword-only (passing them positionally is deprecated).

The `canvas` and `background` attributes of `MultiCursor` are deprecated with no replacement.

The _visible_ attribute of Selector widgets has been deprecated; use `set_visible` or `get_visible` instead.

The _state\_modifier\_keys_ attribute of Selector widgets has been privatized and the modifier keys must be set when creating the widget.

### `Axes3D.dist`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#axes3d-dist "Link to this heading")

... has been privatized. Use the _zoom_ keyword argument in [`Axes3D.set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect")
 instead.

### 3D Axis[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#d-axis "Link to this heading")

The previous constructor of [`axis3d.Axis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis "mpl_toolkits.mplot3d.axis3d.Axis")
, with signature `(self, adir, v_intervalx, d_intervalx, axes, *args, rotate_label=None, **kwargs)` is deprecated in favor of a new signature closer to the one of 2D Axis; it is now `(self, axes, *, rotate_label=None, **kwargs)` where `kwargs` are forwarded to the 2D Axis constructor. The axis direction is now inferred from the axis class' `axis_name` attribute (as in the 2D case); the `adir` attribute is deprecated.

The `init3d` method of 3D Axis is also deprecated; all the relevant initialization is done as part of the constructor.

The `d_interval` and `v_interval` attributes of 3D Axis are deprecated; use `get_data_interval` and `get_view_interval` instead.

The `w_xaxis`, `w_yaxis`, and `w_zaxis` attributes of `Axis3D` have been pending deprecation since 3.1. They are now deprecated. Instead use `xaxis`, `yaxis`, and `zaxis`.

`mplot3d.axis3d.Axis.set_pane_pos` is deprecated. This is an internal method where the provided values are overwritten during drawing. Hence, it does not serve any purpose to be directly accessible.

The two helper functions `mplot3d.axis3d.move_from_center` and `mplot3d.axis3d.tick_update_position` are considered internal and deprecated. If these are required, please vendor the code from the corresponding private methods `_move_from_center` and `_tick_update_position`.

### `Figure.callbacks` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#figure-callbacks-is-deprecated "Link to this heading")

The Figure `callbacks` property is deprecated. The only signal was "dpi\_changed", which can be replaced by connecting to the "resize\_event" on the canvas `figure.canvas.mpl_connect("resize_event", func)` instead.

### `FigureCanvas` without a `required_interactive_framework` attribute[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#figurecanvas-without-a-required-interactive-framework-attribute "Link to this heading")

Support for such canvas classes is deprecated. Note that canvas classes which inherit from `FigureCanvasBase` always have such an attribute.

### Backend-specific deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#backend-specific-deprecations "Link to this heading")

*   `backend_gtk3.FigureManagerGTK3Agg` and `backend_gtk4.FigureManagerGTK4Agg`; directly use `backend_gtk3.FigureManagerGTK3` and `backend_gtk4.FigureManagerGTK4` instead.
    
*   The _window_ parameter to `backend_gtk3.NavigationToolbar2GTK3` had no effect, and is now deprecated.
    
*   `backend_gtk3.NavigationToolbar2GTK3.win`
    
*   `backend_gtk3.RendererGTK3Cairo` and `backend_gtk4.RendererGTK4Cairo`; use [`RendererCairo`](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo "matplotlib.backends.backend_cairo.RendererCairo")
     instead, which has gained the `set_context` method, which also auto-infers the size of the underlying surface.
    
*   `backend_cairo.RendererCairo.set_ctx_from_surface` and `backend_cairo.RendererCairo.set_width_height` in favor of [`RendererCairo.set_context`](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.set_context "matplotlib.backends.backend_cairo.RendererCairo.set_context")
    .
    
*   `backend_gtk3.error_msg_gtk`
    
*   `backend_gtk3.icon_filename` and `backend_gtk3.window_icon`
    
*   `backend_macosx.NavigationToolbar2Mac.prepare_configure_subplots` has been replaced by `configure_subplots()`.
    
*   `backend_pdf.Name.hexify`
    
*   `backend_pdf.Operator` and `backend_pdf.Op.op` are deprecated in favor of a single standard [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)")
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
    
*   `backend_qt.qApp`; use `QtWidgets.QApplication.instance()` instead.
    
*   `backend_svg.escape_attrib`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.escape_cdata`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.escape_comment`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.short_float_fmt`; vendor the code of the similarly named private functions if you rely on it.
    
*   `backend_svg.generate_transform` and `backend_svg.generate_css`
    
*   `backend_tk.NavigationToolbar2Tk.lastrect` and `backend_tk.RubberbandTk.lastrect`
    
*   `backend_tk.NavigationToolbar2Tk.window`; use `toolbar.master` instead.
    
*   `backend_tools.ToolBase.destroy`; To run code upon tool removal, connect to the `tool_removed_event` event.
    
*   `backend_wx.RendererWx.offset_text_height`
    
*   `backend_wx.error_msg_wx`
    
*   `FigureCanvasBase.pick`; directly call [`Figure.pick`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.pick.html#matplotlib.figure.Figure.pick "matplotlib.figure.Figure.pick")
    , which has taken over the responsibility of checking the canvas widget lock as well.
    
*   `FigureCanvasBase.resize`, which has no effect; use `FigureManagerBase.resize` instead.
    
*   `FigureManagerMac.close`
    
*   `FigureFrameWx.sizer`; use `frame.GetSizer()` instead.
    
*   `FigureFrameWx.figmgr` and `FigureFrameWx.get_figure_manager`; use `frame.canvas.manager` instead.
    
*   `FigureFrameWx.num`; use `frame.canvas.manager.num` instead.
    
*   `FigureFrameWx.toolbar`; use `frame.GetToolBar()` instead.
    
*   `FigureFrameWx.toolmanager`; use `frame.canvas.manager.toolmanager` instead.
    

### Modules[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#modules "Link to this heading")

The modules `matplotlib.afm`, `matplotlib.docstring`, `matplotlib.fontconfig_pattern`, `matplotlib.tight_bbox`, `matplotlib.tight_layout`, and `matplotlib.type1font` are considered internal and public access is deprecated.

### `checkdep_usetex` deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#checkdep-usetex-deprecated "Link to this heading")

This method was only intended to disable tests in case no latex install was found. As such, it is considered to be private and for internal use only.

Please vendor the code if you need this.

### `date_ticker_factory` deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#date-ticker-factory-deprecated "Link to this heading")

The `date_ticker_factory` method in the [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 module is deprecated. Instead use [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
 and [`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
 for a more flexible and scalable locator and formatter.

If you need the exact `date_ticker_factory` behavior, please copy the code.

### `dviread.find_tex_file` will raise `FileNotFoundError`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#dviread-find-tex-file-will-raise-filenotfounderror "Link to this heading")

In the future, `dviread.find_tex_file` will raise a [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "(in Python v3.14)")
 for missing files. Previously, it would return an empty string in such cases. Raising an exception allows attaching a user-friendly message instead. During the transition period, a warning is raised.

### `transforms.Affine2D.identity()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#transforms-affine2d-identity "Link to this heading")

... is deprecated in favor of directly calling the [`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 constructor with no arguments.

### Deprecations in `testing.decorators`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#deprecations-in-testing-decorators "Link to this heading")

The unused class `CleanupTestCase` and decorator `cleanup` are deprecated and will be removed. Vendor the code, including the private function `_cleanup_cm`.

The function `check_freetype_version` is considered internal and deprecated. Vendor the code of the private function `_check_freetype_version`.

### `text.get_rotation()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#text-get-rotation "Link to this heading")

... is deprecated with no replacement. Copy the original implementation if needed.

### Miscellaneous internals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#miscellaneous-internals "Link to this heading")

*   `axes_grid1.axes_size.AddList`; use `sum(sizes, start=Fixed(0))` (for example) to sum multiple size objects.
    
*   `axes_size.Padded`; use `size + pad` instead
    
*   `axes_size.SizeFromFunc`, `axes_size.GetExtentHelper`
    
*   `AxisArtistHelper.delta1` and `AxisArtistHelper.delta2`
    
*   `axislines.GridHelperBase.new_gridlines` and `axislines.Axes.new_gridlines`
    
*   `cbook.maxdict`; use the standard library `functools.lru_cache` instead.
    
*   `_DummyAxis.dataLim` and `_DummyAxis.viewLim`; use `get_data_interval()`, `set_data_interval()`, `get_view_interval()`, and `set_view_interval()` instead.
    
*   `GridSpecBase.get_grid_positions(..., raw=True)`
    
*   `ImageMagickBase.delay` and `ImageMagickBase.output_args`
    
*   `MathtextBackend`, `MathtextBackendAgg`, `MathtextBackendPath`, `MathTextWarning`
    
*   `TexManager.get_font_config`; it previously returned an internal hashed key for used for caching purposes.
    
*   `TextToPath.get_texmanager`; directly construct a [`texmanager.TexManager`](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager "matplotlib.texmanager.TexManager")
     instead.
    
*   `ticker.is_close_to_int`; use `math.isclose(x, round(x))` instead.
    
*   `ticker.is_decade`; use `y = numpy.log(x)/numpy.log(base); numpy.isclose(y, numpy.round(y))` instead.
    

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#id4)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following deprecated APIs have been removed:

### Removed behaviour[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#removed-behaviour "Link to this heading")

#### Stricter validation of function parameters[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#stricter-validation-of-function-parameters "Link to this heading")

*   Unknown keyword arguments to [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
    , [`pyplot.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
    , and the `FigureCanvas.print_*` methods now raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
    , instead of being ignored.
    
*   Extra parameters to the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
     constructor, i.e., those other than _fig_ and _rect_, are now keyword only.
    
*   Passing arguments not specifically listed in the signatures of [`Axes3D.plot_surface`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface")
     and [`Axes3D.plot_wireframe`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe")
     is no longer supported; pass any extra arguments as keyword arguments instead.
    
*   Passing positional arguments to [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     has been removed; use specific keyword argument names now.
    

#### `imread` no longer accepts URLs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#imread-no-longer-accepts-urls "Link to this heading")

Passing a URL to [`imread()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread "matplotlib.pyplot.imread")
 has been removed. Please open the URL for reading and directly use the Pillow API (e.g., `PIL.Image.open(urllib.request.urlopen(url))`, or `PIL.Image.open(io.BytesIO(requests.get(url).content))`) instead.

#### MarkerStyle is immutable[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#markerstyle-is-immutable "Link to this heading")

The methods `MarkerStyle.set_fillstyle` and `MarkerStyle.set_marker` have been removed. Create a new [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
 with the respective parameters instead.

#### Passing bytes to `FT2Font.set_text`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#passing-bytes-to-ft2font-set-text "Link to this heading")

... is no longer supported. Pass [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 instead.

#### Support for passing tool names to `ToolManager.add_tool`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#support-for-passing-tool-names-to-toolmanager-add-tool "Link to this heading")

... has been removed. The second parameter to [`ToolManager.add_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.add_tool "matplotlib.backend_managers.ToolManager.add_tool")
 must now always be a tool class.

#### `backend_tools.ToolFullScreen` now inherits from `ToolBase`, not from `ToolToggleBase`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#backend-tools-toolfullscreen-now-inherits-from-toolbase-not-from-tooltogglebase "Link to this heading")

[`ToolFullScreen`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolFullScreen "matplotlib.backend_tools.ToolFullScreen")
 can only switch between the non-fullscreen and fullscreen states, but not unconditionally put the window in a given state; hence the `enable` and `disable` methods were misleadingly named. Thus, the [`ToolToggleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")
\-related API (`enable`, `disable`, etc.) was removed.

#### `BoxStyle._Base` and `transmute` method of box styles[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#boxstyle-base-and-transmute-method-of-box-styles "Link to this heading")

... have been removed. Box styles implemented as classes no longer need to inherit from a base class.

#### Loaded modules logging[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#loaded-modules-logging "Link to this heading")

The list of currently loaded modules is no longer logged at the DEBUG level at Matplotlib import time, because it can produce extensive output and make other valuable DEBUG statements difficult to find. If you were relying on this output, please arrange for your own logging (the built-in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "(in Python v3.14)")
 can be used to get the currently loaded modules).

### Modules[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#id1 "Link to this heading")

*   The `cbook.deprecation` module has been removed from the public API as it is considered internal.
    
*   The `mpl_toolkits.axes_grid` module has been removed. All functionality from `mpl_toolkits.axes_grid` can be found in either [`mpl_toolkits.axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
     or [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
    . Axes classes from `mpl_toolkits.axes_grid` based on `Axis` from [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
     can be found in [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
    .
    

### Classes, methods and attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#classes-methods-and-attributes "Link to this heading")

The following module-level classes/variables have been removed:

*   `cm.cmap_d`
    
*   `colorbar.colorbar_doc`, `colorbar.colorbar_kw_doc`
    
*   `ColorbarPatch`
    
*   `mathtext.Fonts` and all its subclasses
    
*   `mathtext.FontConstantsBase` and all its subclasses
    
*   `mathtext.latex_to_bakoma`, `mathtext.latex_to_cmex`, `mathtext.latex_to_standard`
    
*   `mathtext.MathtextBackendPdf`, `mathtext.MathtextBackendPs`, `mathtext.MathtextBackendSvg`, `mathtext.MathtextBackendCairo`; use `.MathtextBackendPath` instead.
    
*   `mathtext.Node` and all its subclasses
    
*   `mathtext.NUM_SIZE_LEVELS`
    
*   `mathtext.Parser`
    
*   `mathtext.Ship`
    
*   `mathtext.SHRINK_FACTOR` and `mathtext.GROW_FACTOR`
    
*   `mathtext.stix_virtual_fonts`,
    
*   `mathtext.tex2uni`
    
*   `backend_pgf.TmpDirCleaner`
    
*   `backend_ps.GraphicsContextPS`; use `GraphicsContextBase` instead.
    
*   `backend_wx.IDLE_DELAY`
    
*   `axes_grid1.parasite_axes.ParasiteAxesAuxTransBase`; use [`ParasiteAxesBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxesBase "mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxesBase")
     instead.
    
*   `axes_grid1.parasite_axes.ParasiteAxesAuxTrans`; use [`ParasiteAxes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes.html#mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes "mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes")
     instead.
    

The following class attributes have been removed:

*   `Line2D.validCap` and `Line2D.validJoin`; validation is centralized in `rcsetup`.
    
*   `Patch.validCap` and `Patch.validJoin`; validation is centralized in `rcsetup`.
    
*   `renderer.M`, `renderer.eye`, `renderer.vvec`, `renderer.get_axis_position` placed on the Renderer during 3D Axes draw; these attributes are all available via [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
    , which can be accessed via `self.axes` on all [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
    s.
    
*   `RendererPdf.mathtext_parser`, `RendererPS.mathtext_parser`, `RendererSVG.mathtext_parser`, `RendererCairo.mathtext_parser`
    
*   `StandardPsFonts.pswriter`
    
*   `Subplot.figbox`; use [`Axes.get_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_position.html#matplotlib.axes.Axes.get_position "matplotlib.axes.Axes.get_position")
     instead.
    
*   `Subplot.numRows`; `ax.get_gridspec().nrows` instead.
    
*   `Subplot.numCols`; `ax.get_gridspec().ncols` instead.
    
*   `SubplotDivider.figbox`
    
*   `cids`, `cnt`, `observers`, `change_observers`, and `submit_observers` on all [`Widget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget "matplotlib.widgets.Widget")
    s
    

The following class methods have been removed:

*   `Axis.cla()`; use [`Axis.clear`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.clear.html#matplotlib.axis.Axis.clear "matplotlib.axis.Axis.clear")
     instead.
    
*   `RadialAxis.cla()` and `ThetaAxis.cla()`; use [`RadialAxis.clear`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialAxis.clear "matplotlib.projections.polar.RadialAxis.clear")
     or [`ThetaAxis.clear`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaAxis.clear "matplotlib.projections.polar.ThetaAxis.clear")
     instead.
    
*   `Spine.cla()`; use [`Spine.clear`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.clear "matplotlib.spines.Spine.clear")
     instead.
    
*   `ContourLabeler.get_label_coords()`; there is no replacement as it was considered an internal helper.
    
*   `FancyArrowPatch.get_dpi_cor` and `FancyArrowPatch.set_dpi_cor`
    
*   `FigureCanvas.get_window_title()` and `FigureCanvas.set_window_title()`; use [`FigureManagerBase.get_window_title`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.get_window_title "matplotlib.backend_bases.FigureManagerBase.get_window_title")
     or [`FigureManagerBase.set_window_title`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.set_window_title "matplotlib.backend_bases.FigureManagerBase.set_window_title")
     if using pyplot, or use GUI-specific methods if embedding.
    
*   `FigureManager.key_press()` and `FigureManager.button_press()`; trigger the events directly on the canvas using `canvas.callbacks.process(event.name, event)` for key and button events.
    
*   `RendererAgg.get_content_extents()` and `RendererAgg.tostring_rgba_minimized()`
    
*   `NavigationToolbar2Wx.get_canvas()`
    
*   `ParasiteAxesBase.update_viewlim()`; use `ParasiteAxesBase.apply_aspect` instead.
    
*   `Subplot.get_geometry()`; use `SubplotBase.get_subplotspec` instead.
    
*   `Subplot.change_geometry()`; use `SubplotBase.set_subplotspec` instead.
    
*   `Subplot.update_params()`; this method did nothing.
    
*   `Subplot.is_first_row()`; use `ax.get_subplotspec().is_first_row` instead.
    
*   `Subplot.is_first_col()`; use `ax.get_subplotspec().is_first_col` instead.
    
*   `Subplot.is_last_row()`; use `ax.get_subplotspec().is_last_row` instead.
    
*   `Subplot.is_last_col()`; use `ax.get_subplotspec().is_last_col` instead.
    
*   `SubplotDivider.change_geometry()`; use [`SubplotDivider.set_subplotspec`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.set_subplotspec "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.set_subplotspec")
     instead.
    
*   `SubplotDivider.get_geometry()`; use [`SubplotDivider.get_subplotspec`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.get_subplotspec "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.get_subplotspec")
     instead.
    
*   `SubplotDivider.update_params()`
    
*   `get_depth`, `parse`, `to_mask`, `to_rgba`, and `to_png` of [`MathTextParser`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.MathTextParser "matplotlib.mathtext.MathTextParser")
    ; use [`mathtext.math_to_image`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.math_to_image "matplotlib.mathtext.math_to_image")
     instead.
    
*   `MovieWriter.cleanup()`; the cleanup logic is instead fully implemented in [`MovieWriter.finish`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter.finish "matplotlib.animation.MovieWriter.finish")
     and `cleanup` is no longer called.
    

### Functions[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#functions "Link to this heading")

The following functions have been removed;

*   `backend_template.new_figure_manager()`, `backend_template.new_figure_manager_given_figure()`, and `backend_template.draw_if_interactive()` have been removed, as part of the introduction of the simplified backend API.
    
*   Deprecation-related re-imports `cbook.deprecated()`, and `cbook.warn_deprecated()`.
    
*   `colorbar.colorbar_factory()`; use [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
     instead. `colorbar.make_axes_kw_doc()`
    
*   `mathtext.Error()`
    
*   `mathtext.ship()`
    
*   `mathtext.tex2uni()`
    
*   `axes_grid1.parasite_axes.parasite_axes_auxtrans_class_factory()`; use [`parasite_axes_class_factory`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.parasite_axes_class_factory.html#mpl_toolkits.axes_grid1.parasite_axes.parasite_axes_class_factory "mpl_toolkits.axes_grid1.parasite_axes.parasite_axes_class_factory")
     instead.
    
*   `sphinext.plot_directive.align()`; use `docutils.parsers.rst.directives.images.Image.align` instead.
    

### Arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#arguments "Link to this heading")

The following arguments have been removed:

*   _dpi_ from `print_ps()` in the PS backend and `print_pdf()` in the PDF backend. Instead, the methods will obtain the DPI from the `savefig` machinery.
    
*   _dpi\_cor_ from [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
    
*   _minimum\_descent_ from `TextArea`; it is now effectively always True
    
*   _origin_ from `FigureCanvasWx.gui_repaint()`
    
*   _project_ from `Line3DCollection.draw()`
    
*   _renderer_ from [`Line3DCollection.do_3d_projection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection.do_3d_projection "mpl_toolkits.mplot3d.art3d.Line3DCollection.do_3d_projection")
    , [`Patch3D.do_3d_projection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Patch3D.html#mpl_toolkits.mplot3d.art3d.Patch3D.do_3d_projection "mpl_toolkits.mplot3d.art3d.Patch3D.do_3d_projection")
    , [`PathPatch3D.do_3d_projection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.PathPatch3D.html#mpl_toolkits.mplot3d.art3d.PathPatch3D.do_3d_projection "mpl_toolkits.mplot3d.art3d.PathPatch3D.do_3d_projection")
    , [`Path3DCollection.do_3d_projection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.do_3d_projection "mpl_toolkits.mplot3d.art3d.Path3DCollection.do_3d_projection")
    , [`Patch3DCollection.do_3d_projection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Patch3DCollection.html#mpl_toolkits.mplot3d.art3d.Patch3DCollection.do_3d_projection "mpl_toolkits.mplot3d.art3d.Patch3DCollection.do_3d_projection")
    , [`Poly3DCollection.do_3d_projection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.do_3d_projection "mpl_toolkits.mplot3d.art3d.Poly3DCollection.do_3d_projection")
    
*   _resize\_callback_ from the Tk backend; use `get_tk_widget().bind('<Configure>', ..., True)` instead.
    
*   _return\_all_ from `gridspec.get_position()`
    
*   Keyword arguments to `gca()`; there is no replacement.
    

### rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#rcparams "Link to this heading")

The setting `[rcParams["ps.useafm"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ps.useafm#rcparam-ps-useafm) ` (default: `False`) no longer has any effect on [`matplotlib.mathtext`](https://matplotlib.org/stable/api/mathtext_api.html#module-matplotlib.mathtext "matplotlib.mathtext")
.

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#id5)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#development-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Increase to minimum supported versions of dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#increase-to-minimum-supported-versions-of-dependencies "Link to this heading")

For Matplotlib 3.6, the [minimum supported versions](https://matplotlib.org/stable/install/dependencies.html#dependencies)
 are being bumped:

| Dependency | min in mpl3.5 | min in mpl3.6 |
| --- | --- | --- |
| Python | 3.7 | 3.8 |
| NumPy | 1.17 | 1.19 |

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)
 and [NEP29](https://numpy.org/neps/nep-0029-deprecation_policy.html)

### Build setup options changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#build-setup-options-changes "Link to this heading")

The `gui_support.macosx` setup option has been renamed to `packages.macosx`.

### New wheel architectures[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#new-wheel-architectures "Link to this heading")

Wheels have been added for:

*   Python 3.11
    
*   PyPy 3.8 and 3.9
    

### Increase to required versions of documentation dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#increase-to-required-versions-of-documentation-dependencies "Link to this heading")

[sphinx](https://pypi.org/project/Sphinx/)
 >= 3.0 and [numpydoc](https://pypi.org/project/numpydoc/)
 >= 1.0 are now required for building the documentation.

On this page
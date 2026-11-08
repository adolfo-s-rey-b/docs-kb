[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#main-content)

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
    

API Changes for 3.2.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#api-changes-for-3-2-0 "Link to this heading")

=================================================================================================================================================

[Behavior changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#id5)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#behavior-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Reduced default value of `[rcParams["axes.formatter.limits"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.limits#rcparam-axes-formatter-limits) ` (default: `[-5, 6]`)[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#reduced-default-value-of-rcparams-axes-formatter-limits-default-5-6 "Link to this heading")

Changed the default value of `[rcParams["axes.formatter.limits"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.limits#rcparam-axes-formatter-limits) ` (default: `[-5, 6]`) from -7, 7 to -5, 6 for better readability.

([`Source code`](https://matplotlib.org/stable/_downloads/b3458e6f3084b0fb41a3bd2a1734d9f7/api_changes_3-2-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/dad31bb8c63e801cd0a2a0c8063cd17f/api_changes_3-2-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/b98ba881dc29db14ab8857dec55de6e4/api_changes_3-2-0-1.png)
)

[![](https://matplotlib.org/stable/_images/api-prev_api_changes-api_changes_3-2-0-1.2x.png)](https://matplotlib.org/stable/_images/api-prev_api_changes-api_changes_3-2-0-1.2x.png)

### [`matplotlib.colorbar.Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 uses un-normalized axes for all mappables[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#matplotlib-colorbar-colorbar-uses-un-normalized-axes-for-all-mappables "Link to this heading")

Before 3.0, [`matplotlib.colorbar.Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 ([`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
) normalized all axes limits between 0 and 1 and had custom tickers to handle the labelling of the colorbar ticks. After 3.0, colorbars constructed from mappables that were _not_ contours were constructed with axes that had limits between `vmin` and `vmax` of the mappable's norm, and the tickers were made children of the normal axes tickers.

This version of Matplotlib extends that to mappables made by contours, and allows the axes to run between the lowest boundary in the contour and the highest.

Code that worked around the normalization between 0 and 1 will need to be modified.

### `MovieWriterRegistry`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#moviewriterregistry "Link to this heading")

[`MovieWriterRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry "matplotlib.animation.MovieWriterRegistry")
 now always checks the availability of the writer classes before returning them. If one wishes, for example, to get the first available writer, without performing the availability check on subsequent writers, it is now possible to iterate over the registry, which will yield the names of the available classes.

### Autoscaling[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#autoscaling "Link to this heading")

Matplotlib used to recompute autoscaled limits after every plotting (`plot()`, `bar()`, etc.) call. It now only does so when actually rendering the canvas, or when the user queries the Axes limits. This is a major performance improvement for plots with a large number of artists.

In particular, this means that artists added manually with [`Axes.add_line`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line "matplotlib.axes.Axes.add_line")
, [`Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
, etc. will be taken into account by the autoscale, even without an explicit call to [`Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
.

In some cases, this can result in different limits being reported. If this is an issue, consider triggering a draw with `fig.canvas.draw()`.

Autoscaling has also changed for artists that are based on the [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 class. Previously, the method that calculates the automatic limits [`Collection.get_datalim`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_datalim "matplotlib.collections.Collection.get_datalim")
 tried to take into account the size of objects in the collection and make the limits large enough to not clip any of the object, i.e., for [`Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
 it would make the limits large enough to not clip any markers in the scatter. This is problematic when the object size is specified in physical space, or figure-relative space, because the transform from physical units to data limits requires knowing the data limits, and becomes invalid when the new limits are applied. This is an inverse problem that is theoretically solvable (if the object is physically smaller than the axes), but the extra complexity was not deemed worth it, particularly as the most common use case is for markers in scatter that are usually small enough to be accommodated by the default data limit margins.

While the new behavior is algorithmically simpler, it is conditional on properties of the [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 object:

1.  `offsets = None`, `transform` is a child of `Axes.transData`: use the paths for the automatic limits (i.e. for [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     in [`Axes.streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
    ).
    
2.  `offsets != None`, and `offset_transform` is child of `Axes.transData`:
    
    1.  `transform` is child of `Axes.transData`: use the `path + offset` for limits (i.e., for [`Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
        ).
        
    2.  `transform` is not a child of `Axes.transData`: just use the offsets for the limits (i.e. for scatter)
        
3.  otherwise return a null [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    .
    

While this seems complicated, the logic is simply to use the information from the object that are in data space for the limits, but not information that is in physical units.

### log-scale bar() / hist() autolimits[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#log-scale-bar-hist-autolimits "Link to this heading")

The autolimits computation in [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
 when the axes already uses log-scale has changed to match the computation when the axes is switched to log-scale after the call to [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
, and when calling `bar(..., log=True)` / `hist(..., log=True)`: if there are at least two different bar heights, add the normal axes margins to them (in log-scale); if there is only a single bar height, expand the axes limits by one order of magnitude around it and then apply axes margins.

### Axes labels spanning multiple rows/columns[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#axes-labels-spanning-multiple-rows-columns "Link to this heading")

`Axes.label_outer` now correctly keep the x labels and tick labels visible for Axes spanning multiple rows, as long as they cover the last row of the Axes grid. (This is consistent with keeping the y labels and tick labels visible for Axes spanning multiple columns as long as they cover the first column of the Axes grid.)

The `Axes.is_last_row` and `Axes.is_last_col` methods now correctly return True for Axes spanning multiple rows, as long as they cover the last row or column respectively. Again this is consistent with the behavior for axes covering the first row or column.

The `Axes.rowNum` and `Axes.colNum` attributes are deprecated, as they only refer to the first grid cell covered by the Axes. Instead, use the new `ax.get_subplotspec().rowspan` and `ax.get_subplotspec().colspan` properties, which are [`range`](https://docs.python.org/3/library/stdtypes.html#range "(in Python v3.14)")
 objects indicating the whole span of rows and columns covered by the subplot.

(Note that all methods and attributes mentioned here actually only exist on the `Subplot` subclass of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, which is used for grid-positioned Axes but not for Axes positioned directly in absolute coordinates.)

The [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 class gained the `nrows` and `ncols` properties as more explicit synonyms for the parameters returned by `GridSpec.get_geometry`.

### Locators[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#locators "Link to this heading")

When more than [`Locator.MAXTICKS`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.MAXTICKS "matplotlib.ticker.Locator.MAXTICKS")
 ticks are generated, the behavior of [`Locator.raise_if_exceeds`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.raise_if_exceeds "matplotlib.ticker.Locator.raise_if_exceeds")
 changed from raising a RuntimeError to emitting a log at WARNING level.

### nonsingular Locators[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#nonsingular-locators "Link to this heading")

`Locator.nonsingular` (introduced in mpl 3.1), `DateLocator.nonsingular`, and `AutoDateLocator.nonsingular` now returns a range `v0, v1` with `v0 <= v1`. This behavior is consistent with the implementation of `nonsingular` by the `LogLocator` and `LogitLocator` subclasses.

### `get_data_ratio`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#get-data-ratio "Link to this heading")

`Axes.get_data_ratio` now takes the axes scale into account (linear, log, logit, etc.) before computing the y-to-x ratio. This change allows fixed aspects to be applied to any combination of x and y scales.

### Artist sticky edges[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#artist-sticky-edges "Link to this heading")

Previously, the `sticky_edges` attribute of artists was a list of values such that if an axis limit coincides with a sticky edge, it would not be expanded by the axes margins (this is the mechanism that e.g. prevents margins from being added around images).

`sticky_edges` now have an additional effect on margins application: even if an axis limit did not coincide with a sticky edge, it cannot _cross_ a sticky edge through margin application -- instead, the margins will only expand the axis limit until it bumps against the sticky edge.

This change improves the margins of axes displaying a [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
:

*   if the streamplot goes all the way to the edges of the vector field, then the axis limits are set to match exactly the vector field limits (whereas they would sometimes be off by a small floating point error previously).
    
*   if the streamplot does not reach the edges of the vector field (e.g., due to the use of `start_points` and `maxlength`), then margins expansion will not cross the vector field limits anymore.
    

This change is also used internally to ensure that polar plots don't display negative _r_ values unless the user really passes in a negative value.

### `gid` in svg output[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#gid-in-svg-output "Link to this heading")

Previously, if a figure, axis, legend or some other artists had a custom `gid` set (e.g. via `.set_gid()`), this would not be reflected in the svg output. Instead a default gid, like `figure_1` would be shown. This is now fixed, such that e.g. `fig.set_gid("myfigure")` correctly shows up as `<g id="myfigure">` in the svg file. If you relied on the gid having the default format, you now need to make sure not to set the `gid` parameter of the artists.

### Fonts[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#fonts "Link to this heading")

Font weight guessing now first checks for the presence of the FT\_STYLE\_BOLD\_FLAG before trying to match substrings in the font name. In particular, this means that Times New Roman Bold is now correctly detected as bold, not normal weight.

### Color-like checking[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#color-like-checking "Link to this heading")

[`matplotlib.colors.is_color_like`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.is_color_like.html#matplotlib.colors.is_color_like "matplotlib.colors.is_color_like")
 used to return True for all string representations of floats. However, only those with values in 0-1 are valid colors (representing grayscale values). [`is_color_like`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.is_color_like.html#matplotlib.colors.is_color_like "matplotlib.colors.is_color_like")
 now returns False for string representations of floats outside 0-1.

### Default image interpolation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#default-image-interpolation "Link to this heading")

Images displayed in Matplotlib previously used nearest-neighbor interpolation, leading to aliasing effects for downscaling and non-integer upscaling.

New default for `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`) is the new option "antialiased". `imshow(A, interpolation='antialiased')` will apply a Hanning filter when resampling the data in A for display (or saving to file) _if_ the upsample rate is less than a factor of three, and not an integer; downsampled data is always smoothed at resampling.

To get the old behavior, set `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`) to the old default "nearest" (or specify the `interpolation` kwarg of [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
)

To always get the anti-aliasing behavior, no matter what the up/down sample rate, set `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`) to "hanning" (or one of the other filters available).

Note that the "hanning" filter was chosen because it has only a modest performance penalty. Anti-aliasing can be improved with other filters.

### rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#rcparams "Link to this heading")

When using [`RendererSVG`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG "matplotlib.backends.backend_svg.RendererSVG")
 with `rcParams["svg.image_inline"] == True`, externally written images now use a single counter even if the `renderer.basename` attribute is overwritten, rather than a counter per basename.

This change will only affect you if you used `rcParams["svg.image_inline"] = True` (the default is False) _and_ manually modified `renderer.basename`.

Changed the default value of `[rcParams["axes.formatter.limits"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.limits#rcparam-axes-formatter-limits) ` (default: `[-5, 6]`) from -7, 7 to -5, 6 for better readability.

### `add_subplot()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#add-subplot "Link to this heading")

[`Figure.add_subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 and [`pyplot.subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 do not accept a _figure_ keyword argument anymore. It only used to work anyway if the passed figure was `self` or the current figure, respectively.

### `indicate_inset()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#indicate-inset "Link to this heading")

In <= 3.1.0, [`indicate_inset`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html#matplotlib.axes.Axes.indicate_inset "matplotlib.axes.Axes.indicate_inset")
 and [`indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib.axes.Axes.indicate_inset_zoom "matplotlib.axes.Axes.indicate_inset_zoom")
 were documented as returning a 4-tuple of [`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
, where in fact they returned a 4-length list.

They now correctly return a 4-tuple. [`indicate_inset`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html#matplotlib.axes.Axes.indicate_inset "matplotlib.axes.Axes.indicate_inset")
 would previously raise an error if the optional _inset\_ax_ was not supplied; it now completes successfully, and returns _None_ instead of the tuple of `ConnectionPatch`.

### PGF backend[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#pgf-backend "Link to this heading")

The pgf backend's get\_canvas\_width\_height now returns the canvas size in display units rather than in inches, which it previously did. The new behavior is the correct one given the uses of `get_canvas_width_height` in the rest of the codebase.

The pgf backend now includes images using `\includegraphics` instead of `\pgfimage` if the version of `graphicx` is recent enough to support the `interpolate` option (this is detected automatically).

### [`cbook`](https://matplotlib.org/stable/api/cbook_api.html#module-matplotlib.cbook "matplotlib.cbook")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#cbook "Link to this heading")

The default value of the "obj\_type" parameter to `cbook.warn_deprecated` has been changed from "attribute" (a default that was never used internally) to the empty string.

### Testing[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#testing "Link to this heading")

The test suite no longer turns on the Python fault handler by default. Set the standard `PYTHONFAULTHANDLER` environment variable to do so.

### Backend `supports_blit`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#backend-supports-blit "Link to this heading")

Backends do not need to explicitly define the flag `supports_blit` anymore. This is only relevant for backend developers. Backends had to define the flag `supports_blit`. This is not needed anymore because the blitting capability is now automatically detected.

### Exception changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#exception-changes "Link to this heading")

Various APIs that raised a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
 for incorrectly typed inputs now raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 instead: [`backend_bases.GraphicsContextBase.set_clip_path`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_clip_path "matplotlib.backend_bases.GraphicsContextBase.set_clip_path")
, `blocking_input.BlockingInput.__call__`, `matplotlib.cm.register_cmap`, [`dviread.DviFont`](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont "matplotlib.dviread.DviFont")
, [`rcsetup.validate_hatch`](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_hatch "matplotlib.rcsetup.validate_hatch")
, `.rcsetup.validate_animation_writer_path`, [`spines.Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
, many classes in the [`matplotlib.transforms`](https://matplotlib.org/stable/api/transformations.html#module-matplotlib.transforms "matplotlib.transforms")
 module and [`matplotlib.tri`](https://matplotlib.org/stable/api/tri_api.html#module-matplotlib.tri "matplotlib.tri")
 package, and Axes methods that take a `norm` parameter.

If extra kwargs are passed to [`LogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale "matplotlib.scale.LogScale")
, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 will now be raised instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
.

### mplot3d auto-registration[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#mplot3d-auto-registration "Link to this heading")

[`mpl_toolkits.mplot3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d "mpl_toolkits.mplot3d")
 is always registered by default now. It is no longer necessary to import mplot3d to create 3d axes with

ax \= fig.add\_subplot(111, projection\="3d")

### [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
 now has a _base_ parameter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#symlognorm-now-has-a-base-parameter "Link to this heading")

Previously, [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
 had no _base_ keyword argument and the base was hard-coded to `base=np.e`. This was inconsistent with the default behavior of [`SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
 (which defaults to `base=10`) and the use of the word "decade" in the documentation.

In preparation for changing the default base to 10, calling [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
 without the new _base_ keyword argument emits a deprecation warning.

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#id6)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`matplotlib.use`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#matplotlib-use "Link to this heading")

The `warn` parameter to [`matplotlib.use()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
 is deprecated (catch the [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "(in Python v3.14)")
 emitted on backend switch failure and reemit a warning yourself if so desired).

### plotfile[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#plotfile "Link to this heading")

`.pyplot.plotfile` is deprecated in favor of separately loading and plotting the data. Use pandas or NumPy to load data, and pandas or matplotlib to plot the resulting data.

### axes and axis[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#axes-and-axis "Link to this heading")

Setting `Axis.major.locator`, `Axis.minor.locator`, `Axis.major.formatter` or `Axis.minor.formatter` to an object that is not a subclass of [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 or [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 (respectively) is deprecated. Note that these attributes should usually be set using [`Axis.set_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
, [`Axis.set_minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
, etc. which already raise an exception when an object of the wrong class is passed.

Passing more than one positional argument or unsupported keyword arguments to [`axis()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
 is deprecated (such arguments used to be silently ignored).

### `minor` argument will become keyword-only[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#minor-argument-will-become-keyword-only "Link to this heading")

Using the parameter `minor` to `get_*ticks()` / `set_*ticks()` as a positional parameter is deprecated. It will become keyword-only in future versions.

### `axes_grid1`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#axes-grid1 "Link to this heading")

The `mpl_toolkits.axes_grid1.colorbar` module and its colorbar implementation are deprecated in favor of [`matplotlib.colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#module-matplotlib.colorbar "matplotlib.colorbar")
, as the former is essentially abandoned and the latter is a more featureful replacement with a nearly compatible API (for example, the following additional keywords are supported: `panchor`, `extendfrac`, `extendrect`).

The main differences are:

*   Setting the ticks on the colorbar is done by calling `colorbar.set_ticks` rather than `colorbar.cbar_axis.set_xticks` or `colorbar.cbar_axis.set_yticks`; the `locator` parameter to `colorbar()` is deprecated in favor of its synonym `ticks` (which already existed previously, and is consistent with [`matplotlib.colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#module-matplotlib.colorbar "matplotlib.colorbar")
    ).
    
*   The colorbar's long axis is accessed with `colorbar.xaxis` or `colorbar.yaxis` depending on the orientation, rather than `colorbar.cbar_axis`.
    
*   The default ticker is no longer `MaxNLocator(5)`, but a `_ColorbarAutoLocator`.
    
*   Overdrawing multiple colorbars on top of one another in a single Axes (e.g. when using the `cax` attribute of [`ImageGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.axes_grid.ImageGrid")
     elements) is not supported; if you previously relied on the second colorbar being drawn over the first, you can call `cax.cla()` to clear the axes before drawing the second colorbar.
    

During the deprecation period, the `mpl_toolkits.legacy_colorbar` rcParam can be set to True to use `mpl_toolkits.axes_grid1.colorbar` in [`mpl_toolkits.axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
 code with a deprecation warning (the default), or to False to use `matplotlib.colorbar`.

Passing a `pad` size of `None` (the default) as a synonym for zero to the `append_axes`, `new_horizontal` and `new_vertical` methods of [`axes_grid1.axes_divider.AxesDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 is deprecated. In a future release, the default value of `None` will mean "use `[rcParams["figure.subplot.wspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.wspace#rcparam-figure-subplot-wspace) ` (default: `0.2`) or `[rcParams["figure.subplot.hspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.hspace#rcparam-figure-subplot-hspace) ` (default: `0.2`)" (depending on the orientation). Explicitly pass `pad=0` to keep the old behavior.

### Axes3D[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#axes3d "Link to this heading")

`mplot3d.axis3d.get_flip_min_max` is deprecated.

`axes3d.unit_bbox` is deprecated (use `Bbox.unit` instead).

`axes3d.Axes3D.w_xaxis`, `.w_yaxis`, and `.w_zaxis` are deprecated (use `.xaxis`, `.yaxis`, and `.zaxis` instead).

### [`matplotlib.cm`](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#matplotlib-cm "Link to this heading")

`cm.revcmap` is deprecated. Use [`Colormap.reversed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.reversed "matplotlib.colors.Colormap.reversed")
 to reverse a colormap.

`cm.datad` no longer contains entries for reversed colormaps in their "unconverted" form.

### axisartist[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#axisartist "Link to this heading")

`mpl_toolkits.axisartist.grid_finder.GridFinderBase` is deprecated (its only use is to be inherited by the [`GridFinder`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder "mpl_toolkits.axisartist.grid_finder.GridFinder")
 class which just provides more defaults in the constructor and directly sets the transforms, so `GridFinderBase`'s methods were just moved to [`GridFinder`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder "mpl_toolkits.axisartist.grid_finder.GridFinder")
).

`axisartist.axis_artist.BezierPath` is deprecated (use [`patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 to draw arbitrary Paths).

`AxisArtist.line` is now a [`patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 instance instead of a `BezierPath` instance.

Returning a factor equal to None from axisartist Locators (which are **not** the same as "standard" tick Locators), or passing a factor equal to None to axisartist Formatters (which are **not** the same as "standard" tick Formatters) is deprecated. Pass a factor equal to 1 instead.

For the [`mpl_toolkits.axisartist.axis_artist.AttributeCopier`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AttributeCopier.html#mpl_toolkits.axisartist.axis_artist.AttributeCopier "mpl_toolkits.axisartist.axis_artist.AttributeCopier")
 class, the constructor and the `set_ref_artist` method, and the _default\_value_ parameter of `get_attribute_from_ref_artist`, are deprecated.

Deprecation of the constructor means that classes inheriting from [`AttributeCopier`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AttributeCopier.html#mpl_toolkits.axisartist.axis_artist.AttributeCopier "mpl_toolkits.axisartist.axis_artist.AttributeCopier")
 should no longer call its constructor.

### Locators[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#id1 "Link to this heading")

The unused `Locator.autoscale` method is deprecated (pass the axis limits to [`Locator.view_limits`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.view_limits "matplotlib.ticker.Locator.view_limits")
 instead).

### Animation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#animation "Link to this heading")

The following methods and attributes of the [`MovieWriterRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry "matplotlib.animation.MovieWriterRegistry")
 class are deprecated: `set_dirty`, `ensure_not_dirty`, `reset_available_writers`, `avail`.

### `smart_bounds()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#smart-bounds "Link to this heading")

The "smart\_bounds" functionality is deprecated. This includes `Axis.set_smart_bounds()`, `Axis.get_smart_bounds()`, `Spine.set_smart_bounds()`, and `Spine.get_smart_bounds()`.

### `boxplot()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#boxplot "Link to this heading")

Setting the `whis` parameter of [`Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 and [`cbook.boxplot_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
 to "range" to mean "the whole data range" is deprecated; set it to (0, 100) (which gets interpreted as percentiles) to achieve the same effect.

### `fill_between()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#fill-between "Link to this heading")

Passing scalars to parameter _where_ in `fill_between()` and `fill_betweenx()` is deprecated. While the documentation already states that _where_ must be of the same size as _x_ (or _y_), scalars were accepted and broadcasted to the size of _x_. Non-matching sizes will raise a `ValueError` in the future.

### `scatter()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#scatter "Link to this heading")

Passing the _verts_ parameter to [`axes.Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
 is deprecated; use the _marker_ parameter instead.

### `tight_layout()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#tight-layout "Link to this heading")

The `renderer` parameter to [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
 is deprecated; this method now always uses the renderer instance cached on the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

### rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#id2 "Link to this heading")

The `rcsetup.validate_animation_writer_path` function is deprecated.

Setting `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`) to "auto" is deprecated; use its synonym "png" instead.

Setting `[rcParams["text.hinting"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.hinting#rcparam-text-hinting) ` (default: `'default'`) to True or False is deprecated; use their synonyms "auto" or "none" instead.

`rcsetup.update_savefig_format` is deprecated.

`rcsetup.validate_path_exists` is deprecated (use `os.path.exists` to check whether a path exists).

`rcsetup.ValidateInterval` is deprecated.

### Dates[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#dates "Link to this heading")

`dates.mx2num` is deprecated.

### TK[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#tk "Link to this heading")

`NavigationToolbar2Tk.set_active` is deprecated, as it has no (observable) effect.

### WX[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#wx "Link to this heading")

`FigureFrameWx.statusbar` and `NavigationToolbar2Wx.statbar` are deprecated. The status bar can be retrieved by calling standard wx methods (`frame.GetStatusBar()` and `toolbar.GetTopLevelParent().GetStatusBar()`).

`backend_wx.ConfigureSubplotsWx.configure_subplots` and `backend_wx.ConfigureSubplotsWx.get_canvas` are deprecated.

### PGF[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#pgf "Link to this heading")

`backend_pgf.repl_escapetext` and `backend_pgf.repl_mathdefault` are deprecated.

`RendererPgf.latexManager` is deprecated.

### FigureCanvas[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#figurecanvas "Link to this heading")

`FigureCanvasBase.draw_cursor` (which has never done anything and has never been overridden in any backend) is deprecated.

`FigureCanvasMac.invalidate` is deprecated in favor of its synonym, `FigureCanvasMac.draw_idle`.

The `dryrun` parameter to the various `FigureCanvasFoo.print_foo` methods is deprecated.

### QuiverKey doc[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#quiverkey-doc "Link to this heading")

`quiver.QuiverKey.quiverkey_doc` is deprecated; use `quiver.QuiverKey.__init__.__doc__` instead.

### [`matplotlib.mlab`](https://matplotlib.org/stable/api/mlab_api.html#module-matplotlib.mlab "matplotlib.mlab")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#matplotlib-mlab "Link to this heading")

`mlab.apply_window` and `mlab.stride_repeat` are deprecated.

### Fonts[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#id3 "Link to this heading")

`font_manager.JSONEncoder` is deprecated. Use [`font_manager.json_dump`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.json_dump "matplotlib.font_manager.json_dump")
 to dump a [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 instance.

`font_manager.createFontList` is deprecated. [`font_manager.FontManager.addfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.addfont "matplotlib.font_manager.FontManager.addfont")
 is now available to register a font at a given path.

The `as_str`, `as_rgba_str`, `as_array`, `get_width` and `get_height` methods of `matplotlib.ft2font.FT2Image` are deprecated. Convert the `FT2Image` to a NumPy array with `np.asarray` before processing it.

### Colors[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#colors "Link to this heading")

The function `matplotlib.colors.makeMappingArray` is not considered part of the public API any longer. Thus, it's deprecated.

Using a string of single-character colors as a color sequence (e.g. "rgb") is deprecated. Use an explicit list instead.

### Scales[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#scales "Link to this heading")

Passing unsupported keyword arguments to [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
, and its subclasses [`LinearScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LinearScale "matplotlib.scale.LinearScale")
 and [`SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
, is deprecated and will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 in 3.3.

If extra keyword arguments are passed to [`LogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale "matplotlib.scale.LogScale")
, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 will now be raised instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
.

### Testing[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#id4 "Link to this heading")

The `matplotlib.testing.disable_internet` module is deprecated. Use (for example) [pytest-remotedata](https://pypi.org/project/pytest-remotedata/)
 instead.

Support in [`matplotlib.testing`](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing "matplotlib.testing")
 for nose-based tests is deprecated (a deprecation is emitted if using e.g. the decorators from that module while both 1) matplotlib's conftests have not been called and 2) nose is in `sys.modules`).

`testing.is_called_from_pytest` is deprecated.

During the deprecation period, to force the generation of nose base tests, import nose first.

The _switch\_backend\_warn_ parameter to `matplotlib.test` has no effect and is deprecated.

`testing.jpl_units.UnitDbl.UnitDbl.checkUnits` is deprecated.

### `DivergingNorm` renamed to `TwoSlopeNorm`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#divergingnorm-renamed-to-twoslopenorm "Link to this heading")

`DivergingNorm` was a misleading name; although the norm was developed with the idea that it would likely be used with diverging colormaps, the word 'diverging' does not describe or evoke the norm's mapping function. Since that function is monotonic, continuous, and piece-wise linear with two segments, the norm has been renamed to [`TwoSlopeNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm "matplotlib.colors.TwoSlopeNorm")

### Misc[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#misc "Link to this heading")

`matplotlib.get_home` is deprecated (use e.g. `os.path.expanduser("~")`) instead.

`matplotlib.compare_versions` is deprecated (use comparison of `distutils.version.LooseVersion`s instead).

`matplotlib.checkdep_ps_distiller` is deprecated.

`matplotlib.figure.AxesStack` is considered private API and will be removed from the public API in future versions.

`BboxBase.is_unit` is deprecated (check the Bbox extents if needed).

`Affine2DBase.matrix_from_values(...)` is deprecated. Use (for example) `Affine2D.from_values(...).get_matrix()` instead.

`style.core.is_style_file` and `style.core.iter_style_files` are deprecated.

### The `datapath` rcParam[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#the-datapath-rcparam "Link to this heading")

Use [`get_data_path`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_data_path "matplotlib.get_data_path")
 instead. (The rcParam is deprecated because it cannot be meaningfully set by an end user.) The rcParam had no effect from 3.2.0, but was deprecated only in 3.2.1. In 3.2.1+ if `'datapath'` is set in a `matplotlibrc` file it will be respected, but this behavior will be removed in 3.3.

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#id7)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `matplotlib.testing.determinism` module, which exposes no public API, has been deleted.

The following API elements have been removed:

*   `backend_gtk3.PIXELS_PER_INCH`
    
*   `backend_pgf.re_escapetext`, `backend_pgf.re_mathdefault`.
    
*   the `matplotlib.backends.tkagg`, `matplotlib.backends.windowing`, `matplotlib.backends.wx_compat`, and `matplotlib.compat.subprocess` modules
    
*   `RcParams.msg_depr`, `RcParams.msg_depr_ignore`, `RcParams.msg_depr_set`, `RcParams.msg_obsolete`, `RcParams.msg_backend_obsolete`
    
*   `afm.parse_afm` (use `afm.AFM instead`)
    
*   `axes.Axes.mouseover_set`
    
*   `backend_cairo.ArrayWrapper`, `backend_cairo.RendererCairo.convert_path`
    
*   `backend_gtk3.FileChooserDialog.sorted_filetypes` (use `sorted(self.filetypes.items())` instead)
    
*   `backend_pgf.get_texcommand`
    
*   `backend_pdf.PdfFile.texFontMap`
    
*   `backend_ps.get_bbox`
    
*   `backend_qt.FigureCanvasQt.keyAutoRepeat` (use `event.guiEvent.isAutoRepeat` instead), `backend_qt.error_msg_qt`, `backend_qt.exception_handler`
    
*   `backend_wx.FigureCanvasWx.macros`
    
*   `backends.pylab_setup`
    
*   `cbook.Bunch` (use `types.SimpleNamespace` instead), `cbook.Locked`, `cbook.unicode_safe`, `cbook.is_numlike` (use `isinstance(..., numbers.Number)` instead), `cbook.mkdirs` (use `os.makedirs(..., exist_ok=True)` instead), `cbook.GetRealpathAndStat` (use `cbook.get_realpath_and_stat` instead), `cbook.listFiles`
    
*   `container.Container.set_remove_method`
    
*   `contour.ContourLabeler.cl`, `contour.ContourLabeler.cl_xy`, `contour.ContourLabeler.cl_cvalues` (use `labelTexts`, `labelXYs`, `labelCValues` instead)
    
*   `dates.DateFormatter.strftime`, `dates.DateFormatter.strftime_pre_1900`
    
*   `font_manager.TempCache`, `font_manager.FontManager.ttffiles`, `font_manager.FontManager.afmfiles`
    
*   `mathtext.unichr_safe` (use `chr` instead)
    
*   `patches.YAArrow` (use `patches.FancyArrowPatch` instead)
    
*   `sphinxext.plot_directive.remove_coding`
    
*   `table.Table.get_child_artists`
    
*   `testing.compare.compare_float`, `testing.decorators.CleanupTest`, `testing.decorators.ImageComparisonTest`, `testing.decorators.skip_if_command_unavailable`, support for nose-based tests
    
*   `text.Annotation.arrow` (use `text.Annotation.arrow_patch` instead)
    
*   `textpath.TextToPath.tex_font_map`
    
*   `ticker.Base`, `ticker.closeto`, `ticker.nearest_long`
    
*   `axes_grid1.axes_divider.LocatableAxesBase`, `axes_grid1.axes_divider.locatable_axes_factory`, `axes_grid1.axes_divider.Axes` (use `axes_grid1.mpl_axes.Axes` instead), `axes_grid1.axes_divider.LocatableAxes` (use `axes_grid1.mpl_axes.Axes` instead)
    
*   `axisartist.axes_divider.Axes`, `axisartist.axes_divider.LocatableAxes` (use `axisartist.axislines.Axes` instead)
    
*   the _normed_ keyword argument to `hist` (use _density_ instead)
    
*   passing `(verts, 0)` or `(..., 3)` when specifying a marker to specify a path or a circle, respectively (instead, use `verts` or `"o"`, respectively)
    
*   the `examples.directory` rcParam
    

The following members of `matplotlib.backends.backend_pdf.PdfFile` were removed:

*   `nextObject`
    
*   `nextFont`
    
*   `nextAlphaState`
    
*   `nextHatch`
    
*   `nextImage`
    
*   `alphaStateObject`
    

The `required_interactive_framework` attribute of backend modules introduced in Matplotlib 3.0 has been moved to the `FigureCanvas` class, in order to let it be inherited by third-party canvas subclasses and to make it easier to know what interactive framework is required by a canvas class.

`backend_qt4.FigureCanvasQT5`, which is an alias for `backend_qt5.FigureCanvasQT` (but only exists under that name in `backend_qt4`), has been removed.

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#id8)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#development-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows build[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#windows-build "Link to this heading")

Previously, when building the `matplotlib._png` extension, the build script would add "png" and "z" to the extensions `.libraries` attribute (if pkg-config information is not available, which is in particular the case on Windows).

In particular, this implies that the Windows build would look up files named `png.lib` and `z.lib`; but neither libpng upstream nor zlib upstream provides these files by default. (On Linux, this would look up `libpng.so` and `libz.so`, which are indeed standard names.)

Instead, on Windows, we now look up `libpng16.lib` and `zlib.lib`, which _are_ the upstream names for the shared libraries (as of libpng 1.6.x).

For a statically-linked build, the upstream names are `libpng16_static.lib` and `zlibstatic.lib`; one still needs to manually rename them if such a build is desired.

### Packaging DLLs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#packaging-dlls "Link to this heading")

Previously, it was possible to package Windows DLLs into the Matplotlib wheel (or sdist) by copying them into the source tree and setting the `package_data.dlls` entry in `setup.cfg`.

DLLs copied in the source tree are now always packaged; the `package_data.dlls` entry has no effect anymore. If you do not want to include the DLLs, don't copy them into the source tree.

On this page
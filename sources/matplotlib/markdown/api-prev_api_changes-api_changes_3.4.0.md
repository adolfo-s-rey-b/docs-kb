[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#main-content)

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
    

API Changes for 3.4.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#api-changes-for-3-4-0 "Link to this heading")

=================================================================================================================================================

[Behaviour changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#id2)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#behaviour-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Constrained layout rewrite[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#constrained-layout-rewrite "Link to this heading")

The layout manager `constrained_layout` was re-written with different outer constraints that should be more robust to complicated subplot layouts. User-facing changes are:

*   some poorly constrained layouts will have different width/height plots than before.
    
*   colorbars now respect the `anchor` keyword argument of [`matplotlib.colorbar.make_axes`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes "matplotlib.colorbar.make_axes")
    
*   colorbars are wider.
    
*   colorbars in different rows or columns line up more robustly.
    
*   _hspace_ and _wspace_ options to [`Figure.set_constrained_layout_pads`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout_pads.html#matplotlib.figure.Figure.set_constrained_layout_pads "matplotlib.figure.Figure.set_constrained_layout_pads")
     were twice as wide as the docs said they should be. So these now follow the docs.
    

This feature will remain "experimental" until the new changes have been used enough by users, so we anticipate version 3.5 or 3.6. On the other hand, `constrained_layout` is extensively tested and used in examples in the library, so using it should be safe, but layouts may not be exactly the same as more development takes place.

Details of using `constrained_layout`, and its algorithm are available at [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)

### `plt.subplot` re-selection without keyword arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#plt-subplot-re-selection-without-keyword-arguments "Link to this heading")

The purpose of [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 is to facilitate creating and re-selecting Axes in a Figure when working strictly in the implicit pyplot API. When creating new Axes it is possible to select the projection (e.g. polar, 3D, or various cartographic projections) as well as to pass additional keyword arguments through to the Axes-subclass that is created.

The first time [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 is called for a given position in the Axes grid it always creates and returns a new Axes with the passed arguments and projection (defaulting to rectilinear). On subsequent calls to [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 we have to determine if an existing Axes has a) equivalent parameters, in which case it should be selected as the current Axes and returned, or b) different parameters, in which case a new Axes is created and the existing Axes is removed. This leaves the question of what is "equivalent parameters".

Previously it was the case that an existing Axes subclass, except for Axes3D, would be considered equivalent to a 2D rectilinear Axes, despite having different projections, if the keyword arguments (other than _projection_) matched. Thus:

ax1 \= plt.subplot(1, 1, 1, projection\='polar')
ax2 \=  plt.subplots(1, 1, 1)
ax1 is ax2

We are embracing this long standing behavior to ensure that in the case when no keyword arguments (of any sort) are passed to [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 any existing Axes is returned, without consideration for keywords or projection used to initially create it. This will cause a change in behavior when additional keywords were passed to the original Axes:

ax1 \= plt.subplot(111, projection\='polar', theta\_offset\=.75)
ax2 \= plt.subplots(1, 1, 1)
ax1 is ax2         \# new behavior
\# ax1 is not ax2   # old behavior, made a new axes

ax1 \= plt.subplot(111, label\='test')
ax2 \= plt.subplots(1, 1, 1)
ax1 is ax2         \# new behavior
\# ax1 is not ax2   # old behavior, made a new axes

For the same reason, if there was an existing Axes that was not rectilinear, passing `projection='rectilinear'` would reuse the existing Axes

ax1 \= plt.subplot(projection\='polar')
ax2 \= plt.subplot(projection\='rectilinear')
ax1 is not ax2     \# new behavior, makes new Axes
\# ax1 is ax2       # old behavior

contrary to the user's request.

Previously Axes3D could not be re-selected with [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 due to an unrelated bug (also fixed in Matplotlib 3.4). While Axes3D are now consistent with all other projections there is a change in behavior for

plt.subplot(projection\='3d')  \# create a 3D Axes

plt.subplot()                 \# now returns existing 3D Axes, but
                              \# previously created new 2D Axes

plt.subplot(projection\='rectilinear')  \# to get a new 2D Axes

### `ioff` and `ion` can be used as context managers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#ioff-and-ion-can-be-used-as-context-managers "Link to this heading")

[`pyplot.ion`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib.pyplot.ion "matplotlib.pyplot.ion")
 and [`pyplot.ioff`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ioff.html#matplotlib.pyplot.ioff "matplotlib.pyplot.ioff")
 may now be used as context managers to create a context with interactive mode on or off, respectively. The old behavior of calling these functions is maintained. To use the new functionality call as:

with plt.ioff():
   \# non-interactive code

### Locators and formatters must be in the class hierarchy[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#locators-and-formatters-must-be-in-the-class-hierarchy "Link to this heading")

Axis locators and formatters must now be subclasses of [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 and [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 respectively.

### Date locator for DAILY interval now returns middle of month[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#date-locator-for-daily-interval-now-returns-middle-of-month "Link to this heading")

The [`matplotlib.dates.AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
 has a default of `interval_multiples=True` that attempts to align ticks with the start of meaningful intervals like the start of the month, or start of the day, etc. That lead to approximately 140-day intervals being mapped to the first and 22nd of the month. This has now been changed so that it chooses the first and 15th of the month, which is probably what most people want.

### `ScalarFormatter` _useLocale_ option obeys grouping[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#scalarformatter-uselocale-option-obeys-grouping "Link to this heading")

When the [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 option _useLocale_ is enabled (or `[rcParams["axes.formatter.use_locale"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_locale#rcparam-axes-formatter-use-locale) ` (default: `False`) is _True_) and the configured locale uses grouping, a separator will be added as described in [`locale.format_string`](https://docs.python.org/3/library/locale.html#locale.format_string "(in Python v3.14)")
.

### `Axes.errorbar` cycles non-color properties correctly[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#axes-errorbar-cycles-non-color-properties-correctly "Link to this heading")

Formerly, [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 incorrectly skipped the Axes property cycle if a color was explicitly specified, even if the property cycler was for other properties (such as line style). Now, [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 will advance the Axes property cycle as done for [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
, i.e., as long as all properties in the cycler are not explicitly passed.

### pyplot.specgram always uses origin='upper'[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#pyplot-specgram-always-uses-origin-upper "Link to this heading")

Previously if `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`) was set to something other than `'upper'` or if the _origin_ keyword argument was passed with a value other than `'upper'`, the spectrogram itself would flip, but the Axes would remain oriented for an origin value of `'upper'`, so that the resulting plot was incorrectly labelled.

Now, the _origin_ keyword argument is not supported and the `image.origin` rcParam is ignored. The function [`matplotlib.pyplot.specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram "matplotlib.pyplot.specgram")
 is forced to use `origin='upper'`, so that the Axes are correct for the plotted spectrogram.

### xunits=None and yunits=None passed as keyword arguments are treated as "no action"[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#xunits-none-and-yunits-none-passed-as-keyword-arguments-are-treated-as-no-action "Link to this heading")

Many (but not all) of the methods on [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 take the (undocumented) keyword arguments _xunits_ and _yunits_ that will update the units on the given Axis by calling [`Axis.set_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units")
 and [`Axis.update_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.update_units.html#matplotlib.axis.Axis.update_units "matplotlib.axis.Axis.update_units")
.

Previously if _None_ was passed it would clear the value stored in `.Axis.units` which will in turn break converters which rely on the value in `.Axis.units` to work properly (notably [`StrCategoryConverter`](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryConverter "matplotlib.category.StrCategoryConverter")
).

This changes the semantics of `ax.meth(..., xunits=None, yunits=None)` from "please clear the units" to "do the default thing as if they had not been passed" which is consistent with the standard behavior of Matplotlib keyword arguments.

If you were relying on passing `xunits=None` to plotting methods to clear the `.Axes.units` attribute, directly call [`Axis.set_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units")
 (and [`Axis.update_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.update_units.html#matplotlib.axis.Axis.update_units "matplotlib.axis.Axis.update_units")
 if you also require the converter to be updated).

### Annotations with `annotation_clip` no longer affect `tight_layout`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#annotations-with-annotation-clip-no-longer-affect-tight-layout "Link to this heading")

Previously, [`text.Annotation.get_tightbbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.get_tightbbox "matplotlib.text.Annotation.get_tightbbox")
 always returned the full [`text.Annotation.get_window_extent`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.get_window_extent "matplotlib.text.Annotation.get_window_extent")
 of the object, independent of the value of `annotation_clip`. [`text.Annotation.get_tightbbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.get_tightbbox "matplotlib.text.Annotation.get_tightbbox")
 now correctly takes this extra clipping box into account, meaning that [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
s that are not drawn because of `annotation_clip` will not count towards the Axes bounding box calculations, such as those done by [`tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
.

This is now consistent with the API described in [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, which specifies that `get_window_extent` should return the full extents and `get_tightbbox` should "account for any clipping".

### Parasite Axes pcolor and pcolormesh now defaults to placing grid edges at integers, not half-integers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#parasite-axes-pcolor-and-pcolormesh-now-defaults-to-placing-grid-edges-at-integers-not-half-integers "Link to this heading")

This is consistent with [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 and [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
.

### `Colorbar` outline is now a `Spine`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#colorbar-outline-is-now-a-spine "Link to this heading")

The outline of [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 is now a [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
 and drawn as one, instead of a [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 drawn as an artist. This ensures it will always be drawn after (i.e., on top of) all artists, consistent with Spines on normal Axes.

### `Colorbar.dividers` changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#colorbar-dividers-changes "Link to this heading")

This attribute is now always a [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 -- an empty one if `drawedges` is _False_. Its default colors and linewidth (`[rcParams["axes.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.edgecolor#rcparam-axes-edgecolor) ` (default: `'black'`), `[rcParams["axes.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.linewidth#rcparam-axes-linewidth) ` (default: `0.8`)) are now resolved at instantiation time, not at draw time.

### Raise or warn on registering a colormap twice[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#raise-or-warn-on-registering-a-colormap-twice "Link to this heading")

When using `matplotlib.cm.register_cmap` to register a user provided or third-party colormap it will now raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
 if trying to over-write one of the built in colormaps and warn if trying to over write a user registered colormap. This may raise for user-registered colormaps in the future.

### Consecutive rasterized draws now merged[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#consecutive-rasterized-draws-now-merged "Link to this heading")

Tracking of depth of raster draws has moved from [`backend_mixed.MixedModeRenderer.start_rasterizing`](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer.start_rasterizing "matplotlib.backends.backend_mixed.MixedModeRenderer.start_rasterizing")
 and [`backend_mixed.MixedModeRenderer.stop_rasterizing`](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer.stop_rasterizing "matplotlib.backends.backend_mixed.MixedModeRenderer.stop_rasterizing")
 into [`artist.allow_rasterization`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.allow_rasterization.html#matplotlib.artist.allow_rasterization "matplotlib.artist.allow_rasterization")
. This means the start and stop functions are only called when the rasterization actually needs to be started and stopped.

The output of vector backends will change in the case that rasterized elements are merged. This should not change the appearance of outputs.

The renders in 3rd party backends are now expected to have `self._raster_depth` and `self._rasterizing` initialized to `0` and _False_ respectively.

### Consistent behavior of `draw_if_interactive()` across backends[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#consistent-behavior-of-draw-if-interactive-across-backends "Link to this heading")

[`pyplot.draw_if_interactive`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw_if_interactive.html#matplotlib.pyplot.draw_if_interactive "matplotlib.pyplot.draw_if_interactive")
 no longer shows the window (if it was previously unshown) on the Tk and nbAgg backends, consistently with all other backends.

### The Artist property _rasterized_ cannot be _None_ anymore[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#the-artist-property-rasterized-cannot-be-none-anymore "Link to this heading")

It is now a boolean only. Before the default was _None_ and [`Artist.set_rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized")
 was documented to accept _None_. However, _None_ did not have a special meaning and was treated as _False_.

### Canvas's callback registry now stored on Figure[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#canvas-s-callback-registry-now-stored-on-figure "Link to this heading")

The canonical location of the [`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
 used to handle Figure/Canvas events has been moved from the Canvas to the Figure. This change should be transparent to almost all users, however if you are swapping switching the Figure out from on top of a Canvas or visa versa you may see a change in behavior.

### Harmonized key event data across backends[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#harmonized-key-event-data-across-backends "Link to this heading")

The different backends with key translation support, now handle "Shift" as a sometimes modifier, where the `'shift+'` prefix won't be added if a key translation was made.

In the Qt5 backend, the `matplotlib.backends.backend_qt5.SPECIAL_KEYS` dictionary contains keys that do _not_ return their unicode name instead they have manually specified names. The name for `QtCore.Qt.Key_Meta` has changed to `'meta'` to be consistent with the other GUI backends.

The WebAgg backend now handles key translations correctly on non-US keyboard layouts.

In the GTK and Tk backends, the handling of non-ASCII keypresses (as reported in the KeyEvent passed to `key_press_event`\-handlers) now correctly reports Unicode characters (e.g., €), and better respects NumLock on the numpad.

In the GTK and Tk backends, the following key names have changed; the new names are consistent with those reported by the Qt backends:

*   The "Break/Pause" key (keysym 0xff13) is now reported as `"pause"` instead of `"break"` (this is also consistent with the X key name).
    
*   The numpad "delete" key is now reported as `"delete"` instead of `"dec"`.
    

### WebAgg backend no longer reports a middle click as a right click[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#webagg-backend-no-longer-reports-a-middle-click-as-a-right-click "Link to this heading")

Previously when using the WebAgg backend the event passed to a callback by `fig.canvas.mpl_connect('mouse_button_event', callback)` on a middle click would report [`MouseButton.RIGHT`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.RIGHT "matplotlib.backend_bases.MouseButton.RIGHT")
 instead of [`MouseButton.MIDDLE`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.MIDDLE "matplotlib.backend_bases.MouseButton.MIDDLE")
.

### ID attribute of XML tags in SVG files now based on SHA256 rather than MD5[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#id-attribute-of-xml-tags-in-svg-files-now-based-on-sha256-rather-than-md5 "Link to this heading")

Matplotlib generates unique ID attributes for various tags in SVG files. Matplotlib previously generated these unique IDs using the first 10 characters of an MD5 hash. The MD5 hashing algorithm is not available in Python on systems with Federal Information Processing Standards (FIPS) enabled. Matplotlib now uses the first 10 characters of an SHA256 hash instead. SVG files that would otherwise match those saved with earlier versions of matplotlib, will have different ID attributes.

### `RendererPS.set_font` is no longer a no-op in AFM mode[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#rendererps-set-font-is-no-longer-a-no-op-in-afm-mode "Link to this heading")

[`RendererPS.set_font`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.set_font "matplotlib.backends.backend_ps.RendererPS.set_font")
 now sets the current PostScript font in all cases.

### Autoscaling in Axes3D[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#autoscaling-in-axes3d "Link to this heading")

In Matplotlib 3.2.0, autoscaling was made lazier for 2D Axes, i.e., limits would only be recomputed when actually rendering the canvas, or when the user queries the Axes limits. This performance improvement is now extended to [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
. This also fixes some issues with autoscaling being triggered unexpectedly in Axes3D.

Please see [the API change for 2D Axes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.2.0.html#api-changes-3-2-0-autoscaling)
 for further details.

### Axes3D automatically adding itself to Figure is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#axes3d-automatically-adding-itself-to-figure-is-deprecated "Link to this heading")

New [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 objects previously added themselves to figures when they were created, unlike all other Axes classes, which lead to them being added twice if `fig.add_subplot(111, projection='3d')` was called.

This behavior is now deprecated and will warn. The new keyword argument _auto\_add\_to\_figure_ controls the behavior and can be used to suppress the warning. The default value will change to _False_ in Matplotlib 3.5, and any non-_False_ value will be an error in Matplotlib 3.6.

In the future, [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 will need to be explicitly added to the figure

fig \= Figure()
\# create Axes3D
ax \= Axes3d(fig)
\# add to Figure
fig.add\_axes(ax)

as needs to be done for other [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 sub-classes. Or, a 3D projection can be made via:

fig.add\_subplot(projection\='3d')

### `mplot3d.art3d.get_dir_vector` always returns NumPy arrays[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#mplot3d-art3d-get-dir-vector-always-returns-numpy-arrays "Link to this heading")

For consistency, [`get_dir_vector`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl_toolkits.mplot3d.art3d.get_dir_vector "mpl_toolkits.mplot3d.art3d.get_dir_vector")
 now always returns NumPy arrays, even if the input is a 3-element iterable.

### Changed cursive and fantasy font definitions[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#changed-cursive-and-fantasy-font-definitions "Link to this heading")

The Comic Sans and Comic Neue fonts were moved from the default `[rcParams["font.fantasy"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.fantasy#rcparam-font-fantasy) ` (default: `['Chicago', 'Charcoal', 'Impact', 'Western', 'xkcd script', 'fantasy']`) list to the default `[rcParams["font.cursive"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.cursive#rcparam-font-cursive) ` (default: `['Apple Chancery', 'Textile', 'Zapf Chancery', 'Sand', 'Script MT', 'Felipa', 'Comic Neue', 'Comic Sans MS', 'cursive']`) setting, in accordance with the CSS font families [example](https://www.w3.org/Style/Examples/007/fonts.en.html)
 and in order to provide a cursive font present in Microsoft's Core Fonts set.

### docstring.Substitution now always dedents docstrings before string interpolation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#docstring-substitution-now-always-dedents-docstrings-before-string-interpolation "Link to this heading")

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#id3)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Extra parameters to Axes constructor[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#extra-parameters-to-axes-constructor "Link to this heading")

Parameters of the Axes constructor other than _fig_ and _rect_ will become keyword-only in a future version.

### `pyplot.gca` and `Figure.gca` keyword arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#pyplot-gca-and-figure-gca-keyword-arguments "Link to this heading")

Passing keyword arguments to [`pyplot.gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
 or [`figure.Figure.gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#matplotlib.figure.Figure.gca "matplotlib.figure.Figure.gca")
 will not be supported in a future release.

### `Axis.cla`, `RadialAxis.cla`, `ThetaAxis.cla` and `Spine.cla`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#axis-cla-radialaxis-cla-thetaaxis-cla-and-spine-cla "Link to this heading")

These methods are deprecated in favor of the respective `clear()` methods.

### Invalid hatch pattern characters are no longer ignored[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#invalid-hatch-pattern-characters-are-no-longer-ignored "Link to this heading")

When specifying hatching patterns, characters that are not recognized will raise a deprecation warning. In the future, this will become a hard error.

### `imread` reading from URLs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#imread-reading-from-urls "Link to this heading")

Passing a URL to [`imread()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread "matplotlib.pyplot.imread")
 is deprecated. Please open the URL for reading and directly use the Pillow API (`PIL.Image.open(urllib.request.urlopen(url))`, or `PIL.Image.open(io.BytesIO(requests.get(url).content))`) instead.

### Subplot-related attributes and methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#subplot-related-attributes-and-methods "Link to this heading")

Some `SubplotBase` methods and attributes have been deprecated and/or moved to [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
:

*   `get_geometry` (use `SubplotBase.get_subplotspec` instead),
    
*   `change_geometry` (use `SubplotBase.set_subplotspec` instead),
    
*   `is_first_row`, `is_last_row`, `is_first_col`, `is_last_col` (use the corresponding methods on the [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
     instance instead),
    
*   `update_params` (now a no-op),
    
*   `figbox` (use `ax.get_subplotspec().get_geometry(ax.figure)` instead to recompute the geometry, or `ax.get_position()` to read its current value),
    
*   `numRows`, `numCols` (use the `nrows` and `ncols` attribute on the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
     instead).
    

Likewise, the `get_geometry`, `change_geometry`, `update_params`, and `figbox` methods/attributes of [`SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")
 have been deprecated, with similar replacements.

### `is_url` and `URL_REGEX`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#is-url-and-url-regex "Link to this heading")

... are deprecated. (They were previously defined in the toplevel [`matplotlib`](https://matplotlib.org/stable/index.html#module-matplotlib "matplotlib")
 module.)

### `matplotlib.style.core` deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#matplotlib-style-core-deprecations "Link to this heading")

`STYLE_FILE_PATTERN`, `load_base_library`, and `iter_user_libraries` are deprecated.

### `dpi_cor` property of [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#dpi-cor-property-of-fancyarrowpatch "Link to this heading")

This parameter is considered internal and deprecated.

### Passing `boxstyle="custom", bbox_transmuter=...` to `FancyBboxPatch`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#passing-boxstyle-custom-bbox-transmuter-to-fancybboxpatch "Link to this heading")

In order to use a custom boxstyle, directly pass it as the _boxstyle_ argument to [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
. This was previously already possible, and is consistent with custom arrow styles and connection styles.

### BoxStyles are now called without passing the _mutation\_aspect_ parameter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#boxstyles-are-now-called-without-passing-the-mutation-aspect-parameter "Link to this heading")

Mutation aspect is now handled by the artist itself. Hence the _mutation\_aspect_ parameter of `BoxStyle._Base.__call__` is deprecated, and custom boxstyles should be implemented to not require this parameter (it can be left as a parameter defaulting to 1 for back-compatibility).

### `ContourLabeler.get_label_coords` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#contourlabeler-get-label-coords-is-deprecated "Link to this heading")

It is considered an internal helper.

### Line2D and Patch no longer duplicate `validJoin` and `validCap`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#line2d-and-patch-no-longer-duplicate-validjoin-and-validcap "Link to this heading")

Validation of joinstyle and capstyles is now centralized in `rcsetup`.

### Setting a Line2D's pickradius via `set_picker` is undeprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#setting-a-line2d-s-pickradius-via-set-picker-is-undeprecated "Link to this heading")

This cancels the deprecation introduced in Matplotlib 3.3.0.

### `MarkerStyle` is considered immutable[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#markerstyle-is-considered-immutable "Link to this heading")

`MarkerStyle.set_fillstyle()` and `MarkerStyle.set_marker()` are deprecated. Create a new `MarkerStyle` with the respective parameters instead.

### `MovieWriter.cleanup` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#moviewriter-cleanup-is-deprecated "Link to this heading")

Cleanup logic is now fully implemented in [`MovieWriter.finish`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter.finish "matplotlib.animation.MovieWriter.finish")
. Third-party movie writers should likewise move the relevant cleanup logic there, as overridden `cleanup`s will no longer be called in the future.

### _minimumdescent_ parameter/property of `TextArea`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#minimumdescent-parameter-property-of-textarea "Link to this heading")

[`offsetbox.TextArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
 has behaved as if _minimumdescent_ was always True (regardless of the value to which it was set) since Matplotlib 1.3, so the parameter/property is deprecated.

### `colorbar` now warns when the mappable's Axes is different from the current Axes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#colorbar-now-warns-when-the-mappable-s-axes-is-different-from-the-current-axes "Link to this heading")

Currently, [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 and [`pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
 steal space by default from the current Axes to place the colorbar. In a future version, they will steal space from the mappable's Axes instead. In preparation for this change, [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 and [`pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
 now emits a warning when the current Axes is not the same as the mappable's Axes.

### Colorbar docstrings[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#colorbar-docstrings "Link to this heading")

The following globals in [`matplotlib.colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#module-matplotlib.colorbar "matplotlib.colorbar")
 are deprecated: `colorbar_doc`, `colormap_kw_doc`, `make_axes_kw_doc`.

### `ColorbarPatch` and `colorbar_factory` are deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#colorbarpatch-and-colorbar-factory-are-deprecated "Link to this heading")

All the relevant functionality has been moved to the [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 class.

### Backend deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#backend-deprecations "Link to this heading")

*   `FigureCanvasBase.get_window_title` and `FigureCanvasBase.set_window_title` are deprecated. Use the corresponding methods on the FigureManager if using pyplot, or GUI-specific methods if embedding.
    
*   The _resize\_callback_ parameter to `FigureCanvasTk` was never used internally and is deprecated. Tk-level custom event handlers for resize events can be added to a `FigureCanvasTk` using e.g. `get_tk_widget().bind('<Configure>', ..., True)`.
    
*   The `key_press` and `button_press` methods of [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")
    , which incorrectly did nothing when using `toolmanager`, are deprecated in favor of directly passing the event to the [`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
     via `self.canvas.callbacks.process(event.name, event)`.
    
*   `RendererAgg.get_content_extents` and `RendererAgg.tostring_rgba_minimized` are deprecated.
    
*   `backend_pgf.TmpDirCleaner` is deprecated, with no replacement.
    
*   `GraphicsContextPS` is deprecated. The PostScript backend now uses [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
    .
    

### wx backend cleanups[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#wx-backend-cleanups "Link to this heading")

The _origin_ parameter to `_FigureCanvasWxBase.gui_repaint` is deprecated with no replacement; `gui_repaint` now automatically detects the case where it is used with the wx renderer.

The `NavigationToolbar2Wx.get_canvas` method is deprecated; directly instantiate a canvas (`FigureCanvasWxAgg(frame, -1, figure)`) if needed.

### Unused positional parameters to `print_<fmt>` methods are deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#unused-positional-parameters-to-print-fmt-methods-are-deprecated "Link to this heading")

None of the `print_<fmt>` methods implemented by canvas subclasses used positional arguments other that the first (the output filename or file-like), so these extra parameters are deprecated.

### The _dpi_ parameter of `FigureCanvas.print_foo` printers is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#the-dpi-parameter-of-figurecanvas-print-foo-printers-is-deprecated "Link to this heading")

The [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 machinery already took care of setting the figure DPI to the desired value, so `print_foo` can directly read it from there. Not passing _dpi_ to `print_foo` allows clearer detection of unused parameters passed to [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

### Passing [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")
 to `FT2Font.set_text`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#passing-bytes-to-ft2font-set-text "Link to this heading")

... is deprecated, pass [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 instead.

### `ps.useafm` deprecated for mathtext[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#ps-useafm-deprecated-for-mathtext "Link to this heading")

Outputting mathtext using only standard PostScript fonts has likely been broken for a while (issue [#18722](https://github.com/matplotlib/matplotlib/issues/18722)
). In Matplotlib 3.5, the setting `[rcParams["ps.useafm"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ps.useafm#rcparam-ps-useafm) ` (default: `False`) will have no effect on mathtext.

### `MathTextParser("bitmap")` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#mathtextparser-bitmap-is-deprecated "Link to this heading")

The associated APIs `MathtextBackendBitmap`, `MathTextParser.to_mask`, `MathTextParser.to_rgba`, `MathTextParser.to_png`, and `MathTextParser.get_depth` are likewise deprecated.

To convert a text string to an image, either directly draw the text to an empty [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 and save the figure using a tight bbox, as demonstrated in [Convert texts to images](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_asarray.html)
, or use [`mathtext.math_to_image`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.math_to_image "matplotlib.mathtext.math_to_image")
.

When using [`math_to_image`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.math_to_image "matplotlib.mathtext.math_to_image")
, text color can be set with e.g.:

with plt.rc\_context({"text.color": "tab:blue"}):
    mathtext.math\_to\_image(text, filename)

and an RGBA array can be obtained with e.g.:

from io import BytesIO
buf \= BytesIO()
mathtext.math\_to\_image(text, buf, format\="png")
buf.seek(0)
rgba \= plt.imread(buf)

### Deprecation of mathtext internals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#deprecation-of-mathtext-internals "Link to this heading")

The following API elements previously exposed by the [`mathtext`](https://matplotlib.org/stable/api/mathtext_api.html#module-matplotlib.mathtext "matplotlib.mathtext")
 module are considered to be implementation details and public access to them is deprecated:

*   `Fonts` and all its subclasses,
    
*   `FontConstantsBase` and all its subclasses,
    
*   `Node` and all its subclasses,
    
*   `Ship`, `ship`,
    
*   `Error`,
    
*   `Parser`,
    
*   `SHRINK_FACTOR`, `GROW_FACTOR`,
    
*   `NUM_SIZE_LEVELS`,
    
*   `latex_to_bakoma`, `latex_to_cmex`, `latex_to_standard`,
    
*   `stix_virtual_fonts`,
    
*   `tex2uni`.
    

### Deprecation of various mathtext helpers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#deprecation-of-various-mathtext-helpers "Link to this heading")

The `MathtextBackendPdf`, `MathtextBackendPs`, `MathtextBackendSvg`, and `MathtextBackendCairo` classes from the [`mathtext`](https://matplotlib.org/stable/api/mathtext_api.html#module-matplotlib.mathtext "matplotlib.mathtext")
 module, as well as the corresponding `.mathtext_parser` attributes on `RendererPdf`, `RendererPS`, `RendererSVG`, and `RendererCairo`, are deprecated. The `MathtextBackendPath` class can be used to obtain a list of glyphs and rectangles in a mathtext expression, and renderer-specific logic should be directly implemented in the renderer.

`StandardPsFonts.pswriter` is unused and deprecated.

### Widget class internals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#widget-class-internals "Link to this heading")

Several [`widgets.Widget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Widget.html#matplotlib.widgets.Widget "matplotlib.widgets.Widget")
 class internals have been privatized and deprecated:

*   `AxesWidget.cids`
    
*   `Button.cnt` and `Button.observers`
    
*   `CheckButtons.cnt` and `CheckButtons.observers`
    
*   `RadioButtons.cnt` and `RadioButtons.observers`
    
*   `Slider.cnt` and `Slider.observers`
    
*   `TextBox.cnt`, `TextBox.change_observers` and `TextBox.submit_observers`
    

### 3D properties on renderers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#d-properties-on-renderers "Link to this heading")

The properties of the 3D Axes that were placed on the Renderer during draw are now deprecated:

*   `renderer.M`
    
*   `renderer.eye`
    
*   `renderer.vvec`
    
*   `renderer.get_axis_position`
    

These attributes are all available via [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
, which can be accessed via `self.axes` on all [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s.

### _renderer_ argument of `do_3d_projection` method for `Collection3D`/`Patch3D`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#renderer-argument-of-do-3d-projection-method-for-collection3d-patch3d "Link to this heading")

The _renderer_ argument for the `do_3d_projection` method on `Collection3D` and `Patch3D` is no longer necessary, and passing it during draw is deprecated.

### _project_ argument of `draw` method for `Line3DCollection`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#project-argument-of-draw-method-for-line3dcollection "Link to this heading")

The _project_ argument for the `draw` method on `Line3DCollection` is deprecated. Call [`Line3DCollection.do_3d_projection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection.do_3d_projection "mpl_toolkits.mplot3d.art3d.Line3DCollection.do_3d_projection")
 explicitly instead.

### Extra positional parameters to `plot_surface` and `plot_wireframe`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#extra-positional-parameters-to-plot-surface-and-plot-wireframe "Link to this heading")

Positional parameters to [`plot_surface`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface")
 and [`plot_wireframe`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe")
 other than `X`, `Y`, and `Z` are deprecated. Pass additional artist properties as keyword arguments instead.

### `ParasiteAxesAuxTransBase` class[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#parasiteaxesauxtransbase-class "Link to this heading")

The functionality of that mixin class has been moved to the base `ParasiteAxesBase` class. Thus, `ParasiteAxesAuxTransBase`, `ParasiteAxesAuxTrans`, and `parasite_axes_auxtrans_class_factory` are deprecated.

In general, it is suggested to use `HostAxes.get_aux_axes` to create parasite Axes, as this saves the need of manually appending the parasite to `host.parasites` and makes sure that their `remove()` method works properly.

### `AxisArtist.ZORDER` attribute[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#axisartist-zorder-attribute "Link to this heading")

Use `AxisArtist.zorder` instead.

### `GridHelperBase` invalidation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#gridhelperbase-invalidation "Link to this heading")

The `GridHelperBase.invalidate`, `GridHelperBase.valid`, and `axislines.Axes.invalidate_grid_helper` methods are considered internal and deprecated.

### `sphinext.plot_directive.align`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#sphinext-plot-directive-align "Link to this heading")

... is deprecated. Use `docutils.parsers.rst.directives.images.Image.align` instead.

### Deprecation-related functionality is considered internal[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#deprecation-related-functionality-is-considered-internal "Link to this heading")

The module `matplotlib.cbook.deprecation` is considered internal and will be removed from the public API. This also holds for deprecation-related re-imports in `matplotlib.cbook`, i.e. `matplotlib.cbook.deprecated()`, `matplotlib.cbook.warn_deprecated()`, `matplotlib.cbook.MatplotlibDeprecationWarning` and `matplotlib.cbook.mplDeprecation`.

If needed, external users may import `MatplotlibDeprecationWarning` directly from the `matplotlib` namespace. `mplDeprecation` is only an alias of `MatplotlibDeprecationWarning` and should not be used anymore.

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#id4)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following deprecated APIs have been removed:

### Removed behaviour[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#removed-behaviour "Link to this heading")

*   The "smart bounds" functionality on [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
     and [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
     has been deleted, and the related methods have been removed.
    
*   Converting a string with single color characters (e.g. `'cymk'`) in [`to_rgba_array`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#matplotlib.colors.to_rgba_array "matplotlib.colors.to_rgba_array")
     is no longer supported. Instead, the colors can be passed individually in a list (e.g. `['c', 'y', 'm', 'k']`).
    
*   Returning a factor equal to `None` from `mpl_toolkits.axisartist` Locators (which are **not** the same as "standard" tick Locators), or passing a factor equal to `None` to axisartist Formatters (which are **not** the same as "standard" tick Formatters) is no longer supported. Pass a factor equal to 1 instead.
    

### Modules[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#modules "Link to this heading")

*   The entire `matplotlib.testing.disable_internet` module has been removed. The [pytest-remotedata package](https://github.com/astropy/pytest-remotedata)
     can be used instead.
    
*   The `mpl_toolkits.axes_grid1.colorbar` module and its colorbar implementation have been removed in favor of [`matplotlib.colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#module-matplotlib.colorbar "matplotlib.colorbar")
    .
    

### Classes, methods and attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#classes-methods-and-attributes "Link to this heading")

*   The [`animation.MovieWriterRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry "matplotlib.animation.MovieWriterRegistry")
     methods `.set_dirty()`, `.ensure_not_dirty()`, and `.reset_available_writers()` do nothing and have been removed. The `.avail()` method has been removed; use `.list()` instead to get a list of available writers.
    
*   The `matplotlib.artist.Artist.eventson` and `matplotlib.container.Container.eventson` attributes have no effect and have been removed.
    
*   `matplotlib.axes.Axes.get_data_ratio_log` has been removed.
    
*   `matplotlib.axes.SubplotBase.rowNum`; use `ax.get_subplotspec().rowspan.start` instead.
    
*   `matplotlib.axes.SubplotBase.colNum`; use `ax.get_subplotspec().colspan.start` instead.
    
*   `matplotlib.axis.Axis.set_smart_bounds` and `matplotlib.axis.Axis.get_smart_bounds` have been removed.
    
*   `matplotlib.colors.DivergingNorm` has been renamed to [`TwoSlopeNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm "matplotlib.colors.TwoSlopeNorm")
    .
    
*   `matplotlib.figure.AxesStack` has been removed.
    
*   `matplotlib.font_manager.JSONEncoder` has been removed; use [`font_manager.json_dump`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.json_dump "matplotlib.font_manager.json_dump")
     to dump a [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
     instance.
    
*   The `matplotlib.ft2font.FT2Image` methods `.as_array()`, `.as_rgba_str()`, `.as_str()`, `.get_height()` and `.get_width()` have been removed. Convert the `FT2Image` to a NumPy array with `np.asarray` before processing it.
    
*   `matplotlib.quiver.QuiverKey.quiverkey_doc` has been removed; use `matplotlib.quiver.QuiverKey.__init__.__doc__` instead.
    
*   `matplotlib.spines.Spine.set_smart_bounds` and `matplotlib.spines.Spine.get_smart_bounds` have been removed.
    
*   `matplotlib.testing.jpl_units.UnitDbl.checkUnits` has been removed; use `units not in self.allowed` instead.
    
*   The unused `matplotlib.ticker.Locator.autoscale` method has been removed (pass the axis limits to [`Locator.view_limits`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.view_limits "matplotlib.ticker.Locator.view_limits")
     instead). The derived methods `Locator.autoscale`, `AutoDateLocator.autoscale`, `RRuleLocator.autoscale`, `RadialLocator.autoscale`, `ThetaLocator.autoscale`, and `YearLocator.autoscale` have also been removed.
    
*   `matplotlib.transforms.BboxBase.is_unit` has been removed; check the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
     extents if needed.
    
*   `matplotlib.transforms.Affine2DBase.matrix_from_values(...)` has been removed; use (for example) `Affine2D.from_values(...).get_matrix()` instead.
    

*   `matplotlib.backend_bases.FigureCanvasBase.draw_cursor` has been removed.
    
*   `matplotlib.backends.backend_gtk.ConfigureSubplotsGTK3.destroy` and `matplotlib.backends.backend_gtk.ConfigureSubplotsGTK3.init_window` methods have been removed.
    
*   `matplotlib.backends.backend_gtk.ConfigureSubplotsGTK3.window` property has been removed.
    
*   `matplotlib.backends.backend_macosx.FigureCanvasMac.invalidate` has been removed.
    
*   `matplotlib.backends.backend_pgf.RendererPgf.latexManager` has been removed.
    
*   `matplotlib.backends.backend_wx.FigureFrameWx.statusbar`, `matplotlib.backends.backend_wx.NavigationToolbar2Wx.set_status_bar`, and `matplotlib.backends.backend_wx.NavigationToolbar2Wx.statbar` have been removed. The status bar can be retrieved by calling standard wx methods (`frame.GetStatusBar()` and `toolbar.GetTopLevelParent().GetStatusBar()`).
    
*   `matplotlib.backends.backend_wx.ConfigureSubplotsWx.configure_subplots` and `matplotlib.backends.backend_wx.ConfigureSubplotsWx.get_canvas` have been removed.
    

*   `mpl_toolkits.axisartist.grid_finder.GridFinderBase` has been removed; use [`GridFinder`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder "mpl_toolkits.axisartist.grid_finder.GridFinder")
     instead.
    
*   `mpl_toolkits.axisartist.axis_artist.BezierPath` has been removed; use [`patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
     instead.
    

### Functions[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#functions "Link to this heading")

*   `matplotlib.backends.backend_pgf.repl_escapetext` and `matplotlib.backends.backend_pgf.repl_mathdefault` have been removed.
    
*   `matplotlib.checkdep_ps_distiller` has been removed.
    
*   `matplotlib.cm.revcmap` has been removed; use [`Colormap.reversed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.reversed "matplotlib.colors.Colormap.reversed")
     instead.
    
*   `matplotlib.colors.makeMappingArray` has been removed.
    
*   `matplotlib.compare_versions` has been removed; use comparison of `distutils.version.LooseVersion`s instead.
    
*   `matplotlib.dates.mx2num` has been removed.
    
*   `matplotlib.font_manager.createFontList` has been removed; [`font_manager.FontManager.addfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.addfont "matplotlib.font_manager.FontManager.addfont")
     is now available to register a font at a given path.
    
*   `matplotlib.get_home` has been removed; use standard library instead.
    
*   `matplotlib.mlab.apply_window` and `matplotlib.mlab.stride_repeat` have been removed.
    
*   `matplotlib.rcsetup.update_savefig_format` has been removed; this just replaced `'auto'` with `'png'`, so do the same.
    
*   `matplotlib.rcsetup.validate_animation_writer_path` has been removed.
    
*   `matplotlib.rcsetup.validate_path_exists` has been removed; use [`os.path.exists`](https://docs.python.org/3/library/os.path.html#os.path.exists "(in Python v3.14)")
     or [`pathlib.Path.exists`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists "(in Python v3.14)")
     instead.
    
*   `matplotlib.style.core.is_style_file` and `matplotlib.style.core.iter_style_files` have been removed.
    
*   `matplotlib.testing.is_called_from_pytest` has been removed.
    
*   `mpl_toolkits.mplot3d.axes3d.unit_bbox` has been removed; use [`Bbox.unit`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.unit "matplotlib.transforms.Bbox.unit")
     instead.
    

### Arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#arguments "Link to this heading")

*   Passing more than one positional argument to [`axes.Axes.axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
     will now raise an error.
    
*   Passing `"range"` to the _whis_ parameter of [`Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
     and [`cbook.boxplot_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
     to mean "the whole data range" is no longer supported.
    
*   Passing scalars to the _where_ parameter in [`axes.Axes.fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
     and [`axes.Axes.fill_betweenx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
     is no longer accepted and non-matching sizes now raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
    .
    
*   The _verts_ parameter to [`Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
     has been removed; use _marker_ instead.
    
*   The _minor_ parameter in [`Axis.set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")
     and `SecondaryAxis.set_ticks` is now keyword-only.
    
*   [`scale.ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
    , [`scale.LinearScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LinearScale "matplotlib.scale.LinearScale")
     and [`scale.SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
     now error if any unexpected keyword arguments are passed to their constructors.
    
*   The _renderer_ parameter to [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
     has been removed; this method now always uses the renderer instance cached on the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
    .
    
*   The _locator_ parameter to [`mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.html#mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar "mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar")
     has been removed in favor of its synonym _ticks_ (which already existed previously, and is consistent with [`matplotlib.colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#module-matplotlib.colorbar "matplotlib.colorbar")
    ).
    
*   The _switch\_backend\_warn_ parameter to `matplotlib.test` has no effect and has been removed.
    
*   The _dryrun_ parameter to the various `FigureCanvas*.print_*` methods has been removed.
    

### rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#rcparams "Link to this heading")

*   The `datapath` rcParam has been removed. Use [`matplotlib.get_data_path`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_data_path "matplotlib.get_data_path")
     instead.
    
*   The `mpl_toolkits.legacy_colorbar` rcParam has no effect and has been removed.
    
*   Setting `[rcParams["boxplot.whiskers"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=boxplot.whiskers#rcparam-boxplot-whiskers) ` (default: `1.5`) to `"range"` is no longer valid; set it to `0, 100` instead.
    
*   Setting `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`) to `"auto"` is no longer valid; use `"png"` instead.
    
*   Setting `[rcParams["text.hinting"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.hinting#rcparam-text-hinting) ` (default: `'default'`) to [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
     or [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
     is no longer valid; set it to `"auto"` or `"none"` respectively.
    

### sample\_data removals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#sample-data-removals "Link to this heading")

The sample datasets listed below have been removed. Suggested replacements for demonstration purposes are listed in parentheses.

*   `None_vs_nearest-pdf.png`,
    
*   `aapl.npz` (use `goog.npz`),
    
*   `ada.png`, `grace_hopper.png` (use `grace_hopper.jpg`),
    
*   `ct.raw.gz` (use `s1045.ima.gz`),
    
*   `damodata.csv` (use `msft.csv`).
    

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#id5)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#development-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Increase to minimum supported versions of Python and dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#increase-to-minimum-supported-versions-of-python-and-dependencies "Link to this heading")

For Matplotlib 3.4, the [minimum supported versions](https://matplotlib.org/stable/install/dependencies.html#dependencies)
 are being bumped:

| Dependency | min in mpl3.3 | min in mpl3.4 |
| --- | --- | --- |
| Python | 3.6 | 3.7 |
| dateutil | 2.1 | 2.7 |
| numpy | 1.15 | 1.16 |
| pyparsing | 2.0.3 | 2.2.1 |

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)
 and [NEP29](https://numpy.org/neps/nep-0029-deprecation_policy.html)

### Qhull downloaded at build-or-sdist time[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#qhull-downloaded-at-build-or-sdist-time "Link to this heading")

Much like FreeType, Qhull is now downloaded at build time, or upon creation of the sdist. To link against system Qhull, set the `system_qhull` option to [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 in the `setup.cfg` file. Note that Matplotlib now requires the re-entrant version of Qhull (`qhull_r`).

### `FigureBase` class added, and `Figure` class made a child[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.0.html#figurebase-class-added-and-figure-class-made-a-child "Link to this heading")

The new subfigure feature motivated some re-organization of the [`figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class, so that the new [`figure.SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 class could have all the capabilities of a figure.

The [`figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class is now a subclass of [`figure.FigureBase`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase "matplotlib.figure.FigureBase")
, where [`figure.FigureBase`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase "matplotlib.figure.FigureBase")
 contains figure-level artist addition routines, and the [`figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 subclass just contains features that are unique to the outer figure.

Note that there is a new _transSubfigure_ transform associated with the subfigure. This transform also exists for a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 instance, and is equal to _transFigure_ in that case, so code that uses the transform stack that wants to place objects on either the parent figure or one of the subfigures should use _transSubfigure_.

On this page
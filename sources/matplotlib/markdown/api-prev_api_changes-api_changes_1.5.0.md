[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#main-content)

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
    

API Changes in 1.5.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#api-changes-in-1-5-0 "Link to this heading")

===============================================================================================================================================

Code Changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#code-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Reversed [`matplotlib.cbook.ls_mapper`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.ls_mapper "matplotlib.cbook.ls_mapper")
, added [`ls_mapper_r`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.ls_mapper_r "matplotlib.cbook.ls_mapper_r")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#reversed-matplotlib-cbook-ls-mapper-added-ls-mapper-r "Link to this heading")

Formerly, [`matplotlib.cbook.ls_mapper`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.ls_mapper "matplotlib.cbook.ls_mapper")
 was a dictionary with the long-form line-style names (`"solid"`) as keys and the short forms (`"-"`) as values. This long-to-short mapping is now done by [`ls_mapper_r`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.ls_mapper_r "matplotlib.cbook.ls_mapper_r")
, and the short-to-long mapping is done by the [`ls_mapper`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.ls_mapper "matplotlib.cbook.ls_mapper")
.

### Prevent moving artists between Axes, Property-ify Artist.axes, deprecate Artist.{get,set}\_axes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#prevent-moving-artists-between-axes-property-ify-artist-axes-deprecate-artist-get-set-axes "Link to this heading")

This was done to prevent an Artist that is already associated with an Axes from being moved/added to a different Axes. This was never supported as it causes havoc with the transform stack. The apparent support for this (as it did not raise an exception) was the source of multiple bug reports and questions on SO.

For almost all use-cases, the assignment of the axes to an artist should be taken care of by the axes as part of the `Axes.add_*` method, hence the deprecation of {get,set}\_axes.

Removing the `set_axes` method will also remove the 'axes' line from the ACCEPTS kwarg tables (assuming that the removal date gets here before that gets overhauled).

### Tightened input validation on 'pivot' kwarg to quiver[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#tightened-input-validation-on-pivot-kwarg-to-quiver "Link to this heading")

Tightened validation so that only {'tip', 'tail', 'mid', and 'middle'} (but any capitalization) are valid values for the _pivot_ keyword argument in the [`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")
 class (and hence [`axes.Axes.quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
 and [`pyplot.quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver "matplotlib.pyplot.quiver")
 which both fully delegate to [`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")
). Previously any input matching 'mid.\*' would be interpreted as 'middle', 'tip.\*' as 'tip' and any string not matching one of those patterns as 'tail'.

The value of `Quiver.pivot` is normalized to be in the set {'tip', 'tail', 'middle'} in [`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")
.

### Reordered `Axes.get_children`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#reordered-axes-get-children "Link to this heading")

The artist order returned by [`axes.Axes.get_children`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_children.html#matplotlib.axes.Axes.get_children "matplotlib.axes.Axes.get_children")
 did not match the one used by [`axes.Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw")
. They now use the same order, as [`axes.Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw")
 now calls [`axes.Axes.get_children`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_children.html#matplotlib.axes.Axes.get_children "matplotlib.axes.Axes.get_children")
.

### Changed behaviour of contour plots[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#changed-behaviour-of-contour-plots "Link to this heading")

The default behaviour of [`contour()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
 and [`contourf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
 when using a masked array is now determined by the new keyword argument _corner\_mask_, or if this is not specified then the new `[rcParams["contour.corner_mask"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=contour.corner_mask#rcparam-contour-corner-mask) ` (default: `True`) instead. The new default behaviour is equivalent to using `corner_mask=True`; the previous behaviour can be obtained using `corner_mask=False` or by changing the rcParam. The example [https://matplotlib.org/examples/pylab\_examples/contour\_corner\_mask.html](https://matplotlib.org/examples/pylab_examples/contour_corner_mask.html)
 demonstrates the difference. Use of the old contouring algorithm, which is obtained with `corner_mask='legacy'`, is now deprecated.

Contour labels may now appear in different places than in earlier versions of Matplotlib.

In addition, the keyword argument _nchunk_ now applies to [`contour()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
 as well as [`contourf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
, and it subdivides the domain into subdomains of exactly _nchunk_ by _nchunk_ quads, whereas previously it was only roughly _nchunk_ by _nchunk_ quads.

The C/C++ object that performs contour calculations used to be stored in the public attribute `QuadContourSet.Cntr`, but is now stored in a private attribute and should not be accessed by end users.

### Added set\_params function to all Locator types[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#added-set-params-function-to-all-locator-types "Link to this heading")

This was a bug fix targeted at making the api for Locators more consistent.

In the old behavior, only locators of type MaxNLocator have set\_params() defined, causing its use on any other Locator to raise an AttributeError _( aside: set\_params(args) is a function that sets the parameters of a Locator instance to be as specified within args)_. The fix involves moving set\_params() to the Locator class such that all subtypes will have this function defined.

Since each of the Locator subtypes have their own modifiable parameters, a universal set\_params() in Locator isn't ideal. Instead, a default no-operation function that raises a warning is implemented in Locator. Subtypes extending Locator will then override with their own implementations. Subtypes that do not have a need for set\_params() will fall back onto their parent's implementation, which raises a warning as intended.

In the new behavior, Locator instances will not raise an AttributeError when set\_params() is called. For Locators that do not implement set\_params(), the default implementation in Locator is used.

### Disallow `None` as x or y value in ax.plot[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#disallow-none-as-x-or-y-value-in-ax-plot "Link to this heading")

Do not allow `None` as a valid input for the `x` or `y` args in [`axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
. This may break some user code, but this was never officially supported (ex documented) and allowing `None` objects through can lead to confusing exceptions downstream.

To create an empty line use

ln1, \= ax.plot(\[\], \[\], ...)
ln2, \= ax.plot(\[\], ...)

In either case to update the data in the [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 object you must update both the `x` and `y` data.

### Removed _args_ and _kwargs_ from `MicrosecondLocator.__call__`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#removed-args-and-kwargs-from-microsecondlocator-call "Link to this heading")

The call signature of `matplotlib.dates.MicrosecondLocator.__call__` has changed from `__call__(self, *args, **kwargs)` to `__call__(self)`. This is consistent with the superclass [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 and also all the other Locators derived from this superclass.

### No [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
 for the MicrosecondLocator and YearLocator[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#no-valueerror-for-the-microsecondlocator-and-yearlocator "Link to this heading")

The [`MicrosecondLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MicrosecondLocator "matplotlib.dates.MicrosecondLocator")
 and [`YearLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.YearLocator "matplotlib.dates.YearLocator")
 objects when called will return an empty list if the axes have no data or the view has no interval. Previously, they raised a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
. This is consistent with all the Date Locators.

### 'OffsetBox.DrawingArea' respects the 'clip' keyword argument[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#offsetbox-drawingarea-respects-the-clip-keyword-argument "Link to this heading")

The call signature was `OffsetBox.DrawingArea(..., clip=True)` but nothing was done with the _clip_ argument. The object did not do any clipping regardless of that parameter. Now the object can and does clip the child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s if they are set to be clipped.

You can turn off the clipping on a per-child basis using `child.set_clip_on(False)`.

### Add salt to clipPath id[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#add-salt-to-clippath-id "Link to this heading")

Add salt to the hash used to determine the id of the `clipPath` nodes. This is to avoid conflicts when two svg documents with the same clip path are included in the same document (see [ipython/ipython#8133](https://github.com/ipython/ipython/issues/8133)
 and [matplotlib/matplotlib#4349](https://github.com/matplotlib/matplotlib/issues/4349)
 ), however this means that the svg output is no longer deterministic if the same figure is saved twice. It is not expected that this will affect any users as the current ids are generated from an md5 hash of properties of the clip path and any user would have a very difficult time anticipating the value of the id.

### Changed snap threshold for circle markers to inf[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#changed-snap-threshold-for-circle-markers-to-inf "Link to this heading")

When drawing circle markers above some marker size (previously 6.0) the path used to generate the marker was snapped to pixel centers. However, this ends up distorting the marker away from a circle. By setting the snap threshold to inf snapping is never done on circles.

This change broke several tests, but is an improvement.

### Preserve units with Text position[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#preserve-units-with-text-position "Link to this heading")

Previously the 'get\_position' method on Text would strip away unit information even though the units were still present. There was no inherent need to do this, so it has been changed so that unit data (if present) will be preserved. Essentially a call to 'get\_position' will return the exact value from a call to 'set\_position'.

If you wish to get the old behaviour, then you can use the new method called 'get\_unitless\_position'.

### New API for custom Axes view changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#new-api-for-custom-axes-view-changes "Link to this heading")

Interactive pan and zoom were previously implemented using a Cartesian-specific algorithm that was not necessarily applicable to custom Axes. Three new private methods, `matplotlib.axes._base._AxesBase._get_view`, `matplotlib.axes._base._AxesBase._set_view`, and `matplotlib.axes._base._AxesBase._set_view_from_bbox`, allow for custom _Axes_ classes to override the pan and zoom algorithms. Implementers of custom _Axes_ who override these methods may provide suitable behaviour for both pan and zoom as well as the view navigation buttons on the interactive toolbars.

MathTex visual changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#mathtex-visual-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The spacing commands in mathtext have been changed to more closely match vanilla TeX.

### Improved spacing in mathtext[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#improved-spacing-in-mathtext "Link to this heading")

The extra space that appeared after subscripts and superscripts has been removed.

### No annotation coordinates wrap[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#no-annotation-coordinates-wrap "Link to this heading")

In #2351 for 1.4.0 the behavior of \['axes points', 'axes pixel', 'figure points', 'figure pixel'\] as coordinates was change to no longer wrap for negative values. In 1.4.3 this change was reverted for 'axes points' and 'axes pixel' and in addition caused 'axes fraction' to wrap. For 1.5 the behavior has been reverted to as it was in 1.4.0-1.4.2, no wrapping for any type of coordinate.

Deprecation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#deprecation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

### Deprecated `GraphicsContextBase.set_graylevel`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#deprecated-graphicscontextbase-set-graylevel "Link to this heading")

The `GraphicsContextBase.set_graylevel` function has been deprecated in 1.5 and will be removed in 1.6. It has been unused. The [`GraphicsContextBase.set_foreground`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_foreground "matplotlib.backend_bases.GraphicsContextBase.set_foreground")
 could be used instead.

### deprecated idle\_event[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#deprecated-idle-event "Link to this heading")

The `idle_event` was broken or missing in most backends and causes spurious warnings in some cases, and its use in creating animations is now obsolete due to the animations module. Therefore code involving it has been removed from all but the wx backend (where it partially works), and its use is deprecated. The [`animation`](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "matplotlib.animation")
 module may be used instead to create animations.

### `color_cycle` deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#color-cycle-deprecated "Link to this heading")

In light of the new property cycling feature, the Axes method `set_color_cycle` is now deprecated. Calling this method will replace the current property cycle with one that cycles just the given colors.

Similarly, the rc parameter _axes.color\_cycle_ is also deprecated in lieu of the new `[rcParams["axes.prop_cycle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.prop_cycle#rcparam-axes-prop-cycle) ` (default: `cycler('color', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)])`) parameter. Having both parameters in the same rc file is not recommended as the result cannot be predicted. For compatibility, setting _axes.color\_cycle_ will replace the cycler in `[rcParams["axes.prop_cycle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.prop_cycle#rcparam-axes-prop-cycle) ` (default: `cycler('color', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)])`) with a color cycle. Accessing _axes.color\_cycle_ will return just the color portion of the property cycle, if it exists.

Timeline for removal has not been set.

Bundled jquery[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#bundled-jquery "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

The version of jquery bundled with the webagg backend has been upgraded from 1.7.1 to 1.11.3. If you are using the version of jquery bundled with webagg you will need to update your html files as such

\-    <script src="\_static/jquery/js/jquery-1.7.1.min.js"></script>
\+    <script src="\_static/jquery/js/jquery-1.11.3.min.js"></script>

Code Removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#code-removed "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Removed `Image` from main namespace[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#removed-image-from-main-namespace "Link to this heading")

`Image` was imported from PIL/pillow to test if PIL is available, but there is no reason to keep `Image` in the namespace once the availability has been determined.

### Removed `lod` from Artist[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#removed-lod-from-artist "Link to this heading")

Removed the method `set_lod` and all references to the attribute `_lod` as they are not used anywhere else in the code base. It appears to be a feature stub that was never built out.

### Removed threading related classes from cbook[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#removed-threading-related-classes-from-cbook "Link to this heading")

The classes `Scheduler`, `Timeout`, and `Idle` were in cbook, but are not used internally. They appear to be a prototype for the idle event system which was not working and has recently been pulled out.

### Removed _Lena_ images from sample\_data[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#removed-lena-images-from-sample-data "Link to this heading")

The `lena.png` and `lena.jpg` images have been removed from Matplotlib's sample\_data directory. The images are also no longer available from [`matplotlib.cbook.get_sample_data`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
. We suggest using `matplotlib.cbook.get_sample_data('grace_hopper.png')` or `matplotlib.cbook.get_sample_data('grace_hopper.jpg')` instead.

### Legend[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#legend "Link to this heading")

Removed handling of _loc_ as a positional argument to [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

### Legend handlers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#legend-handlers "Link to this heading")

Remove code to allow legend handlers to be callable. They must now implement a method `legend_artist`.

### Axis[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#axis "Link to this heading")

Removed method `set_scale`. This is now handled via a private method which should not be used directly by users. It is called via `Axes.set_{x,y}scale` which takes care of ensuring the related changes are also made to the Axes object.

### finance.py[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#finance-py "Link to this heading")

Removed functions with ambiguous argument order from finance.py

### Annotation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#annotation "Link to this heading")

Removed `textcoords` and `xytext` proprieties from Annotation objects.

### sphinxext.ipython\_\*.py[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#sphinxext-ipython-py "Link to this heading")

Both `ipython_console_highlighting` and `ipython_directive` have been moved to IPython.

Change your import from `matplotlib.sphinxext.ipython_directive` to `IPython.sphinxext.ipython_directive` and from `matplotlib.sphinxext.ipython_directive` to `IPython.sphinxext.ipython_directive`

### LineCollection.color[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#linecollection-color "Link to this heading")

Deprecated in 2005, use `set_color`

### remove `'faceted'` as a valid value for _shading_ in `tri.tripcolor`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#remove-faceted-as-a-valid-value-for-shading-in-tri-tripcolor "Link to this heading")

Use _edgecolor_ instead. Added validation on _shading_ to only be valid values.

### Remove `faceted` kwarg from scatter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#remove-faceted-kwarg-from-scatter "Link to this heading")

Remove support for the `faceted` kwarg. This was deprecated in d48b34288e9651ff95c3b8a071ef5ac5cf50bae7 (2008-04-18!) and replaced by `edgecolor`.

### Remove `set_colorbar` method from `ScalarMappable`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#remove-set-colorbar-method-from-scalarmappable "Link to this heading")

Remove `set_colorbar` method, use [`colorbar`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.colorbar "matplotlib.cm.ScalarMappable.colorbar")
 attribute directly.

### patheffects.svg[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#patheffects-svg "Link to this heading")

*   remove `get_proxy_renderer` method from `AbstractPathEffect` class
    
*   remove `patch_alpha` and `offset_xy` from `SimplePatchShadow`
    

### Remove `testing.image_util.py`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#remove-testing-image-util-py "Link to this heading")

Contained only a no-longer used port of functionality from PIL

### Remove `mlab.FIFOBuffer`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#remove-mlab-fifobuffer "Link to this heading")

Not used internally and not part of core mission of mpl.

### Remove `mlab.prepca`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#remove-mlab-prepca "Link to this heading")

Deprecated in 2009.

### Remove `NavigationToolbar2QTAgg`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#remove-navigationtoolbar2qtagg "Link to this heading")

Added no functionality over the base `NavigationToolbar2Qt`

### mpl.py[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.0.html#mpl-py "Link to this heading")

Remove the module `matplotlib.mpl`. Deprecated in 1.3 by PR #1670 and commit 78ce67d161625833cacff23cfe5d74920248c5b2

On this page
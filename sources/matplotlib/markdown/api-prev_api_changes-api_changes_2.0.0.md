[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#main-content)

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
    

API Changes in 2.0.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#api-changes-in-2-0-0 "Link to this heading")

===============================================================================================================================================

Deprecation and removal[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#deprecation-and-removal "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

### Color of Axes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#color-of-axes "Link to this heading")

The `axisbg` and `axis_bgcolor` properties on _Axes_ have been deprecated in favor of `facecolor`.

### GTK and GDK backends deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#gtk-and-gdk-backends-deprecated "Link to this heading")

The GDK and GTK backends have been deprecated. These obsolete backends allow figures to be rendered via the GDK API to files and GTK2 figures. They are untested and known to be broken, and their use has been discouraged for some time. Instead, use the `GTKAgg` and `GTKCairo` backends for rendering to GTK2 windows.

### WX backend deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#wx-backend-deprecated "Link to this heading")

The WX backend has been deprecated. It is untested, and its use has been discouraged for some time. Instead, use the `WXAgg` backend for rendering figures to WX windows.

### CocoaAgg backend removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#cocoaagg-backend-removed "Link to this heading")

The deprecated and not fully functional CocoaAgg backend has been removed.

### [`round`](https://docs.python.org/3/library/functions.html#round "(in Python v3.14)")
 removed from TkAgg Backend[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#round-removed-from-tkagg-backend "Link to this heading")

The TkAgg backend had its own implementation of the [`round`](https://docs.python.org/3/library/functions.html#round "(in Python v3.14)")
 function. This was unused internally and has been removed. Instead, use either the [`round`](https://docs.python.org/3/library/functions.html#round "(in Python v3.14)")
 builtin function or [`numpy.around`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "(in NumPy v2.5)")
.

### 'hold' functionality deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#hold-functionality-deprecated "Link to this heading")

The 'hold' keyword argument and all functions and methods related to it are deprecated, along with the `axes.hold` rcParams entry. The behavior will remain consistent with the default `hold=True` state that has long been in place. Instead of using a function or keyword argument (`hold=False`) to change that behavior, explicitly clear the axes or figure as needed prior to subsequent plotting commands.

[`Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update")
 has return value[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#artist-update-has-return-value "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The methods [`matplotlib.artist.Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
, [`matplotlib.artist.Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update")
, and the function [`matplotlib.artist.setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.setp.html#matplotlib.artist.setp "matplotlib.artist.setp")
 now use a common codepath to look up how to update the given artist properties (either using the setter methods or an attribute/property).

The behavior of [`matplotlib.artist.Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update")
 is slightly changed to return a list of the values returned from the setter methods to avoid changing the API of [`matplotlib.artist.Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
 and [`matplotlib.artist.setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.setp.html#matplotlib.artist.setp "matplotlib.artist.setp")
.

The keys passed into [`matplotlib.artist.Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update")
 are now converted to lower case before being processed, to match the behavior of [`matplotlib.artist.Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
 and [`matplotlib.artist.setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.setp.html#matplotlib.artist.setp "matplotlib.artist.setp")
. This should not break any user code because there are no set methods with capitals in their names, but this puts a constraint on naming properties in the future.

[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 initializers gain _edgecolor_ and _facecolor_ keyword arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#legend-initializers-gain-edgecolor-and-facecolor-keyword-arguments "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 background patch (or 'frame') can have its `edgecolor` and `facecolor` determined by the corresponding keyword arguments to the [`matplotlib.legend.Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 initializer, or to any of the methods or functions that call that initializer. If left to their default values of [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, their values will be taken from `matplotlib.rcParams`. The previously-existing `framealpha` kwarg still controls the alpha transparency of the patch.

Qualitative colormaps[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#qualitative-colormaps "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Colorbrewer's qualitative/discrete colormaps ("Accent", "Dark2", "Paired", "Pastel1", "Pastel2", "Set1", "Set2", "Set3") are now implemented as [`ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 instead of [`LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
.

To use these for images where categories are specified as integers, for instance, use:

plt.imshow(x, cmap\='Dark2', norm\=colors.NoNorm())

Change in the `draw_image` backend API[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#change-in-the-draw-image-backend-api "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `draw_image` method implemented by backends has changed its interface.

This change is only relevant if the backend declares that it is able to transform images by returning `True` from `option_scale_image`. See the `draw_image` docstring for more information.

`matplotlib.ticker.LinearLocator` algorithm update[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#matplotlib-ticker-linearlocator-algorithm-update "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`matplotlib.ticker.LinearLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")
 is used to define the range and location of axis ticks when the user wants an exact number of ticks. `LinearLocator` thus differs from the default locator `MaxNLocator`, for which the user specifies a maximum number of intervals rather than a precise number of ticks.

The view range algorithm in `matplotlib.ticker.LinearLocator` has been changed so that more convenient tick locations are chosen. The new algorithm returns a plot view range that is a multiple of the user-requested number of ticks. This ensures tick marks will be located at whole integers more consistently. For example, when both y-axes of a\`\`twinx\`\` plot use `matplotlib.ticker.LinearLocator` with the same number of ticks, their y-tick locations and grid lines will coincide.

[`matplotlib.ticker.LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
 gains numticks kwarg[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#matplotlib-ticker-loglocator-gains-numticks-kwarg "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The maximum number of ticks generated by the [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
 can now be controlled explicitly via setting the new 'numticks' kwarg to an integer. By default the kwarg is None which internally sets it to the 'auto' string, triggering a new algorithm for adjusting the maximum according to the axis length relative to the ticklabel font size.

[`matplotlib.ticker.LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter")
: two new kwargs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#matplotlib-ticker-logformatter-two-new-kwargs "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously, minor ticks on log-scaled axes were not labeled by default. An algorithm has been added to the [`LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter")
 to control the labeling of ticks between integer powers of the base. The algorithm uses two parameters supplied in a kwarg tuple named 'minor\_thresholds'. See the docstring for further explanation.

To improve support for axes using [`SymmetricalLogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator "matplotlib.ticker.SymmetricalLogLocator")
, a _linthresh_ keyword argument was added.

New defaults for 3D quiver function in mpl\_toolkits.mplot3d.axes3d.py[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#new-defaults-for-3d-quiver-function-in-mpl-toolkits-mplot3d-axes3d-py "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib has both a 2D and a 3D `quiver` function. These changes affect only the 3D function and make the default behavior of the 3D function match the 2D version. There are two changes:

1.  The 3D quiver function previously normalized the arrows to be the same length, which makes it unusable for situations where the arrows should be different lengths and does not match the behavior of the 2D function. This normalization behavior is now controlled with the `normalize` keyword, which defaults to False.
    
2.  The `pivot` keyword now defaults to `tail` instead of `tip`. This was done in order to match the default behavior of the 2D quiver function.
    

To obtain the previous behavior with the 3D quiver function, one can call the function with

ax.quiver(x, y, z, u, v, w, normalize\=True, pivot\='tip')

where "ax" is an `Axes3d` object created with something like

import mpl\_toolkits.mplot3d.axes3d
ax \= plt.subplot(111, projection\='3d')

Stale figure behavior[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#stale-figure-behavior "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Attempting to draw the figure will now mark it as not stale (independent if the draw succeeds). This change is to prevent repeatedly trying to re-draw a figure which is raising an error on draw. The previous behavior would only mark a figure as not stale after a full re-draw succeeded.

The spectral colormap is now nipy\_spectral[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#the-spectral-colormap-is-now-nipy-spectral "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The colormaps formerly known as `spectral` and `spectral_r` have been replaced by `nipy_spectral` and `nipy_spectral_r` since Matplotlib 1.3.0. Even though the colormap was deprecated in Matplotlib 1.3.0, it never raised a warning. As of Matplotlib 2.0.0, using the old names raises a deprecation warning. In the future, using the old names will raise an error.

Default install no longer includes test images[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#default-install-no-longer-includes-test-images "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To reduce the size of wheels and source installs, the tests and baseline images are no longer included by default.

To restore installing the tests and images, use a `setup.cfg` with

\[packages\]
tests \= True
toolkits\_tests \= True

in the source directory at build/install time.

On this page
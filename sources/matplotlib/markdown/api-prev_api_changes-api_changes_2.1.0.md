[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#main-content)

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
    

API Changes in 2.1.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#api-changes-in-2-1-0 "Link to this heading")

===============================================================================================================================================

Default behavior of log scales changed to mask <= 0 values[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#default-behavior-of-log-scales-changed-to-mask-0-values "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Calling [`matplotlib.axes.Axes.set_xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
 or [`matplotlib.axes.Axes.set_yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
 now uses 'mask' as the default method to handle invalid values (as opposed to 'clip'). This means that any values <= 0 on a log scale will not be shown.

Previously they were clipped to a very small number and shown.

[`matplotlib.cbook.CallbackRegistry.process()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.process "matplotlib.cbook.CallbackRegistry.process")
 suppresses exceptions by default[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#matplotlib-cbook-callbackregistry-process-suppresses-exceptions-by-default "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib uses instances of [`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
 as a bridge between user input event from the GUI and user callbacks. Previously, any exceptions raised in a user call back would bubble out of the `process` method, which is typically in the GUI event loop. Most GUI frameworks simple print the traceback to the screen and continue as there is not always a clear method of getting the exception back to the user. However PyQt5 now exits the process when it receives an un-handled python exception in the event loop. Thus, [`process()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.process "matplotlib.cbook.CallbackRegistry.process")
 now suppresses and prints tracebacks to stderr by default.

What [`process()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.process "matplotlib.cbook.CallbackRegistry.process")
 does with exceptions is now user configurable via the `exception_handler` attribute and kwarg. To restore the previous behavior pass `None`

cb \= CallbackRegistry(exception\_handler\=None)

A function which take and `Exception` as its only argument may also be passed

def maybe\_reraise(exc):
    if isinstance(exc, RuntimeError):
        pass
    else:
        raise exc

cb \= CallbackRegistry(exception\_handler\=maybe\_reraise)

Improved toggling of the axes grids[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#improved-toggling-of-the-axes-grids "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `g` key binding now switches the states of the `x` and `y` grids independently (by cycling through all four on/off combinations).

The new `G` key binding switches the states of the minor grids.

Both bindings are disabled if only a subset of the grid lines (in either direction) is visible, to avoid making irreversible changes to the figure.

Ticklabels are turned off instead of being invisible[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#ticklabels-are-turned-off-instead-of-being-invisible "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Internally, the [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
's `~matplotlib.axis.Tick.label1On` attribute is now used to hide tick labels instead of setting the visibility on the tick label objects. This improves overall performance and fixes some issues. As a consequence, in case those labels ought to be shown, [`tick_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 needs to be used, e.g.

ax.tick\_params(labelbottom\=True)

Removal of warning on empty legends[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#removal-of-warning-on-empty-legends "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`pyplot.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
 used to issue a warning when no labeled artist could be found. This warning has been removed.

More accurate legend autopositioning[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#more-accurate-legend-autopositioning "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Automatic positioning of legends now prefers using the area surrounded by a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 rather than placing the legend over the line itself.

Cleanup of stock sample data[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#cleanup-of-stock-sample-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The sample data of stocks has been cleaned up to remove redundancies and increase portability. The `AAPL.dat.gz`, `INTC.dat.gz` and `aapl.csv` files have been removed entirely and will also no longer be available from [`matplotlib.cbook.get_sample_data`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
. If a CSV file is required, we suggest using the `msft.csv` that continues to be shipped in the sample data. If a NumPy binary file is acceptable, we suggest using one of the following two new files. The `aapl.npy.gz` and `goog.npy` files have been replaced by `aapl.npz` and `goog.npz`, wherein the first column's type has changed from [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)")
 to [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 for better portability across Python versions. Note that Matplotlib does not fully support [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 as yet.

Updated qhull to 2015.2[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#updated-qhull-to-2015-2 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

The version of qhull shipped with Matplotlib, which is used for Delaunay triangulation, has been updated from version 2012.1 to 2015.2.

Improved Delaunay triangulations with large offsets[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#improved-delaunay-triangulations-with-large-offsets "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Delaunay triangulations now deal with large x,y offsets in a better way. This can cause minor changes to any triangulations calculated using Matplotlib, i.e. any use of [`matplotlib.tri.Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 that requests that a Delaunay triangulation is calculated, which includes [`matplotlib.pyplot.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontour.html#matplotlib.pyplot.tricontour "matplotlib.pyplot.tricontour")
, [`matplotlib.pyplot.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib.pyplot.tricontourf "matplotlib.pyplot.tricontourf")
, [`matplotlib.pyplot.tripcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tripcolor.html#matplotlib.pyplot.tripcolor "matplotlib.pyplot.tripcolor")
, [`matplotlib.pyplot.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot "matplotlib.pyplot.triplot")
, `matplotlib.mlab.griddata` and [`mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf")
.

Use `backports.functools_lru_cache` instead of `functools32`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#use-backports-functools-lru-cache-instead-of-functools32 "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It's better maintained and more widely used (by pylint, jaraco, etc).

`cbook.is_numlike` only performs an instance check[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#cbook-is-numlike-only-performs-an-instance-check "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`matplotlib.cbook.is_numlike` now only checks that its argument is an instance of `(numbers.Number, np.Number)`. In particular, this means that arrays are now not num-like.

Elliptical arcs now drawn between correct angles[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#elliptical-arcs-now-drawn-between-correct-angles "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`matplotlib.patches.Arc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
 patch is now correctly drawn between the given angles.

Previously a circular arc was drawn and then stretched into an ellipse, so the resulting arc did not lie between _theta1_ and _theta2_.

`-d$backend` no longer sets the backend[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#d-backend-no-longer-sets-the-backend "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is no longer possible to set the backend by passing `-d$backend` at the command line. Use the `MPLBACKEND` environment variable instead.

Path.intersects\_bbox always treats the bounding box as filled[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#path-intersects-bbox-always-treats-the-bounding-box-as-filled "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously, when `Path.intersects_bbox` was called with `filled` set to `False`, it would treat both the path and the bounding box as unfilled. This behavior was not well documented and it is usually not the desired behavior, since bounding boxes are used to represent more complex shapes located inside the bounding box. This behavior has now been changed: when `filled` is `False`, the path will be treated as unfilled, but the bounding box is still treated as filled. The old behavior was arguably an implementation bug.

When `Path.intersects_bbox` is called with `filled` set to `True` (the default value), there is no change in behavior. For those rare cases where `Path.intersects_bbox` was called with `filled` set to `False` and where the old behavior is actually desired, the suggested workaround is to call `Path.intersects_path` with a rectangle as the path:

from matplotlib.path import Path
from matplotlib.transforms import Bbox, BboxTransformTo
rect \= Path.unit\_rectangle().transformed(BboxTransformTo(bbox))
result \= path.intersects\_path(rect, filled\=False)

WX no longer calls generates `IdleEvent` events or calls `idle_event`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#wx-no-longer-calls-generates-idleevent-events-or-calls-idle-event "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Removed unused private method `_onIdle` from `FigureCanvasWx`.

The `IdleEvent` class and `FigureCanvasBase.idle_event` method will be removed in 2.2

Correct scaling of `magnitude_spectrum()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#correct-scaling-of-magnitude-spectrum "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The functions [`matplotlib.mlab.magnitude_spectrum()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "matplotlib.mlab.magnitude_spectrum")
 and [`matplotlib.pyplot.magnitude_spectrum()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.magnitude_spectrum.html#matplotlib.pyplot.magnitude_spectrum "matplotlib.pyplot.magnitude_spectrum")
 implicitly assumed the sum of windowing function values to be one. In Matplotlib and Numpy the standard windowing functions are scaled to have maximum value of one, which usually results in a sum of the order of n/2 for a n-point signal. Thus the amplitude scaling `magnitude_spectrum()` was off by that amount when using standard windowing functions ([Bug 8417](https://github.com/matplotlib/matplotlib/issues/8417)
 ). Now the behavior is consistent with [`matplotlib.pyplot.psd()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html#matplotlib.pyplot.psd "matplotlib.pyplot.psd")
 and [`scipy.signal.welch()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html#scipy.signal.welch "(in SciPy v1.18.0)")
. The following example demonstrates the new and old scaling:

import matplotlib.pyplot as plt
import numpy as np

tau, n \= 10, 1024  \# 10 second signal with 1024 points
T \= tau/n  \# sampling interval
t \= np.arange(n)\*T

a \= 4  \# amplitude
x \= a\*np.sin(40\*np.pi\*t)  \# 20 Hz sine with amplitude a

\# New correct behavior: Amplitude at 20 Hz is a/2
plt.magnitude\_spectrum(x, Fs\=1/T, sides\='onesided', scale\='linear')

\# Original behavior: Amplitude at 20 Hz is (a/2)\*(n/2) for a Hanning window
w \= np.hanning(n)  \# default window is a Hanning window
plt.magnitude\_spectrum(x\*np.sum(w), Fs\=1/T, sides\='onesided', scale\='linear')

Change to signatures of [`bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 & [`barh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#change-to-signatures-of-bar-barh "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For 2.0 the [default value of \*align\*](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#barbarh-align)
 changed to `'center'`. However this caused the signature of [`bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`barh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
 to be misleading as the first parameters were still _left_ and _bottom_ respectively:

bar(left, height, \*, align\='center', \*\*kwargs)
barh(bottom, width, \*, align\='center', \*\*kwargs)

despite behaving as the center in both cases. The methods now take `*args, **kwargs` as input and are documented to have the primary signatures of:

bar(x, height, \*, align\='center', \*\*kwargs)
barh(y, width, \*, align\='center', \*\*kwargs)

Passing _left_ and _bottom_ as keyword arguments to [`bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`barh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
 respectively will warn. Support will be removed in Matplotlib 3.0.

Font cache as json[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#font-cache-as-json "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

The font cache is now saved as json, rather than a pickle.

Invalid (Non-finite) Axis Limit Error[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#invalid-non-finite-axis-limit-error "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using [`set_xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 and [`set_ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
, passing non-finite values now results in a `ValueError`. The previous behavior resulted in the limits being erroneously reset to `(-0.001, 0.001)`.

`scatter` and `Collection` offsets are no longer implicitly flattened[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#scatter-and-collection-offsets-are-no-longer-implicitly-flattened "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 (and thus both 2D [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
 and 3D [`scatter`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl_toolkits.mplot3d.axes3d.Axes3D.scatter "mpl_toolkits.mplot3d.axes3d.Axes3D.scatter")
) no longer implicitly flattens its offsets. As a consequence, `scatter`'s `x` and `y` arguments can no longer be 2+-dimensional arrays.

Deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#deprecations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### `GraphicsContextBase`'s `linestyle` property.[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#graphicscontextbase-s-linestyle-property "Link to this heading")

The `GraphicsContextBase.get_linestyle` and `GraphicsContextBase.set_linestyle` methods, which had no effect, have been deprecated. All of the backends Matplotlib ships use `GraphicsContextBase.get_dashes` and `GraphicsContextBase.set_dashes` which are more general. Third-party backends should also migrate to the `*_dashes` methods.

### `NavigationToolbar2.dynamic_update`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#navigationtoolbar2-dynamic-update "Link to this heading")

Use [`draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
 method on the `Canvas` instance instead.

### Testing[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#testing "Link to this heading")

`matplotlib.testing.noseclasses` is deprecated and will be removed in 2.3

### `EngFormatter` _num_ arg as string[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#engformatter-num-arg-as-string "Link to this heading")

Passing a string as _num_ argument when calling an instance of [`matplotlib.ticker.EngFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
 is deprecated and will be removed in 2.3.

### `mpl_toolkits.axes_grid` module[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#mpl-toolkits-axes-grid-module "Link to this heading")

All functionally from `mpl_toolkits.axes_grid` can be found in either [`mpl_toolkits.axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
 or [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
. Axes classes from `mpl_toolkits.axes_grid` based on `Axis` from [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
 can be found in [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
.

### `Axes` collision in `Figure.add_axes`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#axes-collision-in-figure-add-axes "Link to this heading")

Adding an axes instance to a figure by using the same arguments as for a previous axes instance currently reuses the earlier instance. This behavior has been deprecated in Matplotlib 2.1. In a future version, a _new_ instance will always be created and returned. Meanwhile, in such a situation, a deprecation warning is raised by `matplotlib.figure.AxesStack`.

This warning can be suppressed, and the future behavior ensured, by passing a _unique_ label to each axes instance. See the docstring of [`add_axes()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
 for more information.

Additional details on the rationale behind this deprecation can be found in [#7377](https://github.com/matplotlib/matplotlib/issues/7377/)
 and [#9024](https://github.com/matplotlib/matplotlib/issues/9024/)
.

### Former validators for `contour.negative_linestyle`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#former-validators-for-contour-negative-linestyle "Link to this heading")

The former public validation functions `validate_negative_linestyle` and `validate_negative_linestyle_legacy` will be deprecated in 2.1 and may be removed in 2.3. There are no public functions to replace them.

### `cbook`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#cbook "Link to this heading")

Many unused or near-unused [`matplotlib.cbook`](https://matplotlib.org/stable/api/cbook_api.html#module-matplotlib.cbook "matplotlib.cbook")
 functions and classes have been deprecated: `converter`, `tostr`, `todatetime`, `todate`, `tofloat`, `toint`, `unique`, `is_string_like`, `is_sequence_of_strings`, `is_scalar`, `Sorter`, `Xlator`, `soundex`, `Null`, `dict_delall`, `RingBuffer`, `get_split_ind`, `wrap`, `get_recursive_filelist`, `pieces`, `exception_to_str`, `allequal`, `alltrue`, `onetrue`, `allpairs`, `finddir`, `reverse_dict`, `restrict_dict`, `issubclass_safe`, `recursive_remove`, `unmasked_index_ranges`.

Code Removal[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#code-removal "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### qt4\_compat.py[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#qt4-compat-py "Link to this heading")

Moved to `qt_compat.py`. Renamed because it now handles Qt5 as well.

### Previously Deprecated methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#previously-deprecated-methods "Link to this heading")

The `GraphicsContextBase.set_graylevel`, `FigureCanvasBase.onHilite` and `mpl_toolkits.axes_grid1.mpl_axes.Axes.toggle_axisline` methods have been removed.

The `ArtistInspector.findobj` method, which was never working due to the lack of a `get_children` method, has been removed.

The deprecated `point_in_path`, `get_path_extents`, `point_in_path_collection`, `path_intersects_path`, `convert_path_to_polygons`, `cleanup_path` and `clip_path_to_rect` functions in the `matplotlib.path` module have been removed. Their functionality remains exposed as methods on the `Path` class.

The deprecated `Artist.get_axes` and `Artist.set_axes` methods have been removed

The `matplotlib.backends.backend_ps.seq_allequal` function has been removed. Use `np.array_equal` instead.

The deprecated `matplotlib.rcsetup.validate_maskedarray`, `matplotlib.rcsetup.deprecate_savefig_extension` and `matplotlib.rcsetup.validate_tkpythoninspect` functions, and associated `savefig.extension` and `tk.pythoninspect` rcparams entries have been removed.

The keyword argument _resolution_ of [`matplotlib.projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
 has been removed. It has deprecation with no effect from version _0.98.x_.

### `Axes.set_aspect("normal")`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#axes-set-aspect-normal "Link to this heading")

Support for setting an `Axes`'s aspect to `"normal"` has been removed, in favor of the synonym `"auto"`.

### `shading` kwarg to `pcolor`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#shading-kwarg-to-pcolor "Link to this heading")

The `shading` kwarg to [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 has been removed. Set `edgecolors` appropriately instead.

### Functions removed from the `lines` module[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#functions-removed-from-the-lines-module "Link to this heading")

The [`matplotlib.lines`](https://matplotlib.org/stable/api/lines_api.html#module-matplotlib.lines "matplotlib.lines")
 module no longer imports the `pts_to_prestep`, `pts_to_midstep` and `pts_to_poststep` functions from [`matplotlib.cbook`](https://matplotlib.org/stable/api/cbook_api.html#module-matplotlib.cbook "matplotlib.cbook")
.

### PDF backend functions[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#pdf-backend-functions "Link to this heading")

The methods `embedTeXFont` and `tex_font_mapping` of [`matplotlib.backends.backend_pdf.PdfFile`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile "matplotlib.backends.backend_pdf.PdfFile")
 have been removed. It is unlikely that external users would have called these methods, which are related to the font system internal to the PDF backend.

### matplotlib.delaunay[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.0.html#matplotlib-delaunay "Link to this heading")

Remove the delaunay triangulation code which is now handled by Qhull via [`matplotlib.tri`](https://matplotlib.org/stable/api/tri_api.html#module-matplotlib.tri "matplotlib.tri")
.

On this page
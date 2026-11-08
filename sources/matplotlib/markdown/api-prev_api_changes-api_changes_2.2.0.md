[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#main-content)

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
    

API Changes in 2.2.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#api-changes-in-2-2-0 "Link to this heading")

===============================================================================================================================================

New dependency[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#new-dependency "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

[kiwisolver](https://github.com/nucleic/kiwi)
 is now a required dependency to support the new constrained\_layout, see [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
 for more details.

Deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#deprecations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Classes, functions, and methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#classes-functions-and-methods "Link to this heading")

The unused and untested `Artist.onRemove` and `Artist.hitlist` methods have been deprecated.

The now unused `mlab.less_simple_linear_interpolation` function is deprecated.

The unused `ContourLabeler.get_real_label_width` method is deprecated.

The unused `FigureManagerBase.show_popup` method is deprecated. This introduced in e945059b327d42a99938b939a1be867fa023e7ba in 2005 but never built out into any of the backends.

`backend_tkagg.AxisMenu` is deprecated, as it has become unused since the removal of "classic" toolbars.

### Changed function signatures[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#changed-function-signatures "Link to this heading")

kwarg `fig` to [`GridSpec.get_subplot_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.get_subplot_params "matplotlib.gridspec.GridSpec.get_subplot_params")
 is deprecated, use `figure` instead.

Using [`pyplot.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
 with an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 as argument is deprecated. This sets the current axes, i.e. it has the same effect as [`pyplot.sca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.sca.html#matplotlib.pyplot.sca "matplotlib.pyplot.sca")
. For clarity `plt.sca(ax)` should be preferred over `plt.axes(ax)`.

Using strings instead of booleans to control grid and tick visibility is deprecated. Using `"on"`, `"off"`, `"true"`, or `"false"` to control grid and tick visibility has been deprecated. Instead, use normal booleans (`True`/`False`) or boolean-likes. In the future, all non-empty strings may be interpreted as `True`.

When given 2D inputs with non-matching numbers of columns, [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
 currently cycles through the columns of the narrower input, until all the columns of the wider input have been plotted. This behavior is deprecated; in the future, only broadcasting (1 column to _n_ columns) will be performed.

### rcparams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#rcparams "Link to this heading")

The `backend.qt4` and `backend.qt5` rcParams were deprecated in version 2.2. In order to force the use of a specific Qt binding, either import that binding first, or set the `QT_API` environment variable.

Deprecation of the `nbagg.transparent` rcParam. To control transparency of figure patches in the nbagg (or any other) backend, directly set `figure.patch.facecolor`, or the `figure.facecolor` rcParam.

### Deprecated `Axis.unit_data`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#deprecated-axis-unit-data "Link to this heading")

Use `Axis.units` (which has long existed) instead.

Removals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#removals "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

### Function Signatures[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#function-signatures "Link to this heading")

Contouring no longer supports `legacy` corner masking. The deprecated `ContourSet.vmin` and `ContourSet.vmax` properties have been removed.

Passing `None` instead of `"none"` as format to [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 is no longer supported.

The `bgcolor` keyword argument to `Axes` has been removed.

### Modules, methods, and functions[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#modules-methods-and-functions "Link to this heading")

The `matplotlib.finance`, `mpl_toolkits.exceltools` and `mpl_toolkits.gtktools` modules have been removed. `matplotlib.finance` remains available at [matplotlib/mpl\_finance](https://github.com/matplotlib/mpl_finance)
.

The `mpl_toolkits.mplot3d.art3d.iscolor` function has been removed.

The `Axes.get_axis_bgcolor`, `Axes.set_axis_bgcolor`, `Bbox.update_from_data`, `Bbox.update_datalim_numerix`, `MaxNLocator.bin_boundaries` methods have been removed.

`mencoder` can no longer be used to encode animations.

The unused `FONT_SCALE` and `fontd` attributes of the [`RendererSVG`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG "matplotlib.backends.backend_svg.RendererSVG")
 class have been removed.

### colormaps[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#colormaps "Link to this heading")

The `spectral` colormap has been removed. The `Vega*` colormaps, which were aliases for the `tab*` colormaps, have been removed.

### rcparams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#id1 "Link to this heading")

The following deprecated rcParams have been removed:

*   `axes.color_cycle` (see `axes.prop_cycle`),
    
*   `legend.isaxes`,
    
*   `svg.embed_char_paths` (see `svg.fonttype`),
    
*   `text.fontstyle`, `text.fontangle`, `text.fontvariant`, `text.fontweight`, `text.fontsize` (renamed to `text.style`, etc.),
    
*   `tick.size` (renamed to `tick.major.size`).
    

Only accept string-like for Categorical input[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#only-accept-string-like-for-categorical-input "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Do not accept mixed string / float / int input, only strings are valid categoricals.

Removal of unused imports[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#removal-of-unused-imports "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

Many unused imports were removed from the codebase. As a result, trying to import certain classes or functions from the "wrong" module (e.g. [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 from [`matplotlib.backends.backend_agg`](https://matplotlib.org/stable/api/backend_agg_api.html#module-matplotlib.backends.backend_agg "matplotlib.backends.backend_agg")
 instead of [`matplotlib.figure`](https://matplotlib.org/stable/api/figure_api.html#module-matplotlib.figure "matplotlib.figure")
) will now raise an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "(in Python v3.14)")
.

`Axes3D.get_xlim`, `get_ylim` and `get_zlim` now return a tuple[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#axes3d-get-xlim-get-ylim-and-get-zlim-now-return-a-tuple "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

They previously returned an array. Returning a tuple is consistent with the behavior for 2D axes.

Exception type changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#exception-type-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

If [`MovieWriterRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry "matplotlib.animation.MovieWriterRegistry")
 can't find the requested [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")
, a more helpful [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)")
 message is now raised instead of the previously raised [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)")
.

`matplotlib.tight_layout.auto_adjust_subplotpars` now raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
 instead of [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)")
 when sizes of input lists don't match

[`Figure.set_figwidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figwidth.html#matplotlib.figure.Figure.set_figwidth "matplotlib.figure.Figure.set_figwidth")
 and [`Figure.set_figheight`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figheight.html#matplotlib.figure.Figure.set_figheight "matplotlib.figure.Figure.set_figheight")
 default _forward_ to True[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#figure-set-figwidth-and-figure-set-figheight-default-forward-to-true "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`matplotlib.figure.Figure.set_figwidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figwidth.html#matplotlib.figure.Figure.set_figwidth "matplotlib.figure.Figure.set_figwidth")
 and [`matplotlib.figure.Figure.set_figheight`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figheight.html#matplotlib.figure.Figure.set_figheight "matplotlib.figure.Figure.set_figheight")
 had the keyword argument `forward=False` by default, but [`figure.Figure.set_size_inches`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html#matplotlib.figure.Figure.set_size_inches "matplotlib.figure.Figure.set_size_inches")
 now defaults to `forward=True`. This makes these functions consistent.

Do not truncate svg sizes to nearest point[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#do-not-truncate-svg-sizes-to-nearest-point "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There is no reason to size the SVG out put in integer points, change to out putting floats for the _height_, _width_, and _viewBox_ attributes of the _svg_ element.

Fontsizes less than 1 pt are clipped to be 1 pt.[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#fontsizes-less-than-1-pt-are-clipped-to-be-1-pt "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

FreeType doesn't allow fonts to get smaller than 1 pt, so all Agg backends were silently rounding up to 1 pt. PDF (other vector backends?) were letting us write fonts that were less than 1 pt, but they could not be placed properly because position information comes from FreeType. This change makes it so no backends can use fonts smaller than 1 pt, consistent with FreeType and ensuring more consistent results across backends.

Changes to Qt backend class MRO[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#changes-to-qt-backend-class-mro "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

To support both Agg and cairo rendering for Qt backends all of the non-Agg specific code previously in `backend_qt5agg.FigureCanvasQTAggBase` has been moved to `backend_qt5.FigureCanvasQT` so it can be shared with the cairo implementation. The `FigureCanvasQTAggBase.paintEvent`, `FigureCanvasQTAggBase.blit`, and `FigureCanvasQTAggBase.print_figure` methods have moved to `FigureCanvasQTAgg.paintEvent`, `FigureCanvasQTAgg.blit`, and `FigureCanvasQTAgg.print_figure`. The first two methods assume that the instance is also a `QWidget` so to use `FigureCanvasQTAggBase` it was required to multiple inherit from a `QWidget` sub-class.

Having moved all of its methods either up or down the class hierarchy `FigureCanvasQTAggBase` has been deprecated. To do this without warning and to preserve as much API as possible, `.backend_qt5agg.FigureCanvasQTAggBase` now inherits from `backend_qt5.FigureCanvasQTAgg`.

The MRO for `FigureCanvasQTAgg` and `FigureCanvasQTAggBase` used to be

\[matplotlib.backends.backend\_qt5agg.FigureCanvasQTAgg,\
 matplotlib.backends.backend\_qt5agg.FigureCanvasQTAggBase,\
 matplotlib.backends.backend\_agg.FigureCanvasAgg,\
 matplotlib.backends.backend\_qt5.FigureCanvasQT,\
 PyQt5.QtWidgets.QWidget,\
 PyQt5.QtCore.QObject,\
 sip.wrapper,\
 PyQt5.QtGui.QPaintDevice,\
 sip.simplewrapper,\
 matplotlib.backend\_bases.FigureCanvasBase,\
 object\]

and

\[matplotlib.backends.backend\_qt5agg.FigureCanvasQTAggBase,\
 matplotlib.backends.backend\_agg.FigureCanvasAgg,\
 matplotlib.backend\_bases.FigureCanvasBase,\
 object\]

respectively. They are now

\[matplotlib.backends.backend\_qt5agg.FigureCanvasQTAgg,\
 matplotlib.backends.backend\_agg.FigureCanvasAgg,\
 matplotlib.backends.backend\_qt5.FigureCanvasQT,\
 PyQt5.QtWidgets.QWidget,\
 PyQt5.QtCore.QObject,\
 sip.wrapper,\
 PyQt5.QtGui.QPaintDevice,\
 sip.simplewrapper,\
 matplotlib.backend\_bases.FigureCanvasBase,\
 object\]

and

\[matplotlib.backends.backend\_qt5agg.FigureCanvasQTAggBase,\
 matplotlib.backends.backend\_qt5agg.FigureCanvasQTAgg,\
 matplotlib.backends.backend\_agg.FigureCanvasAgg,\
 matplotlib.backends.backend\_qt5.FigureCanvasQT,\
 PyQt5.QtWidgets.QWidget,\
 PyQt5.QtCore.QObject,\
 sip.wrapper,\
 PyQt5.QtGui.QPaintDevice,\
 sip.simplewrapper,\
 matplotlib.backend\_bases.FigureCanvasBase,\
 object\]

[`axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 clips RGB values to the valid range[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#axes-axes-imshow-clips-rgb-values-to-the-valid-range "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When [`axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 is passed an RGB or RGBA value with out-of-range values, it now logs a warning and clips them to the valid range. The old behaviour, wrapping back in to the range, often hid outliers and made interpreting RGB images unreliable.

GTKAgg and GTKCairo backends deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.2.0.html#gtkagg-and-gtkcairo-backends-deprecated "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The GTKAgg and GTKCairo backends have been deprecated. These obsolete backends allow figures to be rendered via the GTK+ 2 toolkit. They are untested, known to be broken, will not work with Python 3, and their use has been discouraged for some time. Instead, use the `GTK3Agg` and `GTK3Cairo` backends for rendering to GTK+ 3 windows.

On this page
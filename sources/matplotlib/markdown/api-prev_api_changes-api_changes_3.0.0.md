[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#main-content)

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
    

API Changes for 3.0.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#api-changes-for-3-0-0 "Link to this heading")

=================================================================================================================================================

Drop support for python 2[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#drop-support-for-python-2 "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib 3 only supports python 3.5 and higher.

Changes to backend loading[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#changes-to-backend-loading "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Failure to load backend modules (`macosx` on non-framework builds and `gtk3` when running headless) now raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "(in Python v3.14)")
 (instead of [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)")
 and [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
, respectively).

Third-party backends that integrate with an interactive framework are now encouraged to define the `required_interactive_framework` global value to one of the following values: "qt5", "qt4", "gtk3", "wx", "tk", or "macosx". This information will be used to determine whether it is possible to switch from a backend to another (specifically, whether they use the same interactive framework).

[`Axes.hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")
 now uses [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 instead of [`pcolorfast`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#matplotlib.axes.Axes.pcolorfast "matplotlib.axes.Axes.pcolorfast")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#axes-hist2d-now-uses-pcolormesh-instead-of-pcolorfast "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Axes.hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")
 now uses [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 instead of [`pcolorfast`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#matplotlib.axes.Axes.pcolorfast "matplotlib.axes.Axes.pcolorfast")
, which will improve the handling of log-axes. Note that the returned _image_ now is of type [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 instead of [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
.

[`matplotlib.axes.Axes.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib.axes.Axes.get_tightbbox "matplotlib.axes.Axes.get_tightbbox")
 now includes all artists[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#matplotlib-axes-axes-get-tightbbox-now-includes-all-artists "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For Matplotlib 3.0, _all_ artists are now included in the bounding box returned by [`matplotlib.axes.Axes.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib.axes.Axes.get_tightbbox "matplotlib.axes.Axes.get_tightbbox")
.

[`matplotlib.axes.Axes.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib.axes.Axes.get_tightbbox "matplotlib.axes.Axes.get_tightbbox")
 adds a new kwarg `bbox_extra_artists` to manually specify the list of artists on the axes to include in the tight bounding box calculation.

Layout tools like [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
, `constrained_layout`, and `fig.savefig('fname.png', bbox_inches="tight")` use [`matplotlib.axes.Axes.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib.axes.Axes.get_tightbbox "matplotlib.axes.Axes.get_tightbbox")
 to determine the bounds of each axes on a figure and adjust spacing between axes.

In Matplotlib 2.2 `get_tightbbox` started to include legends made on the axes, but still excluded some other artists, like text that may overspill an axes. This has been expanded to include _all_ artists.

This new default may be overridden in either of three ways:

1.  Make the artist to be excluded a child of the figure, not the axes. E.g., call `fig.legend()` instead of `ax.legend()` (perhaps using [`get_legend_handles_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html#matplotlib.axes.Axes.get_legend_handles_labels "matplotlib.axes.Axes.get_legend_handles_labels")
     to gather handles and labels from the parent axes).
    
2.  If the artist is a child of the axes, set the artist property `artist.set_in_layout(False)`.
    
3.  Manually specify a list of artists in the new kwarg `bbox_extra_artists`.
    

[`Text.set_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text")
 with string argument `None` sets string to empty[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#text-set-text-with-string-argument-none-sets-string-to-empty "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Text.set_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text")
 when passed a string value of `None` would set the string to `"None"`, so subsequent calls to [`Text.get_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_text "matplotlib.text.Text.get_text")
 would return the ambiguous `"None"` string.

This change sets text objects passed `None` to have empty strings, so that [`Text.get_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_text "matplotlib.text.Text.get_text")
 returns an empty string.

`Axes3D.get_xlim`, `get_ylim` and `get_zlim` now return a tuple[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#axes3d-get-xlim-get-ylim-and-get-zlim-now-return-a-tuple "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

They previously returned an array. Returning a tuple is consistent with the behavior for 2D axes.

`font_manager.list_fonts` now follows the platform's casefolding semantics[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#font-manager-list-fonts-now-follows-the-platform-s-casefolding-semantics "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

i.e., it behaves case-insensitively on Windows only.

`bar` / `barh` no longer accepts `left` / `bottom` as first named argument[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#bar-barh-no-longer-accepts-left-bottom-as-first-named-argument "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These arguments were renamed in 2.0 to `x` / `y` following the change of the default alignment from `edge` to `center`.

Different exception types for undocumented options[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#different-exception-types-for-undocumented-options "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Passing `style='comma'` to [`ticklabel_format()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib.axes.Axes.ticklabel_format "matplotlib.axes.Axes.ticklabel_format")
     was never supported. It now raises `ValueError` like all other unsupported styles, rather than `NotImplementedError`.
    
*   Passing the undocumented `xmin` or `xmax` arguments to [`set_xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
     would silently override the `left` and `right` arguments. [`set_ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
     and the 3D equivalents (e.g. [`set_zlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim")
    ) had a corresponding problem. A `TypeError` will be raised if they would override the earlier limit arguments. In 3.0 these were kwargs were deprecated, but in 3.1 the deprecation was undone.
    

Improved call signature for `Axes.margins`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#improved-call-signature-for-axes-margins "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Axes.margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
 and [`Axes3D.margins`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.margins.html#mpl_toolkits.mplot3d.axes3d.Axes3D.margins "mpl_toolkits.mplot3d.axes3d.Axes3D.margins")
 no longer accept arbitrary keywords. `TypeError` will therefore be raised if unknown kwargs are passed; previously they would be silently ignored.

If too many positional arguments are passed, `TypeError` will be raised instead of `ValueError`, for consistency with other call-signature violations.

[`Axes3D.margins`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.margins.html#mpl_toolkits.mplot3d.axes3d.Axes3D.margins "mpl_toolkits.mplot3d.axes3d.Axes3D.margins")
 now raises `TypeError` instead of emitting a deprecation warning if only two positional arguments are passed. To supply only `x` and `y` margins, use keyword arguments.

Explicit arguments instead of \*args, \*\*kwargs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#explicit-arguments-instead-of-args-kwargs "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[**PEP 3102**](https://peps.python.org/pep-3102/)
 describes keyword-only arguments, which allow Matplotlib to provide explicit call signatures - where we previously used `*args, **kwargs` and `kwargs.pop`, we can now expose named arguments. In some places, unknown kwargs were previously ignored but now raise `TypeError` because `**kwargs` has been removed.

*   [`matplotlib.axes.Axes.stem()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
     no longer accepts unknown keywords, and raises `TypeError` instead of emitting a deprecation.
    
*   [`matplotlib.axes.Axes.stem()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
     now raises TypeError when passed unhandled positional arguments. If two or more arguments are passed (ie X, Y, \[linefmt\], ...) and Y cannot be cast to an array, an error will be raised instead of treating X as Y and Y as linefmt.
    
*   [`mpl_toolkits.axes_grid1.axes_divider.SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")
     raises `TypeError` instead of `Exception` when passed unknown kwargs.
    

Cleanup decorators and test classes no longer destroy warnings filter on exit[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#cleanup-decorators-and-test-classes-no-longer-destroy-warnings-filter-on-exit "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The decorators and classes in matplotlib.testing.decorators no longer destroy the warnings filter on exit. Instead, they restore the warnings filter that existed before the test started using `warnings.catch_warnings`.

Non-interactive FigureManager classes are now aliases of FigureManagerBase[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#non-interactive-figuremanager-classes-are-now-aliases-of-figuremanagerbase "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `FigureManagerPdf`, `FigureManagerPS`, and `FigureManagerSVG` classes, which were previously empty subclasses of [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")
 (i.e., not adding or overriding any attribute or method), are now direct aliases for [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")
.

Change to the output of [`image.thumbnail`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.thumbnail "matplotlib.image.thumbnail")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#change-to-the-output-of-image-thumbnail "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When called with `preview=False`, [`image.thumbnail`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.thumbnail "matplotlib.image.thumbnail")
 previously returned an figure whose canvas class was set according to the output file extension. It now returns a figure whose canvas class is the base [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
 (and relies on [`FigureCanvasBase.print_figure`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.print_figure "matplotlib.backend_bases.FigureCanvasBase.print_figure")
) to handle the canvas switching properly).

As a side effect of this change, [`image.thumbnail`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.thumbnail "matplotlib.image.thumbnail")
 now also supports .ps, .eps, and .svgz output.

[`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 now draws artists according to their zorder when blitting[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#funcanimation-now-draws-artists-according-to-their-zorder-when-blitting "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 now draws artists returned by the user- function according to their zorder when using blitting, instead of using the order in which they are being passed. However, note that only zorder of passed artists will be respected, as they are drawn on top of any existing artists (see [#11369](https://github.com/matplotlib/matplotlib/issues/11369)
).

Contour color autoscaling improvements[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#contour-color-autoscaling-improvements "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Selection of contour levels is now the same for contour and contourf; previously, for contour, levels outside the data range were deleted. (Exception: if no contour levels are found within the data range, the `levels` attribute is replaced with a list holding only the minimum of the data range.)

When contour is called with levels specified as a target number rather than a list, and the 'extend' kwarg is used, the levels are now chosen such that some data typically will fall in the extended range.

When contour is called with a [`LogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")
 or a [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
, it will now select colors using the geometric mean rather than the arithmetic mean of the contour levels.

Streamplot last row and column fixed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#streamplot-last-row-and-column-fixed "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A bug was fixed where the last row and column of data in [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
 were being dropped.

Changed default [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
 kwarg _interval\_multiples_ to `True`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#changed-default-autodatelocator-kwarg-interval-multiples-to-true "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default value of the tick locator for dates, [`dates.AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
 kwarg _interval\_multiples_ was set to `False` which leads to not-nice looking automatic ticks in many instances. The much nicer `interval_multiples=True` is the new default. See below to get the old behavior back:

([`Source code`](https://matplotlib.org/stable/_downloads/fdc1df0f609e6635dfd30e0709a5f479/api_changes_3-0-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9849d911edb3ce63462bb2f671722e1f/api_changes_3-0-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/274be763ffe285fe7b86680fbae4d516/api_changes_3-0-0-1.png)
)

[![](https://matplotlib.org/stable/_images/api-prev_api_changes-api_changes_3-0-0-1.2x.png)](https://matplotlib.org/stable/_images/api-prev_api_changes-api_changes_3-0-0-1.2x.png)

[`Axes.get_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_position.html#matplotlib.axes.Axes.get_position "matplotlib.axes.Axes.get_position")
 now returns actual position if aspect changed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#axes-get-position-now-returns-actual-position-if-aspect-changed "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Axes.get_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_position.html#matplotlib.axes.Axes.get_position "matplotlib.axes.Axes.get_position")
 used to return the original position unless a draw had been triggered or [`Axes.apply_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.apply_aspect.html#matplotlib.axes.Axes.apply_aspect "matplotlib.axes.Axes.apply_aspect")
 had been called, even if the kwarg _original_ was set to `False`. Now [`Axes.apply_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.apply_aspect.html#matplotlib.axes.Axes.apply_aspect "matplotlib.axes.Axes.apply_aspect")
 is called so `ax.get_position()` will return the new modified position. To get the old behavior use `ax.get_position(original=True)`.

The ticks for colorbar now adjust for the size of the colorbar[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#the-ticks-for-colorbar-now-adjust-for-the-size-of-the-colorbar "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Colorbar ticks now adjust for the size of the colorbar if the colorbar is made from a mappable that is not a contour or doesn't have a BoundaryNorm, or boundaries are not specified. If boundaries, etc are specified, the colorbar maintains the original behavior.

Colorbar for log-scaled hexbin[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#colorbar-for-log-scaled-hexbin "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using [`hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
 and plotting with a logarithmic color scale, the colorbar ticks are now correctly log scaled. Previously the tick values were linear scaled log(number of counts).

PGF backend now explicitly makes black text black[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#pgf-backend-now-explicitly-makes-black-text-black "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previous behavior with the pgf backend was for text specified as black to actually be the default color of whatever was rendering the pgf file (which was of course usually black). The new behavior is that black text is black, regardless of the default color. However, this means that there is no way to fall back on the default color of the renderer.

Blacklisted rcparams no longer updated by [`rcdefaults`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcdefaults "matplotlib.rcdefaults")
, [`rc_file_defaults`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file_defaults "matplotlib.rc_file_defaults")
, [`rc_file`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file "matplotlib.rc_file")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#blacklisted-rcparams-no-longer-updated-by-rcdefaults-rc-file-defaults-rc-file "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The rc modifier functions [`rcdefaults`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcdefaults "matplotlib.rcdefaults")
, [`rc_file_defaults`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file_defaults "matplotlib.rc_file_defaults")
 and [`rc_file`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file "matplotlib.rc_file")
 now ignore rcParams in the `matplotlib.style.core.STYLE_BLACKLIST` set. In particular, this prevents the `backend` and `interactive` rcParams from being incorrectly modified by these functions.

[`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
 now stores callbacks using stdlib's [`weakref.WeakMethod`](https://docs.python.org/3/library/weakref.html#weakref.WeakMethod "(in Python v3.14)")
s[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#callbackregistry-now-stores-callbacks-using-stdlib-s-weakref-weakmethods "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In particular, this implies that `CallbackRegistry.callbacks[signal]` is now a mapping of callback ids to [`weakref.WeakMethod`](https://docs.python.org/3/library/weakref.html#weakref.WeakMethod "(in Python v3.14)")
s (i.e., they need to be first called with no arguments to retrieve the method itself).

Changes regarding the text.latex.unicode rcParam[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#changes-regarding-the-text-latex-unicode-rcparam "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The rcParam now defaults to True and is deprecated (i.e., in future versions of Matplotlib, unicode input will always be supported).

Moreover, the underlying implementation now uses `\usepackage[utf8]{inputenc}` instead of `\usepackage{ucs}\usepackage[utf8x]{inputenc}`.

Return type of ArtistInspector.get\_aliases changed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#return-type-of-artistinspector-get-aliases-changed "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`ArtistInspector.get_aliases` previously returned the set of aliases as `{fullname: {alias1: None, alias2: None, ...}}`. The dict-to-None mapping was used to simulate a set in earlier versions of Python. It has now been replaced by a set, i.e. `{fullname: {alias1, alias2, ...}}`.

This value is also stored in `ArtistInspector.aliasd`, which has likewise changed.

Removed `pytz` as a dependency[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#removed-pytz-as-a-dependency "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Since `dateutil` and `pytz` both provide time zones, and matplotlib already depends on `dateutil`, matplotlib will now use `dateutil` time zones internally and drop the redundant dependency on `pytz`. While `dateutil` time zones are preferred (and currently recommended in the Python documentation), the explicit use of `pytz` zones is still supported.

Deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#deprecations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Modules[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#modules "Link to this heading")

The following modules are deprecated:

*   `matplotlib.compat.subprocess`. This was a python 2 workaround, but all the functionality can now be found in the python 3 standard library [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "(in Python v3.14)")
    .
    
*   `matplotlib.backends.wx_compat`. Python 3 is only compatible with wxPython 4, so support for wxPython 3 or earlier can be dropped.
    

### Classes, methods, functions, and attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#classes-methods-functions-and-attributes "Link to this heading")

The following classes, methods, functions, and attributes are deprecated:

*   `RcParams.msg_depr`, `RcParams.msg_depr_ignore`, `RcParams.msg_depr_set`, `RcParams.msg_obsolete`, `RcParams.msg_backend_obsolete`
    
*   `afm.parse_afm`
    
*   `backend_pdf.PdfFile.texFontMap`
    
*   `backend_pgf.get_texcommand`
    
*   `backend_ps.get_bbox`
    
*   `backend_qt5.FigureCanvasQT.keyAutoRepeat` (directly check `event.guiEvent.isAutoRepeat()` in the event handler to decide whether to handle autorepeated key presses).
    
*   `backend_qt5.error_msg_qt`, `backend_qt5.exception_handler`
    
*   `backend_wx.FigureCanvasWx.macros`
    
*   `backends.pylab_setup`
    
*   `cbook.GetRealpathAndStat`, `cbook.Locked`
    
*   `cbook.is_numlike` (use `isinstance(..., numbers.Number)` instead), `cbook.listFiles`, `cbook.unicode_safe`
    
*   `container.Container.set_remove_method`,
    
*   `contour.ContourLabeler.cl`, `.cl_xy`, and `.cl_cvalues`
    
*   `dates.DateFormatter.strftime_pre_1900`, `dates.DateFormatter.strftime`
    
*   `font_manager.TempCache`
    
*   `image._ImageBase.iterpnames`, use the `interpolation_names` property instead. (this affects classes that inherit from `_ImageBase` including [`FigureImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage "matplotlib.image.FigureImage")
    , [`BboxImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
    , and [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
    )
    
*   `mathtext.unichr_safe` (use `chr` instead)
    
*   `patches.Polygon.xy`
    
*   `table.Table.get_child_artists` (use `get_children` instead)
    
*   `testing.compare.ImageComparisonTest`, `testing.compare.compare_float`
    
*   `testing.decorators.CleanupTest`, `testing.decorators.skip_if_command_unavailable`
    
*   `FigureCanvasQT.keyAutoRepeat` (directly check `event.guiEvent.isAutoRepeat()` in the event handler to decide whether to handle autorepeated key presses)
    
*   `FigureCanvasWx.macros`
    
*   `_ImageBase.iterpnames`, use the `interpolation_names` property instead. (this affects classes that inherit from `_ImageBase` including [`FigureImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage "matplotlib.image.FigureImage")
    , [`BboxImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
    , and [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
    )
    
*   `patches.Polygon.xy`
    
*   `texmanager.dvipng_hack_alpha`
    
*   `text.Annotation.arrow`
    
*   `Legend.draggable()`, in favor of [`Legend.set_draggable()`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_draggable "matplotlib.legend.Legend.set_draggable")
    
    (`Legend.draggable` may be reintroduced as a property in future releases)
    
*   `textpath.TextToPath.tex_font_map`
    
*   `matplotlib.cbook.deprecation.mplDeprecation` will be removed in future versions. It is just an alias for `matplotlib.cbook.deprecation.MatplotlibDeprecationWarning`. Please use `matplotlib.cbook.MatplotlibDeprecationWarning` directly if necessary.
    
*   The `matplotlib.cbook.Bunch` class has been deprecated. Instead, use [`types.SimpleNamespace`](https://docs.python.org/3/library/types.html#types.SimpleNamespace "(in Python v3.14)")
     from the standard library which provides the same functionality.
    
*   `Axes.mouseover_set` is now a frozenset, and deprecated. Directly manipulate the artist's `.mouseover` attribute to change their mouseover status.
    

The following keyword arguments are deprecated:

*   passing `verts` to `Axes.scatter` (use `marker` instead)
    
*   passing `obj_type` to `cbook.deprecated`
    

The following call signatures are deprecated:

*   passing a `wx.EvtHandler` as first argument to `backend_wx.TimerWx`
    

### rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#rcparams "Link to this heading")

The following rcParams are deprecated:

*   `examples.directory` (use `datapath` instead)
    
*   `pgf.debug` (the pgf backend relies on logging)
    
*   `text.latex.unicode` (always True now)
    

### marker styles[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#marker-styles "Link to this heading")

*   Using `(n, 3)` as marker style to specify a circle marker is deprecated. Use `"o"` instead.
    
*   Using `([(x0, y0), (x1, y1), ...], 0)` as marker style to specify a custom marker path is deprecated. Use `[(x0, y0), (x1, y1), ...]` instead.
    

### Deprecation of `LocatableAxes` in toolkits[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#deprecation-of-locatableaxes-in-toolkits "Link to this heading")

The `LocatableAxes` classes in toolkits have been deprecated. The base [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 classes provide the same functionality to all subclasses, thus these mixins are no longer necessary. Related functions have also been deprecated. Specifically:

*   `mpl_toolkits.axes_grid1.axes_divider.LocatableAxesBase`: no specific replacement; use any other `Axes`\-derived class directly instead.
    
*   `mpl_toolkits.axes_grid1.axes_divider.locatable_axes_factory`: no specific replacement; use any other `Axes`\-derived class directly instead.
    
*   `mpl_toolkits.axes_grid1.axes_divider.Axes`: use [`mpl_toolkits.axes_grid1.mpl_axes.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
     directly.
    
*   `mpl_toolkits.axes_grid1.axes_divider.LocatableAxes`: use [`mpl_toolkits.axes_grid1.mpl_axes.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
     directly.
    
*   `mpl_toolkits.axisartist.axes_divider.Axes`: use [`mpl_toolkits.axisartist.axislines.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.axislines.Axes")
     directly.
    
*   `mpl_toolkits.axisartist.axes_divider.LocatableAxes`: use [`mpl_toolkits.axisartist.axislines.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.axislines.Axes")
     directly.
    

Removals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#removals "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

### Hold machinery[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#hold-machinery "Link to this heading")

Setting or unsetting `hold` ([deprecated in version 2.0](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.0.0.html#v200-deprecate-hold)
) has now been completely removed. Matplotlib now always behaves as if `hold=True`. To clear an axes you can manually use [`cla()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.cla.html#matplotlib.axes.Axes.cla "matplotlib.axes.Axes.cla")
, or to clear an entire figure use [`clear()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.clear.html#matplotlib.figure.Figure.clear "matplotlib.figure.Figure.clear")
.

### Removal of deprecated backends[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#removal-of-deprecated-backends "Link to this heading")

Deprecated backends have been removed:

*   GTKAgg
    
*   GTKCairo
    
*   GTK
    
*   GDK
    

### Deprecated APIs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#deprecated-apis "Link to this heading")

The following deprecated API elements have been removed:

*   The deprecated methods `knownfailureif` and `remove_text` have been removed from [`matplotlib.testing.decorators`](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing.decorators "matplotlib.testing.decorators")
    .
    
*   The entire contents of `testing.noseclasses` have also been removed.
    
*   `matplotlib.checkdep_tex`, `matplotlib.checkdep_xmllint`
    
*   `backend_bases.IdleEvent`
    
*   `cbook.converter`, `cbook.tostr`, `cbook.todatetime`, `cbook.todate`, `cbook.tofloat`, `cbook.toint`, `cbook.unique`, `cbook.is_string_like`, `cbook.is_sequence_of_strings`, `cbook.is_scalar`, `cbook.soundex`, `cbook.dict_delall`, `cbook.get_split_ind`, `cbook.wrap`, `cbook.get_recursive_filelist`, `cbook.pieces`, `cbook.exception_to_str`, `cbook.allequal`, `cbook.alltrue`, `cbook.onetrue`, `cbook.allpairs`, `cbook.finddir`, `cbook.reverse_dict`, `cbook.restrict_dict`, `cbook.issubclass_safe`, `cbook.recursive_remove`, `cbook.unmasked_index_ranges`, `cbook.Null`, `cbook.RingBuffer`, `cbook.Sorter`, `cbook.Xlator`,
    
*   `font_manager.weight_as_number`, `font_manager.ttfdict_to_fnames`
    
*   `pyplot.colors`, `pyplot.spectral`
    
*   `rcsetup.validate_negative_linestyle`, `rcsetup.validate_negative_linestyle_legacy`,
    
*   `testing.compare.verifiers`, `testing.compare.verify`
    
*   `testing.decorators.knownfailureif`, `testing.decorators.ImageComparisonTest.remove_text`
    
*   `tests.assert_str_equal`, `tests.test_tinypages.file_same`
    
*   `texmanager.dvipng_hack_alpha`,
    
*   `_AxesBase.axesPatch`, `_AxesBase.set_color_cycle`, `_AxesBase.get_cursor_props`, `_AxesBase.set_cursor_props`
    
*   `_ImageBase.iterpnames`
    
*   `FigureCanvasBase.start_event_loop_default`;
    
*   `FigureCanvasBase.stop_event_loop_default`;
    
*   `Figure.figurePatch`,
    
*   `FigureCanvasBase.dynamic_update`, `FigureCanvasBase.idle_event`, `FigureCanvasBase.get_linestyle`, `FigureCanvasBase.set_linestyle`
    
*   `FigureCanvasQTAggBase`
    
*   `FigureCanvasQTAgg.blitbox`
    
*   `FigureCanvasTk.show` (alternative: `FigureCanvasTk.draw`)
    
*   `FigureManagerTkAgg` (alternative: `FigureManagerTk`)
    
*   `NavigationToolbar2TkAgg` (alternative: `NavigationToolbar2Tk`)
    
*   `backend_wxagg.Toolbar` (alternative: `backend_wxagg.NavigationToolbar2WxAgg`)
    
*   `RendererAgg.debug()`
    
*   passing non-numbers to `EngFormatter.format_eng`
    
*   passing `frac` to `PolarAxes.set_theta_grids`
    
*   any mention of idle events
    

The following API elements have been removed:

*   `backend_cairo.HAS_CAIRO_CFFI`
    
*   `sphinxext.sphinx_version`
    

### Proprietary sphinx directives[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#proprietary-sphinx-directives "Link to this heading")

The matplotlib documentation used the proprietary sphinx directives `.. htmlonly::`, and `.. latexonly::`. These have been replaced with the standard sphinx directives `.. only:: html` and `.. only:: latex`. This change will not affect any users. Only downstream package maintainers, who have used the proprietary directives in their docs, will have to switch to the sphinx directives.

### lib/mpl\_examples symlink[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.0.html#lib-mpl-examples-symlink "Link to this heading")

The symlink from lib/mpl\_examples to ../examples has been removed. This is not installed as an importable package and should not affect end users, however this may require down-stream packagers to adjust. The content is still available top-level examples directory.

On this page
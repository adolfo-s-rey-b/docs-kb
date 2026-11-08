[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#main-content)

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
    

API Changes for 3.3.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#api-changes-for-3-3-0 "Link to this heading")

=================================================================================================================================================

[Behaviour changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#id1)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#behaviour-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `Formatter.fix_minus`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#formatter-fix-minus "Link to this heading")

[`Formatter.fix_minus`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.fix_minus "matplotlib.ticker.Formatter.fix_minus")
 now performs hyphen-to-unicode-minus replacement whenever `[rcParams["axes.unicode_minus"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.unicode_minus#rcparam-axes-unicode-minus) ` (default: `True`) is True; i.e. its behavior matches the one of `ScalarFormatter.fix_minus` ([`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 now just inherits that implementation).

This replacement is now used by the `format_data_short` method of the various builtin formatter classes, which affects the cursor value in the GUI toolbars.

### `FigureCanvasBase` now always has a `manager` attribute, which may be None[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#figurecanvasbase-now-always-has-a-manager-attribute-which-may-be-none "Link to this heading")

Previously, it did not necessarily have such an attribute. A check for `hasattr(figure.canvas, "manager")` should now be replaced by `figure.canvas.manager is not None` (or `getattr(figure.canvas, "manager", None) is not None` for back-compatibility).

### [`cbook.CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
 now propagates exceptions when no GUI event loop is running[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#cbook-callbackregistry-now-propagates-exceptions-when-no-gui-event-loop-is-running "Link to this heading")

[`cbook.CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
 now defaults to propagating exceptions thrown by callbacks when no interactive GUI event loop is running. If a GUI event loop _is_ running, [`cbook.CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
 still defaults to just printing a traceback, as unhandled exceptions can make the program completely `abort()` in that case.

### `Axes.locator_params()` validates `axis` parameter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axes-locator-params-validates-axis-parameter "Link to this heading")

[`axes.Axes.locator_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.locator_params.html#matplotlib.axes.Axes.locator_params "matplotlib.axes.Axes.locator_params")
 used to accept any value for `axis` and silently did nothing, when passed an unsupported value. It now raises a `ValueError`.

### `Axis.set_tick_params()` validates `which` parameter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axis-set-tick-params-validates-which-parameter "Link to this heading")

[`Axis.set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 (and the higher level [`axes.Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 and [`pyplot.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params "matplotlib.pyplot.tick_params")
) used to accept any value for `which` and silently did nothing, when passed an unsupported value. It now raises a `ValueError`.

### `Axis.set_ticklabels()` must match `FixedLocator.locs`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axis-set-ticklabels-must-match-fixedlocator-locs "Link to this heading")

If an axis is using a [`ticker.FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
, typically set by a call to [`Axis.set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")
, then the number of ticklabels supplied must match the number of locations available (`FixedFormattor.locs`). If not, a `ValueError` is raised.

### `backend_pgf.LatexManager.latex`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#backend-pgf-latexmanager-latex "Link to this heading")

`backend_pgf.LatexManager.latex` is now created with `encoding="utf-8"`, so its `stdin`, `stdout`, and `stderr` attributes are utf8-encoded.

### `pyplot.xticks()` and `pyplot.yticks()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#pyplot-xticks-and-pyplot-yticks "Link to this heading")

Previously, passing labels without passing the ticks to either [`pyplot.xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
 and [`pyplot.yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
 would result in:

TypeError: object of type 'NoneType' has no len()

It now raises a `TypeError` with a proper description of the error.

### Setting the same property under multiple aliases now raises a TypeError[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#setting-the-same-property-under-multiple-aliases-now-raises-a-typeerror "Link to this heading")

Previously, calling e.g. `plot(..., color=somecolor, c=othercolor)` would emit a warning because `color` and `c` actually map to the same Artist property. This now raises a TypeError.

### [`FileMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "matplotlib.animation.FileMovieWriter")
 temporary frames directory[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#filemoviewriter-temporary-frames-directory "Link to this heading")

[`FileMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "matplotlib.animation.FileMovieWriter")
 now defaults to writing temporary frames in a temporary directory, which is always cleared at exit. In order to keep the individual frames saved on the filesystem, pass an explicit _frame\_prefix_.

### [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 no longer accepts _x_ and _y_ being both 2D and with different numbers of columns[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axes-plot-no-longer-accepts-x-and-y-being-both-2d-and-with-different-numbers-of-columns "Link to this heading")

Previously, calling [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 e.g. with _x_ of shape `(n, 3)` and _y_ of shape `(n, 2)` would plot the first column of _x_ against the first column of _y_, the second column of _x_ against the second column of _y_, **and** the first column of _x_ against the third column of _y_. This now raises an error instead.

### [`Text.update_from`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.update_from "matplotlib.text.Text.update_from")
 now copies usetex state from the source Text[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#text-update-from-now-copies-usetex-state-from-the-source-text "Link to this heading")

### [`stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
 now defaults to `use_line_collection=True`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#stem-now-defaults-to-use-line-collection-true "Link to this heading")

This creates the stem plot as a [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 rather than individual [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 objects, greatly improving performance.

### rcParams color validator is now stricter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#rcparams-color-validator-is-now-stricter "Link to this heading")

Previously, rcParams entries whose values were color-like accepted "spurious" extra letters or characters in the "middle" of the string, e.g. `"(0, 1a, '0.5')"` would be interpreted as `(0, 1, 0.5)`. These extra characters (including the internal quotes) now cause a ValueError to be raised.

### [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
 now has a _base_ parameter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#symlognorm-now-has-a-base-parameter "Link to this heading")

Previously, [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
 had no _base_ keyword argument, and defaulted to `base=np.e` whereas the documentation said it was `base=10`. In preparation to make the default 10, calling [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
 without the new _base_ keyword argument emits a deprecation warning.

### [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 now color cycles when only errorbar color is set[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#errorbar-now-color-cycles-when-only-errorbar-color-is-set "Link to this heading")

Previously setting the _ecolor_ would turn off automatic color cycling for the plot, leading to the the lines and markers defaulting to whatever the first color in the color cycle was in the case of multiple plot calls.

### [`rcsetup.validate_color_for_prop_cycle`](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_color_for_prop_cycle "matplotlib.rcsetup.validate_color_for_prop_cycle")
 now always raises TypeError for bytes input[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#rcsetup-validate-color-for-prop-cycle-now-always-raises-typeerror-for-bytes-input "Link to this heading")

It previously raised [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
, **except** when the input was of the form `b"C[number]"` in which case it raised a ValueError.

### [`FigureCanvasPS.print_ps`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS.print_ps "matplotlib.backends.backend_ps.FigureCanvasPS.print_ps")
 and [`FigureCanvasPS.print_eps`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS.print_eps "matplotlib.backends.backend_ps.FigureCanvasPS.print_eps")
 no longer apply edgecolor and facecolor[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#figurecanvasps-print-ps-and-figurecanvasps-print-eps-no-longer-apply-edgecolor-and-facecolor "Link to this heading")

These methods now assume that the figure edge and facecolor have been correctly applied by [`FigureCanvasBase.print_figure`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.print_figure "matplotlib.backend_bases.FigureCanvasBase.print_figure")
, as they are normally called through it.

This behavior is consistent with other figure saving methods ([`FigureCanvasAgg.print_png`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_png "matplotlib.backends.backend_agg.FigureCanvasAgg.print_png")
, [`FigureCanvasPdf.print_pdf`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvasPdf.print_pdf "matplotlib.backends.backend_pdf.FigureCanvasPdf.print_pdf")
, [`FigureCanvasSVG.print_svg`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.print_svg "matplotlib.backends.backend_svg.FigureCanvasSVG.print_svg")
).

### [`pyplot.subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 now raises TypeError when given an incorrect number of arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#pyplot-subplot-now-raises-typeerror-when-given-an-incorrect-number-of-arguments "Link to this heading")

This is consistent with other signature mismatch errors. Previously a ValueError was raised.

### Shortcut for closing all figures[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#shortcut-for-closing-all-figures "Link to this heading")

Shortcuts for closing all figures now also work for the classic toolbar. There is no default shortcut any more because unintentionally closing all figures by a key press might happen too easily. You can configure the shortcut yourself using `[rcParams["keymap.quit_all"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.quit_all#rcparam-keymap-quit-all) ` (default: `[]`).

### Autoscale for arrow[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#autoscale-for-arrow "Link to this heading")

Calling ax.arrow() will now autoscale the axes.

### `set_tick_params(label1On=False)` now also makes the offset text (if any) invisible[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#set-tick-params-label1on-false-now-also-makes-the-offset-text-if-any-invisible "Link to this heading")

... because the offset text can rarely be interpreted without tick labels anyways.

### [`Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
 and [`pyplot.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")
 parameter name changed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axes-annotate-and-pyplot-annotate-parameter-name-changed "Link to this heading")

The parameter `s` to [`Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
 and [`pyplot.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")
 is renamed to `text`, matching [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
.

The old parameter name remains supported, but support for it will be dropped in a future Matplotlib release.

### [`font_manager.json_dump`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.json_dump "matplotlib.font_manager.json_dump")
 now locks the font manager dump file[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#font-manager-json-dump-now-locks-the-font-manager-dump-file "Link to this heading")

... to prevent multiple processes from writing to it at the same time.

### [`pyplot.rgrids`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rgrids.html#matplotlib.pyplot.rgrids "matplotlib.pyplot.rgrids")
 and [`pyplot.thetagrids`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.thetagrids.html#matplotlib.pyplot.thetagrids "matplotlib.pyplot.thetagrids")
 now act as setters also when called with only kwargs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#pyplot-rgrids-and-pyplot-thetagrids-now-act-as-setters-also-when-called-with-only-kwargs "Link to this heading")

Previously, keyword arguments were silently ignored when no positional arguments were given.

### [`Axis.get_minorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minorticklabels.html#matplotlib.axis.Axis.get_minorticklabels "matplotlib.axis.Axis.get_minorticklabels")
 and [`Axis.get_majorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_majorticklabels.html#matplotlib.axis.Axis.get_majorticklabels "matplotlib.axis.Axis.get_majorticklabels")
 now returns plain list[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axis-get-minorticklabels-and-axis-get-majorticklabels-now-returns-plain-list "Link to this heading")

Previously, [`Axis.get_minorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minorticklabels.html#matplotlib.axis.Axis.get_minorticklabels "matplotlib.axis.Axis.get_minorticklabels")
 and [`Axis.get_majorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_majorticklabels.html#matplotlib.axis.Axis.get_majorticklabels "matplotlib.axis.Axis.get_majorticklabels")
 returns silent\_list. Their return type is now changed to normal list. [`get_xminorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xminorticklabels.html#matplotlib.axes.Axes.get_xminorticklabels "matplotlib.axes.Axes.get_xminorticklabels")
, [`get_yminorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yminorticklabels.html#matplotlib.axes.Axes.get_yminorticklabels "matplotlib.axes.Axes.get_yminorticklabels")
, [`get_zminorticklabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zminorticklabels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zminorticklabels "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zminorticklabels")
, [`Axis.get_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "matplotlib.axis.Axis.get_ticklabels")
, [`get_xmajorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xmajorticklabels.html#matplotlib.axes.Axes.get_xmajorticklabels "matplotlib.axes.Axes.get_xmajorticklabels")
, [`get_ymajorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ymajorticklabels.html#matplotlib.axes.Axes.get_ymajorticklabels "matplotlib.axes.Axes.get_ymajorticklabels")
 and [`get_zmajorticklabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmajorticklabels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmajorticklabels "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmajorticklabels")
 methods will be affected by this change.

### Default slider formatter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#default-slider-formatter "Link to this heading")

The default method used to format [`Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 values has been changed to use a [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 adapted the slider values limits. This should ensure that values are displayed with an appropriate number of significant digits even if they are much smaller or much bigger than 1. To restore the old behavior, explicitly pass a "%1.2f" as the _valfmt_ parameter to [`Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
.

### Add _normalize_ keyword argument to `Axes.pie`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#add-normalize-keyword-argument-to-axes-pie "Link to this heading")

`pie()` used to draw a partial pie if the sum of the values was < 1. This behavior is deprecated and will change to always normalizing the values to a full pie by default. If you want to draw a partial pie, please pass `normalize=False` explicitly.

### `table.CustomCell` is now an alias for [`table.Cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell "matplotlib.table.Cell")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#table-customcell-is-now-an-alias-for-table-cell "Link to this heading")

All the functionality of `CustomCell` has been moved to its base class [`Cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell "matplotlib.table.Cell")
.

### wx Timer interval[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#wx-timer-interval "Link to this heading")

Setting the timer interval on a not-yet-started `TimerWx` won't start it anymore.

### "step"-type histograms default to the zorder of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#step-type-histograms-default-to-the-zorder-of-line2d "Link to this heading")

This ensures that they go above gridlines by default. The old `zorder` can be kept by passing it as a keyword argument to [`Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
.

### [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 and [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
 visibility[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#legend-and-offsetbox-visibility "Link to this heading")

[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 and [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
 subclasses ([`PaddedBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PaddedBox "matplotlib.offsetbox.PaddedBox")
, [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
, and [`AnnotationBbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
) no longer directly keep track of the visibility of their underlying [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 artist, but instead pass that flag down to the [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
.

### [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 and [`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")
 no longer allow invalid locations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#legend-and-table-no-longer-allow-invalid-locations "Link to this heading")

This affects legends produced on an Axes ([`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
 and [`pyplot.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
) and on a Figure ([`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
 and [`pyplot.figlegend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figlegend.html#matplotlib.pyplot.figlegend "matplotlib.pyplot.figlegend")
). Figure legends also no longer accept the unsupported `'best'` location. Previously, invalid Axes locations would use `'best'` and invalid Figure locations would used `'upper right'`.

### Passing Line2D's _drawstyle_ together with _linestyle_ is removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#passing-line2d-s-drawstyle-together-with-linestyle-is-removed "Link to this heading")

Instead of `plt.plot(..., linestyle="steps--")`, use `plt.plot(..., linestyle="--", drawstyle="steps")`. `ds` is also an alias for `drawstyle`.

### Upper case color strings[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#upper-case-color-strings "Link to this heading")

Support for passing single-letter colors (one of "rgbcmykw") as UPPERCASE characters is removed; these colors are now case-sensitive (lowercase).

### tight/constrained\_layout no longer worry about titles that are too wide[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#tight-constrained-layout-no-longer-worry-about-titles-that-are-too-wide "Link to this heading")

_tight\_layout_ and _constrained\_layout_ shrink axes to accommodate "decorations" on the axes. However, if an xlabel or title is too long in the x direction, making the axes smaller in the x-direction doesn't help. The behavior of both has been changed to ignore the width of the title and xlabel and the height of the ylabel in the layout logic.

This also means there is a new keyword argument for [`axes.Axes.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib.axes.Axes.get_tightbbox "matplotlib.axes.Axes.get_tightbbox")
 and [`axis.Axis.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tightbbox.html#matplotlib.axis.Axis.get_tightbbox "matplotlib.axis.Axis.get_tightbbox")
: `for_layout_only`, which defaults to _False_, but if _True_ returns a bounding box using the rules above.

### `[rcParams["savefig.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.facecolor#rcparam-savefig-facecolor) ` (default: `'auto'`) and `[rcParams["savefig.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.edgecolor#rcparam-savefig-edgecolor) ` (default: `'auto'`) now default to "auto"[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#rcparams-savefig-facecolor-default-auto-and-rcparams-savefig-edgecolor-default-auto-now-default-to-auto "Link to this heading")

This newly allowed value for `[rcParams["savefig.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.facecolor#rcparam-savefig-facecolor) ` (default: `'auto'`) and `[rcParams["savefig.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.edgecolor#rcparam-savefig-edgecolor) ` (default: `'auto'`), as well as the _facecolor_ and _edgecolor_ parameters to [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
, means "use whatever facecolor and edgecolor the figure current has".

### When using a single dataset, [`Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
 no longer wraps the added artist in a [`silent_list`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.silent_list "matplotlib.cbook.silent_list")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#when-using-a-single-dataset-axes-hist-no-longer-wraps-the-added-artist-in-a-silent-list "Link to this heading")

When [`Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
 is called with a single dataset, it adds to the axes either a [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 object (when `histtype="bar"` or `"barstacked"`), or a [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 object (when `histype="step"` or `"stepfilled"`) -- the latter being wrapped in a list-of-one-element. Previously, either artist would be wrapped in a [`silent_list`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.silent_list "matplotlib.cbook.silent_list")
. This is no longer the case: the [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 is now returned as is (this is an API breaking change if you were directly relying on the concrete [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")
 API; however, [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 inherits from [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
 so most common operations remain available), and the list-of-one [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 is returned as is. This makes the [`repr`](https://docs.python.org/3/library/functions.html#repr "(in Python v3.14)")
 of the returned artist more accurate: it is now

<BarContainer object of 10 artists\>  \# "bar", "barstacked"
\[<matplotlib.patches.Polygon object at 0xdeadbeef\>\]  \# "step", "stepfilled"

instead of

<a list of 10 Patch objects\>  \# "bar", "barstacked"
<a list of 1 Patch objects\>  \# "step", "stepfilled"

When [`Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
 is called with multiple artists, it still wraps its return value in a [`silent_list`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.silent_list "matplotlib.cbook.silent_list")
, but uses more accurate type information

<a list of 3 BarContainer objects\>  \# "bar", "barstacked"
<a list of 3 List\[Polygon\] objects\>  \# "step", "stepfilled"

instead of

<a list of 3 Lists of Patches objects\>  \# "bar", "barstacked"
<a list of 3 Lists of Patches objects\>  \# "step", "stepfilled"

### Qt and wx backends no longer create a status bar by default[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#qt-and-wx-backends-no-longer-create-a-status-bar-by-default "Link to this heading")

The coordinates information is now displayed in the toolbar, consistently with the other backends. This is intended to simplify embedding of Matplotlib in larger GUIs, where Matplotlib may control the toolbar but not the status bar.

### `[rcParams["text.hinting"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.hinting#rcparam-text-hinting) ` (default: `'default'`) now supports names mapping to FreeType flags[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#rcparams-text-hinting-default-default-now-supports-names-mapping-to-freetype-flags "Link to this heading")

`[rcParams["text.hinting"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.hinting#rcparam-text-hinting) ` (default: `'default'`) now supports the values "default", "no\_autohint", "force\_autohint", and "no\_hinting", which directly map to the FreeType flags FT\_LOAD\_DEFAULT, etc. The old synonyms (respectively "either", "native", "auto", and "none") are still supported, but their use is discouraged. To get normalized values, use [`backend_agg.get_hinting_flag`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.get_hinting_flag "matplotlib.backends.backend_agg.get_hinting_flag")
, which returns integer flag values.

### [`cbook.get_sample_data`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
 auto-loads numpy arrays[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#cbook-get-sample-data-auto-loads-numpy-arrays "Link to this heading")

When [`cbook.get_sample_data`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
 is used to load a npy or npz file and the keyword-only parameter `np_load` is True, the file is automatically loaded using [`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "(in NumPy v2.5)")
. `np_load` defaults to False for backwards compatibility, but will become True in a later release.

### `get_text_width_height_descent` now checks `ismath` rather than `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`)[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#get-text-width-height-descent-now-checks-ismath-rather-than-rcparams-text-usetex-default-false "Link to this heading")

... to determine whether a string should be passed to the usetex machinery or not. This allows single strings to be marked as not-usetex even when the rcParam is True.

### [`Axes.vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")
, [`Axes.hlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hlines.html#matplotlib.axes.Axes.hlines "matplotlib.axes.Axes.hlines")
, [`pyplot.vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")
 and [`pyplot.hlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html#matplotlib.pyplot.hlines "matplotlib.pyplot.hlines")
 _colors_ parameter default change[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axes-vlines-axes-hlines-pyplot-vlines-and-pyplot-hlines-colors-parameter-default-change "Link to this heading")

The _colors_ parameter will now default to `[rcParams["lines.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.color#rcparam-lines-color) ` (default: `'C0'`), while previously it defaulted to 'k'.

### Aggressively autoscale clim in `ScalerMappable` classes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#aggressively-autoscale-clim-in-scalermappable-classes "Link to this heading")

Previously some plotting methods would defer autoscaling until the first draw if only one of the _vmin_ or _vmax_ keyword arguments were passed ([`Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
, [`Axes.hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
, [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
, [`Axes.pcolorfast`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#matplotlib.axes.Axes.pcolorfast "matplotlib.axes.Axes.pcolorfast")
) but would scale based on the passed data if neither was passed (independent of the _norm_ keyword arguments). Other methods ([`Axes.pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
, [`Axes.pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
) always autoscaled base on the initial data.

All of the plotting methods now resolve the unset _vmin_ or _vmax_ at the initial call time using the data passed in.

If you were relying on exactly one of the _vmin_ or _vmax_ remaining unset between the time when the method is called and the first time the figure is rendered you get back the old behavior by manually setting the relevant limit back to [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

cm\_obj.norm.vmin \= None
\# or
cm\_obj.norm.vmax \= None

which will be resolved during the draw process.

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#id2)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `figure.add_axes()` without arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#figure-add-axes-without-arguments "Link to this heading")

Calling `fig.add_axes()` with no arguments currently does nothing. This call will raise an error in the future. Adding a free-floating axes needs a position rectangle. If you want a figure-filling single axes, use `add_subplot()` instead.

### `backend_wx.DEBUG_MSG`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#backend-wx-debug-msg "Link to this heading")

`backend_wx.DEBUG_MSG` is deprecated. The wx backends now use regular logging.

### `Colorbar.config_axis()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#colorbar-config-axis "Link to this heading")

`Colorbar.config_axis()` is considered internal. Its use is deprecated.

### `NonUniformImage.is_grayscale` and `PcolorImage.is_grayscale`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#nonuniformimage-is-grayscale-and-pcolorimage-is-grayscale "Link to this heading")

These attributes are deprecated, for consistency with `AxesImage.is_grayscale`, which was removed back in Matplotlib 2.0.0. (Note that previously, these attributes were only available _after rendering the image_).

### `den` parameter and attribute to [`mpl_toolkits.axisartist.angle_helper`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.html#module-mpl_toolkits.axisartist.angle_helper "mpl_toolkits.axisartist.angle_helper")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#den-parameter-and-attribute-to-mpl-toolkits-axisartist-angle-helper "Link to this heading")

For all locator classes defined in [`mpl_toolkits.axisartist.angle_helper`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.html#module-mpl_toolkits.axisartist.angle_helper "mpl_toolkits.axisartist.angle_helper")
, the `den` parameter has been renamed to `nbins`, and the `den` attribute deprecated in favor of its (preexisting) synonym `nbins`, for consistency with locator classes defined in [`matplotlib.ticker`](https://matplotlib.org/stable/api/ticker_api.html#module-matplotlib.ticker "matplotlib.ticker")
.

### `backend_pgf.LatexManager.latex_stdin_utf8`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#backend-pgf-latexmanager-latex-stdin-utf8 "Link to this heading")

`backend_pgf.LatexManager.latex` is now created with `encoding="utf-8"`, so its `stdin` attribute is already utf8-encoded; the `latex_stdin_utf8` attribute is thus deprecated.

### Flags containing "U" passed to [`cbook.to_filehandle`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.to_filehandle "matplotlib.cbook.to_filehandle")
 and [`cbook.open_file_cm`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.open_file_cm "matplotlib.cbook.open_file_cm")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#flags-containing-u-passed-to-cbook-to-filehandle-and-cbook-open-file-cm "Link to this heading")

Please remove "U" from flags passed to [`cbook.to_filehandle`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.to_filehandle "matplotlib.cbook.to_filehandle")
 and [`cbook.open_file_cm`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.open_file_cm "matplotlib.cbook.open_file_cm")
. This is consistent with their removal from [`open`](https://docs.python.org/3/library/functions.html#open "(in Python v3.14)")
 in Python 3.9.

### PDF and PS character tracking internals[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#pdf-and-ps-character-tracking-internals "Link to this heading")

The `used_characters` attribute and `track_characters` and `merge_used_characters` methods of [`RendererPdf`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf "matplotlib.backends.backend_pdf.RendererPdf")
, [`PdfFile`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile "matplotlib.backends.backend_pdf.PdfFile")
, and [`RendererPS`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS "matplotlib.backends.backend_ps.RendererPS")
 are deprecated.

### Case-insensitive capstyles and joinstyles[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#case-insensitive-capstyles-and-joinstyles "Link to this heading")

Please pass capstyles ("miter", "round", "bevel") and joinstyles ("butt", "round", "projecting") as lowercase.

### Passing raw data to `register_cmap()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#passing-raw-data-to-register-cmap "Link to this heading")

Passing raw data via parameters _data_ and _lut_ to `matplotlib.cm.register_cmap()` is deprecated. Instead, explicitly create a [`LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 and pass it via the _cmap_ parameter: `register_cmap(cmap=LinearSegmentedColormap(name, data, lut))`.

### `DateFormatter.illegal_s`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#dateformatter-illegal-s "Link to this heading")

This attribute is unused and deprecated.

### `widgets.TextBox.params_to_disable`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#widgets-textbox-params-to-disable "Link to this heading")

This attribute is deprecated.

### Revert deprecation \*min, \*max keyword arguments to `set_x/y/zlim_3d()`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#revert-deprecation-min-max-keyword-arguments-to-set-x-y-zlim-3d "Link to this heading")

These keyword arguments were deprecated in 3.0, alongside with the respective parameters in `set_xlim()` / `set_ylim()`. The deprecations of the 2D versions were already reverted in 3.1.

### `cbook.local_over_kwdict`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#cbook-local-over-kwdict "Link to this heading")

This function is deprecated. Use [`cbook.normalize_kwargs`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.normalize_kwargs "matplotlib.cbook.normalize_kwargs")
 instead.

### Passing both singular and plural _colors_, _linewidths_, _linestyles_ to [`Axes.eventplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.eventplot.html#matplotlib.axes.Axes.eventplot "matplotlib.axes.Axes.eventplot")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#passing-both-singular-and-plural-colors-linewidths-linestyles-to-axes-eventplot "Link to this heading")

Passing e.g. both _linewidth_ and _linewidths_ will raise a TypeError in the future.

### Setting `text.latex.preamble` or `pdf.preamble` rcParams to non-strings[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#setting-text-latex-preamble-or-pdf-preamble-rcparams-to-non-strings "Link to this heading")

These rcParams should be set to string values. Support for None (meaning the empty string) and lists of strings (implicitly joined with newlines) is deprecated.

### Parameters _norm_ and _vmin_/_vmax_ should not be used simultaneously[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#parameters-norm-and-vmin-vmax-should-not-be-used-simultaneously "Link to this heading")

Passing parameters _norm_ and _vmin_/_vmax_ simultaneously to functions using colormapping such as `scatter()` and `imshow()` is deprecated. Instead of `norm=LogNorm(), vmin=min_val, vmax=max_val` pass `norm=LogNorm(min_val, max_val)`. _vmin_ and _vmax_ should only be used without setting _norm_.

### Effectless parameters of [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 and [`matplotlib.colorbar.Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#effectless-parameters-of-figure-colorbar-and-matplotlib-colorbar-colorbar "Link to this heading")

The _cmap_ and _norm_ parameters of [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 and [`matplotlib.colorbar.Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 have no effect because they are always overridden by the mappable's colormap and norm; they are thus deprecated. Likewise, passing the _alpha_, _boundaries_, _values_, _extend_, or _filled_ parameters with a [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 mappable, or the _alpha_ parameter with an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 mappable, is deprecated, as the mappable would likewise override them.

### `args_key` and `exec_key` attributes of builtin [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")
s[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#args-key-and-exec-key-attributes-of-builtin-moviewriters "Link to this heading")

These attributes are deprecated.

### Unused parameters[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#unused-parameters "Link to this heading")

The following parameters do not have any effect and are deprecated:

*   arbitrary keyword arguments to `StreamplotSet`
    
*   parameter _quantize_ of [`Path.cleaned()`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.cleaned "matplotlib.path.Path.cleaned")
    
*   parameter _s_ of [`AnnotationBbox.get_fontsize()`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.get_fontsize "matplotlib.offsetbox.AnnotationBbox.get_fontsize")
    
*   parameter _label_ of [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
    

### Passing _props_ to [`Shadow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#passing-props-to-shadow "Link to this heading")

The parameter _props_ of [`Shadow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
 is deprecated. Use keyword arguments instead.

### `Axes.update_datalim_bounds`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axes-update-datalim-bounds "Link to this heading")

This method is deprecated. Use `ax.dataLim.set(Bbox.union([ax.dataLim, bounds]))` instead.

### `{,Symmetrical}LogScale.{,Inverted}LogTransform`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#symmetrical-logscale-inverted-logtransform "Link to this heading")

`LogScale.LogTransform`, `LogScale.InvertedLogTransform`, `SymmetricalScale.SymmetricalTransform` and `SymmetricalScale.InvertedSymmetricalTransform` are deprecated. Directly access the transform classes from the [`scale`](https://matplotlib.org/stable/api/scale_api.html#module-matplotlib.scale "matplotlib.scale")
 module.

### `TexManager.cachedir`, `TexManager.rgba_arrayd`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#texmanager-cachedir-texmanager-rgba-arrayd "Link to this heading")

Use [`matplotlib.get_cachedir()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_cachedir "matplotlib.get_cachedir")
 instead for the former; there is no replacement for the latter.

### Setting [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
's pickradius via [`Line2D.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker "matplotlib.lines.Line2D.set_picker")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#setting-line2d-s-pickradius-via-line2d-set-picker "Link to this heading")

Setting a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
's pickradius (i.e. the tolerance for pick events and containment checks) via [`Line2D.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker "matplotlib.lines.Line2D.set_picker")
 is deprecated. Use [`Line2D.set_pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_pickradius "matplotlib.lines.Line2D.set_pickradius")
 instead.

[`Line2D.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker "matplotlib.lines.Line2D.set_picker")
 no longer sets the artist's custom-contain() check.

### `Artist.set_contains`, `Artist.get_contains`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#artist-set-contains-artist-get-contains "Link to this heading")

Setting a custom method overriding [`Artist.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib.artist.Artist.contains "matplotlib.artist.Artist.contains")
 is deprecated. There is no replacement, but you may still customize pick events using [`Artist.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker")
.

### [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#colorbar-methods "Link to this heading")

The `on_mappable_changed` and `update_bruteforce` methods of [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 are deprecated; both can be replaced by calls to [`update_normal`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.update_normal "matplotlib.colorbar.Colorbar.update_normal")
.

### `OldScalarFormatter`, `IndexFormatter` and `IndexDateFormatter`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#oldscalarformatter-indexformatter-and-indexdateformatter "Link to this heading")

These formatters are deprecated. Their functionality can be implemented using e.g. [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
.

### `OldAutoLocator`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#oldautolocator "Link to this heading")

This ticker is deprecated.

### _required_, _forbidden_ and _allowed_ parameters of [`cbook.normalize_kwargs`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.normalize_kwargs "matplotlib.cbook.normalize_kwargs")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#required-forbidden-and-allowed-parameters-of-cbook-normalize-kwargs "Link to this heading")

These parameters are deprecated.

### The `TTFPATH` and `AFMPATH` environment variables[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#the-ttfpath-and-afmpath-environment-variables "Link to this heading")

Support for the (undocumented) `TTFPATH` and `AFMPATH` environment variables is deprecated. Additional fonts may be registered using `matplotlib.font_manager.fontManager.addfont()`.

### `matplotlib.compat`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#matplotlib-compat "Link to this heading")

This module is deprecated.

### `matplotlib.backends.qt_editor.formsubplottool`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#matplotlib-backends-qt-editor-formsubplottool "Link to this heading")

This module is deprecated. Use `matplotlib.backends.backend_qt5.SubplotToolQt` instead.

### AVConv animation writer deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#avconv-animation-writer-deprecated "Link to this heading")

The `AVConvBase`, `AVConvWriter` and `AVConvFileWriter` classes, and the associated `animation.avconv_path` and `animation.avconv_args` rcParams are deprecated.

Debian 8 (2015, EOL 06/2020) and Ubuntu 14.04 (EOL 04/2019) were the last versions of Debian and Ubuntu to ship avconv. It remains possible to force the use of avconv by using the ffmpeg-based writers with `[rcParams["animation.ffmpeg_path"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.ffmpeg_path#rcparam-animation-ffmpeg-path) ` (default: `'ffmpeg'`) set to "avconv".

### log/symlog scale base, ticks, and nonpos specification[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#log-symlog-scale-base-ticks-and-nonpos-specification "Link to this heading")

[`semilogx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogx.html#matplotlib.axes.Axes.semilogx "matplotlib.axes.Axes.semilogx")
, [`semilogy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogy.html#matplotlib.axes.Axes.semilogy "matplotlib.axes.Axes.semilogy")
, [`loglog`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html#matplotlib.axes.Axes.loglog "matplotlib.axes.Axes.loglog")
, [`LogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale "matplotlib.scale.LogScale")
, and [`SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
 used to take keyword arguments that depends on the axis orientation ("basex" vs "basey", "subsx" vs "subsy", "nonposx" vs "nonposy"); these parameter names are now deprecated in favor of "base", "subs", "nonpositive". This deprecation also affects e.g. `ax.set_yscale("log", basey=...)` which must now be spelled `ax.set_yscale("log", base=...)`.

The change from "nonpos" to "nonpositive" also affects [`LogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform "matplotlib.scale.LogTransform")
, [`InvertedLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform "matplotlib.scale.InvertedLogTransform")
, [`SymmetricalLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform "matplotlib.scale.SymmetricalLogTransform")
, etc.

To use _different_ bases for the x-axis and y-axis of a [`loglog`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html#matplotlib.axes.Axes.loglog "matplotlib.axes.Axes.loglog")
 plot, use e.g. `ax.set_xscale("log", base=10); ax.set_yscale("log", base=2)`.

### `DraggableBase.artist_picker`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#draggablebase-artist-picker "Link to this heading")

This method is deprecated. If you previously reimplemented it in a subclass, set the artist's picker instead with [`Artist.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker")
.

### _clear\_temp_ parameter and attribute of [`FileMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "matplotlib.animation.FileMovieWriter")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#clear-temp-parameter-and-attribute-of-filemoviewriter "Link to this heading")

The _clear\_temp_ parameter and attribute of [`FileMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "matplotlib.animation.FileMovieWriter")
 is deprecated. In the future, files placed in a temporary directory (using `frame_prefix=None`, the default) will be cleared; files placed elsewhere will not.

### Deprecated rcParams validators[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#deprecated-rcparams-validators "Link to this heading")

The following validators, defined in [`rcsetup`](https://matplotlib.org/stable/api/rcsetup_api.html#module-matplotlib.rcsetup "matplotlib.rcsetup")
, are deprecated: `validate_fontset`, `validate_mathtext_default`, `validate_alignment`, `validate_svg_fonttype`, `validate_pgf_texsystem`, `validate_movie_frame_fmt`, `validate_axis_locator`, `validate_movie_html_fmt`, `validate_grid_axis`, `validate_axes_titlelocation`, `validate_toolbar`, `validate_ps_papersize`, `validate_legend_loc`, `validate_bool_maybe_none`, `validate_hinting`, `validate_movie_writer`, `validate_webagg_address`, `validate_nseq_float`, `validate_nseq_int`. To test whether an rcParam value would be acceptable, one can test e.g. `rc = RcParams(); rc[k] = v` raises an exception.

### Stricter rcParam validation[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#stricter-rcparam-validation "Link to this heading")

`[rcParams["axes.axisbelow"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.axisbelow#rcparam-axes-axisbelow) ` (default: `'line'`) currently normalizes all strings starting with "line" (case-insensitive) to the option "line". This is deprecated; in a future version only the exact string "line" (case-sensitive) will be supported.

### `add_subplot()` validates its inputs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#add-subplot-validates-its-inputs "Link to this heading")

In particular, for `add_subplot(rows, cols, index)`, all parameters must be integral. Previously strings and floats were accepted and converted to int. This will now emit a deprecation warning.

### Toggling axes navigation from the keyboard using "a" and digit keys[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#toggling-axes-navigation-from-the-keyboard-using-a-and-digit-keys "Link to this heading")

Axes navigation can still be toggled programmatically using [`Axes.set_navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate")
.

The following related APIs are also deprecated: `backend_tools.ToolEnableAllNavigation`, `backend_tools.ToolEnableNavigation`, and `rcParams["keymap.all_axes"]`.

### `matplotlib.test(recursionlimit=...)`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#matplotlib-test-recursionlimit "Link to this heading")

The _recursionlimit_ parameter of `matplotlib.test` is deprecated.

### mathtext glues[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#mathtext-glues "Link to this heading")

The _copy_ parameter of `mathtext.Glue` is deprecated (the underlying glue spec is now immutable). `mathtext.GlueSpec` is deprecated.

### Signatures of [`Artist.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#matplotlib.artist.Artist.draw "matplotlib.artist.Artist.draw")
 and [`matplotlib.axes.Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#signatures-of-artist-draw-and-matplotlib-axes-axes-draw "Link to this heading")

The _inframe_ parameter to [`matplotlib.axes.Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw")
 is deprecated. Use [`Axes.redraw_in_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.redraw_in_frame.html#matplotlib.axes.Axes.redraw_in_frame "matplotlib.axes.Axes.redraw_in_frame")
 instead.

Not passing the _renderer_ parameter to [`matplotlib.axes.Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw")
 is deprecated. Use `axes.draw_artist(axes)` instead.

These changes make the signature of the `draw` (`artist.draw(renderer)`) method consistent across all artists; thus, additional parameters to [`Artist.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#matplotlib.artist.Artist.draw "matplotlib.artist.Artist.draw")
 are deprecated.

### `DraggableBase.on_motion_blit`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#draggablebase-on-motion-blit "Link to this heading")

This method is deprecated. [`DraggableBase.on_motion`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.on_motion "matplotlib.offsetbox.DraggableBase.on_motion")
 now handles both the blitting and the non-blitting cases.

### Passing the dash offset as None[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#passing-the-dash-offset-as-none "Link to this heading")

Fine control of dash patterns can be achieved by passing an `(offset, (on-length, off-length, on-length, off-length, ...))` pair as the linestyle property of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 and [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
. Previously, certain APIs would accept `offset = None` as a synonym for `offset = 0`, but this was never universally implemented, e.g. for vector output. Support for `offset = None` is deprecated, set the offset to 0 instead.

### `RendererCairo.fontweights`, `RendererCairo.fontangles`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#renderercairo-fontweights-renderercairo-fontangles "Link to this heading")

... are deprecated.

### `autofmt_xdate(which=None)`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#autofmt-xdate-which-none "Link to this heading")

This is deprecated, use its more explicit synonym, `which="major"`, instead.

### JPEG options[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#jpeg-options "Link to this heading")

The _quality_, _optimize_, and _progressive_ keyword arguments to [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
, which were only used when saving to JPEG, are deprecated. The `savefig.jpeg_quality` rcParam is likewise deprecated.

Such options should now be directly passed to Pillow using `savefig(..., pil_kwargs={"quality": ..., "optimize": ..., "progressive": ...})`.

### `dviread.Encoding`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#dviread-encoding "Link to this heading")

This class was (mostly) broken and is deprecated.

### Axis and Locator `pan` and `zoom`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axis-and-locator-pan-and-zoom "Link to this heading")

The unused `pan` and `zoom` methods of [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 and [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 are deprecated. Panning and zooming are now implemented using the `start_pan`, `drag_pan`, and `end_pan` methods of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.

### Passing None to various Axes subclass factories[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#passing-none-to-various-axes-subclass-factories "Link to this heading")

Support for passing `None` as base class to `axes.subplot_class_factory`, `axes_grid1.parasite_axes.host_axes_class_factory`, `axes_grid1.parasite_axes.host_subplot_class_factory`, `axes_grid1.parasite_axes.parasite_axes_class_factory`, and `axes_grid1.parasite_axes.parasite_axes_auxtrans_class_factory` is deprecated. Explicitly pass the correct base `Axes` class instead.

### `axes_rgb`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axes-rgb "Link to this heading")

In [`mpl_toolkits.axes_grid1.axes_rgb`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.html#module-mpl_toolkits.axes_grid1.axes_rgb "mpl_toolkits.axes_grid1.axes_rgb")
, `imshow_rgb` is deprecated (use `ax.imshow(np.dstack([r, g, b]))` instead); `RGBAxesBase` is deprecated (use `RGBAxes` instead); `RGBAxes.add_RGB_to_figure` is deprecated (it was an internal helper).

### `Substitution.from_params`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#substitution-from-params "Link to this heading")

This method is deprecated. If needed, directly assign to the `params` attribute of the Substitution object.

### PGF backend cleanups[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#pgf-backend-cleanups "Link to this heading")

The _dummy_ parameter of [`RendererPgf`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf "matplotlib.backends.backend_pgf.RendererPgf")
 is deprecated.

`GraphicsContextPgf` is deprecated (use [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
 instead).

### `set_factor` method of [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
 locators[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#set-factor-method-of-mpl-toolkits-axisartist-locators "Link to this heading")

The `set_factor` method of [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
 locators (which are different from "standard" Matplotlib tick locators) is deprecated.

### [`widgets.SubplotTool`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SubplotTool.html#matplotlib.widgets.SubplotTool "matplotlib.widgets.SubplotTool")
 callbacks and axes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#widgets-subplottool-callbacks-and-axes "Link to this heading")

The `funcleft`, `funcright`, `funcbottom`, `functop`, `funcwspace`, and `funchspace` methods of [`widgets.SubplotTool`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SubplotTool.html#matplotlib.widgets.SubplotTool "matplotlib.widgets.SubplotTool")
 are deprecated.

The `axleft`, `axright`, `axbottom`, `axtop`, `axwspace`, and `axhspace` attributes of [`widgets.SubplotTool`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SubplotTool.html#matplotlib.widgets.SubplotTool "matplotlib.widgets.SubplotTool")
 are deprecated. Access the `ax` attribute of the corresponding slider, if needed.

### mathtext `Glue` helper classes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#mathtext-glue-helper-classes "Link to this heading")

The `Fil`, `Fill`, `Filll`, `NegFil`, `NegFill`, `NegFilll`, and `SsGlue` classes in the [`matplotlib.mathtext`](https://matplotlib.org/stable/api/mathtext_api.html#module-matplotlib.mathtext "matplotlib.mathtext")
 module are deprecated. As an alternative, directly construct glue instances with `Glue("fil")`, etc.

### NavigationToolbar2.\_init\_toolbar[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#navigationtoolbar2-init-toolbar "Link to this heading")

Overriding this method to initialize third-party toolbars is deprecated. Instead, the toolbar should be initialized in the `__init__` method of the subclass (which should call the base-class' `__init__` as appropriate). To keep back-compatibility with earlier versions of Matplotlib (which _required_ `_init_toolbar` to be overridden), a fully empty implementation (`def _init_toolbar(self): pass`) may be kept and will not trigger the deprecation warning.

### NavigationToolbar2QT.parent and .basedir[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#navigationtoolbar2qt-parent-and-basedir "Link to this heading")

These attributes are deprecated. In order to access the parent window, use `toolbar.canvas.parent()`. Once the deprecation period is elapsed, it will also be accessible as `toolbar.parent()`. The base directory to the icons is `os.path.join(mpl.get_data_path(), "images")`.

### NavigationToolbar2QT.ctx[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#navigationtoolbar2qt-ctx "Link to this heading")

This attribute is deprecated.

### NavigationToolbar2Wx attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#navigationtoolbar2wx-attributes "Link to this heading")

The `prevZoomRect`, `retinaFix`, `savedRetinaImage`, `wxoverlay`, `zoomAxes`, `zoomStartX`, and `zoomStartY` attributes are deprecated.

### NavigationToolbar2.press and .release[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#navigationtoolbar2-press-and-release "Link to this heading")

These methods were called when pressing or releasing a mouse button, but _only_ when an interactive pan or zoom was occurring (contrary to what the docs stated). They are deprecated; if you write a backend which needs to customize such events, please directly override `press_pan`/`press_zoom`/`release_pan`/`release_zoom` instead.

### FigureCanvasGTK3.\_renderer\_init[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#figurecanvasgtk3-renderer-init "Link to this heading")

Overriding this method to initialize renderers for GTK3 canvases is deprecated. Instead, the renderer should be initialized in the `__init__` method of the subclass (which should call the base-class' `__init__` as appropriate). To keep back-compatibility with earlier versions of Matplotlib (which _required_ `_renderer_init` to be overridden), a fully empty implementation (`def _renderer_init(self): pass`) may be kept and will not trigger the deprecation warning.

### Path helpers in [`bezier`](https://matplotlib.org/stable/api/bezier_api.html#module-matplotlib.bezier "matplotlib.bezier")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#path-helpers-in-bezier "Link to this heading")

`bezier.make_path_regular` is deprecated. Use `Path.cleaned()` (or `Path.cleaned(curves=True)`, etc.) instead (but note that these methods add a `STOP` code at the end of the path).

`bezier.concatenate_paths` is deprecated. Use `Path.make_compound_path()` instead.

### `animation.html_args` rcParam[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#animation-html-args-rcparam "Link to this heading")

The unused `animation.html_args` rcParam and `animation.HTMLWriter.args_key` attribute are deprecated.

### `text.latex.preview` rcParam[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#text-latex-preview-rcparam "Link to this heading")

This rcParam, which controlled the use of the preview.sty LaTeX package to align TeX string baselines, is deprecated, as Matplotlib's own dvi parser now computes baselines just as well as preview.sty.

### `SubplotSpec.get_rows_columns`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#subplotspec-get-rows-columns "Link to this heading")

This method is deprecated. Use the `GridSpec.nrows`, `GridSpec.ncols`, `SubplotSpec.rowspan`, and `SubplotSpec.colspan` properties instead.

### Qt4-based backends[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#qt4-based-backends "Link to this heading")

The qt4agg and qt4cairo backends are deprecated. Qt4 has reached its end-of-life in 2015 and there are no releases for recent versions of Python. Please consider switching to Qt5.

### _fontdict_ and _minor_ parameters of [`Axes.set_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
 and [`Axes.set_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
 will become keyword-only[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#fontdict-and-minor-parameters-of-axes-set-xticklabels-and-axes-set-yticklabels-will-become-keyword-only "Link to this heading")

### All parameters of [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 except _nrows_ and _ncols_ will become keyword-only[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#all-parameters-of-figure-subplots-except-nrows-and-ncols-will-become-keyword-only "Link to this heading")

This avoids typing e.g. `subplots(1, 1, 1)` when meaning `subplot(1, 1, 1)`, but actually getting `subplots(1, 1, sharex=1)`.

### `RendererWx.get_gc`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#rendererwx-get-gc "Link to this heading")

This method is deprecated. Access the `gc` attribute directly instead.

### _add\_all_ parameter in `axes_grid`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#add-all-parameter-in-axes-grid "Link to this heading")

The _add\_all_ parameter of [`axes_grid1.axes_grid.Grid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.axes_grid.Grid")
, [`axes_grid1.axes_grid.ImageGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.axes_grid.ImageGrid")
, [`axes_grid1.axes_rgb.make_rgb_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes.html#mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes "mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes")
 and [`axes_grid1.axes_rgb.RGBAxes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#mpl_toolkits.axes_grid1.axes_rgb.RGBAxes "mpl_toolkits.axes_grid1.axes_rgb.RGBAxes")
 is deprecated. Axes are now always added to the parent figure, though they can be later removed with `ax.remove()`.

### `BboxBase.inverse_transformed`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#bboxbase-inverse-transformed "Link to this heading")

`.BboxBase.inverse_transformed` is deprecated (call [`BboxBase.transformed`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.transformed "matplotlib.transforms.BboxBase.transformed")
 on the [`inverted()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "matplotlib.transforms.Transform.inverted")
 transform instead).

### _orientation_ of `eventplot()` and [`EventCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#orientation-of-eventplot-and-eventcollection "Link to this heading")

Setting the _orientation_ of an `eventplot()` or [`EventCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
 to "none" or None is deprecated; set it to "horizontal" instead. Moreover, the two orientations ("horizontal" and "vertical") will become case-sensitive in the future.

### _minor_ kwarg to [`Axis.get_ticklocs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklocs.html#matplotlib.axis.Axis.get_ticklocs "matplotlib.axis.Axis.get_ticklocs")
 will become keyword-only[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#minor-kwarg-to-axis-get-ticklocs-will-become-keyword-only "Link to this heading")

Passing this argument positionally is deprecated.

### Case-insensitive properties[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#case-insensitive-properties "Link to this heading")

Normalization of upper or mixed-case property names to lowercase in [`Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
 and [`Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update")
 is deprecated. In the future, property names will be passed as is, allowing one to pass names such as _patchA_ or _UVC_.

### `ContourSet.ax`, `Quiver.ax`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#contourset-ax-quiver-ax "Link to this heading")

These attributes are deprecated in favor of `ContourSet.axes` and `Quiver.axes`, for consistency with other artists.

### `Locator.refresh()` and associated methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#locator-refresh-and-associated-methods "Link to this heading")

`Locator.refresh()` is deprecated. This method was called at certain places to let locators update their internal state, typically based on the axis limits. Locators should now always consult the axis limits when called, if needed.

The associated helper methods `NavigationToolbar2.draw()` and `ToolViewsPositions.refresh_locators()` are deprecated, and should be replaced by calls to `draw_idle()` on the corresponding canvas.

### [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 checkers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#scalarmappable-checkers "Link to this heading")

The `add_checker` and `check_update` methods and `update_dict` attribute of [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 are deprecated.

### [`pyplot.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 and `ColorbarBase` parameters will become keyword-only[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#pyplot-tight-layout-and-colorbarbase-parameters-will-become-keyword-only "Link to this heading")

All parameters of [`pyplot.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 and all parameters of `ColorbarBase` except for the first (_ax_) will become keyword-only, consistently with [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
 and `Colorbar`, respectively.

### [`Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 radius and startangle[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axes-pie-radius-and-startangle "Link to this heading")

Passing `None` as either the `radius` or `startangle` of an [`Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 is deprecated; use the explicit defaults of 1 and 0, respectively, instead.

### `AxisArtist.dpi_transform`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axisartist-dpi-transform "Link to this heading")

... is deprecated. Scale `Figure.dpi_scale_trans` by 1/72 to achieve the same effect.

### `offset_position` property of [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#offset-position-property-of-collection "Link to this heading")

The `offset_position` property of [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 is deprecated. In the future, [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
s will always behave as if `offset_position` is set to "screen" (the default).

Support for passing `offset_position="data"` to the `draw_path_collection` of all renderer classes is deprecated.

[`transforms.AffineDeltaTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.AffineDeltaTransform "matplotlib.transforms.AffineDeltaTransform")
 can be used as a replacement. This API is experimental and may change in the future.

### `testing.compare.make_external_conversion_command`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#testing-compare-make-external-conversion-command "Link to this heading")

... is deprecated.

### `epoch2num` and `num2epoch` are deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#epoch2num-and-num2epoch-are-deprecated "Link to this heading")

These are unused and can be easily reproduced by other date tools. [`get_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
 will return Matplotlib's epoch.

### `axes_grid1.CbarAxes` attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#axes-grid1-cbaraxes-attributes "Link to this heading")

The `cbid` and `locator` attribute are deprecated. Use `mappable.colorbar_cid` and `colorbar.locator`, as for standard colorbars.

### `qt_compat.is_pyqt5`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#qt-compat-is-pyqt5 "Link to this heading")

This function is deprecated in prevision of the future release of PyQt6. The Qt version can be checked using `QtCore.qVersion()`.

### Reordering of parameters by [`Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#reordering-of-parameters-by-artist-set "Link to this heading")

In a future version, `Artist.set` will apply artist properties in the order in which they are given. This only affects the interaction between the _color_, _edgecolor_, _facecolor_, and, for [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
s, _alpha_ properties: the _color_ property now needs to be passed first in order not to override the other properties. This is consistent with e.g. [`Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update")
, which did not reorder the properties passed to it.

### Passing multiple keys as a single comma-separated string or multiple arguments to [`ToolManager.update_keymap`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.update_keymap "matplotlib.backend_managers.ToolManager.update_keymap")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#passing-multiple-keys-as-a-single-comma-separated-string-or-multiple-arguments-to-toolmanager-update-keymap "Link to this heading")

This is deprecated; pass keys as a list of strings instead.

### Statusbar classes and attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#statusbar-classes-and-attributes "Link to this heading")

The `statusbar` attribute of [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")
, `StatusbarBase` and all its subclasses, and `StatusBarWx`, are deprecated, as messages are now displayed in the toolbar instead.

### `ismath` parameter of `draw_tex`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#ismath-parameter-of-draw-tex "Link to this heading")

The `ismath` parameter of the `draw_tex` method of all renderer classes is deprecated (as a call to `draw_tex` -- not to be confused with `draw_text`! -- means that the entire string should be passed to the `usetex` machinery anyways). Likewise, the text machinery will no longer pass the `ismath` parameter when calling `draw_tex` (this should only matter for backend implementers).

Passing `ismath="TeX!"` to [`RendererAgg.get_text_width_height_descent`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.get_text_width_height_descent "matplotlib.backends.backend_agg.RendererAgg.get_text_width_height_descent")
 is deprecated. Pass `ismath="TeX"` instead, consistently with other low-level APIs which support the values True, False, and "TeX" for `ismath`.

### `matplotlib.ttconv`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#matplotlib-ttconv "Link to this heading")

This module is deprecated.

### Stricter PDF metadata keys in PGF[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#stricter-pdf-metadata-keys-in-pgf "Link to this heading")

Saving metadata in PDF with the PGF backend currently normalizes all keys to lowercase, unlike the PDF backend, which only accepts the canonical case. This is deprecated; in a future version, only the canonically cased keys listed in the PDF specification (and the [`PdfPages`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages "matplotlib.backends.backend_pgf.PdfPages")
 documentation) will be accepted.

### Qt modifier keys[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#qt-modifier-keys "Link to this heading")

The `MODIFIER_KEYS`, `SUPER`, `ALT`, `CTRL`, and `SHIFT` global variables of the `matplotlib.backends.backend_qt4agg`, `matplotlib.backends.backend_qt4cairo`, [`matplotlib.backends.backend_qt5agg`](https://matplotlib.org/stable/api/backend_qt_api.html#module-matplotlib.backends.backend_qt5agg "matplotlib.backends.backend_qt5agg")
 and [`matplotlib.backends.backend_qt5cairo`](https://matplotlib.org/stable/api/backend_qt_api.html#module-matplotlib.backends.backend_qt5cairo "matplotlib.backends.backend_qt5cairo")
 modules are deprecated.

### `TexManager`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#texmanager "Link to this heading")

The `TexManager.serif`, `TexManager.sans_serif`, `TexManager.cursive` and `TexManager.monospace` attributes are deprecated.

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#id3)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following deprecated APIs have been removed:

### Modules[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#modules "Link to this heading")

*   `backends.qt_editor.formlayout` (use the formlayout module available on PyPI instead).
    

### Classes, methods and attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#classes-methods-and-attributes "Link to this heading")

*   `artist.Artist.aname` property (no replacement)
    
*   `axis.Axis.iter_ticks` (no replacement)
    
*   Support for custom backends that do not provide a `backend_bases.GraphicsContextBase.set_hatch_color` method
    
*   `backend_bases.RendererBase.strip_math()` (use `cbook.strip_math()` instead)
    
*   `backend_wx.debug_on_error()` (no replacement)
    
*   `backend_wx.raise_msg_to_str()` (no replacement)
    
*   `backend_wx.fake_stderr` (no replacement)
    
*   `backend_wx.MenuButtonWx` (no replacement)
    
*   `backend_wx.PrintoutWx` (no replacement)
    
*   `_backend_tk.NavigationToolbar2Tk.set_active()` (no replacement)
    
*   `backend_ps.PsBackendHelper.gs_exe` property (no replacement)
    
*   `backend_ps.PsBackendHelper.gs_version` property (no replacement)
    
*   `backend_ps.PsBackendHelper.supports_ps2write` property (no replacement)
    
*   `backend_ps.RendererPS.afmfontd` property (no replacement)
    
*   `backend_ps.GraphicsContextPS.shouldstroke` property (no replacement)
    
*   `backend_gtk3.FileChooserDialog` (no replacement)
    
*   `backend_gtk3.SaveFigureGTK3.get_filechooser()` (no replacement)
    
*   `backend_gtk3.NavigationToolbar2GTK3.get_filechooser()` (no replacement)
    
*   `backend_gtk3cairo.FigureManagerGTK3Cairo` (use `backend_gtk3.FigureManagerGTK3` instead)
    
*   `backend_pdf.RendererPdf.afm_font_cache` property (no replacement)
    
*   `backend_pgf.LatexManagerFactory` (no replacement)
    
*   `backend_qt5.NavigationToolbar2QT.buttons` property (no replacement)
    
*   `backend_qt5.NavigationToolbar2QT.adj_window` property (no replacement)
    
*   `bezier.find_r_to_boundary_of_closedpath()` (no replacement)
    
*   `cbook.dedent()` (use [`inspect.cleandoc`](https://docs.python.org/3/library/inspect.html#inspect.cleandoc "(in Python v3.14)")
     instead)
    
*   `cbook.get_label()` (no replacement)
    
*   `cbook.is_hashable()` (use `isinstance(..., collections.abc.Hashable)` instead)
    
*   `cbook.iterable()` (use `numpy.iterable()` instead)
    
*   `cbook.safezip()` (no replacement)
    
*   `colorbar.ColorbarBase.get_cmap` (use `ScalarMappable.get_cmap` instead)
    
*   `colorbar.ColorbarBase.set_cmap` (use `ScalarMappable.set_cmap` instead)
    
*   `colorbar.ColorbarBase.get_clim` (use `ScalarMappable.get_clim` instead)
    
*   `colorbar.ColorbarBase.set_clim` (use `ScalarMappable.set_clim` instead)
    
*   `colorbar.ColorbarBase.set_norm` (use `ScalarMappable.set_norm` instead)
    
*   `dates.seconds()` (no replacement)
    
*   `dates.minutes()` (no replacement)
    
*   `dates.hours()` (no replacement)
    
*   `dates.weeks()` (no replacement)
    
*   `dates.strpdate2num` and `dates.bytespdate2num` (use [`time.strptime`](https://docs.python.org/3/library/time.html#time.strptime "(in Python v3.14)")
     or [`dateutil.parser.parse`](https://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.parse "(in dateutil v3.9.0)")
     or [`dates.datestr2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.datestr2num "matplotlib.dates.datestr2num")
     instead)
    
*   `docstring.Appender` (no replacement)
    
*   `docstring.dedent()` (use [`inspect.getdoc`](https://docs.python.org/3/library/inspect.html#inspect.getdoc "(in Python v3.14)")
     instead)
    
*   `docstring.copy_dedent()` (use `docstring.copy()` and [`inspect.getdoc`](https://docs.python.org/3/library/inspect.html#inspect.getdoc "(in Python v3.14)")
     instead)
    
*   `font_manager.OSXInstalledFonts()` (no replacement)
    
*   `image.BboxImage.interp_at_native` property (no replacement)
    
*   `lines.Line2D.verticalOffset` property (no replacement)
    
*   `matplotlib.checkdep_dvipng` (no replacement)
    
*   `matplotlib.checkdep_ghostscript` (no replacement)
    
*   `matplotlib.checkdep_pdftops` (no replacement)
    
*   `matplotlib.checkdep_inkscape` (no replacement)
    
*   `matplotlib.get_py2exe_datafiles` (no replacement)
    
*   `matplotlib.tk_window_focus` (use `rcParams['tk.window_focus']` instead)
    
*   `mlab.demean()` (use `mlab.detrend_mean()` instead)
    
*   `path.get_paths_extents()` (use `path.get_path_collection_extents()` instead)
    
*   `path.Path.has_nonfinite()` (use `not np.isfinite(self.vertices).all()` instead)
    
*   `projections.process_projection_requirements()` (no replacement)
    
*   `pyplot.plotfile()` (Instead, load the data using [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "(in pandas v3.0.5)")
     or [`numpy.loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "(in NumPy v2.5)")
     or similar and use regular pyplot functions to plot the loaded data.)
    
*   `quiver.Quiver.color()` (use `Quiver.get_facecolor()` instead)
    
*   `quiver.Quiver.keyvec` property (no replacement)
    
*   `quiver.Quiver.keytext` property (no replacement)
    
*   `rcsetup.validate_qt4()` (no replacement)
    
*   `rcsetup.validate_qt5()` (no replacement)
    
*   `rcsetup.validate_verbose()` (no replacement)
    
*   `rcsetup.ValidateInterval` (no replacement)
    
*   `scale.LogTransformBase` (use `scale.LogTransform` instead)
    
*   `scale.InvertedLogTransformBase` (use `scale.InvertedLogTransform` instead)
    
*   `scale.Log10Transform` (use `scale.LogTransform` instead)
    
*   `scale.InvertedLog10Transform` (use `scale.InvertedLogTransform` instead)
    
*   `scale.Log2Transform` (use `scale.LogTransform` instead)
    
*   `scale.InvertedLog2Transform` (use `scale.InvertedLogTransform` instead)
    
*   `scale.NaturalLogTransform` (use `scale.LogTransform` instead)
    
*   `scale.InvertedNaturalLogTransform` (use `scale.InvertedLogTransform` instead)
    
*   `scale.get_scale_docs()` (no replacement)
    
*   `sphinxext.plot_directive.plot_directive()` (use the class `PlotDirective` instead)
    
*   `sphinxext.mathmpl.math_directive()` (use the class `MathDirective` instead)
    
*   `spines.Spine.is_frame_like()` (no replacement)
    
*   `testing.decorators.switch_backend()` (use `@pytest.mark.backend` decorator instead)
    
*   `text.Text.is_math_text()` (use `cbook.is_math_text()` instead)
    
*   `text.TextWithDash()` (use `text.Annotation` instead)
    
*   `textpath.TextPath.is_math_text()` (use `cbook.is_math_text()` instead)
    
*   `textpath.TextPath.text_get_vertices_codes()` (use `textpath.text_to_path.get_text_path()` instead)
    
*   `textpath.TextToPath.glyph_to_path()` (use `font.get_path()` and manual translation of the vertices instead)
    
*   `ticker.OldScalarFormatter.pprint_val()` (no replacement)
    
*   `ticker.ScalarFormatter.pprint_val()` (no replacement)
    
*   `ticker.LogFormatter.pprint_val()` (no replacement)
    
*   `ticker.decade_down()` (no replacement)
    
*   `ticker.decade_up()` (no replacement)
    
*   `Tick` properties `gridOn`, `tick1On`, `tick2On`, `label1On`, `label2On` (use `set_visible()` / `get_visible()` on `Tick.gridline`, `Tick.tick1line`, `Tick.tick2line`, `Tick.label1`, `Tick.label2` instead)
    
*   `widgets.SpanSelector.buttonDown` property (no replacement)
    
*   `mplot3d.proj3d.line2d()` (no replacement)
    
*   `mplot3d.proj3d.line2d_dist()` (no replacement)
    
*   `mplot3d.proj3d.line2d_seg_dist()` (no replacement)
    
*   `mplot3d.proj3d.mod()` (use [`numpy.linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "(in NumPy v2.5)")
     instead)
    
*   `mplot3d.proj3d.proj_transform_vec()` (no replacement)
    
*   `mplot3d.proj3d.proj_transform_vec_clip()` (no replacement)
    
*   `mplot3d.proj3d.vec_pad_ones()` (no replacement)
    
*   `mplot3d.proj3d.proj_trans_clip_points()` (no replacement)
    
*   `mplot3d.art3d.norm_angle()` (no replacement)
    
*   `mplot3d.art3d.norm_text_angle()` (no replacement)
    
*   `mplot3d.art3d.path_to_3d_segment()` (no replacement)
    
*   `mplot3d.art3d.paths_to_3d_segments()` (no replacement)
    
*   `mplot3d.art3d.path_to_3d_segment_with_codes()` (no replacement)
    
*   `mplot3d.art3d.paths_to_3d_segments_with_codes()` (no replacement)
    
*   `mplot3d.art3d.get_patch_verts()` (no replacement)
    
*   `mplot3d.art3d.get_colors()` (no replacement)
    
*   `mplot3d.art3d.zalpha()` (no replacement)
    
*   `mplot3d.axis3d.get_flip_min_max()` (no replacement)
    
*   `mplot3d.axis3d.Axis.get_tick_positions()` (no replacement)
    
*   `axisartist.axis_artist.UnimplementedException` (no replacement)
    
*   `axisartist.axislines.SimpleChainedObjects` (use `axis_grid1.mpl_axes.SimpleChainedObjects` instead)
    
*   `axisartist.axislines.Axes.AxisDict` (use `axis_grid1.mpl_axes.Axes.AxisDict` instead)
    

### Arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#arguments "Link to this heading")

*   `Axes.text()` / `pyplot.text()` do not support the parameter `withdash` anymore. Use `Axes.annotate()` and `pyplot.annotate()` instead.
    
*   The first parameter of [`matplotlib.use`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
     has been renamed from `arg` to `backend` (only relevant if you pass by keyword).
    
*   The parameter `warn` of [`matplotlib.use`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
     has been removed. A failure to switch the backend will now always raise an `ImportError` if `force` is set; catch that error if necessary.
    
*   All parameters of [`matplotlib.use`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
     except the first one are now keyword-only.
    
*   The unused parameters `shape` and `imlim` of [`imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     are now removed. All parameters beyond `extent` are now keyword-only.
    
*   The unused parameter `interp_at_native` of [`BboxImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
     has been removed.
    
*   The parameter `usetex` of [`TextToPath.get_text_path`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath.get_text_path "matplotlib.text.TextToPath.get_text_path")
     has been removed. Use `ismath='TeX'` instead.
    
*   The parameter `block` of `show()` is now keyword-only, and arbitrary arguments or keyword arguments are no longer accepted.
    
*   The parameter `frameon` of [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
     has been removed. Use `facecolor="none"` to get a transparent background.
    
*   Passing a `wx.EvtHandler` as the first argument to `backend_wx.TimerWx` is not supported anymore; the signature of `TimerWx` is now consistent with [`TimerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase "matplotlib.backend_bases.TimerBase")
    .
    
*   The `manage_xticks` parameter of [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
     and [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
     has been renamed to `manage_ticks`.
    
*   The `normed` parameter of [`hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")
     has been renamed to `density`.
    
*   The `s` parameter of [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
     has been renamed to `text`.
    
*   For all functions in [`bezier`](https://matplotlib.org/stable/api/bezier_api.html#module-matplotlib.bezier "matplotlib.bezier")
     that supported a `tolerance` parameter, this parameter has been renamed to `tolerance`.
    
*   `axis("normal")` is not supported anymore. Use the equivalent `axis("auto")` instead.
    
*   `axis()` does not accept arbitrary keyword arguments anymore.
    
*   `Axis.set_ticklabels()` does not accept arbitrary positional arguments other than `ticklabels`.
    
*   `mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_zsort` does not accept the value `True` anymore. Pass the equivalent value 'average' instead.
    
*   [`AnchoredText`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")
     no longer accepts `horizontalalignment` or `verticalalignment` keyword arguments.
    
*   [`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
     no longer accepts the `arrow_transmuter` and `connector` keyword arguments, which did nothing since 3.0.
    
*   [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
     no longer accepts the `arrow_transmuter` and `connector` keyword arguments, which did nothing since 3.0.
    
*   [`TextPath`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath "matplotlib.text.TextPath")
     no longer accepts arbitrary positional or keyword arguments.
    
*   [`MaxNLocator.set_params()`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator.set_params "matplotlib.ticker.MaxNLocator.set_params")
     no longer accepts arbitrary keyword arguments.
    
*   [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     no longer accepts and squeezes non-1D inputs; pass 1D input to the `x` argument.
    
*   Passing (n, 1)-shaped error arrays to [`Axes.errorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
     is no longer supported; pass a 1D array instead.
    

### rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#rcparams "Link to this heading")

*   The `text.latex.unicode` rcParam has been removed, with no replacement. Matplotlib now always supports unicode in usetex.
    
*   The `savefig.frameon` rcParam has been removed. Set `[rcParams["savefig.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.facecolor#rcparam-savefig-facecolor) ` (default: `'auto'`) to "none" to get a transparent background.
    
*   The `pgf.debug`, `verbose.fileo` and `verbose.verbose.level` rcParams, which had no effect, have been removed.
    
*   Support for setting `[rcParams["mathtext.default"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.default#rcparam-mathtext-default) ` (default: `'normal'`) to "circled" has been removed.
    

### Environment variables[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#environment-variables "Link to this heading")

*   `MATPLOTLIBDATA` (no replacement).
    

### mathtext[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#mathtext "Link to this heading")

*   The `\stackrel` command (which behaved differently from its LaTeX version) has been removed. Use `\genfrac` instead.
    
*   The `\mathcircled` command has been removed. Directly use Unicode characters, such as `'\N{CIRCLED LATIN CAPITAL LETTER A}'`, instead.
    

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#id4)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#development-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Matplotlib now requires numpy>=1.15[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#matplotlib-now-requires-numpy-1-15 "Link to this heading")

### Matplotlib now uses Pillow to save and read pngs[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.0.html#matplotlib-now-uses-pillow-to-save-and-read-pngs "Link to this heading")

The builtin png encoder and decoder has been removed, and Pillow is now a dependency. Note that when reading 16-bit RGB(A) images, Pillow truncates them to 8-bit precision, whereas the old builtin decoder kept the full precision.

The deprecated wx backend (not wxagg!) now always uses wx's builtin jpeg and tiff support rather than relying on Pillow for writing these formats; this behavior is consistent with wx's png output.

On this page
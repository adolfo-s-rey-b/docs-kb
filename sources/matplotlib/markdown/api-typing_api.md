[Skip to main content](https://matplotlib.org/stable/api/typing_api.html#main-content)

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
    

`matplotlib.typing`[#](https://matplotlib.org/stable/api/typing_api.html#module-matplotlib.typing "Link to this heading")

==========================================================================================================================

Typing support for Matplotlib

This module contains Type aliases which are useful for Matplotlib and potentially downstream libraries.

Warning

**Provisional status of typing**

The `typing` module and type stub files are considered provisional and may change at any time without a deprecation period.

Color[#](https://matplotlib.org/stable/api/typing_api.html#color "Link to this heading")

-----------------------------------------------------------------------------------------

matplotlib.typing.ColorType \= tuple\[float, float, float\] | str | tuple\[float, float, float, float\] | tuple\[tuple\[float, float, float\] | str, float\] | tuple\[tuple\[float, float, float, float\], float\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.ColorType "Link to this definition")

Any color specification accepted by Matplotlib. See [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
.

matplotlib.typing.RGBColorType \= tuple\[float, float, float\] | str[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RGBColorType "Link to this definition")

Any RGB color specification accepted by Matplotlib.

matplotlib.typing.RGBAColorType \= str | tuple\[float, float, float, float\] | tuple\[tuple\[float, float, float\] | str, float\] | tuple\[tuple\[float, float, float, float\], float\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RGBAColorType "Link to this definition")

Any RGBA color specification accepted by Matplotlib.

matplotlib.typing.ColourType \= tuple\[float, float, float\] | str | tuple\[float, float, float, float\] | tuple\[tuple\[float, float, float\] | str, float\] | tuple\[tuple\[float, float, float, float\], float\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.ColourType "Link to this definition")

Alias of [`ColorType`](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.ColorType "matplotlib.typing.ColorType")
.

matplotlib.typing.RGBColourType \= tuple\[float, float, float\] | str[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RGBColourType "Link to this definition")

Alias of [`RGBColorType`](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RGBColorType "matplotlib.typing.RGBColorType")
.

matplotlib.typing.RGBAColourType \= str | tuple\[float, float, float, float\] | tuple\[tuple\[float, float, float\] | str, float\] | tuple\[tuple\[float, float, float, float\], float\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RGBAColourType "Link to this definition")

Alias of [`RGBAColorType`](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RGBAColorType "matplotlib.typing.RGBAColorType")
.

Artist styles[#](https://matplotlib.org/stable/api/typing_api.html#artist-styles "Link to this heading")

---------------------------------------------------------------------------------------------------------

matplotlib.typing.LineStyleType \= typing.Literal\['-', 'solid', '--', 'dashed', '-.', 'dashdot', ':', 'dotted', '', 'none', ' ', 'None'\] | tuple\[float, collections.abc.Sequence\[float\]\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.LineStyleType "Link to this definition")

Any line style specification accepted by Matplotlib. See [Linestyles](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)
.

matplotlib.typing.DrawStyleType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.DrawStyleType "Link to this definition")

See [Step Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/step_demo.html)
.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'\]

matplotlib.typing.MarkEveryType \= None | int | tuple\[int, int\] | slice | list\[int\] | float | tuple\[float, float\] | list\[bool\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.MarkEveryType "Link to this definition")

See [Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)
.

matplotlib.typing.MarkerType \= matplotlib.path.Path | matplotlib.markers.MarkerStyle | str | typing.Literal\['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '\*', 'h', 'H', '+', 'x', 'X', 'D', 'd', '|', '\_', 'none', ' ', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\] | list\[tuple\[int, int\]\] | tuple\[int, typing.Literal\[0, 1, 2\], int\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.MarkerType "Link to this definition")

Marker specification. See [Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)
.

matplotlib.typing.FillStyleType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.FillStyleType "Link to this definition")

Marker fill styles. See [Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)
.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['full', 'left', 'right', 'bottom', 'top', 'none'\]

matplotlib.typing.CapStyleType \= matplotlib.\_enums.CapStyle | typing.Literal\['butt', 'projecting', 'round'\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.CapStyleType "Link to this definition")

Line cap styles. See [CapStyle](https://matplotlib.org/stable/gallery/lines_bars_and_markers/capstyle.html)
.

matplotlib.typing.JoinStyleType \= matplotlib.\_enums.JoinStyle | typing.Literal\['miter', 'round', 'bevel'\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.JoinStyleType "Link to this definition")

Line join styles. See [JoinStyle](https://matplotlib.org/stable/gallery/lines_bars_and_markers/joinstyle.html)
.

Events[#](https://matplotlib.org/stable/api/typing_api.html#events "Link to this heading")

-------------------------------------------------------------------------------------------

matplotlib.typing.MouseEventType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.MouseEventType "Link to this definition")

Literal type for valid [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
 names.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['button\_press\_event', 'button\_release\_event', 'motion\_notify\_event', 'scroll\_event', 'figure\_enter\_event', 'figure\_leave\_event', 'axes\_enter\_event', 'axes\_leave\_event'\]

matplotlib.typing.KeyEventType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.KeyEventType "Link to this definition")

Literal type for valid [`KeyEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "matplotlib.backend_bases.KeyEvent")
 names.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['key\_press\_event', 'key\_release\_event'\]

matplotlib.typing.DrawEventType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.DrawEventType "Link to this definition")

Literal type for valid [`DrawEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.DrawEvent "matplotlib.backend_bases.DrawEvent")
 names.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['draw\_event'\]

matplotlib.typing.PickEventType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.PickEventType "Link to this definition")

Literal type for valid [`PickEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.PickEvent "matplotlib.backend_bases.PickEvent")
 names.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['pick\_event'\]

matplotlib.typing.ResizeEventType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.ResizeEventType "Link to this definition")

Literal type for valid [`ResizeEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ResizeEvent "matplotlib.backend_bases.ResizeEvent")
 names.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['resize\_event'\]

matplotlib.typing.CloseEventType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.CloseEventType "Link to this definition")

Literal type for valid [`CloseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.CloseEvent "matplotlib.backend_bases.CloseEvent")
 names.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['close\_event'\]

matplotlib.typing.EventType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.EventType "Link to this definition")

Literal type for all valid events.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['button\_press\_event', 'button\_release\_event', 'motion\_notify\_event', 'scroll\_event', 'figure\_enter\_event', 'figure\_leave\_event', 'axes\_enter\_event', 'axes\_leave\_event', 'key\_press\_event', 'key\_release\_event', 'draw\_event', 'pick\_event', 'resize\_event', 'close\_event'\]

rcParams and stylesheets[#](https://matplotlib.org/stable/api/typing_api.html#rcparams-and-stylesheets "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

matplotlib.typing.RcKeyType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RcKeyType "Link to this definition")

Valid specifiers for keys in [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 and [`matplotlib.rc_context`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['agg.path.chunksize', 'animation.bitrate', 'animation.codec', 'animation.convert\_args', 'animation.convert\_path', 'animation.embed\_limit', 'animation.ffmpeg\_args', 'animation.ffmpeg\_path', 'animation.frame\_format', 'animation.html', 'animation.writer', 'axes.autolimit\_mode', 'axes.axisbelow', 'axes.edgecolor', 'axes.facecolor', 'axes.formatter.limits', 'axes.formatter.min\_exponent', 'axes.formatter.offset\_threshold', 'axes.formatter.use\_locale', 'axes.formatter.use\_mathtext', 'axes.formatter.useoffset', 'axes.grid', 'axes.grid.axis', 'axes.grid.which', 'axes.labelcolor', 'axes.labelpad', 'axes.labelsize', 'axes.labelweight', 'axes.linewidth', 'axes.prop\_cycle', 'axes.spines.bottom', 'axes.spines.left', 'axes.spines.right', 'axes.spines.top', 'axes.titlecolor', 'axes.titlelocation', 'axes.titlepad', 'axes.titlesize', 'axes.titleweight', 'axes.titley', 'axes.unicode\_minus', 'axes.xmargin', 'axes.ymargin', 'axes.zmargin', 'axes3d.automargin', 'axes3d.depthshade', 'axes3d.depthshade\_minalpha', 'axes3d.grid', 'axes3d.mouserotationstyle', 'axes3d.trackballborder', 'axes3d.snap\_rotation', 'axes3d.trackballsize', 'axes3d.xaxis.panecolor', 'axes3d.yaxis.panecolor', 'axes3d.zaxis.panecolor', 'backend', 'backend\_fallback', 'boxplot.bootstrap', 'boxplot.boxprops.color', 'boxplot.boxprops.linestyle', 'boxplot.boxprops.linewidth', 'boxplot.capprops.color', 'boxplot.capprops.linestyle', 'boxplot.capprops.linewidth', 'boxplot.flierprops.color', 'boxplot.flierprops.linestyle', 'boxplot.flierprops.linewidth', 'boxplot.flierprops.marker', 'boxplot.flierprops.markeredgecolor', 'boxplot.flierprops.markeredgewidth', 'boxplot.flierprops.markerfacecolor', 'boxplot.flierprops.markersize', 'boxplot.meanline', 'boxplot.meanprops.color', 'boxplot.meanprops.linestyle', 'boxplot.meanprops.linewidth', 'boxplot.meanprops.marker', 'boxplot.meanprops.markeredgecolor', 'boxplot.meanprops.markerfacecolor', 'boxplot.meanprops.markersize', 'boxplot.medianprops.color', 'boxplot.medianprops.linestyle', 'boxplot.medianprops.linewidth', 'boxplot.notch', 'boxplot.patchartist', 'boxplot.showbox', 'boxplot.showcaps', 'boxplot.showfliers', 'boxplot.showmeans', 'boxplot.vertical', 'boxplot.whiskerprops.color', 'boxplot.whiskerprops.linestyle', 'boxplot.whiskerprops.linewidth', 'boxplot.whiskers', 'contour.algorithm', 'contour.corner\_mask', 'contour.linewidth', 'contour.negative\_linestyle', 'date.autoformatter.day', 'date.autoformatter.hour', 'date.autoformatter.microsecond', 'date.autoformatter.minute', 'date.autoformatter.month', 'date.autoformatter.second', 'date.autoformatter.year', 'date.converter', 'date.epoch', 'date.interval\_multiples', 'docstring.hardcopy', 'errorbar.capsize', 'errorbar.capthick', 'errorbar.elinewidth', 'figure.autolayout', 'figure.constrained\_layout.h\_pad', 'figure.constrained\_layout.hspace', 'figure.constrained\_layout.use', 'figure.constrained\_layout.w\_pad', 'figure.constrained\_layout.wspace', 'figure.dpi', 'figure.edgecolor', 'figure.facecolor', 'figure.figsize', 'figure.frameon', 'figure.hooks', 'figure.labelsize', 'figure.labelweight', 'figure.max\_open\_warning', 'figure.raise\_window', 'figure.subplot.bottom', 'figure.subplot.hspace', 'figure.subplot.left', 'figure.subplot.right', 'figure.subplot.top', 'figure.subplot.wspace', 'figure.titlesize', 'figure.titleweight', 'font.cursive', 'font.enable\_last\_resort', 'font.family', 'font.fantasy', 'font.monospace', 'font.sans-serif', 'font.serif', 'font.size', 'font.stretch', 'font.style', 'font.variant', 'font.weight', 'grid.alpha', 'grid.color', 'grid.linestyle', 'grid.linewidth', 'grid.major.alpha', 'grid.major.color', 'grid.major.linestyle', 'grid.major.linewidth', 'grid.minor.alpha', 'grid.minor.color', 'grid.minor.linestyle', 'grid.minor.linewidth', 'hatch.color', 'hatch.linewidth', 'hist.bins', 'image.aspect', 'image.cmap', 'image.composite\_image', 'image.interpolation', 'image.interpolation\_stage', 'image.lut', 'image.origin', 'image.resample', 'interactive', 'keymap.back', 'keymap.copy', 'keymap.forward', 'keymap.fullscreen', 'keymap.grid', 'keymap.grid\_minor', 'keymap.help', 'keymap.home', 'keymap.pan', 'keymap.quit', 'keymap.quit\_all', 'keymap.save', 'keymap.xscale', 'keymap.yscale', 'keymap.zoom', 'legend.borderaxespad', 'legend.borderpad', 'legend.columnspacing', 'legend.edgecolor', 'legend.facecolor', 'legend.fancybox', 'legend.fontsize', 'legend.framealpha', 'legend.frameon', 'legend.handleheight', 'legend.handlelength', 'legend.handletextpad', 'legend.labelcolor', 'legend.labelspacing', 'legend.linewidth', 'legend.loc', 'legend.markerscale', 'legend.numpoints', 'legend.scatterpoints', 'legend.shadow', 'legend.title\_fontsize', 'lines.antialiased', 'lines.color', 'lines.dash\_capstyle', 'lines.dash\_joinstyle', 'lines.dashdot\_pattern', 'lines.dashed\_pattern', 'lines.dotted\_pattern', 'lines.linestyle', 'lines.linewidth', 'lines.marker', 'lines.markeredgecolor', 'lines.markeredgewidth', 'lines.markerfacecolor', 'lines.markersize', 'lines.scale\_dashes', 'lines.solid\_capstyle', 'lines.solid\_joinstyle', 'macosx.window\_mode', 'markers.fillstyle', 'mathtext.bf', 'mathtext.bfit', 'mathtext.cal', 'mathtext.default', 'mathtext.fallback', 'mathtext.fontset', 'mathtext.it', 'mathtext.rm', 'mathtext.sf', 'mathtext.tt', 'patch.antialiased', 'patch.edgecolor', 'patch.facecolor', 'patch.force\_edgecolor', 'patch.linewidth', 'path.effects', 'path.simplify', 'path.simplify\_threshold', 'path.sketch', 'path.snap', 'pcolor.shading', 'pcolormesh.snap', 'pdf.compression', 'pdf.fonttype', 'pdf.inheritcolor', 'pdf.use14corefonts', 'pgf.preamble', 'pgf.rcfonts', 'pgf.texsystem', 'polaraxes.grid', 'ps.distiller.res', 'ps.fonttype', 'ps.papersize', 'ps.useafm', 'ps.usedistiller', 'savefig.bbox', 'savefig.directory', 'savefig.dpi', 'savefig.edgecolor', 'savefig.facecolor', 'savefig.format', 'savefig.orientation', 'savefig.pad\_inches', 'savefig.transparent', 'scatter.edgecolors', 'scatter.marker', 'svg.fonttype', 'svg.hashsalt', 'svg.id', 'svg.image\_inline', 'text.antialiased', 'text.color', 'text.hinting', 'text.hinting\_factor', 'text.kerning\_factor', 'text.language', 'text.latex.engine', 'text.latex.preamble', 'text.parse\_math', 'text.usetex', 'timezone', 'tk.window\_focus', 'toolbar', 'webagg.address', 'webagg.open\_in\_browser', 'webagg.port', 'webagg.port\_retries', 'xaxis.labellocation', 'xtick.alignment', 'xtick.bottom', 'xtick.color', 'xtick.direction', 'xtick.labelbottom', 'xtick.labelcolor', 'xtick.labelsize', 'xtick.labeltop', 'xtick.major.bottom', 'xtick.major.pad', 'xtick.major.size', 'xtick.major.top', 'xtick.major.width', 'xtick.minor.bottom', 'xtick.minor.ndivs', 'xtick.minor.pad', 'xtick.minor.size', 'xtick.minor.top', 'xtick.minor.visible', 'xtick.minor.width', 'xtick.top', 'yaxis.labellocation', 'ytick.alignment', 'ytick.color', 'ytick.direction', 'ytick.labelcolor', 'ytick.labelleft', 'ytick.labelright', 'ytick.labelsize', 'ytick.left', 'ytick.major.left', 'ytick.major.pad', 'ytick.major.right', 'ytick.major.size', 'ytick.major.width', 'ytick.minor.left', 'ytick.minor.ndivs', 'ytick.minor.pad', 'ytick.minor.right', 'ytick.minor.size', 'ytick.minor.visible', 'ytick.minor.width', 'ytick.right'\]

matplotlib.typing.RcGroupKeyType[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RcGroupKeyType "Link to this definition")

Literal type for valid groups accepted by [`matplotlib.rc`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc "matplotlib.rc")
.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['agg', 'agg.path', 'animation', 'axes', 'axes.formatter', 'axes.grid', 'axes.spines', 'axes3d', 'axes3d.xaxis', 'axes3d.yaxis', 'axes3d.zaxis', 'boxplot', 'boxplot.boxprops', 'boxplot.capprops', 'boxplot.flierprops', 'boxplot.meanprops', 'boxplot.medianprops', 'boxplot.whiskerprops', 'contour', 'date', 'date.autoformatter', 'docstring', 'errorbar', 'figure', 'figure.constrained\_layout', 'figure.subplot', 'font', 'grid', 'grid.major', 'grid.minor', 'hatch', 'hist', 'image', 'keymap', 'legend', 'lines', 'macosx', 'markers', 'mathtext', 'patch', 'path', 'pcolor', 'pcolormesh', 'pdf', 'pgf', 'polaraxes', 'ps', 'ps.distiller', 'savefig', 'scatter', 'svg', 'text', 'text.latex', 'tk', 'webagg', 'xaxis', 'xtick', 'xtick.major', 'xtick.minor', 'yaxis', 'ytick', 'ytick.major', 'ytick.minor'\]

matplotlib.typing.RcStyleType \= str | dict\[str, typing.Any\] | pathlib.Path | collections.abc.Sequence\[str | pathlib.Path | dict\[str, typing.Any\]\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.RcStyleType "Link to this definition")

Valid specifiers for styles as used in [`matplotlib.style.use`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use "matplotlib.style.use")
 and [`matplotlib.style.context`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.context "matplotlib.style.context")
.

Other types[#](https://matplotlib.org/stable/api/typing_api.html#other-types "Link to this heading")

-----------------------------------------------------------------------------------------------------

matplotlib.typing.CoordsType \= str | matplotlib.artist.Artist | matplotlib.transforms.Transform | collections.abc.Callable\[\[matplotlib.backend\_bases.RendererBase\], matplotlib.transforms.Bbox | matplotlib.transforms.Transform\] | tuple\[str | matplotlib.artist.Artist | matplotlib.transforms.Transform | collections.abc.Callable\[\[matplotlib.backend\_bases.RendererBase\], matplotlib.transforms.Bbox | matplotlib.transforms.Transform\], str | matplotlib.artist.Artist | matplotlib.transforms.Transform | collections.abc.Callable\[\[matplotlib.backend\_bases.RendererBase\], matplotlib.transforms.Bbox | matplotlib.transforms.Transform\]\][#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.CoordsType "Link to this definition")

Annotation coordinate systems. See [Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)
.

matplotlib.typing.DataParamType \= collections.abc.Mapping\[str, typing.Any\] | None[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.DataParamType "Link to this definition")

The type of the _data_ parameter in plotting functions.

matplotlib.typing.LegendLocType \= typing.Literal\['upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center', 'best', 'outside upper left', 'outside upper center', 'outside upper right', 'outside right upper', 'outside right center', 'outside right lower', 'outside lower right', 'outside lower center', 'outside lower left', 'outside left lower', 'outside left center', 'outside left upper'\] | tuple\[float, float\] | int[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.LegendLocType "Link to this definition")

Supported location specifiers for legends.

This is a superset of permissible entries. "best" is only applicable to Axes legends. All the "outside ..." locations are only applicable to figure legends.

matplotlib.typing.LogLevel[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.LogLevel "Link to this definition")

Literal type for valid logging levels accepted by [`matplotlib.set_loglevel()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.set_loglevel "matplotlib.set_loglevel")
.

alias of [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'\]

matplotlib.typing.HashableList(_iterable\=()_, _/_)[#](https://matplotlib.org/stable/api/typing_api.html#matplotlib.typing.HashableList "Link to this definition")

A nested list of Hashable values.

alias of [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")
\[`_HT` | `HashableList[_HT]`\]

On this page
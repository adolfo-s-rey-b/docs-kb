[Skip to main content](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#main-content)

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
    

`matplotlib`[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib "Link to this heading")

=======================================================================================================================

An object-oriented plotting library.

A procedural interface is provided by the companion pyplot module, which may be imported directly, e.g.:

import matplotlib.pyplot as plt

or using ipython:

ipython

at your terminal, followed by:

In \[1\]: %matplotlib
In \[2\]: import matplotlib.pyplot as plt

at the ipython shell prompt.

For the most part, direct use of the explicit object-oriented library is encouraged when programming; the implicit pyplot interface is primarily for working interactively. The exceptions to this suggestion are the pyplot functions [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
, [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
, [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
, and [`pyplot.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
, which can greatly simplify scripting. See [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces)
 for an explanation of the tradeoffs between the implicit and explicit interfaces.

Modules include:

[`matplotlib.axes`](https://matplotlib.org/stable/api/axes_api.html#module-matplotlib.axes "matplotlib.axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 class. Most pyplot functions are wrappers for [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 methods. The axes module is the highest level of OO access to the library.

[`matplotlib.figure`](https://matplotlib.org/stable/api/figure_api.html#module-matplotlib.figure "matplotlib.figure")

The [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class.

[`matplotlib.artist`](https://matplotlib.org/stable/api/artist_api.html#module-matplotlib.artist "matplotlib.artist")

The [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 base class for all classes that draw things.

[`matplotlib.lines`](https://matplotlib.org/stable/api/lines_api.html#module-matplotlib.lines "matplotlib.lines")

The [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 class for drawing lines and markers.

[`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")

Classes for drawing polygons.

[`matplotlib.text`](https://matplotlib.org/stable/api/text_api.html#module-matplotlib.text "matplotlib.text")

The [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 and [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 classes.

[`matplotlib.image`](https://matplotlib.org/stable/api/image_api.html#module-matplotlib.image "matplotlib.image")

The [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 and [`FigureImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage "matplotlib.image.FigureImage")
 classes.

[`matplotlib.collections`](https://matplotlib.org/stable/api/collections_api.html#module-matplotlib.collections "matplotlib.collections")

Classes for efficient drawing of groups of lines or polygons.

[`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")

Color specifications and making colormaps.

[`matplotlib.cm`](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")

Colormaps, and the [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 mixin class for providing color mapping functionality to other classes.

[`matplotlib.ticker`](https://matplotlib.org/stable/api/ticker_api.html#module-matplotlib.ticker "matplotlib.ticker")

Calculation of tick mark locations and formatting of tick labels.

[`matplotlib.backends`](https://matplotlib.org/stable/api/index_backend_api.html#module-matplotlib.backends "matplotlib.backends")

A subpackage with modules for various GUI libraries and output formats.

The base matplotlib namespace includes:

[`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")

Default configuration settings; their defaults may be overridden using a `matplotlibrc` file.

[`use`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")

Setting the Matplotlib backend. This should be called before any figure is created, because it is not possible to switch between different GUI backends after that.

The following environment variables can be used to customize the behavior:

[`MPLBACKEND`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLBACKEND)

This optional variable can be set to choose the Matplotlib backend. See [What is a backend?](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend)
.

[`MPLCONFIGDIR`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLCONFIGDIR)

This is the directory used to store user customizations to Matplotlib, as well as some caches to improve performance. If [`MPLCONFIGDIR`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLCONFIGDIR)
 is not defined, `_HOME_/.config/matplotlib` and `_HOME_/.cache/matplotlib` are used on Linux, and `_HOME_/.matplotlib` on other platforms, if they are writable. Otherwise, the Python standard library's [`tempfile.gettempdir`](https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir "(in Python v3.14)")
 is used to find a base directory in which the `matplotlib` subdirectory is created.

Matplotlib was initially written by John D. Hunter (1968-2012) and is now developed and maintained by a host of others.

Occasionally the internal documentation (python docstrings) will refer to MATLAB®, a registered trademark of The MathWorks, Inc.

Backend management[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#backend-management "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

matplotlib.use(_backend_, _\*_, _force\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1219-L1288)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "Link to this definition")

Select the backend used for rendering and GUI integration.

If pyplot is already imported, [`switch_backend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.switch_backend.html#matplotlib.pyplot.switch_backend "matplotlib.pyplot.switch_backend")
 is used to switch the backend.

Parameters:

**backend**str

The backend to switch to. This can either be one of the standard backend names, which are case-insensitive:

*   interactive backends: GTK3Agg, GTK3Cairo, GTK4Agg, GTK4Cairo, MacOSX, nbAgg, notebook, QtAgg, QtCairo, TkAgg, TkCairo, WebAgg, WX, WXAgg, WXCairo, Qt5Agg, Qt5Cairo
    
*   non-interactive backends: agg, cairo, pdf, pgf, ps, svg, template
    

or a string of the form: `module://my.module.name`.

notebook is a synonym for nbAgg.

Switching to an interactive backend is not possible if an unrelated event loop has already been started (e.g., switching to GTK3Agg if a TkAgg window has already been opened). Switching to a non-interactive backend is always possible.

**force**bool, default: True

If True (the default), raise an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "(in Python v3.14)")
 if the backend cannot be set up (either because it fails to import, or because an incompatible GUI interactive framework is already running); if False, silently ignore the failure.

See also

[Backends](https://matplotlib.org/stable/users/explain/figure/backends.html#backends)

[`matplotlib.get_backend`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_backend "matplotlib.get_backend")

[`matplotlib.pyplot.switch_backend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.switch_backend.html#matplotlib.pyplot.switch_backend "matplotlib.pyplot.switch_backend")

matplotlib.get\_backend(_\*_, _auto\_select\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1295-L1325)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_backend "Link to this definition")

Return the name of the current backend.

Parameters:

**auto\_select**bool, default: True

Whether to trigger backend resolution if no backend has been selected so far. If True, this ensures that a valid backend is returned. If False, this returns None if no backend has been selected so far.

Added in version 3.10.

Provisional

The _auto\_select_ flag is provisional. It may be changed or removed without prior warning.

See also

[`matplotlib.use`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")

matplotlib.interactive(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1328-L1332)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.interactive "Link to this definition")

Set whether to redraw after every plotting command (e.g. [`pyplot.xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
).

matplotlib.is\_interactive()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1335-L1344)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.is_interactive "Link to this definition")

Return whether to redraw after every plotting command.

Note

This function is only intended for use in backends. End users should use [`pyplot.isinteractive`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.isinteractive.html#matplotlib.pyplot.isinteractive "matplotlib.pyplot.isinteractive")
 instead.

Default values and styling[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#default-values-and-styling "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

matplotlib.rcParams: [RcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "Link to this definition")

The global configuration settings for Matplotlib.

This is a dictionary-like variable that stores the current configuration settings. Many of the values control styling, but others control various aspects of Matplotlib's behavior.

See [Matplotlib configuration - rcParams](https://matplotlib.org/stable/users/explain/configuration.html)
 for a full list of config parameters.

See [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
 for usage information.

### Notes[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#notes "Link to this heading")

This object is also available as `plt.rcParams` via the [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 module (which by convention is imported as `plt`).

class matplotlib.RcParams(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L688-L847)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "Link to this definition")

A dict-like key-value store for config parameters, including validation.

This is the data structure behind [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
.

The complete list of rcParams can be found in [Matplotlib configuration - rcParams](https://matplotlib.org/stable/users/explain/configuration.html)
.

find\_all(_pattern_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L826-L840)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams.find_all "Link to this definition")

Return the subset of this RcParams dictionary whose keys match, using [`re.search()`](https://docs.python.org/3/library/re.html#re.search "(in Python v3.14)")
, the given `pattern`.

Note

Changes to the returned dictionary are _not_ propagated to the parent RcParams dictionary.

copy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L842-L847)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams.copy "Link to this definition")

Copy this RcParams instance.

matplotlib.rc\_context(_rc\=None_, _fname\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1162-L1216)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "Link to this definition")

Return a context manager for temporarily changing rcParams.

The `[rcParams["backend"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=backend#rcparam-backend) ` will not be reset by the context manager.

rcParams changed both through the context manager invocation and in the body of the context will be reset on context exit.

Parameters:

**rc**dict

The rcParams to temporarily set.

**fname**str or path-like

A file with Matplotlib rc settings. If both _fname_ and _rc_ are given, settings from _rc_ take precedence.

See also

[The matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)

Examples

Passing explicit values via a dict:

with mpl.rc\_context({'interactive': False}):
    fig, ax \= plt.subplots()
    ax.plot(range(3), range(3))
    fig.savefig('example.png')
    plt.close(fig)

Loading settings from a file:

with mpl.rc\_context(fname\='print.rc'):
    plt.plot(x, y)  \# uses 'print.rc'

Setting in the context body:

with mpl.rc\_context():
    \# will be reset
    mpl.rcParams\['lines.linewidth'\] \= 5
    plt.plot(x, y)

matplotlib.rc(_group_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1017-L1092)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc "Link to this definition")

Set the current [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
. _group_ is the grouping for the rc, e.g., for `lines.linewidth` the group is `lines`, for `axes.facecolor`, the group is `axes`, and so on. Group may also be a list or tuple of group names, e.g., (_xtick_, _ytick_). _kwargs_ is a dictionary attribute name/value pairs, e.g.,:

rc('lines', linewidth\=2, color\='r')

sets the current [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 and is equivalent to:

rcParams\['lines.linewidth'\] \= 2
rcParams\['lines.color'\] \= 'r'

The following aliases are available to save typing for interactive users:

| Alias | Property |
| --- | --- |
| 'lw' | 'linewidth' |
| 'ls' | 'linestyle' |
| 'c' | 'color' |
| 'fc' | 'facecolor' |
| 'ec' | 'edgecolor' |
| 'mew' | 'markeredgewidth' |
| 'aa' | 'antialiased' |
| 'sans' | 'sans-serif' |

Thus you could abbreviate the above call as:

rc('lines', lw\=2, c\='r')

Note you can use python's kwargs dictionary facility to store dictionaries of default parameters. e.g., you can customize the font rc as follows:

font \= {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 'large'}
rc('font', \*\*font)  \# pass in the font dict as kwargs

This enables you to easily switch between several configurations. Use `matplotlib.style.use('default')` or [`rcdefaults()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcdefaults "matplotlib.rcdefaults")
 to restore the default [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 after changes.

Notes

Similar functionality is available by using the normal dict interface, i.e. `rcParams.update({"lines.linewidth": 2, ...})` (but `rcParams.update` does not support abbreviations or grouping).

matplotlib.rcdefaults()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1095-L1117)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcdefaults "Link to this definition")

Restore the [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 from Matplotlib's internal default style.

Style-blacklisted [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 (defined in `matplotlib.style.core.STYLE_BLACKLIST`) are not updated.

See also

[`matplotlib.rc_file_defaults`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file_defaults "matplotlib.rc_file_defaults")

Restore the [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 from the rc file originally loaded by Matplotlib.

[`matplotlib.style.use`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use "matplotlib.style.use")

Use a specific style file. Call `style.use('default')` to restore the default style.

matplotlib.rc\_file\_defaults()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1120-L1132)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file_defaults "Link to this definition")

Restore the [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 from the original rc file loaded by Matplotlib.

Style-blacklisted [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 (defined in `matplotlib.style.core.STYLE_BLACKLIST`) are not updated.

matplotlib.rc\_file(_fname_, _\*_, _use\_default\_template\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L1135-L1159)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file "Link to this definition")

Update [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 from file.

Style-blacklisted [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 (defined in `matplotlib.style.core.STYLE_BLACKLIST`) are not updated.

Parameters:

**fname**str or path-like

A file with Matplotlib rc settings.

**use\_default\_template**bool

If True, initialize with default parameters before updating with those in the given file. If False, the current configuration persists and only the parameters specified in the file are updated.

matplotlib.rc\_params(_fail\_on\_error\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L850-L852)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_params "Link to this definition")

Construct a [`RcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
 instance from the default Matplotlib rc file.

matplotlib.rc\_params\_from\_file(_fname_, _fail\_on\_error\=False_, _use\_default\_template\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L956-L989)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_params_from_file "Link to this definition")

Construct a [`RcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
 from file _fname_.

Parameters:

**fname**str or path-like

A file with Matplotlib rc settings.

**fail\_on\_error**bool

If True, raise an error when the parser fails to convert a parameter.

**use\_default\_template**bool

If True, initialize with default parameters before updating with those in the given file. If False, the configuration class only contains the parameters specified in the file. (Useful for updating dicts.)

matplotlib.get\_configdir()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L605-L622)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_configdir "Link to this definition")

Return the string path of the configuration directory.

The directory is chosen as follows:

1.  If the MPLCONFIGDIR environment variable is supplied, choose that.
    
2.  On Linux, follow the XDG specification and look first in `$XDG_CONFIG_HOME`, if defined, or `$HOME/.config`. On Windows, use `%LOCALAPPDATA%\matplotlib`. On other platforms, choose `$HOME/.matplotlib`.
    
3.  If the chosen directory exists and is writable, use that as the configuration directory.
    
4.  Else, create a temporary directory, and use it as the configuration directory.
    

matplotlib.matplotlib\_fname()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L643-L685)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.matplotlib_fname "Link to this definition")

Get the location of the config file.

The file location is determined in the following order

*   `$PWD/matplotlibrc`
    
*   `$MATPLOTLIBRC` if it is not a directory
    
*   `$MATPLOTLIBRC/matplotlibrc`
    
*   `$MPLCONFIGDIR/matplotlibrc`
    
*   On Linux,
    
    *   `$XDG_CONFIG_HOME/matplotlib/matplotlibrc` (if `$XDG_CONFIG_HOME` is defined)
        
    *   or `$HOME/.config/matplotlib/matplotlibrc` (if `$XDG_CONFIG_HOME` is not defined)
        
    
*   On other platforms, - `$HOME/.matplotlib/matplotlibrc` if `$HOME` is defined
    
*   Lastly, it looks in `$MATPLOTLIBDATA/matplotlibrc`, which should always exist.
    

matplotlib.get\_data\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L637-L640)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_data_path "Link to this definition")

Return the path to Matplotlib data.

Logging[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#logging "Link to this heading")

---------------------------------------------------------------------------------------------------------------

matplotlib.set\_loglevel(_level_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L284-L319)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.set_loglevel "Link to this definition")

Configure Matplotlib's logging levels.

Matplotlib uses the standard library [`logging`](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.14)")
 framework under the root logger 'matplotlib'. This is a helper function to:

*   set Matplotlib's root logger level
    
*   set the root logger handler's level, creating the handler if it does not exist yet
    

Typically, one should call `set_loglevel("INFO")` or `set_loglevel("DEBUG")` to get additional debugging information.

Users or applications that are installing their own logging handlers may want to directly manipulate `logging.getLogger('matplotlib')` rather than use this function.

Parameters:

**level**{"NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

The log level as defined in [Python logging levels](https://docs.python.org/3/library/logging.html#logging-levels)
.

For backwards compatibility, the levels are case-insensitive, but the capitalized version is preferred in analogy to [`logging.Logger.setLevel`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel "(in Python v3.14)")
.

Notes

The first time this function is called, an additional handler is attached to Matplotlib's root handler; this handler is reused every time and this function simply manipulates the logger and handler's level.

Colormaps and color sequences[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#colormaps-and-color-sequences "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

matplotlib.colormaps[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cm.py)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "Link to this definition")

Container for colormaps that are known to Matplotlib by name.

The universal registry instance is [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
. There should be no need for users to instantiate [`ColormapRegistry`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
 themselves.

Read access uses a dict-like interface mapping names to [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
s:

import matplotlib as mpl
cmap \= mpl.colormaps\['viridis'\]

Returned [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
s are copies, so that their modification does not change the global definition of the colormap.

Additional colormaps can be added via [`ColormapRegistry.register`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
:

mpl.colormaps.register(my\_colormap)

To get a list of all registered colormaps, you can do:

from matplotlib import colormaps
list(colormaps)

matplotlib.color\_sequences[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.color_sequences "Link to this definition")

Container for sequences of colors that are known to Matplotlib by name.

The universal registry instance is [`matplotlib.color_sequences`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.color_sequences "matplotlib.color_sequences")
. There should be no need for users to instantiate [`ColorSequenceRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")
 themselves.

Read access uses a dict-like interface mapping names to lists of colors:

import matplotlib as mpl
colors \= mpl.color\_sequences\['tab10'\]

For a list of built in color sequences, see [Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)
. The returned lists are copies, so that their modification does not change the global definition of the color sequence.

Additional color sequences can be added via [`ColorSequenceRegistry.register`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry.register "matplotlib.colors.ColorSequenceRegistry.register")
:

mpl.color\_sequences.register('rgb', \['r', 'g', 'b'\])

Miscellaneous[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#miscellaneous "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

class matplotlib.MatplotlibDeprecationWarning[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L20-L21)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.MatplotlibDeprecationWarning "Link to this definition")

A class for issuing deprecation warnings for Matplotlib users.

matplotlib.get\_cachedir()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/__init__.py#L625-L634)
[#](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_cachedir "Link to this definition")

Return the string path of the cache directory.

The procedure used to find the directory is the same as for [`get_configdir`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_configdir "matplotlib.get_configdir")
, except using `$XDG_CACHE_HOME`/`$HOME/.cache` instead on Linux. On Windows, uses `%LOCALAPPDATA%\matplotlib` (same as config).

On this page
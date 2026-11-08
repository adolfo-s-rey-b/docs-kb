[Skip to main content](https://matplotlib.org/stable/users/explain/customizing.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/users/explain/customizing.html#sphx-glr-download-users-explain-customizing-py)
 to download the full example code.

Customizing Matplotlib with style sheets and rcParams[#](https://matplotlib.org/stable/users/explain/customizing.html#customizing-matplotlib-with-style-sheets-and-rcparams "Link to this heading")

====================================================================================================================================================================================================

Many aspects of Matplotlib's behavior and default styles can be customized through the use of rc (runtime configuration) settings. The current values are stored in [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
.

There are three ways to customize Matplotlib, all of which effectively change [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
:

1.  [Setting rcParams at runtime](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-dynamic-rc-settings)
    .
    
2.  [Using style sheets](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-style-sheets)
    .
    
3.  [Changing your matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)
    .
    

Setting rcParams at runtime takes precedence over style sheets, style sheets take precedence over `matplotlibrc` files.

Runtime rc settings[#](https://matplotlib.org/stable/users/explain/customizing.html#runtime-rc-settings "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

You can dynamically change the default rc (runtime configuration) settings in a python script or interactively from the python shell. All rc settings are stored in a dictionary-like variable called [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
, which is global to the matplotlib package. See [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 for a full list of configurable rcParams. rcParams can be modified directly, for example:

from cycler import [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

[mpl.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['lines.linewidth'\] \= 2
[mpl.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['lines.linestyle'\] \= '--'
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(50)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![customizing](https://matplotlib.org/stable/_images/sphx_glr_customizing_001_2_00x.png)

Note, that in order to change the usual [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 color you have to change the _prop\_cycle_ property of _axes_:

[mpl.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.prop\_cycle'\] \= [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(color\=\['r', 'g', 'b', 'y'\])
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)  \# first color is red

![customizing](https://matplotlib.org/stable/_images/sphx_glr_customizing_002_2_00x.png)

Matplotlib also provides a couple of convenience functions for modifying rc settings. [`matplotlib.rc`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc "matplotlib.rc")
 can be used to modify multiple settings in a single group at once, using keyword arguments:

[mpl.rc](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc "matplotlib.rc")
('lines', linewidth\=4, linestyle\='-.')
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![customizing](https://matplotlib.org/stable/_images/sphx_glr_customizing_003_2_00x.png)

### Temporary rc settings[#](https://matplotlib.org/stable/users/explain/customizing.html#temporary-rc-settings "Link to this heading")

The [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 object can also be changed temporarily using the [`matplotlib.rc_context`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
 context manager:

with [mpl.rc\_context](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
({'lines.linewidth': 2, 'lines.linestyle': ':'}):
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![customizing](https://matplotlib.org/stable/_images/sphx_glr_customizing_004_2_00x.png)

[`matplotlib.rc_context`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
 can also be used as a decorator to modify the defaults within a function:

@mpl.rc\_context({'lines.linewidth': 3, 'lines.linestyle': '-'})
def plotting\_function():
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

plotting\_function()

![customizing](https://matplotlib.org/stable/_images/sphx_glr_customizing_005_2_00x.png)

[`matplotlib.rcdefaults`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcdefaults "matplotlib.rcdefaults")
 will restore the standard Matplotlib default settings.

There is some degree of validation when setting the values of rcParams, see [`matplotlib.rcsetup`](https://matplotlib.org/stable/api/rcsetup_api.html#module-matplotlib.rcsetup "matplotlib.rcsetup")
 for details.

Using style sheets[#](https://matplotlib.org/stable/users/explain/customizing.html#using-style-sheets "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

Another way to change the visual appearance of plots is to set the rcParams in a so-called style sheet and import that style sheet with [`matplotlib.style.use`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use "matplotlib.style.use")
. In this way you can switch easily between different styles by simply changing the imported style sheet. A style sheets looks the same as a [matplotlibrc](https://matplotlib.org/stable/users/explain/customizing.html#matplotlibrc-sample)
 file, but in a style sheet you can only set rcParams that are related to the actual style of a plot. Other rcParams, like _backend_, will be ignored. `matplotlibrc` files support all rcParams. The rationale behind this is to make style sheets portable between different machines without having to worry about dependencies which might or might not be installed on another machine. For a full list of rcParams see [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
. For a list of rcParams that are ignored in style sheets see [`matplotlib.style.use`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use "matplotlib.style.use")
.

There are a number of pre-defined styles [provided by Matplotlib](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
. For example, there's a pre-defined style called "ggplot", which emulates the aesthetics of [ggplot](https://ggplot2.tidyverse.org/)
 (a popular plotting package for [R](https://www.r-project.org/)
). To use this style, add:

plt.style.use('ggplot')

To list all available styles, use:

print([plt.style.available](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

\['Solarize\_Light2', 'bmh', 'classic', 'dark\_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'petroff6', 'petroff8', 'seaborn-v0\_8', 'seaborn-v0\_8-bright', 'seaborn-v0\_8-colorblind', 'seaborn-v0\_8-dark', 'seaborn-v0\_8-dark-palette', 'seaborn-v0\_8-darkgrid', 'seaborn-v0\_8-deep', 'seaborn-v0\_8-muted', 'seaborn-v0\_8-notebook', 'seaborn-v0\_8-paper', 'seaborn-v0\_8-pastel', 'seaborn-v0\_8-poster', 'seaborn-v0\_8-talk', 'seaborn-v0\_8-ticks', 'seaborn-v0\_8-white', 'seaborn-v0\_8-whitegrid', 'tableau-colorblind10'\]

### Defining your own style[#](https://matplotlib.org/stable/users/explain/customizing.html#defining-your-own-style "Link to this heading")

You can create custom styles and use them by calling [`style.use`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use "matplotlib.style.use")
 with the path or URL to the style sheet.

For example, you might want to create `./images/presentation.mplstyle` with the following:

axes.titlesize : 24
axes.labelsize : 20
lines.linewidth : 3
lines.markersize : 10
xtick.labelsize : 16
ytick.labelsize : 16

Then, when you want to adapt a plot designed for a paper to one that looks good in a presentation, you can just add:

\>>> import matplotlib.pyplot as plt
\>>> plt.style.use('./images/presentation.mplstyle')

### Distributing styles[#](https://matplotlib.org/stable/users/explain/customizing.html#distributing-styles "Link to this heading")

You can include style sheets into standard importable Python packages (which can be e.g. distributed on PyPI). If your package is importable as `import mypackage`, with a `mypackage/__init__.py` module, and you add a `mypackage/presentation.mplstyle` style sheet, then it can be used as `plt.style.use("mypackage.presentation")`. Subpackages (e.g. `dotted.package.name`) are also supported.

Alternatively, you can make your style known to Matplotlib by placing your `<style-name>.mplstyle` file into `mpl_configdir/stylelib`. You can then load your custom style sheet with a call to `style.use(<style-name>)`. By default `mpl_configdir` should be `~/.config/matplotlib`, but you can check where yours is with [`matplotlib.get_configdir()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_configdir "matplotlib.get_configdir")
; you may need to create this directory. You also can change the directory where Matplotlib looks for the stylelib/ folder by setting the [`MPLCONFIGDIR`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLCONFIGDIR)
 environment variable, see [matplotlib configuration and cache directory locations](https://matplotlib.org/stable/install/index.html#locating-matplotlib-config-dir)
.

Note that a custom style sheet in `mpl_configdir/stylelib` will override a style sheet defined by Matplotlib if the styles have the same name.

Once your `<style-name>.mplstyle` file is in the appropriate `mpl_configdir` you can specify your style with:

\>>> import matplotlib.pyplot as plt
\>>> plt.style.use(<style\-name\>)

### Composing styles[#](https://matplotlib.org/stable/users/explain/customizing.html#composing-styles "Link to this heading")

Style sheets are designed to be composed together. So you can have a style sheet that customizes colors and a separate style sheet that alters element sizes for presentations. These styles can easily be combined by passing a list of styles:

\>>> import matplotlib.pyplot as plt
\>>> plt.style.use(\['dark\_background', 'presentation'\])

Note that styles further to the right will overwrite values that are already defined by styles on the left.

### Temporary styling[#](https://matplotlib.org/stable/users/explain/customizing.html#temporary-styling "Link to this heading")

If you only want to use a style for a specific block of code but don't want to change the global styling, the style package provides a context manager for limiting your changes to a specific scope. To isolate your styling changes, you can write something like the following:

with plt.style.context('dark\_background'):
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
)), 'r-o')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![customizing](https://matplotlib.org/stable/_images/sphx_glr_customizing_006_2_00x.png)

The `matplotlibrc` file[#](https://matplotlib.org/stable/users/explain/customizing.html#the-matplotlibrc-file "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Matplotlib uses `matplotlibrc` configuration files to customize all kinds of properties, which we call 'rc settings' or 'rc parameters'. You can control the defaults of almost every property in Matplotlib: figure size and DPI, line width, color and style, Axes, axis and grid properties, text and font properties and so on. The `matplotlibrc` is read at startup to configure Matplotlib. Matplotlib looks for `matplotlibrc` in four locations, in the following order:

1.  `matplotlibrc` in the current working directory, usually used for specific customizations that you do not want to apply elsewhere.
    
2.  `$MATPLOTLIBRC` if it is a file, else `$MATPLOTLIBRC/matplotlibrc`.
    
3.  It next looks in a user-specific place, depending on your platform:
    
    *   On Linux and FreeBSD, it looks in `.config/matplotlib/matplotlibrc` (or `$XDG_CONFIG_HOME/matplotlib/matplotlibrc`) if you've customized your environment.
        
    *   On other platforms, it looks in `.matplotlib/matplotlibrc`.
        
    
    See [matplotlib configuration and cache directory locations](https://matplotlib.org/stable/install/index.html#locating-matplotlib-config-dir)
    .
    
4.  `_INSTALL_/matplotlib/mpl-data/matplotlibrc`, where `_INSTALL_` is something like `/usr/lib/python3.10/site-packages` on Linux, and maybe `C:\Python310\Lib\site-packages` on Windows. Every time you install matplotlib, this file will be overwritten, so if you want your customizations to be saved, please move this file to your user-specific matplotlib directory.
    

Once a `matplotlibrc` file has been found, it will _not_ search any of the other paths. When a [style sheet](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-style-sheets)
 is given with `style.use('<path>/<style-name>.mplstyle')`, settings specified in the style sheet take precedence over settings in the `matplotlibrc` file.

To display where the currently active `matplotlibrc` file was loaded from, one can do the following:

\>>> import matplotlib
\>>> matplotlib.matplotlib\_fname()
'/home/foo/.config/matplotlib/matplotlibrc'

See below for a sample [matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#matplotlibrc-sample)
 and see [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 for a full list of configurable rcParams.

### The default `matplotlibrc` file[#](https://matplotlib.org/stable/users/explain/customizing.html#the-default-matplotlibrc-file "Link to this heading")

\#### MATPLOTLIBRC FORMAT

\## DO NOT EDIT THIS FILE, MAKE A COPY FIRST
##
\## This is a sample Matplotlib configuration file - you can find a copy
\## of it on your system in site-packages/matplotlib/mpl-data/matplotlibrc
\## (relative to your Python installation location).
\## DO NOT EDIT IT!
##
\## If you wish to change your default style, copy this file to one of the
\## following locations:
\##     Unix/Linux:
\##         $HOME/.config/matplotlib/matplotlibrc OR
\##         $XDG\_CONFIG\_HOME/matplotlib/matplotlibrc (if $XDG\_CONFIG\_HOME is set)
\##     Other platforms:
\##         $HOME/.matplotlib/matplotlibrc
\## and edit that copy.
##
\## See https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files
\## for more details on the paths which are checked for the configuration file.
##
\## Blank lines, or lines starting with a comment symbol, are ignored, as are
\## trailing comments.  Other lines must have the format:
\##     key: val  # optional comment
##
\## Formatting: Use PEP8-like style (as enforced in the rest of the codebase).
\## All lines start with an additional '#', so that removing all leading '#'s
\## yields a valid style file.
##
\## Colors: for the color values below, you can either use
\##     - a Matplotlib color string, such as r, k, or b
\##     - an RGB tuple, such as (1.0, 0.5, 0.0)
\##     - a double-quoted hex string, such as "#ff00ff".
\##       The unquoted string ff00ff is also supported for backward
\##       compatibility, but is discouraged.
\##     - a scalar grayscale intensity such as 0.75
\##     - a legal html color name, e.g., red, blue, darkslategray
##
\## String values may optionally be enclosed in double quotes, which allows
\## using the comment character # in the string.
##
\## This file (and other style files) must be encoded as utf-8.
##
\## Matplotlib configuration are currently divided into following parts:
\##     - BACKENDS
\##     - LINES
\##     - PATCHES
\##     - HATCHES
\##     - BOXPLOT
\##     - FONT
\##     - TEXT
\##     - LaTeX
\##     - AXES
\##     - DATES
\##     - TICKS
\##     - GRIDS
\##     - LEGEND
\##     - FIGURE
\##     - IMAGES
\##     - CONTOUR PLOTS
\##     - ERRORBAR PLOTS
\##     - HISTOGRAM PLOTS
\##     - SCATTER PLOTS
\##     - AGG RENDERING
\##     - PATHS
\##     - SAVING FIGURES
\##     - INTERACTIVE KEYMAPS
\##     - ANIMATION

\##### CONFIGURATION BEGINS HERE

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* BACKENDS                                                                \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## The default backend.  If you omit this parameter, the first working
\## backend from the following list is used:
\##     MacOSX QtAgg Gtk4Agg Gtk3Agg TkAgg WxAgg Agg
\## Other choices include:
\##     QtCairo GTK4Cairo GTK3Cairo TkCairo WxCairo Cairo
\##     Qt5Agg Qt5Cairo Wx  # deprecated.
\##     PS PDF SVG Template
\## You can also deploy your own backend outside of Matplotlib by referring to
\## the module name (which must be in the PYTHONPATH) as 'module://my\_backend'.
##backend: Agg

\## The port to use for the web server in the WebAgg backend.
#webagg.port: 8988

\## The address on which the WebAgg web server should be reachable
#webagg.address: 127.0.0.1

\## If webagg.port is unavailable, a number of other random ports will
\## be tried until one that is available is found.
#webagg.port\_retries: 50

\## When True, open the web browser to the plot that is shown
#webagg.open\_in\_browser: True

\## If you are running pyplot inside a GUI and your backend choice
\## conflicts, we will automatically try to find a compatible one for
\## you if backend\_fallback is True
#backend\_fallback: True

#interactive: False
#figure.hooks:          # list of dotted.module.name:dotted.callable.name
#toolbar:     toolbar2  # {None, toolbar2, toolmanager}
#timezone:    UTC       # a pytz timezone string, e.g., US/Central or Europe/Paris

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* LINES                                                                   \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## See https://matplotlib.org/stable/api/artist\_api.html#module-matplotlib.lines
\## for more information on line properties.
#lines.linewidth: 1.5               # line width in points
#lines.linestyle: -                 # solid line
#lines.color:     C0                # has no affect on plot(); see axes.prop\_cycle
#lines.marker:          None        # the default marker
#lines.markerfacecolor: auto        # the default marker face color
#lines.markeredgecolor: auto        # the default marker edge color
#lines.markeredgewidth: 1.0         # the line width around the marker symbol
#lines.markersize:      6           # marker size, in points
#lines.dash\_joinstyle:  round       # {miter, round, bevel}
#lines.dash\_capstyle:   butt        # {butt, round, projecting}
#lines.solid\_joinstyle: round       # {miter, round, bevel}
#lines.solid\_capstyle:  projecting  # {butt, round, projecting}
#lines.antialiased: True            # render lines in antialiased (no jaggies)

\## The three standard dash patterns.  These are scaled by the linewidth.
#lines.dashed\_pattern: 3.7, 1.6
#lines.dashdot\_pattern: 6.4, 1.6, 1, 1.6
#lines.dotted\_pattern: 1, 1.65
#lines.scale\_dashes: True

#markers.fillstyle: full  # {full, left, right, bottom, top, none}

#pcolor.shading: auto
#pcolormesh.snap: True  # Whether to snap the mesh to pixel boundaries. This is
                        \# provided solely to allow old test images to remain
                        \# unchanged. Set to False to obtain the previous behavior.

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* PATCHES                                                                 \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## Patches are graphical objects that fill 2D space, like polygons or circles.
\## See https://matplotlib.org/stable/api/artist\_api.html#module-matplotlib.patches
\## for more information on patch properties.
#patch.linewidth:       1.0    # edge width in points.
#patch.facecolor:       C0
#patch.edgecolor:       black  # By default, Patches and Collections do not draw edges.
                               \# This value is only used if facecolor is "none"
                               \# (an Artist without facecolor and edgecolor would be
                               \# invisible)  or if patch.force\_edgecolor is True.
#patch.force\_edgecolor: False  # By default, Patches and Collections do not draw edges.
                               \# Set this to True to draw edges with patch.edgedcolor
                               \# as the default edgecolor.
                               \# This is mainly relevant for styles.
#patch.antialiased:     True   # render patches in antialiased (no jaggies)

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* HATCHES                                                                 \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#hatch.color:     edge
#hatch.linewidth: 1.0

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* BOXPLOT                                                                 \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#boxplot.notch:       False
#boxplot.vertical:    True
#boxplot.whiskers:    1.5
#boxplot.bootstrap:   None
#boxplot.patchartist: False
#boxplot.showmeans:   False
#boxplot.showcaps:    True
#boxplot.showbox:     True
#boxplot.showfliers:  True
#boxplot.meanline:    False

#boxplot.flierprops.color:           black
#boxplot.flierprops.marker:          o
#boxplot.flierprops.markerfacecolor: none
#boxplot.flierprops.markeredgecolor: black
#boxplot.flierprops.markeredgewidth: 1.0
#boxplot.flierprops.markersize:      6
#boxplot.flierprops.linestyle:       none
#boxplot.flierprops.linewidth:       1.0

#boxplot.boxprops.color:     black
#boxplot.boxprops.linewidth: 1.0
#boxplot.boxprops.linestyle: -

#boxplot.whiskerprops.color:     black
#boxplot.whiskerprops.linewidth: 1.0
#boxplot.whiskerprops.linestyle: -

#boxplot.capprops.color:     black
#boxplot.capprops.linewidth: 1.0
#boxplot.capprops.linestyle: -

#boxplot.medianprops.color:     C1
#boxplot.medianprops.linewidth: 1.0
#boxplot.medianprops.linestyle: -

#boxplot.meanprops.color:           C2
#boxplot.meanprops.marker:          ^
#boxplot.meanprops.markerfacecolor: C2
#boxplot.meanprops.markeredgecolor: C2
#boxplot.meanprops.markersize:       6
#boxplot.meanprops.linestyle:       --
#boxplot.meanprops.linewidth:       1.0

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* FONT                                                                    \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## The font properties used by \`text.Text\`.
\## See https://matplotlib.org/stable/api/font\_manager\_api.html for more information
\## on font properties.  The 6 font properties used for font matching are
\## given below with their default values.
##
\## The font.family property can take either a single or multiple entries of any
\## combination of concrete font names (not supported when rendering text with
\## usetex) or the following five generic values:
\##     - 'serif' (e.g., Times),
\##     - 'sans-serif' (e.g., Helvetica),
\##     - 'cursive' (e.g., Zapf-Chancery),
\##     - 'fantasy' (e.g., Western), and
\##     - 'monospace' (e.g., Courier).
\## Each of these values has a corresponding default list of font names
\## (font.serif, etc.); the first available font in the list is used.  Note that
\## for font.serif, font.sans-serif, and font.monospace, the first element of
\## the list (a DejaVu font) will always be used because DejaVu is shipped with
\## Matplotlib and is thus guaranteed to be available; the other entries are
\## left as examples of other possible values.
##
\## The font.style property has three values: normal (or roman), italic
\## or oblique.  The oblique style will be used for italic, if it is not
\## present.
##
\## The font.variant property has two values: normal or small-caps.  For
\## TrueType fonts, which are scalable fonts, small-caps is equivalent
\## to using a font size of 'small', or about 83 % of the current font
\## size.
##
\## The font.weight property has effectively 13 values: normal, bold,
\## bolder, lighter, 100, 200, 300, ..., 900.  Normal is the same as
\## 400, and bold is 700.  bolder and lighter are relative values with
\## respect to the current weight.
##
\## The font.stretch property has 11 values: ultra-condensed,
\## extra-condensed, condensed, semi-condensed, normal, semi-expanded,
\## expanded, extra-expanded, ultra-expanded, wider, and narrower.  This
\## property is not currently implemented.
##
\## The font.size property is the default font size for text, given in points.
\## 10 pt is the standard value.
##
\## Note that font.size controls default text sizes.  To configure
\## special text sizes tick labels, axes, labels, title, etc., see the rc
\## settings for axes and ticks.  Special text sizes can be defined
\## relative to font.size, using the following values: xx-small, x-small,
\## small, medium, large, x-large, xx-large

#font.family:  sans-serif
#font.style:   normal
#font.variant: normal
#font.weight:  normal
#font.stretch: normal
#font.size:    10.0

#font.serif:      DejaVu Serif, Bitstream Vera Serif, Computer Modern Roman, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif
#font.sans-serif: DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
#font.cursive:    Apple Chancery, Textile, Zapf Chancery, Sand, Script MT, Felipa, Comic Neue, Comic Sans MS, cursive
#font.fantasy:    Chicago, Charcoal, Impact, Western, xkcd script, fantasy
#font.monospace:  DejaVu Sans Mono, Bitstream Vera Sans Mono, Computer Modern Typewriter, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace

\## If font.enable\_last\_resort is True, then Unicode Consortium's Last Resort
\## font will be appended to all font selections. This ensures that there will
\## always be a glyph displayed.
#font.enable\_last\_resort: true

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* TEXT                                                                    \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## The text properties used by \`text.Text\`.
\## See https://matplotlib.org/stable/api/artist\_api.html#module-matplotlib.text
\## for more information on text properties
#text.color: black

\## The language of the text in a format accepted by libraqm, namely \`a BCP47 language
\## code <https://www.w3.org/International/articles/language-tags/>\`\_. If None, then no
\## particular language will be implied, and default font settings will be used.
#text.language: None

\## FreeType hinting flag ("foo" corresponds to FT\_LOAD\_FOO); may be one of the
\## following (Proprietary Matplotlib-specific synonyms are given in parentheses,
\## but their use is discouraged):
\## - default: Use the font's native hinter if possible, else FreeType's auto-hinter.
\##            ("either" is a synonym).
\## - no\_autohint: Use the font's native hinter if possible, else don't hint.
\##                ("native" is a synonym.)
\## - force\_autohint: Use FreeType's auto-hinter.  ("auto" is a synonym.)
\## - no\_hinting: Disable hinting.  ("none" is a synonym.)
#text.hinting: default

#text.hinting\_factor: None  # This setting does nothing and is deprecated.
#text.kerning\_factor: None  # Specifies the scaling factor for kerning values. Values
                            \# other than 0, 6, or None have no defined meaning.
                            \# This setting is deprecated.
#text.antialiased: True  # If True (default), the text will be antialiased.
                         \# This only affects raster outputs.
#text.parse\_math: True  # Use mathtext if there is an even number of unescaped
                        \# dollar signs.

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* LaTeX                                                                   \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## For more information on LaTeX properties, see
\## https://matplotlib.org/stable/users/explain/text/usetex.html
#text.usetex: False  # use latex for all text handling. The following fonts
                     \# are supported through the usual rc parameter settings:
                     \# new century schoolbook, bookman, times, palatino,
                     \# zapf chancery, charter, serif, sans-serif, helvetica,
                     \# avant garde, courier, monospace, computer modern roman,
                     \# computer modern sans serif, computer modern typewriter

\## The TeX engine/format to use.  The following values are supported:
\## - "latex": The classic TeX engine (the current default).  All backends render
\##    TeX's output by parsing the DVI output into glyphs and boxes and emitting
\##    those one by one.
\## - "latex+dvipng": The same as "latex", with the exception that Agg-based
\##   backends rely on dvipng to rasterize TeX's output.  This value was the
\##   default up to Matplotlib 3.10.
#text.latex.engine: latex

#text.latex.preamble:   # IMPROPER USE OF THIS FEATURE WILL LEAD TO LATEX FAILURES
                        \# AND IS THEREFORE UNSUPPORTED. PLEASE DO NOT ASK FOR HELP
                        \# IF THIS FEATURE DOES NOT DO WHAT YOU EXPECT IT TO.
                        \# text.latex.preamble is a single line of LaTeX code that
                        \# will be passed on to the LaTeX system. It may contain
                        \# any code that is valid for the LaTeX "preamble", i.e.
                        \# between the "\\documentclass" and "\\begin{document}"
                        \# statements.
                        \# Note that it has to be put on a single line, which may
                        \# become quite long.
                        \# The following packages are always loaded with usetex,
                        \# so beware of package collisions:
                        \#   color, fix-cm, geometry, graphicx, textcomp.
                        \# PostScript (PSNFSS) font packages may also be
                        \# loaded, depending on your font settings.

\## The following settings allow you to select the fonts in math mode.
#mathtext.fontset: dejavusans  # Should be 'dejavusans' (default),
                               \# 'dejavuserif', 'cm' (Computer Modern), 'stix',
                               \# 'stixsans' or 'custom'
\## "mathtext.fontset: custom" is defined by the mathtext.bf, .cal, .it, ...
\## settings which map a TeX font name to a fontconfig font pattern.  (These
\## settings are not used for other font sets.)
#mathtext.bf:  sans:bold
#mathtext.bfit: sans:italic:bold
#mathtext.cal: cursive
#mathtext.it:  sans:italic
#mathtext.rm:  sans
#mathtext.sf:  sans
#mathtext.tt:  monospace
#mathtext.fallback: cm  # Select fallback font from \['cm' (Computer Modern), 'stix'\
                        \# 'stixsans'\] when a symbol cannot be found in one of the
                        \# custom math fonts. Select 'None' to not perform fallback
                        \# and replace the missing character by a dummy symbol.
#mathtext.default: normal  # The default font to use for math.
                           \# Can be any of the LaTeX font names (normal, it, bf,
                           \# etc.), including the special name "regular" for the
                           \# same font used in regular text.

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* AXES                                                                    \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## Following are default face and edge colors, default tick sizes,
\## default font sizes for tick labels, and so on.  See
\## https://matplotlib.org/stable/api/axes\_api.html#module-matplotlib.axes
#axes.facecolor:     white   # axes background color
#axes.edgecolor:     black   # axes edge color
#axes.linewidth:     0.8     # edge line width
#axes.grid:          False   # display grid or not
#axes.grid.axis:     both    # which axis the grid should apply to
#axes.grid.which:    major   # grid lines at {major, minor, both} ticks
#axes.titlelocation: center  # alignment of the title: {left, right, center}
#axes.titlesize:     large   # font size of the axes title
#axes.titleweight:   normal  # font weight of title
#axes.titlecolor:    auto    # color of the axes title, auto falls back to
                             \# text.color as default value
#axes.titley:        None    # position title (axes relative units).  None implies auto
#axes.titlepad:      6.0     # pad between axes and title in points
#axes.labelsize:     medium  # font size of the x and y labels
#axes.labelpad:      4.0     # space between label and axis
#axes.labelweight:   normal  # weight of the x and y labels
#axes.labelcolor:    black
#axes.axisbelow:     line    # draw axis gridlines and ticks:
                             \#     - below patches (True)
                             \#     - above patches but below lines ('line')
                             \#     - above all (False)

#axes.formatter.limits: -5, 6  # use scientific notation if log10
                               \# of the axis range is smaller than the
                               \# first or larger than the second
#axes.formatter.use\_locale: False  # When True, format tick labels
                                   \# according to the user's locale.
                                   \# For example, use ',' as a decimal
                                   \# separator in the fr\_FR locale.
#axes.formatter.use\_mathtext: False  # When True, use mathtext for scientific
                                     \# notation.
#axes.formatter.min\_exponent: 0  # minimum exponent to format in scientific notation
#axes.formatter.useoffset: True  # If True, the tick label formatter
                                 \# will default to labeling ticks relative
                                 \# to an offset when the data range is
                                 \# small compared to the minimum absolute
                                 \# value of the data.
#axes.formatter.offset\_threshold: 4  # When useoffset is True, the offset
                                     \# will be used when it can remove
                                     \# at least this number of significant
                                     \# digits from tick labels.

#axes.spines.left:   True  # display axis spines
#axes.spines.bottom: True
#axes.spines.top:    True
#axes.spines.right:  True

#axes.unicode\_minus: True  # use Unicode for the minus symbol rather than hyphen.  See
                           \# https://en.wikipedia.org/wiki/Plus\_and\_minus\_signs#Character\_codes
#axes.prop\_cycle: cycler(color='tab10')
                  \# color cycle for plot lines as either a named color sequence or a list
                  \# of string color specs: single letter, long name, or web-style hex
                  \# As opposed to all other parameters in this file, the color
                  \# values must be enclosed in quotes for this parameter,
                  \# e.g. '1f77b4', instead of 1f77b4.
                  \# See also https://matplotlib.org/stable/users/explain/artists/color\_cycle.html
                  \# for more details on prop\_cycle usage.
#axes.xmargin:   .05  # x margin.  See \`axes.Axes.margins\`
#axes.ymargin:   .05  # y margin.  See \`axes.Axes.margins\`
#axes.zmargin:   .05  # z margin.  See \`axes.Axes.margins\`
#axes.autolimit\_mode: data  # If "data", use axes.xmargin and axes.ymargin as is.
                            \# If "round\_numbers", after application of margins, axis
                            \# limits are further expanded to the nearest "round" number.
#polaraxes.grid:    True   # display grid on polar axes
#axes3d.grid:       True   # display grid on 3D axes
#axes3d.automargin: False  # automatically add margin when manually setting 3D axis limits

#axes3d.xaxis.panecolor:    (0.95, 0.95, 0.95, 0.5)  # background pane on 3D axes
#axes3d.yaxis.panecolor:    (0.90, 0.90, 0.90, 0.5)  # background pane on 3D axes
#axes3d.zaxis.panecolor:    (0.925, 0.925, 0.925, 0.5)  # background pane on 3D axes

#axes3d.depthshade: True  # depth shade for 3D scatter plots
#axes3d.depthshade\_minalpha: 0.3  # minimum alpha value for depth shading

#axes3d.mouserotationstyle: arcball  # {azel, trackball, sphere, arcball}
                            \# See also https://matplotlib.org/stable/api/toolkits/mplot3d/view\_angles.html#rotation-with-mouse
#axes3d.trackballsize: 0.667  # trackball diameter, in units of the Axes bbox
#axes3d.trackballborder: 0.2  # trackball border width, in units of the Axes bbox (only for 'sphere' and 'arcball' style)
#axes3d.snap\_rotation: 5.0  # Snap angle (degrees) for 3D rotation when holding Control.
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* AXIS                                                                    \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#xaxis.labellocation: center  # alignment of the xaxis label: {left, right, center}
#yaxis.labellocation: center  # alignment of the yaxis label: {bottom, top, center}

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* DATES                                                                   \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## These control the default format strings used in AutoDateFormatter.
\## Any valid format datetime format string can be used (see the python
\## \`datetime\` for details).  For example, by using:
\##     - '%x' will use the locale date representation
\##     - '%X' will use the locale time representation
\##     - '%c' will use the full locale datetime representation
\## These values map to the scales:
\##     {'year': 365, 'month': 30, 'day': 1, 'hour': 1/24, 'minute': 1 / (24 \* 60)}

#date.autoformatter.year:        %Y
#date.autoformatter.month:       %Y-%m
#date.autoformatter.day:         %Y-%m-%d
#date.autoformatter.hour:        %m-%d %H
#date.autoformatter.minute:      %d %H:%M
#date.autoformatter.second:      %H:%M:%S
#date.autoformatter.microsecond: %M:%S.%f
\## The reference date for Matplotlib's internal date representation
\## See https://matplotlib.org/stable/gallery/ticks/date\_precision\_and\_epochs.html
#date.epoch: 1970-01-01T00:00:00
\## 'auto', 'concise':
#date.converter:                  auto
\## For auto converter whether to use interval\_multiples:
#date.interval\_multiples:         True

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* TICKS                                                                   \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## See https://matplotlib.org/stable/api/axis\_api.html#matplotlib.axis.Tick
#xtick.top:           False   # draw ticks on the top side
#xtick.bottom:        True    # draw ticks on the bottom side
#xtick.labeltop:      False   # draw label on the top
#xtick.labelbottom:   True    # draw label on the bottom
#xtick.major.size:    3.5     # major tick size in points
#xtick.minor.size:    2       # minor tick size in points
#xtick.major.width:   0.8     # major tick width in points
#xtick.minor.width:   0.6     # minor tick width in points
#xtick.major.pad:     3.5     # distance to major tick label in points
#xtick.minor.pad:     3.4     # distance to the minor tick label in points
#xtick.color:         black   # color of the ticks
#xtick.labelcolor:    inherit # color of the tick labels or inherit from xtick.color
#xtick.labelsize:     medium  # font size of the tick labels
#xtick.direction:     out     # direction: {in, out, inout}
#xtick.minor.visible: False   # visibility of minor ticks on x-axis
#xtick.major.top:     True    # draw x axis top major ticks
#xtick.major.bottom:  True    # draw x axis bottom major ticks
#xtick.minor.top:     True    # draw x axis top minor ticks
#xtick.minor.bottom:  True    # draw x axis bottom minor ticks
#xtick.minor.ndivs:   auto    # number of minor ticks between the major ticks on x-axis
#xtick.alignment:     center  # alignment of xticks

#ytick.left:          True    # draw ticks on the left side
#ytick.right:         False   # draw ticks on the right side
#ytick.labelleft:     True    # draw tick labels on the left side
#ytick.labelright:    False   # draw tick labels on the right side
#ytick.major.size:    3.5     # major tick size in points
#ytick.minor.size:    2       # minor tick size in points
#ytick.major.width:   0.8     # major tick width in points
#ytick.minor.width:   0.6     # minor tick width in points
#ytick.major.pad:     3.5     # distance to major tick label in points
#ytick.minor.pad:     3.4     # distance to the minor tick label in points
#ytick.color:         black   # color of the ticks
#ytick.labelcolor:    inherit # color of the tick labels or inherit from ytick.color
#ytick.labelsize:     medium  # font size of the tick labels
#ytick.direction:     out     # direction: {in, out, inout}
#ytick.minor.visible: False   # visibility of minor ticks on y-axis
#ytick.major.left:    True    # draw y axis left major ticks
#ytick.major.right:   True    # draw y axis right major ticks
#ytick.minor.left:    True    # draw y axis left minor ticks
#ytick.minor.right:   True    # draw y axis right minor ticks
#ytick.minor.ndivs:   auto    # number of minor ticks between the major ticks on y-axis
#ytick.alignment:     center\_baseline  # alignment of yticks

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* GRIDS                                                                   \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#grid.color:     "#b0b0b0"  # grid color
#grid.linestyle: -          # solid
#grid.linewidth: 0.8        # in points
#grid.alpha:     1.0        # transparency, between 0.0 and 1.0

#grid.major.color:     None # If None defaults to grid.color
#grid.major.linestyle: None # If None defaults to grid.linestyle
#grid.major.linewidth: None # If None defaults to grid.linewidth
#grid.major.alpha:     None # If None defaults to grid.alpha

#grid.minor.color:     None # If None defaults to grid.color
#grid.minor.linestyle: None # If None defaults to grid.linestyle
#grid.minor.linewidth: None # If None defaults to grid.linewidth
#grid.minor.alpha:     None # If None defaults to grid.alpha

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* LEGEND                                                                  \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#legend.loc:           best
#legend.frameon:       True     # if True, draw the legend on a background patch
#legend.framealpha:    0.8      # legend patch transparency
#legend.facecolor:     inherit  # inherit from axes.facecolor; or color spec
#legend.edgecolor:     0.8      # background patch boundary color
#legend.linewidth:     None     # line width of the legend frame, None means inherit from patch.linewidth
#legend.fancybox:      True     # if True, use a rounded box for the
                                \# legend background, else a rectangle
#legend.shadow:        False    # if True, give background a shadow effect
#legend.numpoints:     1        # the number of marker points in the legend line
#legend.scatterpoints: 1        # number of scatter points
#legend.markerscale:   1.0      # the relative size of legend markers vs. original
#legend.fontsize:      medium
#legend.labelcolor:    None
#legend.title\_fontsize: None    # None sets to the same as the default axes.

\## Dimensions as fraction of font size:
#legend.borderpad:     0.4  # border whitespace
#legend.labelspacing:  0.5  # the vertical space between the legend entries
#legend.handlelength:  2.0  # the length of the legend lines
#legend.handleheight:  0.7  # the height of the legend handle
#legend.handletextpad: 0.8  # the space between the legend line and legend text
#legend.borderaxespad: 0.5  # the border between the axes and legend edge
#legend.columnspacing: 2.0  # column separation

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* FIGURE                                                                  \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## See https://matplotlib.org/stable/api/figure\_api.html#matplotlib.figure.Figure
#figure.titlesize:   large     # size of the figure title (\`\`Figure.suptitle()\`\`)
#figure.titleweight: normal    # weight of the figure title
#figure.labelsize:   large     # size of the figure label (\`\`Figure.sup\[x|y\]label()\`\`)
#figure.labelweight: normal    # weight of the figure label
#figure.figsize:     6.4, 4.8  # figure size in inches
#figure.dpi:         100       # figure dots per inch
#figure.facecolor:   white     # figure face color
#figure.edgecolor:   white     # figure edge color
#figure.frameon:     True      # enable figure frame
#figure.max\_open\_warning: 20   # The maximum number of figures to open through
                               \# the pyplot interface before emitting a warning.
                               \# If less than one this feature is disabled.
#figure.raise\_window : True    # Raise the GUI window to front when show() is called.
                               \# If set to False, we currently do not take any further
                               \# actions and whether the window appears on the front
                               \# may depend on the GUI framework and window manager.

\## The figure subplot parameters.  All dimensions are a fraction of the figure width and height.
#figure.subplot.left:   0.125  # the left side of the subplots of the figure
#figure.subplot.right:  0.9    # the right side of the subplots of the figure
#figure.subplot.bottom: 0.11   # the bottom of the subplots of the figure
#figure.subplot.top:    0.88   # the top of the subplots of the figure
#figure.subplot.wspace: 0.2    # the amount of width reserved for space between subplots,
                               \# expressed as a fraction of the average axis width
#figure.subplot.hspace: 0.2    # the amount of height reserved for space between subplots,
                               \# expressed as a fraction of the average axis height

\## Figure layout
#figure.autolayout: False  # When True, automatically adjust subplot
                           \# parameters to make the plot fit the figure
                           \# using \`tight\_layout\`
#figure.constrained\_layout.use: False  # When True, automatically make plot
                                       \# elements fit on the figure. (Not
                                       \# compatible with \`autolayout\`, above).
\## Padding (in inches) around axes; defaults to 3/72 inches, i.e. 3 points.
#figure.constrained\_layout.h\_pad:  0.04167
#figure.constrained\_layout.w\_pad:  0.04167
\## Spacing between subplots, relative to the subplot sizes.  Much smaller than for
\## tight\_layout (figure.subplot.hspace, figure.subplot.wspace) as constrained\_layout
\## already takes surrounding texts (titles, labels, # ticklabels) into account.
#figure.constrained\_layout.hspace: 0.02
#figure.constrained\_layout.wspace: 0.02

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* IMAGES                                                                  \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#image.aspect:          equal        # {equal, auto} or a number
#image.interpolation:   auto         # see help(imshow) for options
#image.interpolation\_stage: auto     # see help(imshow) for options
#image.cmap:            viridis      # A colormap name (plasma, magma, etc.)
#image.lut:             256          # the size of the colormap lookup table
#image.origin:          upper        # {lower, upper}
#image.resample:        True
#image.composite\_image: True  # When True, all the images on a set of axes are
                              \# combined into a single composite image before
                              \# saving a figure as a vector graphics file,
                              \# such as a PDF.

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* CONTOUR PLOTS                                                           \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#contour.negative\_linestyle: dashed  # string or on-off ink sequence
#contour.corner\_mask:        True    # {True, False}
#contour.linewidth:          None    # {float, None} Size of the contour line
                                     \# widths. If set to None, it falls back to
                                     \# \`line.linewidth\`.
#contour.algorithm:          mpl2014 # {mpl2005, mpl2014, serial, threaded}

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* ERRORBAR PLOTS                                                          \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#errorbar.capsize: 0  # length of end cap on error bars in pixels
#errorbar.capthick: None  # thickness of end cap on error bars in points
#errorbar.elinewidth: None  # line width of error bar lines in points

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* HISTOGRAM PLOTS                                                         \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#hist.bins: 10  # The default number of histogram bins or 'auto'.

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* SCATTER PLOTS                                                           \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#scatter.marker: o         # The default marker type for scatter plots.
#scatter.edgecolors: face  # The default edge colors for scatter plots.

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* AGG RENDERING                                                           \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## Warning: experimental, 2008/10/10
#agg.path.chunksize: 0  # 0 to disable; values in the range
                        \# 10000 to 100000 can improve speed slightly
                        \# and prevent an Agg rendering failure
                        \# when plotting very large data sets,
                        \# especially if they are very gappy.
                        \# It may cause minor artifacts, though.
                        \# A value of 20000 is probably a good
                        \# starting point.

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* PATHS                                                                   \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#path.simplify: True  # When True, simplify paths by removing "invisible"
                      \# points to reduce file size and increase rendering
                      \# speed
#path.simplify\_threshold: 0.111111111111  # The threshold of similarity below
                                          \# which vertices will be removed in
                                          \# the simplification process.
#path.snap: True  # When True, rectilinear axis-aligned paths will be snapped
                  \# to the nearest pixel when certain criteria are met.
                  \# When False, paths will never be snapped.
#path.sketch: None  # May be None, or a tuple of the form:
                    \#  path.sketch: (scale, length, randomness)
                    \# - \*scale\* is the amplitude of the wiggle
                    \#    perpendicular to the line (in pixels).
                    \# - \*length\* is the length of the wiggle along the
                    \#    line (in pixels).
                    \# - \*randomness\* is the factor by which the length is
                    \#    randomly scaled.
#path.effects:

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* SAVING FIGURES                                                          \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## The default savefig parameters can be different from the display parameters
\## e.g., you may want a higher resolution, or to make the figure
\## background white
#savefig.dpi:       figure      # figure dots per inch or 'figure'
#savefig.facecolor: auto        # figure face color when saving
#savefig.edgecolor: auto        # figure edge color when saving
#savefig.format:    png         # {png, ps, pdf, svg}
#savefig.bbox:      standard    # {tight, standard}
                                \# 'tight' is incompatible with generating frames
                                \# for animation
#savefig.pad\_inches:  0.1       # padding to be used, when bbox is set to 'tight'
#savefig.directory:   ~         # default directory in savefig dialog, gets updated after
                                \# interactive saves, unless set to the empty string (i.e.
                                \# the current directory); use '.' to start at the current
                                \# directory but update after interactive saves
#savefig.transparent: False     # whether figures are saved with a transparent
                                \# background by default
#savefig.orientation: portrait  # orientation of saved figure, for PostScript output only

\### macosx backend params
#macosx.window\_mode : system   # How to open new figures (system, tab, window)
                               \# system uses the MacOS system preferences

\### tk backend params
#tk.window\_focus:   False  # Maintain shell focus for TkAgg

\### ps backend params
#ps.papersize:      letter  # {figure, letter, legal, ledger, A0-A10, B0-B10}
#ps.useafm:         False   # use AFM fonts, results in small files
#ps.usedistiller:   False   # {ghostscript, xpdf, None}
                            \# Experimental: may produce smaller files.
                            \# xpdf intended for production of publication quality files,
                            \# but requires ghostscript, xpdf and ps2eps
#ps.distiller.res:  6000    # dpi
#ps.fonttype:       3       # Output Type 3 (Type3) or Type 42 (TrueType)

\### PDF backend params
#pdf.compression:    6  # integer from 0 to 9
                        \# 0 disables compression (good for debugging)
#pdf.fonttype:       3  # Output Type 3 (Type3) or Type 42 (TrueType)
#pdf.use14corefonts: False
#pdf.inheritcolor:   False

\### SVG backend params
#svg.image\_inline: True  # Write raster image data directly into the SVG file
#svg.fonttype: path      # How to handle SVG fonts:
                         \#     path: Embed characters as paths -- supported
                         \#           by most SVG renderers
                         \#     none: Assume fonts are installed on the
                         \#           machine where the SVG will be viewed.
#svg.hashsalt: None      # If not None, use this string as hash salt instead of uuid4
#svg.id: None            # If not None, use this string as the value for the \`id\`
                         \# attribute in the top <svg> tag

\### pgf parameter
\## See https://matplotlib.org/stable/tutorials/text/pgf.html for more information.
#pgf.rcfonts: True
#pgf.preamble:  # See text.latex.preamble for documentation
#pgf.texsystem: xelatex

\### docstring params
#docstring.hardcopy: False  # set this when you want to generate hardcopy docstring

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* INTERACTIVE KEYMAPS                                                     \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## Event keys to interact with figures/plots via keyboard.
\## See https://matplotlib.org/stable/users/explain/interactive.html for more
\## details on interactive navigation.  Customize these settings according to
\## your needs. Leave the field(s) empty if you don't need a key-map. (i.e.,
\## fullscreen : '')
#keymap.fullscreen: f, ctrl+f   # toggling
#keymap.home: h, r, home        # home or reset mnemonic
#keymap.back: left, c, backspace, MouseButton.BACK  # forward / backward keys
#keymap.forward: right, v, MouseButton.FORWARD      # for quick navigation
#keymap.pan: p                  # pan mnemonic
#keymap.zoom: o                 # zoom mnemonic
#keymap.save: s, ctrl+s         # saving current figure
#keymap.help: f1                # display help about active tools
#keymap.quit: ctrl+w, cmd+w, q  # close the current figure
#keymap.quit\_all:               # close all figures
#keymap.grid: g                 # switching on/off major grids in current axes
#keymap.grid\_minor: G           # switching on/off minor grids in current axes
#keymap.yscale: l               # toggle scaling of y-axes ('log'/'linear')
#keymap.xscale: k, L            # toggle scaling of x-axes ('log'/'linear')
#keymap.copy: ctrl+c, cmd+c     # copy figure to clipboard

\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\## \* ANIMATION                                                               \*
\## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#animation.html: none  # How to display the animation as HTML in
                       \# the IPython notebook:
                       \#     - 'html5' uses HTML5 video tag
                       \#     - 'jshtml' creates a JavaScript animation
#animation.writer:  ffmpeg        # MovieWriter 'backend' to use
#animation.codec:   h264          # Codec to use for writing movie
#animation.bitrate: -1            # Controls size/quality trade-off for movie.
                                  \# -1 implies let utility auto-determine
#animation.frame\_format: png      # Controls frame format used by temp files

\## Path to ffmpeg binary.  Unqualified paths are resolved by subprocess.Popen.
#animation.ffmpeg\_path:  ffmpeg
\## Additional arguments to pass to ffmpeg.
#animation.ffmpeg\_args:

\## Path to ImageMagick's convert binary.  Unqualified paths are resolved by
\## subprocess.Popen, except that on Windows, we look up an install of
\## ImageMagick in the registry (as convert is also the name of a system tool).
#animation.convert\_path: convert
\## Additional arguments to pass to convert.
#animation.convert\_args: -layers, OptimizePlus
#
#animation.embed\_limit:  20.0     # Limit, in MB, of size of base64 encoded
                                  \# animation in HTML (i.e. IPython notebook)

**Total running time of the script:** (0 minutes 2.717 seconds)

[`Download Jupyter notebook: customizing.ipynb`](https://matplotlib.org/stable/_downloads/fbba825e740063cf0f062ae506ac5fc3/customizing.ipynb)

[`Download Python source code: customizing.py`](https://matplotlib.org/stable/_downloads/94d8a348ee00a3f4afcdc2e530f954ce/customizing.py)

[`Download zipped: customizing.zip`](https://matplotlib.org/stable/_downloads/5e3e92c5a97db68275f27e57a4532110/customizing.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page
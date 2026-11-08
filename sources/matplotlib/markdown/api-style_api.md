[Skip to main content](https://matplotlib.org/stable/api/style_api.html#main-content)

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
    

`matplotlib.style`[#](https://matplotlib.org/stable/api/style_api.html#matplotlib-style "Link to this heading")

================================================================================================================

Styles are predefined sets of [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 that define the visual appearance of a plot.

[Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
 describes the mechanism and usage of styles.

The [Style sheets reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
 gives an overview of the builtin styles.

Core functions and attributes for the matplotlib style library:

`use`

Select style sheet to override the current matplotlib settings.

`context`

Context manager to use a style sheet temporarily.

`available`

List available style sheets. Underscore-prefixed names are considered private and not listed, though may still be accessed directly from `library`.

`library`

A dictionary of style names and matplotlib settings.

matplotlib.style.context(_style_, _after\_reset\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/style/__init__.py#L147-L188)
[#](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.context "Link to this definition")

Context manager for using style settings temporarily.

Parameters:

**style**str, dict, Path or list

A style specification. Valid options are:

str

*   One of the style names in [`style.available`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.available "matplotlib.style.available")
     (a builtin style or a style installed in the user library path).
    
*   A dotted name of the form "package.style\_name"; in that case, "package" should be an importable Python package name, e.g. at `/path/to/package/__init__.py`; the loaded style file is `/path/to/package/style_name.mplstyle`. (Style files in subpackages are likewise supported.)
    
*   The path or URL to a style file, which gets loaded by [`rc_params_from_file`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_params_from_file "matplotlib.rc_params_from_file")
    .
    

dict

A mapping of key/value pairs for [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
.

Path

The path to a style file, which gets loaded by [`rc_params_from_file`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_params_from_file "matplotlib.rc_params_from_file")
.

list

A list of style specifiers (str, Path or dict), which are applied from first to last in the list.

**after\_reset**bool

If True, apply style after resetting settings to their defaults; otherwise, apply style on top of the current settings.

matplotlib.style.reload\_library()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/style/__init__.py#L246-L250)
[#](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.reload_library "Link to this definition")

Reload the style library.

matplotlib.style.use(_style_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/style/__init__.py#L43-L144)
[#](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use "Link to this definition")

Use Matplotlib style settings from a style specification.

The style name of 'default' is reserved for reverting back to the default style settings.

Note

This updates the [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 with the settings from the style. [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 not defined in the style are kept.

Parameters:

**style**str, dict, Path or list

A style specification. Valid options are:

str

*   One of the style names in [`style.available`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.available "matplotlib.style.available")
     (a builtin style or a style installed in the user library path).
    
*   A dotted name of the form "package.style\_name"; in that case, "package" should be an importable Python package name, e.g. at `/path/to/package/__init__.py`; the loaded style file is `/path/to/package/style_name.mplstyle`. (Style files in subpackages are likewise supported.)
    
*   The path or URL to a style file, which gets loaded by [`rc_params_from_file`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_params_from_file "matplotlib.rc_params_from_file")
    .
    

dict

A mapping of key/value pairs for [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
.

Path

The path to a style file, which gets loaded by [`rc_params_from_file`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_params_from_file "matplotlib.rc_params_from_file")
.

list

A list of style specifiers (str, Path or dict), which are applied from first to last in the list.

Notes

The following [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 are not related to style and will be ignored if found in a style specification:

*   backend
    
*   backend\_fallback
    
*   date.epoch
    
*   docstring.hardcopy
    
*   figure.max\_open\_warning
    
*   figure.raise\_window
    
*   interactive
    
*   savefig.directory
    
*   timezone
    
*   tk.window\_focus
    
*   toolbar
    
*   webagg.address
    
*   webagg.open\_in\_browser
    
*   webagg.port
    
*   webagg.port\_retries
    

matplotlib.style.library[#](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.library "Link to this definition")

A dict mapping from style name to [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 defining that style.

This is meant to be read-only. Use [`reload_library`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.reload_library "matplotlib.style.reload_library")
 to update.

matplotlib.style.available[#](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.available "Link to this definition")

List of the names of the available styles.

This is meant to be read-only. Use [`reload_library`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.reload_library "matplotlib.style.reload_library")
 to update.

On this page
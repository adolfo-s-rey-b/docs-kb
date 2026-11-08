[Skip to main content](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#main-content)

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
    

`matplotlib.sphinxext.plot_directive`[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#module-matplotlib.sphinxext.plot_directive "Link to this heading")

================================================================================================================================================================================

A directive for including a Matplotlib plot in a Sphinx document[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#a-directive-for-including-a-matplotlib-plot-in-a-sphinx-document "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is a Sphinx extension providing a reStructuredText directive `.. plot::` for including a plot in a Sphinx document.

In HTML output, `.. plot::` will include a .png file with a link to a high-res .png and .pdf. In LaTeX output, it will include a .pdf.

The plot content may be defined in one of three ways:

1.  **A path to a source file** as the argument to the directive:
    
    .. plot:: path/to/plot.py
    
    When a path to a source file is given, the content of the directive may optionally contain a caption for the plot:
    
    .. plot:: path/to/plot.py
    
       The plot caption.
    
    Additionally, one may specify the name of a function to call (with no arguments) immediately after importing the module:
    
    .. plot:: path/to/plot.py plot\_function1
    
2.  Included as **inline content** to the directive:
    
    .. plot::
    
       import matplotlib.pyplot as plt
       plt.plot(\[1, 2, 3\], \[4, 5, 6\])
       plt.title("A plotting example")
    
3.  Using **doctest** syntax:
    
    .. plot::
    
       A plotting example:
       \>>> import matplotlib.pyplot as plt
       \>>> plt.plot(\[1, 2, 3\], \[4, 5, 6\])
    

### Options[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#options "Link to this heading")

The `.. plot::` directive supports the following options:

`:filename-prefix:`str

The base name (without the extension) of the outputted image and script files. The default is to use the same name as the input script, or the name of the RST document if no script is provided. The filename-prefix for each plot directive must be unique.

`:format:`{'python', 'doctest'}

The format of the input. If unset, the format is auto-detected.

`:include-source:`bool

Whether to display the source code. The default can be changed using the `plot_include_source` variable in `conf.py` (which itself defaults to False).

`:show-source-link:`bool

Whether to show a link to the source in HTML. The default can be changed using the `plot_html_show_source_link` variable in `conf.py` (which itself defaults to True).

`:context:`bool or str

If provided, the code will be run in the context of all previous plot directives for which the `:context:` option was specified. This only applies to inline code plot directives, not those run from files. If the `:context: reset` option is specified, the context is reset for this and future plots, and previous figures are closed prior to running the code. `:context: close-figs` keeps the context but closes previous figures before running the code.

`:nofigs:`bool

If specified, the code block will be run, but no figures will be inserted. This is usually useful with the `:context:` option.

`:caption:`str

If specified, the option's argument will be used as a caption for the figure. This overwrites the caption given in the content, when the plot is generated from a file.

`:code-caption:`str

If specified, the option's argument will be used as a caption for the code block (when `:include-source:` is used). This is added as the `:caption:` option to the `.. code-block::` directive.

Additionally, this directive supports all the options of the [image directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#image)
, except for `:target:` (since plot will add its own target). These include `:alt:`, `:height:`, `:width:`, `:scale:`, `:align:` and `:class:`.

### Configuration options[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#configuration-options "Link to this heading")

The plot directive has the following configuration options:

plot\_include\_source

Default value for the include-source option (default: False).

plot\_html\_show\_source\_link

Whether to show a link to the source in HTML (default: True).

plot\_pre\_code

Code that should be executed before each plot. If None (the default), it will default to a string containing:

import numpy as np
from matplotlib import pyplot as plt

plot\_basedir

Base directory, to which `plot::` file names are relative to. If None or empty (the default), file names are relative to the directory where the file containing the directive is.

plot\_formats

File formats to generate (default: \['png', 'hires.png', 'pdf'\]). List of tuples or strings:

\[(suffix, dpi), suffix, ...\]

that determine the file format and the DPI. For entries whose DPI was omitted, sensible defaults are chosen. When passing from the command line through sphinx\_build the list should be passed as suffix:dpi,suffix:dpi, ...

plot\_html\_show\_formats

Whether to show links to the files in HTML (default: True).

plot\_rcparams

A dictionary containing any non-standard rcParams that should be applied before each plot (default: {}).

plot\_apply\_rcparams

By default, rcParams are applied when `:context:` option is not used in a plot directive. If set, this configuration option overrides this behavior and applies rcParams before each plot.

plot\_working\_directory

By default, the working directory will be changed to the directory of the example, so the code can get at its data files, if any. Also its path will be added to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.14)")
 so it can import any helper modules sitting beside it. This configuration option can be used to specify a central directory (also added to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.14)")
) where data files and helper modules for all code are located.

plot\_template

Provide a customized template for preparing restructured text.

plot\_srcset

Allow the srcset image option for responsive image resolutions. List of strings with the multiplicative factors followed by an "x". e.g. \["2.0x", "1.5x"\]. "2.0x" will create a png with the default "png" resolution from plot\_formats, multiplied by 2. If plot\_srcset is specified, the plot directive uses the [matplotlib.sphinxext.figmpl\_directive](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html)
 (instead of the usual figure directive) in the intermediary rst file that is generated. The plot\_srcset option is incompatible with _singlehtml_ builds, and an error will be raised.

### Notes on how it works[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#notes-on-how-it-works "Link to this heading")

The plot directive runs the code it is given, either in the source file or the code under the directive. The figure created (if any) is saved in the sphinx build directory under a subdirectory named `plot_directive`. It then creates an intermediate rst file that calls a `.. figure:` directive (or `.. figmpl::` directive if `plot_srcset` is being used) and has links to the `*.png` files in the `plot_directive` directory. These translations can be customized by changing the _plot\_template_. See the source of [matplotlib.sphinxext.plot\_directive](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#)
 for the templates defined in _TEMPLATE_ and _TEMPLATE\_SRCSET_.

class matplotlib.sphinxext.plot\_directive.PlotDirective(_name_, _arguments_, _options_, _content_, _lineno_, _content\_offset_, _block\_text_, _state_, _state\_machine_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/plot_directive.py#L268-L298)
[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.PlotDirective "Link to this definition")

The `.. plot::` directive, as documented in the module's docstring.

final\_argument\_whitespace \= False[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.PlotDirective.final_argument_whitespace "Link to this definition")

May the final argument contain whitespace?

has\_content \= True[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.PlotDirective.has_content "Link to this definition")

May the directive have content?

option\_spec \= {'align': <function Image.align>, 'alt': <function unchanged>, 'caption': <function unchanged>, 'class': <function class\_option>, 'code-caption': <function unchanged>, 'context': <function \_option\_context>, 'filename-prefix': <function unchanged>, 'format': <function \_option\_format>, 'height': <function length\_or\_unitless>, 'include-source': <function \_option\_boolean>, 'nofigs': <function flag>, 'scale': <function nonnegative\_int>, 'show-source-link': <function \_option\_boolean>, 'width': <function length\_or\_percentage\_or\_unitless>}[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.PlotDirective.option_spec "Link to this definition")

Mapping of option names to validator functions.

optional\_arguments \= 2[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.PlotDirective.optional_arguments "Link to this definition")

Number of optional arguments after the required arguments.

required\_arguments \= 0[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.PlotDirective.required_arguments "Link to this definition")

Number of required directive arguments.

run()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/plot_directive.py#L292-L298)
[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.PlotDirective.run "Link to this definition")

Run the plot directive.

exception matplotlib.sphinxext.plot\_directive.PlotError[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/plot_directive.py#L548-L549)
[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.PlotError "Link to this definition")

matplotlib.sphinxext.plot\_directive.mark\_plot\_labels(_app_, _document_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/plot_directive.py#L238-L265)
[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.mark_plot_labels "Link to this definition")

To make plots referenceable, we need to move the reference from the "htmlonly" (or "latexonly") node to the actual figure node itself.

matplotlib.sphinxext.plot\_directive.out\_of\_date(_original_, _derived_, _includes\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/plot_directive.py#L526-L545)
[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.out_of_date "Link to this definition")

Return whether _derived_ is out-of-date relative to _original_ or any of the RST files included in it using the RST include directive (_includes_). _derived_ and _original_ are full paths, and _includes_ is optionally a list of full paths which may have been included in the _original_.

matplotlib.sphinxext.plot\_directive.render\_figures(_code_, _code\_path_, _output\_dir_, _output\_base_, _context_, _function\_name_, _config_, _context\_reset\=False_, _close\_figs\=False_, _code\_includes\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/plot_directive.py#L664-L781)
[#](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#matplotlib.sphinxext.plot_directive.render_figures "Link to this definition")

Run a pyplot script and save the images in _output\_dir_.

Save the images under _output\_dir_ with file names derived from _output\_base_

On this page
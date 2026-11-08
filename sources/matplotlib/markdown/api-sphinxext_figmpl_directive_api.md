[Skip to main content](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#main-content)

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
    

`matplotlib.sphinxext.figmpl_directive`[#](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#module-matplotlib.sphinxext.figmpl_directive "Link to this heading")

======================================================================================================================================================================================

Add a `figure-mpl` directive that is a responsive version of `figure`.

This implementation is very similar to `.. figure::`, except it also allows a `srcset=` argument to be passed to the image tag, hence allowing responsive resolution images.

There is no particular reason this could not be used standalone, but is meant to be used with [matplotlib.sphinxext.plot\_directive](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html)
.

Note that the directory organization is a bit different than `.. figure::`. See the _FigureMpl_ documentation below.

class matplotlib.sphinxext.figmpl\_directive.FigureMpl(_name_, _arguments_, _options_, _content_, _lineno_, _content\_offset_, _block\_text_, _state_, _state\_machine_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/figmpl_directive.py#L32-L110)
[#](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#matplotlib.sphinxext.figmpl_directive.FigureMpl "Link to this definition")

Implements a directive to allow an optional hidpi image.

Meant to be used with the _plot\_srcset_ configuration option in conf.py, and gets set in the TEMPLATE of plot\_directive.py

e.g.:

.. figure\-mpl:: plot\_directive/some\_plots\-1.png
    :alt: bar
    :srcset: plot\_directive/some\_plots\-1.png,
             plot\_directive/some\_plots\-1.2x.png 2.00x
    :class: plot\-directive

The resulting html (at `some_plots.html`) is:

<img src\="sphx\_glr\_bar\_001\_hidpi.png"
    srcset\="\_images/some\_plot-1.png,
            \_images/some\_plots\-1.2x.png 2.00x",
    alt\="bar"
    class\="plot\_directive" />

Note that the handling of subdirectories is different than that used by the sphinx figure directive:

.. figure\-mpl:: plot\_directive/nestedpage/index\-1.png
    :alt: bar
    :srcset: plot\_directive/nestedpage/index\-1.png
             plot\_directive/nestedpage/index\-1.2x.png 2.00x
    :class: plot\_directive

The resulting html (at `nestedpage/index.html`):

<img src\="../\_images/nestedpage-index-1.png"
    srcset\="../\_images/nestedpage-index-1.png,
            ../\_images/\_images/nestedpage\-index\-1.2x.png 2.00x",
    alt\="bar"
    class\="sphx-glr-single-img" />

where the subdirectory is included in the image name for uniqueness.

final\_argument\_whitespace \= False[#](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#matplotlib.sphinxext.figmpl_directive.FigureMpl.final_argument_whitespace "Link to this definition")

May the final argument contain whitespace?

has\_content \= False[#](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#matplotlib.sphinxext.figmpl_directive.FigureMpl.has_content "Link to this definition")

May the directive have content?

option\_spec \= {'align': <function Image.align>, 'alt': <function unchanged>, 'caption': <function unchanged>, 'class': <function class\_option>, 'height': <function length\_or\_unitless>, 'scale': <function nonnegative\_int>, 'srcset': <function unchanged>, 'width': <function length\_or\_percentage\_or\_unitless>}[#](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#matplotlib.sphinxext.figmpl_directive.FigureMpl.option_spec "Link to this definition")

Mapping of option names to validator functions.

optional\_arguments \= 2[#](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#matplotlib.sphinxext.figmpl_directive.FigureMpl.optional_arguments "Link to this definition")

Number of optional arguments after the required arguments.

required\_arguments \= 1[#](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#matplotlib.sphinxext.figmpl_directive.FigureMpl.required_arguments "Link to this definition")

Number of required directive arguments.

class matplotlib.sphinxext.figmpl\_directive.figmplnode(_rawsource\=''_, _\*children_, _\*\*attributes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/figmpl_directive.py#L28-L29)
[#](https://matplotlib.org/stable/api/sphinxext_figmpl_directive_api.html#matplotlib.sphinxext.figmpl_directive.figmplnode "Link to this definition")

On this page
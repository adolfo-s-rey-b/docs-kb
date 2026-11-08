[Skip to main content](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#main-content)

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
    

`matplotlib.sphinxext.mathmpl`[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#module-matplotlib.sphinxext.mathmpl "Link to this heading")

===========================================================================================================================================================

A role and directive to display mathtext in Sphinx[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#a-role-and-directive-to-display-mathtext-in-sphinx "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `mathmpl` Sphinx extension creates a mathtext image in Matplotlib and shows it in html output. Thus, it is a true and faithful representation of what you will see if you pass a given LaTeX string to Matplotlib (see [Writing mathematical expressions](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext)
).

Warning

In most cases, you will likely want to use one of [Sphinx's builtin Math extensions](https://www.sphinx-doc.org/en/master/usage/extensions/math.html)
 instead of this one. The builtin Sphinx math directive uses MathJax to render mathematical expressions, and addresses accessibility concerns that `mathmpl` doesn't address.

Mathtext may be included in two ways:

1.  Inline, using the role:
    
    This text uses inline math: :mathmpl:\`\\alpha > \\beta\`.
    
    which produces:
    
    > This text uses inline math: ![](https://matplotlib.org/stable/_images/mathmpl/math-a6af197251-2x.png).
    
2.  Standalone, using the directive:
    
    Here is some standalone math:
    
    .. mathmpl::
    
        \\alpha \> \\beta
    
    which produces:
    
    > Here is some standalone math:
    > 
    > ![](https://matplotlib.org/stable/_images/mathmpl/math-a6af197251-2x.png)
    

### Options[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#options "Link to this heading")

The `mathmpl` role and directive both support the following options:

fontsetstr, default: 'cm'

The font set to use when displaying math. See `[rcParams["mathtext.fontset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.fontset#rcparam-mathtext-fontset) ` (default: `'dejavusans'`).

fontsizefloat

The font size, in points. Defaults to the value from the extension configuration option defined below.

### Configuration options[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#configuration-options "Link to this heading")

The mathtext extension has the following configuration options:

mathmpl\_fontsizefloat, default: 10.0

Default font size, in points.

mathmpl\_srcsetlist of str, default: \[\]

Additional image sizes to generate when embedding in HTML, to support [responsive resolution images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)
. The list should contain additional x-descriptors (`'1.5x'`, `'2x'`, etc.) to generate (1x is the default and always included.)

class matplotlib.sphinxext.mathmpl.MathDirective(_name_, _arguments_, _options_, _content_, _lineno_, _content\_offset_, _block\_text_, _state_, _state\_machine_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/mathmpl.py#L109-L127)
[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#matplotlib.sphinxext.mathmpl.MathDirective "Link to this definition")

The `.. mathmpl::` directive, as documented in the module's docstring.

final\_argument\_whitespace \= False[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#matplotlib.sphinxext.mathmpl.MathDirective.final_argument_whitespace "Link to this definition")

May the final argument contain whitespace?

has\_content \= True[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#matplotlib.sphinxext.mathmpl.MathDirective.has_content "Link to this definition")

May the directive have content?

option\_spec \= {'fontset': <function fontset\_choice>, 'fontsize': <function \_make\_type\_validator.<locals>.validate\_float\_or\_None>}[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#matplotlib.sphinxext.mathmpl.MathDirective.option_spec "Link to this definition")

Mapping of option names to validator functions.

optional\_arguments \= 0[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#matplotlib.sphinxext.mathmpl.MathDirective.optional_arguments "Link to this definition")

Number of optional arguments after the required arguments.

required\_arguments \= 0[#](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#matplotlib.sphinxext.mathmpl.MathDirective.required_arguments "Link to this definition")

Number of required directive arguments.

On this page
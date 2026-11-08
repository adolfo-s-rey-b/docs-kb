[Skip to main content](https://matplotlib.org/stable/api/sphinxext_roles.html#main-content)

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
    

`matplotlib.sphinxext.roles`[#](https://matplotlib.org/stable/api/sphinxext_roles.html#module-matplotlib.sphinxext.roles "Link to this heading")

=================================================================================================================================================

Custom roles for the Matplotlib documentation.

Warning

These roles are considered semi-public. They are only intended to be used in the Matplotlib documentation.

However, it can happen that downstream packages end up pulling these roles into their documentation, which will result in documentation build errors. The following describes the exact mechanism and how to fix the errors.

There are two ways, Matplotlib docstrings can end up in downstream documentation. You have to subclass a Matplotlib class and either use the `:inherited-members:` option in your autodoc configuration, or you have to override a method without specifying a new docstring; the new method will inherit the original docstring and still render in your autodoc. If the docstring contains one of the custom sphinx roles, you'll see one of the following error messages:

Unknown interpreted text role "mpltype".
Unknown interpreted text role "rc".

To fix this, you can add this module as extension to your sphinx `conf.py`:

extensions \= \[\
    'matplotlib.sphinxext.roles',\
    \# Other extensions.\
\]

Warning

Direct use of these roles in other packages is not officially supported. We reserve the right to modify or remove these roles without prior notification.

matplotlib.sphinxext.roles.\_mpltype\_role(_name_, _rawtext_, _text_, _lineno_, _inliner_, _options\=None_, _content\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/roles.py#L129-L152)
[#](https://matplotlib.org/stable/api/sphinxext_roles.html#matplotlib.sphinxext.roles._mpltype_role "Link to this definition")

Sphinx role `:mpltype:` for custom matplotlib types.

In Matplotlib, there are a number of type-like concepts that do not have a direct type representation; example: color. This role allows to properly highlight them in the docs and link to their definition.

Currently supported values:

*   `` :mpltype:`color` `` will render as: [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
    

matplotlib.sphinxext.roles.\_rcparam\_role(_name_, _rawtext_, _text_, _lineno_, _inliner_, _options\=None_, _content\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sphinxext/roles.py#L97-L126)
[#](https://matplotlib.org/stable/api/sphinxext_roles.html#matplotlib.sphinxext.roles._rcparam_role "Link to this definition")

Sphinx role `:rc:` to highlight and link `rcParams` entries.

Usage: Give the desired `rcParams` key as parameter.

`` :rc:`figure.dpi` `` will render as: `[rcParams["figure.dpi"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.dpi#rcparam-figure-dpi) ` (default: `100.0`)

On this page
[Skip to main content](https://matplotlib.org/stable/api/_docstring_api.html#main-content)

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
    

`matplotlib._docstring`[#](https://matplotlib.org/stable/api/_docstring_api.html#module-matplotlib._docstring "Link to this heading")

======================================================================================================================================

class matplotlib.\_docstring.Substitution(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_docstring.py#L34-L69)
[#](https://matplotlib.org/stable/api/_docstring_api.html#matplotlib._docstring.Substitution "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A decorator that performs %-substitution on an object's docstring.

This decorator should be robust even if `obj.__doc__` is None (for example, if -OO was passed to the interpreter).

Usage: construct a docstring.Substitution with a sequence or dictionary suitable for performing substitution; then decorate a suitable function with the constructed object, e.g.:

sub\_author\_name \= Substitution(author\='Jason')

@sub\_author\_name
def some\_function(x):
    "%(author)s wrote this function"

\# note that some\_function.\_\_doc\_\_ is now "Jason wrote this function"

One can also use positional arguments:

sub\_first\_last\_names \= Substitution('Edgar Allen', 'Poe')

@sub\_first\_last\_names
def some\_function(x):
    "%s %s wrote the Raven"

matplotlib.\_docstring.copy(_source_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_docstring.py#L130-L136)
[#](https://matplotlib.org/stable/api/_docstring_api.html#matplotlib._docstring.copy "Link to this definition")

Copy a docstring from another source function (if present).

matplotlib.\_docstring.kwarg\_doc(_text_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_docstring.py#L6-L31)
[#](https://matplotlib.org/stable/api/_docstring_api.html#matplotlib._docstring.kwarg_doc "Link to this definition")

Decorator for defining the kwdoc documentation of artist properties.

This decorator can be applied to artist property setter methods. The given text is stored in a private attribute `_kwarg_doc` on the method. It is used to overwrite auto-generated documentation in the _kwdoc list_ for artists. The kwdoc list is used to document `**kwargs` when they are properties of an artist. See e.g. the `**kwargs` section in [`Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
.

The text should contain the supported types, as well as the default value if applicable, e.g.:

> @\_docstring.kwarg\_doc("bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`)") def set\_usetex(self, usetex):

See also

[`matplotlib.artist.kwdoc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.kwdoc.html#matplotlib.artist.kwdoc "matplotlib.artist.kwdoc")

On this page
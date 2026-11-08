[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#main-content)

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
    

matplotlib.animation.MovieWriterRegistry[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib-animation-moviewriterregistry "Link to this heading")

=====================================================================================================================================================================================================

class matplotlib.animation.MovieWriterRegistry[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L69-L123)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry "Link to this definition")

Registry of available writer classes by human readable name.

\_\_init\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L72-L73)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry.__init__ "matplotlib.animation.MovieWriterRegistry.__init__")<br>() |     |
| [`is_available`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry.is_available "matplotlib.animation.MovieWriterRegistry.is_available")<br>(name) | Check if given writer is available by name. |
| [`list`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry.list "matplotlib.animation.MovieWriterRegistry.list")<br>() | Get a list of available MovieWriters. |
| [`register`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry.register "matplotlib.animation.MovieWriterRegistry.register")<br>(name) | Decorator for registering a class under a name. |

is\_available(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L90-L106)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry.is_available "Link to this definition")

Check if given writer is available by name.

Parameters:

**name**str

Returns:

bool

list()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L114-L116)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry.list "Link to this definition")

Get a list of available MovieWriters.

register(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L75-L88)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry.register "Link to this definition")

Decorator for registering a class under a name.

Example use:

@registry.register(name)
class Foo:
    pass

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.findobj.html#main-content)

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
    

matplotlib.pyplot.findobj[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.findobj.html#matplotlib-pyplot-findobj "Link to this heading")

========================================================================================================================================================

matplotlib.pyplot.findobj(_o\=None_, _match\=None_, _include\_self\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L366-L374)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.findobj.html#matplotlib.pyplot.findobj "Link to this definition")

Find artist objects.

Recursively find all [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 instances contained in the artist.

Parameters:

**match**

A filter criterion for the matches. This can be

*   _None_: Return all objects contained in artist.
    
*   A function with signature `def match(artist: Artist) -> bool`. The result will only contain artists for which the function returns _True_.
    
*   A class instance: e.g., [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
    . The result will only contain artists of this class or its subclasses (`isinstance` check).
    

**include\_self**bool

Include _self_ in the list to be checked for a match.

Returns:

list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

On this page
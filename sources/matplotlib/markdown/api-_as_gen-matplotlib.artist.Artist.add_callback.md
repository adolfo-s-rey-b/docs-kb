[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.add_callback.html#main-content)

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
    

matplotlib.artist.Artist.add\_callback[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.add_callback.html#matplotlib-artist-artist-add-callback "Link to this heading")

=============================================================================================================================================================================================

Artist.add\_callback(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L404-L431)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.add_callback.html#matplotlib.artist.Artist.add_callback "Link to this definition")

Add a callback function that will be called whenever one of the [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
's properties changes.

Parameters:

**func**callable

The callback function. It must have the signature:

def func(artist: Artist) \-> Any

where _artist_ is the calling [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
. Return values may exist but are ignored.

Returns:

int

The observer id associated with the callback. This id can be used for removing the callback with [`remove_callback`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove_callback.html#matplotlib.artist.Artist.remove_callback "matplotlib.artist.Artist.remove_callback")
 later.

See also

[`remove_callback`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove_callback.html#matplotlib.artist.Artist.remove_callback "matplotlib.artist.Artist.remove_callback")

On this page
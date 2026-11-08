[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.kwdoc.html#main-content)

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
    

matplotlib.artist.kwdoc[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.kwdoc.html#matplotlib-artist-kwdoc "Link to this heading")

==================================================================================================================================================

matplotlib.artist.kwdoc(_artist_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1915-L1934)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.kwdoc.html#matplotlib.artist.kwdoc "Link to this definition")

Inspect an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 class (using [`ArtistInspector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector "matplotlib.artist.ArtistInspector")
) and return information about its settable properties and their current values.

Parameters:

**artist**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or an iterable of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s

Returns:

str

The settable properties of _artist_, as plain text if `[rcParams["docstring.hardcopy"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=docstring.hardcopy#rcparam-docstring-hardcopy) ` (default: `False`) is False and as an rst table (intended for use in Sphinx) if it is True.

On this page
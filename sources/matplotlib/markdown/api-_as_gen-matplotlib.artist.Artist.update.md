[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#main-content)

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
    

matplotlib.artist.Artist.update[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib-artist-artist-update "Link to this heading")

==========================================================================================================================================================================

Artist.update(_props_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1280-L1304)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "Link to this definition")

\[_Discouraged_\] Update this artist's properties from the dictionary _props_.

Discouraged

This method exists for historic reasons. Please use [`Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
 instead. `artist.update(props)` is nowadays almost identical to `artist.set(**props)` with the only difference that `set` will additionally check that a property is not specified multiple times through aliases.

Parameters:

**props**dict

Dictionary of properties (keys) and their new values.

Returns:

list

A list of return values from the configured setters.

On this page
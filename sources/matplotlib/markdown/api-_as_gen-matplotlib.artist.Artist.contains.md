[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#main-content)

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
    

matplotlib.artist.Artist.contains[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib-artist-artist-contains "Link to this heading")

================================================================================================================================================================================

Artist.contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L508-L526)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib.artist.Artist.contains "Link to this definition")

Test whether the artist contains the mouse event.

Parameters:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

Returns:

**contains**bool

Whether any values are within the radius.

**details**dict

An artist-specific dictionary of details of the event context, such as which points are contained in the pick radius. See the individual Artist subclasses for details.

Examples using `matplotlib.artist.Artist.contains`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#examples-using-matplotlib-artist-artist-contains "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_looking_glass_thumb.png)

[Looking glass](https://matplotlib.org/stable/gallery/event_handling/looking_glass.html)

Looking glass

On this page
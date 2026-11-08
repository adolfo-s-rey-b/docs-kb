[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_cursor_data.html#main-content)

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
    

matplotlib.artist.Artist.get\_cursor\_data[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_cursor_data.html#matplotlib-artist-artist-get-cursor-data "Link to this heading")

=======================================================================================================================================================================================================

Artist.get\_cursor\_data(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1382-L1411)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_cursor_data.html#matplotlib.artist.Artist.get_cursor_data "Link to this definition")

Return the cursor data for a given event.

Note

This method is intended to be overridden by artist subclasses. As an end-user of Matplotlib you will most likely not call this method yourself.

Cursor data can be used by Artists to provide additional context information for a given event. The default implementation just returns _None_.

Subclasses can override the method and return arbitrary data. However, when doing so, they must ensure that [`format_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.format_cursor_data.html#matplotlib.artist.Artist.format_cursor_data "matplotlib.artist.Artist.format_cursor_data")
 can convert the data to a string representation.

The only current use case is displaying the z-value of an [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 in the status bar of a plot window, while moving the mouse.

Parameters:

**event**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

See also

[`format_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.format_cursor_data.html#matplotlib.artist.Artist.format_cursor_data "matplotlib.artist.Artist.format_cursor_data")

On this page
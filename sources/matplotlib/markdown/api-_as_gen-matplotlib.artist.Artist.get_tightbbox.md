[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#main-content)

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
    

matplotlib.artist.Artist.get\_tightbbox[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#matplotlib-artist-artist-get-tightbbox "Link to this heading")

================================================================================================================================================================================================

Artist.get\_tightbbox(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L373-L402)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#matplotlib.artist.Artist.get_tightbbox "Link to this definition")

Get the artist's bounding box in display space, taking clipping into account.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
, optional

Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).

Returns:

[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 or None

The enclosing bounding box (in figure pixel coordinates), or None if clipping results in no intersection.

See also

[`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")

Get the artist bounding box, ignoring clipping.

On this page
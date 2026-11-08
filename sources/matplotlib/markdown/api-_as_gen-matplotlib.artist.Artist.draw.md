[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#main-content)

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
    

matplotlib.artist.Artist.draw[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#matplotlib-artist-artist-draw "Link to this heading")

====================================================================================================================================================================

Artist.draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1044-L1061)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#matplotlib.artist.Artist.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

Examples using `matplotlib.artist.Artist.draw`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#examples-using-matplotlib-artist-artist-draw "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_line_with_text_thumb.png)

[Artist within an artist](https://matplotlib.org/stable/gallery/text_labels_and_annotations/line_with_text.html)

Artist within an artist

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.allow_rasterization.html#main-content)

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
    

matplotlib.artist.allow\_rasterization[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.allow_rasterization.html#matplotlib-artist-allow-rasterization "Link to this heading")

=============================================================================================================================================================================================

matplotlib.artist.allow\_rasterization(_draw_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L44-L84)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.allow_rasterization.html#matplotlib.artist.allow_rasterization "Link to this definition")

Decorator for Artist.draw method. Provides routines that run before and after the draw call. The before and after functions are useful for changing artist-dependent renderer attributes or making other setup function calls, such as starting and flushing a mixed-mode renderer.

On this page
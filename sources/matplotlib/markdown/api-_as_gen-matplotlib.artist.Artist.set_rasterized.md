[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#main-content)

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
    

matplotlib.artist.Artist.set\_rasterized[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib-artist-artist-set-rasterized "Link to this heading")

===================================================================================================================================================================================================

Artist.set\_rasterized(_rasterized_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L999-L1020)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "Link to this definition")

Force rasterized (bitmap) drawing for vector graphics output.

Rasterized drawing is not supported by all artists. If you try to enable this on an artist that does not support it, the command has no effect and a warning will be issued.

This setting is ignored for pixel-based output.

See also [Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)
.

Parameters:

**rasterized**bool

Examples using `matplotlib.artist.Artist.set_rasterized`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#examples-using-matplotlib-artist-artist-set-rasterized "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_rasterization_demo_thumb.png)

[Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)

Rasterization for vector graphics

On this page
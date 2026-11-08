[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.bbox_artist.html#main-content)

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
    

matplotlib.patches.bbox\_artist[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.bbox_artist.html#matplotlib-patches-bbox-artist "Link to this heading")

========================================================================================================================================================================

matplotlib.patches.bbox\_artist(_artist_, _renderer_, _props\=None_, _fill\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2359-L2379)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.bbox_artist.html#matplotlib.patches.bbox_artist "Link to this definition")

A debug function to draw a rectangle around the bounding box returned by an artist's [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")
 to test whether the artist is returning the correct bbox.

_props_ is a dict of rectangle props with the additional property 'pad' that sets the padding around the bbox in points.

On this page
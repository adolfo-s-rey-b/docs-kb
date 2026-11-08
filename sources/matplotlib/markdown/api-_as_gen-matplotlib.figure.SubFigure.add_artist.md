[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_artist.html#main-content)

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
    

matplotlib.figure.SubFigure.add\_artist[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_artist.html#matplotlib-figure-subfigure-add-artist "Link to this heading")

================================================================================================================================================================================================

SubFigure.add\_artist(_artist_, _clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L503-L536)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_artist.html#matplotlib.figure.SubFigure.add_artist "Link to this definition")

Add an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 to the figure.

Usually artists are added to [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 objects using [`Axes.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
; this method can be used in the rare cases where one needs to add artists directly to the figure instead.

Parameters:

**artist**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The artist to add to the figure. If the added artist has no transform previously set, its transform will be set to `figure.transSubfigure`.

**clip**bool, default: False

Whether the added artist should be clipped by the figure patch.

Returns:

[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The added artist.

On this page
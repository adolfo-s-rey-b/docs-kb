[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#main-content)

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
    

matplotlib.artist.Artist.set\_animated[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib-artist-artist-set-animated "Link to this heading")

=============================================================================================================================================================================================

Artist.set\_animated(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1118-L1136)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "Link to this definition")

Set whether the artist is intended to be used in an animation.

If True, the artist is excluded from regular drawing of the figure. You have to call [`Figure.draw_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_artist.html#matplotlib.figure.Figure.draw_artist "matplotlib.figure.Figure.draw_artist")
 / [`Axes.draw_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw_artist.html#matplotlib.axes.Axes.draw_artist "matplotlib.axes.Axes.draw_artist")
 explicitly on the artist. This approach is used to speed up animations using blitting.

See also [`matplotlib.animation`](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "matplotlib.animation")
 and [Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html#blitting)
.

Parameters:

**b**bool

On this page
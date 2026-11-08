[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_tightbbox.html#main-content)

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
    

matplotlib.figure.Figure.get\_tightbbox[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_tightbbox.html#matplotlib-figure-figure-get-tightbbox "Link to this heading")

================================================================================================================================================================================================

Figure.get\_tightbbox(_renderer\=None_, _\*_, _bbox\_extra\_artists\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1808-L1879)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_tightbbox.html#matplotlib.figure.Figure.get_tightbbox "Link to this definition")

Return a (tight) bounding box of the figure _in inches_.

Note that [`FigureBase`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase "matplotlib.figure.FigureBase")
 differs from all other artists, which return their [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 in pixels.

Artists that have `artist.set_in_layout(False)` are not included in the bbox.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass

Renderer that will be used to draw the figures (i.e. `fig.canvas.get_renderer()`)

**bbox\_extra\_artists**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or `None`

List of artists to include in the tight bounding box. If `None` (default), then all artist children of each Axes are included in the tight bounding box.

Returns:

[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

containing the bounding box (in figure inches).

On this page
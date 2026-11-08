[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#main-content)

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
    

matplotlib.axes.Axes.get\_tightbbox[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib-axes-axes-get-tightbbox "Link to this heading")

====================================================================================================================================================================================

Axes.get\_tightbbox(_renderer\=None_, _\*_, _call\_axes\_locator\=True_, _bbox\_extra\_artists\=None_, _for\_layout\_only\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L4706-L4792)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib.axes.Axes.get_tightbbox "Link to this definition")

Return the tight bounding box of the Axes, including axis and their decorators (xlabel, title, etc).

Artists that have `artist.set_in_layout(False)` are not included in the bbox.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass

renderer that will be used to draw the figures (i.e. `fig.canvas.get_renderer()`)

**bbox\_extra\_artists**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or `None`

List of artists to include in the tight bounding box. If `None` (default), then all artist children of the Axes are included in the tight bounding box.

**call\_axes\_locator**bool, default: True

If _call\_axes\_locator_ is `False`, it does not call the `_axes_locator` attribute, which is necessary to get the correct bounding box. `call_axes_locator=False` can be used if the caller is only interested in the relative size of the tightbbox compared to the Axes bbox.

**for\_layout\_only**default: False

The bounding box will _not_ include the x-extent of the title and the xlabel, or the y-extent of the ylabel.

Returns:

[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

Bounding box in figure pixel coordinates.

See also

[`matplotlib.axes.Axes.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_window_extent.html#matplotlib.axes.Axes.get_window_extent "matplotlib.axes.Axes.get_window_extent")

[`matplotlib.axis.Axis.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tightbbox.html#matplotlib.axis.Axis.get_tightbbox "matplotlib.axis.Axis.get_tightbbox")

[`matplotlib.spines.Spine.get_window_extent`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.get_window_extent "matplotlib.spines.Spine.get_window_extent")

On this page
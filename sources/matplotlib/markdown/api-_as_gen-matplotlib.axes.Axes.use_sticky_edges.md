[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html#main-content)

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
    

matplotlib.axes.Axes.use\_sticky\_edges[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html#matplotlib-axes-axes-use-sticky-edges "Link to this heading")

==============================================================================================================================================================================================

property Axes.use\_sticky\_edges[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html#matplotlib.axes.Axes.use_sticky_edges "Link to this definition")

When autoscaling, whether to obey all [`Artist.sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib.artist.Artist.sticky_edges "matplotlib.artist.Artist.sticky_edges")
.

Default is `True`.

Setting this to `False` ensures that the specified margins will be applied, even if the plot includes an image, for example, which would otherwise force a view limit to coincide with its data limit.

The changing this property does not change the plot until [`autoscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
 or [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
 is called.

On this page
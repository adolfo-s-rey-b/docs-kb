[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clim.html#main-content)

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
    

matplotlib.pyplot.clim[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clim.html#matplotlib-pyplot-clim "Link to this heading")

===============================================================================================================================================

matplotlib.pyplot.clim(_vmin\=None_, _vmax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2686-L2704)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clim.html#matplotlib.pyplot.clim "Link to this definition")

Set the color limits of the current image.

If either _vmin_ or _vmax_ is None, the image min/max respectively will be used for color scaling.

If you want to set the clim of multiple images, use [`set_clim`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_clim "matplotlib.cm.ScalarMappable.set_clim")
 on every image, for example:

for im in gca().get\_images():
    im.set\_clim(0, 0.5)

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gci.html#main-content)

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
    

matplotlib.pyplot.gci[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gci.html#matplotlib-pyplot-gci "Link to this heading")

============================================================================================================================================

matplotlib.pyplot.gci()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2937-L2939)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gci.html#matplotlib.pyplot.gci "Link to this definition")

Get the current colorable artist.

Specifically, returns the current [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 instance (`Image` created by [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
 or [`figimage`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figimage.html#matplotlib.pyplot.figimage "matplotlib.pyplot.figimage")
, [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 created by [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolor.html#matplotlib.pyplot.pcolor "matplotlib.pyplot.pcolor")
 or [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
, etc.), or _None_ if no such instance has been defined.

The current image is an attribute of the current Axes, or the nearest earlier Axes in the current figure that contains an image.

Notes

Historically, the only colorable artists were images; hence the name `gci` (get current image).

On this page
[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.disconnect.html#main-content)

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
    

matplotlib.pyplot.disconnect[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.disconnect.html#matplotlib-pyplot-disconnect "Link to this heading")

=================================================================================================================================================================

matplotlib.pyplot.disconnect(_cid_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L1263-L1265)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.disconnect.html#matplotlib.pyplot.disconnect "Link to this definition")

Disconnect the callback with id _cid_.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`FigureCanvasBase.mpl_disconnect`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_disconnect "matplotlib.backend_bases.FigureCanvasBase.mpl_disconnect")
.

Examples

cid \= canvas.mpl\_connect('button\_press\_event', on\_press)
\# ... later
canvas.mpl\_disconnect(cid)

Examples using `matplotlib.pyplot.disconnect`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.disconnect.html#examples-using-matplotlib-pyplot-disconnect "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_coords_demo_thumb.png)

[Mouse move and click events](https://matplotlib.org/stable/gallery/event_handling/coords_demo.html)

Mouse move and click events

On this page
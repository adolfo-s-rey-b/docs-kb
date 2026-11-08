[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#main-content)

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
    

matplotlib.figure.Figure.show[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib-figure-figure-show "Link to this heading")

====================================================================================================================================================================

Figure.show(_warn\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2769-L2811)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "Link to this definition")

If using a GUI backend with pyplot, display the figure window.

If the figure was not created using [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
, it will lack a [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")
, and this method will raise an AttributeError.

Warning

This does not manage a GUI event loop. Consequently, the figure may only be shown briefly or not shown at all if you or your environment are not managing an event loop.

Use cases for [`Figure.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "matplotlib.figure.Figure.show")
 include running this from a GUI application (where there is persistently an event loop running) or from a shell, like IPython, that install an input hook to allow the interactive shell to accept input while the figure is also being shown and interactive. Some, but not all, GUI toolkits will register an input hook on import. See [Command prompt integration](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#cp-integration)
 for more details.

If you're in a shell without input hook integration or executing a python script, you should use [`matplotlib.pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
 with `block=True` instead, which takes care of starting and running the event loop for you.

Parameters:

**warn**bool, default: True

If `True` and we are not running headless (i.e. on Linux with an unset DISPLAY), issue warning when called on a non-GUI backend.

Examples using `matplotlib.figure.Figure.show`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#examples-using-matplotlib-figure-figure-show "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_simple_thumb.png)

[Polygon Selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html)

Polygon Selector

On this page